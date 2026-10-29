"""Export and Formatting Functions for Microsimulation Results (Track 2)."""
from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path
from typing import Any

from ubr.microsim.engine import SimulationRunResult


def export_microsim_json(result: SimulationRunResult, output_path: str | Path) -> None:
    """Export simulation results to a JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = {
        "metadata": {
            "tier": result.tier,
            "scenario": result.scenario,
            "rent_stabilizers_active": result.rent_stabilizers_active,
            "no_loser_guarantee_active": result.no_loser_guarantee_active,
            "behavioral_eti_active": result.behavioral_eti_active,
            "total_population": result.total_population,
            "total_households": result.total_households,
            "total_adults": result.total_adults,
            "total_minors": result.total_minors,
        },
        "fiscal_bridge": {
            "spain_gdp_eur": result.fiscal_bridge.spain_gdp_eur,
            "gross_ubr_outlays_eur": result.fiscal_bridge.gross_ubr_outlays_eur,
            "gross_ubr_outlays_pct_gdp": result.fiscal_bridge.gross_ubr_outlays_pct_gdp,
            "baseline_ai_tax_erosion_eur": result.fiscal_bridge.baseline_ai_tax_erosion_eur,
            "baseline_ai_tax_erosion_pct_gdp": result.fiscal_bridge.baseline_ai_tax_erosion_pct_gdp,
            "no_loser_guarantee_cost_eur": result.fiscal_bridge.no_loser_guarantee_cost_eur,
            "no_loser_guarantee_cost_pct_gdp": result.fiscal_bridge.no_loser_guarantee_cost_pct_gdp,
            "total_commitments_eur": result.fiscal_bridge.total_commitments_eur,
            "total_commitments_pct_gdp": result.fiscal_bridge.total_commitments_pct_gdp,
            "delta_irpf_collections_eur": result.fiscal_bridge.delta_irpf_collections_eur,
            "delta_irpf_collections_pct_gdp": result.fiscal_bridge.delta_irpf_collections_pct_gdp,
            "dual_pillar_pension_savings_eur": result.fiscal_bridge.dual_pillar_pension_savings_eur,
            "dual_pillar_pension_savings_pct_gdp": result.fiscal_bridge.dual_pillar_pension_savings_pct_gdp,
            "abolished_non_contributory_welfare_eur": result.fiscal_bridge.abolished_non_contributory_welfare_eur,
            "abolished_non_contributory_welfare_pct_gdp": result.fiscal_bridge.abolished_non_contributory_welfare_pct_gdp,
            "ieca_compute_withholding_eur": result.fiscal_bridge.ieca_compute_withholding_eur,
            "ieca_compute_withholding_pct_gdp": result.fiscal_bridge.ieca_compute_withholding_pct_gdp,
            "corporate_automation_levy_eur": result.fiscal_bridge.corporate_automation_levy_eur,
            "corporate_automation_levy_pct_gdp": result.fiscal_bridge.corporate_automation_levy_pct_gdp,
            "consumption_wealth_tax_adjustments_eur": result.fiscal_bridge.consumption_wealth_tax_adjustments_eur,
            "consumption_wealth_tax_adjustments_pct_gdp": result.fiscal_bridge.consumption_wealth_tax_adjustments_pct_gdp,
            "total_structural_financing_eur": result.fiscal_bridge.total_structural_financing_eur,
            "total_structural_financing_pct_gdp": result.fiscal_bridge.total_structural_financing_pct_gdp,
            "consolidated_net_balance_eur": result.fiscal_bridge.consolidated_net_balance_eur,
            "consolidated_net_balance_pct_gdp": result.fiscal_bridge.consolidated_net_balance_pct_gdp,
            "is_budget_neutral": result.fiscal_bridge.is_budget_neutral,
            "breakeven_gross_income_eur": result.fiscal_bridge.breakeven_gross_income_eur,
            "breakeven_percentile": result.fiscal_bridge.breakeven_percentile,
        },
        "poverty_and_inequality": {
            "baseline": {
                "median_eq_bhc": result.baseline_distribution.median_equivalized_income_bhc,
                "median_eq_ahc": result.baseline_distribution.median_equivalized_income_ahc,
                "gini": result.baseline_distribution.gini_coefficient,
                "s80_s20": result.baseline_distribution.s80_s20_ratio,
                "theil": result.baseline_distribution.theil_index,
                "atkinson_e1": result.baseline_distribution.atkinson_index_e1,
                "bhc_floating_60_p0": result.baseline_distribution.bhc_floating_60.p0_headcount_ratio,
                "bhc_severe_40_p0": result.baseline_distribution.bhc_severe_40.p0_headcount_ratio,
                "bhc_child_poverty": result.baseline_distribution.bhc_child_poverty_rate,
                "ahc_floating_60_p0": result.baseline_distribution.ahc_floating_60.p0_headcount_ratio,
                "ahc_severe_40_p0": result.baseline_distribution.ahc_severe_40.p0_headcount_ratio,
                "ahc_child_poverty": result.baseline_distribution.ahc_child_poverty_rate,
                "individualized_poverty": result.baseline_distribution.individualized_poverty_rate,
                "impairment_adjusted_poverty": result.baseline_distribution.impairment_adjusted_poverty_rate,
            },
            "post_reform": {
                "median_eq_bhc": result.post_distribution.median_equivalized_income_bhc,
                "median_eq_ahc": result.post_distribution.median_equivalized_income_ahc,
                "gini": result.post_distribution.gini_coefficient,
                "s80_s20": result.post_distribution.s80_s20_ratio,
                "theil": result.post_distribution.theil_index,
                "atkinson_e1": result.post_distribution.atkinson_index_e1,
                "bhc_floating_60_p0": result.post_distribution.bhc_floating_60.p0_headcount_ratio,
                "bhc_anchored_60_p0": result.post_distribution.bhc_anchored_60.p0_headcount_ratio,
                "bhc_severe_40_p0": result.post_distribution.bhc_severe_40.p0_headcount_ratio,
                "bhc_child_poverty": result.post_distribution.bhc_child_poverty_rate,
                "ahc_floating_60_p0": result.post_distribution.ahc_floating_60.p0_headcount_ratio,
                "ahc_anchored_60_p0": result.post_distribution.ahc_anchored_60.p0_headcount_ratio,
                "ahc_severe_40_p0": result.post_distribution.ahc_severe_40.p0_headcount_ratio,
                "ahc_child_poverty": result.post_distribution.ahc_child_poverty_rate,
                "individualized_poverty": result.post_distribution.individualized_poverty_rate,
                "impairment_adjusted_poverty": result.post_distribution.impairment_adjusted_poverty_rate,
            },
        },
        "housing": asdict(result.housing_metrics),
        "deciles": [asdict(row) for row in result.decile_rows],
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def render_fiscal_bridge_table(result: SimulationRunResult) -> str:
    """Render the General Government Fiscal Bridge table."""
    fb = result.fiscal_bridge
    lines = [
        f"=== Administraciones Públicas Consolidated Gross-to-Net Fiscal Bridge ===",
        f"Configuration: Tier {result.tier} | Scenario {result.scenario} | GDP: €{fb.spain_gdp_eur/1e9:,.0f} Billion",
        "-" * 84,
        f"{'Component':<50} {'Amount (€B)':>14} {'% GDP':>14}",
        "-" * 84,
        f"{'A. Gross Commitments & Outlays':<50} {'':>14} {'':>14}",
        f"{'   1. Gross UBR Cash Disbursements':<50} {-fb.gross_ubr_outlays_eur/1e9:>14.2f} {-fb.gross_ubr_outlays_pct_gdp:>13.2f}%",
        f"{'   2. Baseline AI Labor Tax Base Erosion':<50} {-fb.baseline_ai_tax_erosion_eur/1e9:>14.2f} {-fb.baseline_ai_tax_erosion_pct_gdp:>13.2f}%",
        f"{'   3. No-Loser Guarantee (Complemento Neutralidad)':<50} {-fb.no_loser_guarantee_cost_eur/1e9:>14.2f} {-fb.no_loser_guarantee_cost_pct_gdp:>13.2f}%",
        f"{'   Total Gross Commitments':<50} {-fb.total_commitments_eur/1e9:>14.2f} {-fb.total_commitments_pct_gdp:>13.2f}%",
        f"{'B. Structural Financing Sources':<50} {'':>14} {'':>14}",
        f"{'   4. Net IRPF Restructuring Increment (euro 1)':<50} {+fb.delta_irpf_collections_eur/1e9:>14.2f} {+fb.delta_irpf_collections_pct_gdp:>13.2f}%",
        f"{'   5. Dual-Pillar Contributory Pension Offsets':<50} {+fb.dual_pillar_pension_savings_eur/1e9:>14.2f} {+fb.dual_pillar_pension_savings_pct_gdp:>13.2f}%",
        f"{'   6. Abolished Non-Contributory Welfare (IMV/PNC)':<50} {+fb.abolished_non_contributory_welfare_eur/1e9:>14.2f} {+fb.abolished_non_contributory_welfare_pct_gdp:>13.2f}%",
        f"{'   7. IECA B2B AI Compute Withholding (D-007)':<50} {+fb.ieca_compute_withholding_eur/1e9:>14.2f} {+fb.ieca_compute_withholding_pct_gdp:>13.2f}%",
        f"{'   8. Corporate Automation Surplus Levies':<50} {+fb.corporate_automation_levy_eur/1e9:>14.2f} {+fb.corporate_automation_levy_pct_gdp:>13.2f}%",
        f"{'   9. Consumption & Wealth Tax Adjustments':<50} {+fb.consumption_wealth_tax_adjustments_eur/1e9:>14.2f} {+fb.consumption_wealth_tax_adjustments_pct_gdp:>13.2f}%",
        f"{'   Total Structural Financing':<50} {+fb.total_structural_financing_eur/1e9:>14.2f} {+fb.total_structural_financing_pct_gdp:>13.2f}%",
        "-" * 84,
        f"{'Consolidated Net Balance':<50} {fb.consolidated_net_balance_eur/1e9:>+14.2f} {fb.consolidated_net_balance_pct_gdp:>+13.2f}%",
        f"{'Status-Quo Budget Neutrality':<50} {('ACHIEVED (PASS)' if fb.is_budget_neutral else 'DEFICIT (FAIL)'):>29}",
        f"{'Breakeven Income Threshold':<50} {f'€{fb.breakeven_gross_income_eur:,.0f} (p{fb.breakeven_percentile:.1f})':>29}",
        "-" * 84,
    ]
    return "\n".join(lines)


def render_decile_table(result: SimulationRunResult) -> str:
    """Render decile-by-decile winner/loser and income shift table."""
    lines = [
        f"=== Household Disposable Income and Winner/Loser Profile by Decile ===",
        f"Configuration: Tier {result.tier} | Scenario {result.scenario}",
        "-" * 96,
        f"{'Decile':<8} {'Base Disp (€)':>14} {'Post Disp (€)':>14} {'Delta (€)':>14} {'Delta (%)':>12} {'Winners':>12} {'Losers':>12}",
        "-" * 96,
    ]
    for row in result.decile_rows:
        lines.append(
            f"{row.decile:<8} "
            f"€{row.mean_baseline_disposable_income_eur:>12,.0f} "
            f"€{row.mean_post_disposable_income_eur:>12,.0f} "
            f"€{row.delta_disposable_income_eur:>+12,.0f} "
            f"{row.delta_disposable_income_pct:>+11.1f}% "
            f"{row.net_winner_share_pct:>11.1f}% "
            f"{row.net_loser_share_pct:>11.1f}%"
        )
    lines.append("-" * 96)
    lines.append(f"Breakeven Point: p{result.fiscal_bridge.breakeven_percentile:.1f} (~€{result.fiscal_bridge.breakeven_gross_income_eur:,.0f}/year)")
    return "\n".join(lines)


def render_poverty_table(result: SimulationRunResult) -> str:
    """Render comprehensive poverty, inequality, and housing table."""
    b = result.baseline_distribution
    p = result.post_distribution
    h = result.housing_metrics

    lines = [
        f"=== Poverty, Inequality, and Housing Living Standards Impact ===",
        f"Configuration: Tier {result.tier} | Scenario {result.scenario}",
        "-" * 90,
        f"{'Metric':<42} {'Baseline':>15} {'Post-Reform':>15} {'Delta':>14}",
        "-" * 90,
        f"{'Median Equivalized Income (BHC)':<42} {f'€{b.median_equivalized_income_bhc:,.0f}':>15} {f'€{p.median_equivalized_income_bhc:,.0f}':>15} {f'€{p.median_equivalized_income_bhc - b.median_equivalized_income_bhc:+,.0f}':>14}",
        f"{'Severe Poverty (<40% BHC P0)':<42} {f'{b.bhc_severe_40.p0_headcount_ratio:.1%}':>15} {f'{p.bhc_severe_40.p0_headcount_ratio:.1%}':>15} {f'{(p.bhc_severe_40.p0_headcount_ratio - b.bhc_severe_40.p0_headcount_ratio)*100:+.1f} pp':>14}",
        f"{'Child Monetary Poverty (BHC)':<42} {f'{b.bhc_child_poverty_rate:.1%}':>15} {f'{p.bhc_child_poverty_rate:.1%}':>15} {f'{(p.bhc_child_poverty_rate - b.bhc_child_poverty_rate)*100:+.1f} pp':>14}",
        f"{'Anchored Poverty (60% baseline BHC)':<42} {f'{b.bhc_anchored_60.p0_headcount_ratio:.1%}':>15} {f'{p.bhc_anchored_60.p0_headcount_ratio:.1%}':>15} {f'{(p.bhc_anchored_60.p0_headcount_ratio - b.bhc_anchored_60.p0_headcount_ratio)*100:+.1f} pp':>14}",
        f"{'Floating Poverty (60% post BHC)':<42} {f'{b.bhc_floating_60.p0_headcount_ratio:.1%}':>15} {f'{p.bhc_floating_60.p0_headcount_ratio:.1%}':>15} {f'{(p.bhc_floating_60.p0_headcount_ratio - b.bhc_floating_60.p0_headcount_ratio)*100:+.1f} pp':>14}",
        f"{'After-Housing-Cost Severe Poverty (AHC)':<42} {f'{b.ahc_severe_40.p0_headcount_ratio:.1%}':>15} {f'{p.ahc_severe_40.p0_headcount_ratio:.1%}':>15} {f'{(p.ahc_severe_40.p0_headcount_ratio - b.ahc_severe_40.p0_headcount_ratio)*100:+.1f} pp':>14}",
        f"{'After-Housing-Cost Child Poverty (AHC)':<42} {f'{b.ahc_child_poverty_rate:.1%}':>15} {f'{p.ahc_child_poverty_rate:.1%}':>15} {f'{(p.ahc_child_poverty_rate - b.ahc_child_poverty_rate)*100:+.1f} pp':>14}",
        "-" * 90,
        f"{'Gini Coefficient':<42} {f'{b.gini_coefficient:.3f}':>15} {f'{p.gini_coefficient:.3f}':>15} {f'{(p.gini_coefficient - b.gini_coefficient)*100:+.1f} pts':>14}",
        f"{'S80/S20 Ratio':<42} {f'{b.s80_s20_ratio:.2f}':>15} {f'{p.s80_s20_ratio:.2f}':>15} {f'{p.s80_s20_ratio - b.s80_s20_ratio:+.2f}':>14}",
        f"{'Theil Entropy Index':<42} {f'{b.theil_index:.3f}':>15} {f'{p.theil_index:.3f}':>15} {f'{p.theil_index - b.theil_index:+.3f}':>14}",
        f"{'Atkinson Index (e=1.0)':<42} {f'{b.atkinson_index_e1:.3f}':>15} {f'{p.atkinson_index_e1:.3f}':>15} {f'{p.atkinson_index_e1 - b.atkinson_index_e1:+.3f}':>14}",
        "-" * 90,
        f"{'Individualized Hidden Poverty (Ponthieux)':<42} {f'{b.individualized_poverty_rate:.1%}':>15} {f'{p.individualized_poverty_rate:.1%}':>15} {f'{(p.individualized_poverty_rate - b.individualized_poverty_rate)*100:+.1f} pp':>14}",
        f"{'Impairment-Adjusted Poverty (Zaidi)':<42} {f'{b.impairment_adjusted_poverty_rate:.1%}':>15} {f'{p.impairment_adjusted_poverty_rate:.1%}':>15} {f'{(p.impairment_adjusted_poverty_rate - b.impairment_adjusted_poverty_rate)*100:+.1f} pp':>14}",
        f"{'Housing-Cost Overburden Rate (All)':<42} {f'{h.overburden_rate_baseline_pct:.1f}%':>15} {f'{h.overburden_rate_post_pct:.1f}%':>15} {f'{h.overburden_rate_post_pct - h.overburden_rate_baseline_pct:+.1f} pp':>14}",
        f"{'Private Renter Housing Overburden':<42} {f'{h.private_renter_overburden_baseline_pct:.1f}%':>15} {f'{h.private_renter_overburden_post_pct:.1f}%':>15} {f'{h.private_renter_overburden_post_pct - h.private_renter_overburden_baseline_pct:+.1f} pp':>14}",
        "-" * 90,
    ]
    return "\n".join(lines)
