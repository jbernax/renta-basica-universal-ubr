"""Export and ASCII Formatting for Currency-Union HANK Model Results (Track 3)."""
from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path
from typing import Any

from ubr.macro.fiscal_rules import FiscalRulesEvaluationResult
from ubr.macro.hank_model import HANKSimulationResult
from ubr.macro.sovereign_fund import SovereignFundSimulationResult
from ubr.macro.stress_tests import StressTestBatteryResult


def export_hank_json(result: HANKSimulationResult, output_path: str | Path) -> None:
    """Export HANK simulation IRFs and summary metrics to a JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "metadata": {
            "tier": result.tier,
            "scenario": result.scenario,
            "rent_stabilizers_active": result.rent_stabilizers_active,
            "stress_test_name": result.stress_test_name,
        },
        "summary_metrics": {
            "peak_non_tradable_inflation_pct": result.peak_non_tradable_inflation_pct,
            "non_tradable_inflation_deviation_from_target_pp": result.non_tradable_inflation_deviation_from_target_pp,
            "peak_sovereign_spread_bps": result.peak_sovereign_spread_bps,
            "terminal_debt_to_gdp_pct": result.terminal_debt_to_gdp_pct,
            "gdp_multiplier": result.gdp_multiplier,
            "is_ecb_target_preserved": result.is_ecb_target_preserved,
            "is_spread_stable": result.is_spread_stable,
        },
        "quarterly_irf": [asdict(q) for q in result.quarters],
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def export_fiscal_rules_json(result: FiscalRulesEvaluationResult, output_path: str | Path) -> None:
    """Export EU Regulation 2024/1263 compliance evaluation to a JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "metadata": {
            "tier": result.tier,
            "scenario": result.scenario,
            "is_fully_compliant_eu_framework": result.is_fully_compliant_eu_framework,
            "max_cumulative_debit_pct_gdp": result.max_cumulative_debit_pct_gdp,
            "tpi_eligibility_preserved": result.tpi_eligibility_preserved,
            "summary_memo": result.summary_memo,
        },
        "years": [asdict(y) for y in result.years],
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def export_sovereign_fund_json(result: SovereignFundSimulationResult, output_path: str | Path) -> None:
    """Export 15-year Sovereign AI Dividend Fund simulation to a JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "metadata": {
            "scenario": result.scenario,
            "horizon_years": result.horizon_years,
            "portfolio_real_return_pct": result.portfolio_real_return_pct,
            "terminal_assets_eur": result.terminal_assets_eur,
            "terminal_assets_pct_gdp": result.terminal_assets_pct_gdp,
            "terminal_annual_dividend_eur": result.terminal_annual_dividend_eur,
            "terminal_annual_dividend_pct_gdp": result.terminal_annual_dividend_pct_gdp,
            "target_15yr_achieved": result.target_15yr_achieved,
        },
        "snapshots": [asdict(s) for s in result.snapshots],
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def export_stress_tests_json(result: StressTestBatteryResult, output_path: str | Path) -> None:
    """Export compound tail-risk stress test battery results to a JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "metadata": {
            "all_tests_contained_or_resilient": result.all_tests_contained_or_resilient,
            "circuit_breakers_effective": result.circuit_breakers_effective,
        },
        "outcomes": [asdict(o) for o in result.outcomes],
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def render_irf_table(result: HANKSimulationResult) -> str:
    """Render quarterly Impulse Response Function table."""
    lines = [
        f"=== Currency-Union HANK Quarterly Impulse Response Functions (IRFs) ===",
        f"Configuration: Tier {result.tier} | Scenario {result.scenario} | Stress: {result.stress_test_name}",
        "-" * 102,
        f"{'Qtr':<5} {'GDP Grw (%)':>12} {'OutGap (%)':>11} {'CPI (%)':>9} {'Non-Trad (%)':>13} {'ECB Rate (%)':>13} {'Real Rate (%)':>14} {'Spread (bps)':>13} {'Debt (%GDP)':>12}",
        "-" * 102,
    ]
    for s in result.quarters:
        if s.quarter <= 12 or s.quarter == 20:  # Display first 3 years and terminal quarter
            lines.append(
                f"Q{s.quarter:<3} "
                f"{s.real_gdp_growth_annual_pct:>11.2f}% "
                f"{s.output_gap_pct:>+10.2f}% "
                f"{s.headline_inflation_annual_pct:>8.2f}% "
                f"{s.non_tradable_inflation_annual_pct:>12.2f}% "
                f"{s.ecb_policy_rate_annual_pct:>12.2f}% "
                f"{s.spain_real_rate_annual_pct:>13.2f}% "
                f"{s.sovereign_spread_bps:>12.1f} "
                f"{s.debt_to_gdp_pct:>11.1f}%"
            )
    lines.append("-" * 102)
    lines.append(
        f"ECB Inflation Target Preserved: {'YES (PASS, within ±0.3 pp)' if result.is_ecb_target_preserved else 'NO (FAIL)'} "
        f"| Peak Spread: {result.peak_sovereign_spread_bps:.1f} bps"
    )
    return "\n".join(lines)


def render_fiscal_rules_table(result: FiscalRulesEvaluationResult) -> str:
    """Render EU Regulation 2024/1263 compliance table."""
    lines = [
        f"=== EU Regulation 2024/1263 Net Primary Expenditure & LOEPSF Compliance ===",
        f"Configuration: Tier {result.tier} | Scenario {result.scenario}",
        "-" * 98,
        f"{'Year':<6} {'Gross Exp (€B)':>15} {'MDI Offset (€B)':>16} {'Net Exp Growth':>15} {'Ceiling':>10} {'Control Debit':>15} {'EDP Risk':>14}",
        "-" * 98,
    ]
    for r in result.years:
        lines.append(
            f"Y{r.year:<4} "
            f"€{r.gross_primary_expenditure_eur/1e9:>13.2f} "
            f"€{r.discretionary_revenue_measures_mdi_eur/1e9:>14.2f} "
            f"{r.net_primary_expenditure_growth_pct:>14.2f}% "
            f"{r.npe_ceiling_growth_pct:>9.1f}% "
            f"{r.cumulative_control_account_debit_pct_gdp:>14.2f}% "
            f"{('NO (COMPLIANT)' if not r.edp_procedure_risk else 'YES (BREACH)'):>14}"
        )
    lines.append("-" * 98)
    lines.append(f"European Commission Framework Status: {'FULLY COMPLIANT' if result.is_fully_compliant_eu_framework else 'NON-COMPLIANT'}")
    lines.append(f"ECB Transmission Protection Instrument (TPI) Eligibility: {'PRESERVED' if result.tpi_eligibility_preserved else 'JEOPARDIZED'}")
    lines.append(f"Summary Memo: {result.summary_memo}")
    return "\n".join(lines)


def render_sovereign_fund_table(result: SovereignFundSimulationResult) -> str:
    """Render 15-year sovereign fund accumulation table."""
    lines = [
        f"=== Fondo Soberano de Renta Básica y Dividendos de IA (15-Year Path) ===",
        f"Scenario: {result.scenario} | Real Portfolio Return: {result.portfolio_real_return_pct:.1f}%/yr",
        "-" * 92,
        f"{'Year':<6} {'EBE (€B)':>11} {'Triggered':>11} {'Inflow (€B)':>13} {'Assets (€B)':>14} {'Assets (%GDP)':>14} {'Dividend (€B)':>15}",
        "-" * 92,
    ]
    for s in result.snapshots:
        if s.year in (1, 2, 3, 5, 8, 10, 12, 15):
            lines.append(
                f"Y{s.year:<4} "
                f"€{s.gross_operating_surplus_ebe_eur/1e9:>9.1f} "
                f"{('YES' if s.is_windfall_triggered else 'NO'):>10} "
                f"€{s.annual_inflow_eur/1e9:>11.2f} "
                f"€{s.cumulative_fund_assets_eur/1e9:>12.2f} "
                f"{s.cumulative_fund_assets_pct_gdp:>13.1f}% "
                f"€{s.annual_dividend_payout_eur/1e9:>13.2f}"
            )
    lines.append("-" * 92)
    lines.append(
        f"15-Year Endowment Target (>=15% GDP): {'ACHIEVED (PASS)' if result.target_15yr_achieved else 'UNACHIEVED (FAIL)'} "
        f"| Terminal Capital: €{result.terminal_assets_eur/1e9:,.1f}B ({result.terminal_assets_pct_gdp:.1f}% GDP) "
        f"| Annual Dividend Flow: €{result.terminal_annual_dividend_eur/1e9:,.1f}B/yr"
    )
    return "\n".join(lines)


def render_stress_battery_table(result: StressTestBatteryResult) -> str:
    """Render comparative compound stress-test battery table."""
    lines = [
        f"=== Compound Tail-Risk Stress-Test Battery & Circuit-Breakers (M17) ===",
        "-" * 105,
        f"{'Test ID':<10} {'Stress Name':<42} {'Peak CPI':>9} {'Peak Spread':>13} {'Terminal Debt':>14} {'Status':>12}",
        "-" * 105,
    ]
    for o in result.outcomes:
        lines.append(
            f"{o.stress_id:<10} "
            f"{o.stress_name[:40]:<42} "
            f"{o.peak_inflation_pct:>8.2f}% "
            f"{o.peak_sovereign_spread_bps:>11.1f} bps "
            f"{o.terminal_debt_to_gdp_pct:>13.1f}% "
            f"{o.system_resilience_status:>12}"
        )
        lines.append(f"   └─ Active Circuit-Breaker: {o.circuit_breaker_name}")
    lines.append("-" * 105)
    lines.append(
        f"Overall System Resilience: {'ALL TESTS RESILIENT OR CONTAINED (PASS)' if result.all_tests_contained_or_resilient else 'SYSTEM BREACH (FAIL)'}"
    )
    return "\n".join(lines)
