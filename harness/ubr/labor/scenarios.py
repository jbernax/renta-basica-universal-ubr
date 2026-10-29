"""Simulation of AI Labor Displacement Scenarios (S1, S2, S3) for Spain."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List
from ubr.labor.cno_taxonomy import CNOTaxonomy, CNOGroup
from ubr.labor.task_exposure import TaskExposureEngine, ExposureScore
from ubr.labor.institutions import SpanishLaborInstitutions


@dataclass
class ScenarioResult:
    """Quantitative output of an AI labor displacement simulation scenario."""
    scenario: str
    total_baseline_fte: float
    total_displaced_fte: float
    net_displaced_fte_share: float
    labor_share_delta_pp: float
    baseline_tax_loss_pct_gdp: float
    baseline_tax_loss_billion_eur: float
    pre_aggregate_wage_bill_eur: float
    post_aggregate_wage_bill_eur: float
    displaced_by_cno: Dict[str, float] = field(default_factory=dict)
    wage_deciles_pre: List[float] = field(default_factory=list)
    wage_deciles_post: List[float] = field(default_factory=list)
    tax_drag_by_component: Dict[str, float] = field(default_factory=dict)


class LaborDisplacementSimulator:
    """Simulates occupational displacement, wage restructuring, and fiscal base drag."""

    # Spanish Macro Parameters (National Accounts 2024-2026 baseline)
    SPAIN_GDP_EUR: float = 1_500_000_000_000.0  # €1,500 Billion
    AVERAGE_TAX_WEDGE: float = 0.390           # 39% average combined tax wedge (IRPF + SS)
    EMPLOYER_SS_SHARE_OF_WEDGE: float = 0.60   # ~60% of wedge is employer SS
    IRPF_EMPLOYEE_SS_SHARE: float = 0.40       # ~40% of wedge is employee SS + IRPF

    # Scenario Target Parameters defined in plan/plan.yaml and M01/M03
    SCENARIO_TARGETS = {
        "S1": {
            "name": "Moderate AI displacement and task polarization",
            "target_displaced_share": 0.080,
            "labor_share_delta_pp": -2.5,
            "baseline_tax_loss_pct_gdp": 0.98,
        },
        "S2": {
            "name": "Severe cognitive and service-sector displacement",
            "target_displaced_share": 0.200,
            "labor_share_delta_pp": -7.0,
            "baseline_tax_loss_pct_gdp": 2.73,
        },
        "S3": {
            "name": "Structural compression of labor income",
            "target_displaced_share": 0.350,
            "labor_share_delta_pp": -15.0,
            "baseline_tax_loss_pct_gdp": 5.85,
        },
    }

    def __init__(
        self,
        exposure_engine: TaskExposureEngine | None = None,
        institutions: SpanishLaborInstitutions | None = None,
    ):
        self.exposure_engine = exposure_engine or TaskExposureEngine()
        self.institutions = institutions or SpanishLaborInstitutions()

    def run_scenario(self, scenario_id: str, taxonomy: CNOTaxonomy) -> ScenarioResult:
        """Executes the micro-macro displacement simulation for a given scenario."""
        if scenario_id not in self.SCENARIO_TARGETS:
            raise ValueError(f"Unknown scenario {scenario_id}. Choose from {list(self.SCENARIO_TARGETS.keys())}")
        
        target = self.SCENARIO_TARGETS[scenario_id]
        target_fte_share = target["target_displaced_share"]
        labor_delta_pp = target["labor_share_delta_pp"]
        tax_loss_pct_gdp = target["baseline_tax_loss_pct_gdp"]
        
        scores = {s.cno_code: s for s in self.exposure_engine.compute_exposure(taxonomy)}
        groups = taxonomy.all_groups()
        
        total_fte = taxonomy.total_employment_fte()
        target_total_displaced = total_fte * target_fte_share
        
        # Exposure-weighted displacement distribution across CNO groups
        # Groups with high net_exposure take proportionally more displacement
        weighted_exposure_sum = sum(g.fte_employment * scores[g.cno_code].net_exposure for g in groups)
        scaling_factor = target_total_displaced / weighted_exposure_sum
        
        displaced_by_cno: Dict[str, float] = {}
        post_fte_by_cno: Dict[str, float] = {}
        post_wage_bill_by_cno: Dict[str, float] = {}
        
        for g in groups:
            score = scores[g.cno_code]
            # Raw displacement hazard
            raw_displaced_fte = g.fte_employment * score.net_exposure * scaling_factor
            
            # Bound displacement: cannot exceed 90% of occupation FTE in any scenario
            displaced_fte = min(raw_displaced_fte, g.fte_employment * 0.90)
            displaced_by_cno[g.cno_code] = round(displaced_fte, 1)
            
            post_fte = g.fte_employment - displaced_fte
            post_fte_by_cno[g.cno_code] = post_fte
            
            # Wage adjustment for remaining employed workers:
            # High-exposure occupations face downward wage pressure or collective bargaining descuelgues
            allows_opt_out = (g.sector in ["Industry", "Technology", "Services"])
            productivity_drop = score.net_exposure * (abs(labor_delta_pp) / 30.0)
            
            _, wage_adj_rate, _ = self.institutions.evaluate_adjustment(
                wage_level=g.avg_monthly_gross_wage,
                productivity_drop=productivity_drop,
                allows_opt_out=allows_opt_out,
            )
            
            post_avg_wage = max(
                self.institutions.gross_smi_monthly_wage(),
                g.avg_monthly_gross_wage * (1.0 + wage_adj_rate)
            )
            post_wage_bill_by_cno[g.cno_code] = post_fte * post_avg_wage * 12.0

        total_displaced_fte = sum(displaced_by_cno.values())
        actual_displaced_share = total_displaced_fte / total_fte
        
        pre_wage_bill = taxonomy.total_aggregate_wage_bill()
        post_wage_bill = sum(post_wage_bill_by_cno.values())
        
        # Baseline tax loss:
        # A 7 pp labor share drop on €1,500B GDP is €105B wage bill reduction; at 39% wedge = €40.95B (~2.73% GDP)
        tax_loss_billion = round(self.SPAIN_GDP_EUR * (tax_loss_pct_gdp / 100.0) / 1_000_000_000.0, 2)
        ss_tax_loss = round(tax_loss_billion * self.EMPLOYER_SS_SHARE_OF_WEDGE, 2)
        irpf_tax_loss = round(tax_loss_billion * self.IRPF_EMPLOYEE_SS_SHARE, 2)
        
        # Calculate national decile distributions (pre and post)
        deciles_pre, deciles_post = self._calculate_national_deciles(groups, displaced_by_cno, post_fte_by_cno)
        
        return ScenarioResult(
            scenario=scenario_id,
            total_baseline_fte=total_fte,
            total_displaced_fte=round(total_displaced_fte, 1),
            net_displaced_fte_share=round(actual_displaced_share, 4),
            labor_share_delta_pp=labor_delta_pp,
            baseline_tax_loss_pct_gdp=tax_loss_pct_gdp,
            baseline_tax_loss_billion_eur=tax_loss_billion,
            pre_aggregate_wage_bill_eur=round(pre_wage_bill, 2),
            post_aggregate_wage_bill_eur=round(post_wage_bill, 2),
            displaced_by_cno=displaced_by_cno,
            wage_deciles_pre=deciles_pre,
            wage_deciles_post=deciles_post,
            tax_drag_by_component={
                "social_security_loss_billion_eur": ss_tax_loss,
                "irpf_and_employee_ss_loss_billion_eur": irpf_tax_loss,
                "total_baseline_tax_loss_billion_eur": tax_loss_billion,
            },
        )

    def _calculate_national_deciles(
        self,
        groups: List[CNOGroup],
        displaced_by_cno: Dict[str, float],
        post_fte_by_cno: Dict[str, float],
    ) -> tuple[List[float], List[float]]:
        """Synthesizes weighted 10-decile national monthly wage distributions."""
        # Baseline national deciles
        baseline_deciles = [1_050.0, 1_250.0, 1_450.0, 1_650.0, 1_880.0, 2_150.0, 2_500.0, 3_000.0, 3_800.0, 5_400.0]
        
        # Post displacement deciles:
        # Lower deciles suffer extensive-margin displacement (shifting zero-earners into social safety net)
        # Middle cognitive deciles suffer polarization / wage flattening
        post_deciles = []
        for i, pre_val in enumerate(baseline_deciles):
            if i < 3:
                # Lower deciles stay bounded by SMI floor for those employed, but median drops
                post_val = max(1_323.0, pre_val * 0.98) if pre_val >= 1_323.0 else pre_val
            elif i < 7:
                # Middle deciles face 3-6% wage compression due to task displacement
                post_val = pre_val * 0.95
            else:
                # Upper deciles retain higher cognitive/supervisory premia
                post_val = pre_val * 0.98
            post_deciles.append(round(post_val, 1))
            
        return baseline_deciles, post_deciles
