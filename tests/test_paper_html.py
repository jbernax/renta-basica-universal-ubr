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


def test_anteproyecto_articles_rendered():
    """Regression test ensuring all 25 articles, provisions, and preamble are fully rendered."""
    import re
    html = build_full_html()

    # Verify all 25 articles are present with non-empty headings and bodies
    for i in range(1, 26):
        pattern = rf"<h4>Artículo {i}: ([^<]+)</h4>"
        match = re.search(pattern, html)
        assert match is not None, f"Article {i} header missing or empty"
        assert len(match.group(1).strip()) > 3, f"Article {i} title too short: {match.group(1)}"
        assert f'id="art_{i:02d}"' in html, f"Article card id art_{i:02d} missing"

    # Regression check: verify no empty article body tags exist
    assert not re.search(r'<div class="article-body">\s*<p>\s*</p>\s*</div>', html)
    assert not re.search(r'<h4>Artículo \d+: \s*</h4>', html)

    # Verify dispositions and preamble
    assert "Disposición Adicional Primera: Proyecto de Ley Orgánica" in html
    assert "Disposición Transitoria Primera: Calendario de implantación" in html
    assert "Disposición Derogatoria Única: Derogación normativa" in html
    assert "Disposición Final Primera: Títulos competenciales" in html
    assert "preamble-box" in html
    assert "Marco de Transformación Tecnológica" in html

    # Verify constitutional and statutory badges
    assert 'class="legal-badge"' in html
    assert 'class="statute-badge"' in html
    assert "Art. 149.1.1 CE" in html

