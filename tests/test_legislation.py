"""Comprehensive Unit and Integration Tests for Track 5: Model Legislation & Governance.

Tests statutory Anteproyecto codification, constitutional & EU law competence matrices,
CPFF intergovernmental fiscal equalization, bicameral veto-player modeling, and CLI subcommands.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from ubr.cli import main
from ubr.legislation.anteproyecto import (
    AnteproyectoCorpus,
    build_anteproyecto_corpus,
)
from ubr.legislation.bicameral_engine import (
    get_spanish_parliamentary_parties,
    simulate_bicameral_pathway,
)
from ubr.legislation.competence_matrix import (
    build_competence_anchors,
    evaluate_competence_architecture,
)
from ubr.legislation.equalization import (
    calculate_intergovernmental_equalization,
)
from ubr.legislation.export import (
    export_all_legislation_artifacts,
    format_anteproyecto_summary,
    format_bicameral_summary,
    format_competence_matrix_summary,
    format_equalization_summary,
    format_legislation_executive_summary,
)


class TestAnteproyectoCorpus:
    """Tests the statutory corpus structure and official legal drafting."""

    def test_corpus_structure_and_titles(self):
        corpus = build_anteproyecto_corpus()
        assert "Renta Básica Universal" in corpus.official_title
        assert len(corpus.titles) == 9
        assert len(corpus.additional_provisions) == 2
        assert len(corpus.transitory_provisions) == 2
        assert len(corpus.final_provisions) == 3

        # Verify all 9 titles are properly numbered
        expected_titles = [f"Título {roman}" for roman in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]]
        for t, exp in zip(corpus.titles, expected_titles):
            assert t.title_number == exp
            assert len(t.articles) >= 2

    def test_specific_articles_and_mechanisms(self):
        corpus = build_anteproyecto_corpus()
        articles_by_id = {}
        for t in corpus.titles:
            for art in t.articles:
                articles_by_id[art.id] = art

        # Art. 5: Deducción Reembolsable en LIRPF
        art_05 = articles_by_id["ART_05"]
        assert "Deducción Reembolsable Universal" in art_05.heading
        assert "61 bis" in art_05.text
        assert "Art. 149.1.14 CE" in art_05.constitutional_bases

        # Art. 7: Parámetro Fiscal Federal Objetivo en Alquileres (D-008)
        art_07 = articles_by_id["ART_07"]
        assert "23" in art_07.text
        assert "0 por ciento" in art_07.text
        assert "STC 79/2024" in " ".join(art_07.constitutional_bases)

        # Art. 8 & 9: IECA y condicionalidad de gasto en LIS Art. 15 (D-007)
        art_08 = articles_by_id["ART_08"]
        assert "IECA" in art_08.heading
        assert "5 por ciento" in art_08.text

        art_09 = articles_by_id["ART_09"]
        assert "artículo 15" in art_09.text
        assert "Ley 27/2014" in art_09.text

        # Art. 10: Paridad Schumacker
        art_10 = articles_by_id["ART_10"]
        assert "Schumacker" in art_10.heading
        assert "75 por ciento" in art_10.text

        # Art. 11 & 12: Pension continuity & Crédito Cotizatorio (D-009)
        art_11 = articles_by_id["ART_11"]
        assert "273" in art_11.text
        assert "SEPE" in art_11.text

        art_12 = articles_by_id["ART_12"]
        assert "273 bis" in art_12.text
        assert "100 por ciento de la base mínima" in art_12.text

        # Art. 13: Inembargabilidad LEC 607 y excepción alimentos 608
        art_13 = articles_by_id["ART_13"]
        assert "607" in art_13.text
        assert "608" in art_13.text

        # Art. 15: Código de Retención Sintético y GDPR Art. 9
        art_15 = articles_by_id["ART_15"]
        assert "Código de Retención Sintético" in art_15.text
        assert "Reglamento (UE) 2016/679" in art_15.text

        # Art. 18 & 19: CPFF Fondo y Concierto/Convenio Foral
        art_18 = articles_by_id["ART_18"]
        assert "Fondo de Compensación" in art_18.heading
        assert "Consejo de Política Fiscal y Financiera" in art_18.text

        art_19 = articles_by_id["ART_19"]
        assert "carga no asumida" in art_19.text
        assert "6,24%" in art_19.text
        assert "1,60%" in art_19.text

        # Art. 21: Regla Windfall EBE > 120% y 3/5 del Congreso
        art_21 = articles_by_id["ART_21"]
        assert "120 por ciento" in art_21.text
        assert "tres quintos" in art_21.text
        assert "Reglamento (UE) 2024/1263" in art_21.text

        # Art. 22: Legalidad Tributaria y veto a Decretos-Leyes (STC 73/2017)
        art_22 = articles_by_id["ART_22"]
        assert "urgencia parlamentaria" in art_22.text
        assert "STC 73/2017" in " ".join(art_22.constitutional_bases)

        # Art. 24: No suplantación salarial
        art_24 = articles_by_id["ART_24"]
        assert "prohibida su absorción" in art_24.text
        assert "82.3 del Estatuto de los Trabajadores" in art_24.text

    def test_additional_provisions_loepsf_and_infancy(self):
        corpus = build_anteproyecto_corpus()
        da1 = corpus.additional_provisions[0]
        assert "15.6" in da1["heading"]
        assert "LOEPSF" in da1["heading"]
        assert "STC 179/1989" in " ".join(da1["constitutional_bases"])

        da2 = corpus.additional_provisions[1]
        assert "Infancia" in da2["heading"]
        assert "Art. 39 CE" in " ".join(da2["constitutional_bases"])


class TestCompetenceMatrix:
    """Tests Constitutional and EU Law evaluation."""

    def test_anchors_and_scores(self):
        result = evaluate_competence_architecture()
        assert result.total_anchors >= 14
        assert result.fully_compliant_count >= 12
        assert result.firewall_compliant_count >= 2
        assert result.constitutional_coverage_score >= 99.0
        assert result.eu_compliance_score >= 98.0

    def test_specific_constitutional_anchors(self):
        anchors = {a.id: a for a in build_competence_anchors()}
        assert "COMP_149_1_1" in anchors
        assert "COMP_149_1_14" in anchors
        assert "COMP_149_1_17" in anchors
        assert "COMP_128_2" in anchors
        assert "PREC_STC_158_2021" in anchors
        assert "PREC_STC_19_2024" in anchors
        assert "PREC_STC_79_2024" in anchors
        assert "PREC_STC_182_2021" in anchors
        assert "PREC_STC_73_2017" in anchors
        assert "PREC_STC_179_1989" in anchors
        assert "EU_DIR_2004_38" in anchors
        assert "EU_REG_883_2004" in anchors
        assert "CJEU_SCHUMACKER" in anchors
        assert "CJEU_CREMONA" in anchors


class TestIntergovernmentalEqualization:
    """Tests CPFF equalization across Common Regime and Foral territories."""

    def test_scenarios_s1_s2_s3(self):
        for scen in ["S1", "S2", "S3"]:
            rep = calculate_intergovernmental_equalization(scenario=scen)
            assert rep.scenario == scen
            assert len(rep.common_regime_regions) == 15
            assert len(rep.foral_records) == 2
            assert rep.total_cpff_fund_size_eur_b > 0.0

            # Check that Basque Cupo adjustment is negative (deduction)
            pva = rep.foral_records[0]
            assert pva.territory == "País Vasco"
            assert pva.statutory_index_pct == 6.24
            assert pva.non_assumed_burden_deduction_eur_b > 0.0
            assert pva.net_adjusted_cupo_eur_b < pva.gross_cupo_baseline_eur_b

            # Check Navarre Aportación
            nav = rep.foral_records[1]
            assert nav.territory == "Comunidad Foral de Navarra"
            assert nav.statutory_index_pct == 1.60
            assert nav.non_assumed_burden_deduction_eur_b > 0.0
            assert nav.net_adjusted_cupo_eur_b < nav.gross_cupo_baseline_eur_b

    def test_common_regime_per_capita_equalization(self):
        rep = calculate_intergovernmental_equalization(scenario="S2")
        # Every common regime region achieves identical equalized baseline allocation per capita
        per_capita_values = [r.equalized_balance_per_capita_eur for r in rep.common_regime_regions]
        assert max(per_capita_values) - min(per_capita_values) < 0.1


class TestBicameralEngine:
    """Tests parliamentary seats, LOEPSF reform, and CARIN framing."""

    def test_parliamentary_seat_totals(self):
        parties = get_spanish_parliamentary_parties()
        cong_seats = sum(p.congress_seats for p in parties)
        assert cong_seats == 350

        sen_seats = sum(p.senate_seats for p in parties)
        assert sen_seats == 266

    def test_loepsf_reform_pathway(self):
        rep = simulate_bicameral_pathway()
        # Vote 1: Congress passes Organic Law with absolute majority
        assert rep.loepsf_congress_vote.passed is True
        assert rep.loepsf_congress_vote.yes_votes >= 176

        # Vote 2: Senate vetoes
        assert rep.loepsf_senate_vote.passed is False
        assert rep.loepsf_senate_vote.no_votes >= 134

        # Vote 3: Congress overrides Senate veto by absolute majority (Art. 90.2 CE)
        assert rep.loepsf_congress_override.passed is True
        assert rep.loepsf_congress_override.yes_votes >= 176

        # Vote 4: UBR statute passes in Congress
        assert rep.ubr_statute_congress_vote.passed is True
        assert rep.ubr_statute_congress_vote.yes_votes >= 176

    def test_carin_framing_shift(self):
        rep = simulate_bicameral_pathway()
        assert rep.ai_productivity_approval_pct > rep.traditional_welfare_approval_pct
        assert rep.framing_delta_pp >= 15.0
        assert rep.tsebelis_winset_volume > 0.40


class TestCliLegalSubcommands:
    """Tests CLI integration and JSON serialization."""

    def test_cli_legal_anteproyecto(self, capsys):
        rc = main(["legal", "anteproyecto", "--title", "Título I"])
        assert rc == 0
        out = capsys.readouterr().out
        assert "ESTATUTO MODELO" in out
        assert "Título I" in out

    def test_cli_legal_competence(self, capsys):
        rc = main(["legal", "competence", "--detail"])
        assert rc == 0
        out = capsys.readouterr().out
        assert "MATRIZ DE COMPATIBILIDAD CONSTITUCIONAL" in out
        assert "STC 158/2021" in out

    def test_cli_legal_equalization(self, capsys):
        rc = main(["legal", "equalization", "--scenario", "S2"])
        assert rc == 0
        out = capsys.readouterr().out
        assert "BALANZA DE EQUALIZACIÓN" in out
        assert "Andalucía" in out
        assert "País Vasco" in out

    def test_cli_legal_bicameral(self, capsys):
        rc = main(["legal", "bicameral"])
        assert rc == 0
        out = capsys.readouterr().out
        assert "SIMULADOR BICAMERAL" in out
        assert "APROBADO" in out

    def test_cli_legal_summary(self, capsys):
        rc = main(["legal", "summary"])
        assert rc == 0
        out = capsys.readouterr().out
        assert "TRACK 5 EXECUTIVE DASHBOARD" in out
        assert "ESTATUTO MODELO" in out

    def test_json_export_integrity(self, tmp_path):
        paths = export_all_legislation_artifacts(tmp_path)
        for key, p in paths.items():
            assert p.exists()
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
                assert isinstance(data, dict)
                assert len(data) > 0
