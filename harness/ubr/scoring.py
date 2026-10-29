"""Turn a judge verdict plus deterministic metrics into an iteration's scores.json."""
from __future__ import annotations

import json
from datetime import datetime, timezone

from ubr.iterations import Iteration, list_iterations
from ubr.metrics import compute_metrics
from ubr.project import Project, load_yaml
from ubr.reviews import check_reviews

REQUIRED_ARTIFACTS = ("synthesis.md", "changelog.md")


class ScoringError(Exception):
    pass


def load_scores(iteration: Iteration) -> dict | None:
    path = iteration.path / "scores.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None


def score_history(project: Project) -> list[dict]:
    return [s for s in (load_scores(it) for it in list_iterations(project)) if s]


def weighted_score(rubric: list[dict], scores: dict[str, float]) -> float:
    total_weight = sum(float(c["weight"]) for c in rubric)
    return sum(float(c["weight"]) * scores[c["id"]] for c in rubric) / total_weight


def score_iteration(project: Project, iteration: Iteration, now: datetime | None = None) -> dict:
    for name in REQUIRED_ARTIFACTS:
        if not (iteration.path / name).is_file():
            raise ScoringError(f"{iteration.id} has no {name}; every iteration must record it before scoring.")
    report = check_reviews(project, iteration, require_judge=True)
    if not report.ok:
        raise ScoringError(f"{iteration.id} reviews/judge are invalid:\n{report.render()}")

    judge = load_yaml(iteration.path / "judge.yaml")
    criteria = {cid: float(judge["scores"][cid]["score"]) for cid in project.criterion_ids}
    previous = _previous_scores(project, iteration)
    weighted = weighted_score(project.rubric, criteria)
    scores = {
        "iteration": iteration.number,
        "scored_at": (now or datetime.now(timezone.utc)).isoformat(timespec="seconds"),
        "weighted": round(weighted, 4),
        "criteria": criteria,
        "min_criterion": min(criteria.values()),
        "delta": round(weighted - previous["weighted"], 4) if previous else None,
        "criteria_delta": {c: round(v - previous["criteria"].get(c, 0.0), 4) for c, v in criteria.items()}
        if previous else {},
        "open_critical": len(judge.get("critical_issues") or []),
        "metrics": compute_metrics(project),
    }
    (iteration.path / "scores.json").write_text(json.dumps(scores, indent=2), encoding="utf-8")
    return scores


def _previous_scores(project: Project, iteration: Iteration) -> dict | None:
    earlier = [it for it in list_iterations(project) if it.number < iteration.number]
    for it in reversed(earlier):
        scores = load_scores(it)
        if scores:
            return scores
    return None
