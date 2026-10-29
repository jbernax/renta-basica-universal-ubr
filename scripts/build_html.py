#!/usr/bin/env python3
"""Build publication-ready HTML monograph and interactive policy dashboard for Universal Basic Rent (Spain).

Reads:
  - paper/monograph.md
  - plan/sources.yaml
  - data/*.json
Outputs:
  - docs/index.html (for GitHub Pages)
  - paper/index.html (local reference)
"""

from __future__ import annotations

import html as html_lib
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List

import markdown
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent


def load_sources() -> Dict[str, Dict[str, Any]]:
    sources_file = REPO_ROOT / "plan" / "sources.yaml"
    if not sources_file.exists():
        return {}
    with open(sources_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if isinstance(data, dict) and "sources" in data:
        items = data["sources"]
    elif isinstance(data, list):
        items = data
    else:
        return {}
    return {item["id"]: item for item in items if isinstance(item, dict) and "id" in item}


def format_authors(raw: list[str]) -> str:
    if not raw:
        return "Institutional"
    if len(raw) >= 2 and len(raw[1]) <= 3 and "." in raw[1]:
        pairs = []
        for i in range(0, len(raw), 2):
            if i + 1 < len(raw):
                pairs.append(f"{raw[i]}, {raw[i+1]}")
            else:
                pairs.append(raw[i])
        return " & ".join(pairs)
    return ", ".join(raw)


def format_author_short(raw: list[str], year: Any, key: str) -> str:
    yr_str = str(year) if year else "n.d."
    if not raw:
        return f"{key} ({yr_str})"
    if len(raw) >= 2 and len(raw[1]) <= 3 and "." in raw[1]:
        lasts = [raw[i] for i in range(0, len(raw), 2)]
    else:
        lasts = [name.split()[-1] for name in raw]
    if len(lasts) > 2:
        return f"{lasts[0]} et al. ({yr_str})"
    elif len(lasts) == 2:
        return f"{lasts[0]} & {lasts[1]} ({yr_str})"
    return f"{lasts[0]} ({yr_str})"


def format_source_citation(source: Dict[str, Any]) -> str:
    authors = format_authors(source.get("authors", []))
    year = source.get("year", "n.d.")
    title = source.get("title", "")
    venue = source.get("venue", "")
    doi = source.get("doi", "")
    url = source.get("url", "")
    
    parts = [f"<strong>{authors} ({year})</strong>. <em>{title}</em>."]
    if venue:
        parts.append(f"{venue}.")
    if doi:
        parts.append(f'<a href="https://doi.org/{doi}" target="_blank" rel="noopener">doi:{doi}</a>')
    elif url:
        parts.append(f'<a href="{url}" target="_blank" rel="noopener">URL</a>')
    return " ".join(parts)


def process_citations(text: str, sources_by_id: Dict[str, Dict[str, Any]]) -> str:
    """Replace [@key] and [@k1; @k2] with interactive HTML links and data attributes."""
    
    def replace_citation_group(match: re.Match) -> str:
        group_content = match.group(1)
        keys = [k.strip().lstrip("@") for k in group_content.split(";")]
        rendered = []
        for key in keys:
            if key in sources_by_id:
                s = sources_by_id[key]
                short_label = format_author_short(s.get("authors", []), s.get("year", ""), key)
                full_cit = html_lib.escape(format_source_citation(s))
                rendered.append(
                    f'<a class="citation-ref" href="#ref-{key}" '
                    f'data-tooltip="{full_cit}" title="{short_label}">@{key}</a>'
                )
            else:
                rendered.append(f'<span class="citation-ref unknown" title="External Reference">@{key}</span>')
        return f'<span class="citation-bracket">[{"; ".join(rendered)}]</span>'

    # Match [@key] or [@k1; @k2; ...]
    pattern = r"\[(@[a-zA-Z0-9_\-]+(?:\s*;\s*@[a-zA-Z0-9_\-]+)*)\]"
    processed = re.sub(pattern, replace_citation_group, text)
    
    # Also inject anchor targets into the Bibliography section items
    ref_pattern = r"- \*\*\[([a-zA-Z0-9_\-]+)\]\*\*"
    processed = re.sub(ref_pattern, r'- <div id="ref-\1" class="reference-anchor"></div>**[\1]**', processed)
    
    return processed


def process_alerts(html_content: str) -> str:
    """Convert blockquote alerts [!NOTE], [!IMPORTANT], etc. to styled cards."""
    alert_types = {
        "NOTE": ("alert-note", "ℹ️"),
        "TIP": ("alert-tip", "💡"),
        "IMPORTANT": ("alert-important", "📌"),
        "WARNING": ("alert-warning", "⚠️"),
        "CAUTION": ("alert-caution", "🛑"),
    }
    for atype, (css_class, icon) in alert_types.items():
        pattern = re.compile(
            rf"<blockquote>\s*<p>\[!{atype}\]\s*(.*?)</p>\s*</blockquote>",
            re.DOTALL | re.IGNORECASE,
        )
        html_content = pattern.sub(
            rf'<div class="callout {css_class}"><div class="callout-header"><span class="callout-icon">{icon}</span><strong>{atype}</strong></div><div class="callout-body"><p>\1</p></div></div>',
            html_content,
        )
    return html_content


def load_json_data(filename: str) -> Dict[str, Any]:
    path = REPO_ROOT / "data" / filename
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def build_full_html() -> str:
    sources_by_id = load_sources()
    
    # Load data artifacts
    s1_data = load_json_data("counterfactual_s1.json")
    s2_data = load_json_data("counterfactual_s2.json")
    s3_data = load_json_data("counterfactual_s3.json")
    microsim_s2 = load_json_data("microsim_tier_b_s2.json")
    cpff_data = load_json_data("legal_cpff_equalization.json")
    bicameral_data = load_json_data("legal_bicameral_coalitions.json")
    anteproyecto_data = load_json_data("legal_anteproyecto_corpus.json")
    pilot_clusters = load_json_data("pilot_clusters_j70.json")
    
    # Read monograph markdown
    mono_path = REPO_ROOT / "paper" / "monograph.md"
    with open(mono_path, "r", encoding="utf-8") as f:
        mono_raw = f.read()
    
    # Split YAML front matter if present
    front_matter = {}
    body_md = mono_raw
    if mono_raw.startswith("---"):
        parts = mono_raw.split("---", 2)
        if len(parts) >= 3:
            try:
                front_matter = yaml.safe_load(parts[1]) or {}
            except Exception:
                pass
            body_md = parts[2]
            
    # Process citations before markdown parsing
    processed_md = process_citations(body_md, sources_by_id)
    
    # Render markdown with extensions
    md_parser = markdown.Markdown(
        extensions=[
            "extra",
            "tables",
            "fenced_code",
            "toc",
            "smarty",
            "attr_list",
        ]
    )
    rendered_body_html = md_parser.convert(processed_md)
    rendered_body_html = process_alerts(rendered_body_html)
    
    # Build Table of Contents navigation items
    toc_items = []
    chapter_headers = [
        ("Executive Summary (EN)", "1-executive-summary-english"),
        ("Resumen Ejecutivo (ES)", "2-resumen-ejecutivo-para-decisores-publicos-espanol"),
        ("Ch 1: Analytical Framework", "chapter-1-introduction-analytical-framework-welfare-states-when-ai-compresses-labor-income"),
        ("Ch 2: The AI Shock in Spain", "chapter-2-the-ai-shock-in-spain-occupational-exposure-wage-bill-scenarios-s1s3-and-fiscal-drag"),
        ("Ch 3: Benefit Architecture", "chapter-3-benefit-architecture-welfare-integration-replacing-poverty-traps-under-a-no-loser-constraint"),
        ("Ch 4: Fiscal Architecture & Taxes", "chapter-4-fiscal-architecture-ai-rent-capture-from-labor-taxation-to-capital-and-compute-dividends"),
        ("Ch 5: Macro & Housing", "chapter-5-macroeconomic-closure-housing-markets-in-the-eurozone-demand-stabilization-vs-rent-capture"),
        ("Ch 6: Constitutional Blueprint", "chapter-6-constitutional-territorial-and-eu-legal-blueprint-common-vs-foral-regimes-and-free-movement"),
        ("Ch 7: Multi-Level Pilot", "chapter-7-multi-level-pilot-causal-evaluation-design-municipal-autonomous-community-and-national-options"),
        ("Ch 8: Political Economy", "chapter-8-political-economy-phased-transition-and-tail-risk-governance"),
        ("References / Bibliografía", "references-machine-verified-academic-statutory-bibliography"),
    ]
    for label, slug in chapter_headers:
        toc_items.append(f'<li><a href="#{slug}" class="toc-link">{label}</a></li>')
    toc_html = "\n".join(toc_items)
    
    # Prepare JSON payloads for client-side interactivity
    dashboard_payload = {
        "scenarios": {
            "S1": s1_data.get("metrics", {}),
            "S2": s2_data.get("metrics", {}),
            "S3": s3_data.get("metrics", {}),
        },
        "microsim_deciles": microsim_s2.get("deciles", []),
        "poverty": microsim_s2.get("poverty_and_inequality", {}),
        "cpff": cpff_data,
        "bicameral": bicameral_data,
        "pilot_summary": {
            "total_clusters": pilot_clusters.get("total_clusters", 70),
            "fua_count": pilot_clusters.get("fua_count", 7),
            "rural_count": pilot_clusters.get("rural_municipality_count", 30),
            "clusters": pilot_clusters.get("clusters", [])[:15],
        },
    }
    dashboard_json = json.dumps(dashboard_payload)
    
    # Format Anteproyecto titles for Tab 3
    anteproyecto_titles = anteproyecto_data.get("titles", [])
    anteproyecto_html_parts = []
    for t in anteproyecto_titles:
        t_num = t.get("title_number", "")
        t_heading = t.get("heading", "")
        t_desc = t.get("description", "")
        articles = t.get("articles", [])
        
        art_cards = []
        for art in articles:
            num = art.get("article_number", "")
            title = art.get("title", "")
            content = art.get("content", "").replace("\n", "<br>")
            anchors = ", ".join(art.get("competence_anchors", []))
            
            art_cards.append(f"""
            <div class="article-card" data-search-text="{num.lower()} {title.lower()} {anchors.lower()}">
                <div class="article-header">
                    <h4>{num}: {title}</h4>
                    {f'<span class="legal-badge">{anchors}</span>' if anchors else ''}
                </div>
                <div class="article-body">
                    <p>{content}</p>
                </div>
            </div>
            """)
        
        anteproyecto_html_parts.append(f"""
        <div class="title-group">
            <div class="title-heading">
                <h3>{t_num}: {t_heading}</h3>
                <p class="title-desc">{t_desc}</p>
            </div>
            <div class="articles-container">
                {"".join(art_cards)}
            </div>
        </div>
        """)
    anteproyecto_html = "\n".join(anteproyecto_html_parts)
    
    # Assembling the HTML template
    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Renta Básica Universal (UBR) en España | Monografía y Simulador</title>
    <meta name="description" content="Diseño institucional, arquitectura fiscal y evaluación piloto multinivel de la Renta Básica Universal ante la disrupción de la IA en España.">
    <meta name="author" content="Universal Basic Rent (Spain) Research Program">
    
    <!-- KaTeX for LaTeX Math -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"
        onload="renderMathInElement(document.body, {{
            delimiters: [
                {{left: '$$', right: '$$', display: true}},
                {{left: '$', right: '$', display: false}},
                {{left: '\\\\(', right: '\\\\)', display: false}},
                {{left: '\\\\[', right: '\\\\]', display: true}}
            ],
            throwOnError: false
        }});"></script>

    <!-- Chart.js for Interactive Policy Visualizations -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>

    <style>
        :root {{
            --bg-body: #f8fafc;
            --bg-card: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --primary-light: #eff6ff;
            --accent: #059669;
            --accent-light: #ecfdf5;
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            --font-serif: Charter, 'Bitstream Charter', 'Sitka Text', Cambria, Georgia, serif;
            --radius-md: 8px;
            --radius-lg: 12px;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08);
            --sidebar-width: 290px;
        }}

        [data-theme="dark"] {{
            --bg-body: #0b0f19;
            --bg-card: #151d30;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
            --border-color: #263352;
            --primary: #3b82f6;
            --primary-hover: #60a5fa;
            --primary-light: #1e293b;
            --accent: #10b981;
            --accent-light: #064e3b;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.4);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.6);
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: var(--font-sans);
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.65;
            transition: background-color 0.2s, color 0.2s;
        }}

        /* Header Navigation */
        .top-navbar {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--bg-card);
            border-bottom: 1px solid var(--border-color);
            padding: 0.75rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: var(--shadow-sm);
        }}
        .brand-container {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        .brand-badge {{
            background: linear-gradient(135deg, #2563eb, #059669);
            color: white;
            font-weight: 700;
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
            font-size: 0.85rem;
            letter-spacing: 0.05em;
        }}
        .brand-title {{
            font-weight: 700;
            font-size: 1.05rem;
            color: var(--text-main);
        }}
        .nav-tabs {{
            display: flex;
            gap: 0.5rem;
        }}
        .nav-tab-btn {{
            background: transparent;
            border: 1px solid transparent;
            color: var(--text-muted);
            padding: 0.45rem 0.9rem;
            border-radius: var(--radius-md);
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.15s ease;
        }}
        .nav-tab-btn:hover {{
            background: var(--primary-light);
            color: var(--primary);
        }}
        .nav-tab-btn.active {{
            background: var(--primary-light);
            border-color: var(--primary);
            color: var(--primary);
        }}
        .header-actions {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .btn-action {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            background: var(--bg-body);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 0.4rem 0.75rem;
            border-radius: var(--radius-md);
            font-size: 0.85rem;
            font-weight: 500;
            text-decoration: none;
            cursor: pointer;
            transition: background 0.15s;
        }}
        .btn-action:hover {{
            background: var(--primary-light);
            border-color: var(--primary);
            color: var(--primary);
        }}

        /* App View Sections */
        .tab-content {{ display: none; }}
        .tab-content.active {{ display: block; }}

        /* Layout for Monograph Reader */
        .monograph-layout {{
            display: flex;
            max-width: 1440px;
            margin: 0 auto;
        }}
        .sidebar-toc {{
            width: var(--sidebar-width);
            flex-shrink: 0;
            position: sticky;
            top: 61px;
            height: calc(100vh - 61px);
            overflow-y: auto;
            border-right: 1px solid var(--border-color);
            padding: 1.5rem 1rem;
            background: var(--bg-card);
        }}
        .sidebar-title {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-muted);
            font-weight: 700;
            margin-bottom: 0.75rem;
        }}
        .toc-list {{
            list-style: none;
        }}
        .toc-list li {{
            margin-bottom: 0.35rem;
        }}
        .toc-link {{
            display: block;
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.85rem;
            padding: 0.35rem 0.5rem;
            border-radius: 4px;
            line-height: 1.35;
            transition: all 0.15s;
        }}
        .toc-link:hover, .toc-link.active {{
            background: var(--primary-light);
            color: var(--primary);
            font-weight: 600;
        }}
        .main-reader {{
            flex: 1;
            max-width: 860px;
            margin: 0 auto;
            padding: 2.5rem 2.5rem 6rem;
            background: var(--bg-card);
            border-right: 1px solid var(--border-color);
            min-height: calc(100vh - 61px);
        }}

        /* Academic Typography */
        .main-reader h1 {{
            font-family: var(--font-serif);
            font-size: 2.25rem;
            margin: 2.2rem 0 1rem;
            color: var(--text-main);
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 0.5rem;
            line-height: 1.25;
        }}
        .main-reader h2 {{
            font-family: var(--font-serif);
            font-size: 1.65rem;
            margin: 1.8rem 0 0.85rem;
            color: var(--text-main);
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.35rem;
        }}
        .main-reader h3 {{
            font-size: 1.25rem;
            margin: 1.4rem 0 0.6rem;
            color: var(--text-main);
        }}
        .main-reader h4 {{
            font-size: 1.05rem;
            margin: 1.1rem 0 0.4rem;
            color: var(--text-muted);
        }}
        .main-reader p {{
            font-family: var(--font-serif);
            font-size: 1.05rem;
            line-height: 1.75;
            margin-bottom: 1.25rem;
            color: var(--text-main);
        }}
        .main-reader ul, .main-reader ol {{
            margin: 0.85rem 0 1.25rem 1.75rem;
            font-family: var(--font-serif);
            font-size: 1.02rem;
        }}
        .main-reader li {{
            margin-bottom: 0.4rem;
        }}
        .main-reader hr {{
            border: 0;
            height: 1px;
            background: var(--border-color);
            margin: 2.5rem 0;
        }}
        .main-reader table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.75rem 0;
            font-size: 0.92rem;
            box-shadow: var(--shadow-sm);
            border-radius: var(--radius-md);
            overflow: hidden;
        }}
        .main-reader th, .main-reader td {{
            padding: 0.65rem 0.85rem;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }}
        .main-reader th {{
            background: var(--bg-body);
            font-weight: 700;
            color: var(--text-main);
        }}
        .main-reader tr:hover {{
            background: var(--primary-light);
        }}

        /* Callouts / Alerts */
        .callout {{
            border-left: 4px solid var(--primary);
            background: var(--bg-body);
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            padding: 1rem 1.25rem;
            margin: 1.5rem 0;
            border-top: 1px solid var(--border-color);
            border-right: 1px solid var(--border-color);
            border-bottom: 1px solid var(--border-color);
        }}
        .callout-header {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.5rem;
        }}
        .callout-body p {{
            margin-bottom: 0.35rem;
            font-size: 0.95rem;
        }}
        .callout.alert-note {{ border-left-color: #3b82f6; }}
        .callout.alert-important {{ border-left-color: #8b5cf6; }}
        .callout.alert-tip {{ border-left-color: #10b981; }}
        .callout.alert-warning {{ border-left-color: #f59e0b; }}
        .callout.alert-caution {{ border-left-color: #ef4444; }}

        /* Citations & Tooltips */
        .citation-ref {{
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
            background: var(--primary-light);
            padding: 0.15rem 0.35rem;
            border-radius: 4px;
            font-size: 0.88em;
            transition: all 0.15s;
            position: relative;
            cursor: pointer;
        }}
        .citation-ref:hover {{
            background: var(--primary);
            color: white;
            text-decoration: none;
        }}
        .citation-bracket {{
            white-space: nowrap;
        }}
        .reference-anchor {{
            position: relative;
            top: -70px;
            display: block;
            visibility: hidden;
        }}

        /* Custom Hover Tooltip */
        .citation-ref:hover::after {{
            content: attr(data-tooltip);
            position: absolute;
            bottom: 125%;
            left: 50%;
            transform: translateX(-50%);
            background: #1e293b;
            color: #f8fafc;
            padding: 0.5rem 0.75rem;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 400;
            line-height: 1.4;
            width: 320px;
            max-width: 80vw;
            white-space: normal;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3);
            z-index: 1000;
            pointer-events: none;
        }}

        /* Dashboard Styles */
        .dashboard-container {{
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1.5rem 4rem;
        }}
        .dash-hero {{
            text-align: center;
            margin-bottom: 2.5rem;
        }}
        .dash-hero h1 {{
            font-size: 2.2rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            color: var(--text-main);
        }}
        .dash-hero p {{
            font-size: 1.1rem;
            color: var(--text-muted);
            max-width: 750px;
            margin: 0 auto;
        }}
        .grid-2 {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}
        .grid-3 {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.25rem;
            margin-bottom: 2rem;
        }}
        .dash-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
            box-shadow: var(--shadow-sm);
        }}
        .dash-card h3 {{
            font-size: 1.15rem;
            font-weight: 700;
            margin-bottom: 0.85rem;
            color: var(--text-main);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .metric-badge {{
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            background: var(--primary-light);
            color: var(--primary);
        }}
        .kpi-val {{
            font-size: 1.85rem;
            font-weight: 800;
            color: var(--primary);
            line-height: 1.1;
            margin-bottom: 0.25rem;
        }}
        .kpi-label {{
            font-size: 0.85rem;
            color: var(--text-muted);
        }}

        /* Interactive Calculator */
        .calc-row {{
            margin-bottom: 1.1rem;
        }}
        .calc-row label {{
            display: flex;
            justify-content: space-between;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 0.35rem;
        }}
        .calc-slider {{
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: var(--border-color);
            outline: none;
            accent-color: var(--primary);
        }}
        .calc-result-box {{
            background: var(--bg-body);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1rem;
            margin-top: 1.2rem;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }}

        /* Anteproyecto Viewer */
        .anteproyecto-container {{
            max-width: 1100px;
            margin: 2rem auto;
            padding: 0 1.5rem 4rem;
        }}
        .search-bar {{
            width: 100%;
            padding: 0.75rem 1rem;
            font-size: 1rem;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            background: var(--bg-card);
            color: var(--text-main);
            margin-bottom: 2rem;
        }}
        .title-group {{
            margin-bottom: 2.5rem;
        }}
        .title-heading h3 {{
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 0.25rem;
        }}
        .title-desc {{
            font-size: 0.9rem;
            color: var(--text-muted);
            margin-bottom: 1rem;
        }}
        .article-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.25rem;
            margin-bottom: 1rem;
            box-shadow: var(--shadow-sm);
        }}
        .article-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.6rem;
        }}
        .article-header h4 {{
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--text-main);
        }}
        .legal-badge {{
            font-size: 0.75rem;
            font-weight: 600;
            background: var(--accent-light);
            color: var(--accent);
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
        }}
        .article-body p {{
            font-family: var(--font-serif);
            font-size: 0.95rem;
            color: var(--text-main);
            line-height: 1.6;
        }}

        /* Print Media Styles */
        @media print {{
            .top-navbar, .sidebar-toc, .nav-tabs, .header-actions {{ display: none !important; }}
            .monograph-layout {{ display: block; }}
            .main-reader {{ max-width: 100%; padding: 0; border: none; }}
            body {{ background: #fff; color: #000; font-size: 11pt; }}
            h1 {{ page-break-before: always; }}
            a {{ text-decoration: none; color: #000; }}
            .citation-ref {{ background: transparent; color: #000; font-weight: bold; }}
        }}

        @media (max-width: 900px) {{
            .sidebar-toc {{ display: none; }}
            .main-reader {{ padding: 1.5rem 1rem; }}
        }}
    </style>
</head>
<body>

    <!-- Header Navigation Bar -->
    <header class="top-navbar">
        <div class="brand-container">
            <span class="brand-badge">UBR ESPAÑA</span>
            <span class="brand-title">Renta Básica Universal</span>
        </div>
        
        <nav class="nav-tabs">
            <button class="nav-tab-btn active" onclick="switchTab('monograph')">📄 Monografía Académica</button>
            <button class="nav-tab-btn" onclick="switchTab('dashboard')">📊 Simulador de Políticas</button>
            <button class="nav-tab-btn" onclick="switchTab('anteproyecto')">⚖️ Anteproyecto de Ley</button>
        </nav>

        <div class="header-actions">
            <button class="btn-action" onclick="toggleLanguageQuick()">🇪🇸 / 🇬🇧 Resumen</button>
            <button class="btn-action" onclick="window.print()">🖨️ Imprimir / PDF</button>
            <a href="https://github.com/jbernax/renta-basica-universal-ubr" target="_blank" rel="noopener" class="btn-action">
                <svg height="16" width="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
                GitHub
            </a>
            <button class="btn-action" onclick="toggleTheme()" id="themeBtn">🌙</button>
        </div>
    </header>

    <!-- Tab 1: Monograph Reader -->
    <div id="tab-monograph" class="tab-content active">
        <div class="monograph-layout">
            <aside class="sidebar-toc">
                <div class="sidebar-title">Índice de la Monografía</div>
                <ul class="toc-list">
                    {toc_html}
                </ul>
            </aside>
            <main class="main-reader">
                {rendered_body_html}
            </main>
        </div>
    </div>

    <!-- Tab 2: Interactive Policy Dashboard -->
    <div id="tab-dashboard" class="tab-content">
        <div class="dashboard-container">
            <div class="dash-hero">
                <h1>Simulador de Políticas: Renta Básica Universal</h1>
                <p>Explore los resultados cuantitativos de los 5 motores empíricos: escenarios de disrupción por IA, redistribución de renta por deciles, equilibrio territorial del CPFF y viabilidad parlamentaria.</p>
            </div>

            <!-- Escenarios de Desplazamiento por IA -->
            <div class="dash-card" style="margin-bottom: 2rem;">
                <h3>
                    <span>Escenarios de Disrupción Laboral por Inteligencia Artificial</span>
                    <span class="metric-badge">Track 1: CNO-11 & Macro Drag</span>
                </h3>
                <div class="grid-3" style="margin-top: 1rem;">
                    <div class="dash-card" style="border-left: 4px solid #3b82f6;">
                        <span class="metric-badge">Escenario S1 · Moderado</span>
                        <div class="kpi-val">-2.5 pp</div>
                        <div class="kpi-label">Contracción de la cuota del trabajo (Δs_L)</div>
                        <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.5rem;">
                            Erosión de cotizaciones: <strong>-€7.2B/año</strong>. Horas humanas desplazadas: <strong>-7.5%</strong>. Nivel RBU recomendado: <strong>Tier A (€600/mes)</strong>.
                        </p>
                    </div>
                    <div class="dash-card" style="border-left: 4px solid #059669; background: var(--accent-light);">
                        <span class="metric-badge">Escenario S2 · Severo (Central)</span>
                        <div class="kpi-val">-7.0 pp</div>
                        <div class="kpi-label">Contracción de la cuota del trabajo (Δs_L)</div>
                        <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.5rem;">
                            Erosión de cotizaciones: <strong>-€18.4B/año</strong>. Horas humanas desplazadas: <strong>-20.0%</strong>. Nivel RBU recomendado: <strong>Tier B (€900/mes)</strong>.
                        </p>
                    </div>
                    <div class="dash-card" style="border-left: 4px solid #ef4444;">
                        <span class="metric-badge">Escenario S3 · Estructural</span>
                        <div class="kpi-val">-15.0 pp</div>
                        <div class="kpi-label">Contracción de la cuota del trabajo (Δs_L)</div>
                        <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.5rem;">
                            Erosión de cotizaciones: <strong>-€38.9B/año</strong>. Horas humanas desplazadas: <strong>-42.0%</strong>. Nivel RBU recomendado: <strong>Tier C (€1.200/mes)</strong>.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Calculadora Familiar y Distribución por Deciles -->
            <div class="grid-2">
                <!-- Calculadora de Prestación Familiar -->
                <div class="dash-card">
                    <h3>
                        <span>Calculadora Familiar de RBU</span>
                        <span class="metric-badge">Micro-Simulador</span>
                    </h3>
                    
                    <div class="calc-row">
                        <label>
                            <span>Adultos en el hogar (≥18 años):</span>
                            <span id="adultCountDisplay">2 adultos</span>
                        </label>
                        <input type="range" class="calc-slider" id="sliderAdults" min="1" max="4" value="2" oninput="updateCalculator()">
                    </div>

                    <div class="calc-row">
                        <label>
                            <span>Menores de edad (&lt;18 años, factor 0.40):</span>
                            <span id="childCountDisplay">1 menor</span>
                        </label>
                        <input type="range" class="calc-slider" id="sliderChildren" min="0" max="4" value="1" oninput="updateCalculator()">
                    </div>

                    <div class="calc-row">
                        <label>
                            <span>Ingresos laborales brutos mensuales:</span>
                            <span id="incomeDisplay">€1.800 / mes</span>
                        </label>
                        <input type="range" class="calc-slider" id="sliderIncome" min="0" max="6000" step="100" value="1800" oninput="updateCalculator()">
                    </div>

                    <div class="calc-result-box">
                        <div>
                            <div class="kpi-label">RBU Bruta Familiar (Nivel B)</div>
                            <div class="kpi-val" id="grossUbrVal">€2.160</div>
                            <span style="font-size: 0.75rem; color: var(--text-muted);">€900/ad + €360/men</span>
                        </div>
                        <div>
                            <div class="kpi-label">Ganancia Neta Disponible</div>
                            <div class="kpi-val" style="color: var(--accent);" id="netGainVal">+€1.240</div>
                            <span style="font-size: 0.75rem; color: var(--text-muted);">Tras retención IRPF armonizada</span>
                        </div>
                    </div>
                </div>

                <!-- Gráfico de Impacto Distributivo por Deciles -->
                <div class="dash-card">
                    <h3>
                        <span>Variación de Renta Disponible por Decil</span>
                        <span class="metric-badge">EUROMOD · Nivel B</span>
                    </h3>
                    <div style="height: 260px; position: relative;">
                        <canvas id="decilesChart"></canvas>
                    </div>
                    <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem; text-align: center;">
                        El punto de equilibrio se sitúa en el <strong>percentil 84</strong>: el 84% de los ciudadanos resulta beneficiario neto.
                    </p>
                </div>
            </div>

            <!-- Fondo de Compensación CPFF y Aritmética Parlamentaria -->
            <div class="grid-2">
                <!-- Fondo de Compensación UBR (CPFF) -->
                <div class="dash-card">
                    <h3>
                        <span>Fondo de Compensación CPFF (CCAA)</span>
                        <span class="metric-badge">€56.84B · Régimen Común</span>
                    </h3>
                    <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.8rem;">
                        Distribución per cápita garantizada de <strong>€1.134,80 por habitante</strong> en las 15 Comunidades Autónomas de Régimen Común:
                    </p>
                    <div style="max-height: 240px; overflow-y: auto; border: 1px solid var(--border-color); border-radius: var(--radius-md);">
                        <table style="width: 100%; font-size: 0.82rem; border-collapse: collapse;">
                            <thead style="background: var(--bg-body); position: sticky; top: 0;">
                                <tr>
                                    <th style="padding: 0.4rem 0.6rem; text-align: left;">Comunidad Autónoma</th>
                                    <th style="padding: 0.4rem 0.6rem; text-align: right;">Población</th>
                                    <th style="padding: 0.4rem 0.6rem; text-align: right;">Fondo UBR (€M)</th>
                                </tr>
                            </thead>
                            <tbody id="cpffTableBody">
                                <!-- Populated dynamically -->
                            </tbody>
                        </table>
                    </div>
                    <p style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.5rem;">
                        * País Vasco (6,24%) y Navarra (1,60%) computan la RBU como <em>carga no asumida</em> en Cupo y Aportación.
                    </p>
                </div>

                <!-- Viabilidad Bicameral y Veto LOEPSF -->
                <div class="dash-card">
                    <h3>
                        <span>Aritmética Bicameral y Reforma LOEPSF</span>
                        <span class="metric-badge">Congreso: 179 Votos</span>
                    </h3>
                    <div style="margin: 1rem 0;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.35rem; font-size: 0.85rem;">
                            <span>Mayoría Absoluta en Congreso (Art. 15.6 LOEPSF):</span>
                            <strong>179 / 350 escaños (51.1%)</strong>
                        </div>
                        <div style="height: 12px; border-radius: 6px; background: var(--border-color); overflow: hidden; display: flex;">
                            <div style="width: 51.1%; background: var(--accent);"></div>
                            <div style="width: 48.9%; background: var(--text-muted);"></div>
                        </div>
                    </div>
                    <p style="font-size: 0.85rem; color: var(--text-main); margin-bottom: 0.8rem;">
                        La reforma orgánica suprime el veto absoluto del Senado establecido en la LOEPSF, restaurando la doctrina del Tribunal Constitucional (STC 179/1989 y Art. 90.2 CE).
                    </p>
                    <div style="background: var(--bg-body); border-radius: var(--radius-md); padding: 0.75rem; font-size: 0.82rem;">
                        <strong>Efecto Framing CARIN ("Dividendo de Productividad IA"):</strong><br>
                        El apoyo ciudadano asciende del <strong>44.2% al 62.8% (+18.6 pp)</strong> al vincular la transferencia con el dividendo del capital algorítmico y no como subsidio asistencial.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Tab 3: Anteproyecto de Ley Viewer -->
    <div id="tab-anteproyecto" class="tab-content">
        <div class="anteproyecto-container">
            <div class="dash-hero">
                <h1>Anteproyecto de Ley de Renta Básica Universal</h1>
                <p>Texto legal completo estructurado en 9 Títulos y 25 artículos. Incorpora el Fondo de Compensación CPFF, el anclaje constitucional (Arts. 149.1.1, 149.1.14 y 149.1.17 CE), el Impuesto IECA y el Parámetro Fiscal Federal de Vivienda.</p>
            </div>

            <input type="text" id="legalSearch" class="search-bar" placeholder="🔍 Buscar por artículo, concepto o anclaje constitucional (ej: 'vivienda', '149.1.14', 'computación', 'IRPF')..." oninput="filterArticles()">

            <div id="anteproyectoList">
                {anteproyecto_html}
            </div>
        </div>
    </div>

    <!-- Client-side Logic -->
    <script>
        const DASHBOARD_DATA = {dashboard_json};

        function switchTab(tabId) {{
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-tab-btn').forEach(el => el.classList.remove('active'));
            
            document.getElementById('tab-' + tabId).classList.add('active');
            event.target.classList.add('active');
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function toggleTheme() {{
            const current = document.documentElement.getAttribute('data-theme');
            const target = current === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', target);
            document.getElementById('themeBtn').innerText = target === 'dark' ? '☀️' : '🌙';
        }}

        function toggleLanguageQuick() {{
            const esHeading = document.getElementById('2-resumen-ejecutivo-para-decisores-publicos-espanol');
            const enHeading = document.getElementById('1-executive-summary-english');
            
            if (window.scrollY < 2000 && esHeading) {{
                esHeading.scrollIntoView({{ behavior: 'smooth' }});
            }} else if (enHeading) {{
                enHeading.scrollIntoView({{ behavior: 'smooth' }});
            }}
        }}

        function updateCalculator() {{
            const adults = parseInt(document.getElementById('sliderAdults').value);
            const children = parseInt(document.getElementById('sliderChildren').value);
            const income = parseInt(document.getElementById('sliderIncome').value);

            document.getElementById('adultCountDisplay').innerText = adults + (adults === 1 ? ' adulto' : ' adultos');
            document.getElementById('childCountDisplay').innerText = children + (children === 1 ? ' menor' : ' menores');
            document.getElementById('incomeDisplay').innerText = '€' + income.toLocaleString('es-ES') + ' / mes';

            // Tier B rates: €900 adult, €360 minor (0.40)
            const grossUbr = (adults * 900) + (children * 360);
            
            // Simplified effective tax clawback on income (Tier B integration with 44% flat reform rate - current basic allowances)
            const clawback = Math.max(0, income * 0.40);
            const netGain = Math.round(grossUbr - clawback + (income * 0.15)); // net disposable difference

            document.getElementById('grossUbrVal').innerText = '€' + grossUbr.toLocaleString('es-ES');
            document.getElementById('netGainVal').innerText = (netGain >= 0 ? '+€' : '-€') + Math.abs(netGain).toLocaleString('es-ES');
        }}

        function filterArticles() {{
            const query = document.getElementById('legalSearch').value.toLowerCase();
            const cards = document.querySelectorAll('.article-card');
            cards.forEach(card => {{
                const text = card.getAttribute('data-search-text');
                if (!query || text.includes(query)) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        // Initialize Decile Chart and CPFF table on page load
        window.addEventListener('DOMContentLoaded', () => {{
            // CPFF table population
            const cpffTbody = document.getElementById('cpffTableBody');
            if (cpffTbody && DASHBOARD_DATA.cpff && DASHBOARD_DATA.cpff.ccaa_allocations) {{
                let rows = '';
                DASHBOARD_DATA.cpff.ccaa_allocations.forEach(item => {{
                    rows += `<tr>
                        <td style="padding: 0.35rem 0.6rem; border-bottom: 1px solid var(--border-color);">${{item.ccaa_name}}</td>
                        <td style="padding: 0.35rem 0.6rem; border-bottom: 1px solid var(--border-color); text-align: right;">${{item.population.toLocaleString('es-ES')}}</td>
                        <td style="padding: 0.35rem 0.6rem; border-bottom: 1px solid var(--border-color); text-align: right; font-weight: 600; color: var(--primary);">€${{item.allocation_eur_m.toLocaleString('es-ES', {{maximumFractionDigits: 1}})}}</td>
                    </tr>`;
                }});
                cpffTbody.innerHTML = rows;
            }}

            // Chart.js Deciles
            const ctx = document.getElementById('decilesChart');
            if (ctx && DASHBOARD_DATA.microsim_deciles) {{
                const decileLabels = DASHBOARD_DATA.microsim_deciles.map(d => 'Decil ' + d.decile);
                const pctGains = DASHBOARD_DATA.microsim_deciles.map(d => d.pct_change_disp_income);

                new Chart(ctx, {{
                    type: 'bar',
                    data: {{
                        labels: decileLabels,
                        datasets: [{{
                            label: 'Ganancia en Renta Disponible (%)',
                            data: pctGains,
                            backgroundColor: pctGains.map(val => val >= 0 ? '#10b981' : '#ef4444'),
                            borderRadius: 4,
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {{
                            legend: {{ display: false }},
                            tooltip: {{
                                callbacks: {{
                                    label: function(context) {{
                                        return (context.raw >= 0 ? '+' : '') + context.raw + '% renta disponible';
                                    }}
                                }}
                            }}
                        }},
                        scales: {{
                            y: {{
                                title: {{ display: true, text: '% Variación' }},
                                grid: {{ color: 'rgba(0,0,0,0.06)' }}
                            }},
                            x: {{
                                grid: {{ display: false }}
                            }}
                        }}
                    }}
                }});
            }}
        }});
    </script>
</body>
</html>
"""
    return full_html


def main() -> None:
    print("[1/3] Compiling standalone HTML monograph and interactive dashboard...")
    html_content = build_full_html()
    
    docs_dir = REPO_ROOT / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    docs_index = docs_dir / "index.html"
    with open(docs_index, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  ✓ Written {len(html_content):,} bytes to {docs_index}")
    
    paper_dir = REPO_ROOT / "paper"
    paper_index = paper_dir / "index.html"
    with open(paper_index, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  ✓ Written {len(html_content):,} bytes to {paper_index}")
    print("[2/3] Validating HTML outputs...")
    assert docs_index.exists() and docs_index.stat().st_size > 50000
    assert paper_index.exists() and paper_index.stat().st_size > 50000
    print("[3/3] Done! HTML monograph is ready for local reading and GitHub Pages.")


if __name__ == "__main__":
    main()
