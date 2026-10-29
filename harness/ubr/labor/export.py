"""Serialization and Export of Counterfactual Labor Distributions for EUROMOD-Spain."""
from __future__ import annotations

import json
from pathlib import Path
from ubr.labor.scenarios import ScenarioResult


def export_counterfactual_json(result: ScenarioResult, output_path: Path | str) -> None:
    """Exports ScenarioResult to a structured JSON file ready for EUROMOD-Spain ingestion."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    data = {
        "scenario": result.scenario,
        "metrics": {
            "total_baseline_fte": result.total_baseline_fte,
            "total_displaced_fte": result.total_displaced_fte,
            "net_displaced_fte_share": result.net_displaced_fte_share,
            "labor_share_delta_pp": result.labor_share_delta_pp,
            "baseline_tax_loss_pct_gdp": result.baseline_tax_loss_pct_gdp,
            "baseline_tax_loss_billion_eur": result.baseline_tax_loss_billion_eur,
            "pre_aggregate_wage_bill_eur": result.pre_aggregate_wage_bill_eur,
            "post_aggregate_wage_bill_eur": result.post_aggregate_wage_bill_eur,
        },
        "tax_drag_by_component": result.tax_drag_by_component,
        "wage_deciles_pre": result.wage_deciles_pre,
        "wage_deciles_post": result.wage_deciles_post,
        "occupational_breakdown": {
            cno: {
                "displaced_fte": count,
                "displacement_share": round(count / (count + (result.total_baseline_fte / len(result.displaced_by_cno))), 4),
            }
            for cno, count in result.displaced_by_cno.items()
        },
        "handoff_metadata": {
            "destination_module": "M03 / M09 / EUROMOD-Spain",
            "statutory_smi_cost_floor_eur": 1739.75,
            "average_tax_wedge": 0.39,
            "spain_gdp_baseline_eur": 1_500_000_000_000.0,
        },
    }
    
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
