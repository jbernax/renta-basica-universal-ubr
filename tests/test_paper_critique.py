"""Unit tests for the adversarial paper critique harness."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from ubr.paper_critique import (
    PaperCritiqueError,
    check_paper_reviews,
    list_paper_iterations,
    resolve_paper_iteration,
    score_paper_iteration,
    start_paper_iteration,
)
from ubr.project import Project, dump_yaml


@pytest.fixture
def temp_project(tmp_path: Path) -> Project:
    root = tmp_path / "repo"
    root.mkdir()

    # Create harness structure
    harness = root / "harness"
    harness.mkdir()
    shutil.copy2(Path("harness/config.yaml"), harness / "config.yaml")
    shutil.copy2(Path("harness/paper_rubric.yaml"), harness / "paper_rubric.yaml")
    schemas = harness / "schemas"
    schemas.mkdir()
    shutil.copy2(Path("harness/schemas/paper_review.schema.json"), schemas / "paper_review.schema.json")
    shutil.copy2(Path("harness/schemas/paper_judge.schema.json"), schemas / "paper_judge.schema.json")

    # Create mock paper directory with sample chapters
    paper = root / "paper"
    paper.mkdir()
    (paper / "ch00-executive-summary.md").write_text("# Chapter 0\nExecutive summary.", encoding="utf-8")
    (paper / "ch01-introduction-analytical-framework.md").write_text("# Chapter 1\nIntro text.", encoding="utf-8")
    (paper / "ch04-fiscal-architecture-ai-rent-capture.md").write_text("# Chapter 4\nFiscal bridge.", encoding="utf-8")

    return Project(root)


def test_start_paper_iteration(temp_project: Project):
    it = start_paper_iteration(temp_project)
    assert it.number == 1
    assert it.id == "iter-0001"
    assert it.is_open is True
    assert it.bundle_path.is_file()
    assert (it.snapshot_paper / "ch00-executive-summary.md").is_file()
    assert len(it.reviewers) == 5

    # Cannot start another while it-0001 is open
    with pytest.raises(PaperCritiqueError):
        start_paper_iteration(temp_project)


def test_check_paper_reviews_and_judge(temp_project: Project):
    it = start_paper_iteration(temp_project, reviewers=["adversarial-fiscal"])

    # Missing review
    rep = check_paper_reviews(temp_project, it)
    assert not rep.ok

    # Provide valid review
    review_data = {
        "reviewer": "adversarial-fiscal",
        "iteration": 1,
        "summary": "This is an adversarial analysis of the fiscal sustainability.",
        "scores": {
            "fiscal_realism_sustainability": {
                "score": 3.5,
                "rationale": "Reasonable baseline but vulnerable to dynamic revenue leakage.",
            }
        },
        "issues": [
            {
                "id": "ADV-FISCAL-01-01",
                "severity": "major",
                "chapter": "ch04",
                "finding": "Dynamic ETI is assumed to be zero for compute levies.",
                "counterargument_or_flaw": "Hyperscalers can reroute compute workloads outside Spain.",
                "proposed_amendment": "Introduce statutory destination-based compute reverse-charge safeguards.",
            }
        ],
    }
    dump_yaml(it.path / "reviews" / "adversarial-fiscal.yaml", review_data)

    rep2 = check_paper_reviews(temp_project, it)
    assert rep2.ok

    # Invalid chapter ref
    review_data_bad = dict(review_data)
    review_data_bad["issues"] = [
        {
            "id": "ADV-FISCAL-01-01",
            "severity": "major",
            "chapter": "ch99",
            "finding": "Invalid chapter reference.",
            "counterargument_or_flaw": "Some flaw.",
            "proposed_amendment": "Some amendment.",
        }
    ]
    dump_yaml(it.path / "reviews" / "adversarial-fiscal.yaml", review_data_bad)
    rep3 = check_paper_reviews(temp_project, it)
    assert not rep3.ok


def test_score_paper_iteration(temp_project: Project):
    it = start_paper_iteration(temp_project, reviewers=["adversarial-fiscal"])

    # Provide review
    dump_yaml(
        it.path / "reviews" / "adversarial-fiscal.yaml",
        {
            "reviewer": "adversarial-fiscal",
            "iteration": 1,
            "summary": "Detailed fiscal review with critical stress testing.",
            "scores": {
                "fiscal_realism_sustainability": {
                    "score": 4.0,
                    "rationale": "High quality fiscal defense under dynamic scoring.",
                }
            },
            "issues": [
                {
                    "id": "ADV-FISCAL-01-01",
                    "severity": "minor",
                    "chapter": "ch04",
                    "finding": "Minor parameter uncertainty in reverse-charge compute base.",
                    "counterargument_or_flaw": "Cross-border compliance friction.",
                    "proposed_amendment": "Add OECD BEPS Pillar 1 harmonization cross-reference.",
                }
            ],
        },
    )

    # Required artifacts
    (it.path / "synthesis.md").write_text("# Synthesis\nActionable amendments.", encoding="utf-8")
    (it.path / "changelog.md").write_text("# Changelog\nApplied amendments.", encoding="utf-8")

    # Provide judge verdict
    judge_data = {
        "iteration": 1,
        "scores": {
            "fiscal_realism_sustainability": {"score": 4.2, "rationale": "Strong fiscal bridge."},
            "administrative_feasibility": {"score": 3.8, "rationale": "Solid AEAT/INSS protocol."},
            "legal_robustness_anti_abuse": {"score": 4.5, "rationale": "Clear constitutional competence."},
            "macro_productivity_incentives": {"score": 4.0, "rationale": "Microfounded labor supply bounds."},
            "housing_rent_resilience": {"score": 3.7, "rationale": "Credible benchmark and supply link."},
            "argumentative_rigor_honesty": {"score": 4.6, "rationale": "Honest engagement with skeptics."},
        },
        "critical_vulnerabilities": [
            {
                "id": "ADV-JD-01-01",
                "chapter": "ch05",
                "vulnerability": "Rental supply elasticity assumptions in prime tourist urban areas.",
            }
        ],
        "top_required_revisions": [
            "Clarify seasonal lease anti-evasion under Ley 12/2023.",
        ],
        "overall_robustness_verdict": "The monograph demonstrates high adversarial resistance against standard orthodox critiques.",
    }
    dump_yaml(it.path / "judge.yaml", judge_data)

    scores = score_paper_iteration(temp_project, it)
    assert scores["iteration"] == 1
    assert scores["weighted"] > 3.9
    assert scores["critical_vulnerabilities"] == 1
    assert (it.path / "scores.json").is_file()
    assert (temp_project.root / "paper_iterations" / "REPORT.md").is_file()
    assert it.is_open is False
