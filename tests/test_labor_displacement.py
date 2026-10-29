"""Tests for Track 1: Empirical CNO-11 AI Task Exposure and Labor Displacement Scenarios."""
from __future__ import annotations

import json
from pathlib import Path
import pytest

from ubr.labor.cno_taxonomy import CNOTaxonomy, CNOGroup
from ubr.labor.task_exposure import TaskExposureEngine, ExposureScore
from ubr.labor.institutions import SpanishLaborInstitutions
from ubr.labor.scenarios import LaborDisplacementSimulator, ScenarioResult
from ubr.labor.export import export_counterfactual_json


def test_cno_taxonomy_coverage():
    taxonomy = CNOTaxonomy.load_default()
    groups = taxonomy.all_groups()
    assert len(groups) >= 10
    
    # Check that major 1-digit groups 1 through 9 are represented
    major_digits = {g.cno_code[0] for g in groups}
    for digit in "123456789":
        assert digit in major_digits
        
    total_employment = taxonomy.total_employment_fte()
    # Spanish EPA employment in 2024-2026 is approx 21.0 - 22.0 million
    assert 20_000_000 <= total_employment <= 23_000_000
    
    # Check wage bounds
    for g in groups:
        assert g.avg_monthly_gross_wage > 1000
        assert len(g.wage_deciles) == 10
        # Wage deciles must be monotonically increasing
        assert all(g.wage_deciles[i] <= g.wage_deciles[i+1] for i in range(9))


def test_task_exposure_bounds():
    engine = TaskExposureEngine()
    taxonomy = CNOTaxonomy.load_default()
    scores = engine.compute_exposure(taxonomy)
    
    assert len(scores) == len(taxonomy.all_groups())
    for s in scores:
        assert 0.0 <= s.alpha_direct <= 1.0
        assert 0.0 <= s.beta_augmented <= 1.0
        assert 0.0 <= s.net_exposure <= 1.0
        assert s.alpha_direct <= s.beta_augmented  # Augmented exposure is >= direct
        
    # Clerical (Group 4) and Professionals (Group 2) must have higher exposure than Agricultural (Group 6) and Elementary (Group 9)
    clerical_scores = [s.net_exposure for s in scores if s.cno_code.startswith("4")]
    agricultural_scores = [s.net_exposure for s in scores if s.cno_code.startswith("6")]
    elementary_scores = [s.net_exposure for s in scores if s.cno_code.startswith("9")]
    
    avg_clerical = sum(clerical_scores) / len(clerical_scores)
    avg_agri = sum(agricultural_scores) / len(agricultural_scores)
    avg_elem = sum(elementary_scores) / len(elementary_scores)
    
    assert avg_clerical > avg_agri + 0.25
    assert avg_clerical > avg_elem + 0.25


def test_spanish_labor_institutions():
    institutions = SpanishLaborInstitutions()
    
    # Check gross SMI labor cost floor per RD 145/2024
    smi_cost = institutions.gross_smi_cost_floor()
    # SMI is €1,134/mo (14 payments) = €1,323/mo gross + ~31.5% employer SS = ~€1,740/mo
    assert 1700 <= smi_cost <= 1800
    
    # Test displacement vs. wage adjustment around SMI floor
    # When productivity drops below SMI floor, worker is displaced rather than receiving sub-SMI wage
    displaced, wage_adj, inactivity = institutions.evaluate_adjustment(
        wage_level=1400.0,
        productivity_drop=0.25,
        allows_opt_out=False
    )
    assert displaced is True  # extensive margin cliff
    
    # When collective bargaining opt-out (Art. 82.3 ET) applies for higher wages
    displaced_opt, wage_adj_opt, inactivity_opt = institutions.evaluate_adjustment(
        wage_level=3000.0,
        productivity_drop=0.10,
        allows_opt_out=True
    )
    assert displaced_opt is False
    assert wage_adj_opt < 0  # wage reduction allowed via descuelgue


def test_scenarios_s1_s2_s3_macro_arithmetic():
    simulator = LaborDisplacementSimulator()
    taxonomy = CNOTaxonomy.load_default()
    
    # S1: Moderate displacement
    r1 = simulator.run_scenario("S1", taxonomy)
    assert 0.07 <= r1.net_displaced_fte_share <= 0.09  # ~8%
    assert 2.0 <= abs(r1.labor_share_delta_pp) <= 3.0  # -2.5 pp
    assert 0.8 <= r1.baseline_tax_loss_pct_gdp <= 1.2  # ~0.98% of GDP
    
    # S2: Severe displacement
    r2 = simulator.run_scenario("S2", taxonomy)
    assert 0.18 <= r2.net_displaced_fte_share <= 0.22  # ~20%
    assert 6.5 <= abs(r2.labor_share_delta_pp) <= 7.5  # -7.0 pp
    # Check the critical M01/M03/SYN-03-01 figure: ~2.73% of GDP tax erosion (~€41B on €1,500B GDP)
    assert 2.5 <= r2.baseline_tax_loss_pct_gdp <= 3.0
    assert 38.0 <= r2.baseline_tax_loss_billion_eur <= 43.0
    
    # S3: Structural compression
    r3 = simulator.run_scenario("S3", taxonomy)
    assert 0.32 <= r3.net_displaced_fte_share <= 0.38  # ~35%
    assert 14.0 <= abs(r3.labor_share_delta_pp) <= 16.0  # -15.0 pp
    assert 5.0 <= r3.baseline_tax_loss_pct_gdp <= 6.5  # ~5.85% of GDP
    
    # Displaced workers in S2 must exceed S1, and S3 must exceed S2
    assert r1.total_displaced_fte < r2.total_displaced_fte < r3.total_displaced_fte


def test_export_counterfactual_json(tmp_path: Path):
    simulator = LaborDisplacementSimulator()
    taxonomy = CNOTaxonomy.load_default()
    result = simulator.run_scenario("S2", taxonomy)
    
    out_file = tmp_path / "counterfactual_s2.json"
    export_counterfactual_json(result, out_file)
    
    assert out_file.is_file()
    data = json.loads(out_file.read_text(encoding="utf-8"))
    
    assert data["scenario"] == "S2"
    assert "metrics" in data
    assert "occupational_breakdown" in data
    assert "wage_deciles_post" in data
    assert len(data["occupational_breakdown"]) >= 10
    assert len(data["wage_deciles_post"]) == 10
    
    # Check that decile wage post-distribution has lower aggregate wage bill than baseline
    pre_wage_bill = sum(g.avg_monthly_gross_wage * g.fte_employment for g in taxonomy.all_groups()) * 12
    post_wage_bill = data["metrics"]["post_aggregate_wage_bill_eur"]
    assert post_wage_bill < pre_wage_bill


def test_cli_labor_subcommands(capsys, tmp_path: Path):
    from ubr.cli import main
    
    # Test labor summary
    ret_sum = main(["labor", "summary"])
    assert ret_sum == 0
    captured = capsys.readouterr()
    assert "S1" in captured.out
    assert "S2" in captured.out
    assert "S3" in captured.out
    assert "40.95B" in captured.out

    # Test labor occupations
    ret_occ = main(["labor", "occupations"])
    assert ret_occ == 0
    captured_occ = capsys.readouterr()
    assert "21,510,000" in captured_occ.out

    # Test labor simulate with export
    out_json = tmp_path / "test_s2_export.json"
    ret_sim = main(["labor", "simulate", "--scenario", "S2", "--export", str(out_json)])
    assert ret_sim == 0
    assert out_json.is_file()

