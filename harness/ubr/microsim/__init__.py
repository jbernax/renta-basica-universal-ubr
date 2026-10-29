"""Microsimulation Engine for Universal Basic Rent (Spain) - Track 2.

Integrates EUROMOD-Spain / Python simulation pipeline:
- M02: Benefit parameters, disability complements, parity-modulated child scale
- M03: Progressive IRPF restructuring, behavioral ETI, and General Government Fiscal Bridge
- M07: Dual-Pillar contributory pension integration and No-Loser Guarantee
- M09: Distributional atlas, dual BHC/AHC poverty indices, and housing rent-capture
"""
from ubr.microsim.population import (
    DisabilityGrade,
    HousingTenure,
    MicroHousehold,
    MicroIndividual,
    PopulationDataset,
    TerritorialRegime,
    generate_calibrated_spanish_population,
)
from ubr.microsim.benefits import (
    BenefitCalculator,
    BenefitDisbursement,
    HouseholdBenefitResult,
    TIER_SPECS,
    TierParameters,
    UBRTier,
)
from ubr.microsim.taxation import (
    BASELINE_IRPF_BRACKETS,
    FiscalBridgeBreakdown,
    IndividualTaxResult,
    REFORM_IRPF_BRACKETS,
    TaxBracket,
    TaxCalculator,
)
from ubr.microsim.housing import (
    HouseholdHousingResult,
    HousingAggregateMetrics,
    HousingCalculator,
)
from ubr.microsim.poverty_metrics import (
    DistributionalSummary,
    FGTResult,
    compute_atkinson,
    compute_fgt,
    compute_gini,
    compute_s80_s20,
    compute_theil,
    compute_weighted_median,
)
from ubr.microsim.engine import (
    DecileDistributionRow,
    MicrosimulationEngine,
    SimulationRunResult,
)
from ubr.microsim.export import (
    export_microsim_json,
    render_decile_table,
    render_fiscal_bridge_table,
    render_poverty_table,
)

__all__ = [
    "DisabilityGrade",
    "HousingTenure",
    "MicroHousehold",
    "MicroIndividual",
    "PopulationDataset",
    "TerritorialRegime",
    "generate_calibrated_spanish_population",
    "BenefitCalculator",
    "BenefitDisbursement",
    "HouseholdBenefitResult",
    "TIER_SPECS",
    "TierParameters",
    "UBRTier",
    "BASELINE_IRPF_BRACKETS",
    "FiscalBridgeBreakdown",
    "IndividualTaxResult",
    "REFORM_IRPF_BRACKETS",
    "TaxBracket",
    "TaxCalculator",
    "HouseholdHousingResult",
    "HousingAggregateMetrics",
    "HousingCalculator",
    "DistributionalSummary",
    "FGTResult",
    "compute_atkinson",
    "compute_fgt",
    "compute_gini",
    "compute_s80_s20",
    "compute_theil",
    "compute_weighted_median",
    "DecileDistributionRow",
    "MicrosimulationEngine",
    "SimulationRunResult",
    "export_microsim_json",
    "render_decile_table",
    "render_fiscal_bridge_table",
    "render_poverty_table",
]
