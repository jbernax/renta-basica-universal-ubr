"""Intergovernmental Fiscal Equalization and CPFF Balancing Engine.

Simulates fiscal flows across Spain's 15 Common Regime Autonomous Communities (Ley 22/2009)
and 2 Foral Regimes (Concierto Vasco Ley 12/2002 and Convenio de Navarra Ley 28/1990)
under AI displacement scenarios S1, S2, and S3 (Track 5: M06, M13).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class RegionalEqualizationRecord:
    """Fiscal equalization balance for an individual Autonomous Community."""

    code: str
    name: str
    is_foral: bool
    population: int
    gross_irpf_base_eur_b: float
    regional_irpf_share_eur_b: float
    ubr_gross_transfers_eur_b: float
    ubr_clawback_and_corporate_eur_b: float
    pre_equalization_balance_eur_b: float
    cpff_equalization_transfer_eur_b: float
    post_equalization_balance_eur_b: float
    equalized_balance_per_capita_eur: float

    def to_dict(self) -> Dict[str, Any]:
        return {
            "code": self.code,
            "name": self.name,
            "is_foral": self.is_foral,
            "population": self.population,
            "gross_irpf_base_eur_b": round(self.gross_irpf_base_eur_b, 3),
            "regional_irpf_share_eur_b": round(self.regional_irpf_share_eur_b, 3),
            "ubr_gross_transfers_eur_b": round(self.ubr_gross_transfers_eur_b, 3),
            "ubr_clawback_and_corporate_eur_b": round(self.ubr_clawback_and_corporate_eur_b, 3),
            "pre_equalization_balance_eur_b": round(self.pre_equalization_balance_eur_b, 3),
            "cpff_equalization_transfer_eur_b": round(self.cpff_equalization_transfer_eur_b, 3),
            "post_equalization_balance_eur_b": round(self.post_equalization_balance_eur_b, 3),
            "equalized_balance_per_capita_eur": round(self.equalized_balance_per_capita_eur, 1),
        }


@dataclass
class ForalCupoRecord:
    """Foral Cupo / Aportación adjustment calculations."""

    territory: str
    regime_statute: str
    statutory_index_pct: float
    population: int
    gross_cupo_baseline_eur_b: float
    ubr_disbursements_in_territory_eur_b: float
    non_assumed_burden_deduction_eur_b: float
    net_adjusted_cupo_eur_b: float
    per_capita_fiscal_impact_eur: float

    def to_dict(self) -> Dict[str, Any]:
        return {
            "territory": self.territory,
            "regime_statute": self.regime_statute,
            "statutory_index_pct": self.statutory_index_pct,
            "population": self.population,
            "gross_cupo_baseline_eur_b": round(self.gross_cupo_baseline_eur_b, 3),
            "ubr_disbursements_in_territory_eur_b": round(self.ubr_disbursements_in_territory_eur_b, 3),
            "non_assumed_burden_deduction_eur_b": round(self.non_assumed_burden_deduction_eur_b, 3),
            "net_adjusted_cupo_eur_b": round(self.net_adjusted_cupo_eur_b, 3),
            "per_capita_fiscal_impact_eur": round(self.per_capita_fiscal_impact_eur, 1),
        }


@dataclass
class IntergovernmentalEqualizationReport:
    """Consolidated territorial equalization report."""

    scenario: str
    tier: str
    ubr_monthly_rate_eur: float
    total_population_spain: int
    common_regime_population: int
    foral_population: int
    total_cpff_fund_size_eur_b: float
    common_regime_regions: List[RegionalEqualizationRecord] = field(default_factory=list)
    foral_records: List[ForalCupoRecord] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "scenario": self.scenario,
            "tier": self.tier,
            "ubr_monthly_rate_eur": self.ubr_monthly_rate_eur,
            "total_population_spain": self.total_population_spain,
            "common_regime_population": self.common_regime_population,
            "foral_population": self.foral_population,
            "total_cpff_fund_size_eur_b": round(self.total_cpff_fund_size_eur_b, 3),
            "common_regime_regions": [r.to_dict() for r in self.common_regime_regions],
            "foral_records": [f.to_dict() for f in self.foral_records],
        }


# Calibrated Baseline Regional Demographic & Tax Parameters (INE / AEAT 2024-2026)
REGIONAL_DATA_SPAIN = [
    {"code": "AND", "name": "Andalucía", "pop": 8580000, "irpf_base_share": 0.125, "is_foral": False},
    {"code": "ARA", "name": "Aragón", "pop": 1340000, "irpf_base_share": 0.032, "is_foral": False},
    {"code": "AST", "name": "Principado de Asturias", "pop": 1010000, "irpf_base_share": 0.024, "is_foral": False},
    {"code": "BAL", "name": "Illes Balears", "pop": 1220000, "irpf_base_share": 0.034, "is_foral": False},
    {"code": "CAN", "name": "Canarias", "pop": 2230000, "irpf_base_share": 0.038, "is_foral": False},
    {"code": "CAB", "name": "Cantabria", "pop": 590000, "irpf_base_share": 0.014, "is_foral": False},
    {"code": "CLM", "name": "Castilla-La Mancha", "pop": 2080000, "irpf_base_share": 0.036, "is_foral": False},
    {"code": "CYL", "name": "Castilla y León", "pop": 2380000, "irpf_base_share": 0.052, "is_foral": False},
    {"code": "CAT", "name": "Cataluña", "pop": 7900000, "irpf_base_share": 0.218, "is_foral": False},
    {"code": "EXT", "name": "Extremadura", "pop": 1050000, "irpf_base_share": 0.016, "is_foral": False},
    {"code": "GAL", "name": "Galicia", "pop": 2690000, "irpf_base_share": 0.056, "is_foral": False},
    {"code": "MAD", "name": "Comunidad de Madrid", "pop": 6850000, "irpf_base_share": 0.235, "is_foral": False},
    {"code": "MUR", "name": "Región de Murcia", "pop": 1550000, "irpf_base_share": 0.027, "is_foral": False},
    {"code": "RIO", "name": "La Rioja", "pop": 320000, "irpf_base_share": 0.008, "is_foral": False},
    {"code": "VAL", "name": "Comunitat Valenciana", "pop": 5150000, "irpf_base_share": 0.085, "is_foral": False},
    {"code": "PVA", "name": "País Vasco", "pop": 2210000, "irpf_base_share": 0.065, "is_foral": True},
    {"code": "NAV", "name": "Comunidad Foral de Navarra", "pop": 665000, "irpf_base_share": 0.018, "is_foral": True},
]


def calculate_intergovernmental_equalization(
    scenario: str = "S2",
) -> IntergovernmentalEqualizationReport:
    """Calculates intergovernmental CPFF equalization balances and Foral Cupo adjustments.

    Args:
        scenario: "S1" (Tier A, €600), "S2" (Tier B, €900), or "S3" (Tier C, €1200).
    """
    scenario_cfg = {
        "S1": {"tier": "Tier A", "rate": 600.0, "total_gross_b": 288.0, "clawback_rate": 0.65, "nat_irpf_base_b": 110.0},
        "S2": {"tier": "Tier B", "rate": 900.0, "total_gross_b": 432.0, "clawback_rate": 0.72, "nat_irpf_base_b": 102.0},
        "S3": {"tier": "Tier C", "rate": 1200.0, "total_gross_b": 576.0, "clawback_rate": 0.78, "nat_irpf_base_b": 93.0},
    }
    cfg = scenario_cfg.get(scenario, scenario_cfg["S2"])
    total_pop = sum(r["pop"] for r in REGIONAL_DATA_SPAIN)
    common_pop = sum(r["pop"] for r in REGIONAL_DATA_SPAIN if not r["is_foral"])
    foral_pop = sum(r["pop"] for r in REGIONAL_DATA_SPAIN if r["is_foral"])

    common_regions: List[RegionalEqualizationRecord] = []
    total_cpff_fund = 0.0

    for reg in REGIONAL_DATA_SPAIN:
        if reg["is_foral"]:
            continue

        pop_share = reg["pop"] / total_pop
        gross_disbursement = cfg["total_gross_b"] * pop_share
        irpf_base = cfg["nat_irpf_base_b"] * reg["irpf_base_share"]
        reg_irpf_share = irpf_base * 0.50  # 50% regional ceded tranche

        # Clawback & Corporate algorithm recovery in territory
        clawback_corp = gross_disbursement * cfg["clawback_rate"]

        # Pre-equalization balance for regional government (regional tranche share minus regional share of net deficit)
        net_transfer_deficit = gross_disbursement - clawback_corp
        pre_balance = reg_irpf_share - (net_transfer_deficit * 0.50)

        # CPFF Fondo de Compensación UBR calculation (Zabalza & López-Laborda formula)
        # Guaranteeing per-capita equality in fundamental public services
        target_per_capita = (cfg["nat_irpf_base_b"] * 0.50) / common_pop
        target_allocation = target_per_capita * reg["pop"]
        equalization_transfer = target_allocation - pre_balance

        if equalization_transfer > 0:
            total_cpff_fund += equalization_transfer

        post_balance = pre_balance + equalization_transfer
        per_capita_net = (post_balance * 1e9) / reg["pop"]

        common_regions.append(
            RegionalEqualizationRecord(
                code=reg["code"],
                name=reg["name"],
                is_foral=False,
                population=reg["pop"],
                gross_irpf_base_eur_b=irpf_base,
                regional_irpf_share_eur_b=reg_irpf_share,
                ubr_gross_transfers_eur_b=gross_disbursement,
                ubr_clawback_and_corporate_eur_b=clawback_corp,
                pre_equalization_balance_eur_b=pre_balance,
                cpff_equalization_transfer_eur_b=equalization_transfer,
                post_equalization_balance_eur_b=post_balance,
                equalized_balance_per_capita_eur=per_capita_net,
            )
        )

    # Foral Calculations
    foral_records: List[ForalCupoRecord] = []

    # 1. Basque Country
    pva_pop = 2210000
    pva_share = pva_pop / total_pop
    pva_disbursement = cfg["total_gross_b"] * pva_share
    # Statutory Cupo coefficient: 6.24% of state non-assumed competencies
    pva_baseline_cupo = 1.480  # Baseline annual Cupo (EUR B)
    # Deduction for non-assumed state expenditure (State pays national UBR)
    pva_deduction = pva_disbursement * 0.0624
    pva_net_cupo = pva_baseline_cupo - pva_deduction
    foral_records.append(
        ForalCupoRecord(
            territory="País Vasco",
            regime_statute="Ley 12/2002 del Concierto Económico",
            statutory_index_pct=6.24,
            population=pva_pop,
            gross_cupo_baseline_eur_b=pva_baseline_cupo,
            ubr_disbursements_in_territory_eur_b=pva_disbursement,
            non_assumed_burden_deduction_eur_b=pva_deduction,
            net_adjusted_cupo_eur_b=pva_net_cupo,
            per_capita_fiscal_impact_eur=(pva_net_cupo * 1e9) / pva_pop,
        )
    )

    # 2. Navarre
    nav_pop = 665000
    nav_share = nav_pop / total_pop
    nav_disbursement = cfg["total_gross_b"] * nav_share
    # Statutory Aportación coefficient: 1.60%
    nav_baseline_aportacion = 0.620  # Baseline annual Aportación (EUR B)
    nav_deduction = nav_disbursement * 0.0160
    nav_net_aportacion = nav_baseline_aportacion - nav_deduction
    foral_records.append(
        ForalCupoRecord(
            territory="Comunidad Foral de Navarra",
            regime_statute="Ley 28/1990 del Convenio Económico",
            statutory_index_pct=1.60,
            population=nav_pop,
            gross_cupo_baseline_eur_b=nav_baseline_aportacion,
            ubr_disbursements_in_territory_eur_b=nav_disbursement,
            non_assumed_burden_deduction_eur_b=nav_deduction,
            net_adjusted_cupo_eur_b=nav_net_aportacion,
            per_capita_fiscal_impact_eur=(nav_net_aportacion * 1e9) / nav_pop,
        )
    )

    return IntergovernmentalEqualizationReport(
        scenario=scenario,
        tier=cfg["tier"],
        ubr_monthly_rate_eur=cfg["rate"],
        total_population_spain=total_pop,
        common_regime_population=common_pop,
        foral_population=foral_pop,
        total_cpff_fund_size_eur_b=total_cpff_fund,
        common_regime_regions=common_regions,
        foral_records=foral_records,
    )
