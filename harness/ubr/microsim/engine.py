"""Comprehensive EUROMOD-Spain / Python Microsimulation Engine (Track 2).

Orchestrates population microdata, UBR benefit parameters (M02), welfare integration (M07),
progressive IRPF restructuring (M03), housing rent-capture (M05/M09), and poverty/inequality metrics.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any, Sequence

from ubr.microsim.benefits import (
    BenefitCalculator,
    HouseholdBenefitResult,
    TIER_SPECS,
    UBRTier,
)
from ubr.microsim.housing import (
    HousingAggregateMetrics,
    HousingCalculator,
    HouseholdHousingResult,
)
from ubr.microsim.poverty_metrics import (
    DistributionalSummary,
    FGTResult,
    compute_atkinson,
    compute_fgt,
    compute_gini,
    compute_s80_s20,
    compute_theil,
    compute_weighted_median,
)
from ubr.microsim.population import (
    DisabilityGrade,
    MicroHousehold,
    PopulationDataset,
    generate_calibrated_spanish_population,
)
from ubr.microsim.taxation import (
    FiscalBridgeBreakdown,
    IndividualTaxResult,
    TaxCalculator,
)


@dataclass
class DecileDistributionRow:
    decile: int
    mean_baseline_gross_income_eur: float
    mean_baseline_disposable_income_eur: float
    mean_post_disposable_income_eur: float
    delta_disposable_income_eur: float
    delta_disposable_income_pct: float
    net_winner_share_pct: float
    net_loser_share_pct: float


@dataclass
class SimulationRunResult:
    scenario: str
    tier: str
    rent_stabilizers_active: bool
    no_loser_guarantee_active: bool
    behavioral_eti_active: bool

    # Aggregates (National Scaled, Euros)
    total_population: float
    total_adults: float
    total_minors: float
    total_households: float
    gross_ubr_outlays_eur: float
    total_absorbed_welfare_eur: float
    dual_pillar_pension_savings_eur: float
    net_irpf_collections_eur: float
    no_loser_guarantee_cost_eur: float

    # Fiscal Bridge
    fiscal_bridge: FiscalBridgeBreakdown

    # Baseline Distribution & Poverty
    baseline_distribution: DistributionalSummary

    # Post-Reform Distribution & Poverty
    post_distribution: DistributionalSummary

    # Housing Metrics
    housing_metrics: HousingAggregateMetrics

    # Decile Winner / Loser Profile
    decile_rows: list[DecileDistributionRow]


class MicrosimulationEngine:
    """End-to-end EUROMOD-Spain / Python microsimulation engine."""

    def __init__(
        self,
        population: PopulationDataset | None = None,
        spain_gdp_eur: float = 1_500_000_000_000.0,
    ):
        self.population = population or generate_calibrated_spanish_population(3000)
        self.spain_gdp_eur = spain_gdp_eur

    def run_simulation(
        self,
        tier: UBRTier = UBRTier.TIER_B,
        scenario: str = "S2",
        enable_rent_stabilizers: bool = True,
        enable_no_loser_guarantee: bool = True,
        enable_behavioral_eti: bool = True,
        counterfactual_filepath: str | Path | None = None,
    ) -> SimulationRunResult:
        """Run a full counterfactual microsimulation."""
        # Load counterfactual labor data if provided or if standard file exists
        counterfactual_data: dict[str, Any] | None = None
        if counterfactual_filepath:
            path = Path(counterfactual_filepath)
            if path.exists():
                with open(path, "r", encoding="utf-8") as f:
                    counterfactual_data = json.load(f)
        else:
            default_path = Path("data") / f"counterfactual_{scenario.lower()}.json"
            if default_path.exists():
                with open(default_path, "r", encoding="utf-8") as f:
                    counterfactual_data = json.load(f)

        # Apply counterfactual wage shocks if available
        if counterfactual_data:
            self.population.apply_labor_counterfactual(counterfactual_data)

        # Initialize domain calculators
        benefit_calc = BenefitCalculator(tier=tier)
        tax_calc = TaxCalculator(
            eti=0.25,
            enable_behavioral_eti=enable_behavioral_eti,
            spain_gdp_eur=self.spain_gdp_eur,
        )
        housing_calc = HousingCalculator(enable_rent_stabilizers=enable_rent_stabilizers)

        scaling = self.population.scaling_factor

        # 1. Baseline Computation across all households
        baseline_hh_disp_incomes: list[float] = []
        baseline_hh_eq_bhc: list[float] = []
        baseline_hh_eq_ahc: list[float] = []
        hh_weights: list[float] = []

        # Individual level arrays
        ind_baseline_eq_bhc: list[float] = []
        ind_baseline_eq_ahc: list[float] = []
        ind_baseline_raw: list[float] = []
        ind_weights: list[float] = []
        ind_is_minor: list[bool] = []
        ind_disab_costs: list[float] = []

        total_baseline_irpf = 0.0

        for hh in self.population.households:
            hh_market_gross = 0.0
            hh_baseline_tax = 0.0
            hh_non_contrib = hh.baseline_imv_received

            for ind in hh.members:
                t_irpf, t_ss = tax_calc.compute_baseline_tax(ind)
                hh_baseline_tax += t_irpf + t_ss
                hh_market_gross += ind.labor_earnings_gross + ind.contributory_pension_gross + ind.capital_income_gross
                hh_non_contrib += ind.baseline_non_contributory_cash
                total_baseline_irpf += t_irpf * hh.weight * scaling

            # Baseline Household Disposable Income
            base_disp = max(0.0, hh_market_gross + hh_non_contrib - hh_baseline_tax)
            baseline_hh_disp_incomes.append(base_disp)
            hh_weights.append(hh.weight)

            eq_bhc = base_disp / hh.modified_oecd_scale
            eq_ahc = max(0.0, base_disp - hh.baseline_housing_cost_annual) / hh.modified_oecd_scale
            baseline_hh_eq_bhc.append(eq_bhc)
            baseline_hh_eq_ahc.append(eq_ahc)

            for ind in hh.members:
                ind_baseline_eq_bhc.append(eq_bhc)
                ind_baseline_eq_ahc.append(eq_ahc)
                ind_weights.append(hh.weight)
                ind_is_minor.append(not ind.is_adult)
                
                # Raw individualized income before pooling (Ponthieux 2013)
                raw_ind = ind.labor_earnings_gross + ind.contributory_pension_gross + ind.baseline_non_contributory_cash
                ind_baseline_raw.append(raw_ind)

                # Disability living cost extra burden (Zaidi & Burchardt 2005)
                extra_cost = 0.0
                if ind.disability_grade == DisabilityGrade.GRADE_1:
                    extra_cost = 3500.0
                elif ind.disability_grade == DisabilityGrade.GRADE_2:
                    extra_cost = 6000.0
                elif ind.disability_grade == DisabilityGrade.GRADE_3:
                    extra_cost = 10000.0
                ind_disab_costs.append(extra_cost)

        # Baseline Distributional Metrics
        med_base_bhc = compute_weighted_median(ind_baseline_eq_bhc, ind_weights)
        med_base_ahc = compute_weighted_median(ind_baseline_eq_ahc, ind_weights)
        z60_base_bhc = 0.60 * med_base_bhc
        z40_base_bhc = 0.40 * med_base_bhc
        z60_base_ahc = 0.60 * med_base_ahc
        z40_base_ahc = 0.40 * med_base_ahc

        fgt_base_bhc_60 = compute_fgt(ind_baseline_eq_bhc, ind_weights, z60_base_bhc)
        fgt_base_bhc_40 = compute_fgt(ind_baseline_eq_bhc, ind_weights, z40_base_bhc)
        fgt_base_ahc_60 = compute_fgt(ind_baseline_eq_ahc, ind_weights, z60_base_ahc)
        fgt_base_ahc_40 = compute_fgt(ind_baseline_eq_ahc, ind_weights, z40_base_ahc)

        # Baseline child poverty
        minor_weights = [w for w, is_m in zip(ind_weights, ind_is_minor) if is_m]
        minor_bhc_eq = [eq for eq, is_m in zip(ind_baseline_eq_bhc, ind_is_minor) if is_m]
        minor_ahc_eq = [eq for eq, is_m in zip(ind_baseline_eq_ahc, ind_is_minor) if is_m]
        base_child_bhc_rate = compute_fgt(minor_bhc_eq, minor_weights, z60_base_bhc).p0_headcount_ratio
        base_child_ahc_rate = compute_fgt(minor_ahc_eq, minor_weights, z60_base_ahc).p0_headcount_ratio

        # Baseline inequality
        base_gini = compute_gini(ind_baseline_eq_bhc, ind_weights)
        base_s80_s20 = compute_s80_s20(ind_baseline_eq_bhc, ind_weights)
        base_theil = compute_theil(ind_baseline_eq_bhc, ind_weights)
        base_atkinson = compute_atkinson(ind_baseline_eq_bhc, ind_weights)

        # Baseline individualized poverty & impairment adjusted
        base_indiv_fgt = compute_fgt(ind_baseline_raw, ind_weights, z60_base_bhc)
        impair_base_eq = [max(0.0, eq - cost) for eq, cost in zip(ind_baseline_eq_bhc, ind_disab_costs)]
        base_impair_fgt = compute_fgt(impair_base_eq, ind_weights, z60_base_bhc)

        baseline_dist = DistributionalSummary(
            median_equivalized_income_bhc=med_base_bhc,
            median_equivalized_income_ahc=med_base_ahc,
            poverty_threshold_60_bhc=z60_base_bhc,
            poverty_threshold_40_bhc=z40_base_bhc,
            poverty_threshold_60_ahc=z60_base_ahc,
            poverty_threshold_40_ahc=z40_base_ahc,
            bhc_floating_60=fgt_base_bhc_60,
            bhc_anchored_60=fgt_base_bhc_60,
            bhc_severe_40=fgt_base_bhc_40,
            bhc_child_poverty_rate=base_child_bhc_rate,
            ahc_floating_60=fgt_base_ahc_60,
            ahc_anchored_60=fgt_base_ahc_60,
            ahc_severe_40=fgt_base_ahc_40,
            ahc_child_poverty_rate=base_child_ahc_rate,
            gini_coefficient=base_gini,
            s80_s20_ratio=base_s80_s20,
            theil_index=base_theil,
            atkinson_index_e1=base_atkinson,
            individualized_poverty_rate=base_indiv_fgt.p0_headcount_ratio,
            impairment_adjusted_poverty_rate=base_impair_fgt.p0_headcount_ratio,
        )

        # 2. Post-Reform Simulation
        total_gross_ubr = 0.0
        total_absorbed_welfare = 0.0
        total_dual_pillar_savings = 0.0
        total_reform_irpf = 0.0
        total_no_loser_cost = 0.0

        post_hh_disp_incomes: list[float] = []
        post_hh_eq_bhc: list[float] = []
        post_hh_eq_ahc: list[float] = []

        ind_post_eq_bhc: list[float] = []
        ind_post_eq_ahc: list[float] = []
        ind_post_raw: list[float] = []

        housing_results: list[HouseholdHousingResult] = []

        for idx, hh in enumerate(self.population.households):
            hh_benefit = benefit_calc.calculate_household_benefits(hh)
            total_gross_ubr += hh_benefit.total_household_ubr_annual * hh.weight * scaling
            total_absorbed_welfare += hh_benefit.total_absorbed_welfare_annual * hh.weight * scaling

            hh_market_income = 0.0
            hh_reform_tax = 0.0

            for ind, disb in zip(hh.members, hh_benefit.member_disbursements):
                tax_res = tax_calc.calculate_individual_tax(ind, disb.retained_contributory_pension)
                
                # Contributory Pension Neutrality Shield (M07):
                # Ensure retained contributory pension is not taxed above baseline liability
                ind_tax = tax_res.total_reform_tax
                if ind.contributory_pension_gross > 0 and ind.labor_earnings_gross == 0:
                    base_ind_tax, _ = tax_calc.compute_baseline_tax(ind)
                    ind_tax = min(ind_tax, base_ind_tax)

                hh_reform_tax += ind_tax
                total_reform_irpf += tax_res.reform_irpf * hh.weight * scaling

                # Dual-Pillar savings to Social Security: base UBR portion offset against pension
                if ind.contributory_pension_gross > 0.0:
                    savings = min(ind.contributory_pension_gross, disb.base_ubr_annual)
                    total_dual_pillar_savings += savings * hh.weight * scaling

                hh_market_income += (
                    ind.labor_earnings_gross
                    + disb.retained_contributory_pension
                    + ind.capital_income_gross
                )

            # Unadjusted post-reform disposable income
            raw_post_disp = (
                hh_market_income
                + hh_benefit.total_household_ubr_annual
                + hh_benefit.regional_top_up_annual
                - hh_reform_tax
            )

            # Statutory No-Loser Guarantee (Complemento de Neutralidad Fiscal, M07)
            # Guarantees zero disposable income loss for vulnerable cohorts, single parents,
            # disabled persons, and deciles 1-7 below the breakeven threshold
            base_disp = baseline_hh_disp_incomes[idx]
            no_loser_topup = 0.0
            is_protected_cohort = (
                (hh_market_income / max(1, hh.num_adults)) < 42000.0
                or any(m.disability_grade != DisabilityGrade.NONE for m in hh.members)
                or any(m.contributory_pension_gross > 0 for m in hh.members)
                or hh.is_single_parent
            )
            if enable_no_loser_guarantee and is_protected_cohort and raw_post_disp < base_disp:
                no_loser_topup = base_disp - raw_post_disp
                total_no_loser_cost += no_loser_topup * hh.weight * scaling

            final_post_disp = raw_post_disp + no_loser_topup
            post_hh_disp_incomes.append(final_post_disp)

            # Housing evaluation
            housing_res = housing_calc.evaluate_household_housing(
                hh=hh,
                gross_ubr_received=hh_benefit.total_household_ubr_annual,
                baseline_disposable_income=base_disp,
                post_disposable_income=final_post_disp,
            )
            housing_results.append(housing_res)

            eq_bhc = final_post_disp / hh.modified_oecd_scale
            eq_ahc = max(0.0, final_post_disp - housing_res.post_reform_housing_cost) / hh.modified_oecd_scale
            post_hh_eq_bhc.append(eq_bhc)
            post_hh_eq_ahc.append(eq_ahc)

            for ind, disb in zip(hh.members, hh_benefit.member_disbursements):
                ind_post_eq_bhc.append(eq_bhc)
                ind_post_eq_ahc.append(eq_ahc)
                # Raw individualized income after UBR (Ponthieux 2013)
                raw_post_ind = (
                    ind.labor_earnings_gross
                    + disb.retained_contributory_pension
                    + disb.total_cash_ubr_annual
                )
                ind_post_raw.append(raw_post_ind)

        # Post-Reform Distributional Metrics
        med_post_bhc = compute_weighted_median(ind_post_eq_bhc, ind_weights)
        med_post_ahc = compute_weighted_median(ind_post_eq_ahc, ind_weights)
        z60_post_bhc = 0.60 * med_post_bhc
        z40_post_bhc = 0.40 * med_post_bhc
        z60_post_ahc = 0.60 * med_post_ahc
        z40_post_ahc = 0.40 * med_post_ahc

        fgt_post_bhc_floating_60 = compute_fgt(ind_post_eq_bhc, ind_weights, z60_post_bhc)
        fgt_post_bhc_anchored_60 = compute_fgt(ind_post_eq_bhc, ind_weights, z60_base_bhc)  # Anchored at baseline z60
        fgt_post_bhc_severe_40 = compute_fgt(ind_post_eq_bhc, ind_weights, z40_post_bhc)

        fgt_post_ahc_floating_60 = compute_fgt(ind_post_eq_ahc, ind_weights, z60_post_ahc)
        fgt_post_ahc_anchored_60 = compute_fgt(ind_post_eq_ahc, ind_weights, z60_base_ahc)  # Anchored at baseline z60
        fgt_post_ahc_severe_40 = compute_fgt(ind_post_eq_ahc, ind_weights, z40_post_ahc)

        # Child poverty post-reform
        minor_post_bhc_eq = [eq for eq, is_m in zip(ind_post_eq_bhc, ind_is_minor) if is_m]
        minor_post_ahc_eq = [eq for eq, is_m in zip(ind_post_eq_ahc, ind_is_minor) if is_m]
        post_child_bhc_rate = compute_fgt(minor_post_bhc_eq, minor_weights, z60_post_bhc).p0_headcount_ratio
        post_child_ahc_rate = compute_fgt(minor_post_ahc_eq, minor_weights, z60_post_ahc).p0_headcount_ratio

        # Post-reform inequality
        post_gini = compute_gini(ind_post_eq_bhc, ind_weights)
        post_s80_s20 = compute_s80_s20(ind_post_eq_bhc, ind_weights)
        post_theil = compute_theil(ind_post_eq_bhc, ind_weights)
        post_atkinson = compute_atkinson(ind_post_eq_bhc, ind_weights)

        # Post individualized poverty & impairment adjusted
        post_indiv_fgt = compute_fgt(ind_post_raw, ind_weights, z60_post_bhc)
        impair_post_eq = [max(0.0, eq - cost) for eq, cost in zip(ind_post_eq_bhc, ind_disab_costs)]
        post_impair_fgt = compute_fgt(impair_post_eq, ind_weights, z60_post_bhc)

        post_dist = DistributionalSummary(
            median_equivalized_income_bhc=med_post_bhc,
            median_equivalized_income_ahc=med_post_ahc,
            poverty_threshold_60_bhc=z60_post_bhc,
            poverty_threshold_40_bhc=z40_post_bhc,
            poverty_threshold_60_ahc=z60_post_ahc,
            poverty_threshold_40_ahc=z40_post_ahc,
            bhc_floating_60=fgt_post_bhc_floating_60,
            bhc_anchored_60=fgt_post_bhc_anchored_60,
            bhc_severe_40=fgt_post_bhc_severe_40,
            bhc_child_poverty_rate=post_child_bhc_rate,
            ahc_floating_60=fgt_post_ahc_floating_60,
            ahc_anchored_60=fgt_post_ahc_anchored_60,
            ahc_severe_40=fgt_post_ahc_severe_40,
            ahc_child_poverty_rate=post_child_ahc_rate,
            gini_coefficient=post_gini,
            s80_s20_ratio=post_s80_s20,
            theil_index=post_theil,
            atkinson_index_e1=post_atkinson,
            individualized_poverty_rate=post_indiv_fgt.p0_headcount_ratio,
            impairment_adjusted_poverty_rate=post_impair_fgt.p0_headcount_ratio,
        )

        # 3. Aggregate Housing Metrics
        housing_metrics = housing_calc.compute_aggregate_housing_metrics(
            housing_results=housing_results,
            baseline_disposable_incomes=baseline_hh_disp_incomes,
            weights=hh_weights,
            scaling_factor=scaling,
        )

        # 4. Decile Winner / Loser Profile (sorted by baseline equivalized income)
        sorted_indices = sorted(range(len(baseline_hh_eq_bhc)), key=lambda i: baseline_hh_eq_bhc[i])
        n_hh = len(sorted_indices)
        decile_rows: list[DecileDistributionRow] = []

        for d in range(10):
            start_idx = int(d * n_hh / 10)
            end_idx = int((d + 1) * n_hh / 10) if d < 9 else n_hh
            d_indices = sorted_indices[start_idx:end_idx]

            d_base_disp = [baseline_hh_disp_incomes[i] for i in d_indices]
            d_post_disp = [post_hh_disp_incomes[i] for i in d_indices]
            d_w = [hh_weights[i] for i in d_indices]
            tot_dw = sum(d_w)

            mean_base = sum(b * w for b, w in zip(d_base_disp, d_w)) / tot_dw
            mean_post = sum(p * w for p, w in zip(d_post_disp, d_w)) / tot_dw
            delta_eur = mean_post - mean_base
            delta_pct = (delta_eur / mean_base * 100.0) if mean_base > 0 else 0.0

            winner_w = sum(w for b, p, w in zip(d_base_disp, d_post_disp, d_w) if p > b + 1.0)
            loser_w = sum(w for b, p, w in zip(d_base_disp, d_post_disp, d_w) if p < b - 1.0)

            decile_rows.append(
                DecileDistributionRow(
                    decile=d + 1,
                    mean_baseline_gross_income_eur=mean_base * 1.15,  # approximate gross
                    mean_baseline_disposable_income_eur=mean_base,
                    mean_post_disposable_income_eur=mean_post,
                    delta_disposable_income_eur=delta_eur,
                    delta_disposable_income_pct=delta_pct,
                    net_winner_share_pct=(winner_w / tot_dw) * 100.0,
                    net_loser_share_pct=(loser_w / tot_dw) * 100.0,
                )
            )

        # Compute incremental IRPF collections over baseline public services
        delta_irpf = max(0.0, total_reform_irpf - total_baseline_irpf)

        # 5. Consolidated Fiscal Bridge
        fiscal_bridge = tax_calc.build_consolidated_fiscal_bridge(
            tier=tier,
            scenario=scenario,
            gross_ubr_outlays=total_gross_ubr,
            delta_irpf_collections=delta_irpf,
            dual_pillar_pension_savings=total_dual_pillar_savings,
            abolished_non_contributory_welfare=total_absorbed_welfare,
            no_loser_guarantee_cost=total_no_loser_cost,
            counterfactual_data=counterfactual_data,
        )

        return SimulationRunResult(
            scenario=scenario,
            tier=tier.value,
            rent_stabilizers_active=enable_rent_stabilizers,
            no_loser_guarantee_active=enable_no_loser_guarantee,
            behavioral_eti_active=enable_behavioral_eti,
            total_population=self.population.total_individuals(),
            total_adults=self.population.total_adults(),
            total_minors=self.population.total_minors(),
            total_households=self.population.total_households(),
            gross_ubr_outlays_eur=total_gross_ubr,
            total_absorbed_welfare_eur=total_absorbed_welfare,
            dual_pillar_pension_savings_eur=total_dual_pillar_savings,
            net_irpf_collections_eur=total_reform_irpf,
            no_loser_guarantee_cost_eur=total_no_loser_cost,
            fiscal_bridge=fiscal_bridge,
            baseline_distribution=baseline_dist,
            post_distribution=post_dist,
            housing_metrics=housing_metrics,
            decile_rows=decile_rows,
        )
