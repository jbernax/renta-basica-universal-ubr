"""Human-facing status line and REPORT.md generator across iterations."""
from __future__ import annotations

from pathlib import Path

from ubr.iterations import format_id, last_checkpoint, list_iterations, open_iteration
from ubr.metrics import compute_metrics
from ubr.project import Project, load_yaml
from ubr.scoring import score_history
from ubr.stopping import decide


def status_line(project: Project) -> str:
    current = open_iteration(project)
    if current:
        return (
            f"{current.id} OPEN (reviewers: {', '.join(current.reviewers)}) — "
            "complete reviews, synthesis, changelog, judge, then run `python -m ubr score`."
        )
    history = score_history(project)
    if not history:
        metrics = compute_metrics(project)
        return (
            f"No iterations yet — {metrics['modules']} module(s), "
            f"coverage {metrics['coverage']:.0%}, verified sources {metrics['verified_ratio']:.0%}. "
            "Run `python -m ubr iteration start`."
        )
    latest = history[-1]
    decision = decide(history, project.config, last_checkpoint=last_checkpoint(project))
    delta = f"{latest['delta']:+.2f}" if latest.get("delta") is not None else "n/a"
    return (
        f"{format_id(latest['iteration'])} scored: weighted={latest['weighted']:.2f} "
        f"(delta={delta}, min={latest['min_criterion']:.2f}, critical={latest.get('open_critical', 0)}, "
        f"coverage={latest['metrics']['coverage']:.0%}, verified={latest['metrics']['verified_ratio']:.0%}) "
        f"→ {decision.outcome}"
    )


def build_report(project: Project) -> Path:
    project.iterations_dir.mkdir(parents=True, exist_ok=True)
    history = score_history(project)
    decision = decide(history, project.config, last_checkpoint=last_checkpoint(project))
    iterations = list_iterations(project)

    lines = [
        "# Research Plan Improvement Report",
        "",
        f"**Status:** `{decision.outcome}`",
        "",
    ]
    if decision.reasons:
        lines.append("**Reasons / SOTA gates:**")
        lines.extend(f"- {r}" for r in decision.reasons)
        lines.append("")

    if history:
        lines.extend(_history_table(history))
        lines.extend(_latest_criteria_section(project, history[-1]))
    else:
        lines.extend(["_No scored iterations yet._", ""])

    if iterations:
        lines.extend(_latest_iteration_details(iterations[-1]))

    target = project.iterations_dir / "REPORT.md"
    target.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return target


def _history_table(history: list[dict]) -> list[str]:
    rows = [
        "## Score History",
        "",
        "| Iteration | Weighted | Delta | Min Criterion | Open Critical | Coverage | Verified Sources |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for h in history:
        delta = f"{h['delta']:+.2f}" if h.get("delta") is not None else "—"
        m = h.get("metrics", {})
        rows.append(
            f"| `{format_id(h['iteration'])}` | **{h['weighted']:.2f}** | {delta} | "
            f"{h['min_criterion']:.2f} | {h.get('open_critical', 0)} | "
            f"{m.get('coverage', 0.0):.0%} | {m.get('verified_ratio', 0.0):.0%} |"
        )
    rows.append("")
    return rows


def _latest_criteria_section(project: Project, latest: dict) -> list[str]:
    rows = [
        f"## Rubric Breakdown (`{format_id(latest['iteration'])}`)",
        "",
        "| Criterion | Weight | Score | Delta |",
        "|---|---:|---:|---:|",
    ]
    deltas = latest.get("criteria_delta") or {}
    for c in project.rubric:
        cid = c["id"]
        score = latest["criteria"].get(cid, 0.0)
        d = f"{deltas[cid]:+.2f}" if cid in deltas else "—"
        rows.append(f"| {c['name']} (`{cid}`) | {c['weight']:.2f} | {score:.2f} | {d} |")
    rows.append("")
    return rows


def _latest_iteration_details(latest) -> list[str]:
    out = [f"## Latest Iteration Details (`{latest.id}`)", ""]
    judge_path = latest.path / "judge.yaml"
    if judge_path.is_file():
        judge = load_yaml(judge_path) or {}
        if judge.get("sota_assessment"):
            out.extend(["### Judge Assessment", "", judge["sota_assessment"].strip(), ""])
        criticals = judge.get("critical_issues") or []
        if criticals:
            out.extend(["### Open Critical Issues", ""])
            for item in criticals:
                out.append(f"- **{item['id']}** ({item['module']}): {item['finding']}")
            out.append("")

    changelog = latest.path / "changelog.md"
    if changelog.is_file():
        out.extend(["### Latest Changelog", "", changelog.read_text(encoding="utf-8").strip(), ""])

    proposals = latest.path / "proposals-for-human.md"
    if proposals.is_file():
        text = proposals.read_text(encoding="utf-8").strip()
        if text:
            out.extend(["### Proposals Requiring Human Decision", "", text, ""])
    return out
