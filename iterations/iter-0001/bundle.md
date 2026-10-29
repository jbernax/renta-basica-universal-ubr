# Research plan bundle — iter-0001

Read-only snapshot for reviewers. File boundaries are marked with `<!-- FILE: path -->`.


<!-- FILE: plan/plan.yaml -->
```yaml
version: 0.1.0
title: "Universal Basic Rent in an AI-Disrupted Labor Market: Institutional Design, Fiscal Architecture, and Multi-Level Pilot Evaluation for Spain"
central_question: >-
  How can Spain design, finance, legally anchor, and empirically pilot an unconditional Universal Basic Rent
  (Renta Básica Universal) that protects household welfare and macroeconomic stability across moderate, severe,
  and structural AI labor-displacement scenarios?
pilot_setting: Spain
pilot_levels_compared:
  - municipal
  - regional
  - national
scenarios:
  S1:
    name: Moderate AI displacement and task polarization
    horizon: "3-5 years"
    labor_share_delta_pp: -2.5
    displaced_fte_share: 0.08
    description: >-
      Generative and agentic AI automate routine administrative, customer-support, and junior cognitive tasks;
      unemployment rises moderately (+2-3 pp) while wage growth stagnates in middle-skill deciles.
  S2:
    name: Severe cognitive and service-sector displacement
    horizon: "5-10 years"
    labor_share_delta_pp: -7.0
    displaced_fte_share: 0.20
    description: >-
      Autonomous AI systems substitute broadly across professional, back-office, logistics, and retail roles;
      IRPF and Social Security payroll tax bases contract markedly and structural underemployment reaches 18-22%.
  S3:
    name: Structural compression of labor income
    horizon: "8-15 years"
    labor_share_delta_pp: -15.0
    displaced_fte_share: 0.35
    description: >-
      Capital and compute capture the majority of marginal productivity gains; traditional wage employment ceases
      to clear household subsistence for over a third of working-age adults, requiring a permanent shift from
      payroll-based welfare to capital/AI-rent-financed Universal Basic Rent.
modules:
  - M01
  - M02
  - M03
  - M04
  - M05
  - M06
  - M07
  - M08
  - M09
  - M10
  - M11
  - M12
  - M13
  - M14
  - M15
  - M16
  - M17
```


<!-- FILE: plan/00-scope.md -->
# 00 · Research Scope, Conceptual Architecture, and Scenarios

## 1. Central Research Question
**How can Spain design, finance, legally anchor, and empirically pilot an unconditional Universal Basic Rent (*Renta Básica Universal*, UBR) that safeguards household living standards and macroeconomic stability across moderate, severe, and structural AI labor-displacement scenarios?**

Rapid advances in generative and agentic artificial intelligence alter the historical relationship between productivity growth and labor demand [@acemoglu-restrepo-2019; @eloundou-2024-gpts; @cazzaniga-imf-2024]. Whereas classic industrial automation primarily displaced routine manual tasks while creating complementary clerical and professional employment, frontier AI directly targets non-routine cognitive, administrative, legal, financial, and customer-service work [@webb-2020-ai; @felten-2021-aioe; @gmyrek-ilo-2023]. In Spain—a labor market characterized by structural unemployment above the EU average, historic duality, and a welfare system heavily reliant on contributory Social Security payroll taxes—a sustained compression of the labor income share threatens both household subsistence and the fiscal viability of existing transfers [@boe-ce-1978; @boe-imv-2021].

## 2. Core Definitions and Institutional Distinctions
To ensure analytical consistency across all 17 modules (`M01`–`M17`), this research plan adopts strict operational definitions [@van-parijs-vanderborght-2017; @hoynes-rothstein-2019]:

1. **Universal Basic Rent (UBR / *Renta Básica Universal*):** An unconditional, periodic (monthly) cash transfer paid in euros on an **individual** basis to all qualifying residents, without means-testing, work requirements, or behavioral conditionalities (`D-001`). While gross UBR is paid universally ex ante, it is integrated into the Personal Income Tax (*Impuesto sobre la Renta de las Personas Físicas*, IRPF [@boe-irpf-2006]) so that high-income earners are net contributors ex post.
2. **Guaranteed Minimum Income (*Ingreso Mínimo Vital*, IMV & *Rentas Mínimas Autonómicas*):** Means-tested, household-based top-up transfers subject to ex-post income verification, complex household unit definitions, and 100% (or near-100%) phase-out rates that create severe marginal effective tax rate (METR) poverty traps and >50% non-take-up [@boe-imv-2021; @arcelus-bade-2015-rgi].
3. **Negative Income Tax (NIT):** A tax-administered transfer that is economically equivalent to a UBR + flat/progressive income tax in static net fiscal terms, but differs in disbursement timing, intra-household distribution (individual monthly liquidity vs. annual household tax filing), and administrative take-up [@saez-2002-optimal-transfers; @ghatak-maniquet-2019].

## 3. Conditional AI Labor-Displacement Scenarios (S1–S3)
Following `D-006`, the research plan avoids assuming an unquantified "end of work" and instead evaluates policy designs across three formal macroeconomic and labor-market scenarios [@acemoglu-2024-macro-ai; @korinek-suh-2024]:

| Parameter | **S1: Moderate Polarization** | **S2: Severe Displacement** | **S3: Structural Compression** |
|---|---|---|---|
| **Time Horizon** | 3–5 years | 5–10 years | 8–15 years |
| **Labor Share Shift ($\Delta s_L$)** | $-2.5$ pp of GDP | $-7.0$ pp of GDP | $-15.0$ pp of GDP |
| **Displaced FTE Share** | $8\%$ of hours worked | $20\%$ of hours worked | $35\%$ of hours worked |
| **Primary Shock Channel** | Routine clerical, translation, junior coding, customer support | Broad administrative, legal/accounting, mid-tier services, logistics | Pervasive autonomous agent substitution across cognitive & service work |
| **Fiscal Baseline Impact** | Mild IRPF/cotizaciones drag; manageable within reformed IMV + IRPF | Major erosion of payroll & middle-bracket IRPF; requires capital/IVA shift | Structural collapse of payroll tax base; requires AI-rent & wealth/capital capture |

## 4. Reference Parameter Baselines for Cross-Module Coherence
All modules calibrate against a harmonized menu of three UBR benefit tiers (expressed in 2026 euros per month, indexed to CPI/ECV thresholds):
- **Tier A (Partial / Floor UBR):** €600/month per adult (€300/month per minor $<18$), approximating the individual *Ingreso Mínimo Vital* guaranteed threshold, paired with a **No-Loser Guarantee** supplement for households whose existing contributory/disability entitlements exceed UBR (`M02`, `M07`).
- **Tier B (Poverty-Line UBR):** €900/month per adult (€360/month per minor), anchored to 60% of Spanish median equivalized disposable income (AROPE at-risk-of-poverty line from INE's *Encuesta de Condiciones de Vida*).
- **Tier C (Full AI-Dividend UBR, S3 target):** €1,200/month per adult (€420/month per minor), calibrated to structural labor-income replacement under Scenario S3.

## 5. Multi-Level Governance Comparison (`D-005`)
Every module evaluates implementation feasibility and pilot design across three Spanish territorial tiers:
- **Municipal Tier:** High-saturation urban or rural municipal pilots (building on Barcelona's B-MINCOME [@todeschini-bmincome-2020]), testing local labor, consumption, health, and housing pass-through effects without tax sovereignty.
- **Regional Tier (*Comunidades Autónomas*):** Comparing a **Common Regime** region (e.g. Catalonia's proposed pilot office, constrained by LOFCA [@boe-lofca-1980] and limited IRPF normative brackets) against a **Foral Regime** region (Basque Country or Navarre, which possess full tax-collection and IRPF/Corporate normative autonomy to test joint tax-plus-transfer UBR).
- **National Tier:** State-level constitutional and fiscal integration across AEAT, INSS, and the 17 Autonomous Communities [@boe-ce-1978].


<!-- FILE: plan/decisions.md -->
# Human-Locked Architecture & Scope Decisions (`decisions.md`)

> **Harness Lock Notice:** This file is listed in `plan.always_locked` in `harness/config.yaml`. During an open iteration, the AI improvement loop is strictly forbidden from editing this file. If a reviewer or synthesizer believes a decision here should be revisited, it must record a proposal in `iterations/iter-NNNN/proposals-for-human.md` for human review at the next checkpoint.

## D-001 · Definition of Universal Basic Rent (UBR)
- **Status:** Locked (User confirmed, 2026-10-29)
- **Decision:** In this research program, *Universal Basic Rent* corresponds to the Spanish concept of *Renta Básica Universal* (RBU) / Universal Basic Income (UBI): an unconditional, periodic, individual cash transfer paid to all qualifying residents without means-testing or work requirements. Housing and rent-capture effects are analyzed as critical economic channels (`M05`), not as an in-kind housing voucher.

## D-002 · Execution Architecture of the Improvement Harness
- **Status:** Locked (User confirmed, 2026-10-29)
- **Decision:** The improvement loop runs natively inside Antigravity using specialist subagent reviewers and an independent judge subagent, backed by deterministic Python CLI tools (`python -m ubr`) for structural validation, source verification, metric calculation, scoring, and stopping rules. No external paid LLM API keys are required.

## D-003 · Language and Target Deliverable Format
- **Status:** Locked (User confirmed, 2026-10-29)
- **Decision:** The research plan and final academic/policy paper are written in **English**, citing Spanish legal, statistical, and institutional sources in their original designations, and the final paper will include a comprehensive **Spanish executive summary** (*Resumen Ejecutivo para decisores públicos*).

## D-004 · Human-in-the-Loop Cadence
- **Status:** Locked (User confirmed, 2026-10-29)
- **Decision:** The improvement loop runs up to $N = 3$ autonomous iterations per cycle (stopping earlier on regression, plateau, or SOTA candidacy) and then halts for human review with a consolidated changelog and score-delta report (`iterations/REPORT.md`).

## D-005 · Spain Pilot Governance Level Left Open for Comparative Analysis
- **Status:** Locked (User confirmed, 2026-10-29)
- **Decision:** Rather than pre-committing to a single administrative tier, the research plan systematically compares **Municipal** (e.g. B-MINCOME follow-on), **Regional / Autonomous Community** (both *régimen común* such as Catalonia and *régimen foral* such as the Basque Country / Navarre), and **National** (State-level building on the *Ingreso Mínimo Vital* and IRPF) pilot and implementation options across every module.

## D-006 · Conditional AI Labor-Displacement Scenarios (S1–S3)
- **Status:** Locked (Default adopted at plan approval, 2026-10-29)
- **Decision:** Rather than treating complete labor-market collapse as an unexamined premise, all modules evaluate UBR across three explicit AI labor-displacement scenarios defined in `plan/plan.yaml`: **S1** (Moderate displacement & task polarization), **S2** (Severe cognitive & service displacement), and **S3** (Structural compression of labor income).


<!-- FILE: plan/methods.md -->
# Cross-Cutting Methodological Architecture (`methods.md`)

This document specifies the five core analytical pillars linking the 17 modules (`M01`–`M17`) into a closed, internally consistent research pipeline.

## 1. Task-Based AI Exposure & Labor-Share Projections (`M01`, `M08`, `M16`)
- **Occupational Mapping:** Crosswalk US O*NET task exposure indices (Eloundou et al. $\beta$-exposure [@eloundou-2024-gpts], Felten AIOE [@felten-2021-aioe], Webb patent-task overlap [@webb-2020-ai], and ILO Gen-AI scores [@gmyrek-ilo-2023]) to ISCO-08 and Spain's 3-digit *Clasificación Nacional de Ocupaciones* (CNO-11) using INE *Encuesta de Población Activa* (EPA) microdata.
- **Task Displacement vs. Reinstatement Model:** Calibrate an Acemoglu-Restrepo task-allocation framework [@acemoglu-restrepo-2019; @acemoglu-2024-macro-ai] to Spanish sectoral production functions (Contabilidad Nacional, INE) and administrative social security histories (*Muestra Continua de Vidas Laborales*, MCVL) to derive scenario paths **S1**, **S2**, and **S3** [@korinek-suh-2024; @cazzaniga-imf-2024].

## 2. Static & Behavioral Tax-Benefit Microsimulation (`M02`, `M03`, `M07`, `M09`, `M14`)
- **EUROMOD-Spain Backbone:** Implement UBR Tiers A, B, and C inside EUROMOD-Spain [@sutherland-figari-2013-euromod] running on INE's *Encuesta de Condiciones de Vida* (ECV) cross-validated with the *Instituto de Estudios Fiscales* (IEF) / AEAT *Muestra de Declarantes de IRPF* and *Panel de Hogares*.
- **Joint Tax-Transfer Schedule:** Simulate abolishing the current IRPF *mínimo personal y familiar* [@boe-irpf-2006] and replacing means-tested cash benefits (`M07`, subject to a strict **No-Loser Guarantee** for disability and high-need households) with a unified marginal rate schedule, computing exact gross vs. net fiscal cost, decile winners/losers, Gini, S80/S20, and AROPE poverty impacts.
- **Behavioral Labor-Supply Module:** Embed discrete-choice structural labor supply elasticities (intensive and extensive margins calibrated from Spanish MCVL/ECV and experimental literature [@saez-2002-optimal-transfers; @vivalt-2024-openresearch; @jones-marinescu-2022]) to compute second-round revenue and poverty effects.

## 3. Open-Economy HANK General-Equilibrium Closure (`M03`, `M04`, `M05`, `M16`, `M17`)
- **Heterogeneous-Agent New Keynesian (HANK) Model for Spain:** Build a small-open-economy monetary-union HANK model [@kaplan-moll-violante-2018-hank; @auclert-rognlie-straub-2024] calibrated to Spanish liquid/illiquid wealth distributions (Banco de España *Encuesta Financiera de las Familias*, EFF) and decile-specific marginal propensities to consume (MPCs).
- **Tradable vs. Non-Tradable & Housing Sector Split:** Separate tradable goods (Eurozone price-taking, import leakage) from non-tradable services and inelastic urban rental housing (`M05` [@fack-2006-housing-benefits; @diamond-mcquade-qian-2019-rent]) to quantify when UBR acts as a non-inflationary demand stabilizer (offsetting AI wage compression in S2/S3) versus when it triggers domestic shelter/service inflation or sovereign spread widening.

## 4. Multi-Level Experimental & Quasi-Experimental Identification (`M05`, `M08`, `M10`, `M15`)
- **Two-Stage Randomized Saturation Design:** Combine individual-level randomization (identifying partial-equilibrium labor, health, and consumption responses [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health]) with municipality/census-tract cluster saturation variation (identifying local general-equilibrium rent pass-through, wage bargaining, and consumption multipliers [@egger-2022-ge-kenya; @todeschini-bmincome-2020]).
- **Simulated Net-Tax Arm in Foral / Regional Pilots:** Where regional fiscal competence allows (e.g. Basque Country / Navarre or State-delegated IRPF pilot), test both net-recipient and tax-clawback arms to overcome the classic pilot flaw of testing unfinanced transfers [@hoynes-rothstein-2019; @kangas-2021-finland].

## 5. Constitutional, Statutory, and Political-Economy Veto Analysis (`M06`, `M11`, `M12`, `M13`)
- **Doctrinal & Competence Stress-Test:** Map every statutory reform required across the Spanish Constitution [@boe-ce-1978], LOFCA [@boe-lofca-1980], Ley del IRPF [@boe-irpf-2006], Ley del IMV [@boe-imv-2021], and EU Regulation 883/2004 [@eu-reg-883-2004].
- **Conjoint Survey & Coalition Modeling:** Pair CIS public-opinion microdata with a pre-registered conjoint survey experiment testing multidimensional UBR packages (benefit level, tax source, residency rule, AI-dividend framing) across Spanish partisan and territorial cleavages.


<!-- FILE: plan/modules/M01-ai-labor-displacement.md -->
---
id: M01
title: AI labor displacement and macroeconomic scenarios
status: draft
locked: false
depends_on: [M08, M16]
covers: [F01]
feeds_chapters: [1, 2]
last_iteration: 0
---
# M01 · AI labor displacement and macroeconomic scenarios

## 1. Why this matters
The case for a Universal Basic Rent in Spain rests on whether generative and agentic AI produce a qualitatively different labor shock than previous automation waves [@acemoglu-restrepo-2019; @eloundou-2024-gpts]. If AI substitution outpaces task reinstatement across clerical, professional, and service occupations, Spain faces simultaneous compression of household wage income and erosion of the IRPF and Social Security payroll tax bases (`M03`, `M16`).

## 2. Research questions
- **RQ-M01-01**: What share of Spanish full-time equivalent (FTE) employment and aggregate wage bill in 3-digit CNO-11 occupations is exposed to direct substitution versus complementarity under AI scenarios S1, S2, and S3?
  - *Hypothesis:* At least 28% of Spanish FTE employment and 34% of the gross wage bill reside in high-exposure cognitive and administrative clusters where agentic substitution dominates complementarity under S2 and S3.
- **RQ-M01-02**: How does task-level AI displacement translate into net payroll tax (*cotizaciones sociales*) and IRPF revenue elasticity across Spanish autonomous communities?
  - *Hypothesis:* Each 1 percentage-point AI-induced drop in the labor income share reduces combined Spanish IRPF and Social Security revenues by 1.25–1.40 percentage points under the current tax schedule, with the steepest revenue drag in service-intensive urban regions (Madrid, Catalonia).

## 3. State of knowledge
Task-based frameworks show that automation depresses the labor share whenever displacement effects exceed productivity and new-task reinstatement effects [@acemoglu-restrepo-2019; @acemoglu-2024-macro-ai]. Empirical indices of LLM and AI exposure [@eloundou-2024-gpts; @felten-2021-aioe; @webb-2020-ai] and cross-country assessments by the IMF and ILO [@cazzaniga-imf-2024; @gmyrek-ilo-2023] indicate that advanced economies face higher gross exposure than emerging markets, with clerical, financial, legal, and customer-service workers particularly vulnerable to displacement, while transition models to AGI demonstrate sharp wage compression once cognitive tasks are automated [@korinek-suh-2024].

## 4. Spain context & data sources
Spain enters the AI transition with structural unemployment near 11%, youth unemployment above 25%, and a dual labor market only partially mitigated by the 2021 labor reform. Primary datasets include:
- INE *Encuesta de Población Activa* (EPA) quarterly microdata (occupational structure at 3-digit CNO-11, hours, tenure).
- *Muestra Continua de Vidas Laborales* (MCVL, Seguridad Social) linked to tax records for longitudinal wage and contribution trajectories.
- INE *Encuesta Anual de Estructura Salarial* (EAES) and *Encuesta sobre el uso de TIC y comercio electrónico en las empresas* (firm-level AI adoption).

## 5. Methods & identification
1. **Crosswalk & Exposure Scoring:** Map O*NET task exposure scores [@eloundou-2024-gpts; @felten-2021-aioe; @webb-2020-ai] to ISCO-08 and Spanish CNO-11 using European Skills/Competences (ESCO) weights.
2. **Shift-Share & Event-Study Identification:** Estimate causal displacement elasticities in MCVL/EPA using pre-shock occupational exposure interacted with sectoral AI compute/software investment shocks (shift-share IV), controlling for firm and worker fixed effects.
3. **Scenario Calibration (S1–S3):** Feed estimated task-substitution elasticities into an Acemoglu-Restrepo sectoral model to generate quarterly paths of displaced FTEs, wage deciles, and payroll tax erosion for `M03` and `M04`.

## 6. Pilot implications
- **Municipal:** Select pilot municipalities spanning high service/back-office exposure (e.g. metropolitan Barcelona/Madrid suburbs) and manufacturing/agricultural baselines.
- **Regional:** Stratify Autonomous Community comparisons by CNO-11 cognitive exposure share.
- **National:** Define macroeconomic indicators (quarterly EPA cognitive-displacement index and Social Security contribution-to-GDP ratio) that automatically trigger transitions from S1 to S2/S3 policy tiers (`M17`).

## 7. Risks, counterarguments & open issues
- **Counterargument (Aggregate Productivity Modesty):** Acemoglu [@acemoglu-2024-macro-ai] argues five-year TFP gains from AI may be modest (~0.7%), implying slow displacement. *Mitigation:* Explicitly bracket S1 (slow/moderate, consistent with Acemoglu) against S2 and S3 [@korinek-suh-2024] rather than assuming immediate collapse.
- **Occupational Reclassification Noise:** CNO-11 codes may mask within-occupation task reorganization.

## 8. Deliverables & effort
- CNO-11 AI Exposure & Wage-Bill Dataset for Spain (R/Python pipeline on EPA + EAES).
- Chapter 2 empirical tables and S1–S3 scenario input vectors for EUROMOD (`M03`, `M09`) and HANK (`M04`). (Effort: 6 person-weeks).


<!-- FILE: plan/modules/M02-benefit-design.md -->
---
id: M02
title: Benefit design, eligibility, and parameter architecture
status: draft
locked: false
depends_on: [M03, M07, M09]
covers: [F02]
feeds_chapters: [3]
last_iteration: 0
---
# M02 · Benefit design, eligibility, and parameter architecture

## 1. Why this matters
Small changes in benefit architecture—individual versus household unit, adult versus minor amounts, age thresholds, and indexation rules—determine whether UBR eliminates poverty and intra-household dependency or becomes fiscally unviable [@van-parijs-vanderborght-2017; @hoynes-rothstein-2019]. In Spain, where the *Ingreso Mínimo Vital* (IMV) suffers from complex household-unit assessments and >50% non-take-up [@boe-imv-2021], parameter simplicity is essential.

## 2. Research questions
- **RQ-M02-01**: How do purely individual UBR schedules (Tiers A: €600, B: €900, C: €1,200 per adult; €300/€360/€420 per minor) compare against OECD-equivalized household schedules in reducing severe material and social deprivation in Spain per net euro spent?
  - *Hypothesis:* An individual UBR at Tier B (€900/adult, €360/minor) paired with a single-adult housing/vulnerability supplement achieves lower child and female poverty per net fiscal euro than household-equivalized schedules while eliminating cohabitation penalties.
- **RQ-M02-02**: What indexation formula (headline CPI vs. essential-basket CPI vs. median equivalized income) best preserves real poverty reduction across S1–S3 without triggering automatic wage-price spirals in `M04`?
  - *Hypothesis:* Indexing UBR to a dual anchor—essential consumption basket CPI capped by nominal GDP-per-capita growth—preserves real subsistence floors while acting as an automatic macroeconomic stabilizer.

## 3. State of knowledge
Theoretical public economics demonstrates that unconditional individual transfers avoid the high marginal effective tax rates (METRs) and monitoring costs of means-tested programs, at the cost of higher gross fiscal outlays that must be recouped through the income tax schedule [@ghatak-maniquet-2019; @saez-2002-optimal-transfers; @van-parijs-vanderborght-2017]. Empirical evidence from Spanish minimum income schemes shows that household-level means testing penalizes household formation, delays emancipated youth transitions, and creates administrative bottlenecks [@arcelus-bade-2015-rgi; @todeschini-bmincome-2020].

## 4. Spain context & data sources
- **Poverty & Living Standards Benchmarks:** INE *Encuesta de Condiciones de Vida* (ECV) AROPE thresholds (60% and 40% of median equivalized disposable income across Spain and by Autonomous Community).
- **IMV Statutory Baseline:** *Ley 19/2021* [@boe-imv-2021] guaranteed amounts, *Complemento de Ayuda para la Infancia* (CAPI), and disability supplements.
- **Demographics:** INE *Censo de Población* and *Padrón Continuo* (adult/minor age cohorts, household size distributions).

## 5. Methods & identification
1. **Parametric Dominance Grid in EUROMOD-Spain:** Simulate a $3 \times 3 \times 2$ design grid (Tiers A/B/C $\times$ child weight $\{0.3, 0.4, 0.5\}$ $\times$ youth emancipating age $\{18, 23\}$) in EUROMOD [@sutherland-figari-2013-euromod].
2. **Equivalence Scale Sensitivity:** Evaluate poverty gaps (FGT indices $P_0, P_1, P_2$) under both the modified OECD scale ($1.0 / 0.5 / 0.3$) and single-person urban rent-adjusted budgets.

## 6. Pilot implications
- **Municipal:** Test Tier A vs. Tier B individual payments against B-MINCOME's household-conditioned modalities [@todeschini-bmincome-2020].
- **Regional:** Compare uniform nominal regional amounts against cost-of-living top-ups.
- **National:** Phase from Tier A (€600, S1) to Tier B (€900, S2) and Tier C (€1,200, S3).

## 7. Risks, counterarguments & open issues
- **Counterargument (Single-Adult Adequacy vs. Multi-Adult Windfall):** Purely individual transfers ignore household economies of scale in housing, potentially under-protecting single adults living alone while over-subsidizing multi-adult households. *Mitigation:* Test pairing individual UBR with the `M07` No-Loser Guarantee and `M05` social rental policies.

## 8. Deliverables & effort
- Parameter Specification Matrix & EUROMOD input rulefiles for Tiers A, B, and C.
- Adequacy vs. Net Cost Pareto frontier curves for Chapter 3. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M03-fiscal-financing.md -->
---
id: M03
title: Fiscal financing and tax-transfer integration
status: draft
locked: false
depends_on: [M01, M02, M07, M09, M16]
covers: [F03]
feeds_chapters: [4]
last_iteration: 0
---
# M03 · Fiscal financing and tax-transfer integration

## 1. Why this matters
Gross cost is the most frequent critique of UBR in Spain: paying €900/month to ~40 million adults and €360/month to ~8 million minors implies a gross outlay near €466 billion (~30% of Spanish GDP). However, economic feasibility depends on **net redistributive transfer**—the amount moved from net contributors to net recipients after integrating UBR with IRPF [@boe-irpf-2006], folding redundant cash benefits (`M07`), and reforming consumption and capital taxes [@hoynes-rothstein-2019; @saez-2002-optimal-transfers].

## 2. Research questions
- **RQ-M03-01**: What is the static and behavioral net fiscal cost of UBR Tiers A, B, and C in Spain once the IRPF *mínimo personal y familiar* and replaced cash transfers are integrated into a unified progressive tax schedule?
  - *Hypothesis:* Integrating Tier B (€900/month) into IRPF reduces the net financing requirement from ~30% of GDP (gross) to 4.5–5.8% of GDP (net), with the zero-net-transfer breakeven occurring between the 65th and 72nd percentile of individual gross income.
- **RQ-M03-02**: As AI displacement erodes labor income under scenarios S2 and S3 (`M01`), what combination of IRPF dual-base unification (taxing *renta del ahorro* at progressive *renta general* rates), IVA base broadening, and `M16` AI/capital levies closes the fiscal gap with minimal efficiency loss?
  - *Hypothesis:* Unifying IRPF savings and general tax bases plus reclassifying super-reduced/reduced IVA exemptions (compensated ex ante by UBR for lower deciles) finances Tier A/B under S1–S2, while S3 requires at least 3.0% of GDP from `M16` capital/AI-rent taxes.

## 3. State of knowledge
Public finance theory establishes that a universal demogrant financed by a linear or progressive income tax is fiscally equivalent to a Negative Income Tax of equal net transfer schedule [@saez-2002-optimal-transfers; @ghatak-maniquet-2019]. Microsimulation studies using EUROMOD [@sutherland-figari-2013-euromod] show that gross-cost estimates overstate fiscal burden by a factor of 4 to 6 because they count self-financed tax clawbacks on middle and upper deciles as new net expenditure [@hoynes-rothstein-2019; @van-parijs-vanderborght-2017].

## 4. Spain context & data sources
- **Tax Law & Bases:** *Ley 35/2006 del IRPF* [@boe-irpf-2006] (general vs. savings base, *mínimos personales y familiares*, autonomous vs. state brackets) and *LOFCA* [@boe-lofca-1980].
- **Microdata:** IEF/AEAT *Muestra de Declarantes de IRPF* (>2.5 million tax records), *Panel de Hogares* (linked AEAT + INE + Catastro), and INE *Encuesta de Presupuestos Familiares* (EPF, for IVA incidence by decile).

## 5. Methods & identification
1. **Joint IRPF-UBR Microsimulation:** In EUROMOD-Spain + IEF IRPF Muestra, abolish current IRPF personal/family allowances, make UBR non-taxable but tax all other earned and capital income from the first euro at calibrated marginal schedules ($t \in [38\%, 52\%]$).
2. **Consumption Tax Incidence (EPF-EUROMOD Link):** Match EPF expenditure shares to ECV households to simulate eliminating regressive IVA tax expenditures whose distributional purpose is superseded by UBR.
3. **Dynamic S1–S3 Stress Test:** Apply `M01` wage-bill compression vectors to project IRPF and Social Security revenue loss and solve for revenue-neutral tax rates.

## 6. Pilot implications
- **Municipal:** Cannot test tax financing (municipalities only control IBI/local fees).
- **Regional:** A *régimen foral* pilot (Basque Country / Navarre) can legally enact the exact IRPF withholding schedule to test net-taxpayer behavioral responses; a *régimen común* pilot can only adjust the 50% regional IRPF tariff or simulate clawbacks contractually.
- **National:** Full AEAT monthly withholding (*retenciones*) + UBR clearing.

## 7. Risks, counterarguments & open issues
- **Counterargument (High Marginal Tax Rates & Tax Evasion):** Marginal IRPF rates near 45–50% from the first euro of earned income could depress formal labor supply or increase underground activity (*economía sumergida*). *Mitigation:* Estimate taxable income elasticities (ETI) on Spanish IRPF bunching points and shift financing toward consumption (IVA) and AI/capital rents (`M16`).

## 8. Deliverables & effort
- Full Gross-to-Net Fiscal Bridge Table (Tiers A/B/C $\times$ Scenarios S1/S2/S3).
- Statutory IRPF Tariff Reform Schedule & Revenue Decomposition for Chapter 4. (Effort: 8 person-weeks).


<!-- FILE: plan/modules/M04-macroeconomics-eurozone.md -->
---
id: M04
title: Macroeconomic dynamics, inflation, and Eurozone constraints
status: draft
locked: false
depends_on: [M01, M03, M05, M16]
covers: [F05]
feeds_chapters: [5]
last_iteration: 0
---
# M04 · Macroeconomic dynamics, inflation, and Eurozone constraints

## 1. Why this matters
Spain is a medium-sized open economy inside the Eurozone: it cannot devalue its currency or instruct the Banco de España to monetize fiscal deficits, and it is bound by the EU's reformed fiscal governance framework (Debt Sustainability Analysis and net primary expenditure ceilings). A state-of-the-art plan must prove that UBR stabilizes aggregate demand during an AI-driven wage contraction without igniting non-tradable inflation, current-account deficits, or sovereign debt crises [@kaplan-moll-violante-2018-hank; @auclert-rognlie-straub-2024].

## 2. Research questions
- **RQ-M04-01**: In a small-open-economy HANK model calibrated to Spain, under what combinations of AI productivity growth (`M01`) and tax financing (`M03`, `M16`) is UBR non-inflationary in the non-tradable sector?
  - *Hypothesis:* When UBR is 100% tax-financed (zero primary deficit increase) under S1 and S2, the demand boost from redistributing toward high-MPC bottom deciles (+0.8 to +1.4% GDP) is offset by AI-driven marginal cost reductions in services, keeping core non-tradable inflation within $\pm 0.3$ pp of the ECB target—except in supply-inelastic urban housing (`M05`).
- **RQ-M04-02**: How do EU fiscal rules (structural primary balance and net expenditure path) constrain transitional deficit financing during the S2/S3 rollout, and what domestic fiscal multipliers justify a structural reform clause?
  - *Hypothesis:* Deficit-financed UBR violates EU DSA debt-reduction paths within 2 years and widens the Bonos-Bund spread by >80 bps; therefore, statutory revenue-neutrality (`M03` + `M16`) is a binding macroeconomic constraint for Spain.

## 3. State of knowledge
Heterogeneous-Agent New Keynesian (HANK) models show that redistributive transfers from low-MPC savers to high-MPC hand-to-mouth households generate positive balanced-budget multipliers [@kaplan-moll-violante-2018-hank; @auclert-rognlie-straub-2024]. Meanwhile, macroeconomic models of AI indicate that automation acts as a positive supply shock that raises capital income shares while potentially depressing wage-driven aggregate demand [@acemoglu-2024-macro-ai; @korinek-suh-2024]. Experimental general-equilibrium evidence from high-saturation transfers confirms strong local output multipliers with minimal goods-price inflation when supply is elastic [@egger-2022-ge-kenya].

## 4. Spain context & data sources
- **Household Balance Sheets & MPCs:** Banco de España *Encuesta Financiera de las Familias* (EFF) for liquid vs. illiquid wealth distributions and hand-to-mouth household shares.
- **Macro & External Accounts:** INE *Contabilidad Nacional Trimestral*, input-output tables (import content of consumption by COICOP category), and AIReF / Banco de España fiscal sustainability projections.

## 5. Methods & identification
1. **Two-Sector Open-Economy HANK Model:** Calibrate a Spanish monetary-union HANK model with tradable (Eurozone price-taking) and non-tradable sectors, matching EFF liquid wealth deciles and EPF consumption baskets.
2. **AI Supply + Redistribution Counterfactuals:** Simulate joint shocks: (i) AI TFP + labor-share compression (S1–S3) without UBR vs. (ii) AI shock + tax-financed UBR Tiers A/B/C.
3. **EU DSA Compliance Check:** Embed the HANK output, inflation, and revenue paths into the European Commission's deterministic Debt Sustainability Analysis (DSA) equations.

## 6. Pilot implications
- **Municipal / Regional:** High-saturation municipal pilots (`M10`) allow empirical estimation of local non-tradable price responses and consumption multipliers, though regional trade leakage is much higher than national import leakage.
- **National:** Macro-level CPI and sovereign spread circuit-breakers (`M17`) govern Tier transitions.

## 7. Risks, counterarguments & open issues
- **Counterargument (Import Leakage to Foreign Tech/Goods):** Bottom-decile consumption of tradables and digital subscriptions could leak abroad, worsening Spain's trade balance. *Mitigation:* Quantify COICOP-level import propensities from INE Input-Output tables.

## 8. Deliverables & effort
- Calibrated Spanish Open-Economy HANK Model codebase & impulse-response functions (S1–S3).
- EU Fiscal Framework & DSA compliance memo for Chapter 5. (Effort: 7 person-weeks).


<!-- FILE: plan/modules/M05-housing-rent-capture.md -->
---
id: M05
title: Housing market pass-through and landlord rent capture
status: draft
locked: false
depends_on: [M02, M04, M10, M13]
covers: [F06]
feeds_chapters: [5]
last_iteration: 0
---
# M05 · Housing market pass-through and landlord rent capture

## 1. Why this matters
Housing is the single largest threat to the real welfare impact of a cash UBR in Spain. In metropolitan areas with rigid housing supply and high tourist/seasonal rental pressure (Madrid, Barcelona, Málaga, Balearic and Canary Islands), an unconditional increase in tenant disposable income risks being partially captured by landlords through higher rents [@fack-2006-housing-benefits], converting a public transfer into private land rent.

## 2. Research questions
- **RQ-M05-01**: What fraction of an unconditional cash transfer (Tiers A/B) is capitalized into higher private market rents across Spanish municipalities with low versus high housing supply elasticity?
  - *Hypothesis:* In supply-inelastic stressed urban zones (*zonas de mercado residencial tensionado*) without complementary supply or rent-cap enforcement, 22–35% of the marginal income gain for bottom-decile private renters is captured by rent increases within 24 months, compared to <5% in elastic rural and mid-sized municipalities.
- **RQ-M05-02**: Which complementary housing policy package—reference rent caps under *Ley 12/2023* [@boe-vivienda-2023], rapid expansion of public social rental stock (*parque público*), or vacant-property/land-value surcharges in IBI/IRPF—most effectively suppresses rent pass-through without freezing tenant mobility?
  - *Hypothesis:* Combining UBR with automatic rural/mid-sized residential mobility portability (`M13`), vacant-unit tax surcharges, and public rental stock expansion outperforms standalone rent caps, which reduce pass-through for incumbents but shrink available rental listings [@diamond-mcquade-qian-2019-rent].

## 3. State of knowledge
Empirical evaluations of housing allowances and cash transfers demonstrate substantial incidence on rents when low-quality rental supply is inelastic: Fack [@fack-2006-housing-benefits] finds that 50–78% of French housing benefit increases were absorbed by higher rents. Conversely, rent control studies [@diamond-mcquade-qian-2019-rent] show strong protection for incumbent tenants alongside supply withdrawal via owner-occupancy or short-term conversions. Unconditional cash transfer RCTs show that liquidity enables residential moves toward opportunity or lower-cost areas [@bartik-2024-openresearch].

## 4. Spain context & data sources
- **Legal Framework:** *Ley 12/2023, por el derecho a la vivienda* [@boe-vivienda-2023] (*zonas tensionadas*, state rent reference index *SERPAVI*).
- **Datasets:** INE *Índice de Precios de la Vivienda en Alquiler* (IPVA), Ministry of Housing (MIVAU) *Sistema Estatal de Referencia del Precio del Alquiler de Vivienda*, AEAT IRPF real-estate return declarations, Dirección General del Catastro, and Idealista/Fotocasa municipal listing panels.

## 5. Methods & identification
1. **Historical Pass-Through Identification:** Estimate local rental pass-through elasticities in Spain using spatial variation in IMV/CAPI rollouts [@boe-imv-2021] and regional minimum incomes interacted with municipal topographic and regulatory supply constraints (Saiz-style elasticity proxy from Catastro + municipal urban plans).
2. **Spatial Equilibrium Simulation:** Link `M05` rental supply elasticities with `M13` internal migration choices to model equilibrium rent paths in Madrid/Barcelona vs. *España vaciada*.

## 6. Pilot implications
- **Municipal:** High-saturation census tracts in `M10` must track matched landlord-tenant contract registries (*fianzas de alquiler* deposited in INCASÒL / IVIMA) to measure real-time rent pass-through against control tracts.
- **Regional:** Compare pass-through in regions applying *Ley 12/2023* stressed-zone caps (Catalonia) versus non-applying regions.
- **National:** Pair national UBR rollout with a statutory social-housing co-investment rule.

## 7. Risks, counterarguments & open issues
- **Counterargument (UBR Fuels Urban Rent Inflation):** Critics argue in-kind housing provision should precede cash UBR. *Mitigation:* Quantify the exact pass-through threshold and test whether portable UBR reduces metropolitan crowding by making lower-cost municipalities economically viable (`M13`).

## 8. Deliverables & effort
- Municipal Rental Supply Elasticity & Pass-Through Risk Map for Spain.
- Housing Policy Complementarity Simulation for Chapter 5. (Effort: 5 person-weeks).


<!-- FILE: plan/modules/M06-constitutional-eu-law.md -->
---
id: M06
title: Constitutional, competence, and EU legal architecture
status: draft
locked: false
depends_on: [M03, M07, M12, M13]
covers: [F07]
feeds_chapters: [6]
last_iteration: 0
---
# M06 · Constitutional, competence, and EU legal architecture

## 1. Why this matters
Any Spanish UBR proposal will face immediate constitutional challenges before the *Tribunal Constitucional* (TC) over the distribution of powers between the State and the 17 *Comunidades Autónomas*, as well as scrutiny under European Union free-movement and social-security coordination law [@boe-ce-1978; @eu-reg-883-2004]. Furthermore, Spain's asymmetric fiscal federalism—split between the *régimen común* (LOFCA [@boe-lofca-1980]) and the *régimen foral* (Basque *Concierto Económico* and Navarre *Convenio*)—requires distinct statutory instruments.

## 2. Research questions
- **RQ-M06-01**: Can a national UBR be enacted in Spain via ordinary State legislation (*Ley Ordinaria* + *Ley Orgánica* modifying LOFCA) anchored in Articles 149.1.1, 149.1.14, 149.1.17, and 41 of the Spanish Constitution without requiring constitutional reform?
  - *Hypothesis:* Yes—structuring UBR as a dual instrument combining a refundable individual IRPF credit (State competence over *Hacienda general*, Art. 149.1.14 CE [@boe-ce-1978]) with a non-contributory Social Security floor (Arts. 41 and 149.1.17 CE, backed by TC doctrine on IMV) is fully constitutional without amending the 1978 Constitution, provided LOFCA [@boe-lofca-1980] and the Foral Treaties are coordinated.
- **RQ-M06-02**: Under EU Regulation 883/2004 [@eu-reg-883-2004] and Directive 2004/38/EC, what legal classification and continuous-residency requirement prevent mandatory cross-border exportability of UBR while complying with EU non-discrimination principles?
  - *Hypothesis:* Classifying UBR as an integrated direct-tax refundable credit and/or a listed Annex X "special non-contributory cash benefit" conditioned on habitual, lawful residence in Spain (e.g. 24–36 months of continuous registration for economically inactive EU/third-country nationals, subject to CJEU proportionality standards) prevents exportability abroad.

## 3. State of knowledge
Spanish constitutional scholarship and *Tribunal Constitucional* rulings on the *Ingreso Mínimo Vital* [@boe-imv-2021] confirm that while Autonomous Communities hold exclusive competence over regional *asistencia social* (Art. 148.1.20 CE), the State holds exclusive competence to guarantee basic equality in constitutional rights (Art. 149.1.1 CE), basic legislation and economic regime of Social Security (Art. 149.1.17 CE), and general taxation (Art. 149.1.14 CE) [@boe-ce-1978; @arcelus-bade-2015-rgi]. At the EU level, Regulation 883/2004 [@eu-reg-883-2004] distinguishes exportable contributory benefits from non-exportable special non-contributory cash benefits and pure social assistance.

## 4. Spain context & data sources
- **Primary Legal Sources:** *Constitución Española* (Arts. 9.2, 14, 31, 41, 148.1.20, 149.1.1, 149.1.14, 149.1.17, Disposición Adicional Primera [@boe-ce-1978]), *LOFCA* [@boe-lofca-1980], *Ley 35/2006 del IRPF* [@boe-irpf-2006], *Ley 19/2021 del IMV* [@boe-imv-2021], and EU Regulation 883/2004 [@eu-reg-883-2004].
- **Case Law:** *Tribunal Constitucional* rulings on IMV management transfers (STC 19/2022, STC 62/2022) and CJEU jurisprudence (*Dano*, *Alimanovic*, *Commission v UK*).

## 5. Methods & identification
1. **Doctrinal & Competence Mapping:** Construct a legal compatibility matrix across the three territorial levels (Municipal *Ley de Bases del Régimen Local*, Regional *Estatutos de Autonomía* + LOFCA/Foral, and State).
2. **Draft Statutory Architecture (*Anteproyecto de Ley* Blueprint):** Specify the exact articles of *Ley 35/2006* (IRPF), *Texto Refundido de la Ley General de la Seguridad Social* (TRLGSS), and *LOFCA* requiring amendment.

## 6. Pilot implications
- **Municipal:** Legal basis rests on Art. 25.2.e of *Ley 7/1985 Reguladora de las Bases del Régimen Local* (limited to municipal social emergencies; requires State IRPF exemption so pilot transfers do not trigger clawbacks of existing IMV/benefits).
- **Regional:** *Régimen común* pilots require an explicit IRPF exemption in the State *Ley de Presupuestos Generales del Estado*; *régimen foral* pilots (Basque *Diputaciones Forales* / Navarre) can legislate both the transfer and the IRPF tariff autonomously.
- **National:** State *Ley Ordinaria* + *Comisión Mixta del Concierto Económico* agreement.

## 7. Risks, counterarguments & open issues
- **Counterargument (Foral Asymmetry & Cupo Disputes):** Integrating UBR into IRPF alters the tax weight of the Basque *Cupo* and Navarre *Aportación*. *Mitigation:* Draft an explicit adjustment formula for the *Concierto Económico* clearing mechanism.

## 8. Deliverables & effort
- Constitutional & EU Law Compatibility Matrix across Municipal, Regional (Común vs. Foral), and National tiers.
- Statutory Reform Blueprint for Chapter 6. (Effort: 5 person-weeks).


<!-- FILE: plan/modules/M07-welfare-benefit-integration.md -->
---
id: M07
title: Interaction with existing Spanish welfare benefits
status: draft
locked: false
depends_on: [M02, M03, M06, M09, M14]
covers: [F08]
feeds_chapters: [3]
last_iteration: 0
---
# M07 · Interaction with existing Spanish welfare benefits

## 1. Why this matters
Spain operates a fragmented patchwork of contributory and non-contributory cash benefits: the state *Ingreso Mínimo Vital* (IMV [@boe-imv-2021]), 17 distinct *Rentas Mínimas Autonómicas* (such as the Basque *RGI* and Catalan *RGC* [@arcelus-bade-2015-rgi]), SEPE unemployment insurance (*prestación contributiva*) and assistance (*subsidios por desempleo*), non-contributory retirement and disability pensions (*PNC*), and *Ley de Dependencia* care allowances. Naively abolishing all cash benefits to fund UBR would impoverish pensioners, disabled persons, and high-entitlement unemployed workers; conversely, stacking UBR on top of all existing benefits without integration inflates net fiscal cost (`M03`).

## 2. Research questions
- **RQ-M07-01**: Which Spanish non-contributory and contributory cash transfers can be fully absorbed into UBR Tiers A, B, and C, and which require preservation as top-up supplements under a strict **No-Loser Guarantee** (zero disposable-income loss for any bottom-50% or vulnerable household)?
  - *Hypothesis:* Under Tier B (€900/adult, €360/minor), 100% of IMV, CAPI, non-contributory pensions (*PNC*), and SEPE unemployment *subsidios* are absorbed with positive net gains for recipients, whereas contributory pensions, contributory unemployment insurance above €900/month, severe disability supplements, and high-tier regional schemes (e.g. Basque *RGI* single-parent housing top-ups) require a statutory **Complemento de Garantía de Derechos Adquiridos** costing <0.6% of GDP.
- **RQ-M07-02**: How does replacing means-tested IMV and SEPE *subsidios* with an unconditional UBR floor change the distribution of Marginal Effective Tax Rates (METRs) when transitioning from unemployment or informal work into formal part-time and full-time jobs?
  - *Hypothesis:* Replacing means-tested phase-outs with IRPF-integrated UBR lowers the average participation tax rate (PTR) for current IMV/subsidio beneficiaries from 78–100% to 38–46%, eliminating the formal-employment poverty trap.

## 3. State of knowledge
Evaluations of Spanish minimum income architecture highlight severe horizontal inequities across Autonomous Communities, overlapping administrative checks between INSS, SEPE, and regional social services, and welfare traps caused by abrupt benefit withdrawal upon formal job entry [@arcelus-bade-2015-rgi; @todeschini-bmincome-2020]. International basic income experiments (Finland [@kangas-2021-finland] and B-MINCOME [@todeschini-bmincome-2020]) confirm that removing bureaucratic clawbacks when taking temporary or part-time work increases formal employment stability and self-reported autonomy.

## 4. Spain context & data sources
- **Benefit Inventory & Budgets:** Ministerio de Inclusión, Seguridad Social y Migraciones (INSS statistical yearbook on IMV, PNC, and contributory pensions), SEPE unemployment benefit micro-statistics, and Ministry of Social Rights *Informe de Rentas Mínimas de Inserción* across all 17 Autonomous Communities.
- **Microsimulation Data:** EUROMOD-Spain policy spine + ECV + MCVL.

## 5. Methods & identification
1. **Benefit-by-Benefit Replacement Taxonomy:** Classify all Spanish cash transfers into three legal/fiscal categories: (i) *Fully Absorbed* (IMV, CAPI, PNC, child allowances, SEPE *subsidios*), (ii) *Floored & Topped Up* (contributory pensions and contributory unemployment insurance: UBR forms the €600/€900/€1,200 base and the contributory system pays $\max(0, B_{\text{contrib}} - \text{UBR})$), and (iii) *Strictly Additive* (disability/dependency extra-cost allowances under *Ley 39/2006* and *grado III* invalidity).
2. **No-Loser Microsimulation Audit:** Run a cell-by-cell audit in EUROMOD-Spain to verify that zero households in deciles 1–5 with disability, single-parent, or pensioner status suffer a net disposable income drop.

## 6. Pilot implications
- **Municipal / Regional:** Pilot participants must receive a statutory safe-harbor waiver (*exención de cómputo de rentas*) from INSS, SEPE, and the Autonomous Community so that receiving pilot UBR never causes permanent forfeiture of pre-existing IMV, RGI/RGC, or disability entitlements when the pilot ends.
- **National:** Automated INSS-SEPE-AEAT benefit-offset clearing (`M12`).

## 7. Risks, counterarguments & open issues
- **Counterargument (Erosion of Contributory Bismarckian Legitimacy):** Trade unions may object if UBR replaces the bottom €900 of contributory pensions, reducing the perceived return to Social Security contributions. *Mitigation:* Preserve a positive contributory slope above the UBR floor so every contributed euro still raises total retirement income.

## 8. Deliverables & effort
- Complete Spanish Cash-Benefit Integration & Savings Schedule (by program and Autonomous Community).
- METR & Participation Tax Rate distributions (Baseline vs. Tiers A/B/C) for Chapter 3. (Effort: 5 person-weeks).


<!-- FILE: plan/modules/M08-labor-supply-behavior.md -->
---
id: M08
title: Labor supply, reservation wages, and behavioral responses
status: draft
locked: false
depends_on: [M01, M02, M03, M07, M10]
covers: [F09]
feeds_chapters: [2, 7]
last_iteration: 0
---
# M08 · Labor supply, reservation wages, and behavioral responses

## 1. Why this matters
A central objection to UBR is that an unconditional income floor will induce large reductions in labor supply, exacerbating fiscal pressures (`M03`). Conversely, in an AI-disrupted labor market (`M01`) with pervasive Spanish informality and welfare traps (`M07`), UBR may raise formal participation among welfare recipients, strengthen worker reservation wages against exploitative precarious contracts, and finance human-capital reallocation, caregiving (`M14`), and entrepreneurship [@hoynes-rothstein-2019; @vivalt-2024-openresearch].

## 2. Research questions
- **RQ-M08-01**: What are the extensive-margin (participation) and intensive-margin (hours worked) elasticities of Spanish workers by gender, age, household structure, and CNO-11 AI-exposure tier when moving from means-tested transfers (IMV/subsidios) to an IRPF-integrated UBR?
  - *Hypothesis:* Aggregate hours worked decline by less than 1.5–2.5% under Tier B, concentrated in voluntary reductions of overtime by secondary earners with young children and youth extending education, while formal extensive-margin participation among former IMV/informal workers *increases* by 3–5 percentage points due to eliminating the 100% benefit clawback.
- **RQ-M08-02**: Under AI displacement scenarios S1–S3, does UBR shorten or lengthen unemployment spells, and does it improve post-displacement occupational match quality (wage and skill upgrading via retraining and self-employment)?
  - *Hypothesis:* Unconditional liquidity increases post-displacement search duration by 3–6 weeks on average, but yields a 6–10% higher re-employment wage stability and higher survival of solo self-employment (*autónomos*) compared to liquidity-constrained displaced workers.

## 3. State of knowledge
Recent high-powered RCTs and natural experiments show small extensive-margin employment reductions from unconditional transfers: in the US OpenResearch RCT ($1,000/month for 3 years), Vivalt et al. [@vivalt-2024-openresearch] find a 1.3 hour/week reduction and a 2 pp participation effect driven by selectivity in job search and leisure, with higher educational enrollment among younger adults. In Alaska's permanent universal dividend, Jones & Marinescu [@jones-marinescu-2022] find zero aggregate employment decline because positive local demand multipliers offset individual income effects. In Finland [@kangas-2021-finland], replacing conditional unemployment benefits with an unconditional basic income increased employment days slightly once bureaucratic disincentives were removed.

## 4. Spain context & data sources
- **Labor & Longitudinal Data:** INE *Encuesta de Población Activa* (EPA longitudinal rotating panel), *Muestra Continua de Vidas Laborales* (MCVL matched with AEAT tax withholdings), and INE *Encuesta de Empleo del Tiempo* (EET).
- **Informality & Self-Employment:** RETA (*Régimen Especial de Trabajadores Autónomos*) survival cohorts and AIReF evaluations of IMV labor incentives.

## 5. Methods & identification
1. **Structural Discrete-Choice Labor Supply Model:** Estimate a random-utility discrete hours-choice model ($h \in \{0, 20, 30, 40\}$) on Spanish ECV + EPA data, separately identifying substitution elasticities ($\varepsilon^c$) and income elasticities ($\eta$) across demographic cells [@saez-2002-optimal-transfers].
2. **Bunching & RD on Existing Spanish Thresholds:** Exploit sharp kinks and notches in the IRPF tariff [@boe-irpf-2006], IMV income phase-out [@boe-imv-2021], and SEPE *subsidio para mayores de 52 años* in MCVL to estimate Spanish extensive/intensive elasticities.
3. **Transition-to-Formal-Work Hazard Model:** Model informal-to-formal and *autónomo* entry hazards when METRs drop from ~100% (IMV) to ~45% (UBR + IRPF).

## 6. Pilot implications
- **Municipal / Regional / National (`M10`):** Link pilot participants (with informed GDPR consent) directly to monthly Seguridad Social affiliation records (*vidas laborales*) and AEAT 190 withholdings so labor supply, contract type (*indefinido*, *fijo discontinuo*, *autónomo*), and wage match quality are measured without survey recall bias.

## 7. Risks, counterarguments & open issues
- **Counterargument (Tax-Financed Substitution Effect):** RCTs test windfall transfers ($+\text{income effect}$ only), whereas a permanent national UBR also raises marginal IRPF rates ($+\text{substitution effect}$ [@hoynes-rothstein-2019]). *Mitigation:* Always simulate the **combined** income + marginal-tax substitution effect in EUROMOD/structural models and include a simulated tax-rate arm in the regional pilot (`M10`).

## 8. Deliverables & effort
- Demographic Cell Matrix of Spanish Income & Substitution Elasticities ($\eta, \varepsilon^c$).
- Behavioral Labor-Supply Adjustment Module for EUROMOD (`M03`, `M09`) and Chapter 2/7. (Effort: 6 person-weeks).


<!-- FILE: plan/modules/M09-distribution-poverty-euromod.md -->
---
id: M09
title: Distributional, poverty, and inequality microsimulation
status: draft
locked: false
depends_on: [M01, M02, M03, M07, M08]
covers: [F10]
feeds_chapters: [4]
last_iteration: 0
---
# M09 · Distributional, poverty, and inequality microsimulation

## 1. Why this matters
Spain persistently exhibits one of the highest child poverty, anchored poverty, and disposable-income inequality (Gini and S80/S20) rates in Western Europe, driven by unemployment volatility and weak cash transfers for working-age households and children [@arcelus-bade-2015-rgi]. As AI displacement (`M01`) widens market-income inequality across S1–S3, this module quantifies the exact distributional impact of UBR Tiers A, B, and C across income deciles, family types, age cohorts, and Autonomous Communities.

## 2. Research questions
- **RQ-M09-01**: What is the static and behavioral impact of UBR Tiers A, B, and C (integrated with IRPF `M03` and the `M07` No-Loser Guarantee) on Spain's headline AROPE rate, severe poverty (<40% median equivalized income), child poverty, Gini coefficient, and S80/S20 ratio across S1–S3?
  - *Hypothesis:* Tier B (€900/adult, €360/minor) reduces severe monetary poverty (<40% median) in Spain by >85%, cuts child monetary poverty by >70%, and lowers the disposable-income Gini coefficient by 6.5–8.0 Gini points even under Scenario S2 market-income polarization.
- **RQ-M09-02**: Which household types and income deciles are net winners versus net contributors under each financing mix (`M03`, `M16`), and what share of households in deciles 1–5 experience any net income loss?
  - *Hypothesis:* Deciles 1–6 are net financial winners on average, decile 7 is approximately net-neutral ($\pm 2\%$ of disposable income), deciles 8–10 are net contributors, and the `M07` No-Loser Guarantee reduces the share of losing households in deciles 1–4 below 0.5%.

## 3. State of knowledge
Tax-benefit microsimulation using EUROMOD [@sutherland-figari-2013-euromod] is the gold standard for evaluating distributional reforms in Europe. Prior Spanish microsimulations show that while the 2021 IMV [@boe-imv-2021] significantly reduces deep poverty (the poverty gap $P_1$) among households that actually receive it, high non-take-up (>50%) and restrictive eligibility criteria leave headline AROPE poverty largely unchanged [@arcelus-bade-2015-rgi]. Universal schemes eliminate non-take-up exclusion errors (Type I errors) entirely [@van-parijs-vanderborght-2017; @hoynes-rothstein-2019].

## 4. Spain context & data sources
- **Survey & Administrative Microdata:** INE *Encuesta de Condiciones de Vida* (ECV, EU-SILC Spanish component with Autonomous Community oversampling), IEF/AEAT *Muestra de Declarantes de IRPF* (to correct ECV top-income truncation), and INE *Encuesta de Presupuestos Familiares* (EPF, to account for indirect IVA tax incidence).
- **Take-Up Calibration:** AIReF *Opinión sobre el Ingreso Mínimo Vital* municipal/regional take-up rates to construct a realistic baseline counterfactual (comparing UBR at ~98% automatic take-up against IMV at observed vs. 100% theoretical take-up).

## 5. Methods & identification
1. **Top-Coding Correction & ECV-IRPF Statistical Matching:** Reweight and impute top 5% capital and business incomes in ECV using the IEF/AEAT IRPF administrative sample so top-decile tax capacity is accurately measured.
2. **Decomposition of Inequality & Poverty Changes:** Compute Foster-Greer-Thorbecke ($P_0, P_1, P_2$) poverty indices, Gini, Atkinson ($\varepsilon \in \{0.5, 1.0, 2.0\}$), and Shorrocks-Shapley decompositions isolating the direct UBR transfer effect, the benefit-replacement effect (`M07`), the IRPF/IVA financing effect (`M03`), and the behavioral labor-supply effect (`M08`).

## 6. Pilot implications
- **Municipal / Regional / National:** Use microsimulation distributional maps to select pilot stratification cells (`M10`) and benchmark experimental poverty declines against EUROMOD predictions.

## 7. Risks, counterarguments & open issues
- **Counterargument (Middle-Class Tax Squeeze in Deciles 6–8):** Dual-earner middle-class households without children in high-cost cities may become net contributors at relatively modest real living standards. *Mitigation:* Report granular winner/loser matrices cross-tabulated by decile $\times$ family type $\times$ housing tenure (`M05`) and shift part of the financing burden from IRPF labor brackets to `M16` AI/capital/wealth bases.

## 8. Deliverables & effort
- Open-Source EUROMOD-Spain UBR Policy Add-On & Replication Package.
- Complete Decile, Demographic, and Regional Distributional Atlas for Chapter 4. (Effort: 6 person-weeks).


<!-- FILE: plan/modules/M10-pilot-evaluation-design.md -->
---
id: M10
title: Multi-level pilot and causal evaluation design
status: draft
locked: false
depends_on: [M02, M05, M06, M08, M12, M15]
covers: [F11]
feeds_chapters: [7]
last_iteration: 0
---
# M10 · Multi-level pilot and causal evaluation design

## 1. Why this matters
Past basic income pilots worldwide have suffered from three recurrent methodological limitations: (i) dispersed individual randomization that cannot detect general-equilibrium effects on local rents, prices, or wages [@egger-2022-ge-kenya; @hoynes-rothstein-2019]; (ii) testing only gross windfall transfers without the tax-financing clawback; and (iii) reliance on high-attrition self-reported surveys [@kangas-2021-finland]. Following `D-005`, this module designs a rigorous, pre-registered multi-level Spanish pilot architecture comparing **Municipal**, **Regional (Común vs. Foral)**, and **National** experimental options.

## 2. Research questions
- **RQ-M10-01**: How can a two-stage randomized saturation design in Spain jointly identify partial-equilibrium behavioral responses (individual labor supply, health, consumption) and local general-equilibrium spillovers (rental pass-through `M05`, wage bargaining `M08`, local multipliers `M04`)?
  - *Hypothesis:* Combining Arm 1 (dispersed individual RCT across 60 municipalities, $N = 5,000$ treated, $N = 10,000$ control) with Arm 2 (cluster-randomized 80–100% universal saturation in 6 matched municipal/comarcal units vs. 12 synthetic/matched controls, $N \approx 15,000$ treated) achieves 80% statistical power ($\alpha = 0.05$) to detect a $\ge 1.5$ hour/week labor supply shift and a $\ge 3.5\%$ local rental pass-through differential.
- **RQ-M10-02**: How can a regional or national pilot incorporate a **Net-Tax / Clawback Treatment Arm** to measure real-world elasticity to the combined UBR + IRPF marginal tax schedule (`M03`)?
  - *Hypothesis:* Running a dedicated arm in a *régimen foral* community (Basque Country or Navarre) or under a State IRPF delegation where treated middle-income participants receive UBR alongside adjusted monthly withholding rates ($t = 45\%$) provides the first causal estimate in Europe of net tax-transfer labor elasticity.

## 3. State of knowledge
Recent landmark trials—OpenResearch [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health], GiveDirectly's village-saturation experiment in Kenya [@egger-2022-ge-kenya], Finland's nationwide register-linked RCT [@kangas-2021-finland], Stockton SEED [@west-2024-seed], and Barcelona's B-MINCOME [@todeschini-bmincome-2020]—demonstrate that linking administrative registers eliminates differential attrition on employment and tax outcomes, while cluster saturation is indispensable for capturing general equilibrium. Catalonia's 2021–2023 Office for the Basic Income Pilot Plan (*Oficina del Pla Pilot per Implementar la Renda Bàsica Universal*) designed a hybrid individual + municipal saturation blueprint that was halted solely by parliamentary budget veto (`M11`).

## 4. Spain context & data sources
- **Spanish Precedents:** B-MINCOME (Barcelona 2017–2019, 1,000 vulnerable households across 4 modalities in Eix Besòs [@todeschini-bmincome-2020]), Catalonia's designed saturation protocol, and the Ministry of Inclusion's 34 IMV inclusion-itinerary RCTs.
- **Administrative Register Spine:** Continuous linkage via DNI/NIE to Seguridad Social (INSS/TGSS daily affiliation & contribution bases), AEAT/Foral tax filings, SEPE unemployment records, SNS primary-care/mental-health electronic records, and INCASÒL/autonomous rental deposit registries.

## 5. Methods & identification
1. **Three-Tier Comparative Pilot Blueprint (`D-005`):**
   - *Option 1 (Municipal Tier):* Urban/rural pair (e.g. metropolitan Barcelona/Madrid district + rural Castile/Extremadura municipality), duration 36 months, testing Tier A (€600) vs. Tier B (€900).
   - *Option 2 (Regional Tier):* Parallel *Régimen Común* (Catalonia saturation + individual RCT) and *Régimen Foral* (Basque Country / Navarre net-tax IRPF integration arm).
   - *Option 3 (National Phase-In Cohort):* Staggered national rollout by birth-cohort or AI-displaced sector (`M17`) evaluated via regression discontinuity and difference-in-differences.
2. **Power, MDE & Budget Calculator:** Derive exact sample sizes, ICC adjustments, MDEs, and net fiscal pilot budgets (€180M–€450M over 3 years, co-financeable via EU ESF+ social innovation funds).

## 6. Pilot implications
- **Ethics & Post-Pilot Cliff (`ethics_equity`):** Pre-commit to a 6-month tapered step-down transition after month 36 plus a binding legal guarantee (`M06`, `M07`) that no participant loses prior entitlement to IMV, RGI/RGC, or disability benefits.
- **Pre-Registration:** Register complete Pre-Analysis Plan (PAP) at the AEA RCT Registry before baseline randomization.

## 7. Risks, counterarguments & open issues
- **Counterargument (Hawthorne & Horizon Bias):** Participants know a 3-year pilot is temporary, attenuating permanent-income responses (such as career switches or fertility/migration) relative to a permanent law [@hoynes-rothstein-2019]. *Mitigation:* Stratify horizon expectations and combine 3-year RCT estimates with structural parameters from permanent Spanish pension/disability discontinuities (`M08`).

## 8. Deliverables & effort
- Complete Pre-Analysis Plan (PAP) Template, Power/MDE Tables, and Budget Envelopes for Municipal, Regional, and National pilots.
- Administrative Data-Linking Protocol (INSS-AEAT-INE-SNS) for Chapter 7. (Effort: 7 person-weeks).


<!-- FILE: plan/modules/M11-political-economy.md -->
---
id: M11
title: Political economy, public opinion, and coalition feasibility
status: draft
locked: false
depends_on: [M03, M06, M09, M16, M17]
covers: [F12]
feeds_chapters: [8]
last_iteration: 0
---
# M11 · Political economy, public opinion, and coalition feasibility

## 1. Why this matters
Even an economically optimal and constitutionally valid UBR plan will fail if it cannot assemble a durable legislative coalition in Spain's fragmented multi-party parliament (*Congreso de los Diputados*), secure buy-in from social partners (trade unions CCOO and UGT, employers CEOE), and survive autonomous-community veto politics—as illustrated by the parliamentary blockage of the Catalan UBR pilot budget [@van-parijs-vanderborght-2017].

## 2. Research questions
- **RQ-M11-01**: How do policy design attributes—framing (traditional "Universal Basic Income" vs. "AI Productivity Dividend" vs. "Refundable IRPF Tax Credit"), financing source (labor IRPF vs. AI/corporate/wealth levies `M16`), residency rules (`M13`), and benefit level—shift support among Spanish median-decile voters and across party electorates?
  - *Hypothesis:* In a pre-registered conjoint experiment on a representative Spanish sample, framing UBR as an IRPF-integrated "AI & Automation Dividend" financed predominantly by corporate/AI/capital levies (`M16`) with a 2–3 year residency requirement increases majority support by +14 to +20 percentage points compared to a labor-tax-financed welfare framing, winning majority backing across left, center, and regionalist voters.
- **RQ-M11-02**: Under what institutional bargains do Spanish trade unions (CCOO, UGT)—historically protective of contributory Bismarckian rights and collective bargaining—endorse UBR rather than opposing it as a wage subsidy or welfare deregulation?
  - *Hypothesis:* Union endorsement requires three explicit statutory guarantees: (i) strict preservation of the `M07` contributory slope and collective-bargaining SMI floors, (ii) ring-fencing health, education, and dependency budgets against UBR crowd-out, and (iii) co-governance of S1–S3 AI displacement triggers (`M17`).

## 3. State of knowledge
Comparative political economy shows that universal programs enjoy greater long-term fiscal resilience than narrowly targeted means-tested programs ("paradox of redistribution"), yet face high initial enactment hurdles because visible gross tax hikes alarm middle-decile voters and insiders [@van-parijs-vanderborght-2017; @hoynes-rothstein-2019]. In Spain, survey research indicates high baseline sympathy for basic income principles alongside sharp sensitivity to perceived fiscal cost and reciprocity norms.

## 4. Spain context & data sources
- **Public Opinion Data:** *Centro de Investigaciones Sociológicas* (CIS) barometers, European Social Survey (ESS) Spanish waves on welfare attitudes, and CEO (*Centre d'Estudis d'Opinió*) surveys on the Catalan UBR pilot.
- **Institutional Actors:** Parliamentary records (*Diario de Sesiones del Congreso* on IMV [@boe-imv-2021]), official position papers of CCOO, UGT, USO, CEOE-CEPYME, and autonomous-community governments.

## 5. Methods & identification
1. **Pre-Registered Conjoint Survey Experiment ($N = 3,500$ Spanish Voters):** Randomize 6 policy dimensions (Benefit Amount, Tax Financing Mechanism, AI Trigger Condition, Residency Rule, Treatment of Existing Pensions/Benefits, Administrative Level) to estimate Average Marginal Component Effects (AMCEs) by income decile, CNO-11 AI-exposure risk (`M01`), autonomous community, and party vote recall.
2. **Veto-Player & Coalition Mapping:** Combine EUROMOD decile/regional net-winner tables (`M09`) with electoral district demographics to model parliamentary coalition equilibria across S1–S3.

## 6. Pilot implications
- **Municipal / Regional / National:** Insulate the `M10` pilot from mid-cycle electoral cancellation by anchoring its multi-year budget in an independent consortium overseen by AIReF / IEF and co-financed by European Union research/social-innovation grants.

## 7. Risks, counterarguments & open issues
- **Counterargument (Territorial Fiscal Backlash):** Net-contributing regions with higher nominal wages and cost of living (Madrid, Catalonia, Balearics) will show a higher share of net IRPF contributors to a uniform national UBR (`M09`). *Mitigation:* Quantify inter-regional fiscal flows transparently and test whether pairing national Tier A with regionally financed cost-of-living supplements (`M13`) stabilizes territorial coalitions.

## 8. Deliverables & effort
- Conjoint Survey Experiment Questionnaire, Pre-Registration, and AMCE Estimation Pipeline.
- Spanish Stakeholder & Parliamentary Coalition Matrix for Chapter 8. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M12-administration-delivery.md -->
---
id: M12
title: Administrative delivery, digital infrastructure, and take-up
status: draft
locked: false
depends_on: [M03, M06, M07, M10]
covers: [F13]
feeds_chapters: [6]
last_iteration: 0
---
# M12 · Administrative delivery, digital infrastructure, and take-up

## 1. Why this matters
The flagship lesson from Spain's *Ingreso Mínimo Vital* (IMV [@boe-imv-2021]) is that statutory generosity fails when administrative delivery relies on ex-ante means testing, complex household cohabitation verification, and prior-year tax declarations: according to AIReF, over 55% of eligible households in deep poverty never receive IMV, while thousands of vulnerable families suffer sudden retrospective debt clawbacks (*cobros indebidos*). UBR's primary operational advantage is near-100% automatic delivery through joint AEAT–Seguridad Social infrastructure.

## 2. Research questions
- **RQ-M12-01**: How can Spain's *Agencia Estatal de Administración Tributaria* (AEAT), *Instituto Nacional de la Seguridad Social* (INSS), and INE *Padrón Continuo* execute monthly individual UBR disbursement and real-time IRPF withholding clearing with >98% take-up and zero retrospective debt traps?
  - *Hypothesis:* Operating a **Unified Monthly Tax-Transfer Clearing Account** (*Cuenta Única Tributaria-Social*) linked to DNI/NIE—where every resident receives the monthly UBR transfer (or nets it directly against monthly IRPF payroll withholding *retenciones a cuenta* for formal salaried workers) without application forms—raises take-up above 98% and reduces administrative overhead per beneficiary by >75% relative to IMV.
- **RQ-M12-02**: What outreach, banking-inclusion, and legal-guardianship protocols are required to reach the remaining 2% of residents (unbanked individuals, homeless persons, rural elderly without digital certificates, victims of domestic violence, and institutionalized minors)?
  - *Hypothesis:* Combining automatic *de oficio* enrollment via municipal social services and Correos prepaid basic payment accounts (*cuentas de pago básicas*) closes >80% of the residual exclusion gap without requiring digital literacy.

## 3. State of knowledge
Empirical public administration research demonstrates that application burdens, stigma, recertification requirements, and fear of retrospective overpayments are the primary drivers of welfare non-take-up [@hoynes-rothstein-2019; @arcelus-bade-2015-rgi]. In contrast, universal child benefits and automatic tax credits achieve 96–99% coverage [@van-parijs-vanderborght-2017]. Experimental evidence from B-MINCOME [@todeschini-bmincome-2020] and Finland [@kangas-2021-finland] shows that predictable, unconditional monthly disbursement on a fixed calendar day eliminates cognitive scarcity and short-term predatory borrowing.

## 4. Spain context & data sources
- **Existing Spanish Digital Spine:** AEAT (*Renta Web*, monthly SII and Form 111/190 payroll withholdings, Bizum/SEPA instant disbursement), TGSS/INSS (*Tarjeta Social Digital* integrated registry of all public cash benefits), and INE *Padrón Municipal Continuo*.
- **Legal & Privacy Constraints:** *Ley 58/2003 General Tributaria* Art. 95 (tax data sharing exceptions), *Ley 19/2021* [@boe-imv-2021] data-interoperability provisions, and EU GDPR Art. 6(1)(e) / *Ley Orgánica 3/2018 de Protección de Datos*.

## 5. Methods & identification
1. **Systems & Cash-Flow Architecture Design:** Specify two operational modes for formal employees: (i) *Gross-Flow Mode* (every resident receives €900 on the 1st of the month via SEPA transfer; employer withholds full IRPF rate $t$ on gross salary) vs. (ii) *Net-Withholding Mode* (UBR is credited directly inside the monthly payroll withholding formula, and AEAT transfers the net balance directly only when monthly withholding $< \text{UBR}$). Compare liquidity, visibility, and intra-household autonomy (`M14`).
2. **Administrative Cost-Savings Audit:** Benchmark INSS/AEAT FTE personnel and IT costs under UBR against current IMV + regional minimum income administrative overhead.

## 6. Pilot implications
- **Municipal / Regional / National (`M10`):** Test automated SEPA + Correos basic-account disbursement and measure time-to-first-payment, error rates, and administrative cost per euro transferred.

## 7. Risks, counterarguments & open issues
- **Counterargument (Ghost Residents & Identity Fraud):** Automatic payment tied to *Padrón* registration could incentivize fraudulent registration of non-residents. *Mitigation:* Cross-verify *Padrón* entries against active healthcare card (*Tarjeta Sanitaria*), tax, school, or Social Security activity trails (`M13`) and periodic survival/presence checks (*fe de vida* for inactive records).

## 8. Deliverables & effort
- AEAT–INSS–Padrón Interoperability & Monthly Clearing Technical Specification.
- Last-Mile Inclusion Protocol (Unbanked, Homeless, Domestic Violence Survivors) for Chapter 6. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M13-migration-territory-residency.md -->
---
id: M13
title: Territorial purchasing power, internal mobility, and residency rules
status: draft
locked: false
depends_on: [M02, M05, M06, M12]
covers: [F14]
feeds_chapters: [5, 6]
last_iteration: 0
---
# M13 · Territorial purchasing power, internal mobility, and residency rules

## 1. Why this matters
Spain displays a 35–45% gap in regional purchasing power parity (PPP) and rental costs between metropolitan cores (Madrid, Barcelona, San Sebastián, Palma) and depopulated rural provinces (*España vaciada*: Soria, Teruel, Cuenca, Zamora) [@boe-vivienda-2023]. A nationally uniform nominal UBR (€900/month) acts as a powerful spatial equalizer—providing a high real living standard in rural municipalities—while simultaneously raising questions about internal migration, urban housing adequacy (`M05`), and external migration residency rules (`M06`).

## 2. Research questions
- **RQ-M13-01**: Should Spain's UBR be paid as a strictly uniform nominal amount across the entire territory, or modulated by regional/municipal cost-of-living indices?
  - *Hypothesis:* A uniform nominal State UBR floor (preserving constitutional equality under Art. 149.1.1 CE [@boe-ce-1978] and avoiding capitalization into metropolitan land rents `M05`) outperforms regionally price-indexed national transfers; Autonomous Communities wishing to top up urban housing costs should finance supplements from own regional taxes (`M03`, `M06`).
- **RQ-M13-02**: To what extent does a portable, nationally uniform UBR induce voluntary residential relocation from high-rent metropolitan areas (`M05`) to mid-sized towns and rural municipalities (*España vaciada*) when remote work or AI displacement (`M01`) decouples income from big-city commuting?
  - *Hypothesis:* Under S2 and S3, a portable €900/adult UBR increases net residential retention and in-migration in municipalities under 10,000 inhabitants by 4–7% over 5 years, partially relieving metropolitan rental pressure (`M05`).

## 3. State of knowledge
Spatial equilibrium theory (Roback-Moretti frameworks) predicts that nominally uniform national transfers subsidize relocation to lower-cost, high-amenity regions, whereas cost-of-living-indexed transfers lock households into congested cities and capitalize into urban land values [@fack-2006-housing-benefits; @diamond-mcquade-qian-2019-rent]. Empirical cash-transfer studies confirm that unconditional portable transfers increase geographic mobility toward better housing and labor markets [@bartik-2024-openresearch]. Regarding external migration, welfare-magnet literature finds modest empirical effects that are effectively governed by statutory qualifying residency periods under EU Directive 2004/38/EC and Regulation 883/2004 [@eu-reg-883-2004].

## 4. Spain context & data sources
- **Spatial & Demographic Data:** INE *Estadística de Variaciones Residenciales* (EVR, inter-municipal migration flows), *Padrón Continuo*, regional PPP estimates, and MIVAU municipal housing price panels.
- **Residency & Legal Framework:** *Ley Orgánica 4/2000 sobre derechos y libertades de los extranjeros*, *Ley 19/2021* [@boe-imv-2021] (IMV requires 1 year of continuous legal residence in Spain, with exceptions for minors, trafficking victims, and gender-violence survivors), and EU Regulation 883/2004 [@eu-reg-883-2004].

## 5. Methods & identification
1. **Spatial Discrete-Choice Location Model:** Estimate a municipality choice model on EVR + MCVL data as a function of real net disposable income $(w_m + \text{UBR} - r_m)$, local public services, and AI remote-work feasibility (`M01`).
2. **Residency Eligibility Comparison:** Compare three residency rules—(R1) 12 months lawful residence (IMV baseline [@boe-imv-2021]), (R2) 24–36 months continuous lawful residence and fiscal domicile, and (R3) phased-in fractional accrual over years 1–3—evaluating fiscal cost (`M03`), EU legal validity (`M06`), and human-rights/destitution safeguards.

## 6. Pilot implications
- **Municipal / Regional (`M10`):** Include at least two low-density rural *comarcas* in the saturation pilot arm to measure demographic retention, local small-business creation, and municipal service utilization.
- **Strict Anti-Inflow Rule for Pilots:** Pilot eligibility must be locked to individuals registered in the municipal *Padrón* at least 12 months **prior** to the public announcement date of the pilot.

## 7. Risks, counterarguments & open issues
- **Counterargument (Welfare Magnet / Pull Factor):** Critics argue a €900 unconditional transfer will attract fiscally unsustainable inflows. *Mitigation:* Condition full UBR eligibility on continuous prior legal and fiscal residency (R2/R3, `M06`) with humanitarian exemptions for asylum/gender-violence cases.

## 8. Deliverables & effort
- Regional PPP Real-Value Atlas & Rural Demographic Retention Simulation.
- Statutory Residency Eligibility Specification for Chapter 5 and Chapter 6. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M14-gender-care-health.md -->
---
id: M14
title: Gender, unpaid care, disability, and health outcomes
status: draft
locked: false
depends_on: [M02, M07, M08, M09, M10]
covers: [F15]
feeds_chapters: [3, 7]
last_iteration: 0
---
# M14 · Gender, unpaid care, disability, and health outcomes

## 1. Why this matters
Spanish women perform over two-thirds of unpaid domestic and dependent-care hours, experience higher part-time employment and career interruptions, and consequently receive lower contributory pensions and unemployment benefits (`M07`). Because means-tested schemes like IMV [@boe-imv-2021] assess and pay a single household head (*titular*), they fail to guarantee financial autonomy inside the household. Paying UBR individually (`D-001`) directly alters intra-household bargaining power, financial independence for survivors of gender violence, care valuation, and population mental/physical health [@miller-2024-openresearch-health; @west-2024-seed].

## 2. Research questions
- **RQ-M14-01**: How does an individual UBR (`M02`) change the gender gap in personal disposable income, intra-household bargaining power, time allocation between paid work and unpaid care, and exit capacity from abusive partnerships in Spain?
  - *Hypothesis:* Tier B individual UBR reduces the share of cohabiting Spanish women with zero or below-poverty personal income from ~19% to 0%, increases male partner participation in unpaid care when combined with non-transferable parental leave, and significantly accelerates financial autonomy for gender-violence survivors.
- **RQ-M14-02**: What are the causal impacts of unconditional monthly income security on mental health (anxiety, depression, cortisol/sleep disorders), preventive healthcare utilization, and pharmaceutical expenditure in Spain's *Sistema Nacional de Salud* (SNS)?
  - *Hypothesis:* Consistent with Finland [@kangas-2021-finland], B-MINCOME [@todeschini-bmincome-2020], Stockton [@west-2024-seed], and OpenResearch [@miller-2024-openresearch-health], UBR reduces clinically significant psychological distress (GHQ-12 / PHQ-9) by 0.20–0.35 standard deviations and lowers primary-care mental-health and anxiolytic prescription costs by 8–14% among bottom-quintile adults.

## 3. State of knowledge
Across nearly every basic income trial, improvements in mental health, stress reduction, food security, and subjective wellbeing are the largest and most statistically robust findings [@kangas-2021-finland; @todeschini-bmincome-2020; @west-2024-seed; @miller-2024-openresearch-health]. Feminist economics emphasizes two competing gender effects of basic income: individual unconditional cash empowers women's exit options and values unpaid care [@van-parijs-vanderborght-2017], but could reinforce traditional gendered division of labor if secondary female earners reduce formal hours without accompanying public care infrastructure (*Sistema para la Autonomía y Atención a la Dependencia*, SAAD, and 0–3 early childhood education).

## 4. Spain context & data sources
- **Time-Use & Health Datasets:** INE *Encuesta de Empleo del Tiempo* (EET), *Encuesta Nacional de Salud de España* (ENSE) / *Encuesta Europea de Salud* (EESE), and Ministry of Health *Base de Datos Clínicos de Atención Primaria* (BDCAP).
- **Disability & Care Framework:** *Ley 39/2006 de Promoción de la Autonomía Personal y Atención a las personas en situación de dependencia* (SAAD) and *Real Decreto Legislativo 1/2013* on rights of persons with disabilities.

## 5. Methods & identification
1. **Individual vs. Pooled Intra-Household Microsimulation:** In EUROMOD-Spain (`M09`), compute inequality and poverty under both full income-pooling and zero/partial-sharing collective household models to measure the gender gap in individual economic security.
2. **Health & Healthcare Cost-Offset Estimation (`M10`):** In the Spanish pilot, link consented participants' SNS health-card records to measure PHQ-9/GAD-7 scores, emergency room visits, anxiolytic/antidepressant DDDs (*dosis diarias definidas*), and child birthweight/pediatric outcomes.
3. **Disability Extra-Cost Protection Audit:** Verify that all *Grado I–III* dependency and disability supplements (`M07`) remain strictly additive on top of UBR to cover conversion handicaps.

## 6. Pilot implications
- **Municipal / Regional / National (`M10`):** Stratify randomization by gender and caregiving status; forbid substituting UBR for in-kind public care services (0–3 nurseries, SAAD home care).

## 7. Risks, counterarguments & open issues
- **Counterargument (Maternal Labor Market Detachment):** Unconditional transfers could encourage low-wage mothers to exit the formal labor market permanently. *Mitigation:* Pair UBR with universal 0–3 public childcare and estimate separate female intensive/extensive elasticities in `M08` and `M10`.

## 8. Deliverables & effort
- Intra-Household Gender Autonomy & Care-Time Simulation.
- SNS Mental/Physical Health Cost-Offset & Disability Protection Protocol for Chapter 3 and Chapter 7. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M15-international-evidence.md -->
---
id: M15
title: Comparative international and Spanish empirical evidence
status: draft
locked: false
depends_on: [M08, M10, M14]
covers: [F16]
feeds_chapters: [1, 7]
last_iteration: 0
---
# M15 · Comparative international and Spanish empirical evidence

## 1. Why this matters
To reach state-of-the-art scientific credibility, the Spanish UBR research plan must systematically synthesize and extract structural parameters from all major unconditional cash transfer experiments and permanent dividend programs worldwide, while explicitly correcting for external-validity differences in benefit size, duration, financing, and institutional context [@hoynes-rothstein-2019; @banerjee-niehaus-suri-2019].

## 2. Research questions
- **RQ-M15-01**: What are the meta-analytic pooled causal estimates (and confidence intervals) across global and European UBI/guaranteed-income experiments for extensive-margin employment, weekly hours worked, mental health, educational enrollment, and local price inflation?
  - *Hypothesis:* Across advanced-economy trials (OpenResearch [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health], Finland [@kangas-2021-finland], B-MINCOME [@todeschini-bmincome-2020], Stockton SEED [@west-2024-seed], and Alaska PFD [@jones-marinescu-2022]), the pooled extensive-margin employment effect of an unconditional transfer equal to 25–40% of median income is within $[-2.1, +0.8]$ percentage points, with positive effects on mental health ($+0.25\sigma$) and human-capital investment.
- **RQ-M15-02**: Which institutional design flaws in Barcelona's B-MINCOME (2017–2019) and Catalonia's unimplemented 2023 RBU pilot protocol must be corrected in Spain's next-generation pilot (`M10`)?
  - *Hypothesis:* B-MINCOME's restriction to low-income households in Eix Besòs and interaction with state tax/benefit clawbacks prevented identification of middle-class net-taxpayer responses and municipal rent pass-through; Catalonia's protocol solved cluster saturation but lacked fiscal/IRPF competence (`M06`), proving the necessity of a State-backed or Foral-integrated pilot (`M10`).

## 3. State of knowledge
The empirical literature spans four distinct program classes:
1. **European Welfare-State RCTs:** Barcelona's B-MINCOME ($2\times 2$ factorial of conditionality $\times$ benefit withdrawal rate across 1,000 households [@todeschini-bmincome-2020]) and Finland's nationwide Kela RCT (2,000 unemployed recipients receiving €560/month unconditionally [@kangas-2021-finland]).
2. **US Guaranteed Income RCTs:** OpenResearch ($1,000/month for 3 years across $N=1,000$ treated vs. $2,000$ control [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health]) and Stockton SEED ($500/month [@west-2024-seed]).
3. **Permanent Universal Dividends:** Alaska Permanent Fund Dividend (universal annual resource dividend since 1982 [@jones-marinescu-2022]).
4. **High-Saturation General-Equilibrium Trials:** GiveDirectly's randomized saturation across 653 Kenyan villages [@egger-2022-ge-kenya; @banerjee-niehaus-suri-2019].

## 4. Spain context & data sources
- **Primary Spanish Trial Records:** Ajuntament de Barcelona / Ivàlua B-MINCOME public evaluation datasets and reports [@todeschini-bmincome-2020]; Generalitat de Catalunya *Oficina del Pla Pilot per Implementar la Renda Bàsica Universal* methodological design reports (2021–2023); Ministry of Inclusion IMV Policy Lab RCT syntheses.

## 5. Methods & identification
1. **Bayesian Hierarchical Meta-Analysis & Parameter Transfer:** Standardize effect sizes across trials by transfer-to-median-income ratio, implied marginal tax rate, and duration, using Bayesian hierarchical shrinkage to generate informative priors for `M08` (labor supply) and `M10` (MDE power calculations).
2. **External-Validity Gap Matrix:** Score each historical trial against 6 dimensions required for Spain's AI-displaced context: (i) universality across deciles, (ii) individual vs. household unit, (iii) tax-clawback integration, (iv) spatial saturation, (v) administrative register linkage, and (vi) AI-displaced occupational sampling.

## 6. Pilot implications
- Directly calibrates the MDEs, sample sizes, and treatment arms of `M10` so the Spanish pilot fills the exact empirical gaps left open by B-MINCOME, Finland, and OpenResearch.

## 7. Risks, counterarguments & open issues
- **Counterargument (Non-Transferability of Developing-Country or Windfall Pilots):** Kenyan saturation multipliers [@egger-2022-ge-kenya] or US non-taxed windfalls [@vivalt-2024-openresearch] do not directly transfer to a high-tax Eurozone economy. *Mitigation:* Weight priors by institutional similarity and explicitly separate windfall income effects from tax-financed substitution effects (`M08`).

## 8. Deliverables & effort
- Quantitative Meta-Analysis Table & Standardized Parameter Priors across 12 flagship UBI/GI evaluations.
- Comparative Critique of B-MINCOME and the Catalan Pilot Blueprint for Chapter 1 and Chapter 7. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M16-ai-rent-capture-sovereign-fund.md -->
---
id: M16
title: Capturing AI rents, capital taxation, and sovereign dividend funds
status: draft
locked: false
depends_on: [M01, M03, M04, M06]
covers: [F04]
feeds_chapters: [4]
last_iteration: 0
---
# M16 · Capturing AI rents, capital taxation, and sovereign dividend funds

## 1. Why this matters
Under severe and structural AI displacement scenarios (**S2** and **S3**, `M01`), national income shifts markedly from labor compensation to capital, corporate profits, intellectual property, and compute/automation rents [@acemoglu-2024-macro-ai; @korinek-suh-2024]. Financing UBR solely through labor IRPF brackets (`M03`) becomes mathematically impossible if the labor share falls by 7–15 percentage points of GDP. Crucially, because frontier AI foundation-model firms are overwhelmingly headquartered outside Spain (in the US and China), Spain cannot rely on naïve domestic R&D profit taxes—it must design destination-based, location-inelastic, and EU-coordinated instruments to capture AI productivity rents inside the Spanish economy [@guerreiro-rebelo-teles-2022-robots; @cazzaniga-imf-2024].

## 2. Research questions
- **RQ-M16-01**: What combination of domestic and EU-coordinated tax instruments—Corporate Income Tax (*Impuesto sobre Sociedades*) minimum effective rate reform, destination-based digital/AI service & compute levies, energy/data-center capacity royalties, and net wealth/inheritance taxation (*Impuesto Temporal de Solidaridad de las Grandes Fortunas*)—can sustainably raise 2.5–4.5% of Spanish GDP under S2 and S3 without triggering capital flight?
  - *Hypothesis:* Because Spain is primarily an AI *adopter* and *consumer* rather than a frontier model exporter, destination-based taxation of B2B/B2C automated services, domestic corporate windfall surpluses from labor-cost reductions (reduced employer Social Security *cotizaciones* recycled into a productivity contribution), and immobile land/wealth levies raise 3.2–4.0% of GDP with low relocation elasticity.
- **RQ-M16-02**: How should Spain structure a ring-fenced **Fondo Soberano de Renta Básica y Dividendos de IA** (modeled on the Alaska Permanent Fund [@jones-marinescu-2022] and Norway's GPFG) that accumulates equity stakes, public data/compute licensing fees, and AI tax earmarks to co-finance the transition from Tier A/B to Tier C?
  - *Hypothesis:* Allocating 1.0–1.5% of GDP annually from windfall capital/automation levies and public-sector AI productivity savings into a diversified global equity + compute-infrastructure sovereign fund builds an endowment capable of funding 15–20% of net UBR cost within 12–15 years (Scenario S3 horizon).

## 3. State of knowledge
Optimal automation-taxation theory [@guerreiro-rebelo-teles-2022-robots; @korinek-suh-2024; @cazzaniga-imf-2024] shows that while taxing intermediate capital inputs (standard machinery) can be distortionary when routine workers can retrain, taxing pure economic rents, monopoly markups, and automation windfalls becomes Pareto-improving when displaced workers face structural skill barriers. Resource-dividend evidence from Alaska [@jones-marinescu-2022] demonstrates that earmarking a visible common-asset fund to universal dividends creates durable political legitimacy (`M11`).

## 4. Spain context & data sources
- **Tax & Regulatory Baseline:** *Ley 27/2014 del Impuesto sobre Sociedades* (15% minimum Pillar Two global tax implementation), *Ley 4/2020 del Impuesto sobre Determinados Servicios Digitales* (Tasa Google), *Impuesto de Solidaridad de las Grandes Fortunas*, employer Social Security contribution schedules (*cotizaciones empresariales*), and the EU AI Act [@eu-ai-act-2024].
- **Data Sources:** AEAT corporate tax consolidated accounts (*Cuentas Anuales en el Impuesto sobre Sociedades*), Banco de España *Central de Balances*, and INE *Contabilidad Nacional* gross operating surplus (*Excedente Bruto de Explotación*, EBE) by NACE sector.

## 5. Methods & identification
1. **Employer Payroll-to-Value-Added Tax Shift Simulation:** As firms replace human workers with AI agents in S2/S3, their employer Social Security bill (*cotización empresarial*, ~30% of gross wage) drops sharply while Gross Operating Surplus (EBE) rises. Simulate replacing a share of employer payroll taxes with a **Contribución General sobre el Valor Añadido Neto / Excedente Operativo** (neutral across human vs. AI production factors).
2. **Cross-Border Incidence & Elasticity Audit:** Evaluate each candidate revenue instrument on three criteria: (i) static & dynamic yield (% GDP in S1, S2, S3), (ii) legal compatibility with EU state-aid, VAT Directive, and OECD Pillar One/Two rules (`M06`), and (iii) tax-base mobility/evasion elasticity.

## 6. Pilot implications
- **Regional / National:** While municipal/regional pilots cannot enact international AI taxes, the Basque/Navarre Foral corporate tax (*Impuesto sobre Sociedades foral*) or State legislation can pilot the **Neutral Value-Added Social Contribution** and establish the legal charter of the *Fondo Soberano de Dividendos de IA*.

## 7. Risks, counterarguments & open issues
- **Counterargument (Taxing Automation Slows Spanish AI Adoption & Competitiveness):** A punitive tax on AI software or robots could deter technology adoption in Spain's SME-heavy economy [@guerreiro-rebelo-teles-2022-robots]. *Mitigation:* Do not tax AI adoption inputs directly; instead, shift financing from labor payroll (*cotizaciones*) to neutral net value added / corporate operating surplus and destination-based digital monopoly rents, which actually *lowers* the relative tax wedge on human employment.

## 8. Deliverables & effort
- S1–S3 Revenue Yield & Elasticity Table for 6 AI-Rent and Capital Tax Instruments.
- Charter & Actuarial Accumulation Model for the Spanish *Fondo Soberano de Dividendos de IA* in Chapter 4. (Effort: 6 person-weeks).


<!-- FILE: plan/modules/M17-transition-risks-stress-tests.md -->
---
id: M17
title: Transition path, scenario triggers, and tail-risk stress tests
status: draft
locked: false
depends_on: [M01, M03, M04, M05, M07, M10, M11, M16]
covers: [F17]
feeds_chapters: [8]
last_iteration: 0
---
# M17 · Transition path, scenario triggers, and tail-risk stress tests

## 1. Why this matters
Moving from Spain's current welfare state directly to a full Tier B/C Universal Basic Rent overnight would create severe administrative, fiscal, and macroeconomic friction. Conversely, an open-ended pilot with no statutory scale-up rules risks political stalling (`M11`). A state-of-the-art research plan must specify a reversible, rule-governed **Phased Transition Roadmap** with quantitative macroeconomic triggers linking `M01` AI displacement indicators to benefit and tax tiers, alongside automatic fiscal and inflation circuit-breakers (`M04`, `M05`).

## 2. Research questions
- **RQ-M17-01**: What staged sequencing—from Phase 0 (automatic individualization and take-up reform of IMV + CAPI + IRPF refundable credits) to Phase 1 (Multi-Level Pilot `M10` + Tier A €600 floor under S1), Phase 2 (Tier B €900 poverty-line UBR under S2), and Phase 3 (Tier C €1,200 AI-dividend UBR under S3)—minimizes transitional welfare losses and fiscal deficit spikes?
  - *Hypothesis:* A four-phase rule-based rollout anchored to observable quarterly indicators (EPA cognitive-displacement index, labor-share $\Delta s_L$, and net fiscal neutrality) keeps the structural primary balance within $\pm 0.4\%$ of GDP throughout the transition while guaranteeing zero welfare losses via the `M07` supplement.
- **RQ-M17-02**: Which automatic statutory circuit-breakers (core non-tradable inflation gap vs. Eurozone, urban rental pass-through index, and Bonos-Bund sovereign spread) effectively bound tail risks without undermining household income certainty?
  - *Hypothesis:* Pre-committing to symmetric indexation rules—where nominal UBR step-ups pause or redirect into social housing supply (`M05`) if domestic non-tradable CPI exceeds the Eurozone average by $>1.5$ pp or urban rent pass-through exceeds $20\%$—prevents inflationary spirals while preserving the nominal cash floor.

## 3. State of knowledge
Mechanism design for macroeconomic stabilization emphasizes rule-based automatic stabilizers over discretionary legislative packages, which suffer from recognition and implementation lags [@auclert-rognlie-straub-2024; @kaplan-moll-violante-2018-hank]. Scenario planning for transformative AI [@korinek-suh-2024; @cazzaniga-imf-2024] highlights high uncertainty over arrival speed, making state-contingent policy schedules (policies indexed to realized labor-share and task-displacement thresholds) strictly superior to fixed-calendar commitments.

## 4. Spain context & data sources
- **Institutional Governance & Fiscal Watchdogs:** *Autoridad Independiente de Responsabilidad Fiscal* (AIReF, statutory mandate under *Ley Orgánica 6/2013* to audit fiscal sustainability and evaluate IMV), Banco de España, INE quarterly national accounts, and the *Consejo de Política Fiscal y Financiera* (CPFF).

## 5. Methods & identification
1. **State-Contingent Policy Rule Specification:** Define formal mathematical trigger functions mapping quarterly INE/Seguridad Social indicators $(\Delta s_{L,t}, u_{\text{AI},t}, \pi_{\text{NT},t}, \text{Spread}_t)$ to the active UBR tier and `M03`/`M16` tax parameters.
2. **Adversarial Tail-Risk Stress Testing:** Subject the integrated EUROMOD (`M03`, `M09`) + HANK (`M04`) pipeline to four compound stress scenarios:
   - *Stress 1 (Stagflationary Energy/Geopolitical Shock + S2):* Imported energy price spike coinciding with AI displacement.
   - *Stress 2 (Capital Flight / Tax Evasion Surge):* High-income taxable income elasticity (ETI) double the baseline estimate.
   - *Stress 3 (Metropolitan Rent Surge):* Urban rental supply elasticity half the baseline (`M05`).
   - *Stress 4 (Asymmetric Regional Shock):* Severe service-sector displacement in Madrid/Catalonia alongside tourism boom in coastal regions.

## 6. Pilot implications
- **Pre-Committed Scale-Up & Disconfirmation Criteria (`counterarguments`):** Specify exact quantitative thresholds from the `M10` pilot that either **confirm** readiness for Phase 2 scale-up (e.g. formal labor participation drop $<3$ pp, rent pass-through $<15\%$, net administrative take-up $>95\%$) or **disconfirm** a design feature and trigger mandatory redesign.

## 7. Risks, counterarguments & open issues
- **Counterargument (Time-Inconsistency & Political Manipulation of Triggers):** Governments may override fiscal circuit-breakers before elections. *Mitigation:* Vest trigger certification in AIReF as an independent statutory fiscal council under Organic Law.

## 8. Deliverables & effort
- Phased Implementation Roadmap (Phase 0 to Phase 3) & AIReF Trigger Certification Charter.
- Four-Scenario Tail-Risk Stress-Test Matrix & Disconfirmation Criteria Table for Chapter 8. (Effort: 5 person-weeks).


<!-- FILE: plan/paper-outline.md -->
# Target Paper Structure & Module-to-Chapter Mapping (`paper-outline.md`)

The final deliverable is a monograph-scale academic and policy paper in English with a comprehensive Spanish executive summary (`D-003`). Every module in `plan/modules/` feeds directly into one or more chapters below so that drafting the paper is a deterministic compilation and empirical execution of the approved research plan.

| Chapter | Title | Source Modules | Core Analytical Output |
|---:|---|---|---|
| **0** | **Executive Summary / *Resumen Ejecutivo para Decisores Públicos* (EN + ES)** | `00-scope`, `M01`–`M17` | Synthesis of S1–S3 scenarios, fiscal numbers, legal roadmap, and pilot blueprint |
| **1** | **Introduction & Analytical Framework: Welfare States When AI Compresses Labor Income** | `00-scope`, `M01`, `M15` | Problem statement, UBR vs. IMV/NIT taxonomy, international empirical baseline |
| **2** | **The AI Shock in Spain: Occupational Exposure, Wage-Bill Scenarios (S1–S3), and Fiscal Drag** | `M01`, `M08` | CNO-11/EPA exposure maps, MCVL displacement hazards, S1–S3 payroll erosion paths |
| **3** | **Benefit Architecture & Welfare Integration: Replacing Poverty Traps under a No-Loser Constraint** | `M02`, `M07`, `M14` | Tiers A/B/C (€600/€900/€1,200), folding IMV/regional schemes, care & disability protection |
| **4** | **Fiscal Architecture & AI Rent Capture: From Labor Taxation to Capital and Compute Dividends** | `M03`, `M09`, `M16` | EUROMOD-Spain net cost, IRPF/IVA reform, AI/corporate/wealth taxes, decile distributional tables |
| **5** | **Macroeconomic Closure & Housing Markets in the Eurozone: Demand Stabilization vs. Rent Capture** | `M04`, `M05`, `M13` | Open-economy HANK model, Eurozone fiscal rules, urban rental pass-through & housing supply |
| **6** | **Constitutional, Territorial, and EU Legal Blueprint: Common vs. Foral Regimes and Free Movement** | `M06`, `M12`, `M13` | Arts. 41/149 CE, LOFCA vs. Concierto Vasco, EU Reg. 883/2004, AEAT-INSS-Padrón delivery |
| **7** | **Multi-Level Pilot & Causal Evaluation Design: Municipal, Autonomous Community, and National Options** | `M10`, `M08`, `M15` | Two-stage RCT + cluster saturation design, MDE/power tables, administrative data linkage |
| **8** | **Political Economy, Phased Transition, and Tail-Risk Governance** | `M11`, `M17` | Conjoint voter experiment, union/employer coalition map, S1→S3 triggers & circuit-breakers |


<!-- FILE: plan/open-questions.md -->
# Open Research & Policy Questions (`open-questions.md`)

This file tracks unresolved analytical, empirical, or normative questions surfaced during plan iterations. Items resolved by human decisions are promoted to `plan/decisions.md`.

## Active Questions for Investigation in the Loop
- **OQ-01 (Foral vs. Common Regime Pilot Priority):** In `M06` and `M10`, should the primary regional pilot recommendation favor a *régimen foral* community (Basque Country / Navarre, which can legally modify IRPF withholdings to test a true net-tax UBR) or a *régimen común* community (Catalonia, which already designed a saturation pilot protocol)?
- **OQ-02 (Housing Supply Complementarity):** In `M05`, what minimum elasticity of public/affordable rental supply or rent-index enforcement under *Ley 12/2023* is required in stressed urban zones (*zonas tensionadas*) to keep landlord capture of Tier B UBR (€900/month) below 15%?
- **OQ-03 (Cross-Border AI Rent Capture):** Because frontier AI model providers are predominantly domiciled outside Spain (US/China), how much domestic revenue can Spain realistically raise unilaterally (`M16`) versus requiring an EU-wide pillar (EU Digital/Compute Levy or destination-based cash-flow tax)?
- **OQ-04 (Residency Duration Threshold):** What residency duration (e.g. 1, 2, or 5 years of continuous *empadronamiento* and lawful residence) maximizes legal durability under EU Directive 2004/38/EC (`M06`, `M13`) while preventing destitute exclusion?


<!-- FILE: plan/sources.yaml (summary) -->
## Source registry

| id | authors | year | title | locator | verified |
|---|---|---|---|---|---|
| acemoglu-restrepo-2019 | Acemoglu; D.; Restrepo | 2019 | Automation and New Tasks: How Technology Displaces and Reinstates Labor | doi:10.1257/jep.33.2.3 | yes |
| acemoglu-2024-macro-ai | Acemoglu; D. | 2024 | The Simple Macroeconomics of AI | doi:10.1093/epolic/eiae042 | yes |
| eloundou-2024-gpts | Eloundou; T.; Manning | 2024 | GPTs are GPTs: Labor market impact potential of LLMs | doi:10.1126/science.adj0998 | yes |
| webb-2020-ai | Webb; M. | 2020 | The Impact of Artificial Intelligence on the Labor Market | doi:10.2139/ssrn.3482150 | yes |
| felten-2021-aioe | Felten; E.; Raj | 2021 | Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses | doi:10.1002/smj.3286 | yes |
| korinek-suh-2024 | Korinek; A.; Suh | 2024 | Scenarios for the Transition to AGI | doi:10.3386/w32255 | yes |
| cazzaniga-imf-2024 | Cazzaniga; M.; Jaumotte | 2024 | Gen-AI: Artificial Intelligence and the Future of Work | doi:10.5089/9798400262548.006 | yes |
| gmyrek-ilo-2023 | Gmyrek; P.; Berg | 2023 | Generative AI and Jobs: A global analysis of potential effects on job quantity and quality | doi:10.54394/FHEM8239 | yes |
| van-parijs-vanderborght-2017 | Van Parijs; P.; Vanderborght | 2017 | Basic Income: A Radical Proposal for a Free Society and a Sane Economy | doi:10.4159/9780674978072 | yes |
| hoynes-rothstein-2019 | Hoynes; H.; Rothstein | 2019 | Universal Basic Income in the United States and Advanced Countries | doi:10.1146/annurev-economics-080218-030237 | yes |
| banerjee-niehaus-suri-2019 | Banerjee; A.; Niehaus | 2019 | Universal Basic Income in the Developing World | doi:10.1146/annurev-economics-080218-030229 | yes |
| ghatak-maniquet-2019 | Ghatak; M.; Maniquet | 2019 | Universal Basic Income: Some Theoretical Aspects | doi:10.1146/annurev-economics-080218-030220 | yes |
| jones-marinescu-2022 | Jones; D.; Marinescu | 2022 | The Labor Market Impacts of Universal and Permanent Cash Transfers: Evidence from the Alaska Permanent Fund | doi:10.1257/pol.20190299 | yes |
| vivalt-2024-openresearch | Vivalt; E.; Rhodes | 2024 | The Employment Effects of a Guaranteed Income: Experimental Evidence from Two U.S. States | doi:10.3386/w32719 | yes |
| bartik-2024-openresearch | Bartik; A. W.; Broockman | 2024 | The Impact of Unconditional Cash Transfers on Consumption and Household Balance Sheets: Experimental Evidence from Two US States | doi:10.3386/w32784 | yes |
| miller-2024-openresearch-health | Miller; S.; Rhodes | 2024 | Does Income Affect Health? Evidence from a Randomized Controlled Trial of a Guaranteed Income | doi:10.3386/w32711 | yes |
| egger-2022-ge-kenya | Egger; D.; Haushofer | 2022 | General Equilibrium Effects of Cash Transfers: Experimental Evidence from Kenya | doi:10.3982/ECTA17945 | yes |
| west-2024-seed | West; S.; Castro | 2023 | Impact of Guaranteed Income on Health, Finances, and Agency: Findings from the Stockton Randomized Controlled Trial | doi:10.1007/s11524-023-00723-0 | yes |
| kangas-2021-finland | Kangas; O.; Jauhiainen | 2021 | Experimenting with Unconditional Basic Income: Lessons from the Finnish BI Experiment 2017-2018 | doi:10.4337/9781839104855 | yes |
| todeschini-bmincome-2020 | Riutort, S.; Laín, B.; Julià, A. | 2023 | Basic Income at Municipal Level: Insights from the Barcelona B-MINCOME Pilot | doi:10.1515/bis-2021-0047 | yes |
| arcelus-bade-2015-rgi | De la Rica, S.; Gorjón, L. | 2019 | Assessing the impact of a minimum income scheme: the Basque Country case | doi:10.1007/s13209-019-00203-2 | yes |
| sutherland-figari-2013-euromod | Sutherland; H.; Figari | 2013 | EUROMOD: the European Union tax-benefit microsimulation model | doi:10.34196/ijm.00075 | yes |
| kaplan-moll-violante-2018-hank | Kaplan; G.; Moll | 2018 | Monetary Policy According to HANK | doi:10.1257/aer.20160042 | yes |
| auclert-rognlie-straub-2024 | Auclert; A.; Rognlie | 2024 | The Intertemporal Keynesian Cross | doi:10.1086/731409 | yes |
| saez-2002-optimal-transfers | Saez; E. | 2002 | Optimal Income Transfer Programs: Intensive versus Extensive Labor Supply Responses | doi:10.1162/003355302760193959 | yes |
| guerreiro-rebelo-teles-2022-robots | Guerreiro; J.; Rebelo | 2022 | Should Robots Be Taxed? | doi:10.1093/restud/rdab019 | yes |
| diamond-mcquade-qian-2019-rent | Diamond; R.; McQuade | 2019 | The Effects of Rent Control Expansion on Tenants, Landlords, and Inequality: Evidence from San Francisco | doi:10.1257/aer.20181289 | yes |
| fack-2006-housing-benefits | Fack, G. | 2006 | Are housing benefit an effective way to redistribute income? Evidence from a natural experiment in France | doi:10.1016/j.labeco.2006.01.001 | yes |
| boe-ce-1978 | Cortes Generales | 1978 | Constitución Española (BOE-A-1978-31229) | https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229 | yes |
| boe-imv-2021 | Jefatura del Estado | 2021 | Ley 19/2021, de 20 de diciembre, por la que se establece el ingreso mínimo vital (BOE-A-2021-21007) | https://www.boe.es/buscar/act.php?id=BOE-A-2021-21007 | yes |
| boe-irpf-2006 | Jefatura del Estado | 2006 | Ley 35/2006, de 28 de noviembre, del Impuesto sobre la Renta de las Personas Físicas (BOE-A-2006-20764) | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 | yes |
| boe-vivienda-2023 | Jefatura del Estado | 2023 | Ley 12/2023, de 24 de mayo, por el derecho a la vivienda (BOE-A-2023-12203) | https://www.boe.es/buscar/act.php?id=BOE-A-2023-12203 | yes |
| boe-lofca-1980 | Jefatura del Estado | 1980 | Ley Orgánica 8/1980, de 22 de septiembre, de Financiación de las Comunidades Autónomas (BOE-A-1980-21166) | https://www.boe.es/buscar/act.php?id=BOE-A-1980-21166 | yes |
| eu-reg-883-2004 | European Parliament and Council | 2004 | Regulation (EC) No 883/2004 on the coordination of social security systems | https://eur-lex.europa.eu/eli/reg/2004/883/oj | yes |
| eu-ai-act-2024 | European Parliament and Council | 2024 | Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | yes |
