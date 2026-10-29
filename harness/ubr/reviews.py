"""Contract checks for reviewer and judge outputs of an iteration."""
from __future__ import annotations

from pathlib import Path

import jsonschema
import yaml

from ubr.findings import Report
from ubr.iterations import Iteration
from ubr.plan_model import module_files
from ubr.project import Project


def check_reviews(project: Project, iteration: Iteration, require_judge: bool = False) -> Report:
    report = Report()
    module_ids = {p.name[:3] for p in module_files(project)}
    criteria = set(project.criterion_ids)
    reviews_dir = iteration.path / "reviews"
    expected = iteration.reviewers

    for reviewer in expected:
        if not (reviews_dir / f"{reviewer}.yaml").is_file():
            report.error(f"{iteration.id}/reviews", f"missing review from {reviewer}")
    for path in sorted(reviews_dir.glob("*.yaml")):
        if path.stem not in expected:
            report.warn(_where(iteration, path), f"unexpected review file (not in manifest reviewers)")
        _check_review(project, iteration, path, module_ids, criteria, report)

    judge_path = iteration.path / "judge.yaml"
    if judge_path.is_file():
        _check_judge(project, iteration, judge_path, module_ids, criteria, report)
    elif require_judge:
        report.error(iteration.id, "judge.yaml missing")
    return report


def _where(iteration: Iteration, path: Path) -> str:
    return f"{iteration.id}/{path.relative_to(iteration.path).as_posix()}"


def _load(path: Path, where: str, report: Report):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        report.error(where, f"invalid YAML: {exc}")
        return None


def _schema_errors(project: Project, name: str, data, where: str, report: Report) -> bool:
    errors = list(jsonschema.Draft202012Validator(project.schema(name)).iter_errors(data))
    for err in errors:
        loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
        report.error(where, f"{loc}: {err.message}")
    return bool(errors)


def _check_module_ref(module: str, module_ids: set[str], where: str, ref: str, report: Report) -> None:
    if module.startswith("M") and module not in module_ids:
        report.error(where, f"{ref} references unknown module {module}")


def _check_review(project, iteration, path, module_ids, criteria, report) -> None:
    where = _where(iteration, path)
    data = _load(path, where, report)
    if data is None or _schema_errors(project, "review", data, where, report):
        return
    if data["reviewer"] != path.stem:
        report.error(where, f"reviewer field '{data['reviewer']}' does not match file name '{path.stem}'")
    if data["iteration"] != iteration.number:
        report.error(where, f"iteration field {data['iteration']} != {iteration.number}")
    for criterion in data["scores"]:
        if criterion not in criteria:
            report.error(where, f"unknown rubric criterion '{criterion}'")
    for issue in data["issues"]:
        _check_module_ref(issue["module"], module_ids, where, issue["id"], report)


def _check_judge(project, iteration, path, module_ids, criteria, report) -> None:
    where = _where(iteration, path)
    data = _load(path, where, report)
    if data is None or _schema_errors(project, "judge", data, where, report):
        return
    if data["iteration"] != iteration.number:
        report.error(where, f"iteration field {data['iteration']} != {iteration.number}")
    scored = set(data["scores"])
    for criterion in sorted(criteria - scored):
        report.error(where, f"judge did not score criterion '{criterion}'")
    for criterion in sorted(scored - criteria):
        report.error(where, f"unknown rubric criterion '{criterion}'")
    for issue in data["critical_issues"]:
        _check_module_ref(issue["module"], module_ids, where, issue["id"], report)
