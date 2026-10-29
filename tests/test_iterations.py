import pytest
import yaml
from conftest import FIXED_NOW, complete_iteration

from ubr.iterations import (
    IterationError,
    last_checkpoint,
    list_iterations,
    record_checkpoint,
    resolve_iteration,
    select_reviewers,
    start_iteration,
)
from ubr.scoring import score_iteration

PANEL_CFG = {
    "panel": ["a", "b", "c", "d", "e", "f", "red-team"],
    "always_include": ["red-team"],
    "rotation": 4,
    "full_panel_every": 3,
    "first_iteration_full_panel": False,
}


def test_first_iteration_is_numbered_0001_and_snapshots_the_plan(project):
    iteration = start_iteration(project, now=FIXED_NOW)
    assert iteration.id == "iter-0001"
    snap = iteration.path / "snapshot" / "plan" / "modules" / "M01-alpha.md"
    assert snap.read_text() == next(project.modules_dir.glob("M01-*.md")).read_text()
    assert (iteration.path / "reviews").is_dir()


def test_bundle_contains_every_module_and_the_scope(project):
    iteration = start_iteration(project, now=FIXED_NOW)
    bundle = (iteration.path / "bundle.md").read_text()
    assert "Alpha matters." in bundle
    assert "Beta matters." in bundle
    assert "The mini plan studies alpha" in bundle
    assert "src-a" in bundle


def test_manifest_records_selected_reviewers(project):
    iteration = start_iteration(project, now=FIXED_NOW)
    manifest = yaml.safe_load((iteration.path / "manifest.yaml").read_text())
    assert manifest["iteration"] == 1
    assert manifest["reviewers"] == iteration.reviewers
    assert "red-team" in manifest["reviewers"]


def test_cannot_start_while_previous_iteration_is_open(project):
    start_iteration(project, now=FIXED_NOW)
    with pytest.raises(IterationError, match="open"):
        start_iteration(project, now=FIXED_NOW)


def test_next_iteration_after_scoring_is_0002(project):
    first = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, first)
    score_iteration(project, first)
    second = start_iteration(project, now=FIXED_NOW)
    assert second.id == "iter-0002"
    assert [i.id for i in list_iterations(project)] == ["iter-0001", "iter-0002"]


def test_resolve_iteration_accepts_several_reference_styles(project):
    start_iteration(project, now=FIXED_NOW)
    for ref in ("iter-0001", "0001", "1", "latest", None):
        assert resolve_iteration(project, ref).number == 1
    with pytest.raises(IterationError):
        resolve_iteration(project, "7")


class TestReviewerRotation:
    def test_rotation_size_and_always_included(self):
        for n in (1, 2, 4, 5):
            chosen = select_reviewers(PANEL_CFG, n)
            assert len(chosen) == 4
            assert "red-team" in chosen
            assert len(set(chosen)) == 4

    def test_full_panel_on_schedule(self):
        assert sorted(select_reviewers(PANEL_CFG, 3)) == sorted(PANEL_CFG["panel"])
        assert sorted(select_reviewers(PANEL_CFG, 6)) == sorted(PANEL_CFG["panel"])

    def test_first_iteration_full_panel_when_configured(self):
        cfg = {**PANEL_CFG, "first_iteration_full_panel": True}
        assert sorted(select_reviewers(cfg, 1)) == sorted(PANEL_CFG["panel"])

    def test_rotation_is_deterministic(self):
        assert select_reviewers(PANEL_CFG, 4) == select_reviewers(PANEL_CFG, 4)

    def test_every_panelist_is_used_within_two_rotating_iterations(self):
        used = set(select_reviewers(PANEL_CFG, 1)) | set(select_reviewers(PANEL_CFG, 2))
        assert used == set(PANEL_CFG["panel"])


def test_checkpoints_are_recorded(project):
    assert last_checkpoint(project) == 0
    first = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, first)
    score_iteration(project, first)
    record_checkpoint(project, note="looks good", now=FIXED_NOW)
    assert last_checkpoint(project) == 1
