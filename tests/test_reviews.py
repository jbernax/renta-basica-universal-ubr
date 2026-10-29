from conftest import FIXED_NOW, complete_iteration, make_review, write_yaml

from ubr.iterations import start_iteration
from ubr.reviews import check_reviews


def test_complete_valid_reviews_pass(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it)
    report = check_reviews(project, it, require_judge=True)
    assert report.errors == []


def test_missing_reviewer_output_is_an_error(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it)
    (it.path / "reviews" / f"{it.reviewers[0]}.yaml").unlink()
    report = check_reviews(project, it)
    assert any(it.reviewers[0] in e.message for e in report.errors)


def test_schema_violation_is_an_error(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it)
    bad = make_review(it.reviewers[0], 1)
    bad["issues"][0]["severity"] = "catastrophic"
    write_yaml(it.path / "reviews" / f"{it.reviewers[0]}.yaml", bad)
    report = check_reviews(project, it)
    assert any("catastrophic" in e.message or "severity" in e.message for e in report.errors)


def test_unknown_module_reference_is_an_error(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it)
    bad = make_review(it.reviewers[0], 1)
    bad["issues"][0]["module"] = "M42"
    write_yaml(it.path / "reviews" / f"{it.reviewers[0]}.yaml", bad)
    assert any("M42" in e.message for e in check_reviews(project, it).errors)


def test_unknown_rubric_criterion_is_an_error(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it)
    bad = make_review(it.reviewers[0], 1, scores={"vibes": {"score": 5, "rationale": "Great vibes overall."}})
    write_yaml(it.path / "reviews" / f"{it.reviewers[0]}.yaml", bad)
    assert any("vibes" in e.message for e in check_reviews(project, it).errors)


def test_reviewer_name_must_match_file(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it)
    write_yaml(it.path / "reviews" / f"{it.reviewers[0]}.yaml", make_review("someone-else", 1))
    assert any("someone-else" in e.message for e in check_reviews(project, it).errors)


def test_judge_must_score_every_criterion_when_required(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it)
    judge_path = it.path / "judge.yaml"
    import yaml

    judge = yaml.safe_load(judge_path.read_text())
    del judge["scores"]["methodological_rigor"]
    write_yaml(judge_path, judge)
    errors = check_reviews(project, it, require_judge=True).errors
    assert any("methodological_rigor" in e.message for e in errors)


def test_missing_judge_only_fails_when_required(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it)
    (it.path / "judge.yaml").unlink()
    assert check_reviews(project, it).errors == []
    assert check_reviews(project, it, require_judge=True).errors
