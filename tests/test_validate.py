from conftest import FIXED_NOW

from ubr.iterations import start_iteration
from ubr.validate import validate_plan


def module_path(project, module_id):
    return next(project.modules_dir.glob(f"{module_id}-*.md"))


def replace_in(path, old, new):
    text = path.read_text(encoding="utf-8")
    assert old in text, f"fixture drift: {old!r} not in {path.name}"
    path.write_text(text.replace(old, new), encoding="utf-8")


def error_messages(project):
    return [f.message for f in validate_plan(project).errors]


def test_valid_plan_has_no_errors(project):
    report = validate_plan(project)
    assert report.errors == []
    assert report.ok


def test_uncited_source_is_only_a_warning(project):
    report = validate_plan(project)
    assert any("src-unused" in w.message for w in report.warnings)


def test_missing_required_section_is_an_error(project):
    replace_in(module_path(project, "M01"), "## 5. Methods & identification", "## 5. Approach")
    assert any("Methods & identification" in m for m in error_messages(project))


def test_duplicate_research_question_ids_are_an_error(project):
    replace_in(module_path(project, "M02"), "RQ-M02-01", "RQ-M01-01")
    assert any("RQ-M01-01" in m and "duplicate" in m.lower() for m in error_messages(project))


def test_research_question_must_carry_its_module_prefix(project):
    replace_in(module_path(project, "M01"), "RQ-M01-01", "RQ-M09-01")
    assert any("RQ-M09-01" in m for m in error_messages(project))


def test_research_question_without_hypothesis_is_an_error(project):
    replace_in(module_path(project, "M01"), "*Hypothesis:* Yes, alpha holds.", "*Note:* none.")
    assert any("hypothesis" in m.lower() for m in error_messages(project))


def test_too_few_research_questions_is_an_error(project):
    replace_in(
        module_path(project, "M01"),
        "- **RQ-M01-01**: Does alpha hold?\n  - *Hypothesis:* Yes, alpha holds.\n",
        "No questions yet.\n",
    )
    assert any("research question" in m.lower() for m in error_messages(project))


def test_dangling_citation_is_an_error(project):
    replace_in(module_path(project, "M01"), "[@src-a; @src-b]", "[@src-a; @ghost-2024]")
    assert any("ghost-2024" in m for m in error_messages(project))


def test_unknown_dependency_is_an_error(project):
    replace_in(module_path(project, "M01"), "depends_on: [M02]", "depends_on: [M77]")
    assert any("M77" in m for m in error_messages(project))


def test_unknown_reference_factor_is_an_error(project):
    replace_in(module_path(project, "M01"), "covers: [F01]", "covers: [F99]")
    assert any("F99" in m for m in error_messages(project))


def test_invalid_frontmatter_is_an_error(project):
    replace_in(module_path(project, "M01"), "status: draft", "status: finished")
    assert any("frontmatter" in m.lower() for m in error_messages(project))


def test_module_missing_from_manifest_is_an_error(project):
    replace_in(project.plan_dir / "plan.yaml", "modules: [M01, M02]", "modules: [M01]")
    assert any("M02" in m and "manifest" in m.lower() for m in error_messages(project))


def test_duplicate_source_ids_are_an_error(project):
    replace_in(project.plan_dir / "sources.yaml", "id: src-unused", "id: src-a")
    assert any("src-a" in m and "duplicate" in m.lower() for m in error_messages(project))


class TestLockEnforcementDuringOpenIteration:
    def test_editing_unlocked_module_is_allowed(self, project):
        start_iteration(project, now=FIXED_NOW)
        replace_in(module_path(project, "M01"), "Alpha matters.", "Alpha matters a lot.")
        assert error_messages(project) == []

    def test_editing_locked_module_is_an_error(self, project):
        start_iteration(project, now=FIXED_NOW)
        replace_in(module_path(project, "M02"), "Beta matters.", "Beta matters less.")
        assert any("locked" in m.lower() and "M02" in m for m in error_messages(project))

    def test_unlocking_a_locked_module_is_an_error(self, project):
        start_iteration(project, now=FIXED_NOW)
        replace_in(module_path(project, "M02"), "locked: true", "locked: false")
        assert any("locked" in m.lower() for m in error_messages(project))

    def test_deleting_a_locked_module_is_an_error(self, project):
        start_iteration(project, now=FIXED_NOW)
        replace_in(project.plan_dir / "plan.yaml", "modules: [M01, M02]", "modules: [M01]")
        module_path(project, "M02").unlink()
        assert any("locked" in m.lower() and "M02" in m for m in error_messages(project))

    def test_editing_decisions_is_an_error(self, project):
        start_iteration(project, now=FIXED_NOW)
        replace_in(project.plan_dir / "decisions.md", "D-001", "D-001 (edited by AI)")
        assert any("decisions.md" in m for m in error_messages(project))

    def test_humans_may_edit_locked_files_between_iterations(self, project):
        replace_in(module_path(project, "M02"), "Beta matters.", "Beta matters (human edit).")
        replace_in(project.plan_dir / "decisions.md", "D-001", "D-001 (human edit)")
        assert error_messages(project) == []
