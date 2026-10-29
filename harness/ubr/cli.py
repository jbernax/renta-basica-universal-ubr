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

    return 1

