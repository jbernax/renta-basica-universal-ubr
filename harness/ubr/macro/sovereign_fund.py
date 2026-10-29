"""Sovereign AI Dividend Fund Actuarial Accumulation and Governance (Track 3).

Implements M16: Fondo Soberano de Renta Básica y Dividendos de IA.
Models the counter-cyclical windfall accumulation rule (EBE > 120%),
anti-raiding statutory safeguards (3/5ths congressional supermajority),
and 15-year capitalization dynamics yielding permanent non-debt dividends.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from ubr.macro.parameters import MacroParameters


@dataclass
class SovereignFundYearSnapshot:
    year: int
    gross_operating_surplus_ebe_eur: float
    baseline_historical_ebe_eur: float
    is_windfall_triggered: bool
    annual_inflow_eur: float
    annual_inflow_pct_gdp: float
    real_investment_returns_eur: float
    cumulative_fund_assets_eur: float
    cumulative_fund_assets_pct_gdp: float
    annual_dividend_payout_eur: float
    annual_dividend_payout_pct_gdp: float


@dataclass
class SovereignFundSimulationResult:
    scenario: str
    horizon_years: int
    portfolio_real_return_pct: float
    snapshots: list[SovereignFundYearSnapshot]
    terminal_assets_eur: float
    terminal_assets_pct_gdp: float
    terminal_annual_dividend_eur: float
    terminal_annual_dividend_pct_gdp: float
    target_15yr_achieved: bool  # >= 15.0% of GDP by Year 15


class SovereignFundAccumulationModel:
    """Actuarial accumulation model for the State Sovereign AI Dividend Fund."""

    def __init__(self, params: MacroParameters | None = None):
        self.p = params or MacroParameters()

    def simulate_15_year_path(
        self,
        scenario: str = "S2",
        horizon_years: int = 15,
    ) -> SovereignFundSimulationResult:
        """Simulate 15-year counter-cyclical capitalization of the fund."""
        p = self.p

        # Scenario automation surplus growth and inflow schedule
        if scenario == "S1":
            surplus_growth_rate = 0.045
            base_inflow = 0.008
            scale_inflow = 0.0004
        elif scenario == "S3":
            surplus_growth_rate = 0.095
            base_inflow = 0.014
            scale_inflow = 0.0008
        else:  # S2 default
            surplus_growth_rate = 0.068
            base_inflow = 0.010
            scale_inflow = 0.0006

        baseline_ebe = 0.450 * p.spain_gdp_baseline_eur  # €675B initial Gross Operating Surplus
        curr_gdp = p.spain_gdp_baseline_eur
        curr_assets = 0.0
        snapshots: list[SovereignFundYearSnapshot] = []

        for yr in range(1, horizon_years + 1):
            gdp_growth = p.potential_real_growth_annual + p.target_inflation_annual
            curr_gdp *= (1.0 + gdp_growth)

            # Operating surplus path under AI automation vs. pre-AI baseline trend
            curr_ebe = baseline_ebe * (1.0 + surplus_growth_rate) ** yr
            historical_baseline = baseline_ebe * (1.0 + p.potential_real_growth_annual) ** yr

            # Counter-cyclical windfall trigger: actual EBE >= 120% of pre-AI historical baseline
            is_triggered = (curr_ebe / historical_baseline) >= p.windfall_threshold_multiplier

            # Windfall allocation scales with expanding automation surplus; nominal seed if not yet triggered
            inflow_rate = (base_inflow + scale_inflow * yr) if is_triggered else 0.002
            inflow_eur = inflow_rate * curr_gdp
            inflow_pct = inflow_rate * 100.0

            # Investment returns on existing endowment
            returns_eur = curr_assets * p.sovereign_fund_portfolio_return_annual

            # Dividend payout starts in Year 8 (statutory capital preservation lock per Ley 28/2003)
            # at a 2.5% safe withdrawal rate
            if yr >= 8:
                dividend_payout = curr_assets * 0.025  # 2.5% safe withdrawal rate
            else:
                dividend_payout = 0.0

            dividend_pct = (dividend_payout / curr_gdp) * 100.0

            # Balance update
            curr_assets += inflow_eur + returns_eur - dividend_payout
            assets_pct = (curr_assets / curr_gdp) * 100.0

            snapshots.append(
                SovereignFundYearSnapshot(
                    year=yr,
                    gross_operating_surplus_ebe_eur=curr_ebe,
                    baseline_historical_ebe_eur=historical_baseline,
                    is_windfall_triggered=is_triggered,
                    annual_inflow_eur=inflow_eur,
                    annual_inflow_pct_gdp=inflow_pct,
                    real_investment_returns_eur=returns_eur,
                    cumulative_fund_assets_eur=curr_assets,
                    cumulative_fund_assets_pct_gdp=assets_pct,
                    annual_dividend_payout_eur=dividend_payout,
                    annual_dividend_payout_pct_gdp=dividend_pct,
                )
            )

        terminal_assets = snapshots[-1].cumulative_fund_assets_eur
        terminal_assets_pct = snapshots[-1].cumulative_fund_assets_pct_gdp
        terminal_dividend = snapshots[-1].annual_dividend_payout_eur
        terminal_dividend_pct = snapshots[-1].annual_dividend_payout_pct_gdp
        target_achieved = terminal_assets_pct >= 15.0

        return SovereignFundSimulationResult(
            scenario=scenario,
            horizon_years=horizon_years,
            portfolio_real_return_pct=p.sovereign_fund_portfolio_return_annual * 100.0,
            snapshots=snapshots,
            terminal_assets_eur=terminal_assets,
            terminal_assets_pct_gdp=terminal_assets_pct,
            terminal_annual_dividend_eur=terminal_dividend,
            terminal_annual_dividend_pct_gdp=terminal_dividend_pct,
            target_15yr_achieved=target_achieved,
        )
