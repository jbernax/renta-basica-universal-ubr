"""AEA RCT Registry Pre-Analysis Plan (PAP) Generator (Track 4).

Generates a machine-readable, registry-compliant Pre-Analysis Plan following
AEA RCT Registry guidelines (Duflo et al., 2007; Christensen & Miguel, 2018).
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
import json
from typing import Any


@dataclass
class PreRegisteredHypothesis:
    hypothesis_id: str
    category: str
    statement: str
    target_metric: str
    expected_direction: str
    primary_register: str
    econometric_estimator: str
    significance_level_alpha: float = 0.05


@dataclass
class PrimaryOutcomeEndpoint:
    outcome_id: str
    name: str
    description: str
    source_register: str
    measurement_frequency: str
    baseline_value: float
    mde_threshold: float
    family_group: str


@dataclass
class AEAPreAnalysisPlan:
    trial_id: str
    title: str
    lead_institution: str
    consortium_partners: list[str]
    registration_date: str
    trial_duration_months: int
    cluster_design_summary: dict[str, Any]
    experimental_arms: dict[str, Any]
    hypotheses: list[PreRegisteredHypothesis]
    primary_endpoints: list[PrimaryOutcomeEndpoint]
    econometric_equations: dict[str, str]
    multiple_testing_corrections: dict[str, str]
    data_governance_and_privacy: dict[str, str]
    finite_horizon_mitigations: dict[str, str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class PreAnalysisPlanGenerator:
    """Builds the comprehensive Pre-Analysis Plan artifact for Spain's UBR pilot."""

    def generate_plan(self) -> AEAPreAnalysisPlan:
        hypotheses = [
            PreRegisteredHypothesis(
                hypothesis_id="H1-LaborSupply",
                category="Labor Supply & Participation",
                statement="Unconditional cash transfers reduce weekly hours worked by <= 1.5 h/week, concentrated in voluntary overtime reductions among secondary earners, with zero net contraction in formal participation.",
                target_metric="Hours worked per week (TGSS/MCVL)",
                expected_direction="Small negative (in [-1.5, 0.0])",
                primary_register="TGSS MCVL (bases de cotización & coeficientes de parcialidad)",
                econometric_estimator="Continuous Spatial Spillover OLS with Wild Cluster Bootstrap",
            ),
            PreRegisteredHypothesis(
                hypothesis_id="H2-RentalPassThrough",
                category="Housing & Landlord Capture",
                statement="In supply-inelastic clusters, rental pass-through on active 5-year LAU contracts is <= 5.0%, while turnover leases experience 25-35% pass-through, mitigated by the federal fiscal benchmark.",
                target_metric="Quarterly transaction rent in EUR/m2",
                expected_direction="Dual divergence (active near 0%, turnover positive)",
                primary_register="Regional Rental Deposit Registries (INCASÒL, IVIMA, AVRA)",
                econometric_estimator="Synthetic Difference-in-Differences (SDID)",
            ),
            PreRegisteredHypothesis(
                hypothesis_id="H3-ReservationWages",
                category="Search & Match Quality",
                statement="Unconditional liquidity increases post-displacement search duration by 3-6 weeks, yielding 6-10% higher subsequent wage stability and higher self-employment survival.",
                target_metric="Post-unemployment wage and 12-month contract survival",
                expected_direction="Positive (+6% to +10%)",
                primary_register="SEPE Unemployment Registries & TGSS Affiliation",
                econometric_estimator="Cox Proportional Hazards & IV Matching",
            ),
            PreRegisteredHypothesis(
                hypothesis_id="H4-MentalHealthWellbeing",
                category="Health & Wellbeing",
                statement="UBR receipt improves standardized subjective wellbeing by >= +0.25 SD and reduces psychotropic medical prescription billing by >= 15%.",
                target_metric="GHQ-12 Mental Health Index & SNS Prescription Claims",
                expected_direction="Positive improvement (+0.25 SD)",
                primary_register="INSS Tier 1 Temporary Disability & Regional Health Services",
                econometric_estimator="ANCOVA with baseline adjustment and cluster clustering",
            ),
            PreRegisteredHypothesis(
                hypothesis_id="H5-LaborRationingSeparation",
                category="AI Displacement Decomposition",
                statement="Life-cycle structural decomposition proves that >= 60% of observed non-employment in high AI-exposure CNO-11 occupations is attributable to structural labor demand rationing rather than voluntary leisure preferences.",
                target_metric="Involuntary rationing component zeta * P_disp",
                expected_direction="Rationing share >= 60%",
                primary_register="EPA Flow Data + Track 1 CNO-11 Exposure Crosswalk",
                econometric_estimator="Structural Life-Cycle Decomposition (MaCurdy/Blundell/Bargain)",
            ),
        ]

        endpoints = [
            PrimaryOutcomeEndpoint(
                outcome_id="OUT_01",
                name="Weekly Hours Worked",
                description="Effective weekly hours calculated from TGSS contract coefficient and daily affiliation records",
                source_register="TGSS MCVL",
                measurement_frequency="Monthly",
                baseline_value=37.5,
                mde_threshold=1.20,
                family_group="Labor Market Responses",
            ),
            PrimaryOutcomeEndpoint(
                outcome_id="OUT_02",
                name="Executed Transaction Rent",
                description="Executed lease rent in EUR/month for mandatory rental deposits linked by cadastral reference",
                source_register="INCASÒL / IVIMA / AVRA",
                measurement_frequency="Monthly",
                baseline_value=750.0,
                mde_threshold=21.0,
                family_group="Housing Markets",
            ),
            PrimaryOutcomeEndpoint(
                outcome_id="OUT_03",
                name="Annual Taxable Labor Earnings",
                description="Gross earned income declared under AEAT Modelo 190 / Modelo 100",
                source_register="AEAT / Basque & Navarrese Treasuries",
                measurement_frequency="Annual",
                baseline_value=24200.0,
                mde_threshold=650.0,
                family_group="Labor Market Responses",
            ),
            PrimaryOutcomeEndpoint(
                outcome_id="OUT_04",
                name="Temporary Incapacity Days",
                description="Cumulative days on medically certified sick leave (bajas IT) for stress or depression",
                source_register="INSS Central IT Register",
                measurement_frequency="Quarterly",
                baseline_value=18.4,
                mde_threshold=2.5,
                family_group="Health & Wellbeing",
            ),
            PrimaryOutcomeEndpoint(
                outcome_id="OUT_05",
                name="Solo Self-Employment Entry",
                description="Net transitions into RETA (Régimen Especial de Trabajadores Autónomos)",
                source_register="TGSS Affiliation",
                measurement_frequency="Quarterly",
                baseline_value=8.2,
                mde_threshold=1.4,
                family_group="Entrepreneurship",
            ),
        ]

        equations = {
            "spatial_spillover_model": (
                "Y_{ic} = alpha + beta_1 * T_{ic} + beta_2 * Cash_c + "
                "gamma * sum_j W_{cj} Cash_j + X'_{ic} delta + eps_{ic}"
            ),
            "synthetic_diff_in_diff": (
                "tau_SDID = (Y_{post, treat} - sum_i omega_i Y_{post, i}) - "
                "sum_t lambda_t (Y_{t, treat} - sum_i omega_i Y_{ti})"
            ),
            "saez_chetty_convex_bunching": (
                "b = B / h_0(K) ; eps^c = (b * Delta_w) / (K * ln((1 - tau_1) / (1 - tau_2)))"
            ),
            "lifecycle_frisch_decomposition": (
                "Delta ln h = eps^Frisch Delta ln w^trans + eps^c Delta ln w^perm + "
                "eta [G_pilot / (A + H) * (1 - (1+r)^-T) / (1 - (1+r)^-(T_ret - t))] + "
                "zeta_rationing * P_disp + e"
            ),
        }

        fwer_info = {
            "fwer_primary_family": "Bonferroni-Holm step-down procedure applied within primary outcome families (Labor, Housing, Health).",
            "fdr_exploratory_endpoints": "Benjamini-Hochberg procedure with q = 0.05 applied across all exploratory secondary outcomes.",
            "cluster_inference": "Wild Cluster Bootstrap (Rademacher 2-point weights) with 999 replications, complemented by Fisher Randomization Inference.",
        }

        privacy_info = {
            "pseudonymization": "HMAC-SHA256 salted hashing with master secret held exclusively by AEAT/INE statistical firewall.",
            "legal_basis": "Art. 95.1.k Ley General Tributaria (LGT) and Ley Orgánica 3/2018 (LOPDGDD).",
            "access_tiering": "Tier 1 centralized register access through INE secure data enclaves; Tier 2 regional health via Bilateral Convenios under Ley 16/2003.",
        }

        finite_horizon = {
            "step_down_ramp": "6-month post-pilot phase-out ramp (100% -> 66% -> 33% -> 0%) to prevent welfare cliffs and post-trial dislocation.",
            "sabbatical_separation": "Structural discount factor formula separates temporary 36-month leisure elasticity from permanent life-cycle labor supply.",
        }

        cluster_summary = {
            "total_clusters": 70,
            "treated_clusters": 35,
            "control_clusters": 35,
            "metropolitan_fua_clusters": 40,
            "non_metropolitan_clusters": 30,
            "fua_self_containment_threshold": ">= 80% internal daily commuting retention",
            "non_metro_buffer_ring": ">= 2 to 5 km cash-free geographic buffer",
            "total_participants": 20000,
        }

        arms_summary = {
            "Arm_A": {
                "name": "Pure UBR (0% clawback)",
                "transfer_monthly_eur": 900.0,
                "disregard_annual_eur": None,
                "clawback_rate": 0.0,
                "notch_ceiling_eur": None,
                "share_of_treated": 0.34,
            },
            "Arm_B": {
                "name": "Moderate Clawback (38%)",
                "transfer_monthly_eur": 900.0,
                "disregard_annual_eur": 3600.0,
                "clawback_rate": 0.38,
                "notch_ceiling_eur": 28421.05,
                "share_of_treated": 0.33,
            },
            "Arm_C": {
                "name": "High Clawback (50%)",
                "transfer_monthly_eur": 900.0,
                "disregard_annual_eur": 3600.0,
                "clawback_rate": 0.50,
                "notch_ceiling_eur": 21600.00,
                "share_of_treated": 0.33,
            },
        }

        return AEAPreAnalysisPlan(
            trial_id="AEARCTR-0014821",
            title="Multi-Level Randomized Saturation Trial of Universal Basic Rent in Spain: Labor Supply, Housing Pass-Through, and AI Disruption",
            lead_institution="Consorcio de Investigación en Renta Básica Universal (CIRBU)",
            consortium_partners=[
                "Centro de Estudios Monetarios y Financieros (CEMFI)",
                "Institut Català d'Avaluació de Polítiques Públiques (Ivàlua)",
                "J-PAL Europe",
                "Hacienda Foral de Bizkaia / Gipuzkoa",
                "Instituto Nacional de Estadística (INE)",
                "Agencia Estatal de Administración Tributaria (AEAT)",
            ],
            registration_date="2026-10-29",
            trial_duration_months=36,
            cluster_design_summary=cluster_summary,
            experimental_arms=arms_summary,
            hypotheses=hypotheses,
            primary_endpoints=endpoints,
            econometric_equations=equations,
            multiple_testing_corrections=fwer_info,
            data_governance_and_privacy=privacy_info,
            finite_horizon_mitigations=finite_horizon,
        )
