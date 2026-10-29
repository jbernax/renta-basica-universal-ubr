"""Housing Market Interaction, Rent Pass-Through, and Landlord Recycling (Track 2).

Implements M05 (Housing Rent Capture), M09, and D-008 (Objective Federal Fiscal Benchmark).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ubr.microsim.population import (
    HousingTenure,
    MicroHousehold,
    TerritorialRegime,
)


@dataclass
class HouseholdHousingResult:
    household_id: str
    tenure: HousingTenure
    territory: TerritorialRegime
    baseline_housing_cost: float
    post_reform_housing_cost: float
    rent_increase_captured: float
    is_housing_overburdened_baseline: bool
    is_housing_overburdened_post: bool


@dataclass
class HousingAggregateMetrics:
    overburden_rate_baseline_pct: float
    overburden_rate_post_pct: float
    overburden_bottom_quintile_baseline_pct: float
    overburden_bottom_quintile_post_pct: float
    private_renter_overburden_baseline_pct: float
    private_renter_overburden_post_pct: float
    total_rent_captured_by_landlords_eur: float
    landlord_tax_recapture_eur: float
    net_rent_leakage_eur: float


class HousingCalculator:
    """Simulates rent pass-through, rent stabilization, and housing overburden."""

    def __init__(
        self,
        enable_rent_stabilizers: bool = True,
        metro_pass_through_uncontrolled: float = 0.28,
        non_metro_pass_through_uncontrolled: float = 0.18,
    ):
        self.enable_rent_stabilizers = enable_rent_stabilizers
        self.metro_pass_through_uncontrolled = metro_pass_through_uncontrolled
        self.non_metro_pass_through_uncontrolled = non_metro_pass_through_uncontrolled

    def calculate_post_reform_housing_cost(
        self,
        hh: MicroHousehold,
        gross_ubr_received: float,
    ) -> tuple[float, float]:
        """Compute post-reform housing costs and landlord rent capture.
        
        If rent stabilizers (Objective Federal Fiscal Housing Benchmark, D-008) are active,
        landlord rent capture is suppressed to near zero (<3%).
        """
        baseline_cost = hh.baseline_housing_cost_annual

        if hh.tenure != HousingTenure.PRIVATE_RENTER:
            # Mortgaged owners, outright owners, and social renters face no market rent capture
            return baseline_cost, 0.0

        if self.enable_rent_stabilizers:
            # D-008 Objective Federal Fiscal Housing Benchmark conditions LIRPF Art. 23.2 reductions
            # on benchmark adherence, suppressing rent capture
            effective_pass_through = 0.02
        else:
            if hh.territory == TerritorialRegime.COMMON_METRO:
                effective_pass_through = self.metro_pass_through_uncontrolled
            else:
                effective_pass_through = self.non_metro_pass_through_uncontrolled

        rent_captured = gross_ubr_received * effective_pass_through
        post_cost = baseline_cost + rent_captured
        return post_cost, rent_captured

    def evaluate_household_housing(
        self,
        hh: MicroHousehold,
        gross_ubr_received: float,
        baseline_disposable_income: float,
        post_disposable_income: float,
    ) -> HouseholdHousingResult:
        post_cost, rent_captured = self.calculate_post_reform_housing_cost(hh, gross_ubr_received)

        # Eurostat housing-cost overburden: housing costs > 40% of disposable income
        is_overburdened_base = False
        if baseline_disposable_income > 0.0:
            is_overburdened_base = (hh.baseline_housing_cost_annual / baseline_disposable_income) > 0.40

        is_overburdened_post = False
        if post_disposable_income > 0.0:
            is_overburdened_post = (post_cost / post_disposable_income) > 0.40

        return HouseholdHousingResult(
            household_id=hh.id,
            tenure=hh.tenure,
            territory=hh.territory,
            baseline_housing_cost=hh.baseline_housing_cost_annual,
            post_reform_housing_cost=post_cost,
            rent_increase_captured=rent_captured,
            is_housing_overburdened_baseline=is_overburdened_base,
            is_housing_overburdened_post=is_overburdened_post,
        )

    def compute_aggregate_housing_metrics(
        self,
        housing_results: list[HouseholdHousingResult],
        baseline_disposable_incomes: list[float],
        weights: list[float],
        scaling_factor: float,
    ) -> HousingAggregateMetrics:
        """Compute nationwide housing overburden and landlord tax recycling."""
        total_w = sum(w * scaling_factor for w in weights)
        if total_w <= 0.0:
            return HousingAggregateMetrics(0, 0, 0, 0, 0, 0, 0, 0, 0)

        # Baseline and post overburden
        w_overburden_base = sum(
            w * scaling_factor for res, w in zip(housing_results, weights) if res.is_housing_overburdened_baseline
        )
        w_overburden_post = sum(
            w * scaling_factor for res, w in zip(housing_results, weights) if res.is_housing_overburdened_post
        )

        pct_overburden_base = (w_overburden_base / total_w) * 100.0
        pct_overburden_post = (w_overburden_post / total_w) * 100.0

        # Private renters overburden
        renter_results = [(res, w) for res, w in zip(housing_results, weights) if res.tenure == HousingTenure.PRIVATE_RENTER]
        total_renter_w = sum(w * scaling_factor for _, w in renter_results)
        if total_renter_w > 0:
            renter_base_w = sum(w * scaling_factor for res, w in renter_results if res.is_housing_overburdened_baseline)
            renter_post_w = sum(w * scaling_factor for res, w in renter_results if res.is_housing_overburdened_post)
            pct_renter_base = (renter_base_w / total_renter_w) * 100.0
            pct_renter_post = (renter_post_w / total_renter_w) * 100.0
        else:
            pct_renter_base, pct_renter_post = 0.0, 0.0

        # Bottom quintile overburden
        sorted_pairs = sorted(zip(baseline_disposable_incomes, housing_results, weights), key=lambda x: x[0])
        q1_w_target = total_w * 0.20
        curr_w = 0.0
        q1_pairs = []
        for inc, res, w in sorted_pairs:
            q1_pairs.append((res, w))
            curr_w += w * scaling_factor
            if curr_w >= q1_w_target:
                break
        total_q1_w = sum(w * scaling_factor for _, w in q1_pairs)
        if total_q1_w > 0:
            q1_base_w = sum(w * scaling_factor for res, w in q1_pairs if res.is_housing_overburdened_baseline)
            q1_post_w = sum(w * scaling_factor for res, w in q1_pairs if res.is_housing_overburdened_post)
            pct_q1_base = (q1_base_w / total_q1_w) * 100.0
            pct_q1_post = (q1_post_w / total_q1_w) * 100.0
        else:
            pct_q1_base, pct_q1_post = 0.0, 0.0

        # Total rent captured and landlord tax recycling per Khametshin et al. (2024):
        # Physical landlords (75% of private stock): 48% IRPF clawback
        # Corporate SOCIMIs & non-residents (25% of stock): 15% flat/exempt
        total_captured = sum(res.rent_increase_captured * w * scaling_factor for res, w in zip(housing_results, weights))
        tax_recaptured = total_captured * (0.75 * 0.48 + 0.25 * 0.15)
        leakage = total_captured - tax_recaptured

        return HousingAggregateMetrics(
            overburden_rate_baseline_pct=pct_overburden_base,
            overburden_rate_post_pct=pct_overburden_post,
            overburden_bottom_quintile_baseline_pct=pct_q1_base,
            overburden_bottom_quintile_post_pct=pct_q1_post,
            private_renter_overburden_baseline_pct=pct_renter_base,
            private_renter_overburden_post_pct=pct_renter_post,
            total_rent_captured_by_landlords_eur=total_captured,
            landlord_tax_recapture_eur=tax_recaptured,
            net_rent_leakage_eur=leakage,
        )
