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


def test_sober_design_no_emojis():
    """Verify strictly sober visual design without decorative emojis or redundant badges."""
    import re
    html = build_full_html()

    # Regex detecting standard emoji unicode ranges and decorative pictographs
    emoji_pattern = re.compile(
        r'[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]'
    )
    emojis = emoji_pattern.findall(html)
    assert len(emojis) == 0, f"Found unexpected emojis in HTML output: {set(emojis)}"

    # Brand navbar must not have UBR ESPAÑA badge, only clean Renta Básica Universal title
    assert "UBR ESPAÑA" not in html
    assert '<span class="brand-title">Renta Básica Universal</span>' in html
    assert "brand-badge" not in html

    # Navbar buttons must have sober text without emoji icons
    assert ">Monografía Académica<" in html
    assert ">Simulador de Políticas<" in html
    assert ">Anteproyecto de Ley<" in html
    assert ">Resumen (ES / EN)<" in html
    assert ">Imprimir / PDF<" in html
    assert ">Código / GitHub<" in html
    assert ">Modo oscuro<" in html

    # Tab 3 search input must not have emoji prefix
    assert 'placeholder="Buscar por artículo' in html
    assert "🔍" not in html


def test_simulator_multiscenario_payload():
    """Verify multi-scenario dashboard payload provides valid decile and CPFF data."""
    import json
    import re
    html = build_full_html()

    # Extract JSON DASHBOARD_DATA
    match = re.search(r"const DASHBOARD_DATA = ({.*?});\n", html, re.DOTALL)
    assert match is not None, "DASHBOARD_DATA constant missing from script"
    data = json.loads(match.group(1))

    assert data.get("current_scenario") == "S2"
    assert "S1" in data["scenarios"]
    assert "S2" in data["scenarios"]
    assert "S3" in data["scenarios"]

    # Verify microsimulation deciles across all 3 scenarios
    for sc in ("S1", "S2", "S3"):
        sc_info = data["microsim_by_scenario"][sc]
        assert sc_info["monthly_rate_eur"] in (600, 900, 1200)
        assert sc_info["child_rate_eur"] in (210, 360, 420)
        assert len(sc_info["deciles"]) == 10
        for d in sc_info["deciles"]:
            assert "decile" in d
            assert "delta_disposable_income_pct" in d
            assert isinstance(d["delta_disposable_income_pct"], (int, float))

    # Verify CPFF equalization across all 3 scenarios
    for sc in ("S1", "S2", "S3"):
        cpff_info = data["cpff_by_scenario"][sc]
        assert cpff_info["total_cpff_fund_size_eur_b"] > 40
        regions = cpff_info["common_regime_regions"]
        assert len(regions) == 15
        for reg in regions:
            assert "name" in reg
            assert reg["population"] > 0
            assert reg["cpff_equalization_transfer_eur_b"] > 0


def test_simulator_interactive_controls_and_scripts():
    """Verify presence of interactive scenario buttons and dynamic simulator elements."""
    html = build_full_html()

    # Interactive scenario selector buttons
    assert 'id="scenarioBtn-S1"' in html
    assert 'id="scenarioBtn-S2"' in html
    assert 'id="scenarioBtn-S3"' in html
    assert "selectScenario('S1')" in html
    assert "selectScenario('S2')" in html
    assert "selectScenario('S3')" in html

    # Dynamic target IDs for live updates
    assert 'id="calcTierBadge"' in html
    assert 'id="grossUbrBreakdown"' in html
    assert 'id="decilesBadge"' in html
    assert 'id="decilesChart"' in html
    assert 'id="decilesBreakevenNote"' in html
    assert 'id="cpffFundBadge"' in html
    assert 'id="cpffPerCapitaNote"' in html
    assert 'id="cpffTableBody"' in html

    # Client-side functions in <script>
    assert "function selectScenario(scId)" in html
    assert "function updateCalculator()" in html
    assert "function updateDecilesChart(deciles)" in html
    assert "function populateCpffTable(regions)" in html
    assert "function toggleTheme()" in html


