"""Command-line interface for `python -m ubr`."""
from __future__ import annotations

import argparse
import json
import sys

from ubr.iterations import (
    IterationError,
    format_id,
    last_checkpoint,
    record_checkpoint,
    resolve_iteration,
    start_iteration,
)
from ubr.metrics import compute_metrics
from ubr.project import ProjectNotFound, find_project
from ubr.report import build_report, status_line
from ubr.reviews import check_reviews
from ubr.scoring import ScoringError, score_history, score_iteration
from ubr.sources import verify_sources
from ubr.stopping import decide
from ubr.validate import validate_plan


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ubr", description="Universal Basic Rent research-plan harness")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("validate", help="Validate plan structure, citations, dependencies and locks")

    it_parser = sub.add_parser("iteration", help="Manage plan improvement iterations")
    it_sub = it_parser.add_subparsers(dest="it_cmd", required=True)
    it_sub.add_parser("start", help="Snapshot plan, build bundle.md and select reviewers")

    rev = sub.add_parser("reviews", help="Inspect or validate reviewer/judge YAML outputs")
    rev_sub = rev.add_subparsers(dest="rev_cmd", required=True)
    rev_check = rev_sub.add_parser("check", help="Validate review YAML files against schemas")
    rev_check.add_argument("iteration", nargs="?", default="latest")
    rev_check.add_argument("--judge", action="store_true", help="Also require judge.yaml to be present and valid")

    src = sub.add_parser("sources", help="Verify sources in plan/sources.yaml")
    src_sub = src.add_subparsers(dest="src_cmd", required=True)
    src_verify = src_sub.add_parser("verify", help="Check URLs and DOIs over HTTP")
    src_verify.add_argument("--offline", action="store_true", help="Do not make network requests")
    src_verify.add_argument("--recheck", action="store_true", help="Re-probe already machine-verified sources")

    met = sub.add_parser("metrics", help="Compute deterministic plan metrics")
    met.add_argument("--json", action="store_true", help="Emit JSON")

    sc = sub.add_parser("score", help="Combine judge scores and metrics into scores.json")
    sc.add_argument("iteration", nargs="?", default="latest")

    st = sub.add_parser("stop-check", help="Evaluate stopping rules after scoring")
    st.add_argument("iteration", nargs="?", default="latest")

    sub.add_parser("report", help="Write iterations/REPORT.md")
    sub.add_parser("status", help="Print a one-line status summary")

    cp = sub.add_parser("checkpoint", help="Record human review sign-off for the latest iteration")
    cp.add_argument("--note", default="", help="Optional checkpoint note")

    lab = sub.add_parser("labor", help="Track 1: Empirical CNO-11 AI exposure and labor displacement")
    lab_sub = lab.add_subparsers(dest="lab_cmd", required=True)
    
    lab_sim = lab_sub.add_parser("simulate", help="Run labor displacement simulation for a scenario")
    lab_sim.add_argument("--scenario", choices=["S1", "S2", "S3"], default="S2", help="AI displacement scenario")
    lab_sim.add_argument("--export", metavar="PATH", help="Export counterfactual distributions to JSON file")

    lab_sub.add_parser("summary", help="Print comparative summary of S1, S2, and S3 scenarios")
    lab_sub.add_parser("occupations", help="List CNO-11 occupations and AI exposure scores")

    sim = sub.add_parser("sim", help="Track 2: EUROMOD-Spain microsimulation engine (M02, M03, M07, M09)")
    sim_sub = sim.add_subparsers(dest="sim_cmd", required=True)

    sim_run = sim_sub.add_parser("run", help="Run full microsimulation and print key results")
    sim_run.add_argument("--tier", choices=["A", "B", "C"], default="B", help="UBR Benefit Tier (default: B)")
    sim_run.add_argument("--scenario", choices=["S1", "S2", "S3"], default="S2", help="AI displacement scenario (default: S2)")
    sim_run.add_argument("--no-stabilizers", action="store_true", help="Disable rent stabilizers (D-008)")
    sim_run.add_argument("--export", metavar="PATH", help="Export full simulation results to JSON")

    sim_bridge = sim_sub.add_parser("bridge", help="Print Consolidated AP Gross-to-Net Fiscal Bridge")
    sim_bridge.add_argument("--tier", choices=["A", "B", "C"], default="B")
    sim_bridge.add_argument("--scenario", choices=["S1", "S2", "S3"], default="S2")

    sim_dec = sim_sub.add_parser("deciles", help="Print household disposable income and winner/loser decile table")
    sim_dec.add_argument("--tier", choices=["A", "B", "C"], default="B")
    sim_dec.add_argument("--scenario", choices=["S1", "S2", "S3"], default="S2")

    sim_pov = sim_sub.add_parser("poverty", help="Print poverty (BHC/AHC), inequality, and housing metrics")
    sim_pov.add_argument("--tier", choices=["A", "B", "C"], default="B")
    sim_pov.add_argument("--scenario", choices=["S1", "S2", "S3"], default="S2")
    sim_pov.add_argument("--no-stabilizers", action="store_true")

    sim_sum = sim_sub.add_parser("summary", help="Print comparative matrix across Tiers A, B, C and Scenarios S1, S2, S3")

    mac = sub.add_parser("macro", help="Track 3: Currency-Union HANK Model & Fiscal Rules (M04, M16, M17)")
    mac_sub = mac.add_subparsers(dest="mac_cmd", required=True)

    mac_irf = mac_sub.add_parser("irf", help="Simulate open-economy HANK impulse response functions (IRFs)")
    mac_irf.add_argument("--tier", choices=["A", "B", "C"], default="B", help="UBR Benefit Tier (default: B)")
    mac_irf.add_argument("--scenario", choices=["S1", "S2", "S3"], default="S2", help="AI displacement scenario (default: S2)")
    mac_irf.add_argument("--no-stabilizers", action="store_true", help="Disable rent stabilizers (D-008)")
    mac_irf.add_argument("--export", metavar="PATH", help="Export HANK simulation results to JSON")

    mac_npe = mac_sub.add_parser("npe", help="Evaluate EU Regulation 2024/1263 Net Primary Expenditure & LOEPSF compliance")
    mac_npe.add_argument("--tier", choices=["A", "B", "C"], default="B")
    mac_npe.add_argument("--scenario", choices=["S1", "S2", "S3"], default="S2")
    mac_npe.add_argument("--no-mdi", action="store_true", help="Evaluate unfinanced counterfactual without MDI pairing")
    mac_npe.add_argument("--export", metavar="PATH", help="Export fiscal rules compliance to JSON")

    mac_fund = mac_sub.add_parser("fund", help="Simulate 15-year Fondo Soberano de Renta Básica y Dividendos de IA (M16)")
    mac_fund.add_argument("--scenario", choices=["S1", "S2", "S3"], default="S2")
    mac_fund.add_argument("--export", metavar="PATH", help="Export sovereign fund simulation to JSON")

    mac_stress = mac_sub.add_parser("stress", help="Run compound tail-risk stress tests & circuit-breakers (M17)")
    mac_stress.add_argument("--tier", choices=["A", "B", "C"], default="B")
    mac_stress.add_argument("--scenario", choices=["S1", "S2", "S3"], default="S2")
    mac_stress.add_argument("--export", metavar="PATH", help="Export stress battery results to JSON")

    mac_summary = mac_sub.add_parser("summary", help="Print comprehensive macroeconomic dashboard across M04, M16, and M17")
    mac_summary.add_argument("--tier", choices=["A", "B", "C"], default="B")
    mac_summary.add_argument("--scenario", choices=["S1", "S2", "S3"], default="S2")

    pil = sub.add_parser("pilot", help="Track 4: Experimental Pilot Protocol, GIS & AEA PAP (M05, M08, M10, M15)")
    pil_sub = pil.add_subparsers(dest="pil_cmd", required=True)

    pil_clust = pil_sub.add_parser("clusters", help="Inspect J=70 spatial cluster registry and mobility GIS")
    pil_clust.add_argument("--export", metavar="PATH", help="Export cluster registry to JSON")

    pil_pwr = pil_sub.add_parser("power", help="Run two-stage saturation power and MDE calculations")
    pil_pwr.add_argument("--export", metavar="PATH", help="Export power analysis to JSON")

    pil_sdid = pil_sub.add_parser("sdid", help="Simulate SDID rental pass-through across deposit registries (M05)")
    pil_sdid.add_argument("--export", metavar="PATH", help="Export SDID simulation to JSON")

    pil_bunch = pil_sub.add_parser("bunching", help="Saez/Chetty convex disregard and Kleven missing-mass econometrics")
    pil_bunch.add_argument("--export", metavar="PATH", help="Export bunching estimates to JSON")

    pil_dec = pil_sub.add_parser("decompose", help="Structural life-cycle decomposition (Frisch vs wealth vs rationing)")

    pil_pap = pil_sub.add_parser("pap", help="Generate and inspect AEA RCT Registry Pre-Analysis Plan")
    pil_pap.add_argument("--export", metavar="PATH", help="Export AEA PAP to JSON")

    pil_sum = pil_sub.add_parser("summary", help="Print comprehensive Track 4 pilot dashboard")

    leg = sub.add_parser("legal", help="Track 5: Model Legislation & Governance Architecture (M06, M11, M12, M13, M16, M17)")
    leg_sub = leg.add_subparsers(dest="leg_cmd", required=True)

    leg_ant = leg_sub.add_parser("anteproyecto", help="Inspect Model Statute (Anteproyecto de Ley) and official articles")
    leg_ant.add_argument("--title", metavar="TITULO", help="Filter by title number (e.g., 'Título I')")
    leg_ant.add_argument("--export", metavar="PATH", help="Export statutory corpus to JSON")

    leg_comp = leg_sub.add_parser("competence", help="Validate Constitutional & EU Law Competence Matrix")
    leg_comp.add_argument("--detail", action="store_true", help="Show doctrinal defense and supported articles")
    leg_comp.add_argument("--export", metavar="PATH", help="Export competence matrix to JSON")

    leg_eq = leg_sub.add_parser("equalization", help="Simulate CPFF Intergovernmental Equalization & Foral Cupo balances")
    leg_eq.add_argument("--scenario", choices=["S1", "S2", "S3"], default="S2", help="AI displacement scenario (default: S2)")
    leg_eq.add_argument("--export", metavar="PATH", help="Export equalization balances to JSON")

    leg_bic = leg_sub.add_parser("bicameral", help="Simulate bicameral voting, LOEPSF Art. 15.6 override, and CARIN framing")
    leg_bic.add_argument("--export", metavar="PATH", help="Export bicameral report to JSON")

    leg_sum = leg_sub.add_parser("summary", help="Print consolidated Track 5 executive dashboard")

    return parser




def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        project = find_project()
        return _dispatch(project, args)
    except (ProjectNotFound, IterationError, ScoringError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


def _dispatch(project, args) -> int:
    if args.cmd == "validate":
        report = validate_plan(project)
        print(report.render())
        return 0 if report.ok else 1

    if args.cmd == "iteration" and args.it_cmd == "start":
        val = validate_plan(project)
        if not val.ok:
            print("Cannot start iteration; plan has validation errors:\n" + val.render(), file=sys.stderr)
            return 1
        it = start_iteration(project)
        print(f"Started {it.id}")
        print(f"Bundle: {it.path / 'bundle.md'}")
        print(f"Reviewers ({len(it.reviewers)}): {', '.join(it.reviewers)}")
        return 0

    if args.cmd == "reviews" and args.rev_cmd == "check":
        it = resolve_iteration(project, args.iteration)
        report = check_reviews(project, it, require_judge=args.judge)
        print(report.render())
        return 0 if report.ok else 1

    if args.cmd == "sources" and args.src_cmd == "verify":
        summary = verify_sources(project, offline=args.offline, recheck=args.recheck)
        print(
            f"checked={summary['checked']} verified={len(summary['verified'])} "
            f"failed={len(summary['failed'])} skipped={summary['skipped']}"
        )
        if summary["failed"]:
            print("failed ids: " + ", ".join(summary["failed"]))
        return 0

    if args.cmd == "metrics":
        metrics = compute_metrics(project)
        if args.json:
            print(json.dumps(metrics, indent=2))
        else:
            print(
                f"modules={metrics['modules']} (locked={metrics['locked_modules']}) "
                f"rqs={metrics['research_questions_total']} "
                f"coverage={metrics['coverage']:.0%} ({metrics['factors_total'] - len(metrics['uncovered_factors'])}/{metrics['factors_total']}) "
                f"cited_sources={metrics['cited_sources']}/{metrics['sources_total']} "
                f"verified={metrics['verified_ratio']:.0%} "
                f"words={metrics['words_total']} citations/1k={metrics['citations_per_1k_words']}"
            )
        return 0

    if args.cmd == "score":
        it = resolve_iteration(project, args.iteration)
        val = validate_plan(project)
        if not val.ok:
            print("Cannot score iteration; plan has validation errors:\n" + val.render(), file=sys.stderr)
            return 1
        scores = score_iteration(project, it)
        delta = f"{scores['delta']:+.2f}" if scores.get("delta") is not None else "n/a"
        print(
            f"{it.id} weighted={scores['weighted']:.2f} (delta={delta}, "
            f"min={scores['min_criterion']:.2f}, critical={scores['open_critical']})"
        )
        return 0

    if args.cmd == "stop-check":
        it = resolve_iteration(project, args.iteration)
        history = [h for h in score_history(project) if h["iteration"] <= it.number]
        decision = decide(history, project.config, last_checkpoint=last_checkpoint(project))
        print(f"outcome: {decision.outcome}")
        for r in decision.reasons:
            print(f"  - {r}")
        return 0

    if args.cmd == "report":
        out = build_report(project)
        print(f"Wrote {out.relative_to(project.root)}")
        return 0

    if args.cmd == "status":
        print(status_line(project))
        return 0

    if args.cmd == "checkpoint":
        num = record_checkpoint(project, note=args.note)
        print(f"Recorded human checkpoint at {format_id(num)}")
        return 0

    if args.cmd == "labor":
        from ubr.labor.cno_taxonomy import CNOTaxonomy
        from ubr.labor.task_exposure import TaskExposureEngine
        from ubr.labor.scenarios import LaborDisplacementSimulator
        from ubr.labor.export import export_counterfactual_json

        taxonomy = CNOTaxonomy.load_default()
        simulator = LaborDisplacementSimulator()

        if args.lab_cmd == "occupations":
            engine = TaskExposureEngine()
            scores = {s.cno_code: s for s in engine.compute_exposure(taxonomy)}
            print(f"{'CNO':<5} {'Title':<48} {'FTE':>10} {'Avg Wage':>10} {'Alpha':>6} {'Beta':>6} {'Net Exp':>8}")
            print("-" * 98)
            for g in taxonomy.all_groups():
                s = scores[g.cno_code]
                short_title = (g.title[:45] + "...") if len(g.title) > 48 else g.title
                print(
                    f"{g.cno_code:<5} {short_title:<48} {int(g.fte_employment):>10,d} "
                    f"€{g.avg_monthly_gross_wage:>8,.0f} {s.alpha_direct:>6.2f} {s.beta_augmented:>6.2f} {s.net_exposure:>8.2f}"
                )
            print("-" * 98)
            print(f"Total Employment (FTE): {int(taxonomy.total_employment_fte()):,d} | Gross Wage Bill: €{taxonomy.total_aggregate_wage_bill():,.0f}/yr")
            return 0

        if args.lab_cmd == "simulate":
            res = simulator.run_scenario(args.scenario, taxonomy)
            print(f"=== Scenario {res.scenario} AI Labor Displacement Simulation ===")
            print(f"Baseline Employment: {int(res.total_baseline_fte):,d} FTE")
            print(f"Displaced Employment: {int(res.total_displaced_fte):,d} FTE ({res.net_displaced_fte_share:.1%})")
            print(f"Labor Income Share Shock: {res.labor_share_delta_pp:+.1f} pp")
            print(f"Baseline Tax Base Erosion: -{res.baseline_tax_loss_pct_gdp:.2f}% of GDP (€{res.baseline_tax_loss_billion_eur:.2f} Billion/year)")
            print(f"  - Social Security Contribution Loss: €{res.tax_drag_by_component['social_security_loss_billion_eur']:.2f}B")
            print(f"  - IRPF & Employee Withholding Loss:   €{res.tax_drag_by_component['irpf_and_employee_ss_loss_billion_eur']:.2f}B")
            print(f"Pre-Shock Aggregate Wage Bill:  €{res.pre_aggregate_wage_bill_eur:,.0f}/year")
            print(f"Post-Shock Aggregate Wage Bill: €{res.post_aggregate_wage_bill_eur:,.0f}/year")
            if args.export:
                export_counterfactual_json(res, args.export)
                print(f"Exported counterfactual distribution to: {args.export}")
            return 0

        if args.lab_cmd == "summary":
            print(f"{'Scenario':<10} {'Displaced FTE':>14} {'FTE Share':>10} {'Labor Share':>12} {'Tax Loss (%GDP)':>16} {'Tax Loss (€B)':>14}")
            print("-" * 80)
            for sc_id in ["S1", "S2", "S3"]:
                res = simulator.run_scenario(sc_id, taxonomy)
                print(
                    f"{sc_id:<10} {int(res.total_displaced_fte):>14,d} {res.net_displaced_fte_share:>9.1%} "
                    f"{res.labor_share_delta_pp:>11.1f}pp {res.baseline_tax_loss_pct_gdp:>15.2f}% €{res.baseline_tax_loss_billion_eur:>12.2f}B"
                )
            print("-" * 80)
            return 0

    if args.cmd == "sim":
        from ubr.microsim.engine import MicrosimulationEngine
        from ubr.microsim.benefits import UBRTier
        from ubr.microsim.export import (
            export_microsim_json,
            render_decile_table,
            render_fiscal_bridge_table,
            render_poverty_table,
        )

        tier_enum = UBRTier(args.tier) if hasattr(args, "tier") else UBRTier.TIER_B
        engine = MicrosimulationEngine()

        if args.sim_cmd == "run":
            res = engine.run_simulation(
                tier=tier_enum,
                scenario=args.scenario,
                enable_rent_stabilizers=not args.no_stabilizers,
            )
            print(render_fiscal_bridge_table(res))
            print()
            print(render_poverty_table(res))
            print()
            print(f"Breakeven Income: €{res.fiscal_bridge.breakeven_gross_income_eur:,.0f} (p{res.fiscal_bridge.breakeven_percentile:.1f})")
            if args.export:
                export_microsim_json(res, args.export)
                print(f"Exported simulation results to: {args.export}")
            return 0

        if args.sim_cmd == "bridge":
            res = engine.run_simulation(
                tier=tier_enum,
                scenario=args.scenario,
            )
            print(render_fiscal_bridge_table(res))
            return 0

        if args.sim_cmd == "deciles":
            res = engine.run_simulation(
                tier=tier_enum,
                scenario=args.scenario,
            )
            print(render_decile_table(res))
            return 0

        if args.sim_cmd == "poverty":
            res = engine.run_simulation(
                tier=tier_enum,
                scenario=args.scenario,
                enable_rent_stabilizers=not args.no_stabilizers,
            )
            print(render_poverty_table(res))
            return 0

        if args.sim_cmd == "summary":
            print(f"{'Tier':<6} {'Scenario':<10} {'Breakeven':>14} {'Gini Pre/Post':>16} {'Child Pov (AHC)':>18} {'Net Balance (%GDP)':>20}")
            print("-" * 88)
            for t_code in ["A", "B", "C"]:
                for sc_code in ["S1", "S2", "S3"]:
                    t_enum = UBRTier(t_code)
                    res = engine.run_simulation(tier=t_enum, scenario=sc_code)
                    fb = res.fiscal_bridge
                    b_dist = res.baseline_distribution
                    p_dist = res.post_distribution
                    print(
                        f"{t_code:<6} {sc_code:<10} "
                        f"p{fb.breakeven_percentile:>4.1f} (€{fb.breakeven_gross_income_eur/1e3:>2.0f}k) "
                        f"{b_dist.gini_coefficient:.3f} -> {p_dist.gini_coefficient:.3f} "
                        f"{b_dist.ahc_child_poverty_rate:>6.1%} -> {p_dist.ahc_child_poverty_rate:>5.1%} "
                        f"{fb.consolidated_net_balance_pct_gdp:>+18.2f}%"
                    )
            print("-" * 88)
            return 0

    if args.cmd == "macro":
        from ubr.macro import (
            CurrencyUnionHANKModel,
            EUFiscalGovernanceValidator,
            SovereignFundAccumulationModel,
            MacroStressTestHarness,
            export_fiscal_rules_json,
            export_hank_json,
            export_sovereign_fund_json,
            export_stress_tests_json,
            render_fiscal_rules_table,
            render_irf_table,
            render_sovereign_fund_table,
            render_stress_battery_table,
        )

        tier = getattr(args, "tier", "B")
        scenario = getattr(args, "scenario", "S2")

        if args.mac_cmd == "irf":
            model = CurrencyUnionHANKModel()
            res = model.simulate(
                tier=tier,
                scenario=scenario,
                enable_rent_stabilizers=not getattr(args, "no_stabilizers", False),
            )
            print(render_irf_table(res))
            if args.export:
                export_hank_json(res, args.export)
                print(f"Exported HANK simulation IRFs to: {args.export}")
            return 0

        if args.mac_cmd == "npe":
            validator = EUFiscalGovernanceValidator()
            res = validator.evaluate_trajectory(
                tier=tier,
                scenario=scenario,
                pair_with_discretionary_revenue=not getattr(args, "no_mdi", False),
            )
            print(render_fiscal_rules_table(res))
            if args.export:
                export_fiscal_rules_json(res, args.export)
                print(f"Exported EU fiscal rules evaluation to: {args.export}")
            return 0

        if args.mac_cmd == "fund":
            fund_model = SovereignFundAccumulationModel()
            res = fund_model.simulate_15_year_path(scenario=scenario)
            print(render_sovereign_fund_table(res))
            if args.export:
                export_sovereign_fund_json(res, args.export)
                print(f"Exported sovereign fund 15-year simulation to: {args.export}")
            return 0

        if args.mac_cmd == "stress":
            harness = MacroStressTestHarness()
            res = harness.run_battery(tier=tier, scenario=scenario)
            print(render_stress_battery_table(res))
            if args.export:
                export_stress_tests_json(res, args.export)
                print(f"Exported compound stress-test battery to: {args.export}")
            return 0

        if args.mac_cmd == "summary":
            model = CurrencyUnionHANKModel()
            hank_res = model.simulate(tier=tier, scenario=scenario)
            val = EUFiscalGovernanceValidator()
            npe_res = val.evaluate_trajectory(tier=tier, scenario=scenario)
            fund = SovereignFundAccumulationModel()
            fund_res = fund.simulate_15_year_path(scenario=scenario)
            harness = MacroStressTestHarness()
            stress_res = harness.run_battery(tier=tier, scenario=scenario)

            print(render_irf_table(hank_res))
            print()
            print(render_fiscal_rules_table(npe_res))
            print()
            print(render_sovereign_fund_table(fund_res))
            print()
            print(render_stress_battery_table(stress_res))
            return 0

    if args.cmd == "pilot":
        from ubr.pilot import (
            ClusterRegistry,
            TwoStagePowerCalculator,
            SyntheticDiffInDiff,
            BunchingEstimator,
            LifeCycleDecomposition,
            RegisterLinkageProtocol,
            PreAnalysisPlanGenerator,
            export_clusters_json,
            export_power_json,
            export_sdid_json,
            export_bunching_json,
            export_pap_json,
            render_clusters_table,
            render_power_table,
            render_sdid_table,
            render_bunching_table,
            render_decomposition_table,
            render_pilot_summary,
        )

        reg = ClusterRegistry()

        if args.pil_cmd == "clusters":
            print(render_clusters_table(reg))
            if args.export:
                export_clusters_json(reg, args.export)
                print(f"Exported cluster registry to: {args.export}")
            return 0

        if args.pil_cmd == "power":
            calc = TwoStagePowerCalculator()
            p_res = calc.run_full_power_analysis()
            print(render_power_table(p_res))
            if args.export:
                export_power_json(p_res, args.export)
                print(f"Exported power analysis to: {args.export}")
            return 0

        if args.pil_cmd == "sdid":
            sdid = SyntheticDiffInDiff()
            s_res = sdid.estimate(reg.clusters)
            print(render_sdid_table(s_res))
            if args.export:
                export_sdid_json(s_res, args.export)
                print(f"Exported SDID simulation to: {args.export}")
            return 0

        if args.pil_cmd == "bunching":
            buncher = BunchingEstimator()
            b_arms = {
                "Arm_A": buncher.estimate(arm="Arm_A_pure_ubr_0pct", clawback_rate=0.0),
                "Arm_B": buncher.estimate(arm="Arm_B_mod_clawback_38pct", clawback_rate=0.38),
                "Arm_C": buncher.estimate(arm="Arm_C_high_clawback_50pct", clawback_rate=0.50),
            }
            print(render_bunching_table(b_arms))
            if args.export:
                export_bunching_json(b_arms, args.export)
                print(f"Exported bunching estimates to: {args.export}")
            return 0

        if args.pil_cmd == "decompose":
            decomposer = LifeCycleDecomposition()
            d_res = decomposer.decompose()
            print(render_decomposition_table(d_res))
            return 0

        if args.pil_cmd == "pap":
            gen = PreAnalysisPlanGenerator()
            pap_doc = gen.generate_plan()
            print("==================================================================================================")
            print("         AEA RCT REGISTRY PRE-ANALYSIS PLAN (PAP) - SUMMARY METADATA                             ")
            print("==================================================================================================")
            print(f"Trial ID:               {pap_doc.trial_id}")
            print(f"Title:                  {pap_doc.title}")
            print(f"Lead Institution:       {pap_doc.lead_institution}")
            print(f"Partners:               {', '.join(pap_doc.consortium_partners[:3])}...")
            print(f"Registration Date:      {pap_doc.registration_date} | Duration: {pap_doc.trial_duration_months} Months")
            print("Pre-Registered Hypotheses:")
            for h in pap_doc.hypotheses:
                print(f"  * [{h.hypothesis_id}] {h.category}: {h.statement[:80]}...")
            print("Primary Outcome Families:")
            for e in pap_doc.primary_endpoints:
                print(f"  * [{e.outcome_id}] {e.name:<28} | MDE: {e.mde_threshold:<6} | Reg: {e.source_register}")
            print("==================================================================================================")
            if args.export:
                export_pap_json(pap_doc, args.export)
                print(f"Exported AEA Pre-Analysis Plan to: {args.export}")
            return 0

        if args.pil_cmd == "summary":
            calc = TwoStagePowerCalculator()
            p_res = calc.run_full_power_analysis()
            sdid = SyntheticDiffInDiff()
            s_res = sdid.estimate(reg.clusters)
            buncher = BunchingEstimator()
            b_arms = {
                "Arm_A": buncher.estimate(arm="Arm_A_pure_ubr_0pct", clawback_rate=0.0),
                "Arm_B": buncher.estimate(arm="Arm_B_mod_clawback_38pct", clawback_rate=0.38),
                "Arm_C": buncher.estimate(arm="Arm_C_high_clawback_50pct", clawback_rate=0.50),
            }
            decomposer = LifeCycleDecomposition()
            d_res = decomposer.decompose()
            linkage = RegisterLinkageProtocol()
            budget = linkage.compute_budget_breakdown()

            print(render_pilot_summary(reg, p_res, s_res, b_arms, d_res, budget))
            return 0

    if args.cmd == "legal":
        from ubr.legislation.anteproyecto import build_anteproyecto_corpus
        from ubr.legislation.bicameral_engine import simulate_bicameral_pathway
        from ubr.legislation.competence_matrix import evaluate_competence_architecture
        from ubr.legislation.equalization import calculate_intergovernmental_equalization
        from ubr.legislation.export import (
            format_anteproyecto_summary,
            format_bicameral_summary,
            format_competence_matrix_summary,
            format_equalization_summary,
            format_legislation_executive_summary,
        )

        if args.leg_cmd == "anteproyecto":
            corpus = build_anteproyecto_corpus()
            print(format_anteproyecto_summary(corpus, title_num=args.title))
            if args.export:
                with open(args.export, "w", encoding="utf-8") as f:
                    json.dump(corpus.to_dict(), f, indent=2, ensure_ascii=False)
                print(f"Exported Anteproyecto corpus to: {args.export}")
            return 0

        if args.leg_cmd == "competence":
            matrix = evaluate_competence_architecture()
            print(format_competence_matrix_summary(matrix, detail=args.detail))
            if args.export:
                with open(args.export, "w", encoding="utf-8") as f:
                    json.dump(matrix.to_dict(), f, indent=2, ensure_ascii=False)
                print(f"Exported Competence Matrix to: {args.export}")
            return 0

        if args.leg_cmd == "equalization":
            eq_rep = calculate_intergovernmental_equalization(scenario=args.scenario)
            print(format_equalization_summary(eq_rep))
            if args.export:
                with open(args.export, "w", encoding="utf-8") as f:
                    json.dump(eq_rep.to_dict(), f, indent=2, ensure_ascii=False)
                print(f"Exported Equalization report to: {args.export}")
            return 0

        if args.leg_cmd == "bicameral":
            bic_rep = simulate_bicameral_pathway()
            print(format_bicameral_summary(bic_rep))
            if args.export:
                with open(args.export, "w", encoding="utf-8") as f:
                    json.dump(bic_rep.to_dict(), f, indent=2, ensure_ascii=False)
                print(f"Exported Bicameral report to: {args.export}")
            return 0

        if args.leg_cmd == "summary":
            print(format_legislation_executive_summary())
            return 0

    return 1


