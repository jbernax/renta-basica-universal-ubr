"""Comprehensive Test Suite for Track 4: Pilot Protocol, GIS, Econometrics & AEA PAP (M05, M08, M10, M15)."""
from __future__ import annotations

import json
from pathlib import Path
import pytest

from ubr.pilot.clusters import (
    ClusterRegistry,
    MobilityMatrix,
    SpatialCluster,
    haversine_km,
)
from ubr.pilot.power import (
    MDEResult,
    PowerAnalysisResult,
    TwoStagePowerCalculator,
)
from ubr.pilot.econometrics import (
    BunchingEstimator,
    BunchingResult,
    DecompositionResult,
    LifeCycleDecomposition,
    SDIDResult,
    SpatialSpilloverEstimator,
    SpilloverEstimationResult,
    SyntheticDiffInDiff,
)
from ubr.pilot.data_linkage import (
    BudgetModel,
    DataSpineConfig,
    LinkageAuditResult,
    RegisterLinkageProtocol,
)
from ubr.pilot.pap import (
    AEAPreAnalysisPlan,
    PreAnalysisPlanGenerator,
)
from ubr.pilot.export import (
    export_bunching_json,
    export_clusters_json,
    export_pap_json,
    export_power_json,
    export_sdid_json,
    render_bunching_table,
    render_clusters_table,
    render_decomposition_table,
    render_pilot_summary,
    render_power_table,
    render_sdid_table,
)
from ubr.cli import main


def test_cluster_registry_initialization():
    registry = ClusterRegistry(seed=42)
    assert len(registry.clusters) == 70

    # Metropolitan vs Non-Metropolitan
    metro = [c for c in registry.clusters if c.is_metropolitan]
    nonmetro = [c for c in registry.clusters if not c.is_metropolitan]
    assert len(metro) == 40
    assert len(nonmetro) == 30

    # Treated vs Control
    treated = [c for c in registry.clusters if c.is_treated]
    control = [c for c in registry.clusters if not c.is_treated]
    assert len(treated) == 35
    assert len(control) == 35

    # Saturation distribution among treated
    sat_33 = [c for c in treated if abs(c.saturation_rate - 0.33) < 0.01]
    sat_66 = [c for c in treated if abs(c.saturation_rate - 0.66) < 0.01]
    sat_100 = [c for c in treated if abs(c.saturation_rate - 1.00) < 0.01]
    assert len(sat_33) == 12
    assert len(sat_66) == 12
    assert len(sat_100) == 11

    # FUA Commuting containment >= 80%
    for c in metro:
        assert c.internal_commuting_ratio >= 0.80
        assert c.fua_name in ["Madrid", "Barcelona", "Valencia", "Seville", "Bilbao", "Malaga", "Zaragoza"]

    # Non-metro buffer zones >= 2.0 km
    for c in nonmetro:
        assert c.buffer_radius_km >= 2.0
        assert c.fua_name is None


def test_covariate_balance():
    registry = ClusterRegistry(seed=42)
    bal = registry.balance_summary()
    assert len(bal) == 6

    # Normalized differences should all be below 0.20
    for var_name, stats in bal.items():
        assert stats["is_balanced"] is True
        assert abs(stats["normalized_difference"]) < 0.20


def test_mobility_matrix_structure():
    registry = ClusterRegistry(seed=42)
    mat = registry.mobility_matrix
    assert mat is not None
    assert len(mat.cluster_ids) == 70
    assert len(mat.weights) == 70

    # Row normalization
    for row in mat.weights:
        assert len(row) == 70
        assert abs(sum(row) - 1.0) < 1e-5

    # Distance function
    d = haversine_km(40.4168, -3.7038, 41.3879, 2.1699)
    assert 480.0 < d < 520.0  # Madrid to Barcelona ~505 km

    # Spillover exposure calculation
    cash_map = {c.cluster_id: (900.0 if c.is_treated else 0.0) for c in registry.clusters}
    exp_mad = mat.compute_spillover_exposure("MAD_01", cash_map)
    assert exp_mad > 0.0


def test_two_stage_power_and_mde_thresholds():
    calc = TwoStagePowerCalculator(total_clusters=70, total_sample=20000, icc=0.03)
    res = calc.run_full_power_analysis()

    assert isinstance(res, PowerAnalysisResult)
    assert res.total_clusters == 70
    assert res.total_sample_size == 20000

    # Check key MDE targets from RQ-M10-01
    mde_labor = res.mde_results["Labor Supply Hours (weekly)"]
    assert mde_labor.is_target_met is True
    assert mde_labor.mde_absolute <= 1.20

    mde_rent = res.mde_results["Rental Pass-Through (EUR/mo)"]
    assert mde_rent.is_target_met is True
    assert mde_rent.mde_percent <= 2.80

    mde_health = res.mde_results["Mental Health Index (GHQ-12 SD)"]
    assert mde_health.is_target_met is True
    assert mde_health.mde_absolute <= 0.15

    # Achieved power > 80%
    assert res.monte_carlo_power_achieved["Labor Supply Hours (weekly)"] >= 0.80
    assert res.monte_carlo_power_achieved["Rental Pass-Through (EUR/mo)"] >= 0.80


def test_spatial_spillover_estimation():
    registry = ClusterRegistry(seed=42)
    mat = registry.mobility_matrix
    assert mat is not None

    estimator = SpatialSpilloverEstimator(mat)
    res = estimator.estimate(registry.clusters, outcome_type="labor_supply_hours")

    assert isinstance(res, SpilloverEstimationResult)
    assert -2.0 < res.direct_effect_beta1 < 0.0
    assert res.direct_effect_se > 0.0
    assert res.direct_effect_pvalue < 0.05
    assert res.n_observations > 5000


def test_sdid_rental_pass_through_and_dual_tenure():
    registry = ClusterRegistry(seed=42)
    sdid = SyntheticDiffInDiff(pre_quarters=8, post_quarters=12)
    res = sdid.estimate(registry.clusters)

    assert isinstance(res, SDIDResult)
    assert len(res.quarterly_series) == 20
    assert res.tau_sdid_treatment_effect > 0.0
    assert res.p_value < 0.01

    # Weights normalization
    assert abs(sum(res.unit_weights_omega.values()) - 1.0) < 1e-4
    assert abs(sum(res.time_weights_lambda) - 1.0) < 1e-4

    # Dual-tenure divergence from M05:
    # Active leases locked for 5 years: near-zero pass-through (< 5%)
    # Turnover leases: substantial market pass-through (20-35%)
    assert res.active_contracts_pass_through_pct < 5.0
    assert 20.0 <= res.turnover_contracts_pass_through_pct <= 35.0
    assert res.active_contracts_pass_through_pct < res.turnover_contracts_pass_through_pct


def test_bunching_convex_disregard_and_notch_missing_mass():
    buncher = BunchingEstimator(bin_width=250.0)

    # Arm A: Pure UBR (0% clawback) -> zero excess mass at disregard
    res_a = buncher.estimate(arm="Arm_A", clawback_rate=0.0)
    assert res_a.excess_mass_b == 0.0
    assert res_a.implied_compensated_elasticity == 0.0
    assert res_a.missing_mass_notch_ceiling == 0.0

    # Arm B: 38% clawback -> clear excess mass and notch ceiling missing mass
    res_b = buncher.estimate(arm="Arm_B", clawback_rate=0.38)
    assert res_b.excess_mass_b > 0.0
    assert 0.01 <= res_b.implied_compensated_elasticity <= 0.25
    assert res_b.notch_ceiling_eur > 25000.0
    assert res_b.missing_mass_notch_ceiling > 0.0

    # Arm C: 50% clawback -> higher excess mass and lower notch ceiling
    res_c = buncher.estimate(arm="Arm_C", clawback_rate=0.50)
    assert res_c.excess_mass_b > res_b.excess_mass_b
    assert res_c.notch_ceiling_eur == 25200.0 or res_c.notch_ceiling_eur < res_b.notch_ceiling_eur


def test_life_cycle_structural_decomposition():
    decomposer = LifeCycleDecomposition()
    res = decomposer.decompose(observed_delta_hours=-1.25)

    assert isinstance(res, DecompositionResult)
    assert res.observed_hours_change == -1.25

    # Components sum to total observed change
    total = res.frisch_sabbatical_component + res.permanent_income_wealth_component + res.involuntary_ai_rationing_component
    assert abs(total - (-1.25)) < 1e-3

    # Frisch sabbatical accounts for roughly half of the observed trial reduction
    assert 45.0 <= res.frisch_share_pct <= 60.0

    # Involuntary AI labor rationing accounts for significant portion
    assert 15.0 <= res.involuntary_ai_rationing_share_pct <= 30.0


def test_register_linkage_hmac_and_retention():
    protocol = RegisterLinkageProtocol()

    # Cryptographic HMAC-SHA256 test
    id1 = "12345678Z"
    id2 = "12345678z"
    id3 = "87654321A"

    h1 = protocol.pseudonymize_identifier(id1)
    h2 = protocol.pseudonymize_identifier(id2)
    h3 = protocol.pseudonymize_identifier(id3)

    assert len(h1) == 64
    assert h1 == h2  # Case-insensitive normalization
    assert h1 != h3  # Distinct identities

    # Audit evaluation
    audit = protocol.run_linkage_audit()
    assert isinstance(audit, LinkageAuditResult)
    assert audit.treated_retention_rate_36m > 99.0
    assert audit.control_retention_rate_with_stipend_36m > 98.0
    assert audit.control_retention_rate_without_stipend_counterfactual < 80.0
    assert len(audit.register_records) == 6


def test_pilot_budget_model():
    budget = BudgetModel()
    assert budget.gross_cash_transfers_eur == 480_000_000.0
    assert budget.administration_and_gis_spine_eur == 35_000_000.0
    assert budget.clawback_and_welfare_offsets_eur == -220_000_000.0
    assert budget.net_pilot_cost_eur == 295_000_000.0
    assert abs(budget.net_cost_per_year_eur - (295_000_000.0 / 3.0)) < 1e-3


def test_aea_pre_analysis_plan():
    gen = PreAnalysisPlanGenerator()
    pap = gen.generate_plan()

    assert isinstance(pap, AEAPreAnalysisPlan)
    assert pap.trial_id == "AEARCTR-0014821"
    assert pap.trial_duration_months == 36
    assert len(pap.hypotheses) == 5
    assert len(pap.primary_endpoints) == 5
    assert "spatial_spillover_model" in pap.econometric_equations
    assert "synthetic_diff_in_diff" in pap.econometric_equations
    assert "saez_chetty_convex_bunching" in pap.econometric_equations
    assert "lifecycle_frisch_decomposition" in pap.econometric_equations


def test_export_and_ascii_rendering(tmp_path: Path):
    registry = ClusterRegistry(seed=42)
    calc = TwoStagePowerCalculator()
    p_res = calc.run_full_power_analysis()
    sdid = SyntheticDiffInDiff()
    s_res = sdid.estimate(registry.clusters)
    buncher = BunchingEstimator()
    b_dict = {
        "Arm_A": buncher.estimate("Arm_A", clawback_rate=0.0),
        "Arm_B": buncher.estimate("Arm_B", clawback_rate=0.38),
    }
    decomposer = LifeCycleDecomposition()
    d_res = decomposer.decompose()
    gen = PreAnalysisPlanGenerator()
    pap = gen.generate_plan()
    budget = BudgetModel()

    # JSON exports
    p_clusters = tmp_path / "clusters.json"
    p_power = tmp_path / "power.json"
    p_sdid = tmp_path / "sdid.json"
    p_bunching = tmp_path / "bunching.json"
    p_pap = tmp_path / "pap.json"

    export_clusters_json(registry, p_clusters)
    export_power_json(p_res, p_power)
    export_sdid_json(s_res, p_sdid)
    export_bunching_json(b_dict, p_bunching)
    export_pap_json(pap, p_pap)

    assert p_clusters.exists() and p_clusters.stat().st_size > 0
    assert p_power.exists() and p_power.stat().st_size > 0
    assert p_sdid.exists() and p_sdid.stat().st_size > 0
    assert p_bunching.exists() and p_bunching.stat().st_size > 0
    assert p_pap.exists() and p_pap.stat().st_size > 0

    # ASCII tables
    t1 = render_clusters_table(registry)
    t2 = render_power_table(p_res)
    t3 = render_sdid_table(s_res)
    t4 = render_bunching_table(b_dict)
    t5 = render_decomposition_table(d_res)
    t6 = render_pilot_summary(registry, p_res, s_res, b_dict, d_res, budget)

    assert "J=70 SPATIAL CLUSTER REGISTRY" in t1
    assert "TWO-STAGE RANDOMIZED SATURATION" in t2
    assert "SYNTHETIC DIFFERENCE-IN-DIFFERENCES" in t3
    assert "CONVEX DISREGARD BUNCHING" in t4
    assert "STRUCTURAL LIFE-CYCLE DECOMPOSITION" in t5
    assert "PILOT BLUEPRINT & GIS DASHBOARD" in t6


def test_cli_pilot_subcommands(capsys):
    assert main(["pilot", "clusters"]) == 0
    out = capsys.readouterr().out
    assert "J=70 SPATIAL CLUSTER REGISTRY" in out

    assert main(["pilot", "power"]) == 0
    out = capsys.readouterr().out
    assert "TWO-STAGE RANDOMIZED SATURATION" in out

    assert main(["pilot", "sdid"]) == 0
    out = capsys.readouterr().out
    assert "SYNTHETIC DIFFERENCE-IN-DIFFERENCES" in out

    assert main(["pilot", "bunching"]) == 0
    out = capsys.readouterr().out
    assert "CONVEX DISREGARD BUNCHING" in out

    assert main(["pilot", "decompose"]) == 0
    out = capsys.readouterr().out
    assert "STRUCTURAL LIFE-CYCLE DECOMPOSITION" in out

    assert main(["pilot", "pap"]) == 0
    out = capsys.readouterr().out
    assert "AEA RCT REGISTRY PRE-ANALYSIS PLAN" in out

    assert main(["pilot", "summary"]) == 0
    out = capsys.readouterr().out
    assert "PILOT BLUEPRINT & GIS DASHBOARD" in out
