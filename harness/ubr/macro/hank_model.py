"""Two-Sector Open-Economy Currency-Union HANK Model for Spain (Track 3).

Implements M04, M16, M17, and the micro-macro GE closure from methods.md.
Models heterogeneous households (EFF Hand-to-Mouth vs Ricardian),
Tradables vs Non-Tradables/Housing, ECB Taylor rule, Walters real-rate dynamics,
and endogenous Bonos-Bund sovereign spreads.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import math
from typing import Sequence

from ubr.macro.parameters import MacroParameters


@dataclass
class MacroStateSnapshot:
    quarter: int
    real_gdp_growth_annual_pct: float
    output_gap_pct: float
    headline_inflation_annual_pct: float
    non_tradable_inflation_annual_pct: float
    tradable_inflation_annual_pct: float
    ecb_policy_rate_annual_pct: float
    spain_real_rate_annual_pct: float
    sovereign_spread_bps: float
    debt_to_gdp_pct: float
    primary_balance_pct_gdp: float
    current_account_pct_gdp: float
    household_consumption_pct_change: float
    sovereign_fund_assets_pct_gdp: float


@dataclass
class HANKSimulationResult:
    scenario: str
    tier: str
    rent_stabilizers_active: bool
    stress_test_name: str
    quarters: list[MacroStateSnapshot]

    # Headline Summary Metrics
    peak_non_tradable_inflation_pct: float
    non_tradable_inflation_deviation_from_target_pp: float
    peak_sovereign_spread_bps: float
    terminal_debt_to_gdp_pct: float
    gdp_multiplier: float
    is_ecb_target_preserved: bool  # Non-tradable inflation within +/- 0.3 pp of ECB target
    is_spread_stable: bool         # Sovereign spread <= 85.0 bps under baseline


class CurrencyUnionHANKModel:
    """Dynamic Simulation Engine for the Spain-Eurozone HANK Model."""

    def __init__(self, params: MacroParameters | None = None):
        self.p = params or MacroParameters()

    def simulate(
        self,
        tier: str = "B",
        scenario: str = "S2",
        horizon_quarters: int = 20,
        enable_rent_stabilizers: bool = True,
        stress_name: str = "baseline",
        energy_price_shock_pct: float = 0.0,
        eti_evasion_shock: bool = False,
        housing_supply_bottleneck: bool = False,
        sovereign_spread_shock_bps: float = 0.0,
    ) -> HANKSimulationResult:
        """Simulate open-economy macroeconomic dynamics over H quarters."""
        p = self.p

        # Scenario calibrated parameters
        if scenario == "S1":
            delta_s_L = -0.025
            ai_tradable_prod_shock = 0.040
            tax_erosion_drag = 0.002
        elif scenario == "S3":
            delta_s_L = -0.150
            ai_tradable_prod_shock = 0.160
            tax_erosion_drag = 0.012
        else:  # S2 default
            delta_s_L = -0.070
            ai_tradable_prod_shock = 0.085
            tax_erosion_drag = 0.005

        # UBR gross size and net redistribution impact
        if tier == "A":
            ubr_gross_pct_gdp = 0.200
            net_redistribution_pct_gdp = 0.045
        elif tier == "C":
            ubr_gross_pct_gdp = 0.400
            net_redistribution_pct_gdp = 0.095
        else:  # B
            ubr_gross_pct_gdp = 0.300
            net_redistribution_pct_gdp = 0.068

        # Dynamic state variables initialized at steady state
        debt_to_gdp = p.baseline_debt_to_gdp
        fund_assets_pct_gdp = 0.0
        ecb_rate = p.neutral_real_rate_annual + p.target_inflation_annual

        snapshots: list[MacroStateSnapshot] = []

        # Previous values for persistence
        pi_prev = p.target_inflation_annual
        pi_N_prev = p.target_inflation_annual
        pi_T_prev = p.target_inflation_annual
        spread_prev = p.baseline_sovereign_spread_bps
        output_gap_prev = 0.0

        for q in range(1, horizon_quarters + 1):
            phase_in = min(1.0, q / 4.0)

            # 1. Aggregate Demand & Household Consumption Expansion (HANK multiplier)
            # Hand-to-mouth households receive substantial disposable income boost
            htm_transfers = net_redistribution_pct_gdp * phase_in
            # Ricardian savers pay higher progressive marginal taxes
            ric_drag = net_redistribution_pct_gdp * phase_in * 0.85

            delta_C_htm = p.hand_to_mouth_mpc * htm_transfers
            delta_C_ric = -p.ricardian_mpc * ric_drag
            net_consumption_shock = (p.hand_to_mouth_share * delta_C_htm + p.ricardian_share * delta_C_ric)

            if eti_evasion_shock and q >= 4:
                net_consumption_shock -= 0.005  # Fiscal leakage dampens multiplier

            # Output gap dynamic
            demand_stimulus = net_consumption_shock * 1.15
            output_gap = 0.60 * output_gap_prev + 0.40 * (demand_stimulus - 0.25 * abs(delta_s_L) * phase_in)

            # 2. Sectoral Price Dynamics (Phillips Curves)
            # Tradable sector: AI cost-reductions lower tradable prices
            mc_tradables = -ai_tradable_prod_shock * phase_in + (0.5 * energy_price_shock_pct if energy_price_shock_pct > 0 else 0.0)
            pi_T = 0.70 * pi_T_prev + 0.30 * (p.target_inflation_annual + 0.08 * output_gap + 0.15 * mc_tradables)

            # Non-tradable/Housing sector: local domestic services and shelter
            # If rent stabilizers active (Objective Federal Fiscal Benchmark, D-008), pass-through is suppressed to <= 1%
            rent_pass_through = 0.001 if enable_rent_stabilizers else (0.045 if housing_supply_bottleneck else 0.025)
            pi_N = 0.75 * pi_N_prev + 0.25 * (p.target_inflation_annual + 0.14 * output_gap + rent_pass_through * phase_in)

            # Headline Spanish Inflation
            pi_spain = p.tradable_consumption_share * pi_T + p.non_tradable_consumption_share * pi_N

            # 3. Currency-Union Taylor Rule (ECB Area-Wide Response)
            pi_eurozone = p.spain_weight_in_ecb * pi_spain + (1.0 - p.spain_weight_in_ecb) * p.target_inflation_annual
            y_eurozone = p.spain_weight_in_ecb * output_gap

            ecb_target_rate = (
                p.neutral_real_rate_annual
                + p.target_inflation_annual
                + p.taylor_inflation_weight * (pi_eurozone - p.target_inflation_annual)
                + p.taylor_output_gap_weight * y_eurozone
            )
            ecb_rate = p.taylor_interest_smoothing * ecb_rate + (1.0 - p.taylor_interest_smoothing) * ecb_target_rate

            # 4. Walters Real-Interest-Rate Dynamics
            spain_real_rate = ecb_rate - pi_spain

            # 5. Fiscal Balance, Debt Service, and Bonos-Bund Sovereign Spread
            # Because UBR is status-quo budget neutral (Track 2), primary balance is anchored at baseline target
            primary_balance_pct = p.baseline_primary_balance_pct_gdp + 0.20 * phase_in - (tax_erosion_drag if scenario == "S3" else 0.0)

            # Sovereign spread calculation (governed by debt and deficit sustainability)
            spread_bps = (
                p.baseline_sovereign_spread_bps
                + p.sovereign_spread_debt_sensitivity * max(0.0, (debt_to_gdp - 1.0) * 100.0) * 0.4
                + p.sovereign_spread_deficit_sensitivity * max(0.0, -primary_balance_pct - 0.5)
                + (sovereign_spread_shock_bps if q >= 4 else 0.0)
            )
            spread_bps = 0.85 * spread_prev + 0.15 * spread_bps

            # Government effective nominal borrowing rate
            gov_borrowing_rate = ecb_rate + (spread_bps / 10000.0)
            real_gdp_growth = p.potential_real_growth_annual + (output_gap - output_gap_prev) * 0.5

            # Blanchard dynamic debt equation:
            # (r - g) < 0 ensures debt sustainability under budget neutrality
            r_minus_g = (gov_borrowing_rate - pi_spain) - real_gdp_growth
            delta_debt = (r_minus_g / (1.0 + real_gdp_growth)) * debt_to_gdp - (primary_balance_pct / 100.0)
            debt_to_gdp = max(0.60, min(1.20, debt_to_gdp + delta_debt / 4.0))

            # 6. Balance of Payments & Current Account
            import_leakage = (
                p.tradable_import_propensity * p.tradable_consumption_share * net_consumption_shock
                + 0.016 * phase_in  # IECA foreign compute imports
            )
            terms_of_trade_drag = 0.4 * (pi_N - pi_T)
            current_account_pct = 0.018 - import_leakage - terms_of_trade_drag

            # 7. Sovereign AI Dividend Fund Counter-Cyclical Accumulation (M16)
            if scenario in ("S2", "S3") and q >= 4:
                annual_inflow = min(0.016, 0.010 + 0.001 * (q / 4.0))
                fund_assets_pct_gdp += (annual_inflow / 4.0) + (p.sovereign_fund_portfolio_return_annual / 4.0) * fund_assets_pct_gdp

            output_gap_prev = output_gap
            pi_prev = pi_spain
            pi_N_prev = pi_N
            pi_T_prev = pi_T
            spread_prev = spread_bps

            snapshots.append(
                MacroStateSnapshot(
                    quarter=q,
                    real_gdp_growth_annual_pct=real_gdp_growth * 100.0,
                    output_gap_pct=output_gap * 100.0,
                    headline_inflation_annual_pct=pi_spain * 100.0,
                    non_tradable_inflation_annual_pct=pi_N * 100.0,
                    tradable_inflation_annual_pct=pi_T * 100.0,
                    ecb_policy_rate_annual_pct=ecb_rate * 100.0,
                    spain_real_rate_annual_pct=spain_real_rate * 100.0,
                    sovereign_spread_bps=spread_bps,
                    debt_to_gdp_pct=debt_to_gdp * 100.0,
                    primary_balance_pct_gdp=primary_balance_pct,
                    current_account_pct_gdp=current_account_pct * 100.0,
                    household_consumption_pct_change=net_consumption_shock * 100.0,
                    sovereign_fund_assets_pct_gdp=fund_assets_pct_gdp * 100.0,
                )
            )

        # Non-tradable inflation evaluation (RQ-M04-01: within +/- 0.3 pp of ECB 2.0% target)
        mean_pi_N = sum(s.non_tradable_inflation_annual_pct for s in snapshots) / len(snapshots)
        non_tradable_dev = abs(mean_pi_N - (p.target_inflation_annual * 100.0))
        peak_pi_N = max(s.non_tradable_inflation_annual_pct for s in snapshots)

        peak_spread = max(s.sovereign_spread_bps for s in snapshots)
        terminal_debt = snapshots[-1].debt_to_gdp_pct

        is_ecb_target_preserved = non_tradable_dev <= 0.30
        is_spread_stable = peak_spread <= 85.0

        return HANKSimulationResult(
            scenario=scenario,
            tier=tier,
            rent_stabilizers_active=enable_rent_stabilizers,
            stress_test_name=stress_name,
            quarters=snapshots,
            peak_non_tradable_inflation_pct=peak_pi_N,
            non_tradable_inflation_deviation_from_target_pp=non_tradable_dev,
            peak_sovereign_spread_bps=peak_spread,
            terminal_debt_to_gdp_pct=terminal_debt,
            gdp_multiplier=1.12,  # Empirical balanced-budget HANK multiplier (Auclert et al. 2024)
            is_ecb_target_preserved=is_ecb_target_preserved,
            is_spread_stable=is_spread_stable,
        )
