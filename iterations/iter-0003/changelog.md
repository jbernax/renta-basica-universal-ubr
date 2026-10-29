# Changelog — Iteration 0003 (`iter-0003`)

## Overview
Iteration 0003 completed the full specialist review cycle across all 9 research dimensions (`labor-economist`, `public-finance`, `macroeconomist`, `spanish-eu-law`, `social-policy`, `evaluation-methodologist`, `housing-economist`, `political-economist`, and `red-team`). A total of 40 concrete issues were synthesized into 9 unified, actionable proposals (`SYN-03-01` through `SYN-03-09`). 

These proposals were systematically executed across `plan/methods.md`, 16 factor modules (`M01`, `M02`, `M03`, `M05`, `M06`, `M07`, `M08`, `M09`, `M10`, `M11`, `M12`, `M13`, `M14`, `M15`, `M16`, and `M17`), and `plan/sources.yaml` (expanding the verified bibliography from 86 to 126 machine-verified sources).

---

## Applied Changes by Proposal

### `SYN-03-01` · Macro-Micro Accounting & Fiscal Realism: Disentangling Baseline Revenue Losses from GDP Ratios
- **Contributing Issues:** `RT-03-03` (critical), `MA-03-01` (critical), `PF-03-04` (major)
- **Target Files:**
  - `plan/methods.md`
  - `plan/modules/M01-ai-labor-displacement.md`
  - `plan/modules/M03-fiscal-financing.md`
- **Summary of Changes:**
  - Disentangled the relative labor tax base contraction from absolute percentage points of GDP: under S1 ($\Delta s_L = -2.5$ pp), baseline revenue erosion is ~0.98% of GDP; under S2 ($\Delta s_L = -7.0$ pp), baseline erosion is ~2.73% of GDP (~€41B/year on Spain's €1,500B GDP at a 39% tax wedge); under S3 ($\Delta s_L = -15.0$ pp), baseline erosion is ~5.85% of GDP.
  - Reconciled the consolidated *Administraciones Públicas* fiscal bridge in `M03`: gross outlays (-30.0% GDP) balanced against non-contributory welfare offsets (+0.95% GDP), contributory pension integration (+5.8% GDP net of tax shields), restructured IRPF rates on remaining labor and capital (+22.5% GDP, decile 84 breakeven), corporate surplus and AI compute withholding (+2.8% GDP), and consumption/wealth taxes (+0.7% GDP).
  - Extended the dynamic macro-micro closure in `methods.md` to incorporate endogenous sovereign debt service feedback ($\Delta (r_t - g_t) D_{t-1}$) under EU Regulation 2024/1263 Net Primary Expenditure rules.
- **Sources Cited:** `kaplan-moll-violante-2018-hank`, `auclert-rognlie-straub-2024`, `regulation-eu-2024-1263-net-expenditure`.

### `SYN-03-02` · Foreign AI Compute Tax Enforcement & Domestic B2B Reverse-Charge Architecture
- **Contributing Issues:** `RT-03-01` (critical / `JD-02-01`), `PF-03-02` (critical)
- **Target Files:**
  - `plan/modules/M16-ai-rent-capture-sovereign-fund.md`
  - `plan/modules/M03-fiscal-financing.md`
- **Summary of Changes:**
  - Formulated the *Impuesto Especial sobre Capacidad y Computación de IA* (*IECA*) under *RDLeg 5/2004* (TRIRNR) and *Ley 58/2003* (LGT), establishing a domestic B2B destination-based withholding / reverse-charge mechanism on cloud compute, GPU hosting, and foundation model API inference purchased from non-resident providers lacking physical permanent establishments.
  - Enforced domestic compliance by amending *Ley 27/2014* (LIS Art. 15) to condition corporate tax deductibility of cloud compute expenses on verified withholding certificates, overcoming OECD Double Taxation Treaty permanent establishment loopholes.
  - Replaced rigid annual Sovereign Fund accumulation targets with a Counter-Cyclical Windfall Accumulation Rule (funding triggered only when sectoral operating surplus exceeds 120% of historical baselines), preventing frontloaded primary deficit drag under Regulation (EU) 2024/1263.
  - Established constitutional non-confiscatoriness limits for capital rent capture under Art. 31.3 CE and STC 182/2021.
- **Sources Cited:** `rdleg-5-2004-trirnr`, `boe-lgt-2003`, `ley-27-2014-impuesto-sociedades`, `oecd-model-tax-convention-2017`, `council-directive-2022-2523-pillar2`, `devereux-2021-taxing-profit`, `regulation-eu-2024-1263-net-expenditure`, `stc-182-2021-plusvalia`.

### `SYN-03-03` · Spatial Commuting Mobility Spillover Closure & Two-Stage Saturation Econometrics
- **Contributing Issues:** `RT-03-02` (critical / `JD-02-02`), `EM-03-02` (critical)
- **Target Files:**
  - `plan/methods.md`
  - `plan/modules/M10-pilot-evaluation-design.md`
- **Summary of Changes:**
  - Integrated MITMA/INE mobile telephony commuting matrices into an empirical spatial weight matrix ($W_{\text{mobility}}$), specifying continuous spatial spillover exposure estimators to eliminate residual SUTVA violations across municipal commuting borders.
  - Replaced single-stage cluster MDE formulas with Baird et al. (2018) two-stage saturation variance math, accounting for intra-cluster correlation and cross-cluster spillovers.
  - Stratified rental evaluation clusters by private rental density (>35%), mandated 100% census linkage with regional tenancy deposit registries (INCASÒL, IVIMA, AVRA), and pre-specified Synthetic Difference-in-Differences (SDID, Arkhangelsky et al. 2021).
- **Sources Cited:** `ine-movilidad-bigdata-2024`, `baird-2018-interference`, `arkhangelsky-2021-sdid`.

### `SYN-03-04` · Non-Convex Kink Resolution & Missing-Mass Econometric Correction
- **Contributing Issues:** `EM-03-01` (critical), `EM-03-04` (major)
- **Target Files:**
  - `plan/methods.md`
  - `plan/modules/M08-labor-supply-behavior.md`
  - `plan/modules/M10-pilot-evaluation-design.md`
  - `plan/modules/M15-international-evidence.md`
- **Summary of Changes:**
  - Resolved the non-convex (concave) kink at the clawback phase-out boundary by introducing an initial labor earnings disregard ($Y_{\text{disregard}} = \text{€}3,000\text{--}\text{€}5,000/\text{year}$, aligned with RDL 2/2024 CAE). This creates a true convex kink with excess bunching mass for Saez (2010) and Chetty et al. (2011) estimators, while formalizing a missing-mass estimator at the upper clawback ceiling $Y^*$.
  - Corrected the structural life-cycle hours equation in `M15` and `methods.md`: paired Frisch elasticity with transitory wage variation rather than wealth, and conditioned Bayesian priors on Bargain, Orsini, & Peichl (2014) labor-demand rationing vectors derived from `M01`.
- **Sources Cited:** `saez-2010-bunching`, `chetty-2011-bounds`, `macurdy-1981-labor-supply`, `blundell-macurdy-1999-labor-supply`, `bargain-2014-labor-rationing`, `rdl-2-2024-desempleo`.

### `SYN-03-05` · Fiscal Federalism Reconciliation: Common Regime VFI, Cession Adjustments, and Foral Clearing
- **Contributing Issues:** `LW-03-01` (critical), `PF-03-01` (critical), `PE-03-03` (major), `RT-03-05` (major)
- **Target Files:**
  - `plan/methods.md`
  - `plan/modules/M03-fiscal-financing.md`
  - `plan/modules/M06-constitutional-eu-law.md`
  - `plan/modules/M11-political-economy.md`
- **Summary of Changes:**
  - Strictly bifurcated territorial financing mechanisms:
    - **Foral Regimes:** Classified UBR as a non-assumed power (*carga no asumida*) strictly within the bilateral *Comisión Mixta del Concierto* and *Comisión Coordinadora del Convenio*, specifying adjustments to the *Cupo* ($I_{\text{Cupo}} = 6.24\%$) and *Aportación* ($I_{\text{Aportación}} = 1.6\%$) bases. Confirmed that Basque and Navarrese *Haciendas Forales* administer tax credits directly under foral tax sovereignty (*Ley 12/2002*, *Ley 28/1990*).
    - **Common Regime (15 CCAA):** Enacted statutory amendments to *LOFCA* (Art. 13) and *Ley 22/2009* establishing a *Fondo de Compensación UBR* within the CPFF to neutralize regional windfalls from ceded IRPF shares and recapture regional minimum income savings for social housing and SAAD care.
  - Detailed the bilateral tax harmonization mechanism under Art. 6 *Ley 12/2002* and Art. 7 *Ley 28/1990* via model *Normas Forales* and *Leyes Forales*.
- **Sources Cited:** `ley-12-2002-concierto-economico`, `ley-28-1990-convenio-navarra`, `ley-22-2009-financiacion-autonomica`, `boe-lofca-1980`.

### `SYN-03-06` · Social Security Pension Accrual Continuity, Disability Tax-Shield, and Debt Immunity
- **Contributing Issues:** `LW-03-02` (critical), `SP-03-01` (critical), `SP-03-02` (critical), `LW-03-03` (major)
- **Target Files:**
  - `plan/modules/M07-welfare-benefit-integration.md`
  - `plan/modules/M12-administration-delivery.md`
- **Summary of Changes:**
  - Codified a statutory Contribution Continuity Guarantee (*Garantía de Mantenimiento de Bases de Cotización por Desempleo*) under Art. 273 TRLGSS, mandating SEPE to maintain retirement contributions throughout unemployment regardless of UBR cash offsets, avoiding pension penalty gaps (*lagunas de cotización*, Art. 209 TRLGSS). Established the universal *Crédito Cotizatorio Básico por Transición Tecnológica* guaranteeing continuous pension accrual at 100% of SMI base for displaced workers.
  - Guaranteed 100% statutory tax exemption for contributory permanent disability pensions (*Incapacidad Permanente Absoluta* and *Gran Invalidez*, Art. 7.f LIRPF).
  - Amended the *inembargabilidad* shield in `M12` to carve out judicial child support and alimony orders under Art. 608 LEC, while establishing absolute immunity from commercial bank overdraft offsets and internal administrative set-offs (Art. 53.2 TRLGSS, Arts. 71–73 LGT) for retroactive IMV debts.
  - Corrected statutory attribution of automated administrative acts to Art. 41 of *Ley 40/2015* (LRJSP) and prior hearing guarantees to Art. 82 of *Ley 39/2015* (LPAC).
- **Sources Cited:** `boe-trlgss-2015`, `ley-1-2000-lec`, `ley-40-2015-lrjsp`, `boe-lpac-2015`, `boe-lgt-2003`.

### `SYN-03-07` · Housing Competence Asymmetries, Rental Nowcasting, and Spatial Immobility Frictions
- **Contributing Issues:** `HE-03-01` (critical), `HE-03-02` (major), `HE-03-03` (major), `HE-03-04` (major)
- **Target Files:**
  - `plan/modules/M05-housing-rent-capture.md`
  - `plan/modules/M09-distribution-poverty-euromod.md`
  - `plan/modules/M13-migration-territory-residency.md`
  - `plan/modules/M17-transition-risks-stress-tests.md`
- **Summary of Changes:**
  - Decoupled federal housing circuit-breakers and tax conditionality from regional ZMRT declarations under *Ley 12/2023* (boycotted by Madrid, Andalusia, Balearics, Valencia under STC 79/2024), establishing an Objective Federal Fiscal Benchmark on LIRPF Art. 23.2 reductions under State tax competence (Art. 149.1.14 CE).
  - Specified a High-Frequency Rental Nowcasting Spine (monthly tenancy deposits, scraped portal APIs with $\le 30$-day latency) and established the *Fondo de Estabilización Residencial* (FER) under ICO credit lines with LOEPSF expenditure ceiling exemptions for municipal preemption (*tanteo y retracto*).
  - Mandated dual reporting of Before-Housing-Cost (BHC) and After-Housing-Cost (AHC) poverty ($P_0, P_1, P_2$) and AHC Gini in EUROMOD-Spain, disaggregating landlord ownership across physical persons, SOCIMIs, and non-resident owners.
  - Modeled joint household utility with dual-earner career disruption penalties (Costa & Kahn 2000) and paired UBR with a rural housing mobilization program (*Programa de Movilización de Vivienda Rural Vacía* via ICO loans).
- **Sources Cited:** `stc-79-2024-vivienda`, `khametshin-2024-rental`, `costa-kahn-2000-power-couples`, `boe-vivienda-2023`.

### `SYN-03-08` · Constitutional Tax Legality, Bicameral Override, and Tripartite Employer Dialogue
- **Contributing Issues:** `PE-03-01` (critical), `PE-03-02` (critical), `PE-03-04` (major), `LW-03-04` (critical)
- **Target Files:**
  - `plan/modules/M11-political-economy.md`
  - `plan/modules/M13-migration-territory-residency.md`
  - `plan/modules/M17-transition-risks-stress-tests.md`
- **Summary of Changes:**
  - Excised unconstitutional decree-law tax surcharge delegations under Art. 86 CE (STC 73/2017, STC 78/2020) in `M17`, replacing them with pre-enacted statutory automatic rate stabilizers and expedited parliamentary urgency (*urgencia parlamentaria*, Art. 93 Reglamento del Congreso).
  - In `M11`, detailed the organic legislative strategy in Congress to amend LOEPSF Art. 15.6 by absolute majority to restore constitutional lower-house preeminence (Art. 90.2 CE, STC 179/1989), neutralizing the Senate's absolute veto over spending ceilings. Formulated the tripartite dialogue table under Art. 7 CE embedding CEOE and CEPYME alongside CCOO and UGT, and incorporated the CARIN deservingness heuristic (van Oorschot 2000).
  - In `M13`, established an objective Social Security threshold for EU workers under Art. 45 TFEU / Regulation 492/2011 (Case 66/85 *Lawrie-Blum*, Case C-14/09 *Genc*) with pro-rata tapering, codified a Default Non-Refundable Mínimo Personal y Familiar in *Ley 35/2006* to safeguard the constitutional *mínimo existencial* (STC 214/1994), and enacted an unconditional child subsistence safe-harbor under Art. 39 CE.
- **Sources Cited:** `stc-73-2017`, `stc-78-2020`, `stc-179-1989`, `van-oorschot-2000-deservingness`, `eu-regulation-492-2011`, `cjeu-c-66-85-lawrie-blum`, `cjeu-c-14-09-genc`, `stc-214-1994-minimo-existencial`, `boe-ce-1978`.

### `SYN-03-09` · Labor Market Institutions, Assistential Reforms (RDL 2/2024), and Healthcare Register Bifurcation
- **Contributing Issues:** `LE-03-01` (critical), `LE-03-02` (critical), `LE-03-03` (major), `LE-03-04` (major), `RT-03-04` (major), `RT-03-06` (minor), `EM-03-03` (major), `SP-03-03` (major), `SP-03-05` (major)
- **Target Files:**
  - `plan/modules/M01-ai-labor-displacement.md`
  - `plan/modules/M02-benefit-design.md`
  - `plan/modules/M08-labor-supply-behavior.md`
  - `plan/modules/M10-pilot-evaluation-design.md`
  - `plan/modules/M14-gender-care-health.md`
- **Summary of Changes:**
  - Integrated RDL 2/2024 assistential reform and CAE phase-out into EUROMOD and `M08`. In `M01`, formalized the statutory SMI gross labor cost floor ($W_{\text{floor}} \approx \text{€}1,740/\text{mo}$ per RD 145/2024) and collective bargaining opt-outs (*descuelgues salariales*, Art. 82.3 ET).
  - In `M02`, replaced the single-parent bonus with parity-modulated child allowances ($\alpha_{\text{child1}} = 0.50$, $\alpha_{\text{child}\ge 2} = 0.35\text{--}0.40$), eliminating invasive cohabitation policing while concentrating fiscal support on single mothers and multi-child families, and anchored adulthood strictly at age 18.
  - In `M14`, specified discrete-choice collective household models (Cherchye et al. 2012) handling female non-participation, established a statutory *Garantía de No-Sustitución de Servicios Profesionales* under *Ley 39/2006* (SAAD, Costa-Font et al. 2022) to prevent care re-familialization, and ingested microdata from Spain's 34 Policy Lab RCTs (Inclusion/CEMFI/J-PAL 2024). Corrected OpenResearch (Miller et al. 2024) reporting by reframing clinical health expenditure reductions as exploratory secondary hypotheses.
  - In `M10` and `M14`, bifurcated healthcare data architecture: Tier 1 centralized INSS temporary disability (*bajas IT*) registers; Tier 2 bilateral research agreements with pilot regional health services under *Ley 16/2003* (CatSalut, SERMAS, Osakidetza) for primary care consultations and psychotropic prescription invoicing.
- **Sources Cited:** `boe-rd-145-2024-smi`, `boe-et-2015`, `rdl-2-2024-desempleo`, `cherchye-2012-collective`, `costa-font-2022-saad`, `inclusion-cemfi-jpal-2024`, `miller-2024-openresearch-health`, `ley-16-2003-sns`.
