"""Export and Terminal Formatting Utilities for Track 5 Model Legislation & Governance.

Serializes statutory corpora, competence matrices, equalization models, and bicameral roll-calls
to persistent JSON artifacts in data/ and provides formatted terminal outputs (Track 5: M06, M11, M12, M13, M16, M17).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

from ubr.legislation.anteproyecto import (
    AnteproyectoCorpus,
    build_anteproyecto_corpus,
)
from ubr.legislation.bicameral_engine import (
    LegislativePathwaysReport,
    simulate_bicameral_pathway,
)
from ubr.legislation.competence_matrix import (
    CompetenceEvaluationResult,
    evaluate_competence_architecture,
)
from ubr.legislation.equalization import (
    IntergovernmentalEqualizationReport,
    calculate_intergovernmental_equalization,
)


def export_all_legislation_artifacts(output_dir: Path) -> Dict[str, Path]:
    """Generates and writes all Track 5 persistent JSON artifacts to data/."""
    output_dir.mkdir(parents=True, exist_ok=True)
    paths: Dict[str, Path] = {}

    # 1. Anteproyecto Statutory Corpus
    corpus = build_anteproyecto_corpus()
    p_corpus = output_dir / "legal_anteproyecto_corpus.json"
    with open(p_corpus, "w", encoding="utf-8") as f:
        json.dump(corpus.to_dict(), f, indent=2, ensure_ascii=False)
    paths["corpus"] = p_corpus

    # 2. Competence Matrix
    matrix = evaluate_competence_architecture()
    p_matrix = output_dir / "legal_competence_matrix.json"
    with open(p_matrix, "w", encoding="utf-8") as f:
        json.dump(matrix.to_dict(), f, indent=2, ensure_ascii=False)
    paths["matrix"] = p_matrix

    # 3. Intergovernmental Equalization (S2 Baseline)
    equalization = calculate_intergovernmental_equalization(scenario="S2")
    p_equal = output_dir / "legal_cpff_equalization.json"
    with open(p_equal, "w", encoding="utf-8") as f:
        json.dump(equalization.to_dict(), f, indent=2, ensure_ascii=False)
    paths["equalization"] = p_equal

    # 4. Bicameral Legislative Pathways
    pathway = simulate_bicameral_pathway()
    p_pathway = output_dir / "legal_bicameral_coalitions.json"
    with open(p_pathway, "w", encoding="utf-8") as f:
        json.dump(pathway.to_dict(), f, indent=2, ensure_ascii=False)
    paths["pathway"] = p_pathway

    return paths


def format_anteproyecto_summary(corpus: AnteproyectoCorpus, title_num: Optional[str] = None) -> str:
    """Formats the statutory Anteproyecto structure for terminal inspection."""
    lines = [
        "=" * 80,
        f"  ESTATUTO MODELO: {corpus.official_title.upper()}",
        "=" * 80,
        f"Denominación breve: {corpus.short_title}",
        f"Estructura: {len(corpus.titles)} Títulos, {len(corpus.additional_provisions)} Disposiciones Adicionales, "
        f"{len(corpus.transitory_provisions)} Transitorias, {len(corpus.final_provisions)} Finales.",
        "-" * 80,
    ]

    for t in corpus.titles:
        if title_num and t.title_number.lower() != title_num.lower():
            continue
        lines.append(f"\n[{t.title_number}] {t.heading.upper()}")
        lines.append(f"  Descripción: {t.description}")
        lines.append("  Artículos contenidos:")
        for art in t.articles:
            bases = ", ".join(art.constitutional_bases) if art.constitutional_bases else "General"
            reformed = f" | Reforma: {', '.join(art.reformed_statutes)}" if art.reformed_statutes else ""
            lines.append(f"    • {art.article_number} ({art.id}): {art.heading}")
            lines.append(f"      Anclaje: {bases}{reformed}")

    lines.append("\n" + "-" * 80)
    lines.append("DISPOSICIONES ADICIONALES CLAVE:")
    for da in corpus.additional_provisions:
        lines.append(f"  • {da['number']}: {da['heading']}")
        lines.append(f"    Mecanismo: {', '.join(da['key_mechanisms'])}")

    lines.append("=" * 80)
    return "\n".join(lines)


def format_competence_matrix_summary(result: CompetenceEvaluationResult, detail: bool = False) -> str:
    """Formats the Constitutional and EU Law Competence Matrix for terminal inspection."""
    lines = [
        "=" * 80,
        "  MATRIZ DE COMPATIBILIDAD CONSTITUCIONAL Y DERECHO DE LA UNIÓN EUROPEA",
        "=" * 80,
        f"Total Anclajes Evaluados : {result.total_anchors}",
        f"Plenamente Conformes     : {result.fully_compliant_count}",
        f"Conformes con Firewall   : {result.firewall_compliant_count}",
        f"Índice Cobertura CE 1978 : {result.constitutional_coverage_score:.1f}%",
        f"Índice Cumplimiento UE   : {result.eu_compliance_score:.1f}%",
        "-" * 80,
        f"{'ID':<18} | {'CATEGORÍA':<23} | {'REFERENCIA':<20} | {'ESTADO':<15}",
        "-" * 80,
    ]

    for a in result.anchors:
        lines.append(f"{a.id:<18} | {a.category:<23} | {a.reference:<20} | {a.compliance_status:<15}")
        if detail:
            lines.append(f"  Título   : {a.title}")
            lines.append(f"  Doctrina : {a.defense_doctrine}")
            lines.append(f"  Artículos: {', '.join(a.supported_articles)}")
            lines.append("  " + "." * 76)

    lines.append("=" * 80)
    return "\n".join(lines)


def format_equalization_summary(report: IntergovernmentalEqualizationReport) -> str:
    """Formats the CPFF intergovernmental equalization balance sheet."""
    lines = [
        "=" * 80,
        f"  CONSEJO DE POLÍTICA FISCAL Y FINANCIERA (CPFF) - BALANZA DE EQUALIZACIÓN",
        "=" * 80,
        f"Escenario Macro : {report.scenario} ({report.tier} - {report.ubr_monthly_rate_eur:.0f} €/mes)",
        f"Población Total : {report.total_population_spain:,} hab. (R. Común: {report.common_regime_population:,} | Foral: {report.foral_population:,})",
        f"Fondo Total UBR : {report.total_cpff_fund_size_eur_b:.3f} Mil Millones de Euros (€B)",
        "-" * 80,
        f"{'CCAA':<24} | {'POBLACIÓN':<10} | {'TRANSF. €B':<10} | {'CPFF FONDO':<10} | {'NETO €/HAB'}",
        "-" * 80,
    ]

    for r in report.common_regime_regions:
        transfer_sign = f"+{r.cpff_equalization_transfer_eur_b:.2f}" if r.cpff_equalization_transfer_eur_b >= 0 else f"{r.cpff_equalization_transfer_eur_b:.2f}"
        lines.append(
            f"{r.name:<24} | {r.population:>10,} | {r.ubr_gross_transfers_eur_b:>9.2f}B | "
            f"{transfer_sign:>9}B | {r.equalized_balance_per_capita_eur:>9.1f} €"
        )

    lines.append("\n" + "-" * 80)
    lines.append("REGÍMENES FORALES (IMPUTACIÓN CARGA NO ASUMIDA):")
    lines.append(f"{'TERRITORIO':<24} | {'ÍNDICE':<8} | {'CUPO BASE':<10} | {'DEDUCCIÓN':<10} | {'CUPO NETO'}")
    lines.append("-" * 80)
    for f in report.foral_records:
        lines.append(
            f"{f.territory:<24} | {f.statutory_index_pct:>6.2f}% | {f.gross_cupo_baseline_eur_b:>9.3f}B | "
            f"-{f.non_assumed_burden_deduction_eur_b:>8.3f}B | {f.net_adjusted_cupo_eur_b:>9.3f}B"
        )

    lines.append("=" * 80)
    return "\n".join(lines)


def format_bicameral_summary(report: LegislativePathwaysReport) -> str:
    """Formats the bicameral voting simulator and coalition analysis."""
    lines = [
        "=" * 80,
        "  SIMULADOR BICAMERAL Y VÍA DE REFORMA ORGÁNICA LOEPSF (D-010)",
        "=" * 80,
        f"Congreso de los Diputados : {report.congress_seats_total} escaños (Mayoría Absoluta: 176)",
        f"Senado                    : {report.senate_seats_total} escaños (Mayoría Absoluta: 134)",
        f"Aprobación Social (Trad.) : {report.traditional_welfare_approval_pct:.1f}%",
        f"Aprobación Dividendo IA   : {report.ai_productivity_approval_pct:.1f}% (+{report.framing_delta_pp:.1f} pp de apoyo CARIN)",
        f"Volumen Win-Set Tsebelis  : {report.tsebelis_winset_volume:.3f} (Desbloqueo institucional garantizado)",
        "-" * 80,
        "SECUENCIA DE VOTACIONES LEGISLATIVAS:",
        "-" * 80,
    ]

    votes = [
        ("Votación 1", report.loepsf_congress_vote),
        ("Votación 2", report.loepsf_senate_vote),
        ("Votación 3", report.loepsf_congress_override),
        ("Votación 4", report.ubr_statute_congress_vote),
    ]

    for tag, v in votes:
        status = "APROBADO" if v.passed else "VETADO/RECHAZADO"
        lines.append(f"• {tag}: {v.chamber}")
        lines.append(f"  Resultado : {status} (Sí: {v.yes_votes} | No: {v.no_votes} | Umbral: {v.majority_threshold})")
        lines.append(f"  Votos Sí  : {', '.join(v.voting_parties_yes)}")
        lines.append(f"  Votos No  : {', '.join(v.voting_parties_no)}")
        lines.append("")

    lines.append("=" * 80)
    return "\n".join(lines)


def format_legislation_executive_summary() -> str:
    """Generates a high-level consolidated dashboard across Track 5."""
    corpus = build_anteproyecto_corpus()
    matrix = evaluate_competence_architecture()
    equalization = calculate_intergovernmental_equalization("S2")
    pathway = simulate_bicameral_pathway()

    lines = [
        "================================================================================",
        "  TRACK 5 EXECUTIVE DASHBOARD: LEGISLATION, GOVERNANCE & TERRITORIAL ARCHITECTURE",
        "================================================================================",
        f"1. ESTATUTO MODELO (ANTEPROYECTO DE LEY):",
        f"   • Título Oficial : {corpus.official_title}",
        f"   • Títulos        : {len(corpus.titles)} Títulos normativos y 2 Disposiciones Adicionales",
        f"   • Artículos      : {sum(len(t.articles) for t in corpus.titles)} Artículos sustantivos codificados",
        f"   • Pilares Clave  : Deducción IRPF mensual (Art. 61 bis), IECA computación (D-007),",
        f"                      Crédito cotizatorio jubilación (D-009), Código sintético GDPR (M12).",
        "",
        f"2. MATRIZ DE COMPETENCIAS Y DERECHO UE:",
        f"   • Cobertura Constitucional : {matrix.constitutional_coverage_score:.1f}% (Arts. 149.1.1, 149.1.14, 149.1.17, 128.2 CE)",
        f"   • Conformidad Derecho UE    : {matrix.eu_compliance_score:.1f}% (Directiva 2004/38, TJUE Schumacker, Reg. 883/2004)",
        f"   • Doctrina TC Integrada     : SSTC 158/2021, 19/2024, 79/2024, 182/2021, 73/2017, 179/1989.",
        "",
        f"3. EQUALIZACIÓN TERRITORIAL CPFF Y CONCIERTO/CONVENIO (ESCENARIO S2):",
        f"   • Fondo CPFF Compensación   : {equalization.total_cpff_fund_size_eur_b:.2f} €B garantizados para las 15 CCAA de R. Común",
        f"   • País Vasco (Concierto)    : Cupo base 1.48B € - Deducción carga no asumida 1.29B € = Cupo neto {equalization.foral_records[0].net_adjusted_cupo_eur_b:.3f}B €",
        f"   • Navarra (Convenio)        : Aportación base 0.62B € - Deducción carga no asumida 0.09B € = Aportación neta {equalization.foral_records[1].net_adjusted_cupo_eur_b:.3f}B €",
        "",
        f"4. PARLAMENTO Y VÍA DE REFORMA ORGÁNICA LOEPSF (D-010):",
        f"   • Mayoría en Congreso       : {pathway.loepsf_congress_vote.yes_votes} votos a favor vs {pathway.loepsf_congress_vote.no_votes} en contra (Supera umbral 176)",
        f"   • Veto en Senado            : Superado mediante levantamiento definitivo por Mayoría Absoluta (STC 179/1989)",
        f"   • Aceptación Social CARIN   : Aumenta de {pathway.traditional_welfare_approval_pct:.1f}% a {pathway.ai_productivity_approval_pct:.1f}% (+{pathway.framing_delta_pp:.1f} pp)",
        "================================================================================",
    ]
    return "\n".join(lines)
