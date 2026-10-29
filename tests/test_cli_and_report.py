import json

from conftest import FIXED_NOW, complete_iteration, make_judge

from ubr.cli import main
from ubr.iterations import start_iteration
from ubr.report import build_report, status_line
from ubr.scoring import score_iteration


def test_status_line_reflects_empty_open_and_scored_states(project):
    assert "no iterations" in status_line(project).lower()
    it = start_iteration(project, now=FIXED_NOW)
    assert "iter-0001" in status_line(project) and "open" in status_line(project).lower()
    complete_iteration(project, it, judge=make_judge(1, coverage=4.0, rigor=3.5))
    score_iteration(project, it, now=FIXED_NOW)
    line = status_line(project)
    assert "iter-0001" in line and "3.80" in line


def test_report_writes_markdown_with_score_history_and_changelog(project):
    it = start_iteration(project, now=FIXED_NOW)
    complete_iteration(project, it, judge=make_judge(1, coverage=4.0, rigor=3.5))
    (it.path / "changelog.md").write_text("# Changelog\n\n- Applied AB-01-01 to M01.\n", encoding="utf-8")
    (it.path / "proposals-for-human.md").write_text("- Unlock M02 to add regional elasticity.\n", encoding="utf-8")
    score_iteration(project, it, now=FIXED_NOW)
    out = build_report(project)
    text = out.read_text(encoding="utf-8")
    assert out == project.iterations_dir / "REPORT.md"
    assert "iter-0001" in text
    assert "3.80" in text
    assert "Applied AB-01-01" in text
    assert "Unlock M02" in text


def test_cli_end_to_end_cycle(project, monkeypatch, capsys):
    monkeypatch.setenv("UBR_ROOT", str(project.root))
    assert main(["validate"]) == 0
    assert main(["iteration", "start"]) == 0
    it = project.iterations_dir / "iter-0001"
    assert it.is_dir()

    from ubr.iterations import resolve_iteration

    complete_iteration(project, resolve_iteration(project, "1"))
    assert main(["reviews", "check", "iter-0001", "--judge"]) == 0
    assert main(["score", "iter-0001"]) == 0
    assert main(["stop-check", "iter-0001"]) == 0
    out = capsys.readouterr().out
    assert "outcome: continue" in out

    assert main(["metrics", "--json"]) == 0
    metrics = json.loads(capsys.readouterr().out)
    assert metrics["modules"] == 2

    assert main(["sources", "verify", "--offline"]) == 0
    assert main(["report"]) == 0
    assert (project.iterations_dir / "REPORT.md").is_file()
    assert main(["checkpoint", "--note", "Reviewed cycle 1"]) == 0
    assert main(["status"]) == 0
