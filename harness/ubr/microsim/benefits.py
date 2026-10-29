"""Benefit Parameter Design, Disability Supplements, and Welfare Integration (Track 2).

Implements M02 (Benefit Design), M07 (Welfare Benefit Integration), and D-009.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from ubr.microsim.population import (
    DisabilityGrade,
    MicroHousehold,
    MicroIndividual,
    TerritorialRegime,
)


class UBRTier(str, Enum):
    TIER_A = "A"  # €600/mo adult (€7,200/yr), €300/mo child 1, €240/mo child 2+
    TIER_B = "B"  # €900/mo adult (€10,800/yr), €450/mo child 1, €360/mo child 2+
    TIER_C = "C"  # €1,200/mo adult (€14,400/yr), €600/mo child 1, €480/mo child 2+


@dataclass(frozen=True)
class TierParameters:
    tier: UBRTier
    adult_monthly_eur: float
    child1_monthly_eur: float
    child2_plus_monthly_eur: float
    alpha_child1: float = 0.50
    alpha_child2_plus: float = 0.40

    @property
    def adult_annual_eur(self) -> float:
        return self.adult_monthly_eur * 12.0

    @property
    def child1_annual_eur(self) -> float:
        return self.child1_monthly_eur * 12.0

    @property
    def child2_plus_annual_eur(self) -> float:
        return self.child2_plus_monthly_eur * 12.0


TIER_SPECS: dict[UBRTier, TierParameters] = {
    UBRTier.TIER_A: TierParameters(
        tier=UBRTier.TIER_A,
        adult_monthly_eur=600.0,
        child1_monthly_eur=300.0,
        child2_plus_monthly_eur=240.0,
    ),
    UBRTier.TIER_B: TierParameters(
        tier=UBRTier.TIER_B,
        adult_monthly_eur=900.0,
        child1_monthly_eur=450.0,
        child2_plus_monthly_eur=360.0,
    ),
    UBRTier.TIER_C: TierParameters(
        tier=UBRTier.TIER_C,
        adult_monthly_eur=1200.0,
        child1_monthly_eur=600.0,
        child2_plus_monthly_eur=480.0,
    ),
}


@dataclass
class BenefitDisbursement:
    """Individual-level and household-level UBR benefit disbursements."""
    individual_id: str
    is_adult: bool
    base_ubr_annual: float
    disability_supplement_annual: float
    total_cash_ubr_annual: float
    absorbed_baseline_cash: float
    retained_contributory_pension: float
    pension_accrual_credit_smi_annual: float = 0.0


@dataclass
class HouseholdBenefitResult:
    """Consolidated household-level benefit package."""
    household_id: str
    member_disbursements: list[BenefitDisbursement]
    total_household_ubr_annual: float
    total_absorbed_welfare_annual: float
    regional_top_up_annual: float = 0.0
    no_loser_guarantee_supplement: float = 0.0


class BenefitCalculator:
    """Calculates UBR benefits, disability complements, and welfare offsets."""

    def __init__(self, tier: UBRTier = UBRTier.TIER_B):
        self.tier_params = TIER_SPECS[tier]

    def compute_individual_ubr(
        self,
        ind: MicroIndividual,
        child_index: int = 0,
    ) -> tuple[float, float]:
        """Compute base UBR and disability supplement for an individual.
        
        child_index: 0 for first child, 1+ for subsequent children.
        """
        if ind.is_adult:
            base_ubr = self.tier_params.adult_annual_eur
        else:
            if child_index == 0:
                base_ubr = self.tier_params.child1_annual_eur
            else:
                base_ubr = self.tier_params.child2_plus_annual_eur

        # Three-tiered statutory Complemento Universal por Discapacidad (RD 888/2022)
        # Expressed as +25%, +50%, +100% of adult base UBR
        adult_base = self.tier_params.adult_annual_eur
        if ind.disability_grade == DisabilityGrade.GRADE_1:
            disab_supp = 0.25 * adult_base
        elif ind.disability_grade == DisabilityGrade.GRADE_2:
            disab_supp = 0.50 * adult_base
        elif ind.disability_grade == DisabilityGrade.GRADE_3:
            disab_supp = 1.00 * adult_base
        else:
            disab_supp = 0.0

        return base_ubr, disab_supp

    def calculate_household_benefits(
        self,
        hh: MicroHousehold,
    ) -> HouseholdBenefitResult:
        """Calculate UBR entitlements and welfare offsets for a household."""
        disbursements: list[BenefitDisbursement] = []
        child_counter = 0
        total_hh_ubr = 0.0
        total_absorbed_welfare = 0.0

        # Absorbed baseline household IMV
        total_absorbed_welfare += hh.baseline_imv_received

        for ind in hh.members:
            child_idx = 0
            if not ind.is_adult:
                child_idx = child_counter
                child_counter += 1

            base_ubr, disab_supp = self.compute_individual_ubr(ind, child_idx)
            total_ind_ubr = base_ubr + disab_supp
            total_hh_ubr += total_ind_ubr

            # Absorbed non-contributory cash transfers (PNC, subsidios de desempleo)
            absorbed_cash = ind.baseline_non_contributory_cash
            total_absorbed_welfare += absorbed_cash

            # Tier 2 Dual-Pillar Contributory Pension Integration:
            # UBR serves as the non-taxable base floor (€600/€900/€1,200).
            # The contributory Social Security pillar pays the difference:
            # retained = max(0, contributory_pension - UBR_base)
            retained_pension = 0.0
            if ind.contributory_pension_gross > 0.0:
                retained_pension = max(0.0, ind.contributory_pension_gross - base_ubr)

            # Statutory Social Security Pension Accrual Continuity (Art. 273 TRLGSS, D-009):
            # 100% SMI contribution accrual guarantee for inactive or displaced workers
            smi_base_annual = 15876.0
            accrual_credit = 0.0
            if ind.is_adult and not ind.is_employed and ind.contributory_pension_gross == 0.0:
                accrual_credit = smi_base_annual

            disbursements.append(
                BenefitDisbursement(
                    individual_id=ind.id,
                    is_adult=ind.is_adult,
                    base_ubr_annual=base_ubr,
                    disability_supplement_annual=disab_supp,
                    total_cash_ubr_annual=total_ind_ubr,
                    absorbed_baseline_cash=absorbed_cash,
                    retained_contributory_pension=retained_pension,
                    pension_accrual_credit_smi_annual=accrual_credit,
                )
            )

        # Tier 4 Regional Top-Up (Basque RGI + PCV/PEV, Navarre):
        # In Foral territories, if baseline regional minimum entitlement exceeds UBR,
        # preserve the difference as a Complemento Autonómico No Contributivo
        regional_top_up = 0.0
        if hh.territory == TerritorialRegime.FORAL_BASQUE_NAVARRE:
            # High foral minimum income baseline (~€11,500/yr single, ~€15,500/yr with housing/dependents)
            foral_baseline = 11500.0 if hh.num_adults == 1 else 15500.0
            if hh.is_single_parent:
                foral_baseline += 2400.0
            if total_hh_ubr < foral_baseline:
                regional_top_up = foral_baseline - total_hh_ubr

        return HouseholdBenefitResult(
            household_id=hh.id,
            member_disbursements=disbursements,
            total_household_ubr_annual=total_hh_ubr,
            total_absorbed_welfare_annual=total_absorbed_welfare,
            regional_top_up_annual=regional_top_up,
            no_loser_guarantee_supplement=0.0,
        )
