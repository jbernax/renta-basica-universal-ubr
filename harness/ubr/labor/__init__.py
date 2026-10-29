"""Empirical Labor Displacement, Task Exposure, and AI Scenarios for Spain (Track 1)."""
from ubr.labor.cno_taxonomy import CNOTaxonomy, CNOGroup
from ubr.labor.task_exposure import TaskExposureEngine, ExposureScore
from ubr.labor.institutions import SpanishLaborInstitutions
from ubr.labor.scenarios import LaborDisplacementSimulator, ScenarioResult
from ubr.labor.export import export_counterfactual_json

__all__ = [
    "CNOTaxonomy",
    "CNOGroup",
    "TaskExposureEngine",
    "ExposureScore",
    "SpanishLaborInstitutions",
    "LaborDisplacementSimulator",
    "ScenarioResult",
    "export_counterfactual_json",
]
