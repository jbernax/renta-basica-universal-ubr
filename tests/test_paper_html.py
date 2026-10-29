"""Tests for HTML monograph compilation and interactive dashboard."""
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.build_html import build_full_html, load_sources, main as build_html_main


def test_sources_load_non_empty():
    sources = load_sources()
    assert len(sources) > 50
    assert "acemoglu-restrepo-2019" in sources
    assert "tc-stc-158-2021-imv" in sources


def test_build_full_html_output():
    html = build_full_html()
    assert len(html) > 100000
    assert "Renta Básica Universal" in html
    assert "tab-monograph" in html
    assert "tab-dashboard" in html
    assert "tab-anteproyecto" in html
    assert "katex.min.css" in html
    assert "chart.umd.min.js" in html
    assert "class=\"citation-ref\"" in html
    assert "DASHBOARD_DATA" in html


def test_build_script_emits_files():
    build_html_main()
    docs_html = REPO_ROOT / "docs" / "index.html"
    paper_html = REPO_ROOT / "paper" / "index.html"
    assert docs_html.exists()
    assert docs_html.stat().st_size > 100000
    assert paper_html.exists()
    assert paper_html.stat().st_size > 100000
