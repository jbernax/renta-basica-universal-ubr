"""Track 5: Model Legislation (Anteproyecto de Ley), Governance, and Territorial Architecture.

Covers M06, M11, M12, M13, M16, M17, and binding decisions D-001 through D-010.
"""

from ubr.legislation.anteproyecto import (
    AnteproyectoCorpus,
    StatutoryArticle,
    StatutoryTitle,
    build_anteproyecto_corpus,
)
from ubr.legislation.bicameral_engine import (
    ChamberVoteResult,
    LegislativePathwaysReport,
    ParliamentaryParty,
    get_spanish_parliamentary_parties,
    simulate_bicameral_pathway,
)
from ubr.legislation.competence_matrix import (
    CompetenceAnchor,
    CompetenceEvaluationResult,
    build_competence_anchors,
    evaluate_competence_architecture,
)
from ubr.legislation.equalization import (
    ForalCupoRecord,
    IntergovernmentalEqualizationReport,
    RegionalEqualizationRecord,
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

__all__ = [
    "AnteproyectoCorpus",
    "StatutoryArticle",
    "StatutoryTitle",
    "build_anteproyecto_corpus",
    "CompetenceAnchor",
    "CompetenceEvaluationResult",
    "build_competence_anchors",
    "evaluate_competence_architecture",
    "RegionalEqualizationRecord",
    "ForalCupoRecord",
    "IntergovernmentalEqualizationReport",
    "calculate_intergovernmental_equalization",
    "ParliamentaryParty",
    "ChamberVoteResult",
    "LegislativePathwaysReport",
    "get_spanish_parliamentary_parties",
    "simulate_bicameral_pathway",
    "export_all_legislation_artifacts",
    "format_anteproyecto_summary",
    "format_competence_matrix_summary",
    "format_equalization_summary",
    "format_bicameral_summary",
    "format_legislation_executive_summary",
]
