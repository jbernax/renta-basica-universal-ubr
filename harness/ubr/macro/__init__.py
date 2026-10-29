"""Currency-Union Open-Economy HANK Model for Spain - Track 3.

Implements:
- M04: Two-sector HANK model, ECB Taylor rule, Walters real-rate dynamics, sovereign spreads
- M16: Sovereign AI Dividend Fund counter-cyclical accumulation and governance
- M17: Adversarial compound tail-risk stress tests and statutory circuit-breakers
- Regulation (EU) 2024/1263: Net Primary Expenditure ceiling & Control Account tracking
"""
from ubr.macro.parameters import MacroParameters
from ubr.macro.hank_model import (
    CurrencyUnionHANKModel,
    HANKSimulationResult,
    MacroStateSnapshot,
)
from ubr.macro.fiscal_rules import (
    AnnualFiscalComplianceRecord,
    EUFiscalGovernanceValidator,
    FiscalRulesEvaluationResult,
)
from ubr.macro.sovereign_fund import (
    SovereignFundAccumulationModel,
    SovereignFundSimulationResult,
    SovereignFundYearSnapshot,
)
from ubr.macro.stress_tests import (
    MacroStressTestHarness,
    StressTestBatteryResult,
    StressTestOutcome,
)
from ubr.macro.export import (
    export_fiscal_rules_json,
    export_hank_json,
    export_sovereign_fund_json,
    export_stress_tests_json,
    render_fiscal_rules_table,
    render_irf_table,
    render_sovereign_fund_table,
    render_stress_battery_table,
)

__all__ = [
    "MacroParameters",
    "CurrencyUnionHANKModel",
    "HANKSimulationResult",
    "MacroStateSnapshot",
    "AnnualFiscalComplianceRecord",
    "EUFiscalGovernanceValidator",
    "FiscalRulesEvaluationResult",
    "SovereignFundAccumulationModel",
    "SovereignFundSimulationResult",
    "SovereignFundYearSnapshot",
    "MacroStressTestHarness",
    "StressTestBatteryResult",
    "StressTestOutcome",
    "export_fiscal_rules_json",
    "export_hank_json",
    "export_sovereign_fund_json",
    "export_stress_tests_json",
    "render_fiscal_rules_table",
    "render_irf_table",
    "render_sovereign_fund_table",
    "render_stress_battery_table",
]
