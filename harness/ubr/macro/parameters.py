"""Calibrated Parameters for Open-Economy Currency-Union HANK Model (Track 3).

Calibrated to Banco de España Encuesta Financiera de las Familias (EFF),
INE Contabilidad Nacional, and EU Regulation (EU) 2024/1263.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MacroParameters:
    # Baseline National Accounts (Spain 2024-2026)
    spain_gdp_baseline_eur: float = 1_500_000_000_000.0  # €1.50 Trillion
    baseline_debt_to_gdp: float = 1.050                  # 105.0% of GDP
    baseline_primary_balance_pct_gdp: float = -0.50      # -0.50% of GDP
    baseline_sovereign_spread_bps: float = 80.0          # 80 bps Bonos-Bund spread
    potential_real_growth_annual: float = 0.018          # 1.8% potential real growth
    target_inflation_annual: float = 0.020               # 2.0% ECB inflation target
    neutral_real_rate_annual: float = 0.010              # 1.0% r* neutral rate

    # Eurozone Monetary Union & ECB Policy Rule
    spain_weight_in_ecb: float = 0.10                    # 10% Spanish weight in Eurozone
    taylor_inflation_weight: float = 1.50                # phi_pi
    taylor_output_gap_weight: float = 0.50               # phi_y
    taylor_interest_smoothing: float = 0.80              # rho_i
    sovereign_spread_debt_sensitivity: float = 1.20      # Spread sensitivity to debt-to-GDP (bps per pp)
    sovereign_spread_deficit_sensitivity: float = 8.5    # Spread sensitivity to primary deficit (bps per pp)

    # Household Heterogeneity & Consumption Behavior (Banco de España EFF)
    hand_to_mouth_share: float = 0.35                    # lambda_HtM (35% liquidity constrained)
    hand_to_mouth_mpc: float = 0.75                      # High marginal propensity to consume
    ricardian_share: float = 0.65                        # 65% optimizing / wealthy savers
    ricardian_mpc: float = 0.15                          # Low marginal propensity to consume

    # Two-Sector Trade & Consumption Structure (Tradables vs Non-Tradables/Housing)
    tradable_consumption_share: float = 0.45             # gamma_T
    non_tradable_consumption_share: float = 0.55         # gamma_N (services & housing)
    tradable_import_propensity: float = 0.42             # High import leakage in manufactured goods/energy
    non_tradable_import_propensity: float = 0.08         # Low import leakage in domestic services/rents
    calvo_stickiness_tradables: float = 0.60             # theta_T (quarterly price rigidity)
    calvo_stickiness_non_tradables: float = 0.75         # theta_N (sticky service & rental prices)
    elasticity_substitution_tn: float = 0.85             # Intratemporal elasticity between T and N

    # EU Regulation (EU) 2024/1263 Governance Ceilings
    npe_max_growth_annual: float = 0.028                 # 2.8% max nominal Net Primary Expenditure growth
    control_account_annual_debit_ceiling_pct_gdp: float = 0.30  # 0.30% of GDP
    control_account_cumulative_debit_ceiling_pct_gdp: float = 0.60  # 0.60% of GDP
    edp_deficit_threshold_pct_gdp: float = 3.00          # 3.0% GDP deficit ceiling

    # Sovereign AI Dividend Fund (M16)
    windfall_threshold_multiplier: float = 1.20          # Inflows when EBE > 120% baseline
    sovereign_fund_portfolio_return_annual: float = 0.045 # 4.5% real expected return
