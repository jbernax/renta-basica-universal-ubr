"""Experimental Pilot Protocol, GIS Spatial Mapping, Saturation Econometrics, and AEA PAP (Track 4).

Covers M05, M08, M10, M15:
- J=70 spatial cluster design (40 metropolitan FUAs, 30 non-metropolitan with buffer zones)
- MITMA/INE mobile telephony commuting mobility matrix (W_mobility)
- Two-stage randomized saturation power calculation engine (Baird et al., 2018)
- Synthetic Difference-in-Differences (SDID) rental pass-through estimator (Arkhangelsky et al., 2021)
- Saez / Chetty convex disregard bunching and Kleven missing-mass estimators
- Life-cycle structural parameter decomposition (MaCurdy, Blundell, Bargain)
- Cryptographic HMAC-SHA256 register linkage and evaluation stipend retention protocol
- AEA RCT Registry Pre-Analysis Plan (PAP) generator
"""
from __future__ import annotations

from ubr.pilot.clusters import (
    ClusterRegistry,
    MobilityMatrix,
    SpatialCluster,
)
from ubr.pilot.power import (
    MDEResult,
    PowerAnalysisResult,
    TwoStagePowerCalculator,
)
from ubr.pilot.econometrics import (
    BunchingEstimator,
    BunchingResult,
    DecompositionResult,
    LifeCycleDecomposition,
    SDIDResult,
    SpatialSpilloverEstimator,
    SpilloverEstimationResult,
    SyntheticDiffInDiff,
)
from ubr.pilot.data_linkage import (
    BudgetModel,
    DataSpineConfig,
    LinkageAuditResult,
    RegisterLinkageProtocol,
)
from ubr.pilot.pap import (
    AEAPreAnalysisPlan,
    PreAnalysisPlanGenerator,
)
from ubr.pilot.export import (
    export_bunching_json,
    export_clusters_json,
    export_pap_json,
    export_power_json,
    export_sdid_json,
    render_bunching_table,
    render_clusters_table,
    render_decomposition_table,
    render_pilot_summary,
    render_power_table,
    render_sdid_table,
)

__all__ = [
    "SpatialCluster",
    "MobilityMatrix",
    "ClusterRegistry",
    "TwoStagePowerCalculator",
    "PowerAnalysisResult",
    "MDEResult",
    "SyntheticDiffInDiff",
    "SDIDResult",
    "BunchingEstimator",
    "BunchingResult",
    "LifeCycleDecomposition",
    "DecompositionResult",
    "SpatialSpilloverEstimator",
    "SpilloverEstimationResult",
    "RegisterLinkageProtocol",
    "DataSpineConfig",
    "BudgetModel",
    "LinkageAuditResult",
    "PreAnalysisPlanGenerator",
    "AEAPreAnalysisPlan",
    "export_clusters_json",
    "export_power_json",
    "export_sdid_json",
    "export_bunching_json",
    "export_pap_json",
    "render_clusters_table",
    "render_power_table",
    "render_sdid_table",
    "render_bunching_table",
    "render_decomposition_table",
    "render_pilot_summary",
]
