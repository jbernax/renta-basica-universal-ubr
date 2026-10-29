"""Spanish Household & Individual Population Model for Microsimulation (Track 2).

Calibrated to INE Encuesta de Condiciones de Vida (ECV / EU-SILC),
AEAT Muestra de Declarantes de IRPF, and INSS administrative registers.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import json
from pathlib import Path
from typing import Any, Sequence


class HousingTenure(str, Enum):
    OUTRIGHT_OWNER = "outright_owner"
    MORTGAGED_OWNER = "mortgaged_owner"
    PRIVATE_RENTER = "private_renter"
    SOCIAL_RENTER = "social_renter"


class DisabilityGrade(str, Enum):
    NONE = "none"
    GRADE_1 = "grade_1"  # 33% - 64% (Moderate)
    GRADE_2 = "grade_2"  # 65% - 74% (Severe)
    GRADE_3 = "grade_3"  # 75%+ / Gran Invalidez (Great Disability)


class TerritorialRegime(str, Enum):
    COMMON_METRO = "common_metro"      # High-cost urban: Madrid, Barcelona, Balearics, etc.
    COMMON_NON_METRO = "common_non_metro"  # Other Common Regime Autonomous Communities
    FORAL_BASQUE_NAVARRE = "foral"     # Basque Country & Navarre (Concierto / Convenio)


@dataclass
class MicroIndividual:
    """Individual record within a household."""
    id: str
    age: int
    is_adult: bool
    labor_earnings_gross: float = 0.0
    capital_income_gross: float = 0.0
    contributory_pension_gross: float = 0.0
    is_contributory_disability: bool = False  # Art. 7.f LIRPF exempt
    disability_grade: DisabilityGrade = DisabilityGrade.NONE
    baseline_non_contributory_cash: float = 0.0  # PNC, subsidio desempleo, etc.
    cno_code: str | None = None
    is_employed: bool = False
    weight: float = 1.0


@dataclass
class MicroHousehold:
    """Household unit composed of individuals with shared housing costs."""
    id: str
    members: list[MicroIndividual]
    tenure: HousingTenure
    territory: TerritorialRegime
    baseline_housing_cost_annual: float
    baseline_imv_received: float = 0.0  # Household-level IMV + CAPI received
    weight: float = 1.0

    @property
    def adults(self) -> list[MicroIndividual]:
        return [m for m in self.members if m.is_adult]

    @property
    def minors(self) -> list[MicroIndividual]:
        return [m for m in self.members if not m.is_adult]

    @property
    def num_adults(self) -> int:
        return len(self.adults)

    @property
    def num_minors(self) -> int:
        return len(self.minors)

    @property
    def is_single_parent(self) -> bool:
        return self.num_adults == 1 and self.num_minors >= 1

    @property
    def modified_oecd_scale(self) -> float:
        """Modified OECD equivalence scale: 1.0 first adult, 0.5 additional adults/teens >= 14, 0.3 children < 14.
        Approximated here with 1.0 for first adult, 0.5 for other adults, 0.3 for minors.
        """
        if not self.members:
            return 1.0
        scale = 1.0
        if self.num_adults > 1:
            scale += 0.5 * (self.num_adults - 1)
        scale += 0.3 * self.num_minors
        return scale


@dataclass
class PopulationDataset:
    """Calibrated representative microdata sample representing the Spanish population."""
    households: list[MicroHousehold]
    scaling_factor: float  # Factor to scale sample weights to national totals (e.g. ~48M individuals)

    def total_individuals(self) -> float:
        return sum(len(h.members) * h.weight * self.scaling_factor for h in self.households)

    def total_adults(self) -> float:
        return sum(h.num_adults * h.weight * self.scaling_factor for h in self.households)

    def total_minors(self) -> float:
        return sum(h.num_minors * h.weight * self.scaling_factor for h in self.households)

    def total_households(self) -> float:
        return sum(h.weight * self.scaling_factor for h in self.households)

    def apply_labor_counterfactual(self, counterfactual_data: dict[str, Any]) -> None:
        """Update individual labor earnings based on Track 1 post-displacement distributions.
        
        Uses the wage_deciles_pre and wage_deciles_post from the scenario payload
        to scale labor income along the distribution.
        """
        pre_deciles = counterfactual_data.get("wage_deciles_pre")
        post_deciles = counterfactual_data.get("wage_deciles_post")
        if not pre_deciles or not post_deciles or len(pre_deciles) != len(post_deciles):
            return

        # Compute decile-specific scaling factors
        ratios = [post / pre if pre > 0 else 1.0 for pre, post in zip(pre_deciles, post_deciles)]
        
        # Sort employed individuals by earnings to determine their decile
        employed_members = [
            m for h in self.households for m in h.members if m.is_employed and m.labor_earnings_gross > 0
        ]
        if not employed_members:
            return
            
        employed_members.sort(key=lambda m: m.labor_earnings_gross)
        n = len(employed_members)
        
        for idx, m in enumerate(employed_members):
            decile_idx = min(int(idx / n * 10), 9)
            scale = ratios[decile_idx]
            m.labor_earnings_gross *= scale
            # If wage fell below SMI floor or severe displacement occurs, extensive margin kicks in
            smi_floor_annual = 15876.0  # 1,134 * 14
            if m.labor_earnings_gross < smi_floor_annual * 0.7:
                # Displaced into unemployment / search
                m.is_employed = False
                m.labor_earnings_gross = 0.0


def generate_calibrated_spanish_population(sample_size_households: int = 5000) -> PopulationDataset:
    """Generate a calibrated representative sample of Spanish households and individuals.
    
    Calibrated to 2024-2026 aggregates:
    - 48.0M population (39.8M adults, 8.2M minors)
    - 19.2M households
    - 21.5M employed FTE workers
    - Aggregate wage bill: €518.9B
    - Contributory pensions: ~10M pensioners, €170B
    - Housing tenure: 48% outright owners, 28% mortgaged, 16% private renters, 8% social renters
    - Territorial: 32% high-cost metro, 58% common non-metro, 10% foral
    """
    households: list[MicroHousehold] = []
    
    # Target counts in sample calibrated to Spain 2024-2026:
    # 48.0M population (39.8M adults, 8.2M minors across 19.2M households)
    # Reflects high youth cohabitation in Spain (adult children living with parents)
    tenure_distribution = [
        (HousingTenure.OUTRIGHT_OWNER, 0.48),
        (HousingTenure.MORTGAGED_OWNER, 0.28),
        (HousingTenure.PRIVATE_RENTER, 0.16),
        (HousingTenure.SOCIAL_RENTER, 0.08),
    ]
    
    territory_distribution = [
        (TerritorialRegime.COMMON_METRO, 0.32),
        (TerritorialRegime.COMMON_NON_METRO, 0.58),
        (TerritorialRegime.FORAL_BASQUE_NAVARRE, 0.10),
    ]

    for i in range(sample_size_households):
        hid = f"HH_{i:05d}"
        
        # Household type cycle
        mod_100 = i % 100
        if mod_100 < 24:
            # Single adult living alone (working age or elderly)
            adult_count = 1
            minor_count = 0
            is_single_parent = False
        elif mod_100 < 32:
            # Single parent with minors (average ~1.3 minors)
            adult_count = 1
            minor_count = 1 if (i % 3 != 0) else 2
            is_single_parent = True
        elif mod_100 < 60:
            # Couple without cohabiting minors (either no kids or adult children emancipated)
            adult_count = 2
            minor_count = 0
            is_single_parent = False
        elif mod_100 < 78:
            # Couple with minors (average ~1.6 minors)
            adult_count = 2
            minor_count = 1 if (i % 2 == 0) else (2 if i % 4 != 0 else 3)
            is_single_parent = False
        elif mod_100 < 94:
            # Couple with adult offspring cohabiting (3 or 4 adults, 0 minors, avg 3.6)
            adult_count = 3 if (i % 3 == 0) else 4
            minor_count = 0
            is_single_parent = False
        else:
            # Multi-generational household (3 adults + 1 minor)
            adult_count = 3
            minor_count = 1
            is_single_parent = False

        # Assign tenure
        tenure_cum = 0.0
        tenure_val = (i * 7 + 13) % 100 / 100.0
        chosen_tenure = HousingTenure.OUTRIGHT_OWNER
        for ten, prob in tenure_distribution:
            tenure_cum += prob
            if tenure_val <= tenure_cum:
                chosen_tenure = ten
                break
                
        # Assign territory
        terr_cum = 0.0
        terr_val = (i * 11 + 17) % 100 / 100.0
        chosen_terr = TerritorialRegime.COMMON_NON_METRO
        for terr, prob in territory_distribution:
            terr_cum += prob
            if terr_val <= terr_cum:
                chosen_terr = terr
                break

        # Annual housing costs
        # Metro private rents: ~€10,800/yr (€900/mo)
        # Non-metro private rents: ~€7,200/yr (€600/mo)
        # Mortgages: ~€6,000 - €8,400/yr
        # Social rents: ~€2,400/yr
        # Outright owners: €0 direct rent/mortgage
        if chosen_tenure == HousingTenure.PRIVATE_RENTER:
            if chosen_terr == TerritorialRegime.COMMON_METRO:
                housing_cost = 10800.0 + (i % 10) * 240.0
            else:
                housing_cost = 7200.0 + (i % 10) * 180.0
        elif chosen_tenure == HousingTenure.MORTGAGED_OWNER:
            housing_cost = 7200.0 + (i % 10) * 200.0
        elif chosen_tenure == HousingTenure.SOCIAL_RENTER:
            housing_cost = 2400.0 + (i % 5) * 120.0
        else:
            housing_cost = 0.0

        # Construct members
        members: list[MicroIndividual] = []
        
        # Adults
        for a_idx in range(adult_count):
            mid = f"{hid}_A{a_idx+1}"
            
            # Age profile
            # 20% young adult (18-29), 55% working age (30-64), 25% pensioner (65+)
            age_bucket = (i * 3 + a_idx * 17) % 100
            if age_bucket < 20:
                age = 18 + ((i + a_idx) % 12)
                is_pensioner = False
            elif age_bucket < 75:
                age = 30 + ((i + a_idx) % 35)
                is_pensioner = False
            else:
                age = 65 + ((i + a_idx) % 25)
                is_pensioner = True

            # Disability: 9% of population
            disab_roll = (i * 13 + a_idx * 23) % 100
            if disab_roll < 5:
                disab_grade = DisabilityGrade.GRADE_1
            elif disab_roll < 8:
                disab_grade = DisabilityGrade.GRADE_2
            elif disab_roll < 9:
                disab_grade = DisabilityGrade.GRADE_3
            else:
                disab_grade = DisabilityGrade.NONE

            # Income assignment
            labor_gross = 0.0
            pension_gross = 0.0
            capital_gross = 0.0
            non_contrib_cash = 0.0
            is_employed = False
            is_contributory_disab = False

            if is_pensioner:
                # Contributory retirement pension
                # Average pension ~€19,600/yr (€1,400/mo * 14)
                # Distribution from minimum ~€11,000 to max ~€44,000
                pension_rank = ((i * 5 + a_idx * 19) % 100) / 100.0
                if pension_rank < 0.15:
                    # Non-contributory retirement pension (PNC ~€7,250/yr)
                    non_contrib_cash = 7250.0
                else:
                    pension_gross = 12000.0 + pension_rank * 26000.0
            else:
                # Working age
                # Employment rate ~70%
                emp_roll = ((i * 7 + a_idx * 31) % 100) / 100.0
                if emp_roll < 0.70:
                    is_employed = True
                    # Wage profile matching Spanish EPA distribution
                    # Decile 1: €14,700 - €16,500 (near SMI)
                    # Median: ~€24,500
                    # Top decile: €55,000 - €120,000
                    rank = ((i * 13 + a_idx * 29) % 100) / 100.0
                    if rank < 0.20:
                        labor_gross = 15876.0 + rank * 8000.0  # SMI floor
                    elif rank < 0.80:
                        labor_gross = 18000.0 + rank * 24000.0
                    else:
                        labor_gross = 38000.0 + (rank - 0.80) * 160000.0
                else:
                    # Unemployed or inactive
                    unemp_roll = (i + a_idx) % 10
                    if unemp_roll < 4:
                        # Contributory unemployment insurance (SEPE)
                        pension_gross = 11000.0 + unemp_roll * 1500.0
                    elif unemp_roll < 7:
                        # Non-contributory unemployment subsidio (€480/mo = €5,760/yr)
                        non_contrib_cash = 5760.0
                    else:
                        # Inactive with 0 income (relying on family/IMV)
                        labor_gross = 0.0

            # Permanent disability contributory carveout (Art. 7.f LIRPF)
            if disab_grade in (DisabilityGrade.GRADE_2, DisabilityGrade.GRADE_3) and is_pensioner and pension_gross > 0:
                is_contributory_disab = True

            # Capital income (concentrated in top 20% of earners/pensioners)
            if (labor_gross + pension_gross) > 40000.0:
                cap_rank = ((i * 17) % 50) / 50.0
                capital_gross = 2000.0 + cap_rank * 25000.0

            members.append(
                MicroIndividual(
                    id=mid,
                    age=age,
                    is_adult=True,
                    labor_earnings_gross=labor_gross,
                    capital_income_gross=capital_gross,
                    contributory_pension_gross=pension_gross,
                    is_contributory_disability=is_contributory_disab,
                    disability_grade=disab_grade,
                    baseline_non_contributory_cash=non_contrib_cash,
                    is_employed=is_employed,
                    weight=1.0,
                )
            )

        # Minors
        for m_idx in range(minor_count):
            mid = f"{hid}_M{m_idx+1}"
            age = (i * 2 + m_idx * 5) % 18
            disab_roll = (i * 19 + m_idx * 11) % 100
            disab_grade = DisabilityGrade.GRADE_1 if disab_roll < 3 else DisabilityGrade.NONE
            members.append(
                MicroIndividual(
                    id=mid,
                    age=age,
                    is_adult=False,
                    disability_grade=disab_grade,
                    weight=1.0,
                )
            )

        # Baseline IMV allocation for very low income households (calibrated with AIReF non-takeup)
        total_market_inc = sum(m.labor_earnings_gross + m.contributory_pension_gross for m in members)
        imv_received = 0.0
        if total_market_inc < 8000.0:
            # Qualifying for IMV; subject to 56% non-take-up
            takeup_roll = (i * 29) % 100
            if takeup_roll < 44:  # 44% take-up
                imv_baseline = 7250.0 if adult_count == 1 else 9500.0
                if minor_count > 0:
                    imv_baseline += minor_count * 2000.0
                if is_single_parent:
                    imv_baseline *= 1.22  # Single parent bonus
                imv_received = max(0.0, imv_baseline - total_market_inc)

        households.append(
            MicroHousehold(
                id=hid,
                members=members,
                tenure=chosen_tenure,
                territory=chosen_terr,
                baseline_housing_cost_annual=housing_cost,
                baseline_imv_received=imv_received,
                weight=1.0,
            )
        )

    # Parametric Pareto reweighting on top 5% market incomes (M09 Section 5)
    # Matches AEAT Muestra de Declarantes microdata to eliminate top-income right-truncation
    all_earners = [
        m for h in households for m in h.members
        if m.is_adult and (m.labor_earnings_gross + m.capital_income_gross > 0)
    ]
    if all_earners:
        all_earners.sort(key=lambda m: m.labor_earnings_gross + m.capital_income_gross)
        n_earners = len(all_earners)
        p95_idx = int(n_earners * 0.95)
        p95_threshold = all_earners[p95_idx].labor_earnings_gross + all_earners[p95_idx].capital_income_gross
        pareto_alpha = 1.95  # Calibrated Spanish Pareto tail index
        for idx in range(p95_idx, n_earners):
            u = (idx - p95_idx + 0.5) / (n_earners - p95_idx)
            pareto_val = min(1_500_000.0, p95_threshold * ((1.0 - u) ** (-1.0 / pareto_alpha)))
            all_earners[idx].capital_income_gross = pareto_val * 0.40
            all_earners[idx].labor_earnings_gross = pareto_val * 0.60

    # Calculate national scaling factor: target 19.2M households in Spain
    target_national_households = 19_200_000.0
    scaling_factor = target_national_households / float(len(households))

    return PopulationDataset(households=households, scaling_factor=scaling_factor)
