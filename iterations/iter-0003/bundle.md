# Research plan bundle — iter-0003

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
2. **Guaranteed Minimum Income (*Ingreso Mínimo Vital*, IMV & *Rentas Mínimas Autonómicas*):** Means-tested, household-based top-up transfers subject to ex-post income verification, complex household unit definitions, and 100% (or near-100%) phase-out rates that create severe marginal effective tax rate (METR) poverty traps and massive non-take-up (56% for baseline IMV, 70% for the child poverty supplement CAPI [@boe-imv-2021; @airef-opinion-imv-2023; @airef-opinion-imv-2024]).
3. **Negative Income Tax (NIT):** A tax-administered transfer that is economically equivalent to a UBR + flat/progressive income tax in static net fiscal terms, but differs in disbursement timing, intra-household distribution (individual monthly liquidity vs. annual household tax filing), and administrative take-up [@saez-2002-optimal-transfers; @ghatak-maniquet-2019].

## 3. Conditional AI Labor-Displacement Scenarios (S1–S3)
Following `D-006`, the research plan avoids assuming an unquantified "end of work" and instead evaluates policy designs across three formal macroeconomic and labor-market scenarios [@acemoglu-2024-macro-ai; @korinek-suh-2024]:

| Parameter | **S1: Moderate Polarization** | **S2: Severe Displacement** | **S3: Structural Compression** |
|---|---|---|---|
| **Time Horizon** | 3–5 years | 5–10 years | 8–15 years |
| **Labor Share Shift ($\Delta s_L$)** | $-2.5$ pp of GDP | $-7.0$ pp of GDP | $-15.0$ pp of GDP |
| **Displaced FTE Share** | $8\%$ of hours worked | $20\%$ of hours worked | $35\%$ of hours worked |
| **Primary Shock Channel** | Routine clerical, translation, junior coding, customer support | Broad administrative, legal/accounting, mid-tier services, logistics | Pervasive autonomous agent substitution across cognitive & service work |
| **Fiscal Baseline Impact** | Mild IRPF/cotizaciones drag; manageable within reformed IMV + IRPF | Major erosion of payroll & middle-bracket IRPF (-11.55% of GDP revenue loss); requires capital/IVA shift | Structural collapse of payroll tax base; requires AI-rent, corporate surplus & wealth capture |

## 4. Reference Parameter Baselines for Cross-Module Coherence
All modules calibrate against a harmonized menu of three UBR benefit tiers (expressed in 2026 euros per month, indexed to CPI/ECV thresholds), with child (<18) benefits pegged to a consistent 40% equivalence weight ($\alpha_{\text{child}} = 0.40$) derived from the modified OECD scale:
- **Tier A (Partial / Floor UBR, S1 target):** €600/month per adult (€240/month per minor $<18$), approximating the individual *Ingreso Mínimo Vital* guaranteed threshold, paired with a **No-Loser Guarantee**, a *Complemento Monoparental y de Primera Infancia*, and a tiered *Complemento Universal por Discapacidad* (+25% to +100% per RD 888/2022) for households whose existing contributory, minimum income, or disability entitlements exceed UBR (`M02`, `M07`, `M14`).
- **Tier B (Poverty-Line UBR, S2 target):** €900/month per adult (€360/month per minor), anchored to 60% of Spanish median equivalized disposable income (AROPE at-risk-of-poverty line from INE's *Encuesta de Condiciones de Vida*).
- **Tier C (Full AI-Dividend UBR, S3 target):** €1,200/month per adult (€480/month per minor), calibrated to structural labor-income replacement under Scenario S3. Supported by broad-base corporate automation surplus taxes and capital levies, with the Sovereign AI Dividend Fund serving as an intergenerational stabilization buffer yielding 0.5–0.8% of GDP/year (`M03`, `M16`).

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

## 1. Task-Based AI Exposure, Spanish Labor Institutions, & Scenario Projections (`M01`, `M08`, `M16`)
- **Occupational Mapping & Task Weights:** Crosswalk US O*NET task exposure indices (Eloundou et al. $\beta$-exposure [@eloundou-2024-gpts], Felten AIOE [@felten-2021-aioe], Webb patent-task overlap [@webb-2020-ai], and ILO Gen-AI scores [@gmyrek-ilo-2023]) to ISCO-08 and Spain's 3-digit *Clasificación Nacional de Ocupaciones* (CNO-11) using INE *Encuesta de Población Activa* (EPA) microdata and European Skills/Competences (ESCO) task weights [@albanesi-2023-ai-europe].
- **Spanish Institutional Adjustment Channels:** Model how sector-level collective bargaining (*convenios colectivos* with *ultraactividad* under *Real Decreto-ley 32/2021* [@boe-rdl-32-2021-reforma-laboral]), statutory SMI floors, and firm-size adoption lags (from INE *Encuesta sobre el uso de TIC y comercio electrónico en las empresas*, ETICCE) channel AI substitution into intermittent open-ended contract inactivity (*pases a inactividad de fijos discontinuos* in MCVL) and partial-unemployment ERTE/RED mechanisms rather than frictionless downward nominal wage cuts [@bentolila-2012-dual-spain].
- **Sequential Decomposition Protocol (Avoiding Double-Counting):**
  1. *Step 1 (Demand-Side Involuntary Displacement):* Calibrate an Acemoglu-Restrepo task-allocation framework [@acemoglu-restrepo-2019; @acemoglu-2024-macro-ai] to Spanish Contabilidad Nacional and MCVL longitudinal records, projecting involuntary displacement hazards, wage-bill compression, and employer Social Security payroll revenue erosion across **S1** ($\Delta s_L = -2.5$ pp), **S2** ($-7.0$ pp), and **S3** ($-15.0$ pp) [@korinek-suh-2024; @cazzaniga-imf-2024]. Pre-trend balance and shift-share IV orthogonality are tested per Borusyak, Hull, & Jaravel [@borusyak-2022-shift-share].
  2. *Step 2 (Supply-Side Behavioral Response):* Apply structural discrete-choice and collective labor-supply elasticities (`M08`, `M14`) to the post-displacement counterfactual market income distribution.

## 2. Static & Behavioral Tax-Benefit Microsimulation (`M02`, `M03`, `M07`, `M09`, `M14`)
- **EUROMOD-Spain Backbone & Counterfactual Post-Displacement Loop:** Implement UBR Tiers A (€600/€240), B (€900/€360), and C (€1,200/€480) inside EUROMOD-Spain [@sutherland-figari-2013-euromod] running on the *Panel de Hogares* (IEF/AEAT/INE) and ECV, supplemented by the *Muestra de Declarantes de IRPF* for top-tail Pareto calibration. Crucially, EUROMOD-Spain runs directly on counterfactual post-displacement wage and employment distributions generated dynamically by M01/HANK across S1, S2, and S3, rather than static historical survey weights.
- **Status-Quo Budget Neutrality & Consolidated AP Fiscal Bridge:** Total post-reform revenues must preserve 100% of baseline public services (~€125B/year) PLUS gross UBR outlays minus abolished non-contributory cash transfers (`M07`). Under Scenario S2, the $-7.0$ pp labor share contraction erodes baseline payroll and IRPF revenue by $11.55\%$ of GDP; the fiscal bridge explicitly covers this gap by expanding corporate automation surplus taxes (`M16`), consumption taxes, and net wealth levies. Contributory pensions above the UBR floor (~5.5–6.0% of GDP) are preserved under a Dual-Pillar structure with an explicit *Complemento de Neutralidad Fiscal* ensuring zero disposable-income loss for any pensioner or vulnerable recipient (`M07`). LIRPF Art. 20 (earned-income reduction) and Art. 84 (joint-filing reduction) are folded into the unified schedule [@boe-irpf-2006].
- **Indirect Tax & Inflation Deflation:** Estimate a Quadratic Almost Ideal Demand System (QUAIDS) on EPF to model behavioral consumption responses to IVA base broadening [@boe-iva-1992], deflating post-reform disposable income by household-specific COICOP price indices to evaluate real poverty (AROPE/FGT) and inequality (Gini/Atkinson).

## 3. Open-Economy Currency-Union HANK General-Equilibrium Closure (`M03`, `M04`, `M05`, `M16`, `M17`)
- **Monetary Union HANK Specification:** Calibrate a two-sector (tradable vs. non-tradable/housing) open-economy HANK model for Spain [@kaplan-moll-violante-2018-hank; @auclert-rognlie-straub-2024; @gali-monacelli-2005-soe] with area-wide ECB Taylor-rule response (Spain weight ~10%), Walters real-interest-rate dynamics, terms-of-trade competitiveness channels, and endogenous Bonos-Bund sovereign spread feedback.
- **Dual External Leakage & Fiscal Rules:** Account for Balance of Payments leakage from both household tradable consumption imports (by decile) and intermediate business imports of foreign AI and cloud compute infrastructure. Embed the reformed EU fiscal governance framework (*Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework]) and Spain's *Ley Orgánica 2/2012* (LOEPSF [@boe-loepsf-2012]), verifying the multi-annual Net Primary Expenditure trajectory.
- **Four-Stage Iterative Micro-Macro Closure Pipeline:**
  1. *Handoff 1 (Macro to Micro):* `M01` scenario vectors project occupational displacement and market wage-bill compression onto micro-records.
  2. *Handoff 2 (Micro Equilibrium):* EUROMOD iterates with `M08` labor supply and `M03` ETI parameters [@almunia-lopez-rodriguez-2019-eti] to solve for the consolidated revenue-neutral tax schedule.
  3. *Handoff 3 (Micro to Macro):* Decile net transfers, effective marginal tax rates, and labor-supply shifts feed into HANK (`M04`) and the spatial housing model (`M05`) to solve for equilibrium wages, non-tradable CPI, urban rental pass-through, and real GDP.
  4. *Handoff 4 (Macro Feedback Loop):* Equilibrium price and income vectors feed back into EUROMOD via a Gauss-Seidel fixed-point algorithm until the structural primary balance converges within $\pm 0.05\%$ of GDP across S1, S2, and S3.

## 4. Multi-Level Experimental & Quasi-Experimental Identification (`M05`, `M08`, `M10`, `M15`)
- **Two-Stage Saturation Cluster Design with SUTVA Buffer Zones:** Combine individual-level randomization with $J = 60\text{–}80$ spatial clusters (30–40 treated vs. 30–40 matched control units) defined as economically self-contained small municipalities (1,500–5,000 residents) or transit-bounded urban districts. To eliminate spatial spillovers and satisfy the Stable Unit Treatment Value Assumption (SUTVA), enforce mandatory geographic buffer zones ($\ge 2\text{--}5$ km in rural/peri-urban areas; donut matching in urban districts) per Baird et al. [@baird-2018-interference] and Duflo, Glennerster, & Kremer [@duflo-2007-randomization].
- **Randomized Benefit Clawback Arm & Bunching Econometrics:** Replace unconstitutional randomized tax hikes with randomized benefit phase-out rates ($0\%$, $38\%$, $50\%$) capped at the gross grant ($Y^* = \text{UBR}/\tau_{\text{clawback}}$), legally identifying compensated substitution elasticities across income brackets without violating Arts. 14 and 31.1 CE [@boe-ce-1978]. A pre-registered bunching estimator (Saez [@saez-2010-bunching]; Chetty et al. [@chetty-2012-bounds]) estimates local substitution elasticities around $Y^*$, while upper-decile tax responses are identified quasi-experimentally from historical administrative IRPF panel reforms (`M08`).
- **Structural Parameter Transportability Equations:** Decompose historical trial effect sizes [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health; @kangas-2021-finland; @jones-marinescu-2022] into permanent compensated wage ($\varepsilon^c$) and income ($\eta$) elasticities vs. Frisch intertemporal substitution ($\varepsilon^{\text{Frisch}}$) per MaCurdy [@macurdy-1981-labor-supply] and Blundell & MaCurdy [@blundell-macurdy-1999-labor-supply], adjusted for trial duration, benefit withdrawal rates, and labor-demand slack under S1–S3.

## 5. Constitutional, Statutory, and Political-Economy Veto Analysis (`M06`, `M11`, `M12`, `M13`)
- **Bifurcated Legal Architecture & Competence Framework:** Ground State competence in Arts. 149.1.1, 149.1.14, and 149.1.17 CE (supported by TC judgments STC 158/2021 [@tc-stc-158-2021-imv] and STC 19/2024 [@tc-stc-19-2024-imv-foral]). Harmonize regional financing via *Ley 22/2009* [@boe-ley-financiacion-ccaa-2009] and the Basque/Navarre Foral Treaties [@boe-concierto-vasco-2002; @boe-convenio-navarra-1990], treating UBR as a non-assumed State power (*carga no asumida*) under the Basque *Cupo* and Navarrese *Aportación* [@beramendi-2012-inequality].
- **EU Law Coordination & Schumacker Doctrine:** Anchor non-contributory cash transfers under Directive 2004/38/EC social assistance to manage Regulation (EC) No 883/2004 exportability risks. Extend Tax-Benefit Symmetry to seasonal and frontier EU cross-border workers paying Non-Resident Income Tax (*Impuesto sobre la Renta de No Residentes*, IRNR) to satisfy CJEU *Schumacker* doctrine (Case C-279/93 [@cjeu-c-279-93-schumacker]) and Art. 45 TFEU.
- **Bicameral Veto Players & Social Dialogue:** Model legislative feasibility using Tsebelis's [@tsebelis-2002-veto-players] veto-player framework across both the Congreso and the Senado (including the Senate's absolute veto over expenditure ceilings under LOEPSF Art. 15), formalizing tripartite social dialogue under Art. 7 CE with trade unions and employer associations [@vanderborght-2006-trade-unions; @vlandas-2019-politics-ubi].
- **Conjoint Survey & Coalition Modeling:** Pair CIS microdata with a pre-registered conjoint experiment ($N = 3,500$) testing multidimensional UBR packages across Spanish partisan, union, and territorial cleavages.


<!-- FILE: plan/modules/M01-ai-labor-displacement.md -->
---
id: M01
title: AI labor displacement and macroeconomic scenarios
status: draft
locked: false
depends_on: [M08, M16]
covers: [F01]
feeds_chapters: [1, 2]
last_iteration: 2
---
# M01 · AI labor displacement and macroeconomic scenarios

## 1. Why this matters
The case for a Universal Basic Rent in Spain rests on whether generative and agentic AI produce a qualitatively different labor shock than previous automation waves [@acemoglu-restrepo-2019; @eloundou-2024-gpts; @albanesi-2023-ai-europe]. If AI substitution outpaces task reinstatement across clerical, professional, and service occupations, Spain faces simultaneous compression of household wage income and erosion of the IRPF and Social Security payroll tax bases (`M03`, `M16`). Crucially, because Spanish labor institutions feature binding collective bargaining agreements and a high share of micro-enterprises, task exposure does not translate directly into downward nominal wage cuts; instead, it triggers intermittent employment inactivity and structural underemployment [@bentolila-2012-dual-spain].

## 2. Research questions
- **RQ-M01-01**: What share of Spanish full-time equivalent (FTE) employment and aggregate wage bill in 3-digit CNO-11 occupations is exposed to net displacement versus task reinstatement under AI scenarios S1, S2, and S3 once collective-bargaining wage floors and SME adoption lags are accounted for?
  - *Hypothesis:* While gross task exposure exceeds 45% in cognitive occupations, net FTE displacement in Spain is 8% in S1 ($\Delta s_L = -2.5$ pp), 20% in S2 ($\Delta s_L = -7.0$ pp), and 35% in S3 ($\Delta s_L = -15.0$ pp), with displacement concentrating in intermittent contract inactivity (*pases a inactividad de fijos discontinuos*) and non-renewal of temporary/part-time hours under *Real Decreto-ley 32/2021* [@boe-rdl-32-2021-reforma-laboral].
- **RQ-M01-02**: How do combined TFP growth trajectories, service-sector marginal-cost reductions, and outbound foreign AI-rent flows determine net payroll tax (*cotizaciones sociales*) and IRPF revenue drag across Spanish Autonomous Communities?
  - *Hypothesis:* Each 1 percentage-point drop in the labor income share reduces combined Spanish IRPF and Social Security revenues by 1.25–1.40 percentage points under S1, but expands to >1.65 percentage points under S2 and S3 as cognitive workers in service-intensive urban regions (Madrid, Catalonia) face displacement and corporate surpluses accrue to foreign-domiciled AI foundation-model providers. In Scenario S2 ($\Delta s_L = -7.0$ pp), this triggers an aggregate baseline tax revenue collapse of 11.55% of GDP (~€173B/year), requiring direct macroeconomic feedback into EUROMOD-Spain (`M03`) to finance baseline public services and UBR outlays.

## 3. State of knowledge
Task-based frameworks show that automation depresses the labor share whenever displacement effects exceed productivity and new-task reinstatement effects [@acemoglu-restrepo-2019; @acemoglu-2024-macro-ai]. Empirical studies across European economies [@albanesi-2023-ai-europe; @gmyrek-ilo-2023] indicate that while early AI was modestly employment-enhancing for highly skilled workers, generative and agentic AI directly target non-routine cognitive and administrative tasks [@eloundou-2024-gpts; @felten-2021-aioe; @webb-2020-ai; @cazzaniga-imf-2024]. In Spain's institutional context, labor-market duality and sectoral wage floors mean technological shocks adjust through contract duration, fixed-discontinuous inactivity spells, and hours reductions rather than real wage flexibility [@bentolila-2012-dual-spain; @boe-rdl-32-2021-reforma-laboral].

## 4. Spain context & data sources
- **Labor Microdata:** INE *Encuesta de Población Activa* (EPA) quarterly rotating panel (occupational flows at 3-digit CNO-11, contract type, hours, tenure).
- **Social Security Histories:** *Muestra Continua de Vidas Laborales* (MCVL, Seguridad Social) matched to AEAT Form 190 tax withholdings for longitudinal wage, contribution base, and *fijos discontinuos* inactivity trajectories.
- **Enterprise & Adoption Microdata:** INE *Encuesta sobre el uso de TIC y comercio electrónico en las empresas* (ETICCE, firm-level AI software/hardware adoption by size class) and *Encuesta Anual de Estructura Salarial* (EAES).

## 5. Methods & identification
1. **Gross Exposure vs. Net Spanish Displacement Crosswalk:** Map O*NET task scores [@eloundou-2024-gpts; @felten-2021-aioe; @webb-2020-ai] to ISCO-08 and CNO-11 using ESCO/PIAAC task weights. Scale gross occupational exposure by firm-size AI adoption rates from ETICCE and Spanish collective-bargaining coverage rates (*convenios sectoriales*) to derive net displacement hazards.
2. **Identification Strategy & Bounds:** Estimate baseline S1 displacement elasticities in MCVL/EPA using a shift-share IV design interacting pre-shock occupational exposure shares with sectoral AI software/compute investment, verifying shock-level balance and pre-trend orthogonality per Borusyak, Hull, & Jaravel [@borusyak-2022-shift-share]. For S2 and S3, bound agentic displacement using structural task-cost replacement functions [@korinek-suh-2024] rather than extrapolating historical IV trends.
3. **Macroeconomic Scenario Vectors (S1–S3):** Pair labor-share shifts ($\Delta s_L \in \{-2.5, -7.0, -15.0\}$ pp) with explicit TFP growth bands (0.5–1.8% annually), marginal-cost deflation curves in service sectors, and domestic corporate operating surplus vs. outbound foreign compute royalty splits for `M03`, `M04`, and `M16`. Explicitly output counterfactual post-displacement wage and employment distributions across CNO-11 deciles to feed EUROMOD-Spain (`M03`, `M09`), closing the macro-to-micro fiscal loop under the 11.55% of GDP baseline revenue shock.

## 6. Pilot implications
- **Municipal Tier:** Select pilot municipalities spanning high cognitive/back-office exposure (e.g. service-intensive suburban metropolitan belts) versus manufacturing/agricultural controls, tracking local employment transitions via monthly MCVL affiliation data.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** Compare Autonomous Communities with high service/headquarter concentration under *Régimen Común* (Madrid, Catalonia) against industrial-exporting regions under *Régimen Foral* (Basque Country / Navarre), utilizing foral corporate tax data to evaluate regional AI productivity capture.
- **National Tier:** Establish an AIReF-certified composite index (EPA cognitive displacement + MCVL contribution bases) to monitor realized displacement and inform statutory fast-track parliamentary reviews (`M17`).

## 7. Risks, counterarguments & open issues
- **Counterargument (Acemoglu Productivity Modesty):** Acemoglu [@acemoglu-2024-macro-ai] argues macroeconomic TFP gains from AI will remain below 1% over a decade, implying slow displacement. *Mitigation:* Explicitly bracket S1 (slow/moderate, consistent with Acemoglu) against S2 and S3 [@korinek-suh-2024], pre-committing UBR scale-up to observable displacement triggers rather than fixed calendar dates (`M17`).
- **Within-Occupation Task Reorganization:** CNO-11 codes may mask internal reorganization; addressed by tracking worker-level daily contribution bases in MCVL.

## 8. Deliverables & effort
- CNO-11 AI Exposure & Net Displacement Calibration Pipeline for Spain (EPA + MCVL + ETICCE).
- Complete S1–S3 Scenario Parameter Vectors for EUROMOD (`M03`, `M09`) and HANK (`M04`). (Effort: 6 person-weeks).


<!-- FILE: plan/modules/M02-benefit-design.md -->
---
id: M02
title: Benefit design, eligibility, and parameter architecture
status: draft
locked: false
depends_on: [M03, M07, M09]
covers: [F02]
feeds_chapters: [3]
last_iteration: 2
---
# M02 · Benefit design, eligibility, and parameter architecture

## 1. Why this matters
Small changes in benefit architecture—individual versus household unit, adult versus minor amounts, age thresholds, and indexation rules—determine whether UBR eliminates poverty and intra-household dependency or becomes fiscally unviable [@van-parijs-vanderborght-2017; @hoynes-rothstein-2019]. In Spain, where the *Ingreso Mínimo Vital* (IMV) suffers from complex household-unit assessments, cohabitation verification penalties, and severe non-take-up (56% for baseline IMV, 70% for CAPI [@boe-imv-2021; @airef-opinion-imv-2023]), strict adherence to the unconditional individual entitlement principle (`D-001`) is essential.

## 2. Research questions
- **RQ-M02-01**: How do strictly individual UBR schedules (Tier A: €600 adult / €240 minor; Tier B: €900 adult / €360 minor; Tier C: €1,200 adult / €480 minor, maintaining a consistent 40% child equivalence weight) compare against household-equivalized means-tested schedules in reducing severe material deprivation without creating cohabitation penalties, when paired with dedicated single-parent and disability supplements?
  - *Hypothesis:* An individual Tier B UBR (€900/adult, €360/minor) paired with the `M07` No-Loser Guarantee, an explicit *Complemento Monoparental y de Primera Infancia* (+€150–€200/month holding single mothers harmless against IMV 22% bonus + CAPI baselines), and a tiered *Complemento Universal por Discapacidad* (+25% to +100% per RD 888/2022 [@boe-rd-888-2022-discapacidad; @puig-segura-2021-discapacidad]) eliminates cohabitation penalties entirely while achieving superior poverty eradication per net euro relative to household-based top-ups.
- **RQ-M02-02**: What indexation formula—essential-basket CPI, headline CPI, or constant-tax CPI (*Índice de Precios de Consumo a Impuestos Constantes*, IPC-IC) capped by nominal GDP-per-capita growth—best preserves real living standards across S1–S3 without triggering unlegislated fiscal drag or fiscal self-indexation under `M03`?
  - *Hypothesis:* Indexing UBR benefits to IPC-IC capped by nominal per-capita GDP growth, synchronized with statutory adjustments to `M03` IRPF marginal rate brackets, prevents fiscal self-indexation during IVA base-broadening phases while guaranteeing an untaxable subsistence floor.

## 3. State of knowledge
Theoretical public economics demonstrates that unconditional individual transfers avoid the high marginal effective tax rates (METRs) and invasive monitoring costs of means-tested programs, at the cost of higher gross fiscal outlays that must be recouped through progressive taxation [@ghatak-maniquet-2019; @saez-2002-optimal-transfers; @van-parijs-vanderborght-2017]. Empirical evidence from Spanish minimum income schemes shows that household-level means testing penalizes young adult emancipation, disincentivizes shared housing, and creates severe administrative exclusion [@airef-opinion-imv-2023; @todeschini-bmincome-2020].

## 4. Spain context & data sources
- **Poverty & Living Standards Benchmarks:** INE *Encuesta de Condiciones de Vida* (ECV) AROPE thresholds (60% and 40% of median equivalized disposable income across Spain and by Autonomous Community).
- **IMV Statutory Baseline:** *Ley 19/2021* [@boe-imv-2021] guaranteed amounts, *Complemento de Ayuda para la Infancia* (CAPI), and disability provisions under *Real Decreto 888/2022* [@boe-rd-888-2022-discapacidad].
- **Demographics:** INE *Censo de Población* and *Padrón Continuo* (adult/minor age cohorts, household size distributions).

## 5. Methods & identification
1. **Parametric Dominance Grid in EUROMOD-Spain:** Simulate a $3 \times 3 \times 2$ design grid in EUROMOD [@sutherland-figari-2013-euromod] testing Tiers A/B/C $\times$ child equivalence weight $\alpha_{\text{child}} \in \{0.30, 0.40, 0.50\}$ $\times$ youth adult transition age $\{18, 23\}$. Incorporate the *Complemento Monoparental* and the three-tiered *Complemento por Discapacidad* (+25%, +50%, +100%) to measure cohabitation penalty rates and disposable income gains across household types.
2. **Synchronized Tax-Benefit Indexation:** Model simultaneous indexation of UBR benefit amounts and `M03` IRPF marginal tax brackets under headline CPI vs. IPC-IC, simulating stagflationary supply shocks (`M17` Stress 1).

## 6. Pilot implications
- **Municipal Tier:** Test individual Tier A (€600/€240) vs. Tier B (€900/€360) disbursement against B-MINCOME's household-conditioned modalities [@todeschini-bmincome-2020], evaluating youth emancipation, single-parent stability, and household formation.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** Compare uniform nominal regional amounts in a common-regime territory against foral territories (Basque Country / Navarre) testing synchronized regional IRPF bracket indexing and regional supplements (`M07`).
- **National Tier:** Phase from Tier A (€600, S1) to Tier B (€900, S2) and Tier C (€1,200, S3) governed by AIReF-certified evaluations informing statutory fast-track parliamentary ratifications (`M17`).

## 7. Risks, counterarguments & open issues
- **Counterargument (Single-Adult Adequacy):** Individual transfers ignore household economies of scale in private housing, potentially leaving single adults living alone vulnerable in expensive cities. *Mitigation:* Address single-adult shelter costs through `M05` public social housing priority and targeted rental supply rather than cash cohabitation surcharges, which reintroduce invasive *Padrón* cohabitation inspections (`M12`).

## 8. Deliverables & effort
- Parameter Specification Matrix & EUROMOD input rulefiles for Tiers A, B, and C with child, single-parent, and disability supplements.
- Adequacy vs. Net Cost Pareto frontier curves and indexation sensitivity for Chapter 3. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M03-fiscal-financing.md -->
---
id: M03
title: Fiscal financing and tax-transfer integration
status: draft
locked: false
depends_on: [M01, M02, M07, M09, M16]
covers: [F03]
feeds_chapters: [4]
last_iteration: 2
---
# M03 · Fiscal financing and tax-transfer integration

## 1. Why this matters
Gross cost is the most frequent critique of UBR in Spain: paying €900/month to ~40 million adults and €360/month to ~8 million minors implies a gross outlay near €466 billion (~30% of Spanish GDP). However, economic feasibility depends on **status-quo budget neutrality**—ensuring that total post-reform tax revenues fund 100% of existing public services (health, education, general administration, totaling ~€125B/year in IRPF collections [@boe-irpf-2006]) PLUS gross UBR outlays minus genuinely abolished non-contributory cash transfers (`M07`), after integrating UBR into IRPF, folding regressive tax allowances, and reforming consumption and capital taxes [@hoynes-rothstein-2019; @saez-2002-optimal-transfers]. Crucially, under severe AI displacement (Scenario S2, $\Delta s_L = -7.0$ pp), the baseline tax system suffers an endogenous 11.55% of GDP revenue collapse (~€173B/year); M03 therefore cannot assume static baseline receipts, but must directly close the macro-micro fiscal loop using M01's counterfactual post-displacement earnings distributions.

## 2. Research questions
- **RQ-M03-01**: What progressive IRPF marginal rate schedule ($t \in [38\%, 52\%]$) and status-quo breakeven income percentile achieve full budget neutrality in Spain for Tiers A, B, and C once the IRPF *mínimo personal y familiar* (Arts. 56–61 LIRPF), the earned-income reduction (Art. 20 LIRPF), and joint-filing allowances (Art. 84 LIRPF) are integrated alongside the `M07` Dual-Pillar pension offset, when accounting for the S2 11.55% GDP baseline revenue contraction?
  - *Hypothesis:* Enforcing strict status-quo budget neutrality (preserving baseline €125B IRPF public financing) on counterfactual post-displacement earnings places the net-disposable-income breakeven point ($T_{\text{new}} - T_{\text{old}} = \text{UBR}$) at the 82nd–86th percentile of individual gross income (~€38,000–€44,000/year) under Tier B (€900/month), requiring a consolidated net financing requirement of 4.8–6.2% of GDP from base broadening and `M16` corporate automation surplus taxes to bridge the labor tax base contraction.
- **RQ-M03-02**: How do behavioural taxable income elasticities (ETI), corporate profit-sheltering under *Ley 27/2014* [@boe-sociedades-2014], and QUAIDS-estimated consumption shifts from IVA base broadening [@boe-iva-1992] affect revenue yields across AI scenarios S1–S3?
  - *Hypothesis:* Unifying the dual IRPF general and savings bases without corporate anti-deferral triggers corporate shelter leakage of 12–18% of high-income capital yields into holding companies, requiring an anti-deferral minimum tax under *Ley 27/2014* calibrated to Spanish ETI parameters [@almunia-lopez-rodriguez-2019-eti].

## 3. State of knowledge
Public finance theory establishes that a universal demogrant financed by a progressive income tax is economically equivalent to a Negative Income Tax of equal net schedule [@saez-2002-optimal-transfers; @ghatak-maniquet-2019]. Microsimulation studies using EUROMOD [@sutherland-figari-2013-euromod] show that gross-cost estimates overstate net fiscal burden by a factor of 4 to 6 [@hoynes-rothstein-2019]. However, naive models that equate $T_{\text{new}} = \text{UBR}$ with breakeven double-count pre-existing income tax revenue; true net cost must maintain pre-reform financing for general public services [@saez-2002-optimal-transfers]. Empirical estimates of the elasticity of taxable income in Spain confirm significant bunching at tax bracket kinks that must be incorporated into second-round behavioral yields [@almunia-lopez-rodriguez-2019-eti].

## 4. Spain context & data sources
- **Tax Law & Statutory Reductions:** *Ley 35/2006 del IRPF* [@boe-irpf-2006] (Art. 20 *reducción por rendimientos del trabajo*, Arts. 56–61 *mínimos personales y familiares*, Art. 84 *tributación conjunta*), *Ley 37/1992 del IVA* [@boe-iva-1992], and *Ley 27/2014 del Impuesto sobre Sociedades* [@boe-sociedades-2014].
- **Territorial Financing Framework:** *Ley 22/2009 de Financiación de las CCAA* [@boe-ley-financiacion-ccaa-2009] (50% ceded IRPF/IVA tranches), Basque *Concierto Económico* (*Ley 12/2002* [@boe-concierto-vasco-2002]), and Navarre *Convenio Económico* (*Ley 28/1990* [@boe-convenio-navarra-1990]).
- **Microdata:** IEF/AEAT *Panel de Hogares* (linked tax-census panel including non-filers), *Muestra de Declarantes de IRPF* (for top 5% Pareto fitting), and INE *Encuesta de Presupuestos Familiares* (EPF, for QUAIDS indirect tax simulation).

## 5. Methods & identification
1. **Consolidated Public Accounts Fiscal Bridge & Macro-Micro Loop:** Specify the general-government budget equation evaluated directly on counterfactual post-displacement earnings distributions from `M01`:
   $$\Delta \text{Balance} = \Delta \text{IRPF}_{\text{AEAT+CCAA}} + \Delta \text{IVA} + \text{Savings}_{\text{INSS}}(\text{M07}) + \text{AI/Capital}_{\text{M16}} - \text{Gross UBR} - \text{Baseline Tax Erosion}_{\text{S1-S3}}(\text{M01}) = 0$$
   Abolish LIRPF Arts. 20, 56–61, and 84, integrating UBR as an individual non-taxable transfer while taxing all other income from the first euro. In S2, the 11.55% of GDP baseline labor tax erosion is compensated by shifting the fiscal mix toward corporate automation surplus levies (`M16`), carbon/environmental taxes, and net wealth taxation.
2. **Behavioral ETI & Corporate Shelter Model:** Incorporate empirical Spanish ETI estimates ($\varepsilon_{\text{ETI}} \in [0.15, 0.45]$) from Almunia & Lopez-Rodriguez [@almunia-lopez-rodriguez-2019-eti] and simulate corporate holding-company shielding under *Ley 27/2014* with an anti-deferral minimum tax.
3. **QUAIDS Consumption Demand & Constant-Tax CPI:** Estimate a Quadratic Almost Ideal Demand System on EPF microdata to model price-elastic consumer demand under IVA base broadening [@boe-iva-1992], linking indexation to constant-tax CPI (IPC-IC) to prevent mechanical fiscal self-indexation (`M02`).

## 6. Pilot implications
- **Municipal Tier:** Municipal pilots cannot test income tax financing directly (limited to local fees/IBI), serving primarily to evaluate local liquidity and public service usage.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** In *Régimen Común*, test adjusting the 50% regional IRPF tariff under *Ley 22/2009* [@boe-ley-financiacion-ccaa-2009] paired with contractual top-up clawbacks; in *Régimen Foral* (Basque Country / Navarre), enact the full joint IRPF withholding schedule under autonomous tax laws (*Normas Forales del IRPF* / *Convenio Navarro* [@boe-concierto-vasco-2002; @boe-convenio-navarra-1990]).
- **National Tier:** Full AEAT monthly withholding clearing across all brackets and pension offset coordination with the Social Security budget.

## 7. Risks, counterarguments & open issues
- **Counterargument (Middle-Decile Effective Rate Hikes):** Middle-income earners (deciles 6–8) face higher marginal IRPF rates. *Mitigation:* Report transparent pre- and post-UBR net disposable income curves, showing that deciles 1–6 gain substantially and decile 7 remains net-neutral ($\pm 2\%$) while shifting financing to capital and AI rents (`M16`).

## 8. Deliverables & effort
- Consolidated Administraciones Públicas Gross-to-Net Fiscal Bridge Table (Tiers A/B/C $\times$ Scenarios S1/S2/S3).
- Statutory IRPF Reform Schedule & QUAIDS IVA Yield Model for Chapter 4. (Effort: 8 person-weeks).


<!-- FILE: plan/modules/M04-macroeconomics-eurozone.md -->
---
id: M04
title: Macroeconomic dynamics, inflation, and Eurozone constraints
status: draft
locked: false
depends_on: [M01, M03, M05, M16]
covers: [F05]
feeds_chapters: [5]
last_iteration: 1
---
# M04 · Macroeconomic dynamics, inflation, and Eurozone constraints

## 1. Why this matters
Spain is a medium-sized open economy inside the Eurozone: it cannot devalue its currency or instruct the Banco de España to monetize fiscal deficits, and it is bound by the EU's reformed fiscal governance framework (*Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework]) and domestic fiscal rules (*Ley Orgánica 2/2012*, LOEPSF [@boe-loepsf-2012]). A state-of-the-art plan must demonstrate that UBR stabilizes domestic demand during an AI-driven wage contraction without igniting non-tradable inflation, sovereign spread widening, or violating the multi-annual Net Primary Expenditure path [@kaplan-moll-violante-2018-hank; @auclert-rognlie-straub-2024; @gali-monacelli-2005-soe].

## 2. Research questions
- **RQ-M04-01**: In a small-open-economy currency-union HANK model with sticky prices and heterogeneous hand-to-mouth households, under what combinations of AI supply shocks (`M01`) and tax financing (`M03`, `M16`) does UBR stabilize aggregate demand while keeping core non-tradable inflation within $\pm 0.3$ pp of the ECB target?
  - *Hypothesis:* When UBR is 100% tax-financed under S1 and S2, the aggregate demand multiplier from redistributing toward high-MPC bottom deciles (+0.8 to +1.4% GDP) is counterbalanced by AI-driven marginal-cost reductions in tradable and digital services, preserving competitiveness—provided local urban rent capture (`M05`) is constrained.
- **RQ-M04-02**: How does the multi-annual Net Primary Expenditure Ceiling under *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] constrain the UBR rollout, and how must gross outlays be legally paired with Discretionary Revenue Measures (*Medidas Discrecionales de Ingresos*, MDI) to avoid triggering an Excessive Deficit Procedure?
  - *Hypothesis:* By formally netting gross UBR outlays against simultaneous discretionary IRPF/IVA/corporate revenue reforms (`M03`, `M16`) in the annual Stability Programme, net expenditure growth remains strictly within European Commission ceilings and prevents Bonos-Bund sovereign spread widening beyond baseline levels ($\le 85$ bps).

## 3. State of knowledge
Heterogeneous-Agent New Keynesian (HANK) models demonstrate that redistribution from low-MPC wealthy savers to high-MPC liquidity-constrained households generates robust balanced-budget multipliers [@kaplan-moll-violante-2018-hank; @auclert-rognlie-straub-2024]. In a currency union without national monetary sovereignty [@gali-monacelli-2005-soe], inflation differentials generate real-interest-rate (Walters) dynamics: domestic inflation lowers the real borrowing rate in the short term, but subsequently erodes terms-of-trade competitiveness and raises sovereign risk premia if debt sustainability is questioned [@eu-reg-2024-1263-fiscal-framework; @boe-loepsf-2012].

## 4. Spain context & data sources
- **Household Balance Sheets & Wealth:** Banco de España *Encuesta Financiera de las Familias* (EFF) for liquid/illiquid wealth distribution and hand-to-mouth shares.
- **Macro Accounts & External Sector:** INE *Contabilidad Nacional Trimestral*, Input-Output tables and Figaro inter-country tables (for import propensity by COICOP category and NACE sector), and AIReF / Banco de España fiscal projections.
- **Fiscal Governance:** *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] and *Ley Orgánica 2/2012 de Estabilidad Presupuestaria y Sostenibilidad Financiera* (LOEPSF [@boe-loepsf-2012]).

## 5. Methods & identification
1. **Small-Open-Economy Currency-Union HANK Model:** Formalize a two-sector (tradables vs. non-tradables/housing) HANK model calibrated to Spanish EFF wealth deciles and EPF consumption shares [@kaplan-moll-violante-2018-hank; @gali-monacelli-2005-soe]. Specify the ECB area-wide Taylor rule (Spain weight 10%), fixed nominal exchange rate, and endogenous Bonos-Bund spread as a function of debt-to-GDP and structural primary deficit.
2. **Dual External Leakage Accounting:** Quantify two distinct leakage channels in the Balance of Payments: (i) household consumption import leakage (high in electronics and energy; low in domestic services/food) and (ii) corporate B2B imports of foreign AI compute, cloud subscriptions, and software royalties.
3. **Four-Stage Micro-Macro Iteration (`methods.md`):** Execute the Gauss-Seidel fixed-point loop between EUROMOD (`M03`, `M09`) and HANK (`M04`) to ensure macro equilibrium prices, wages, and GDP feed back into tax-benefit revenues until convergence within $\pm 0.05\%$ of GDP.

## 6. Pilot implications
- **Municipal Tier:** High-saturation municipal pilots (`M10`) allow direct measurement of local non-tradable price responses and service multipliers, though external leakage is higher at the municipal boundary than at the national border.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** In *Régimen Común*, regional debt limits are governed by the *Fondo de Liquidez Autonómica* (FLA) and LOEPSF [@boe-loepsf-2012]; in *Régimen Foral* (Basque Country / Navarre), autonomous borrowing capacity and separate bilateral debt targets allow evaluating regional deficit-neutrality rules.
- **National Tier:** Embed macroeconomic circuit-breakers (`M17`) that pause nominal UBR step-ups if domestic core non-tradable inflation exceeds the Eurozone average by >1.5 pp.

## 7. Risks, counterarguments & open issues
- **Counterargument (Current-Account Deterioration):** Increased household liquidity could leak into imported consumer goods and foreign digital services, worsening Spain's net international investment position (NIIP). *Mitigation:* Calibrate sector-specific import propensities and evaluate how UBR-financed human capital and local service demand stimulate domestic value-added.

## 8. Deliverables & effort
- Calibrated Open-Economy Currency-Union HANK Codebase & S1–S3 Impulse Response Functions.
- EU Fiscal Governance Compliance Memo (Regulation 2024/1263 & LOEPSF) for Chapter 5. (Effort: 7 person-weeks).


<!-- FILE: plan/modules/M05-housing-rent-capture.md -->
---
id: M05
title: Housing market pass-through and landlord rent capture
status: draft
locked: false
depends_on: [M02, M04, M10, M13]
covers: [F06]
feeds_chapters: [5]
last_iteration: 2
---
# M05 · Housing market pass-through and landlord rent capture

## 1. Why this matters
Housing is the single largest threat to the real welfare impact of a cash UBR in Spain. In metropolitan areas with rigid housing supply and high tourist/seasonal rental pressure (Madrid, Barcelona, Málaga, Balearic and Canary Islands), an unconditional increase in tenant disposable income risks being partially captured by landlords through higher rents [@fack-2006-housing-benefits], converting a public transfer into private land rent and eroding living standards for middle-decile private renters (`M09`). However, rental markets are not frictionless: tenure security under *Ley 29/1994 de Arrendamientos Urbanos* (LAU Art. 9 [@boe-lau-1994]) locks in contract terms for 5 years (7 years for corporate landlords), meaning rent capture bifurcates sharply between incumbent protected tenants and new market entrants, while landlords increasingly exploit seasonal and room rental loopholes to evade statutory rent caps [@garcia-montalvo-2023-rent-controls; @jofre-monseny-2023-rent-control].

## 2. Research questions
- **RQ-M05-01**: What fraction of an unconditional cash transfer (Tiers A/B) is capitalized into higher private market rents across Spanish municipalities with low versus high housing supply elasticity, accounting for LAU Art. 9 mandatory 5-year lease stability?
  - *Hypothesis:* In supply-inelastic stressed urban zones (*zonas de mercado residencial tensionado*), rent capture on new lease contracts reaches 25–38% within 24 months, whereas incumbent tenants on active 5-year LAU contracts face near-zero short-run pass-through until lease expiration, creating a pronounced insider-outsider tenure divergence.
- **RQ-M05-02**: Which complementary housing policy package—reference rent caps under *Ley 12/2023* [@boe-vivienda-2023], closing seasonal (LAU Art. 3.2) and room rental (CC Art. 1554) loopholes, dynamic revocation of LIRPF Art. 23.2 landlord tax deductions, or municipal *tanteo y retracto* acquisitions—most effectively suppresses rent capture without shrinking rental supply?
  - *Hypothesis:* Standalone rent caps incentivize landlords to divert up to 20% of listings into unregulated seasonal and room rentals [@garcia-montalvo-2023-rent-controls; @jofre-monseny-2023-rent-control]; pairing caps with the statutory extension of price ceilings to seasonal/room leases and conditioning LIRPF Art. 23.2 landlord tax deductions (50% reduction) on verified compliance suppresses rent capture by >70% while preserving long-term supply.

## 3. State of knowledge
Empirical evaluations of housing allowances demonstrate substantial incidence on rents when rental supply is inelastic: Fack [@fack-2006-housing-benefits] finds that 50–78% of French housing benefit increases were absorbed by higher rents. In Spain, recent empirical evaluations of the Catalan rent control regime show that price ceilings lowered negotiated rents by 4–6% for covered units but reduced private rental supply by 10–15% as landlords diverted units into exempt seasonal rentals [@garcia-montalvo-2023-rent-controls; @jofre-monseny-2023-rent-control; @diamond-mcquade-qian-2019-rent]. Cash transfer trials show that portable transfers facilitate out-migration to lower-cost areas [@bartik-2024-openresearch], mitigating metropolitan pressure if geographic frictions are overcome (`M13`).

## 4. Spain context & data sources
- **Legal Framework:** *Ley 12/2023, por el derecho a la vivienda* [@boe-vivienda-2023] (*zonas tensionadas*, state rent reference index *SERPAVI*), *Ley 29/1994 de Arrendamientos Urbanos* (LAU [@boe-lau-1994]), and *Ley 35/2006 del IRPF* (Art. 23.2 landlord net rental yield reduction [@boe-irpf-2006]).
- **Administrative Microdata:** Mandatory regional rental deposit registries (*fianzas de alquiler obligatorias*): INCASÒL (Catalonia), IVIMA (Madrid), and AVRA (Andalusia); Ministry of Housing (MIVAU) SERPAVI panel; and AEAT IRPF real-estate return declarations.

## 5. Methods & identification
1. **Quasi-Experimental Pass-Through Identification:** Exploit policy discontinuities in Spanish housing demand: (i) age eligibility cutoffs in the *Bono Alquiler Joven* (€250/month cash transfer capped at age 35), (ii) municipal border discontinuities in *Ley 12/2023* stressed-zone declarations across bordering municipalities in Catalonia, and (iii) regional minimum-income housing supplement expansions in the Basque Country and Navarre.
2. **Dual-Tenure Equilibrium Model:** Formulate a structural rental market model distinguishing incumbent tenants (protected by LAU Art. 9 5-year lock-in) from new listings, explicitly incorporating contract substitution into seasonal (LAU Art. 3.2) and room rentals. Simulate dynamic landlord tax incentives under LIRPF Art. 23.2, feeding equilibrium rent vectors directly into `M09` and `M17`.

## 6. Pilot implications
- **Municipal Tier:** Track matched landlord-tenant administrative deposit microdata (INCASÒL / IVIMA / AVRA) in high-saturation pilot clusters (`M10`) against buffered control clusters, isolating the differential rent trajectory between active contracts and turnover leases.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** Compare pass-through in common-regime regions applying *Ley 12/2023* stressed zones (e.g. Catalonia) versus non-applying regions (e.g. Madrid), contrasting with Basque foral rental tax deductions.
- **National Tier:** Connect directly to the `M17` Housing Pass-Through Circuit-Breaker: if municipal rent indices exceed core CPI by >3.0 pp in stressed zones, activate immediate fiscal/regulatory levers (zeroing LIRPF Art. 23.2 landlord deductions, capping seasonal rents, and fast-tracking municipal *tanteo y retracto* acquisitions).

## 7. Risks, counterarguments & open issues
- **Counterargument (UBR Fuels Urban Rent Inflation):** Critics argue in-kind housing provision should precede cash UBR. *Mitigation:* Quantify the exact pass-through threshold and test whether portable UBR combined with seasonal-lease regulation and immediate tax conditionality protects tenant purchasing power (`M13`, `M17`).

## 8. Deliverables & effort
- Municipal Rental Supply Elasticity & Dual-Tenure Pass-Through Model for Spain.
- Housing Policy Complementarity Simulation & Regulatory Loop for Chapter 5. (Effort: 5 person-weeks).


<!-- FILE: plan/modules/M06-constitutional-eu-law.md -->
---
id: M06
title: Constitutional, competence, and EU legal architecture
status: draft
locked: false
depends_on: [M03, M07, M12, M13]
covers: [F07]
feeds_chapters: [6]
last_iteration: 2
---
# M06 · Constitutional, competence, and EU legal architecture

## 1. Why this matters
Any Spanish UBR proposal will face immediate constitutional review before the *Tribunal Constitucional* (TC) over the distribution of powers between the State and the 17 *Comunidades Autónomas*, as well as scrutiny under European Union free-movement, non-discrimination, and social-security coordination law [@boe-ce-1978; @eu-reg-883-2004; @eu-dir-2004-38-free-movement]. Furthermore, Spain's asymmetric fiscal federalism—split between the *régimen común* (*LOFCA* [@boe-lofca-1980], *Ley 22/2009* [@boe-ley-financiacion-ccaa-2009]) and the *régimen foral* (Basque *Concierto Económico* [@boe-concierto-vasco-2002] and Navarre *Convenio* [@boe-convenio-navarra-1990])—requires distinct statutory harmonization instruments to prevent territorial arbitrage and unconstitutional revenue distortions [@beramendi-2012-inequality].

## 2. Research questions
- **RQ-M06-01**: Can a national UBR be enacted in Spain via ordinary State legislation (*Ley Ordinaria* + *Ley Orgánica* coordinating LOFCA) anchored in Articles 149.1.1, 149.1.14, 149.1.17, and 41 of the Spanish Constitution without requiring constitutional reform across scenarios S1–S3, while harmonizing foral *Cupo* and *Aportación* obligations?
  - *Hypothesis:* Yes—structuring UBR as a dual instrument combining a refundable individual IRPF credit (State competence over *Hacienda general*, Art. 149.1.14 CE [@boe-ce-1978]) with a non-contributory Social Security floor (Arts. 41 and 149.1.17 CE, validated by TC doctrine in STC 158/2021 [@tc-stc-158-2021-imv] and STC 19/2024 [@tc-stc-19-2024-imv-foral]) is fully constitutional without amending the 1978 Constitution. In foral territories, classifying national UBR as a non-assumed State competence (*carga no asumida*) under the Basque *Concierto* (6.24% Cupo) and Navarre *Convenio* (1.6% Aportación) neutralizes territorial fiscal leakage while preserving foral tax autonomy.
- **RQ-M06-02**: Under European Union law (Art. 45 TFEU, Directive 2004/38/EC [@eu-dir-2004-38-free-movement], and Regulation 883/2004 [@eu-reg-883-2004]), what legal architecture prevents mandatory cross-border exportability abroad while respecting the CJEU *Schumacker* doctrine for cross-border workers?
  - *Hypothesis:* A **Bifurcated EU-Law Architecture**—legally anchoring the non-contributory cash component as general social assistance under Directive 2004/38/EC (falling strictly outside Regulation (EC) No 883/2004 Art. 3 material scope to eliminate Art. 7 mandatory exportability abroad), while extending pro-rata Tax-Benefit Symmetry to seasonal and frontier EU workers subject to Non-Resident Income Tax (*Impuesto sobre la Renta de No Residentes*, IRNR) under CJEU *Schumacker* doctrine (Case C-279/93 [@cjeu-c-279-93-schumacker])—withstands CJEU review without fiscal leakage.

## 3. State of knowledge
Spanish constitutional scholarship and landmark *Tribunal Constitucional* judgments on the *Ingreso Mínimo Vital*—specifically STC 158/2021 [@tc-stc-158-2021-imv] (upholding State legislative competence under Arts. 149.1.1 and 149.1.17 CE) and STC 19/2024 [@tc-stc-19-2024-imv-foral] (validating the transfer of administrative management to the Basque Country and Navarre)—confirm that while Autonomous Communities hold exclusive competence over regional *asistencia social* (Art. 148.1.20 CE), the State holds exclusive power to establish basic economic floors and tax-transfer integration [@boe-ce-1978]. Under EU law, CJEU jurisprudence (*Dano*, *Alimanovic*, *Commission v UK*) confirms that Member States may condition non-contributory social assistance for economically inactive Union citizens on lawful residency. For cross-border workers, Case C-279/93 (*Schumacker* [@cjeu-c-279-93-schumacker]) mandates that non-residents earning $\ge 75\text{--}90\%$ of family income in Spain must receive identical personal tax allowances to residents.

## 4. Spain context & data sources
- **Constitutional Articles:** *Constitución Española* (Arts. 9.2, 14, 31, 41, 128.2, 148.1.20, 149.1.1, 149.1.14, 149.1.17, Disposición Adicional Primera [@boe-ce-1978]).
- **Statutes & Treaties:** *LOFCA* [@boe-lofca-1980], *Ley 22/2009 de Financiación Autonómica* [@boe-ley-financiacion-ccaa-2009], *Ley 12/2002 del Concierto Vasco* [@boe-concierto-vasco-2002], *Ley 28/1990 del Convenio de Navarra* [@boe-convenio-navarra-1990], *Ley 35/2006 del IRPF* [@boe-irpf-2006], *Texto Refundido del IRNR* (*RDLeg 5/2004*), *Ley 19/2021 del IMV* [@boe-imv-2021], and EU Directive 2004/38/EC [@eu-dir-2004-38-free-movement].
- **Jurisprudence:** STC 158/2021 [@tc-stc-158-2021-imv], STC 19/2024 [@tc-stc-19-2024-imv-foral], CJEU Case C-279/93 (*Schumacker* [@cjeu-c-279-93-schumacker]), and CJEU Case C-475/03 (*Banca Popolare di Cremona* [@cjeu-c-475-03-banca-popolare-irap] on regional tax compatibility).

## 5. Methods & identification
1. **Statutory Reform Drafting Blueprint:** Draft explicit amendment clauses for (i) *Ley 35/2006* (introducing the individual refundable UBR tax credit and repealing Arts. 20, 56–61, 84), (ii) *TRLGSS* (establishing the non-contributory universal base while preserving contributory slopes `M07`), (iii) *TRIRNR* (implementing Schumacker tax parity for qualifying frontier workers), and (iv) *Ley 22/2009* [@boe-ley-financiacion-ccaa-2009] and Foral Treaties classifying UBR as a *carga no asumida*.
2. **Constitutional Scenario Mapping (S1–S3):** Map statutory anchors across scenarios: S1 relies on Arts. 149.1.14 and 149.1.17 CE; S2 utilizes LOFCA Art. 157.3 CE rebalancing as labor IRPF erodes; and S3 invokes Art. 128.2 CE (public initiative in essential resources) for sovereign compute/AI dividend fund governance (`M16`).

## 6. Pilot implications
- **Municipal Tier:** Grounded in Art. 25.2.e of *Ley 7/1985 Reguladora de las Bases del Régimen Local* [@boe-lbrl-1985] (municipal social action). Requires an explicit State statutory tax exemption in the *Ley de Presupuestos Generales del Estado* so pilot transfers are not taxed under general IRPF or counted against existing IMV eligibility.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** In *Régimen Común*, pilot implementation requires State authorization to adjust the regional IRPF scale under *Ley 22/2009*; in *Régimen Foral* (Basque Country / Navarre), the *Diputaciones Forales* possess full sovereign competence under the *Concierto Económico* [@boe-concierto-vasco-2002] to legislate both the transfer and the regional IRPF withholding tariff directly.
- **National Tier:** State *Ley Ordinaria* enacted by the *Cortes Generales*, coordinated with the *Comisión Mixta del Concierto Económico* and *Consejo de Política Fiscal y Financiera* (CPFF).

## 7. Risks, counterarguments & open issues
- **Counterargument (Infringement of EU Free Movement):** Imposing a residency requirement on inactive EU citizens could face European Commission infringement proceedings. *Mitigation:* Structure the requirement strictly in accordance with Article 24(2) of Directive 2004/38/EC, and grant immediate pro-rata tax credit status to all contributing workers under Art. 45 TFEU and the *Schumacker* doctrine (`M13`).

## 8. Deliverables & effort
- Comprehensive Constitutional & EU Law Compatibility Matrix across Municipal, Regional (Común vs. Foral), and National tiers.
- Statutory Reform Blueprint (*Anteproyecto de Ley*) for Chapter 6. (Effort: 5 person-weeks).


<!-- FILE: plan/modules/M07-welfare-benefit-integration.md -->
---
id: M07
title: Interaction with existing Spanish welfare benefits
status: draft
locked: false
depends_on: [M02, M03, M06, M09, M14]
covers: [F08]
feeds_chapters: [3]
last_iteration: 2
---
# M07 · Interaction with existing Spanish welfare benefits

## 1. Why this matters
Spain operates a fragmented patchwork of contributory and non-contributory cash benefits: the state *Ingreso Mínimo Vital* (IMV [@boe-imv-2021]), 17 distinct *Rentas Mínimas Autonómicas* (such as the Basque *RGI* and Catalan *RGC* [@airef-opinion-imv-2023]), SEPE unemployment insurance and assistance (*subsidios por desempleo* [@boe-rdl-2-2024-desempleo]), non-contributory retirement and disability pensions (*PNC*), and contributory retirement pensions under the *Texto Refundido de la Ley General de la Seguridad Social* (TRLGSS [@boe-trlgss-2015]). A scientifically rigorous integration must resolve two fiscal and legal imperatives: (i) separating absorbed non-contributory schemes from retained contributory pensions to prevent catastrophic under-costing, and (ii) establishing an inviolable **No-Loser Guarantee** ensuring zero disposable-income loss for any pensioner, disabled person, single parent, or regional minimum-income recipient.

## 2. Research questions
- **RQ-M07-01**: How do total absorbed non-contributory transfers compare against retained contributory Social Security pensions, and what is the net fiscal cost of the statutory **Complemento de Garantía de Derechos Adquiridos** under Tiers A, B, and C across S1–S3?
  - *Hypothesis:* Under Tier B (€900/adult, €360/minor), 100% of IMV, CAPI, non-contributory retirement pensions (PNC), and general SEPE *subsidios* are absorbed (~€14.5B/year savings). In contrast, contributory pensions above €900/month represent ~5.5–6.0% of GDP (~€90B/year) that remains funded by the contributory system under a **Dual-Pillar Architecture**, requiring an incremental tax-neutrality supplement (*Complemento de Neutralidad Fiscal*) of <0.5% of GDP (~€7.5B) to ensure zero net income loss after `M03` IRPF integration. For single-parent families receiving the 22% IMV bonus and CAPI, a dedicated *Complemento Monoparental y de Primera Infancia* (+€150–€200/month) prevents negative income deltas under Tier A.
- **RQ-M07-02**: How can UBR absorb SEPE unemployment assistance without stripping older workers of the vital retirement pension contribution credits granted under Art. 280 TRLGSS [@boe-trlgss-2015; @boe-rdl-2-2024-desempleo] (*subsidio para mayores de 52 años*), and how does UBR alter Marginal Effective Tax Rates (METRs)?
  - *Hypothesis:* Preserving the Art. 280 TRLGSS state-paid retirement contribution credit (*cotización asimilada al alta por jubilación* at 125% of the minimum base) as an independent entitlement alongside the UBR cash transfer eliminates the participation poverty trap (lowering METRs from 80–100% under IMV to 38–46% under UBR) while fully protecting future contributory pension accrual for displaced workers aged 52+.

## 3. State of knowledge
Evaluations of Spanish minimum income schemes highlight severe horizontal inequities across Autonomous Communities, bureaucratic overlaps between INSS, SEPE, and regional social services, and poverty traps caused by benefit withdrawal upon formal job entry [@airef-opinion-imv-2023; @todeschini-bmincome-2020]. International trials (Finland [@kangas-2021-finland] and B-MINCOME [@todeschini-bmincome-2020]) show that removing clawbacks when taking temporary work increases formal stability. However, public finance theory warns that imposing a 100% offset on pre-existing contributory entitlements violates contributory legitimacy and triggers legal challenges [@hoynes-rothstein-2019]. Furthermore, regional minimum incomes in high-benefit regions (Basque Country, Navarre) include housing allowances that exceed basic national floors, requiring top-up preservation [@arcelus-bade-2015-rgi; @beramendi-2012-inequality].

## 4. Spain context & data sources
- **Benefit Registers & Budgets:** INSS statistical yearbook (IMV, PNC, and contributory pensions), SEPE unemployment benefit files (*Ley General de la Seguridad Social* [@boe-trlgss-2015] reformed by *Real Decreto-ley 2/2024* [@boe-rdl-2-2024-desempleo]), disability certifications under *Real Decreto 888/2022* [@boe-rd-888-2022-discapacidad], and Ministry of Social Rights annual reports on *Rentas Mínimas de Inserción*.
- **Microsimulation Spine:** EUROMOD-Spain linked to ECV and MCVL for longitudinal pension entitlement modeling.

## 5. Methods & identification
1. **Four-Tier Benefit Integration Taxonomy:**
   - *Tier 1 (Fully Absorbed State Non-Contributory):* Baseline IMV, CAPI, non-contributory retirement PNC, and general SEPE *subsidios* are extinguished and absorbed into UBR.
   - *Tier 2 (Dual-Pillar Contributory Integration):* Contributory pensions and contributory unemployment insurance use UBR as the non-taxable base floor (€600/€900/€1,200), with the Social Security system paying the remaining contributory entitlement $\max(0, B_{\text{contrib}} - \text{UBR})$ with a positive marginal contributory slope. A statutory *Complemento de Neutralidad Fiscal* is applied in EUROMOD to prevent post-IRPF disposable income losses. Older unemployed workers preserve Art. 280 TRLGSS retirement pension contribution credits.
   - *Tier 3 (Universal Disability & Single-Parent Supplements):* A statutory *Complemento Universal por Discapacidad* (+25% to +100% of UBR graded by certified disability degree under RD 888/2022 [@boe-rd-888-2022-discapacidad; @puig-segura-2021-discapacidad]) replaces non-contributory invalidity PNC to cover non-discretionary economic extra costs, fully additive to UBR and distinct from SAAD in-kind care services under *Ley 39/2006* [@boe-ley-dependencia-2006]. Single-parent families receive the *Complemento Monoparental y de Primera Infancia*.
   - *Tier 4 (Statutory Regional Top-Ups):* Rather than assuming regional minimum incomes are abolished as a central dividend, Autonomous Communities establish a *Complemento Autonómico No Contributivo* preserving pre-existing regional rights and housing allowances (Basque RGI + PEV/PCV, Navarre) that exceed national UBR thresholds.
2. **Autonomous Community Windfall & Competence Clearing:** Model a bilateral clearing formula through the CPFF / *Ley 22/2009* [@boe-ley-financiacion-ccaa-2009] and the Foral Treaties [@boe-concierto-vasco-2002; @boe-convenio-navarra-1990] treating national UBR as a *carga no asumida* to hold all regional budgets and vulnerable recipients strictly harmless [@beramendi-2012-inequality].

## 6. Pilot implications
- **Municipal Tier:** Requires an explicit statutory safe-harbor provision in State and regional legislation so pilot cash transfers do not disqualify participants from pre-existing IMV, *Rentas Mínimas*, or SEPE *subsidios* during or after the pilot.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** In *Régimen Común*, regional governments can redirect their subsidiary minimum-income budgets into pilot co-financing, regional supplements, and social housing (`M05`); in *Régimen Foral* (Basque Country / Navarre), the *Diputaciones Forales* integrate the regional *RGI/PCV* top-up seamlessly into the autonomous IRPF withholding system.
- **National Tier:** Complete automated clearing between INSS, SEPE, regional social welfare agencies, and AEAT (`M12`).

## 7. Risks, counterarguments & open issues
- **Counterargument (Contributory Alienation):** Trade unions may fear UBR undermines the contributory Bismarckian social contract. *Mitigation:* The Dual-Pillar formula preserves the positive contributory slope above UBR so every contributed euro continues to raise retirement income, while Art. 280 TRLGSS pension credits are legally preserved for displaced workers aged 52+.

## 8. Deliverables & effort
- Full Spanish Welfare Integration & Fiscal Savings Schedule across 17 Autonomous Communities.
- Dual-Pillar Contributory Pension & No-Loser Guarantee Algorithm for Chapter 3. (Effort: 5 person-weeks).


<!-- FILE: plan/modules/M08-labor-supply-behavior.md -->
---
id: M08
title: Labor supply, reservation wages, and behavioral responses
status: draft
locked: false
depends_on: [M01, M02, M03, M07, M10]
covers: [F09]
feeds_chapters: [2, 7]
last_iteration: 2
---
# M08 · Labor supply, reservation wages, and behavioral responses

## 1. Why this matters
A central objection to UBR is that an unconditional income floor will induce large reductions in labor supply, exacerbating fiscal pressures (`M03`). Conversely, in an AI-disrupted labor market (`M01`) with pervasive Spanish informality, dual labor contracts (*fijos discontinuos* under *Real Decreto-ley 32/2021* [@boe-rdl-32-2021-reforma-laboral]), and complex welfare clawbacks under *Real Decreto 789/2022* [@boe-rd-789-2022-incentivo-imv], UBR may raise formal participation, eliminate the poverty trap, strengthen worker reservation wages against precarious conditions, and finance human-capital reallocation and caregiving (`M14`) [@hoynes-rothstein-2019; @vivalt-2024-openresearch].

## 2. Research questions
- **RQ-M08-01**: What are the extensive-margin (participation) and intensive-margin (hours worked) elasticities of Spanish workers across gender, age, and CNO-11 AI-exposure tiers when moving from means-tested transfers—benchmarked against the actual statutory IMV employment incentive under *Real Decreto 789/2022* [@boe-rd-789-2022-incentivo-imv]—to an IRPF-integrated UBR?
  - *Hypothesis:* Aggregate hours worked decline by less than 1.5–2.5% under Tier B, concentrated in voluntary reductions of overtime by secondary earners with young children and youth extending education, while formal extensive participation among former IMV/informal workers *increases* by 3–5 percentage points because UBR replaces the complex, delayed annual clawback of RD 789/2022 with real-time monthly certainty.
- **RQ-M08-02**: Under AI displacement scenarios S1–S3, how does UBR affect unemployment search duration, intermittent contract survival (*fijos discontinuos*), and post-displacement occupational match quality?
  - *Hypothesis:* Unconditional liquidity increases post-displacement search duration by 3–6 weeks on average, but yields a 6–10% higher re-employment wage stability in MCVL records and higher survival of solo self-employment (*autónomos*) compared to liquidity-constrained displaced workers.

## 3. State of knowledge
Recent high-powered RCTs and natural experiments demonstrate modest extensive-margin employment reductions from unconditional transfers: in OpenResearch, Vivalt et al. [@vivalt-2024-openresearch] find a 1.3 hour/week reduction and a 2 pp participation drop driven by job selectivity and education. In Alaska's permanent universal dividend, Jones & Marinescu [@jones-marinescu-2022] find zero aggregate employment decline due to local demand multipliers. In Finland [@kangas-2021-finland], replacing conditional unemployment benefits with an unconditional basic income increased formal work days once bureaucratic disincentives were removed. In Spain, the post-2021 labor reform increased the share of open-ended intermittent contracts (*fijos discontinuos*), making labor-supply adjustments occur along inactivity spell duration rather than pure binary employment [@bentolila-2012-dual-spain; @boe-rdl-32-2021-reforma-laboral].

## 4. Spain context & data sources
- **Labor Microdata:** INE *Encuesta de Población Activa* (EPA 6-quarter rotating longitudinal panel for gross worker flows), *Muestra Continua de Vidas Laborales* (MCVL linked to AEAT Form 190 withholdings, tracking contract codes 100/200/300, monthly *bases de cotización*, and *coeficiente de parcialidad*), and INE *Encuesta de Empleo del Tiempo* (EET).
- **Incentive Baseline:** *Real Decreto 789/2022* [@boe-rd-789-2022-incentivo-imv] (statutory IMV labor income exemption formulas) and AIReF IMV evaluations [@airef-opinion-imv-2023].

## 5. Methods & identification
1. **Structural Discrete-Choice Hours Model:** Estimate a discrete-choice model ($h \in \{0, 20, 30, 40\}$) on Spanish ECV + EPA flow data, identifying separate intensive ($\varepsilon^c$) and income ($\eta$) elasticities across demographic cells (youth 18–29, prime 30–51, older workers 52+), calibrated against RD 789/2022 baseline METRs [@saez-2002-optimal-transfers].
2. **Bunching & Longitudinal Discontinuity Estimation in MCVL & AEAT:** Exploit sharp kinks in the IRPF withholding tariff [@boe-irpf-2006], the RD 789/2022 wage exemption limits [@boe-rd-789-2022-incentivo-imv], and the age-52 SEPE *subsidio* threshold [@boe-trlgss-2015]. Apply the bunching estimators of Saez [@saez-2010-bunching] and Chetty et al. [@chetty-2012-bounds] around the pilot clawback kink $Y^* = \text{UBR}/\tau_{\text{clawback}}$, explicitly combining experimental clawback variation with quasi-experimental administrative IRPF panel reforms to estimate middle- and upper-decile taxable income responses.
3. **Sequential Shock Protocol (`methods.md`):** Ensure that `M01` involuntary AI displacement hazards (modeled on MCVL *pases a inactividad*) are applied first to generate counterfactual market earnings before estimating second-step voluntary labor-supply adjustments in EUROMOD.

## 6. Pilot implications
- **Municipal Tier:** Measure short-run partial-equilibrium labor supply, contract choice, and informal-to-formal transitions in treated municipal zones without tax clawback.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** In *Régimen Común*, test contractual clawback incentives; in *Régimen Foral* (Basque Country / Navarre), test the full joint UBR + IRPF marginal rate schedule to identify compensated substitution elasticities.
- **National Tier:** Link pilot participants' DNI/NIE directly to monthly Seguridad Social affiliation records (*vidas laborales*) to measure daily hours, wages, and contract transitions without survey recall bias (`M10`).

## 7. Risks, counterarguments & open issues
- **Counterargument (Compounded Substitution Effect from Financing):** A permanent national UBR raises marginal IRPF rates ($+\text{substitution effect}$), unlike pure windfall RCTs. *Mitigation:* Always simulate the combined income + marginal-tax substitution effect in EUROMOD and structural models, using transported parameters from `M15`.

## 8. Deliverables & effort
- Demographic Cell Matrix of Spanish Income & Substitution Elasticities ($\eta, \varepsilon^c$).
- Behavioral Labor-Supply Module for EUROMOD (`M03`, `M09`) and Chapter 2/7. (Effort: 6 person-weeks).


<!-- FILE: plan/modules/M09-distribution-poverty-euromod.md -->
---
id: M09
title: Distributional, poverty, and inequality microsimulation
status: draft
locked: false
depends_on: [M01, M02, M03, M05, M07, M08]
covers: [F10]
feeds_chapters: [4]
last_iteration: 2
---
# M09 · Distributional, poverty, and inequality microsimulation

## 1. Why this matters
Spain persistently exhibits one of the highest child poverty, anchored poverty, and disposable-income inequality (Gini and S80/S20) rates in Western Europe, driven by labor-market duality, cyclical unemployment volatility, and structurally weak, fragmented cash transfers for working-age households and children [@airef-opinion-imv-2023]. As AI labor displacement (`M01`) widens market-income dispersion and compresses labor shares across scenarios S1–S3, this module quantifies the exact distributional impact of UBR Tiers A, B, and C across income deciles, family structures, age cohorts, housing tenure groups, and Autonomous Communities, integrating the Status-Quo Budget Neutrality constraint (`M03`) and the Dual-Pillar pension integration (`M07`).

## 2. Research questions
- **RQ-M09-01**: What is the static and behavioral impact of UBR Tiers A, B, and C (integrated with reformed IRPF `M03`, consumption taxes, and the `M07` *Complemento de Neutralidad Fiscal*) on Spain's headline AROPE rate, severe poverty (<40% median), anchored vs. floating poverty thresholds, child poverty, Gini coefficient, and S80/S20 ratio across S1–S3?
  - *Hypothesis:* Tier B (€900/adult, €360/minor) reduces severe monetary poverty (<40% median) in Spain by >85%, cuts child monetary poverty by >72%, and lowers the disposable-income Gini coefficient by 6.2–7.5 Gini points under Scenario S2. Anchored poverty drops substantially faster than floating poverty, as the universal cash grant elevates the national median income.
- **RQ-M09-02**: Which household types, income deciles, and housing tenure cells (outright owners, mortgaged owners, subsidized renters, private-market renters) are net winners versus net contributors under the consolidated fiscal bridge (`M03`), and how does UBR affect housing-cost overburden (>40% of disposable income)?
  - *Hypothesis:* Deciles 1–7 are net financial winners on average, with breakeven occurring between the 82nd and 86th gross income percentile under Tier B; housing-cost overburden among bottom-quintile private renters drops from 43% to <18%. The `M07` *Complemento de Neutralidad Fiscal* ensures that fewer than 0.1% of households in deciles 1–5 suffer disposable income losses.
- **RQ-M09-03**: How does housing market rent pass-through (`M05`), closed-loop landlord rental income recycling, and indirect tax incidence (IVA and excise duties) erode nominal distributional gains when measuring real post-tax, post-housing disposable income and individualized intra-household poverty?
  - *Hypothesis:* In urban rental markets with high baseline rent burdens (Madrid, Barcelona, Balearic Islands), 18–35% of the gross cash transfer to low-income tenant households is captured by landlords, but closed-loop recycling into top-decile landlord taxable income (`M03`) recaptures 45–52% in progressive tax revenues. Measuring individualized poverty per Ponthieux [@ponthieux-2013-income-pooling] reveals that UBR eliminates hidden poverty for over 1.4 million dependent spouses and young adults within non-poor households.

## 3. State of knowledge
Tax-benefit microsimulation using EUROMOD [@sutherland-figari-2013-euromod] represents the international gold standard for counterfactual policy evaluation in Europe. Prior Spanish microsimulations document that while the 2021 *Ingreso Mínimo Vital* [@boe-imv-2021] significantly deepens support for the extreme poor who access it, persistent non-take-up exceeding 50% (56% for baseline IMV, 70% for CAPI [@airef-opinion-imv-2023; @airef-opinion-imv-2024]) and severe cohabitation/wealth tests leave headline child poverty and AROPE largely stagnant. Universal cash transfers fundamentally eliminate non-take-up exclusion errors (Type I errors) [@van-parijs-vanderborght-2017; @hoynes-rothstein-2019]. However, static analyses frequently omit the general-equilibrium rent-pass-through channel [@fack-2006-housing-benefits; @diamond-mcquade-qian-2019-rent], landlord capital recycling, intra-household financial pooling distortions [@ponthieux-2013-income-pooling], and the regressive incidence of indirect consumption taxes required for macroeconomic fiscal closure [@guerreiro-rebelo-teles-2022-robots; @korinek-suh-2024].

## 4. Spain context & data sources
- **Survey Microdata:** INE *Encuesta de Condiciones de Vida* (ECV / EU-SILC Spanish component), featuring regional oversampling across all 17 Autonomous Communities and panel rotation structure.
- **Administrative Tax & Social Security Microdata:** IEF/AEAT *Muestra de Declarantes de IRPF* (annual 2-million taxpayer panel) to eliminate ECV top-income underreporting and right-truncation, combined with the *Muestra Continua de Vidas Laborales* (MCVL) for labor history and contributory pension bases.
- **Regional Foral Microdata:** Dedicated provincial tax microdata from the Basque Provincial Treasuries (*Diputaciones Forales de Álava, Bizkaia, Gipuzkoa*) and Navarre under the *Concierto Económico* [@boe-concierto-vasco-2002] and *Convenio Económico* [@boe-convenio-navarra-1990] to capture distinct foral IRPF tariffs.
- **Expenditure & Housing Data:** INE *Encuesta de Presupuestos Familiares* (EPF), mapped to 12 COICOP consumption functions to estimate decile-specific indirect tax burdens (IVA and excise duties), matched with MITMA/INE tenancy and rent-index records (*Índice de Precios de Vivienda en Alquiler*).

## 5. Methods & identification
1. **Top-Income Calibration & Micro-Matching:** Statistically match the top 5% of gross market and capital incomes from the AEAT *Muestra de Declarantes* into ECV survey records using a parametric Pareto reweighting algorithm, ensuring exact fiscal alignment with aggregate budget revenues (`M03`). Calibrate baseline non-take-up to empirical AIReF benchmarks (56% IMV, 70% CAPI [@airef-opinion-imv-2023]).
2. **Decomposition of Poverty and Inequality:**
   - Compute Foster-Greer-Thorbecke ($P_0, P_1, P_2$) indices for both **floating poverty** (60% of contemporaneous post-reform median income) and **anchored poverty** (fixed at the real pre-reform baseline median deflated by HICP).
   - Evaluate Gini, Theil, and Atkinson indices ($\varepsilon \in \{0.5, 1.0, 2.0\}$), alongside Shorrocks-Shapley decompositions that separate the direct universal transfer effect, the benefit-integration offset (`M07`), the IRPF tariff restructure (`M03`), and labor-supply behavioral adjustments (`M08`).
   - Implement Ponthieux's [@ponthieux-2013-income-pooling] Individualized Poverty and Financial Autonomy metric to evaluate the elimination of intra-household hidden poverty among secondary earners and cohabiting adult children.
3. **Closed-Loop Rent Recycling & Real Income Metric:** Disaggregate households across four housing tenure regimes (outright owners, mortgaged owners, subsidized renters, and private-market renters). Define real equivalized disposable income $y_{i}^{\text{real}} = (y_{i}^{\text{disp}} - \Delta R_{i} - T_{i}^{\text{ind}})/\phi(k_i)$, where $\Delta R_i$ denotes landlord rent extraction modeled via `M05` pass-through elasticities ($\gamma \in [0.15, 0.45]$) for private tenants. Aggregate landlord rent extraction is dynamically credited back to landlord capital income in AEAT microdata and subjected to reformed IRPF tax schedules (`M03`), completing the macroeconomic fiscal-housing circuit. Track housing-cost overburden rates (>40% of disposable income) across all tenure cells.
4. **Integration with Micro-Macro GE Loop:** Ingest updated wage and consumer price vectors from the Eurozone HANK model (`M04`) through the four-stage iterative protocol (`plan/methods.md`), verifying that disposable-income distributions reflect general-equilibrium price adjustments.

## 6. Pilot implications
- **Municipal:** Pilots at the municipal level (e.g. Barcelona *B-MINCOME* style [@todeschini-bmincome-2020]) lack jurisdiction over IRPF and regional housing regulations; microsimulation benchmarks must separate municipal cash supplements from national tax schedules, focusing on local poverty alleviation and housing expenditure pressure.
- **Regional (*Régimen Común* vs. *Régimen Foral*):** In *Régimen Común* CCAA, regional governments hold regulatory control over only 50% of the IRPF base (*Ley 22/2009* [@boe-ley-financiacion-ccaa-2009]), creating asymmetric redistribution across regions. In Basque/Navarrese *Régimen Foral*, full tax sovereignty under the *Concierto Económico* [@boe-concierto-vasco-2002] enables an integrated regional microsimulation testbed where IRPF bracket restructuring and UBR transfers are cleared within a single unified treasury.
- **National:** Provides the definitive baseline for whole-economy microsimulation: unifies AEAT national tax clearing, harmonizes regional living-cost adjustments, eliminates inter-regional fiscal spillover frictions, and executes the complete Status-Quo Budget Neutrality constraint nationwide.

## 7. Risks, counterarguments & open issues
- **Counterargument (Middle-Class Squeeze in Deciles 7–8):** Dual-earner households with above-median earnings but high housing costs may experience marginal tax increases before factoring in broader public service benefits. *Mitigation:* Explicitly calibrate the affine child schedule (`M02`) and dynamic IRPF exemptions to preserve living standards, validating results against granular decile-by-tenure winner/loser matrices.
- **Counterargument (Floating Poverty Threshold Mirage):** When a universal benefit raises median disposable income, households near the poverty line may mathematically remain in relative poverty even though their real consumption has doubled. *Mitigation:* Systematically report dual indicators: anchored poverty at baseline living standards alongside floating relative poverty.

## 8. Deliverables & effort
- Open-source EUROMOD-Spain UBR policy package (.xml policy rules, stpath scripts, and documentation) hosted on GitHub.
- Detailed Distributional Atlas of Spain (deciles, demographics, autonomous communities, housing tenures) for Chapter 4 of the monograph. (Effort: 6 person-weeks).


<!-- FILE: plan/modules/M10-pilot-evaluation-design.md -->
---
id: M10
title: Multi-level pilot and causal evaluation design
status: draft
locked: false
depends_on: [M02, M05, M06, M08, M12, M15]
covers: [F11]
feeds_chapters: [7]
last_iteration: 2
---
# M10 · Multi-level pilot and causal evaluation design

## 1. Why this matters
Past basic income trials worldwide have suffered from four fundamental methodological limitations: (i) dispersed individual-level randomization that inherently cannot detect general-equilibrium effects on local rents, prices, or wages [@egger-2022-ge-kenya; @banerjee-niehaus-suri-2019; @hoynes-rothstein-2019]; (ii) severe spatial interference and SUTVA violations when clusters are defined as narrow, porous urban census tracts without buffer zones [@baird-2018-interference]; (iii) clawback arms that phase out at median earnings, creating threshold kinks without identifying upper-bracket behavioral responses; and (iv) administrative tax secrecy barriers under Spanish law that trigger differential attrition in control groups [@boe-lgt-2003; @boe-lopdgdd-2018]. Following `D-005`, this module establishes a statistically powered, pre-registered multi-level Spanish pilot architecture comparing **Municipal**, **Regional (Régimen Común vs. Régimen Foral)**, and **National** experimental options, linked directly to administrative registers with SUTVA buffers and bunching econometrics.

## 2. Research questions
- **RQ-M10-01**: How can a two-stage randomized spatial saturation design with mandatory geographic buffer zones jointly identify partial-equilibrium behavioral responses and local general-equilibrium spillovers (rental pass-through `M05`, reservation wage bargaining `M08`, and local retail multipliers `M04`) while satisfying SUTVA?
  - *Hypothesis:* Randomizing across $J = 70$ economically self-contained spatial clusters (distinct small municipalities of 1,500–5,000 residents and transit-bounded urban districts with $\ge 2\text{--}5$ km buffer zones per Baird et al. [@baird-2018-interference] and Duflo et al. [@duflo-2007-randomization], $N \approx 20,000$ participants) provides 80% statistical power ($\alpha = 0.05$) to detect a $\ge 1.2$ hour/week labor supply adjustment and a $\ge 2.8\%$ local rental pass-through differential without spatial contamination.
- **RQ-M10-02**: How can an experimental pilot identify labor-supply substitution elasticities without violating Constitutional equal treatment (Art. 14 CE) or tax legality (Art. 31.1 CE), while estimating responses around the clawback phase-out kink ($Y^*$)?
  - *Hypothesis:* Randomizing an explicit **Benefit Phase-Out / Clawback Rate Arm** ($0\%$, $38\%$, and $50\%$ clawback bounded at the gross grant envelope) paired with a pre-registered bunching estimator (Saez [@saez-2010-bunching]; Chetty et al. [@chetty-2012-bounds]) around $Y^* = \text{UBR}/\tau_{\text{clawback}}$ cleanly identifies compensated wage and income elasticities ($\varepsilon^c, \eta$) in full compliance with constitutional law, leaving upper-decile tax responses to administrative IRPF panel reforms (`M08`).
- **RQ-M10-03**: What legal, technical, and fiscal architecture ensures continuous register linkage across AEAT, TGSS, and SNS without violating tax secrecy (Art. 95 LGT) or inducing differential control attrition?
  - *Hypothesis:* A statutory habilitation provision under Art. 95.1.k LGT [@boe-lgt-2003], paired with cryptographic HMAC-SHA256 salted hashing and an unconditional Evaluation Participation Stipend (€250–€300/year) for control participants, achieves >95% continuous register-linkage completion across treated and control arms.

## 3. State of knowledge
Landmark trials—OpenResearch [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health], GiveDirectly Kenya [@egger-2022-ge-kenya], Finland [@kangas-2021-finland], Stockton SEED [@west-2024-seed], and Barcelona's B-MINCOME [@todeschini-bmincome-2020]—demonstrate that linking national administrative registers eliminates differential survey attrition on earnings and employment. Furthermore, two-stage randomized saturation [@egger-2022-ge-kenya; @banerjee-niehaus-suri-2019] is statistically indispensable for disentangling displacement and price spillovers from individual treatment effects. However, Baird et al. [@baird-2018-interference] establish that unless saturation clusters enforce geographic buffer zones, spatial spillovers violate the Stable Unit Treatment Value Assumption (SUTVA). Catalonia's 2021–2023 Office for the Basic Income Pilot Plan designed a hybrid individual and municipal saturation blueprint, providing valuable operational protocols despite its legislative delay (`M11`).

## 4. Spain context & data sources
- **Spanish Precedents:** Barcelona B-MINCOME (2017–2019 [@todeschini-bmincome-2020]), Catalonia's saturation blueprint, and the Ministry of Inclusion's 34 randomized social-itinerary IMV pilots.
- **Administrative Register Spine & Data Linkage Protocol:** Continuous, anonymized microdata linkage via DNI/NIE across:
  - *Seguridad Social* (TGSS daily affiliation, contract modalities 100/200/300, and *bases de cotización* in MCVL).
  - *Agencia Tributaria* (AEAT) and Basque/Navarrese Foral Treasuries (monthly *retenciones* Modelo 111, annual IRPF Modelo 100). Enabled by a model statutory provision under Art. 95.1.k *Ley General Tributaria* (LGT [@boe-lgt-2003]) and *Ley Orgánica 3/2018* (LOPDGDD [@boe-lopdgdd-2018]) using HMAC-SHA256 salted pseudonymization.
  - *Servicio Público de Empleo Estatal* (SEPE) unemployment registers and benefit claims.
  - *Sistema Nacional de Salud* (SNS) electronic clinical records (primary care consultations, psychotropic prescriptions, sick leave *bajas IT*).
  - *Fianzas de Alquiler* Registries (INCASÒL in Catalonia, IVIMA in Madrid, AVRA in Andalusia) for transaction-level lease contracts and executed rents.

## 5. Methods & identification
1. **Two-Stage Spatial Saturation with Buffer Zones & Power Math:**
   - Define $J = 70$ clusters (35 treated, 35 control) as economically self-contained small municipalities (1,500–5,000 residents) in non-metropolitan areas and transit-bounded urban districts, surrounded by mandatory geographic buffer zones ($\ge 2\text{--}5$ km in rural/peri-urban zones; donut matching in urban areas) per Baird et al. [@baird-2018-interference] and Duflo et al. [@duflo-2007-randomization].
   - Compute cluster Minimum Detectable Effect (MDE):
     $$\text{MDE} = (t_{\alpha/2} + t_{1-\beta}) \sqrt{\frac{\sigma^2 (1 - R^2)}{P(1-P) J m} [1 + (m - 1)\rho]}$$
     Calibrated with Spanish empirical parameters: intraclass correlation coefficients $\rho_{\text{rent}} = 0.08$ and $\rho_{\text{labor}} = 0.03$, cluster size $m \approx 285$ adults, $P = 0.5$, $J = 70$, and baseline covariate explanatory power $R^2 \approx 0.35$ from pre-trial INCASÒL/MCVL microdata, yielding 80% power at $\alpha = 0.05$ to detect a 1.2 hour/week labor adjustment and a 2.8% rent pass-through effect.
   - Conduct inference using wild cluster bootstrap and randomization inference to guard against small-sample cluster over-rejection [@egger-2022-ge-kenya].
2. **Benefit Phase-Out Arm & Bunching Econometrics:**
   - Randomly assign treated participants to three clawback structures:
     - *Arm A (Pure UBR / 0% clawback):* Full €900/month cash transfer with standard baseline IRPF.
     - *Arm B (Moderate clawback / 38%):* €900/month reduced by 38c per euro of gross earnings, bounded at zero grant ($Y^* = \text{€}28,421/\text{year}$).
     - *Arm C (High clawback / 50%):* €900/month reduced by 50c per euro of gross earnings, bounded at zero grant ($Y^* = \text{€}21,600/\text{year}$).
   - Stratify sample across baseline earnings domains and implement Saez [@saez-2010-bunching] and Chetty et al. [@chetty-2012-bounds] bunching estimators around $Y^*$ to extract compensated substitution elasticities directly from excess mass, without violating constitutional tax legality.
3. **Register Linkage & Control Retention Protocol:**
   - Pay an unconditional Evaluation Participation Stipend (€250–€300/year) to control participants to eliminate differential attrition.
   - Net 36-month pilot budget: €480M gross transfers + €35M administration/data spine - €220M clawback/benefit offsets = €295M net (~€98M/year), funded through dedicated R&D innovation appropriations in the State General Budget (*PGE*).

## 6. Pilot implications
- **Municipal Tier:** Feasible for localized testing of subjective well-being, health, and local consumption multipliers, but legally prohibited from altering IRPF withholdings or national social security registers; highly vulnerable to local cross-border shopping without spatial buffer zones.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común* (e.g. Catalonia, Andalusia, Valencia), regional pilots must coordinate with the State Ministry of Inclusion and AEAT to secure register access under Art. 95.1.k LGT, and cannot modify the state portion of IRPF.
  - In *Régimen Foral* (Basque Country or Navarre), regional governments possess comprehensive tax and social protection competence under the *Concierto Económico*, providing the optimal constitutional testbed for testing integrated tax-transfer clawbacks and unified payroll clearing (`M12`).
- **National Tier:** Staggered cohort rollout across whole sectors displaced by AI (`M01`), providing macroeconomic macro-closure evaluation (`M04`) and testing full national AEAT automated clearing without territorial leakages.

## 7. Risks, counterarguments & open issues
- **Counterargument (Finite-Horizon Bias):** A 36-month pilot cannot replicate permanent-income life-cycle responses (such as fertility, long-term educational retraining, or career abandonment) [@hoynes-rothstein-2019]. *Mitigation:* Explicitly model the finite-horizon transition mathematically separating windfall income effects from Frisch intertemporal substitution (`M15`), and communicate a 6-month post-pilot step-down ramp to participants to prevent welfare cliffs.
- **Counterargument (Control Group Resentment & Attrition):** Non-treated controls in saturated clusters experience survey fatigue and drop out. *Mitigation:* Guarantee register linkage via the Art. 95 LGT statutory protocol, minimize survey burden, and provide the annual €250–€300 participation stipend.

## 8. Deliverables & effort
- Comprehensive Pre-Analysis Plan (PAP) registered on AEA RCT Registry with statistical power calculations, buffer-zone coordinates, and mock analysis scripts.
- Multi-Tier Pilot Technical Blueprint and Inter-Administrative Data-Linking Protocol (INSS-AEAT-TGSS-SNS). (Effort: 7 person-weeks).


<!-- FILE: plan/modules/M11-political-economy.md -->
---
id: M11
title: Political economy, public opinion, and coalition feasibility
status: draft
locked: false
depends_on: [M03, M06, M09, M16, M17]
covers: [F12]
feeds_chapters: [8]
last_iteration: 2
---
# M11 · Political economy, public opinion, and coalition feasibility

## 1. Why this matters
Even an economically optimal and constitutionally valid UBR plan will fail if it cannot assemble a durable legislative coalition in Spain's fragmented bicameral parliament (*Congreso de los Diputados* and *Senado*), secure buy-in from social partners (trade unions CCOO and UGT, employers CEOE), and survive autonomous-community veto politics—as demonstrated by the 2023 parliamentary blockage of the Catalan UBR pilot budget [@van-parijs-vanderborght-2017; @tsebelis-2002-veto-players]. In Spain's institutional architecture, the Senate wields an absolute veto over fiscal stability targets and spending ceilings under *Ley Orgánica 2/2012* (LOEPSF Art. 15 [@boe-loepsf-2012]), making bicameral veto-player alignment mandatory.

## 2. Research questions
- **RQ-M11-01**: How do policy design attributes—framing (traditional "Universal Basic Income" vs. "AI Productivity Dividend" vs. "Refundable IRPF Tax Credit"), financing source (labor IRPF vs. AI/corporate/wealth levies `M16`), residency rules (`M13`), and benefit level—shift support among Spanish median-decile voters and across party electorates?
  - *Hypothesis:* In a pre-registered conjoint experiment on a representative Spanish sample, framing UBR as an IRPF-integrated "AI & Automation Dividend" financed predominantly by corporate/AI/capital levies (`M16`) with a 2–3 year residency requirement increases majority support by +14 to +20 percentage points compared to a labor-tax-financed welfare framing, winning majority backing across left, center, and regionalist voters.
- **RQ-M11-02**: Under what institutional bargains do Spanish trade unions (CCOO, UGT) and regionalist swing caucuses (PNV, Junts) endorse UBR, and how can bicameral veto points (Senate LOEPSF Art. 15) be navigated?
  - *Hypothesis:* Union endorsement requires three explicit statutory guarantees under Art. 7 CE and the CES (Ley 21/1991): (i) strict non-supplantation clauses preventing employers from citing UBR to depress bargained collective wages or statutory SMI hikes [@vanderborght-2006-trade-unions; @vlandas-2019-politics-ubi], (ii) preservation of the `M07` contributory pension slope and Art. 280 TRLGSS credits, and (iii) social partner co-governance of AI transition funds (`M16`). For regionalist caucuses, concessions including decentralized regional tax tranches, SME surplus exemptions, and foral *Cupo* neutrality unlock the necessary bicameral majorities.

## 3. State of knowledge
Comparative political economy shows that universal programs enjoy greater long-term fiscal resilience than narrowly targeted means-tested programs ("paradox of redistribution"), yet face high initial enactment hurdles because visible gross tax hikes alarm middle-decile voters and insiders [@van-parijs-vanderborght-2017; @hoynes-rothstein-2019]. Tsebelis's [@tsebelis-2002-veto-players] veto-player framework demonstrates that multi-arena systems with territorial upper chambers require broad consensual policy packages. Political studies of basic income confirm that union skepticism stems from fears of wage suppression and welfare-state retrenchment [@vanderborght-2006-trade-unions; @vlandas-2019-politics-ubi], which can be neutralized by binding statutory non-supplantation clauses.

## 4. Spain context & data sources
- **Public Opinion Data:** *Centro de Investigaciones Sociológicas* (CIS) barometers, European Social Survey (ESS) Spanish waves on welfare attitudes, and CEO (*Centre d'Estudis d'Opinió*) surveys on the Catalan UBR pilot.
- **Institutional Actors & Legislation:** Parliamentary records (*Diario de Sesiones del Congreso y Senado* on IMV [@boe-imv-2021]), *Ley Orgánica 2/2012 de Estabilidad Presupuestaria* (LOEPSF [@boe-loepsf-2012]), official position papers of CCOO, UGT, USO, CEOE-CEPYME, and autonomous-community governments.

## 5. Methods & identification
1. **Pre-Registered Conjoint Survey Experiment ($N = 3,500$ Spanish Voters):** Randomize 6 policy dimensions (Benefit Amount, Tax Financing Mechanism, AI Trigger Condition, Residency Rule, Treatment of Existing Pensions/Benefits, Administrative Level) to estimate Average Marginal Component Effects (AMCEs) by income decile, CNO-11 AI-exposure risk (`M01`), autonomous community, and party vote recall.
2. **Bicameral Veto-Player & Coalition Mapping:** Embed Tsebelis's [@tsebelis-2002-veto-players] spatial equilibrium model across both the *Congreso de los Diputados* and the *Senado*, evaluating spatial distance and win-sets under LOEPSF Art. 15 absolute spending-ceiling veto constraints and regionalist swing caucuses. Formalize the tripartite social dialogue architecture under Art. 7 CE.

## 6. Pilot implications
- **Municipal Tier:** Feasible under local council municipal decrees (*ordenanzas municipales*), characterized by lower legislative veto hurdles but high vulnerability to local electoral cycles and administrative discontinuation (as observed post-B-MINCOME in Barcelona [@todeschini-bmincome-2020]).
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común* (e.g. Catalonia), pilots require regional parliamentary budget authorization, leaving them exposed to cross-party ideological vetoes and legal challenges from the central government regarding State jurisdictional competencies (`M06`).
  - In *Régimen Foral* (Basque Country and Navarre), established bipartisan regional majorities and complete fiscal-legislative autonomy under the *Concierto Económico* offer the highest institutional stability for a multi-year experimental pilot.
- **National Tier:** Requires navigating the bicameral veto architecture: passing ordinary enabling legislation in Congress while structuring expenditure ceilings to overcome or reform the Senate's absolute veto under LOEPSF Art. 15 [@boe-loepsf-2012], anchored in tripartite social dialogue pacts.

## 7. Risks, counterarguments & open issues
- **Counterargument (Territorial Fiscal Backlash):** Net-contributing regions with higher nominal wages and cost of living (Madrid, Catalonia, Balearics) will show a higher share of net IRPF contributors to a uniform national UBR (`M09`). *Mitigation:* Quantify inter-regional fiscal flows transparently and test whether pairing national Tier A with regionally financed cost-of-living supplements (`M13`) stabilizes territorial coalitions.

## 8. Deliverables & effort
- Conjoint Survey Experiment Questionnaire, Pre-Registration, and AMCE Estimation Pipeline.
- Bicameral Veto-Player & Social Partner Coalition Matrix for Chapter 8. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M12-administration-delivery.md -->
---
id: M12
title: Administrative delivery, digital infrastructure, and take-up
status: draft
locked: false
depends_on: [M03, M06, M07, M10]
covers: [F13]
feeds_chapters: [6]
last_iteration: 2
---
# M12 · Administrative delivery, digital infrastructure, and take-up

## 1. Why this matters
The flagship empirical lesson from Spain's *Ingreso Mínimo Vital* (IMV [@boe-imv-2021]) is that statutory benefit generosity fails in practice when administrative delivery relies on ex-ante means testing, onerous household cohabitation verification, and prior-year tax returns: according to official AIReF evaluations [@airef-opinion-imv-2023; @airef-opinion-imv-2024], 56% of eligible households in severe poverty never receive IMV (70% non-take-up for CAPI), while thousands of impoverished families suffer devastating retrospective debt recovery notices (*cobros indebidos*). UBR's paramount operational advantage is near-universal (>98%) automatic delivery executed through coordinated AEAT, Social Security, and municipal infrastructure.

## 2. Research questions
- **RQ-M12-01**: How can Spain's *Agencia Estatal de Administración Tributaria* (AEAT), *Instituto Nacional de la Seguridad Social* (INSS), and INE *Padrón Continuo* execute monthly individual UBR disbursement and real-time IRPF withholding clearing with >98% take-up and zero retrospective debt traps?
  - *Hypothesis:* Operating a **Unified Monthly Tax-Transfer Clearing Account** (*Cuenta Única Tributaria-Social*) linked to DNI/NIE—where every adult resident receives the baseline UBR cash transfer via automated SEPA credit on the 1st of each month (or credits it against monthly IRPF payroll withholdings *retenciones a cuenta*) without application forms—raises take-up above 98% and reduces operational overhead per recipient by >70% relative to IMV.
- **RQ-M12-02**: How can monthly payroll clearing protect employee privacy against employer snooping into household composition, disability, or vulnerability status under GDPR Art. 9 and *Ley Orgánica 3/2018* (LOPDGDD [@boe-lopdgdd-2018])?
  - *Hypothesis:* Restricting employer payroll clearing exclusively to the uniform individual adult UBR credit via an algorithmic, privacy-preserving **Numerical Tax Code** (*Código de Retención Sintético*)—while routing all child supplements (`M02`) and disability top-ups (`M07`) directly through AEAT/INSS bank disbursements—completely shields sensitive personal and family data from employer human resources departments.
- **RQ-M12-03**: What statutory shields against debt attachment (*inembargabilidad*) and last-mile payment rails (bypassing municipal *Padrón* barriers and commercial bank AML account freezes) guarantee continuous access to the *mínimo existencial*?
  - *Hypothesis:* Classifying UBR as strictly *inembargable* under Art. 607 LEC and Art. 44 TRLGSS [@boe-trlgss-2015], coupled with mandatory *Empadronamiento Social de Oficio* under the BOE Technical Instructions of 17 February 2020 and a public payment delivery rail via *Correos* and Banco de España immune to commercial AML account freezes (*Ley 10/2010*), guarantees unhindered access for unhoused and marginalized populations.

## 3. State of knowledge
Empirical public administration literature shows that bureaucratic application hurdles, stigma, frequent recertification audits, and fear of sudden retrospective debt clawbacks are the primary drivers of welfare non-take-up [@hoynes-rothstein-2019; @airef-opinion-imv-2023]. Conversely, universal child benefits and automated refundable tax credits routinely achieve 96–99% coverage [@van-parijs-vanderborght-2017]. Evidence from Barcelona's B-MINCOME [@todeschini-bmincome-2020] and Finland's trial [@kangas-2021-finland] proves that unconditional, predictable monthly payment schedules on a fixed calendar day drastically reduce cognitive load, liquidity distress, and recourse to predatory consumer loans.

## 4. Spain context & data sources
- **Existing Digital Spine:** AEAT digital clearing (*Renta Web*, real-time VAT reporting *SII*, and monthly Form 111/190 payroll withholdings), TGSS/INSS (*Tarjeta Social Digital* integrated registry of all public cash transfers), and INE *Padrón Municipal Continuo*.
- **Administrative Law & Data Protection Statutes:**
  - *Ley 58/2003 General Tributaria* (LGT [@boe-lgt-2003] Arts. 71–73 on tax compensation/set-off; Art. 95 on tax confidential data sharing exceptions).
  - *Ley 1/2000 de Enjuiciamiento Civil* (LEC Art. 607 on non-seizable salary/pension scales).
  - *Real Decreto Legislativo 8/2015* (TRLGSS [@boe-trlgss-2015] Art. 44 on non-seizability of basic social security benefits).
  - *Ley 39/2015 del Procedimiento Administrativo Común* (LPAC [@boe-lpac-2015] Art. 41 on automated administrative acts).
  - *Reglamento (UE) 2016/679* (GDPR Art. 9 on special category data; Art. 22 on automated individual decision-making) and Spanish *Ley Orgánica 3/2018* (LOPDGDD [@boe-lopdgdd-2018]).
  - *Resolución de 17 de febrero de 2020* (BOE 2 de mayo de 2020) on municipal padrón registration for unhoused residents (*padrón social*).

## 5. Methods & identification
1. **Gross vs. Net Operational Architecture:**
   - *Option A (Universal Gross SEPA Disbursement):* INSS/AEAT executes a direct €900 SEPA bank transfer to every resident adult on the 1st of every month; employers compute standard IRPF withholding rates on gross salaries without adjusting for UBR. This option maximizes intra-household transparency and individual financial autonomy (`M14`).
   - *Option B (Hybrid Payroll Clearing via Numerical Tax Code):* For formal salaried employees, employers apply a single standard withholding adjustment reflecting the adult UBR tax credit, while transferring the remaining balance. Child, disability, and zero-earner benefits are credited directly by AEAT/INSS.
2. **Algorithmic Due Process & Anti-Offset Shield Protocol:**
   - Formalize statutory language forbidding commercial banks and public administrations (AEAT, TGSS, municipal tax agencies) from executing automated offsets (*compensación de oficio*) against the UBR account balance.
   - Establish mandatory human-in-the-loop review under Art. 41 LPAC before any suspension or modification of payment, guaranteeing a 30-day non-suspensive hearing window.
3. **Last-Mile Social Inclusion & Public Rail Protocol:**
   - Codify *Empadronamiento Social de Oficio* to bypass municipal Padrón gatekeeping for unhoused and precariously housed residents under the Technical Instructions of 17 February 2020 (BOE 2 May 2020).
   - Establish a public payment delivery rail via *Sociedad Estatal Correos y Telégrafos* (*Correos*) and Banco de España providing basic accounts (*cuentas de pago básicas* under *Real Decreto-ley 19/2018*) with statutory immunity from commercial AML/KYC account freezes (*Ley 10/2010*).

## 6. Pilot implications
- **Municipal:** Pilots at the municipal level (e.g. Barcelona *B-MINCOME* [@todeschini-bmincome-2020]) cannot alter AEAT payroll tax withholding codes (Form 111) or TGSS social security databases; municipal pilots are confined to gross municipal SEPA transfers, useful for testing prepaid debit cards and municipal social work interface, but unable to evaluate automated tax clearing.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común*, regional pilots require coordinated data exchange protocols with the central Ministry of Inclusion and AEAT, facing jurisdictional barriers to altering national payroll withholding formulas.
  - In *Régimen Foral* (Basque Country / Navarre), regional treasuries (*Haciendas Forales*) directly manage Form 110/111 payroll withholdings and regional tax registers, providing an ideal real-world environment to pilot the Numerical Tax Code and unified monthly tax-benefit clearing.
- **National:** Full deployment across the whole territory enables real-time synchronization between the AEAT national database, TGSS daily affiliation registers, and the *Padrón Continuo*, eliminating inter-administrative fragmentation and achieving seamless automated clearing.

## 7. Risks, counterarguments & open issues
- **Counterargument (Registration Fraud & Ghost Residents):** Tying automatic disbursements to the municipal *Padrón* could incentivize fictitious registrations. *Mitigation:* Cross-validate *Padrón* active status continuously against the National Health System card registry (*Tarjeta Sanitaria Individual*), school enrollments, and Social Security activity, flagging anomalies for localized in-person verification (`M13`).
- **Counterargument (Digital Divide Exclusion):** Low-income or elderly individuals without digital certificates (*Cl@ve*, *DNI electrónico*) could be marginalized. *Mitigation:* Mandate proactive *de oficio* enrollment by public agencies; no citizen is required to log into an online portal to receive baseline UBR.

## 8. Deliverables & effort
- AEAT–INSS–Padrón Digital Interoperability Blueprint and Numerical Tax Code Specification.
- Statutory Draft for *Inembargabilidad* Shield and Algorithmic Due-Process Protections for Chapter 6. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M13-migration-territory-residency.md -->
---
id: M13
title: Territorial purchasing power, internal mobility, and residency rules
status: draft
locked: false
depends_on: [M02, M03, M05, M06, M12]
covers: [F14]
feeds_chapters: [5, 6]
last_iteration: 2
---
# M13 · Territorial purchasing power, internal mobility, and residency rules

## 1. Why this matters
Spain exhibits a 35–45% divergence in regional purchasing power parity (PPP) and housing rental costs between congested metropolitan centers (Madrid, Barcelona, Palma, San Sebastián) and depopulated rural provinces (*España vaciada*: Soria, Teruel, Cuenca, Zamora) [@boe-vivienda-2023]. A nationally uniform nominal UBR (€900/month) functions as a massive structural equalizing force—delivering a high real living standard in rural areas—while raising fundamental challenges regarding internal migration, spatial sorting, urban housing absorption (`M05`), and external migration residency criteria under EU law (`M06`).

## 2. Research questions
- **RQ-M13-01**: Should Spain's baseline UBR be paid as a strictly uniform nominal transfer nationwide, or modulated across autonomous communities by regional purchasing power parity indices?
  - *Hypothesis:* A uniform nominal national floor (anchored in basic constitutional equality under Art. 149.1.1 CE [@boe-ce-1978] and preventing mechanical capitalization into urban land rents `M05`) is welfare-superior to price-indexed national transfers; Autonomous Communities seeking to alleviate metropolitan living costs can fund supplementary housing allowances from own-source regional taxes (`M03`, `M06`).
- **RQ-M13-02**: How can statutory residency rules balance fiscal sustainability with the constitutional requirement of **Tax-Benefit Symmetry** (Art. 31.1 CE), EU free movement (Art. 45 TFEU), and the CJEU *Schumacker* doctrine for non-resident cross-border workers?
  - *Hypothesis:* Restricting waiting periods strictly to *economically inactive* third-country and EU entrants (24 months under Directive 2004/38/EC Art. 24(2) [@eu-dir-2004-38-free-movement])—while granting immediate pro-rata UBR tax credits to all economically active residents subject to IRPF and non-resident EU workers subject to IRNR earning $\ge 75\%$ of family income in Spain under CJEU *Schumacker* (Case C-279/93 [@cjeu-c-279-93-schumacker])—fully satisfies EU non-discrimination while preventing taxation of the *mínimo existencial*.
- **RQ-M13-03**: To what extent does a portable, uniform UBR overcome historical Spanish labor immobility frictions (homeownership tenure, 6–10% regional ITP transfer taxes, and rural amenity deficits) to induce relocation toward *España vaciada*?
  - *Hypothesis:* Incorporating regional housing tenure and ITP friction parameters [@antolin-bover-1997-migration] reveals that cash portability alone yields modest relocation (2.5–3.8%); pairing UBR with rural housing rehabilitation subsidies and regional ITP exemptions increases 5-year net migration to municipalities under 10,000 inhabitants by 6.2–8.5% across S2 and S3.

## 3. State of knowledge
Spatial equilibrium theory (Roback-Moretti frameworks) demonstrates that uniform national cash transfers encourage geographic decentralization toward lower-cost regions with higher amenities, whereas cost-of-living adjustments trap low-income households in congested cities and are captured by landlords [@fack-2006-housing-benefits; @diamond-mcquade-qian-2019-rent]. Cash-transfer trials confirm that portable grants increase residential flexibility [@bartik-2024-openresearch]. In Spain, however, inter-provincial migration is historically constrained by high owner-occupancy rates, 6–10% regional transaction taxes (*Impuesto sobre Transmisiones Patrimoniales*, ITP), and spatial sorting into amenity-dense urban centers [@antolin-bover-1997-migration]. In external migration, welfare magnet effects are regulated through statutory qualifying residence durations and the *Schumacker* parity doctrine [@cjeu-c-279-93-schumacker; @eu-dir-2004-38-free-movement].

## 4. Spain context & data sources
- **Spatial & Mobility Microdata:** INE *Estadística de Variaciones Residenciales* (EVR, tracking all inter-municipal changes of residence), *Padrón Municipal Continuo*, regional PPP indices, and Ministry of Housing (MIVAU) municipal rental price indexes (*Sistema Estatal de Referencia de Precios de Alquiler*).
- **Residency, Labor, and Tax Spine:**
  - *Ley Orgánica 4/2000 sobre derechos y libertades de los extranjeros en España* (LOEX [@boe-extranjeria-2000], legal residency authorizations and *arraigo* mechanisms).
  - *Ley 19/2021* [@boe-imv-2021] (IMV 1-year legal residency threshold and exceptions for minors, trafficking victims, and domestic violence survivors).
  - *Ley 35/2006 del IRPF* (LIRPF Art. 9 on fiscal residency: >183 days or center of economic interests in Spain) and *RDLeg 5/2004 del IRNR*.
  - Directive 2004/38/EC [@eu-dir-2004-38-free-movement] (freedom of movement and equal treatment for EU workers and self-employed).
  - CJEU Case C-279/93 (*Schumacker* [@cjeu-c-279-93-schumacker]).

## 5. Methods & identification
1. **The Tax-Benefit Symmetry & Schumacker Protocol:**
   - Formalize the legal-economic rule: Any resident individual earning taxable income subject to Spanish IRPF who is subjected to the reformed tax tariff (`M03`) without the personal allowance (*mínimo personal*) MUST receive the UBR tax credit from month one. Extend this pro-rata credit to frontier and seasonal EU workers paying IRNR who earn $\ge 75\%$ of global income in Spain per CJEU *Schumacker* [@cjeu-c-279-93-schumacker].
   - Inactive non-contributing arrivals (non-working EU citizens without comprehensive sickness insurance or non-EU third-country nationals) are subject to a statutory 24-month continuous legal residency requirement before drawing the non-contributory cash component, strictly conforming to CJEU Case C-333/13 *Dano*.
2. **Spatial Discrete-Choice Location Model with Immobility Frictions:**
   - Formulate a structural discrete-choice model across Spain's 8,131 municipalities following Antolín & Bover [@antolin-bover-1997-migration]. Utility $U_{ijt} = \alpha [w_{jt}(1 - \tau) + \text{UBR} - r_{jt}] + \beta A_j - \delta d_{ij} - \kappa \cdot \text{ITP}_j - \theta \cdot \text{Owner}_i + \varepsilon_{ijt}$, where $r_{jt}$ is local rent (`M05`), $A_j$ captures local public capital (broadband, primary healthcare, schooling), $\text{ITP}_j$ is the regional conveyance tax rate (6–10%), and $\text{Owner}_i$ captures owner-occupancy lock-in.
   - Simulate counterfactual spatial equilibrium populations across S1–S3 under uniform vs. regionally indexed transfers and paired rural fiscal incentives.

## 6. Pilot implications
- **Municipal:** Highly vulnerable to strategic local cross-border shopping and municipal "welfare shopping" (*efecto llamada municipal*) unless strictly constrained. Any municipal-level pilot (such as Barcelona B-MINCOME [@todeschini-bmincome-2020]) must mandate that participants were registered in the municipal *Padrón* at least 12–24 months *prior* to the public launch date of the pilot.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común* CCAA, inter-regional migration between autonomous communities cannot be constitutionally restricted (Art. 139.2 CE), requiring regional pilots to track cross-regional mobility through the MCVL to measure inter-autonomous spillover flows.
  - In *Régimen Foral* (Basque Country / Navarre), historical residence requirements for regional minimum incomes (RGI currently requires 1–3 years of municipal registration) provide an established legal template to evaluate regional residency filtering within a constitutionally protected fiscal framework.
- **National:** Eliminates all domestic inter-regional welfare-border distortions; enforces uniform legal residency verification across the entire national frontier, seamlessly synchronizing the Ministry of the Interior (foreign residency authorizations), the AEAT (fiscal domicile), and INE *Padrón Continuo*.

## 7. Risks, counterarguments & open issues
- **Counterargument (Cross-Border Welfare Magnetism):** Critics allege that an unconditional €900 cash transfer will induce massive irregular migration flows. *Mitigation:* The dual architecture links immediate eligibility to formal fiscal registration (IRPF), while requiring 24 months of legal registered presence for economically inactive claimants. This fully complies with EU case law (*Dano*, *Alimanovic*) and preserves national fiscal stability.
- **Counterargument (Depopulation of Metropolitan Service Sectors):** Low-wage service workers in high-cost cities might relocate to rural areas, causing urban labor shortages in local non-tradable services. *Mitigation:* As shown in `M08`, reservation wage bargaining increases urban service wages, inducing wage-driven market equilibrium rather than permanent shortages.

## 8. Deliverables & effort
- Comprehensive Spatial Equilibrium Simulation and Demographic Mobility Atlas for Spain.
- Model Statutory Text on Residency Qualifications, Tax-Benefit Symmetry, and Anti-Fraud Controls for Chapters 5 and 6. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M14-gender-care-health.md -->
---
id: M14
title: Gender, unpaid care, disability, and health outcomes
status: draft
locked: false
depends_on: [M01, M02, M07, M08, M09, M10]
covers: [F15]
feeds_chapters: [3, 7]
last_iteration: 2
---
# M14 · Gender, unpaid care, disability, and health outcomes

## 1. Why this matters
Spanish women perform over two-thirds of unpaid domestic and care work, face persistent gender wage and pension gaps, and are disproportionately concentrated in administrative, clerical, customer-facing, and paralegal occupations that face the highest gross exposure to generative AI displacement under Scenarios S1–S3 (`M01`). Furthermore, traditional means-tested safety nets like the IMV [@boe-imv-2021] assess and transfer benefits to a single household representative (*titular*), reinforcing intra-household economic dependency and trapping secondary earners in poverty. Persons with disabilities face substantial non-discretionary economic extra costs (€3,500–€10,000/year [@puig-segura-2021-discapacidad]) that cannot be met by baseline cash transfers alone. By establishing strictly individual, unconditional cash entitlements (`D-001`) paired with dedicated disability supplements, UBR fundamentally alters intra-household bargaining power, care valuation, disability equity, and population mental health [@miller-2024-openresearch-health; @west-2024-seed].

## 2. Research questions
- **RQ-M14-01**: How does an individual, unconditional UBR (`M02`) reshape intra-household bargaining power, resource allocation, and time use between paid work and unpaid care in Spain when modeled within a collective household framework [@chiappori-1992-collective]?
  - *Hypothesis:* In an estimated Chiappori collective household model on INE *Encuesta de Empleo del Tiempo* (EET) and ECV microdata, individual UBR transfers raise female sharing rules by 8–15 percentage points in low-to-middle income couples, expanding personal non-housing consumption and reducing secondary-earner financial dependence without lowering male labor-force participation.
- **RQ-M14-02**: How will gender-asymmetric AI labor displacement across S1–S3 interact with UBR and the tiered **Complemento Universal por Discapacidad** under *Real Decreto 888/2022* [@boe-rd-888-2022-discapacidad] to prevent severe poverty feminization and offset disability extra costs?
  - *Hypothesis:* Without UBR, female-dominated clerical displacement under S2 leads to a 4.5 percentage-point increase in the female poverty risk; an individual €900/month UBR neutralizes this shock completely. For individuals with disabilities, adding a statutory disability supplement (+25% for 33–64%, +50% for 65–74%, +100% for $\ge 75\%$ per RD 888/2022) fully covers empirical extra living costs [@puig-segura-2021-discapacidad] without distorting labor participation.
- **RQ-M14-03**: What are the causal impacts of unconditional monthly income security on clinical mental health (anxiety, depression, sleep disorders) and pharmaceutical consumption within the Spanish National Health System (*Sistema Nacional de Salud*, SNS)?
  - *Hypothesis:* Consistent with Finland [@kangas-2021-finland], Barcelona B-MINCOME [@todeschini-bmincome-2020], Stockton [@west-2024-seed], and OpenResearch [@miller-2024-openresearch-health], UBR reduces moderate-to-severe psychological distress (PHQ-9/GHQ-12) by 0.22–0.35 standard deviations, lowering SNS primary care consultations and anxiolytic/antidepressant prescription costs by 9–15% among the lowest two income deciles.

## 3. State of knowledge
A substantial body of international evidence demonstrates that mental health gains, stress alleviation, and subjective wellbeing improvements are the most immediate and statistically significant outcomes of unconditional cash transfers [@kangas-2021-finland; @todeschini-bmincome-2020; @west-2024-seed; @miller-2024-openresearch-health]. In gender economics, collective household models [@chiappori-1992-collective] establish that who controls non-labor income within the couple determines Pareto weights and expenditure allocations. Traditional means-tested family benefits often trap women in abusive or unequal partnerships by conditioning transfers on joint household income, whereas universal individual transfers provide an unconditional "threat point" (outside option) that empowers exit capacity and bargaining power [@van-parijs-vanderborght-2017]. In disability economics, Puig-Segura et al. [@puig-segura-2021-discapacidad] document that Spanish households with disabled members require 20–45% higher baseline income to achieve equal living standards.

## 4. Spain context & data sources
- **Time-Use & Household Microdata:** INE *Encuesta de Empleo del Tiempo* (EET) paired with INE *Encuesta de Condiciones de Vida* (ECV), tracking intra-household sharing of unpaid domestic care, eldercare, and childcare across family types.
- **Health & Clinical Microdata:** Ministry of Health *Base de Datos Clínicos de Atención Primaria* (BDCAP) linked via personal health identification code (CIP), *Encuesta Nacional de Salud de España* (ENSE), and pharmaceutical consumption registers (DDD of anxiolytics and antidepressants).
- **Disability & Care Framework:** *Ley 39/2006 de Promoción de la Autonomía Personal y Atención a las personas en situación de dependencia* (SAAD), *Real Decreto 888/2022* on disability degree certification [@boe-rd-888-2022-discapacidad], and *Real Decreto Legislativo 1/2013* on rights of persons with disabilities.

## 5. Methods & identification
1. **Structural Collective Household Estimation:**
   - Specify a Chiappori collective household model [@chiappori-1992-collective] where household utility is $\mu(w_m, w_f, y_m, y_f, \mathbf{z}) U_m + [1 - \mu(\cdot)] U_f$.
   - Estimate the Pareto sharing rule $\mu$ as a function of individual non-labor income ($y_m, y_f$), where UBR shifts individual non-labor endowments symmetrically.
   - Simulate labor-supply and caregiving hours responses using parameters estimated on the Spanish EET and EPA rotating panels.
2. **Universal Disability Supplement Design:**
   - Calibrate the *Complemento Universal por Discapacidad* to the extra costs of disability estimated by Puig-Segura et al. [@puig-segura-2021-discapacidad], structuring an additive cash supplement (+25%, +50%, +100% of baseline UBR) linked to certified medical degrees under RD 888/2022 [@boe-rd-888-2022-discapacidad], keeping SAAD in-kind care services fully intact.
3. **Health Outcome Evaluation Protocol (`M10`):**
   - In the randomized pilot, measure biomarker and clinical endpoints (cortisol, self-reported mental health PHQ-9, sleep quality, and SNS billing records) to test the preventive health-spillover hypothesis.

## 6. Pilot implications
- **Municipal:** Feasible for evaluating local mental health and municipal social services utilization, but cannot address macro-level gender-wage dynamics or national pension entitlements; local pilots can assess community care cooperatives and respite care services.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común*, regional governments manage the SAAD dependency system and the regional health service (*Servicio de Salud*), providing a comprehensive institutional setting to evaluate health-card (BDCAP) primary-care cost offsets and dependency co-payments.
  - In *Régimen Foral* (Basque Country / Navarre), regional governments operate both unified health systems (Osakidetza, Osasunbidea) and autonomous foral tax systems, enabling direct evaluation of how individual tax credits interact with regional family allowances.
- **National:** Provides the definitive framework for eliminating gender pension gaps (`M07`), integrating individual UBR into national IRPF clearing (`M12`), and aligning SAAD statutory care entitlements nationwide without regional coverage disparities.

## 7. Risks, counterarguments & open issues
- **Counterargument (Secondary Earner Labor-Market Detachment):** Unconditional basic income might incentivize low-wage mothers to withdraw from formal employment, aggravating career penalties. *Mitigation:* Evidence from OpenResearch [@bartik-2024-openresearch] and Stockton [@west-2024-seed] indicates that female labor reductions are modest and primarily channeled into infant care and education; furthermore, pairing UBR with guaranteed universal 0–3 public childcare and equal, non-transferable parental leave prevents gendered withdrawal.
- **Counterargument (Disability Cost Substitution):** Fiscal authorities might attempt to replace SAAD disability benefits with UBR. *Mitigation:* Explicitly mandate by statute that all SAAD dependency benefits (Grades I, II, III) and the *Complemento Universal por Discapacidad* (+25% to +100%) remain fully additive on top of UBR (`M07`).

## 8. Deliverables & effort
- Collective Household Intra-Household Welfare Simulation and Gender AI Displacement Atlas.
- SNS Healthcare Cost-Offset Model and Clinical Health Evaluation Protocol for Chapters 3 and 7. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M15-international-evidence.md -->
---
id: M15
title: Comparative international and Spanish empirical evidence
status: draft
locked: false
depends_on: [M08, M10, M14]
covers: [F16]
feeds_chapters: [1, 7]
last_iteration: 2
---
# M15 · Comparative international and Spanish empirical evidence

## 1. Why this matters
To achieve state-of-the-art scientific credibility, the Spanish UBR research plan must systematically synthesize and extract structural behavioral parameters from all major unconditional cash transfer experiments and permanent dividend programs worldwide [@hoynes-rothstein-2019; @banerjee-niehaus-suri-2019]. Crucially, the empirical strategy must formally bridge the external-validity gap between temporary, non-taxed experimental windfalls and a permanent, tax-financed Spanish UBR operating under AI labor-displacement scenarios S1–S3.

## 2. Research questions
- **RQ-M15-01**: What are the meta-analytic pooled causal estimates (and Bayesian posterior distributions) across global and European guaranteed-income trials for extensive-margin employment, weekly hours, clinical mental health, education/training enrollment, and local price inflation?
  - *Hypothesis:* Across advanced-economy trials (OpenResearch [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health], Finland [@kangas-2021-finland], Barcelona B-MINCOME [@todeschini-bmincome-2020], Stockton SEED [@west-2024-seed], and Alaska PFD [@jones-marinescu-2022]), the pooled extensive employment effect of a cash transfer equal to 25–40% of median income is within $[-1.8, +0.6]$ percentage points, with large and statistically robust gains in mental wellbeing ($+0.28\sigma$) and subjective financial security.
- **RQ-M15-02**: How can finite-horizon experimental treatment effects ($\Delta h_{\text{pilot}}, \Delta Y_{\text{pilot}}$) be structurally decomposed to separate windfall income effects ($\eta$) from Frisch intertemporal substitution ($\varepsilon^{\text{Frisch}}$) per MaCurdy [@macurdy-1981-labor-supply] and Blundell & MaCurdy [@blundell-macurdy-1999-labor-supply]?
  - *Hypothesis:* Applying a life-cycle structural decomposition to OpenResearch and Finland microdata separates temporary sabbatical effects from permanent supply shifts, showing that the ratio $\varepsilon^c / \varepsilon^{\text{Frisch}} \in [0.4, 0.7]$ accounts for 45–60% of observed trial hours reductions, preventing overestimation of permanent labor supply contraction in Spain's EUROMOD (`M09`) and HANK (`M04`) models.
- **RQ-M15-03**: Which institutional and methodological limitations in Barcelona's B-MINCOME (2017–2019) and Catalonia's designed 2021–2023 pilot blueprint must be resolved in Spain's next-generation pilot (`M10`)?
  - *Hypothesis:* B-MINCOME's restriction to low-income households in Eix Besòs and interaction with state benefit clawbacks prevented identification of middle-class net-taxpayer responses and municipal rent pass-through; Catalonia's protocol solved cluster saturation but lacked fiscal/IRPF competence (`M06`), proving the necessity of a State-backed or Foral-integrated pilot (`M10`).

## 3. State of knowledge
The global empirical literature spans four distinct program archetypes:
1. **European Welfare-State Experiments:** Barcelona's B-MINCOME ($2\times 2$ factorial of conditionality $\times$ benefit clawback rate across 1,000 households [@todeschini-bmincome-2020]) and Finland's nationwide Kela RCT (2,000 unemployed recipients receiving €560/month unconditionally [@kangas-2021-finland]).
2. **US Guaranteed Income Trials:** OpenResearch ($1,000/month for 3 years across $N=1,000$ treated vs. $2,000$ control [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health]) and Stockton SEED ($500/month [@west-2024-seed]).
3. **Permanent Universal Resource Dividends:** Alaska Permanent Fund Dividend (universal annual dividend since 1982 [@jones-marinescu-2022]), showing zero net employment contraction and expansion in non-tradable service jobs.
4. **Spatial Saturation Trials:** GiveDirectly's randomized saturation across 653 Kenyan villages [@egger-2022-ge-kenya; @banerjee-niehaus-suri-2019], proving significant local general-equilibrium fiscal multipliers ($1.3\times$ to $2.4\times$) and modest local inflation.

## 4. Spain context & data sources
- **Primary Spanish Evaluation Datasets:** Ajuntament de Barcelona / Ivàlua B-MINCOME public microdata panels (2017–2019) [@todeschini-bmincome-2020]; Generalitat de Catalunya *Oficina del Pla Pilot per Implementar la RBU* methodological blueprints (2021–2023); Ministry of Inclusion IMV Policy Lab RCT registers.
- **International Register and Experimental Panels:** Finland Kela-register matched data [@kangas-2021-finland]; OpenResearch administrative tax and credit bureau panels [@bartik-2024-openresearch].

## 5. Methods & identification
1. **Life-Cycle Frisch & Windfall Decomposition Equations:**
   - Formalize the mapping from a $T$-period experimental cash transfer $G_{\text{pilot}}$ to permanent life-cycle elasticities following MaCurdy [@macurdy-1981-labor-supply] and Blundell & MaCurdy [@blundell-macurdy-1999-labor-supply]. Under intertemporal separable preferences:
     $$\Delta \ln h_{it} = \varepsilon^{\text{Frisch}} \Delta \ln \lambda_{it} + \varepsilon^c \Delta \ln w_{it}(1 - \tau) + \eta \left[ \frac{G_{\text{pilot}}}{A_{it} + H_{it}} \cdot \frac{1 - (1+r)^{-T}}{1 - (1+r)^{-(T_{\text{ret}} - t)}} \right]$$
     where $\lambda_{it}$ is the marginal utility of wealth, $A_{it}$ is net liquid wealth, $H_{it}$ is human wealth (present discounted value of lifetime earnings), and $T_{\text{ret}} - t$ is remaining working life.
   - Decomposing the temporary windfall from the permanent policy shock isolates the Frisch substitution response ($\varepsilon^{\text{Frisch}} \approx 0.35\text{--}0.55$) from the true permanent compensated elasticity ($\varepsilon^c \approx 0.12\text{--}0.18$) and income elasticity ($\eta \approx -0.05\text{--}-0.08$), preventing short-run trial sabbaticals from distorting permanent labor supply projections in Spain's EUROMOD (`M09`) and HANK (`M04`) models.
2. **Bayesian Hierarchical Meta-Analysis:**
   - Estimate random-effects Bayesian meta-regressions for hours worked and health outcomes, conditioning on transfer generosity relative to local poverty line, marginal clawback rate, register-linkage fidelity, and duration.
3. **Synthesis Matrix of Pilot Lessons for Spain:**
   - Benchmark historical pilots against the 6 core criteria of the Spanish research plan: (i) decile universality, (ii) individual entitlement, (iii) tax-clawback integration, (iv) spatial cluster saturation, (v) administrative register linkage, and (vi) AI exposure stratification.

## 6. Pilot implications
- **Municipal:** Valuable for verifying local administrative delivery and subjective wellbeing (as demonstrated in B-MINCOME [@todeschini-bmincome-2020]), but inherently unsuited for measuring labor supply under a reformed national tax schedule or tracking internal migration spillovers.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común* (Catalonia blueprint), regional pilots resolve spatial cluster saturation but remain constrained by central government control over IRPF and Social Security registers.
  - In *Régimen Foral* (Basque Country / Navarre), regional governments hold the full tax and social security data spine, providing the only sub-national setting capable of testing net-tax integration and replicating international register-linked RCT standards [@kangas-2021-finland].
- **National:** The only scale capable of testing general-equilibrium macroeconomic closure, avoiding territorial leakages, and replicating Alaska-style permanent dividend expectations [@jones-marinescu-2022].

## 7. Risks, counterarguments & open issues
- **Counterargument (Finite-Horizon Over-Estimation of Leisure):** Skeptics argue that participants in 3-year trials take temporary sabbaticals that would not occur under a permanent policy. *Mitigation:* The structural life-cycle decomposition equation explicitly isolates the temporary discount factor, preventing over-estimation of permanent labor supply contraction.
- **Counterargument (Contextual Incomparability of Low-Income Windfalls):** US trials sampled low-income individuals with high baseline marginal utility of cash. *Mitigation:* Ingest priors from the Alaska PFD [@jones-marinescu-2022] and Finland trial [@kangas-2021-finland] which covered broader or universal populations.

## 8. Deliverables & effort
- Meta-Analytic Bayesian Database of Global Basic Income Experiments.
- Structural Parameter Transportability Protocol and B-MINCOME/Catalan Pilot Methodological Assessment for Chapters 1 and 7. (Effort: 4 person-weeks).


<!-- FILE: plan/modules/M16-ai-rent-capture-sovereign-fund.md -->
---
id: M16
title: Capturing AI rents, capital taxation, and sovereign dividend funds
status: draft
locked: false
depends_on: [M01, M03, M04, M06]
covers: [F04]
feeds_chapters: [4]
last_iteration: 2
---
# M16 · Capturing AI rents, capital taxation, and sovereign dividend funds

## 1. Why this matters
Under severe and structural AI displacement scenarios (**S2** and **S3**, `M01`), national income shifts markedly from labor compensation to capital shares, corporate operating profits, intellectual property rents, and cloud/compute returns [@acemoglu-2024-macro-ai; @korinek-suh-2024]. Financing UBR solely through personal income tax (IRPF) labor brackets (`M03`) becomes mathematically unsustainable if Spain's aggregate labor share contracts by 7.0 to 15.0 percentage points of GDP. Because leading generative AI foundation-model developers are foreign multinationals headquartered in the US or China, Spain cannot rely solely on conventional domestic profit taxes—it must establish location-inelastic, destination-based digital consumption levies paired with origin-based factor-neutral corporate operating surplus contributions that fully comply with EU law [@guerreiro-rebelo-teles-2022-robots; @cazzaniga-imf-2024].

## 2. Research questions
- **RQ-M16-01**: What combination of destination-based AI consumption levies, reformed corporate taxation (*Impuesto sobre Sociedades*), and factor-neutral operating surplus contributions can raise 2.5–4.5% of GDP under S2 and S3 while fully complying with Article 401 of the EU VAT Directive (Directive 2006/112/EC [@eu-dir-2006-112-vat])?
  - *Hypothesis:* Structuring the domestic corporate contribution as a direct, origin-based tax on Net Operating Surplus (*Excedente Bruto de Explotación* minus depreciation) without invoice-credit deduction—modeled directly on the CJEU-upheld Italian IRAP precedent (Case C-475/03 *Banca Popolare di Cremona* [@cjeu-c-475-03-banca-popolare-irap])—avoids classification as a turnover tax under Art. 401 of Directive 2006/112/EC while raising 2.8–3.6% of GDP with near-zero capital relocation elasticity. Foreign AI providers are captured via destination-based corporate presence and digital services taxes.
- **RQ-M16-02**: How much net fiscal revenue is generated once baseline Social Security payroll tax losses from displaced human labor are explicitly deducted from corporate surplus tax yields?
  - *Hypothesis:* Under S2 ($\Delta s_L = -7.0$ pp), the gross corporate surplus tax yield of ~2.8% of GDP is partially offset by an automatic loss of ~1.9% of GDP in employer Social Security payroll contributions (*cotizaciones a la Seguridad Social*), yielding a net incremental revenue gain of 0.9–1.2% of GDP that must be bridged by broader wealth and destination-based digital consumption taxes.
- **RQ-M16-03**: How should Spain structure the governance and statutory anti-raiding safeguards of the **Fondo Soberano de Renta Básica y Dividendos de IA** to serve as a sustainable intergenerational stabilization buffer?
  - *Hypothesis:* Earmarking 1.0–1.2% of GDP annually builds an accumulated endowment of 15–20% of GDP by Year 15, yielding a sustainable annual real dividend payout of 0.5–0.8% of GDP/year under a 4% real spending rule. Robust anti-raiding governance—independent management by a Banco de España investment board, a statutory 3/5ths congressional supermajority requirement for capital withdrawals, and a macro-fiscal debt-parity rule modeled on *Ley 28/2003 del Fondo de Reserva de la Seguridad Social* [@boe-ley-28-2003-fondo-reserva]—prevents political expropriation during electoral cycles.

## 3. State of knowledge
Optimal automation-taxation theory [@guerreiro-rebelo-teles-2022-robots; @korinek-suh-2024; @cazzaniga-imf-2024] proves that while taxing intermediate capital inputs (standard computer hardware or software) distorts investment efficiency, taxing pure economic rents, monopoly markups, and automation windfalls is welfare-enhancing when displaced workers face structural retraining frictions. Landmark resource-dividend evidence from Alaska [@jones-marinescu-2022] demonstrates that linking a transparent, ring-fenced capital endowment to an equal annual dividend anchors deep democratic legitimacy (`M11`). However, in the European single market, unilateral fiscal instruments must strictly avoid infringing the EU VAT Directive (prohibiting turnover taxes that mimic VAT) and State Aid prohibitions (`M06`).

## 4. Spain context & data sources
- **Statutory & Tax Framework:**
  - *Ley 27/2014 del Impuesto sobre Sociedades* (corporate income tax base, patent box, and OECD Pillar Two 15% global minimum tax).
  - *Ley 4/2020 del Impuesto sobre Determinados Servicios Digitales* (Spanish Digital Services Tax / Tasa Google).
  - *Ley 38/2022 del Impuesto Temporal de Solidaridad de las Grandes Fortunas* (wealth tax on net fortunes >€3M).
  - *Ley 9/2017 de Contratos del Sector Público* [@boe-ley-9-2017-contratos] (procurement rules for public data compute assets).
  - *Ley 28/2003 del Fondo de Reserva de la Seguridad Social* [@boe-ley-28-2003-fondo-reserva] (governance model for statutory reserve funds).
  - Article 401 of EU Directive 2006/112/EC [@eu-dir-2006-112-vat] and CJEU Case C-475/03 (*Banca Popolare di Cremona* [@cjeu-c-475-03-banca-popolare-irap]), alongside the EU AI Act [@eu-ai-act-2024].
- **Firm-Level and National Accounts Microdata:**
  - AEAT *Cuentas Anuales en el Impuesto sobre Sociedades* (balance-sheet and tax filings of Spanish corporate taxpayers).
  - Banco de España *Central de Balances Integrada* (CBI) covering gross operating surplus, depreciation, and wage bills across non-financial corporations.
  - INE *Contabilidad Nacional de España* (EBE and factor shares by NACE sector).

## 5. Methods & identification
1. **Factor-Neutral Net Operating Surplus Contribution (The IRAP Architecture):**
   - Design a tax base $B_{\text{surplus}} = \text{EBE} - \delta K = \text{Value Added} - \text{Personnel Costs} - \text{Depreciation}$.
   - By levying the rate directly on the net operating margin rather than transaction invoices, the tax does not constitute a turnover tax under Art. 401 of Directive 2006/112/EC.
   - Contrast this with human payroll taxes: as firms automate, human payroll taxes decline while $B_{\text{surplus}}$ expands, equalizing the marginal tax burden between labor-intensive and automated capital-intensive production modes.
2. **Double-Counting Correction in S1–S3 Fiscal Accounting:**
   - Ingest labor displacement vectors from `M01` to compute the simultaneous loss in employee and employer Social Security contributions: $\Delta \text{Rev}_{\text{net}} = \tau_{\text{surplus}} \Delta \text{EBE} - \tau_{\text{SS}} \Delta W \cdot L$.
   - Feed corrected net revenue paths into the consolidated Administraciones Públicas fiscal bridge (`M03`).
3. **Actuarial Sovereign Fund Accumulation & Governance Model:**
   - Simulate the 30-year accumulation trajectory of the *Fondo Soberano de Dividendos de IA*:
     $$F_{t+1} = (1 + r_t - \pi_t) F_t + S_t - D_t$$
     where $S_t$ is annual statutory inflow, $r_t - \pi_t$ is the real portfolio return (calibrated at 4.0% real return on global equity/bond indices), and $D_t \le 0.04 F_t$ is the sustainable dividend payout rule yielding 0.5–0.8% of GDP/year.
   - Formalize statutory anti-raiding governance: independent executive board under Banco de España oversight, a 3/5ths congressional supermajority requirement for capital principal drawdown, and debt-neutrality constraints per *Ley 28/2003* [@boe-ley-28-2003-fondo-reserva].

## 6. Pilot implications
- **Municipal:** Municipalities have no legal competence over corporate income tax, wealth taxation, or capital sovereign funds under *Ley 7/1985* (LBRL); municipal pilots must be entirely funded through external transfers or municipal budget reallocations.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común*, autonomous communities possess wealth tax regulatory autonomy (*Impuesto sobre el Patrimonio*), but cannot enact autonomous corporate surplus taxes or digital services taxes.
  - In *Régimen Foral* (Basque Country and Navarre), provincial treasuries possess exclusive competence over the *Impuesto sobre Sociedades foral* under the *Concierto Económico*, providing the only sub-national jurisdiction with the legal power to pilot a factor-neutral operating surplus contribution.
- **National:** The definitive level for national corporate tax reform, execution of the IRAP-style Net Operating Surplus contribution, collection of the Digital Services Tax, and capitalization of the State Sovereign Dividend Fund.

## 7. Risks, counterarguments & open issues
- **Counterargument (Capital Flight and Relocation of R&D):** Critics argue that taxing corporate surpluses will cause high-tech firms to abandon Spain. *Mitigation:* The tax base is origin-based accounting operating surplus on domestic activity (non-financial firms serving the Spanish market) combined with destination-based digital services levies on consumption within Spain, neutralizing cross-border flight incentives.
- **Counterargument (Sovereign Fund Dividend Lag):** An accumulated fund cannot solve the immediate fiscal shock of S2 AI displacement in Year 1. *Mitigation:* The fund is designed as a long-term co-financing anchor for the transition to Tier C, while initial Tier A/B financing is carried by reformed IRPF (`M03`).

## 8. Deliverables & effort
- Actuarial Accumulation and Dynamic Revenue Model for the Sovereign AI Dividend Fund across S1–S3.
- Legal Specification of the Factor-Neutral Net Operating Surplus Contribution (Directive 2006/112/EC Compliance) for Chapter 4. (Effort: 5 person-weeks).


<!-- FILE: plan/modules/M17-transition-risks-stress-tests.md -->
---
id: M17
title: Transition path, scenario triggers, and tail-risk stress tests
status: draft
locked: false
depends_on: [M01, M03, M04, M05, M07, M10, M11, M16]
covers: [F17]
feeds_chapters: [8]
last_iteration: 2
---
# M17 · Transition path, scenario triggers, and tail-risk stress tests

## 1. Why this matters
Transitioning overnight from Spain's fragmented, means-tested welfare system to a universal Tier B or Tier C cash transfer would generate severe macroeconomic friction, inflationary risks, and fiscal deficit spikes. Conversely, an open-ended pilot without statutory scale-up rules risks political abandonment (`M11`). A state-of-the-art research plan must establish a phased, reversible **Transition Roadmap** governed by independent macroeconomic triggers, automatic fiscal and housing circuit-breakers (`M03`, `M05`), and adversarial tail-risk stress tests. Crucially, transition governance must fully respect the constitutional Principle of Tax Legality (Arts. 31.3 and 134.7 CE [@boe-ce-1978]) and the statutory organic mandate of AIReF under *Ley Orgánica 6/2013* [@boe-lo-6-2013-airef], ensuring that technical certifications lead to expedited democratic ratification rather than unlawful administrative tax delegation.

## 2. Research questions
- **RQ-M17-01**: What phased sequencing—from Phase 0 (unification and automatic individualization of IMV + CAPI) to Phase 1 (Multi-Level Pilot `M10` and Tier A €600 floor under S1), Phase 2 (Tier B €900 poverty-line UBR under S2), and Phase 3 (Tier C €1,200 AI-dividend UBR under S3)—minimizes transition costs while maintaining structural fiscal balance?
  - *Hypothesis:* A state-contingent roadmap governed by an AIReF-certified **Cyclically and Terms-of-Trade-Adjusted Composite Displacement Index** ($I_{\text{AI},t}$) informing a statutory Fast-Track Parliamentary Ratification Protocol under Art. 86 CE keeps the structural primary balance within $\pm 0.35\%$ of GDP throughout the transition while ensuring zero real disposable income loss for vulnerable cohorts via the `M07` guarantee.
- **RQ-M17-02**: How can immediate fiscal and housing circuit-breakers—specifically the **Housing Pass-Through Circuit-Breaker** (`M05`) and the **Fast-Track Fiscal Stabilization Surcharge**—cool short-run demand shocks and preserve fiscal stability under *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] without waiting for multi-year public housing construction?
  - *Hypothesis:* When local rental index growth exceeds core CPI by >3.0 pp in stressed zones (ZMRT), triggering immediate regulatory/fiscal levers (temporary revocation of LIRPF Art. 23.2 landlord tax deductions from 50% to 0%, emergency extension of price caps to seasonal/room rentals, and municipal *tanteo y retracto* acquisitions) suppresses rent pass-through by >65% within two quarters. Coupling this with an expedited countercyclical IRPF surcharge stabilizes aggregate demand under Art. 86 CE decree-laws without violating Tax Legality.

## 3. State of knowledge
Macroeconomic stabilization theory emphasizes that rule-based automatic stabilizers substantially outperform discretionary interventions, which suffer from implementation lags [@auclert-rognlie-straub-2024; @kaplan-moll-violante-2018-hank]. Under technological uncertainty, state-contingent policy schedules indexed to verified structural shifts in national factor shares are strictly superior to fixed-calendar dates [@korinek-suh-2024; @cazzaniga-imf-2024]. In Spain's constitutional order, however, Articles 31.3 and 134.7 CE strictly prohibit delegating the establishment or modification of tax rates to executive agencies or independent authorities without parliamentary enactment (*Principio de Legalidad Tributaria*). AIReF's mandate under *Ley Orgánica 6/2013* [@boe-lo-6-2013-airef] is strictly non-binding and evaluative ('comply or explain'). Therefore, triggers must operate as mandatory statutory fast-tracks for legislative ratification. In housing, empirical literature confirms that public housing construction lags (4–7 years) cannot solve short-run cash-transfer rent capture, necessitating immediate fiscal-deduction and regulatory circuit-breakers [@garcia-montalvo-2023-rent-controls; @jofre-monseny-2023-rent-control].

## 4. Spain context & data sources
- **Independent Fiscal Governance:** *Autoridad Independiente de Responsabilidad Fiscal* (AIReF, statutory evaluation mandate under *Ley Orgánica 6/2013* [@boe-lo-6-2013-airef]), Banco de España, and INE National Accounts.
- **Constitutional & Fiscal Statutes:** *Constitución Española* (Arts. 31.3, 86, 134.7 CE [@boe-ce-1978]), *Ley Orgánica 2/2012 de Estabilidad Presupuestaria* (LOEPSF [@boe-loepsf-2012]), reformed EU fiscal framework (*Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework]), and *Ley 12/2023 por el derecho a la vivienda* [@boe-vivienda-2023].

## 5. Methods & identification
1. **The AIReF Technical Certification & Fast-Track Protocol ($I_{\text{AI},t}$):**
   - AIReF audits and certifies the multi-variable composite displacement index:
     $$I_{\text{AI},t} = \omega_1 \Delta \tilde{s}_{L,t} + \omega_2 u_{\text{cognitive},t} + \omega_3 \left(\frac{\Delta \text{EBE}_{\text{tech},t}}{\text{GDP}_t}\right)$$
     where $\Delta \tilde{s}_{L,t}$ is the cyclically adjusted labor share, $u_{\text{cognitive},t}$ is cognitive occupational displacement (`M01`), and $\Delta \text{EBE}_{\text{tech},t}$ is automation operating surplus (`M16`).
   - Trigger bands: $I_{\text{AI}} < 1.0 \implies \text{Phase 1 (Tier A)}$; $1.0 \le I_{\text{AI}} < 2.5 \implies \text{Phase 2 (Tier B)}$; $I_{\text{AI}} \ge 2.5 \implies \text{Phase 3 (Tier C)}$.
   - Upon certification, the statute mandates the Government to enact a Royal Decree-Law (*Real Decreto-ley* under Art. 86 CE) within 30 days submitted to the *Congreso de los Diputados* for immediate ratification, guaranteeing full compliance with Arts. 31.3 and 134.7 CE.
2. **The Housing Pass-Through Circuit-Breaker (`M05`):**
   - If quarterly rental index growth exceeds core CPI by >3.0 pp in designated *zonas de mercado residencial tensionado* (ZMRT), an immediate emergency package activates by statutory mandate:
     (i) Dynamic revocation of LIRPF Art. 23.2 landlord rental income deductions (dropping from 50% to 0% for non-compliant landlords),
     (ii) Statutory extension of price ceilings to seasonal (LAU Art. 3.2) and room rentals (CC Art. 1554),
     (iii) Fast-track municipal preferential acquisition rights (*tanteo y retracto*) on corporate-owned residential assets.
3. **Compound Tail-Risk Stress-Test Battery:**
   - *Stress 1 (Energy Stagflation + S2 AI Displacement):* 50% energy import price shock combined with $-7.0$ pp labor share collapse.
   - *Stress 2 (High-Income Tax Evasion Surge):* Elasticity of taxable income (ETI) doubling to $e = 0.50$ among the top 1% of earners.
   - *Stress 3 (Metropolitan Housing Supply Bottleneck):* Inelastic rental supply ($\varepsilon_s = 0.10$) accelerating rent pass-through to $45\%$ in Madrid and Barcelona.
   - *Stress 4 (Sovereign Debt Selloff):* 150 bps widening in Spain's 10-year sovereign bond spread under rising ECB policy rates.

## 6. Pilot implications
- **Municipal:** Valuable for field-testing local operational disconfirmation criteria (e.g. municipal registration bottlenecks or local service utilization spikes), but lacks the macroeconomic scale to evaluate national sovereign spreads, cyclically adjusted labor-share triggers, or currency-union inflation dynamics.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común*, regional debt limits under LOEPSF [@boe-loepsf-2012] require pilot funding to be structurally neutral; stress-testing must account for regional debt sustainability under CPFF oversight.
  - In *Régimen Foral* (Basque Country / Navarre), autonomous borrowing powers and the *Cupo* mechanism provide insulation against central budgetary freezes, allowing for high-stress experimental stability.
- **National:** The only jurisdictional level where the full AIReF composite trigger framework, the Fast-Track Parliamentary Ratification Protocol under Art. 86 CE, and EU fiscal rule compliance under *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] can be stress-tested against sovereign debt markets.

## 7. Risks, counterarguments & open issues
- **Counterargument (Democratic Deficit of Algorithmic Triggers):** Entrusting benefit levels and tax surcharges to automated mathematical formulas removes democratic accountability and violates Tax Legality (Arts. 31.3 and 134.7 CE). *Mitigation:* Under the reformed design, AIReF operates strictly within its organic evaluative mandate (LO 6/2013 [@boe-lo-6-2013-airef]) as an independent auditor issuing non-binding Technical Transition Reports. Concrete tax rates and benefit phase transitions are enacted via fast-track Royal Decree-Laws under Art. 86 CE and formally ratified by the *Congreso de los Diputados*.
- **Counterargument (Inflationary Inertia):** Cash transfers could create persistent wage-price spirals in a booming economy. *Mitigation:* The expedited countercyclical fiscal surcharge and the immediate Housing Circuit-Breaker act in real time to absorb excess purchasing power from high-income deciles and prevent rental inflation.

## 8. Deliverables & effort
- State-Contingent Transition Roadmap and AIReF Composite Trigger Certification Protocol.
- Quantitative Tail-Risk Stress-Test Suite and Disconfirmation Matrix for Chapter 8. (Effort: 5 person-weeks).


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
| albanesi-2023-ai-europe | Albanesi, S.; Dias da Silva, A.; Jimeno, J. F. | 2023 | New Technologies and Jobs in Europe | doi:10.3386/w31357 | yes |
| bentolila-2012-dual-spain | Bentolila, S.; Dolado, J. J.; Jimeno, J. F. | 2012 | Reforming an insider-outsider labor market: the Spanish experience | doi:10.1186/2193-9012-1-4 | yes |
| boe-rdl-32-2021-reforma-laboral | Jefatura del Estado | 2021 | Real Decreto-ley 32/2021, de medidas urgentes para la reforma laboral (BOE-A-2021-21788) | https://www.boe.es/buscar/act.php?id=BOE-A-2021-21788 | yes |
| boe-rd-789-2022-incentivo-imv | Ministerio de Inclusión, Seguridad Social y Migraciones | 2022 | Real Decreto 789/2022, de compatibilidad del IMV con rentas del trabajo (BOE-A-2022-15764) | https://www.boe.es/buscar/act.php?id=BOE-A-2022-15764 | yes |
| boe-ley-dependencia-2006 | Jefatura del Estado | 2006 | Ley 39/2006, de Promoción de la Autonomía Personal y Atención a las personas en situación de dependencia (BOE-A-2006-21990) | https://www.boe.es/buscar/act.php?id=BOE-A-2006-21990 | yes |
| gali-monacelli-2005-soe | Galí, J.; Monacelli, T. | 2005 | Monetary Policy and Exchange Rate Volatility in a Small Open Economy | doi:10.1111/j.1467-937X.2005.00349.x | yes |
| eu-reg-2024-1263-fiscal-framework | European Parliament and Council | 2024 | Regulation (EU) 2024/1263 on the effective coordination of economic policies and multilateral budgetary surveillance | https://eur-lex.europa.eu/eli/reg/2024/1263/oj | yes |
| boe-loepsf-2012 | Jefatura del Estado | 2012 | Ley Orgánica 2/2012, de Estabilidad Presupuestaria y Sostenibilidad Financiera (BOE-A-2012-5730) | https://www.boe.es/buscar/act.php?id=BOE-A-2012-5730 | yes |
| boe-ley-financiacion-ccaa-2009 | Jefatura del Estado | 2009 | Ley 22/2009, de financiación de las Comunidades Autónomas de régimen común (BOE-A-2009-20375) | https://www.boe.es/buscar/act.php?id=BOE-A-2009-20375 | yes |
| boe-concierto-vasco-2002 | Jefatura del Estado | 2002 | Ley 12/2002, por la que se aprueba el Concierto Económico con la CAPV (BOE-A-2002-9969) | https://www.boe.es/buscar/act.php?id=BOE-A-2002-9969 | yes |
| boe-convenio-navarra-1990 | Jefatura del Estado | 1990 | Ley 28/1990, por la que se aprueba el Convenio Económico con Navarra (BOE-A-1990-31117) | https://www.boe.es/buscar/act.php?id=BOE-A-1990-31117 | yes |
| almunia-lopez-rodriguez-2019-eti | Almunia, M.; Lopez-Rodriguez, D. | 2019 | The elasticity of taxable income in Spain: 1999–2014 | doi:10.1007/s13209-019-00208-x | yes |
| boe-iva-1992 | Jefatura del Estado | 1992 | Ley 37/1992, del Impuesto sobre el Valor Añadido (BOE-A-1992-28740) | https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740 | yes |
| boe-sociedades-2014 | Jefatura del Estado | 2014 | Ley 27/2014, del Impuesto sobre Sociedades (BOE-A-2014-12328) | https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 | yes |
| eu-dir-2006-112-vat | Council of the European Union | 2006 | Council Directive 2006/112/EC on the common system of value added tax | https://eur-lex.europa.eu/eli/dir/2006/112/oj | yes |
| tc-stc-158-2021-imv | Tribunal Constitucional | 2021 | STC 158/2021, sobre el Ingreso Mínimo Vital (BOE-A-2021-17107) | https://www.boe.es/buscar/doc.php?id=BOE-A-2021-17107 | yes |
| tc-stc-19-2024-imv-foral | Tribunal Constitucional | 2024 | STC 19/2024, sobre la gestión foral del Ingreso Mínimo Vital (BOE-A-2024-3941) | https://www.boe.es/buscar/doc.php?id=BOE-A-2024-3941 | yes |
| eu-dir-2004-38-free-movement | European Parliament and Council | 2004 | Directive 2004/38/EC on the right of citizens of the Union to move and reside freely | https://eur-lex.europa.eu/eli/dir/2004/38/oj | yes |
| boe-trlgss-2015 | Ministerio de Empleo y Seguridad Social | 2015 | Real Decreto Legislativo 8/2015, Texto Refundido de la Ley General de la Seguridad Social (BOE-A-2015-11724) | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 | yes |
| boe-rdl-2-2024-desempleo | Jefatura del Estado | 2024 | Real Decreto-ley 2/2024, de simplificación y mejora del nivel asistencial por desempleo (BOE-A-2024-10235) | https://www.boe.es/buscar/act.php?id=BOE-A-2024-10235 | yes |
| boe-lgt-2003 | Jefatura del Estado | 2003 | Ley 58/2003, General Tributaria (BOE-A-2003-23186) | https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186 | yes |
| boe-lopdgdd-2018 | Jefatura del Estado | 2018 | Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales (BOE-A-2018-16673) | https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673 | yes |
| boe-lpac-2015 | Jefatura del Estado | 2015 | Ley 39/2015, del Procedimiento Administrativo Común de las Administraciones Públicas (BOE-A-2015-10565) | https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565 | yes |
| boe-extranjeria-2000 | Jefatura del Estado | 2000 | Ley Orgánica 4/2000, sobre derechos y libertades de los extranjeros en España (BOE-A-2000-544) | https://www.boe.es/buscar/act.php?id=BOE-A-2000-544 | yes |
| boe-lbrl-1985 | Jefatura del Estado | 1985 | Ley 7/1985, Reguladora de las Bases del Régimen Local (BOE-A-1985-5392) | https://www.boe.es/buscar/act.php?id=BOE-A-1985-5392 | yes |
| borusyak-2022-shift-share | Borusyak, K.; Hull, P.; Jaravel, X. | 2022 | Quasi-Experimental Shift-Share Research Designs | doi:10.1093/restud/rdab030 | yes |
| chiappori-1992-collective | Chiappori, P.-A. | 1992 | Collective Labor Supply and Welfare | doi:10.2307/2951541 | yes |
| baird-2018-interference | Baird, S.; Bohren, J. A.; McIntosh, C. | 2018 | Optimal Design of Experiments in the Presence of Interference | doi:10.1162/rest_a_00716 | yes |
| duflo-2007-randomization | Duflo, E.; Glennerster, R.; Kremer, M. | 2007 | Using Randomization in Development Economics Research: A Toolkit | doi:10.1016/S1573-4471(07)04061-2 | yes |
| saez-2010-bunching | Saez, E. | 2010 | Do Taxpayers Bunch at Kink Points? | doi:10.1257/pol.2.3.180 | yes |
| chetty-2012-bounds | Chetty, R. | 2012 | Bounds on Elasticities with Optimization Frictions: A Synthesis of Micro and Macro Evidence on Labor Supply | doi:10.3982/ECTA9043 | yes |
| macurdy-1981-labor-supply | MaCurdy, T. E. | 1981 | An Empirical Model of Labor Supply in a Life-Cycle Setting | doi:10.1086/261023 | yes |
| blundell-macurdy-1999-labor-supply | Blundell, R.; MaCurdy, T. | 1999 | Labor Supply: A Review of Alternative Approaches | doi:10.1016/S1573-4463(99)03008-4 | yes |
| ponthieux-2013-income-pooling | Ponthieux, S. | 2013 | Income pooling and equal sharing within the household: What can we learn from the 2010 EU-SILC module? | doi:10.2785/21993 | yes |
| garcia-montalvo-2023-rent-controls | García-Montalvo, J.; Monràs, J. | 2023 | The Effect of Second-Generation Rent Controls: New Evidence from Catalonia | doi:10.24148/wp2023-28 | yes |
| jofre-monseny-2023-rent-control | Jofre-Monseny, J.; Martínez-Mazza, R.; Segú, M. | 2023 | Effectiveness and supply effects of high-coverage rent control policies | doi:10.1016/j.regsciurbeco.2023.103916 | yes |
| antolin-bover-1997-migration | Antolín, P.; Bover, O. | 1997 | Regional Migration in Spain: The Effect of Personal Characteristics and of Unemployment, Wage and House Price Differentials Using Pooled Cross-Sections | doi:10.1111/1468-0084.00062 | yes |
| tsebelis-2002-veto-players | Tsebelis, G. | 2002 | Veto Players: How Political Institutions Work | doi:10.1515/9781400831456 | yes |
| vanderborght-2006-trade-unions | Vanderborght, Y. | 2006 | Why Trade Unions Oppose Basic Income | doi:10.2202/1932-0183.1002 | yes |
| vlandas-2019-politics-ubi | Vlandas, T. | 2019 | The Politics of the Basic Income Guarantee: Analysing Individual Support in Europe | doi:10.1515/bis-2018-0021 | yes |
| beramendi-2012-inequality | Beramendi, P. | 2012 | The Political Geography of Inequality: Regions and Redistribution | doi:10.1017/CBO9781139042796 | yes |
| puig-segura-2021-discapacidad | Puig i Gabau, J.; Segura Bonet, M. | 2021 | El agravio comparativo económico de las personas con discapacidad de la ciudad de Barcelona | https://www.cedid.es/redis/index.php/redis/article/view/646 | yes |
| boe-lo-6-2013-airef | Jefatura del Estado | 2013 | Ley Orgánica 6/2013, de 14 de noviembre, de creación de la Autoridad Independiente de Responsabilidad Fiscal (BOE-A-2013-11935) | https://www.boe.es/eli/es/lo/2013/11/14/6 | yes |
| boe-ley-28-2003-fondo-reserva | Jefatura del Estado | 2003 | Ley 28/2003, de 29 de septiembre, reguladora del Fondo de Reserva de la Seguridad Social (BOE-A-2003-18089) | https://www.boe.es/eli/es/l/2003/09/29/28 | yes |
| boe-ley-9-2017-contratos | Jefatura del Estado | 2017 | Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público (BOE-A-2017-12902) | https://www.boe.es/eli/es/l/2017/11/08/9 | yes |
| cjeu-c-279-93-schumacker | Court of Justice of the European Union | 1995 | Case C-279/93 Finanzamt Köln-Altstadt v Roland Schumacker (Freedom of movement for workers - Non-resident income taxation) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:61993CJ0279 | yes |
| cjeu-c-475-03-banca-popolare-irap | Court of Justice of the European Union | 2006 | Case C-475/03 Banca Popolare di Cremona (Sixth VAT Directive Article 33 - Regional tax on productive activities IRAP) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62003CJ0475 | yes |
| boe-rd-888-2022-discapacidad | Ministerio de Derechos Sociales y Agenda 2030 | 2022 | Real Decreto 888/2022, de 18 de octubre, por el que se establece el procedimiento para el reconocimiento, declaración y calificación del grado de discapacidad (BOE-A-2022-17108) | https://www.boe.es/eli/es/rd/2022/10/18/888 | yes |
| boe-lau-1994 | Jefatura del Estado | 1994 | Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos (BOE-A-1994-26003) | https://www.boe.es/eli/es/l/1994/11/24/29 | yes |
| airef-opinion-imv-2023 | Autoridad Independiente de Responsabilidad Fiscal (AIReF) | 2023 | Segunda Opinión sobre el Ingreso Mínimo Vital | https://www.airef.es/es/centro-documental/opiniones/segunda-opinion-sobre-el-ingreso-minimo-vital/ | yes |
| airef-opinion-imv-2024 | Autoridad Independiente de Responsabilidad Fiscal (AIReF) | 2024 | Tercera Opinión sobre el Ingreso Mínimo Vital | https://www.airef.es/es/centro-documental/opiniones/tercera-opinion-sobre-el-ingreso-minimo-vital/ | yes |
