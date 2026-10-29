import json

import pytest
from conftest import FIXED_NOW, complete_iteration, make_judge

from ubr.iterations import start_iteration
from ubr.metrics import compute_metrics
from ubr.scoring import ScoringError, score_iteration


def test_metrics_coverage_counts_factors_declared_by_modules_with_questions(project):
    metrics = compute_metrics(project)
    assert metrics["coverage"] == pytest.approx(2 / 3)
    assert metrics["uncovered_factors"] == ["F03"]


def test_metrics_verified_ratio_only_counts_cited_sources(project):
    metrics = compute_metrics(project)
    # cited: src-a (verified), src-b (unverified); src-unused is ignored
    assert metrics["cited_sources"] == 2
    assert metrics["verified_ratio"] == pytest.approx(0.5)


def test_metrics_research_question_counts(project):
    metrics = compute_metrics(project)
    assert metrics["research_questions"] == {"M01": 1, "M02": 1}


def test_weighted_score_uses_rubric_weights(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it, judge=make_judge(1, coverage=4.0, rigor=3.0))
    scores = score_iteration(project, it)
    assert scores["weighted"] == pytest.approx(0.6 * 4.0 + 0.4 * 3.0)
    assert scores["min_criterion"] == pytest.approx(3.0)
    assert scores["delta"] is None
    assert json.loads((it.path / "scores.json").read_text())["weighted"] == scores["weighted"]


def test_scores_include_deterministic_metrics_and_open_criticals(project):
    it = start_iteration(project, now=FIXED_NOW)
    critical = [{"id": "JD-01-01", "module": "M01", "finding": "No identification strategy at all."}]
    complete_iteration(project, it, judge=make_judge(1, critical=critical))
    scores = score_iteration(project, it)
    assert scores["metrics"]["coverage"] == pytest.approx(2 / 3)
    assert scores["open_critical"] == 1


def test_delta_against_previous_iteration(project):
    first = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, first, judge=make_judge(1, coverage=3.0, rigor=3.0))
    score_iteration(project, first)
    second = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, second, judge=make_judge(2, coverage=4.0, rigor=3.0))
    scores = score_iteration(project, second)
    assert scores["delta"] == pytest.approx(0.6)
    assert scores["criteria_delta"]["coverage"] == pytest.approx(1.0)


def test_scoring_requires_synthesis_and_changelog(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it)
    (it.path / "changelog.md").unlink()
    with pytest.raises(ScoringError, match="changelog"):
        score_iteration(project, it)


def test_scoring_rejects_invalid_judge(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it)
    (it.path / "judge.yaml").write_text("iteration: 1\nscores: {}\n")
    with pytest.raises(ScoringError):
        score_iteration(project, it)
