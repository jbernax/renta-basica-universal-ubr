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

    return 1
