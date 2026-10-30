"""Paper critique harness: adversarial iterations, review schema checks, scoring, and reports."""
from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import jsonschema
import yaml

from ubr.findings import Report
from ubr.project import Project, dump_yaml, load_yaml

PAPER_ITER_PREFIX = "iter-"
DEFAULT_ADVERSARIAL_REVIEWERS = [
    "adversarial-fiscal",
    "adversarial-implementation",
    "adversarial-law-abuse",
    "adversarial-productivity",
    "adversarial-housing",
]
PAPER_CHAPTERS = [
    "ch00-executive-summary.md",
    "ch01-introduction-analytical-framework.md",
    "ch02-ai-shock-spain.md",
    "ch03-benefit-architecture-welfare-integration.md",
    "ch04-fiscal-architecture-ai-rent-capture.md",
    "ch05-macroeconomic-closure-housing-eurozone.md",
    "ch06-constitutional-territorial-eu-legal-blueprint.md",
    "ch07-multi-level-pilot-causal-evaluation.md",
    "ch08-political-economy-transition-governance.md",
]


class PaperCritiqueError(Exception):
    pass


@dataclass(frozen=True)
class PaperIteration:
    number: int
    path: Path

    @property
    def id(self) -> str:
        return f"{PAPER_ITER_PREFIX}{self.number:04d}"

    @property
    def manifest(self) -> dict:
        return load_yaml(self.path / "manifest.yaml") or {}

    @property
    def reviewers(self) -> list[str]:
        return list(self.manifest.get("reviewers", []))

    @property
    def is_open(self) -> bool:
        return not (self.path / "scores.json").exists()

    @property
    def snapshot_paper(self) -> Path:
        return self.path / "snapshot" / "paper"

    @property
    def bundle_path(self) -> Path:
        return self.path / "bundle.md"


def paper_iterations_dir(project: Project) -> Path:
    return project.root / "paper_iterations"


def list_paper_iterations(project: Project) -> list[PaperIteration]:
    pdir = paper_iterations_dir(project)
    if not pdir.is_dir():
        return []
    found = []
    for path in pdir.glob(f"{PAPER_ITER_PREFIX}[0-9][0-9][0-9][0-9]"):
        if path.is_dir():
            found.append(PaperIteration(int(path.name[len(PAPER_ITER_PREFIX):]), path))
    return sorted(found, key=lambda it: it.number)


def current_open_paper_iteration(project: Project) -> PaperIteration | None:
    for it in list_paper_iterations(project):
        if it.is_open:
            return it
    return None


def resolve_paper_iteration(project: Project, ident: str = "latest") -> PaperIteration:
    all_its = list_paper_iterations(project)
    if not all_its:
        raise PaperCritiqueError("No paper iterations exist yet; run 'ubr paper critique start' first.")
    if ident == "latest":
        return all_its[-1]
    for it in all_its:
        if it.id == ident or str(it.number) == ident:
            return it
    raise PaperCritiqueError(f"Unknown paper iteration '{ident}'")


def build_paper_bundle(project: Project) -> str:
    paper_dir = project.root / "paper"
    parts = [
        "# Universal Basic Rent (Spain) · Complete Paper Monograph for Adversarial Review\n",
        "> **Bundle compiled for adversarial critique panel.** Chapters ch00 through ch08.\n\n",
    ]
    for ch_file in PAPER_CHAPTERS:
        path = paper_dir / ch_file
        if path.is_file():
            ch_id = ch_file[:4]
            parts.append(f"\n<!-- BEGIN CHAPTER: {ch_id} ({ch_file}) -->\n\n")
            parts.append(path.read_text(encoding="utf-8"))
            parts.append(f"\n\n<!-- END CHAPTER: {ch_id} -->\n")
    return "".join(parts)


def start_paper_iteration(
    project: Project,
    reviewers: list[str] | None = None,
    now: datetime | None = None,
) -> PaperIteration:
    open_it = current_open_paper_iteration(project)
    if open_it:
        raise PaperCritiqueError(
            f"Paper iteration {open_it.id} is still open (no scores.json). "
            f"Complete or score it before starting a new one."
        )

    all_its = list_paper_iterations(project)
    next_num = (all_its[-1].number + 1) if all_its else 1
    new_id = f"{PAPER_ITER_PREFIX}{next_num:04d}"

    pdir = paper_iterations_dir(project)
    it_dir = pdir / new_id
    it_dir.mkdir(parents=True, exist_ok=False)
    (it_dir / "reviews").mkdir(exist_ok=True)
    snapshot_dir = it_dir / "snapshot" / "paper"
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    paper_dir = project.root / "paper"
    for item in paper_dir.glob("*.md"):
        if item.is_file():
            shutil.copy2(item, snapshot_dir / item.name)

    bundle_content = build_paper_bundle(project)
    (it_dir / "bundle.md").write_text(bundle_content, encoding="utf-8")

    chosen_reviewers = list(reviewers or DEFAULT_ADVERSARIAL_REVIEWERS)
    now_ts = (now or datetime.now(timezone.utc)).isoformat(timespec="seconds")
    manifest = {
        "iteration": next_num,
        "started_at": now_ts,
        "reviewers": chosen_reviewers,
    }
    dump_yaml(it_dir / "manifest.yaml", manifest)

    return PaperIteration(next_num, it_dir)


def load_paper_rubric(project: Project) -> list[dict]:
    rubric_path = project.harness_dir / "paper_rubric.yaml"
    if not rubric_path.is_file():
        raise PaperCritiqueError(f"Missing paper rubric at {rubric_path}")
    data = load_yaml(rubric_path)
    return data.get("criteria", [])


def check_paper_reviews(
    project: Project,
    iteration: PaperIteration,
    require_judge: bool = False,
) -> Report:
    report = Report()
    rubric = load_paper_rubric(project)
    criteria_ids = {c["id"] for c in rubric}
    reviews_dir = iteration.path / "reviews"
    expected = iteration.reviewers

    for reviewer in expected:
        if not (reviews_dir / f"{reviewer}.yaml").is_file():
            report.error(f"{iteration.id}/reviews", f"missing review from {reviewer}")

    review_schema = project.schema("paper_review")
    for path in sorted(reviews_dir.glob("*.yaml")):
        where = f"{iteration.id}/reviews/{path.name}"
        data = _load_yaml_file(path, where, report)
        if data is None:
            continue
        _validate_schema(review_schema, data, where, report)
        if data.get("reviewer") != path.stem:
            report.error(where, f"reviewer field '{data.get('reviewer')}' != filename stem '{path.stem}'")
        if data.get("iteration") != iteration.number:
            report.error(where, f"iteration field {data.get('iteration')} != {iteration.number}")
        for criterion in data.get("scores", {}):
            if criterion not in criteria_ids:
                report.error(where, f"unknown paper rubric criterion '{criterion}'")
        for issue in data.get("issues", []):
            ch = issue.get("chapter", "")
            if not re.match(r"^(ch0[0-8]|GLOBAL|MONOGRAPH)$", ch):
                report.error(where, f"{issue.get('id')}: invalid chapter reference '{ch}'")

    judge_path = iteration.path / "judge.yaml"
    if judge_path.is_file():
        where_j = f"{iteration.id}/judge.yaml"
        judge_data = _load_yaml_file(judge_path, where_j, report)
        if judge_data is not None:
            judge_schema = project.schema("paper_judge")
            _validate_schema(judge_schema, judge_data, where_j, report)
            if judge_data.get("iteration") != iteration.number:
                report.error(where_j, f"iteration field {judge_data.get('iteration')} != {iteration.number}")
            scored = set(judge_data.get("scores", {}).keys())
            for missing in sorted(criteria_ids - scored):
                report.error(where_j, f"judge did not score criterion '{missing}'")
            for unknown in sorted(scored - criteria_ids):
                report.error(where_j, f"unknown criterion '{unknown}' in judge scores")
    elif require_judge:
        report.error(iteration.id, "judge.yaml is missing")

    return report


def score_paper_iteration(
    project: Project,
    iteration: PaperIteration,
    now: datetime | None = None,
) -> dict:
    for name in ("synthesis.md", "changelog.md"):
        if not (iteration.path / name).is_file():
            raise PaperCritiqueError(f"{iteration.id} is missing required {name}")

    report = check_paper_reviews(project, iteration, require_judge=True)
    if not report.ok:
        raise PaperCritiqueError(f"{iteration.id} checks failed:\n{report.render()}")

    judge_path = iteration.path / "judge.yaml"
    judge = load_yaml(judge_path)
    rubric = load_paper_rubric(project)
    criteria_weights = {c["id"]: float(c["weight"]) for c in rubric}

    scores_dict: dict[str, float] = {}
    for cid in criteria_weights:
        scores_dict[cid] = float(judge["scores"][cid]["score"])

    total_weight = sum(criteria_weights.values())
    weighted = sum(scores_dict[cid] * criteria_weights[cid] for cid in criteria_weights) / total_weight

    all_its = list_paper_iterations(project)
    prev_it = None
    for it in all_its:
        if it.number == iteration.number - 1:
            prev_it = it
            break

    prev_scores = None
    if prev_it and (prev_it.path / "scores.json").is_file():
        prev_scores = json.loads((prev_it.path / "scores.json").read_text(encoding="utf-8"))

    delta = round(weighted - prev_scores["weighted"], 4) if prev_scores else None
    criteria_delta = {}
    if prev_scores:
        for cid, val in scores_dict.items():
            prev_val = prev_scores.get("criteria", {}).get(cid, 0.0)
            criteria_delta[cid] = round(val - prev_val, 4)

    scored_at = (now or datetime.now(timezone.utc)).isoformat(timespec="seconds")
    result = {
        "iteration": iteration.number,
        "scored_at": scored_at,
        "weighted": round(weighted, 4),
        "criteria": scores_dict,
        "min_criterion": min(scores_dict.values()),
        "delta": delta,
        "criteria_delta": criteria_delta,
        "critical_vulnerabilities": len(judge.get("critical_vulnerabilities") or []),
    }

    (iteration.path / "scores.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    generate_paper_report(project)
    return result


def generate_paper_report(project: Project) -> Path:
    pdir = paper_iterations_dir(project)
    pdir.mkdir(parents=True, exist_ok=True)
    report_file = pdir / "REPORT.md"

    its = list_paper_iterations(project)
    lines = [
        "# Universal Basic Rent (Spain) · Adversarial Paper Critique Report\n\n",
        "> Tracking adversarial critique cycles, vulnerability scores, and paper refinements.\n\n",
        "## 1. Adversarial Robustness Score Progression\n\n",
        "| Iteration | Scored At | Weighted Score (0-5) | Min Criterion | Delta | Open Vulnerabilities |\n",
        "|---|---|---|---|---|---|\n",
    ]

    for it in its:
        score_file = it.path / "scores.json"
        if score_file.is_file():
            sc = json.loads(score_file.read_text(encoding="utf-8"))
            delta = sc.get("delta")
            if delta is None:
                delta_str = "—"
            elif delta > 0:
                delta_str = f"+{delta:.2f}"
            else:
                delta_str = f"{delta:.2f}"
            lines.append(
                f"| `{it.id}` | {sc['scored_at'][:10]} | **{sc['weighted']:.2f}** | "
                f"{sc['min_criterion']:.2f} | {delta_str} | {sc['critical_vulnerabilities']} |\n"
            )
        else:
            lines.append(f"| `{it.id}` | *(In Progress)* | — | — | — | — |\n")

    lines.append("\n## 2. Latest Iteration Reviewer Breakdown\n\n")
    if its:
        latest = its[-1]
        score_file = latest.path / "scores.json"
        if score_file.is_file():
            sc = json.loads(score_file.read_text(encoding="utf-8"))
            lines.append(f"### Iteration `{latest.id}` Criterion Details\n\n")
            for cid, val in sc.get("criteria", {}).items():
                cdelta = sc.get("criteria_delta", {}).get(cid, 0.0)
                cdelta_str = f" (+{cdelta:.2f})" if cdelta > 0 else (f" ({cdelta:.2f})" if cdelta < 0 else "")
                lines.append(f"- **`{cid}`**: {val:.2f}{cdelta_str}\n")
            lines.append("\n")

        judge_file = latest.path / "judge.yaml"
        if judge_file.is_file():
            jd = load_yaml(judge_file)
            lines.append("### Judge Verdict & Remaining Critical Vulnerabilities\n\n")
            lines.append(f"> {jd.get('overall_robustness_verdict', '')}\n\n")
            vulns = jd.get("critical_vulnerabilities", [])
            if vulns:
                for v in vulns:
                    lines.append(f"- **[{v.get('id')}]** `{v.get('chapter')}`: {v.get('vulnerability')}\n")
            else:
                lines.append("*(No open critical vulnerabilities)*\n")

    report_text = "".join(lines)
    report_file.write_text(report_text, encoding="utf-8")
    return report_file


def _load_yaml_file(path: Path, where: str, report: Report) -> Any | None:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as ex:
        report.error(where, f"invalid YAML: {ex}")
        return None


def _validate_schema(schema: dict, data: Any, where: str, report: Report) -> None:
    validator = jsonschema.Draft202012Validator(schema)
    for err in validator.iter_errors(data):
        loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
        report.error(where, f"{loc}: {err.message}")
