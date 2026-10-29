"""Comprehensive Tests for Track 3: Currency-Union HANK Model & EU Fiscal Rules (M04, M16, M17)."""
from __future__ import annotations

import json
from pathlib import Path
import pytest

from ubr.macro.parameters import MacroParameters
from ubr.macro.hank_model import (
    CurrencyUnionHANKModel,
    HANKSimulationResult,
    MacroStateSnapshot,
)
from ubr.macro.fiscal_rules import (
    AnnualFiscalComplianceRecord,
    EUFiscalGovernanceValidator,
    FiscalRulesEvaluationResult,
)
from ubr.macro.sovereign_fund import (
    SovereignFundAccumulationModel,
    SovereignFundSimulationResult,
    SovereignFundYearSnapshot,
)
from ubr.macro.stress_tests import (
    MacroStressTestHarness,
    StressTestBatteryResult,
    StressTestOutcome,
)
from ubr.macro.export import (
    export_fiscal_rules_json,
    export_hank_json,
    export_sovereign_fund_json,
    export_stress_tests_json,
    render_fiscal_rules_table,
    render_irf_table,
    render_sovereign_fund_table,
    render_stress_battery_table,
)
from ubr.cli import main


def test_macro_parameters_initialization():
    p = MacroParameters()
    assert p.spain_gdp_baseline_eur == 1.5e12
    assert p.baseline_debt_to_gdp == 1.05
    assert p.baseline_sovereign_spread_bps == 80.0
    assert p.hand_to_mouth_share == 0.35
    assert p.ricardian_share == 0.65
    assert p.target_inflation_annual == 0.02
    assert p.npe_max_growth_annual == 0.028
    assert p.control_account_cumulative_debit_ceiling_pct_gdp == 0.60
    assert p.windfall_threshold_multiplier == 1.20


def test_hank_irf_baseline_tier_b_s2():
    model = CurrencyUnionHANKModel()
    res = model.simulate(tier="B", scenario="S2", horizon_quarters=20)

    assert isinstance(res, HANKSimulationResult)
    assert len(res.quarters) == 20
    assert res.tier == "B"
    assert res.scenario == "S2"

    # RQ-M04-01: Core non-tradable inflation stays within +/- 0.3 pp of ECB 2.0% target
    assert res.is_ecb_target_preserved is True
    assert res.non_tradable_inflation_deviation_from_target_pp <= 0.30

    # RQ-M04-02: Peak sovereign spread remains bounded (<= 85 bps under baseline)
    assert res.is_spread_stable is True
    assert res.peak_sovereign_spread_bps <= 85.0

    # Dynamic convergence
    first_q = res.quarters[0]
    last_q = res.quarters[-1]
    assert first_q.quarter == 1
    assert last_q.quarter == 20
    assert first_q.headline_inflation_annual_pct > 1.80
    assert last_q.headline_inflation_annual_pct < 1.70  # Tradable AI productivity disinflation
    assert 1.0 <= res.gdp_multiplier <= 1.3


def test_hank_irf_cross_scenarios():
    model = CurrencyUnionHANKModel()
    res_s1 = model.simulate(tier="B", scenario="S1")
    res_s2 = model.simulate(tier="B", scenario="S2")
    res_s3 = model.simulate(tier="B", scenario="S3")

    # All three scenarios preserve ECB inflation target within +/- 0.3 pp when rent stabilizers are active
    assert res_s1.is_ecb_target_preserved is True
    assert res_s2.is_ecb_target_preserved is True
    assert res_s3.is_ecb_target_preserved is True

    # S3 features highest tradable productivity gains
    assert res_s3.quarters[-1].tradable_inflation_annual_pct < res_s1.quarters[-1].tradable_inflation_annual_pct


def test_hank_irf_rent_stabilizers_impact():
    model = CurrencyUnionHANKModel()
    with_stab = model.simulate(tier="B", scenario="S2", enable_rent_stabilizers=True)
    without_stab = model.simulate(tier="B", scenario="S2", enable_rent_stabilizers=False)

    # Without rent stabilizers (D-008 disabled), non-tradable inflation is higher due to landlord rent capture
    assert without_stab.peak_non_tradable_inflation_pct > with_stab.peak_non_tradable_inflation_pct


def test_eu_fiscal_rules_npe_compliance():
    validator = EUFiscalGovernanceValidator()
    res = validator.evaluate_trajectory(tier="B", scenario="S2", years_horizon=5)

    assert isinstance(res, FiscalRulesEvaluationResult)
    assert len(res.years) == 5
    assert res.is_fully_compliant_eu_framework is True
    assert res.tpi_eligibility_preserved is True
    assert res.max_cumulative_debit_pct_gdp <= 0.60

    for yr in res.years:
        assert yr.npe_compliance is True
        assert yr.net_primary_expenditure_growth_pct <= 2.80
        assert yr.annual_control_account_debit_pct_gdp == 0.0
        assert yr.cumulative_control_account_debit_pct_gdp == 0.0
        assert yr.edp_procedure_risk is False


def test_eu_fiscal_rules_unfinanced_breach():
    validator = EUFiscalGovernanceValidator()
    # Unfinanced counterfactual: gross UBR without discretionary revenue netting (MDI)
    res_unfinanced = validator.evaluate_trajectory(
        tier="B",
        scenario="S2",
        pair_with_discretionary_revenue=False,
    )

    assert res_unfinanced.is_fully_compliant_eu_framework is False
    assert res_unfinanced.tpi_eligibility_preserved is False
    assert res_unfinanced.max_cumulative_debit_pct_gdp > 10.0  # Excessive debit
    assert any(yr.edp_procedure_risk for yr in res_unfinanced.years)


def test_sovereign_ai_dividend_fund_accumulation():
    fund_model = SovereignFundAccumulationModel()
    res = fund_model.simulate_15_year_path(scenario="S2", horizon_years=15)

    assert isinstance(res, SovereignFundSimulationResult)
    assert len(res.snapshots) == 15
    assert res.portfolio_real_return_pct == pytest.approx(4.5, rel=1e-3)

    # In early years (Y1-Y3), windfall trigger is not activated (EBE < 120% of baseline trend)
    assert res.snapshots[0].is_windfall_triggered is False
    assert res.snapshots[1].is_windfall_triggered is False
    assert res.snapshots[2].is_windfall_triggered is False

    # In later years, windfall is triggered
    assert res.snapshots[4].is_windfall_triggered is True

    # Statutory lock: no dividend disbursements before Year 8
    for s in res.snapshots[:7]:
        assert s.annual_dividend_payout_eur == 0.0

    # Dividends paid from Year 8 onwards
    assert res.snapshots[7].annual_dividend_payout_eur > 0.0
    assert res.snapshots[-1].annual_dividend_payout_eur > 10.0e9  # > €10 Billion/yr

    # RQ-M16-03 target: accumulated endowment of 15-20% of GDP by Year 15
    assert res.target_15yr_achieved is True
    assert 15.0 <= res.terminal_assets_pct_gdp <= 20.0
    assert res.terminal_assets_eur > 450.0e9  # > €450 Billion accumulated assets


def test_compound_tail_risk_stress_battery():
    harness = MacroStressTestHarness()
    res = harness.run_battery(tier="B", scenario="S2")

    assert isinstance(res, StressTestBatteryResult)
    assert len(res.outcomes) == 4
    assert res.all_tests_contained_or_resilient is True
    assert res.circuit_breakers_effective is True

    stress_ids = [o.stress_id for o in res.outcomes]
    assert "STRESS_1" in stress_ids
    assert "STRESS_2" in stress_ids
    assert "STRESS_3" in stress_ids
    assert "STRESS_4" in stress_ids

    for o in res.outcomes:
        assert o.circuit_breaker_activated is True
        assert len(o.circuit_breaker_name) > 0
        assert o.system_resilience_status in ("RESILIENT", "CONTAINED")
        assert o.edp_procedure_triggered is False


def test_macro_export_helpers(tmp_path: Path):
    model = CurrencyUnionHANKModel()
    hank_res = model.simulate(tier="B", scenario="S2")
    validator = EUFiscalGovernanceValidator()
    npe_res = validator.evaluate_trajectory(tier="B", scenario="S2")
    fund = SovereignFundAccumulationModel()
    fund_res = fund.simulate_15_year_path(scenario="S2")
    harness = MacroStressTestHarness()
    stress_res = harness.run_battery(tier="B", scenario="S2")

    p_hank = tmp_path / "hank.json"
    p_npe = tmp_path / "npe.json"
    p_fund = tmp_path / "fund.json"
    p_stress = tmp_path / "stress.json"

    export_hank_json(hank_res, p_hank)
    export_fiscal_rules_json(npe_res, p_npe)
    export_sovereign_fund_json(fund_res, p_fund)
    export_stress_tests_json(stress_res, p_stress)

    assert p_hank.exists()
    assert p_npe.exists()
    assert p_fund.exists()
    assert p_stress.exists()

    with open(p_hank, encoding="utf-8") as f:
        data = json.load(f)
        assert data["metadata"]["tier"] == "B"
        assert len(data["quarterly_irf"]) == 20

    with open(p_npe, encoding="utf-8") as f:
        data = json.load(f)
        assert data["metadata"]["is_fully_compliant_eu_framework"] is True
        assert len(data["years"]) == 5

    with open(p_fund, encoding="utf-8") as f:
        data = json.load(f)
        assert data["metadata"]["target_15yr_achieved"] is True
        assert len(data["snapshots"]) == 15

    with open(p_stress, encoding="utf-8") as f:
        data = json.load(f)
        assert data["metadata"]["all_tests_contained_or_resilient"] is True
        assert len(data["outcomes"]) == 4

    # Test table renderers
    assert "Currency-Union HANK" in render_irf_table(hank_res)
    assert "Regulation 2024/1263" in render_fiscal_rules_table(npe_res)
    assert "Fondo Soberano" in render_sovereign_fund_table(fund_res)
    assert "Compound Tail-Risk" in render_stress_battery_table(stress_res)


def test_cli_macro_commands(capsys, tmp_path: Path):
    # Test ubr macro irf
    ret = main(["macro", "irf", "--tier", "B", "--scenario", "S2"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "Currency-Union HANK Quarterly Impulse Response Functions" in captured.out
    assert "ECB Inflation Target Preserved: YES" in captured.out

    # Test ubr macro npe
    ret = main(["macro", "npe", "--tier", "B", "--scenario", "S2"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "Regulation 2024/1263" in captured.out
    assert "FULLY COMPLIANT" in captured.out

    # Test ubr macro fund
    ret = main(["macro", "fund", "--scenario", "S2"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "Fondo Soberano de Renta Básica" in captured.out
    assert "ACHIEVED (PASS)" in captured.out

    # Test ubr macro stress
    ret = main(["macro", "stress", "--tier", "B", "--scenario", "S2"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "ALL TESTS RESILIENT OR CONTAINED" in captured.out

    # Test ubr macro summary
    ret = main(["macro", "summary"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "Currency-Union HANK" in captured.out
    assert "Regulation 2024/1263" in captured.out
    assert "Fondo Soberano" in captured.out
    assert "Compound Tail-Risk" in captured.out
