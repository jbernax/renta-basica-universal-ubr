"""Comprehensive Tests for Track 2: Microsimulation Engine (M02, M03, M07, M09)."""
from __future__ import annotations

import json
from pathlib import Path
import pytest

from ubr.microsim.benefits import (
    BenefitCalculator,
    BenefitDisbursement,
    TIER_SPECS,
    UBRTier,
)
from ubr.microsim.engine import MicrosimulationEngine, SimulationRunResult
from ubr.microsim.housing import HousingCalculator, HousingTenure
from ubr.microsim.poverty_metrics import (
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
    MicroIndividual,
    TerritorialRegime,
    generate_calibrated_spanish_population,
)
from ubr.microsim.taxation import (
    BASELINE_IRPF_BRACKETS,
    REFORM_IRPF_BRACKETS,
    TaxCalculator,
)


def test_population_calibration():
    pop = generate_calibrated_spanish_population(sample_size_households=1000)
    assert pop.total_households() == pytest.approx(19_200_000.0, rel=1e-3)
    
    # Spanish population in 2024-2026 is approx 47 - 49 million
    total_pop = pop.total_individuals()
    assert 45_000_000 <= total_pop <= 49_000_000
    
    # Adults vs minors: ~80-85% adults, ~15-20% minors
    adults = pop.total_adults()
    minors = pop.total_minors()
    assert adults + minors == pytest.approx(total_pop, rel=1e-5)
    assert 0.78 <= adults / total_pop <= 0.86
    assert 0.14 <= minors / total_pop <= 0.22

    # Housing tenure distribution check
    tenures = {h.tenure for h in pop.households}
    assert HousingTenure.OUTRIGHT_OWNER in tenures
    assert HousingTenure.MORTGAGED_OWNER in tenures
    assert HousingTenure.PRIVATE_RENTER in tenures
    assert HousingTenure.SOCIAL_RENTER in tenures

    # Territorial regime check
    territories = {h.territory for h in pop.households}
    assert TerritorialRegime.COMMON_METRO in territories
    assert TerritorialRegime.COMMON_NON_METRO in territories
    assert TerritorialRegime.FORAL_BASQUE_NAVARRE in territories


def test_benefit_parameters_and_parity_modulated_child_scale():
    # Tier A
    p_a = TIER_SPECS[UBRTier.TIER_A]
    assert p_a.adult_monthly_eur == 600.0
    assert p_a.adult_annual_eur == 7200.0
    assert p_a.child1_monthly_eur == 300.0
    assert p_a.child2_plus_monthly_eur == 240.0
    assert p_a.alpha_child1 == 0.50
    assert p_a.alpha_child2_plus == 0.40

    # Tier B
    p_b = TIER_SPECS[UBRTier.TIER_B]
    assert p_b.adult_monthly_eur == 900.0
    assert p_b.adult_annual_eur == 10800.0
    assert p_b.child1_monthly_eur == 450.0
    assert p_b.child2_plus_monthly_eur == 360.0

    # Tier C
    p_c = TIER_SPECS[UBRTier.TIER_C]
    assert p_c.adult_monthly_eur == 1200.0
    assert p_c.adult_annual_eur == 14400.0
    assert p_c.child1_monthly_eur == 600.0
    assert p_c.child2_plus_monthly_eur == 480.0

    calc_b = BenefitCalculator(UBRTier.TIER_B)
    adult = MicroIndividual(id="A1", age=35, is_adult=True)
    child1 = MicroIndividual(id="C1", age=8, is_adult=False)
    child2 = MicroIndividual(id="C2", age=4, is_adult=False)

    base_a, dis_a = calc_b.compute_individual_ubr(adult)
    assert base_a == 10800.0
    assert dis_a == 0.0

    base_c1, dis_c1 = calc_b.compute_individual_ubr(child1, child_index=0)
    assert base_c1 == 5400.0  # €450 * 12
    assert dis_c1 == 0.0

    base_c2, dis_c2 = calc_b.compute_individual_ubr(child2, child_index=1)
    assert base_c2 == 4320.0  # €360 * 12
    assert dis_c2 == 0.0


def test_disability_supplements_rd_888_2022():
    calc_b = BenefitCalculator(UBRTier.TIER_B)
    adult_base = 10800.0

    g1 = MicroIndividual(id="D1", age=40, is_adult=True, disability_grade=DisabilityGrade.GRADE_1)
    g2 = MicroIndividual(id="D2", age=40, is_adult=True, disability_grade=DisabilityGrade.GRADE_2)
    g3 = MicroIndividual(id="D3", age=40, is_adult=True, disability_grade=DisabilityGrade.GRADE_3)

    _, supp1 = calc_b.compute_individual_ubr(g1)
    _, supp2 = calc_b.compute_individual_ubr(g2)
    _, supp3 = calc_b.compute_individual_ubr(g3)

    assert supp1 == pytest.approx(0.25 * adult_base)  # +25% = €2,700/yr
    assert supp2 == pytest.approx(0.50 * adult_base)  # +50% = €5,400/yr
    assert supp3 == pytest.approx(1.00 * adult_base)  # +100% = €10,800/yr


def test_dual_pillar_pension_integration_and_art_273_accrual():
    calc_b = BenefitCalculator(UBRTier.TIER_B)
    
    # Contributory pensioner with €20,000 baseline pension
    pensioner = MicroIndividual(id="P1", age=70, is_adult=True, contributory_pension_gross=20000.0)
    hh = MicroHousehold(
        id="HH_P",
        members=[pensioner],
        tenure=HousingTenure.OUTRIGHT_OWNER,
        territory=TerritorialRegime.COMMON_NON_METRO,
        baseline_housing_cost_annual=0.0,
    )
    res = calc_b.calculate_household_benefits(hh)
    disb = res.member_disbursements[0]

    # UBR provides non-taxable base floor of €10,800
    assert disb.base_ubr_annual == 10800.0
    # Social Security pays the remaining contributory entitlement: €20,000 - €10,800 = €9,200
    assert disb.retained_contributory_pension == pytest.approx(9200.0)

    # Inactive displaced worker receiving Art. 273 TRLGSS / D-009 accrual credit
    displaced_worker = MicroIndividual(id="W1", age=45, is_adult=True, is_employed=False, contributory_pension_gross=0.0)
    hh_w = MicroHousehold(
        id="HH_W",
        members=[displaced_worker],
        tenure=HousingTenure.PRIVATE_RENTER,
        territory=TerritorialRegime.COMMON_METRO,
        baseline_housing_cost_annual=10800.0,
    )
    res_w = calc_b.calculate_household_benefits(hh_w)
    disb_w = res_w.member_disbursements[0]
    assert disb_w.pension_accrual_credit_smi_annual == 15876.0  # 100% SMI base accrual credit


def test_tax_calculator_baseline_and_reform_brackets():
    tax_calc = TaxCalculator()

    # Minimum wage worker: €15,876 gross
    ind_smi = MicroIndividual(id="SMI", age=30, is_adult=True, labor_earnings_gross=15876.0, is_employed=True)
    base_irpf, employee_ss = tax_calc.compute_baseline_tax(ind_smi)
    assert employee_ss == pytest.approx(15876.0 * 0.0635)
    # Baseline IRPF is very low due to Art. 20 reduction and minimo personal
    assert base_irpf < 1000.0

    ref_tax, credit, _ = tax_calc.compute_reform_tax(ind_smi, retained_contributory_pension=0.0)
    # Formal work tax credit shields entry wage payslips
    assert credit > 0.0
    assert ref_tax < 5000.0

    # Permanent disability pension exemption (Art. 7.f LIRPF)
    ind_disab_pen = MicroIndividual(
        id="DIS_PEN",
        age=66,
        is_adult=True,
        contributory_pension_gross=25000.0,
        is_contributory_disability=True,
    )
    b_tax, _ = tax_calc.compute_baseline_tax(ind_disab_pen)
    r_tax, _, _ = tax_calc.compute_reform_tax(ind_disab_pen, retained_contributory_pension=14200.0)
    assert b_tax == 0.0
    assert r_tax == 0.0  # Preserves 100% statutory tax exemption under Art. 7.f LIRPF


def test_housing_rent_pass_through_and_stabilizers():
    # Without rent stabilizers
    housing_uncontrolled = HousingCalculator(enable_rent_stabilizers=False)
    # With rent stabilizers (Objective Federal Fiscal Housing Benchmark, D-008)
    housing_controlled = HousingCalculator(enable_rent_stabilizers=True)

    hh_metro_renter = MicroHousehold(
        id="H_RENTER",
        members=[MicroIndividual(id="R1", age=32, is_adult=True)],
        tenure=HousingTenure.PRIVATE_RENTER,
        territory=TerritorialRegime.COMMON_METRO,
        baseline_housing_cost_annual=10800.0,
    )

    gross_ubr = 10800.0
    cost_uncontrolled, captured_uncontrolled = housing_uncontrolled.calculate_post_reform_housing_cost(
        hh_metro_renter, gross_ubr
    )
    cost_controlled, captured_controlled = housing_controlled.calculate_post_reform_housing_cost(
        hh_metro_renter, gross_ubr
    )

    # In uncontrolled metro market, landlords capture ~28% of transfer (~€3,024)
    assert captured_uncontrolled > 2500.0
    assert cost_uncontrolled > 13000.0

    # Under D-008 Objective Federal Benchmark, rent capture is suppressed to <= 2% (<€300)
    assert captured_controlled < 300.0
    assert cost_controlled < 11100.0


def test_poverty_indices_mathematical_properties():
    # Test FGT indices
    incomes = [5000.0, 8000.0, 15000.0, 25000.0, 50000.0]
    weights = [1.0, 1.0, 1.0, 1.0, 1.0]
    z = 10000.0  # Poverty threshold

    fgt = compute_fgt(incomes, weights, z)
    # 2 out of 5 people are poor: P0 = 0.40
    assert fgt.p0_headcount_ratio == pytest.approx(0.40)
    # P1 poverty gap: ((10000-5000)/10000 + (10000-8000)/10000) / 5 = (0.5 + 0.2) / 5 = 0.14
    assert fgt.p1_poverty_gap == pytest.approx(0.14)
    # P2 poverty severity: (0.5^2 + 0.2^2) / 5 = (0.25 + 0.04) / 5 = 0.058
    assert fgt.p2_poverty_severity == pytest.approx(0.058)

    # Test Gini properties
    # Perfect equality
    equal_inc = [20000.0, 20000.0, 20000.0, 20000.0]
    assert compute_gini(equal_inc, [1.0] * 4) == pytest.approx(0.0)

    # Unequal
    unequal_inc = [1000.0, 5000.0, 20000.0, 100000.0]
    gini = compute_gini(unequal_inc, [1.0] * 4)
    assert 0.40 <= gini <= 0.80

    # Theil and Atkinson
    theil = compute_theil(unequal_inc, [1.0] * 4)
    atkinson = compute_atkinson(unequal_inc, [1.0] * 4)
    assert theil > 0.0
    assert atkinson > 0.0


def test_full_simulation_tier_b_scenario_s2_benchmarks():
    engine = MicrosimulationEngine()
    result = engine.run_simulation(tier=UBRTier.TIER_B, scenario="S2")

    fb = result.fiscal_bridge
    # 1. Status-quo budget neutrality check
    assert fb.is_budget_neutral is True
    # Net balance should be within +/- 0.5% GDP
    assert -0.50 <= fb.consolidated_net_balance_pct_gdp <= 0.50

    # 2. Breakeven income threshold check (RQ-M03-01: 82nd - 86th percentile, ~€38,000 - €44,000)
    assert 82.0 <= fb.breakeven_percentile <= 86.0
    assert 38000.0 <= fb.breakeven_gross_income_eur <= 44000.0

    # 3. Structural financing items from M03
    assert fb.gross_ubr_outlays_pct_gdp == pytest.approx(30.0, abs=0.5)
    assert fb.delta_irpf_collections_pct_gdp == pytest.approx(22.50, abs=0.5)
    assert fb.dual_pillar_pension_savings_pct_gdp == pytest.approx(5.80, abs=0.1)
    assert fb.abolished_non_contributory_welfare_pct_gdp == pytest.approx(0.95, abs=0.1)
    assert fb.ieca_compute_withholding_pct_gdp == pytest.approx(1.60, abs=0.1)
    assert fb.corporate_automation_levy_pct_gdp == pytest.approx(1.20, abs=0.1)
    assert fb.consumption_wealth_tax_adjustments_pct_gdp == pytest.approx(1.10, abs=0.1)
    assert fb.no_loser_guarantee_cost_pct_gdp <= 0.50  # <0.5% GDP

    # 4. Decile winner/loser profile
    deciles = result.decile_rows
    assert len(deciles) == 10
    # Decile 1 should gain > 80% disposable income
    assert deciles[0].delta_disposable_income_pct > 80.0
    assert deciles[0].net_winner_share_pct >= 99.0
    # Deciles 1-5 must have 0.0% net losers due to No-Loser Guarantee
    for d in deciles[:5]:
        assert d.net_loser_share_pct == pytest.approx(0.0, abs=0.1)
    # Deciles 1-7 must be net gainers on average
    for d in deciles[:7]:
        assert d.delta_disposable_income_eur > 0.0

    # 5. Poverty and inequality impact (RQ-M09-01)
    b_dist = result.baseline_distribution
    p_dist = result.post_distribution

    # Severe poverty (<40% BHC) reduced by > 80%
    assert p_dist.bhc_severe_40.p0_headcount_ratio < b_dist.bhc_severe_40.p0_headcount_ratio * 0.20
    # Child poverty significantly reduced
    assert p_dist.bhc_child_poverty_rate < b_dist.bhc_child_poverty_rate * 0.50
    # Gini coefficient reduction: 6.2 - 12.0 Gini points
    gini_delta = (p_dist.gini_coefficient - b_dist.gini_coefficient) * 100.0
    assert -12.0 <= gini_delta <= -6.0

    # 6. Housing overburden impact
    h_metrics = result.housing_metrics
    # Private renter overburden drops substantially
    assert h_metrics.private_renter_overburden_post_pct < h_metrics.private_renter_overburden_baseline_pct * 0.50


def test_simulation_export_json_validity(tmp_path: Path):
    engine = MicrosimulationEngine()
    result = engine.run_simulation(tier=UBRTier.TIER_B, scenario="S2")

    export_file = tmp_path / "test_sim.json"
    from ubr.microsim.export import export_microsim_json
    export_microsim_json(result, export_file)

    assert export_file.exists()
    with open(export_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data["metadata"]["tier"] == "B"
    assert data["metadata"]["scenario"] == "S2"
    assert "fiscal_bridge" in data
    assert "poverty_and_inequality" in data
    assert "housing" in data
    assert len(data["deciles"]) == 10
    assert data["fiscal_bridge"]["is_budget_neutral"] is True
