"""Shared fixtures: every test gets a private, valid mini project it may mutate."""
from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from ubr.project import Project

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE = Path(__file__).parent / "fixtures" / "mini_project"
FIXED_NOW = datetime(2026, 10, 29, 9, 0, tzinfo=timezone.utc)


@pytest.fixture
def project(tmp_path: Path) -> Project:
    root = tmp_path / "proj"
    shutil.copytree(FIXTURE, root)
    shutil.copytree(REPO_ROOT / "harness" / "schemas", root / "harness" / "schemas")
    return Project(root)


def write_yaml(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def make_review(reviewer: str, iteration: int, **overrides) -> dict:
    review = {
        "reviewer": reviewer,
        "iteration": iteration,
        "summary": "A sufficiently long summary of the review findings.",
        "scores": {"coverage": {"score": 3, "rationale": "Covers most factors adequately."}},
        "issues": [
            {
                "id": "AB-01-01",
                "severity": "major",
                "module": "M01",
                "finding": "Alpha lacks an identification strategy.",
                "proposal": "Add an event-study design using EPA microdata.",
            }
        ],
    }
    review.update(overrides)
    return review


def make_judge(iteration: int, coverage: float = 4.0, rigor: float = 3.0, critical=None) -> dict:
    return {
        "iteration": iteration,
        "scores": {
            "coverage": {"score": coverage, "rationale": "Coverage rationale text."},
            "methodological_rigor": {"score": rigor, "rationale": "Rigor rationale text."},
        },
        "critical_issues": critical or [],
        "sota_assessment": "Not yet state of the art; methods need depth.",
    }


def complete_iteration(project: Project, iteration, judge: dict | None = None) -> None:
    """Write the artifacts a finished iteration must contain (reviews, synthesis, changelog, judge)."""
    for reviewer in iteration.reviewers:
        write_yaml(iteration.path / "reviews" / f"{reviewer}.yaml", make_review(reviewer, iteration.number))
    (iteration.path / "synthesis.md").write_text("# Synthesis\n", encoding="utf-8")
    (iteration.path / "changelog.md").write_text("# Changelog\n", encoding="utf-8")
    write_yaml(iteration.path / "judge.yaml", judge or make_judge(iteration.number))
