# Research Plan Improvement Report

**Status:** `continue`

**Reasons / SOTA gates:**
- 1/3 iterations in this cycle

## Score History

| Iteration | Weighted | Delta | Min Criterion | Open Critical | Coverage | Verified Sources |
|---|---:|---:|---:|---:|---:|---:|
| `iter-0001` | **4.65** | — | 4.40 | 0 | 100% | 100% |

## Rubric Breakdown (`iter-0001`)

| Criterion | Weight | Score | Delta |
|---|---:|---:|---:|
| Coverage of factors (`coverage`) | 0.12 | 4.60 | — |
| Research question quality (`rq_quality`) | 0.12 | 4.70 | — |
| Methodological rigor (`methodological_rigor`) | 0.14 | 4.60 | — |
| Evidence grounding (`evidence_grounding`) | 0.12 | 4.70 | — |
| Spain institutional fit (`spain_fit`) | 0.12 | 4.80 | — |
| Treatment of AI-displacement scenarios (`ai_scenarios`) | 0.08 | 4.50 | — |
| Feasibility (data, time, budget) (`feasibility`) | 0.08 | 4.40 | — |
| Internal coherence (`internal_coherence`) | 0.08 | 4.70 | — |
| Counterarguments and risks (`counterarguments`) | 0.08 | 4.70 | — |
| Ethics and equity (`ethics_equity`) | 0.06 | 4.80 | — |

## Latest Iteration Details (`iter-0001`)

### Judge Assessment

The Universal Basic Rent (Spain) research plan represents a comprehensive, methodologically sophisticated, and institutionally precise framework that is exceptionally close to state-of-the-art academic publication and policy readiness. It successfully synthesizes frontier empirical UBI literature (OpenResearch, Finland, B-MINCOME, Kenya, Alaska) with granular Spanish public finance, labor economics, and constitutional jurisprudence. By establishing a rigorous Status-Quo Budget Neutrality constraint, a Dual-Pillar contributory pension integration with an inviolable No-Loser Guarantee, a two-sector currency-union HANK open-economy closure, a statistically powered two-stage spatial saturation RCT with legally compliant clawback arms, and an AIReF-certified composite displacement trigger framework, the plan establishes an audit-ready blueprint capable of withstanding scrutiny by top academic journals, AIReF, the Instituto de Estudios Fiscales, and international bodies.

### Latest Changelog

# Changelog — Iteration 0001 (`iter-0001`)

## Overview
Iteration 0001 resolved critical fiscal, accounting, legal, and causal-identification gaps identified across 5 specialist reviews (`labor-economist`, `public-finance`, `macroeconomist`, `spanish-eu-law`, and `red-team`). A total of 10 high-leverage synthesis proposals (`SYN-01-01` through `SYN-01-10`) were executed across `plan/00-scope.md`, `plan/methods.md`, all 17 factor modules (`plan/modules/M01`–`M17`), and `plan/sources.yaml`.

All 62 cited academic papers, statutory texts, and legal rulings are 100% machine-verified over HTTP. 100% of reference factors (F01–F17) are covered.

---

## Applied Changes by Proposal

### `SYN-01-01` · Status-Quo Fiscal Neutrality & Dual-Pillar Pension Integration
- **Contributing Issues:** `RT-01-01` (critical), `RT-01-02` (critical), `PF-01-01` (critical), `LW-01-02` (critical)
- **Target Files:**
  - `plan/modules/M03-fiscal-financing.md`
  - `plan/modules/M07-welfare-benefit-integration.md`
  - `plan/modules/M09-distribution-poverty-euromod.md`
- **Summary of Changes:**
  - In `M03`, resolved the UBI accounting fallacy by establishing an explicit **Status-Quo Budget Neutrality Constraint**: post-reform IRPF revenues must cover 100% of baseline public services (~€125B/year) plus gross UBR outlays minus abolished non-contributory benefits. Defined the gross zero point ($T_{\text{new}}(y) = \text{UBR}$) vs. net disposable income breakeven ($\Delta T(y) \ge \text{UBR}$), situating net-contributor breakeven between the 82nd and 86th income percentiles.
  - Formulated the consolidated Administraciones Públicas fiscal bridge explicitly integrating LIRPF Art. 20 (earned-income reduction) and Art. 84 (joint-filing reduction) into the integrated tariff.
  - In `M07`, corrected the order-of-magnitude pension arithmetic error: distinguished retained contributory pensions (~5.5–6.0% GDP above the floor) from the incremental tax-neutrality top-up (<0.6% GDP).
  - Designed the **Dual-Pillar Contributory Architecture** preserving marginal returns to Social Security contributions and introducing the EUROMOD *Complemento de Neutralidad Fiscal* to guarantee zero disposable-income losses for existing pensioners. Preserved Art. 280 TRLGSS retirement contribution credits for displaced workers aged 52+.
  - In `M09`, integrated status-quo budget neutrality, breakeven percentiles, and the *Complemento de Neutralidad Fiscal* into microsimulation poverty benchmarks.

### `SYN-01-02` · Constitutional Competence, EU Free Movement, and Tax-Benefit Symmetry
- **Contributing Issues:** `LW-01-01` (critical), `LW-01-04` (critical), `PF-01-01` (critical)
- **Target Files:**
  - `plan/modules/M06-constitutional-eu-law.md`
  - `plan/modules/M13-migration-territory-residency.md`
- **Summary of Changes:**
  - In `M06`, discarded the legally unsound Annex X Regulation 883/2004 SNCB defense; established a bifurcated EU law architecture granting immediate pro-rata IRPF tax credit treatment to economically active EU workers/self-employed under Art. 45 TFEU and Directive 2004/38/EC, while reserving waiting periods strictly for inactive third-country and EU entrants.
  - Replaced prose legal references with verified statutory citations to *Tribunal Constitucional* IMV competence judgments: STC 158/2021 (`tc-stc-158-2021-imv`) and STC 19/2024 (`tc-stc-19-2024-imv-foral`). Incorporated statutory revenue-sharing mechanics for the 50% ceded regional IRPF under *Ley 22/2009* (`boe-ley-financiacion-ccaa-2009`) and the Basque *Concierto Económico* (`boe-concierto-vasco-2002`).
  - In `M13`, established the binding **Tax-Benefit Symmetry Principle** (Art. 31.1 CE): any legal resident paying reformed Spanish IRPF without the personal minimum (*mínimo personal*) must receive the UBR credit from month one.

### `SYN-01-03` · Multi-Level Pilot Redesign & Experimental Power Calibration
- **Contributing Issues:** `RT-01-03` (critical)
- **Target Files:**
  - `plan/modules/M10-pilot-evaluation-design.md`
- **Summary of Changes:**
  - Expanded the two-stage spatial saturation cluster design from 18 units to $J = 60\text{–}80$ spatial clusters (35 treated vs. 35 control census-tract groups / municipalities) to secure genuine 80% statistical power for detecting local general-equilibrium rent pass-through and wage spillovers via wild cluster bootstrap and randomization inference.
  - Replaced the legally unviable randomized tax-increase arm (which violated Arts. 14 and 31.1 CE) with a randomized **Benefit Phase-Out / Clawback Rate Arm** ($0\%$, $38\%$, $50\%$ clawback capped at the experimental grant), cleanly identifying compensated substitution elasticities.
  - Reconciled the 36-month pilot budget (€432M–€648M gross; €295M net after clawbacks) without relying on EU ESF+ poverty funds for non-vulnerable universal cohorts.

### `SYN-01-04` · Spanish Labor Institutions, Collective Bargaining, and AI Shock Mapping
- **Contributing Issues:** `LE-01-01` (critical), `MA-01-03` (major), `RT-01-05` (major)
- **Target Files:**
  - `plan/modules/M01-ai-labor-displacement.md`
  - `plan/methods.md`
- **Summary of Changes:**
  - Separated gross US O*NET task exposure from net equilibrium employment/wage displacement in Spain, incorporating ESCO/PIAAC task weights, ETICCE firm-size adoption thresholds, and Acemoglu-Restrepo cost-saving parameters.
  - Modeled how binding sectoral collective bargaining (*convenios colectivos* under *Real Decreto-ley 32/2021*) and statutory SMI floors channel AI displacement into intermittent contract inactivity (*pases a inactividad de fijos discontinuos* in MCVL) and ERTE/RED hours adjustments rather than uniform wage cuts.
  - Completed macroeconomic scenario vectors pairing S1–S3 labor-share shifts with explicit TFP growth bands, capital shares, and domestic vs. foreign AI rent splits. Formalized shift-share IV identification bounds per Borusyak, Hull, & Jaravel (2022).

### `SYN-01-05` · Eurozone Open-Economy HANK Block & Fiscal Rules Compliance
- **Contributing Issues:** `MA-01-01` (critical)
- **Target Files:**
  - `plan/modules/M04-macroeconomics-eurozone.md`
- **Summary of Changes:**
  - Formalized the open-economy currency-union HANK model with fixed nominal exchange rate, area-wide ECB Taylor rule, terms-of-trade competitiveness channel, and endogenous Bonos-Bund sovereign spread transmission.
  - Embedded full compliance with the reformed EU fiscal governance framework under *Regulation (EU) 2024/1263* and Spain's *Ley Orgánica 2/2012* (LOEPSF), specifying how gross UBR expenditures are legally netted against Discretionary Revenue Measures (MDI) to respect the Net Primary Expenditure Ceiling.
  - Modeled dual external leakage in the Balance of Payments: household consumer imports by decile plus B2B cloud and AI model compute imports.

### `SYN-01-06` · Iterative Micro-Macro General-Equilibrium Closure Protocol
- **Contributing Issues:** `MA-01-02` (major), `PF-01-05` (major), `LE-01-05` (major)
- **Target Files:**
  - `plan/methods.md`
  - `plan/modules/M03-fiscal-financing.md`
  - `plan/modules/M04-macroeconomics-eurozone.md`
- **Summary of Changes:**
  - Specified the four-stage **Iterative Micro-Macro Closure Protocol** linking EUROMOD-Spain (`M03`/`M08`/`M09`) and the Spanish Eurozone HANK model (`M04`):
    - Stage 1: CNO-11 displacement mapped to micro-records via MCVL transition matrices.
    - Stage 2: EUROMOD iterates with labor supply (`M08`) and taxable income elasticity (`M03`) to solve for the revenue-neutral tariff.
    - Stage 3: Decile transfers and marginal tax wedges fed into HANK to solve for equilibrium wages, non-tradable/housing inflation, and real GDP.
    - Stage 4: HANK equilibrium price/wage vectors feed back into EUROMOD via a Gauss-Seidel fixed-point loop until the structural primary balance converges within $\pm 0.05\%$ of GDP.

### `SYN-01-07` · Factor-Neutral AI Rent Capture & EU VAT Directive Compliance
- **Contributing Issues:** `RT-01-04` (major), `PF-01-03` (major)
- **Target Files:**
  - `plan/modules/M16-ai-rent-capture-sovereign-fund.md`
- **Summary of Changes:**
  - Redesigned the domestic AI factor-neutral contribution as a direct levy on accounting Net Operating Surplus (*Excedente Bruto de Explotación* net of depreciation) without invoice-credit deduction—modeled on the CJEU-upheld Italian IRAP framework (Case C-475/03)—to guarantee full compliance with Article 401 of EU VAT Directive 2006/112/EC (`eu-dir-2006-112-vat`).
  - Explicitly deducted S2/S3 baseline Social Security payroll tax losses from gross corporate yields to prevent double-counting.
  - Revised `RQ-M16-03` to distinguish the ~15–20% of GDP accumulated endowment stock at year 15 from its sustainable annual real dividend payout (~0.5–0.8% GDP/year under a 4% spending rule).

### `SYN-01-08` · Baseline Welfare-Trap Calibration with RD 789/2022 & Transportable Elasticities
- **Contributing Issues:** `LE-01-02` (critical), `LE-01-04` (major)
- **Target Files:**
  - `plan/modules/M08-labor-supply-behavior.md`
  - `plan/modules/M15-international-evidence.md`
- **Summary of Changes:**
  - In `M08`, incorporated *Real Decreto 789/2022* (`boe-rd-789-2022-incentivo-imv`) into baseline METR/PTR schedules, contrasting its delayed annual clawback with UBR's real-time monthly clearing.
  - Specified exact MCVL variables (*bases de cotización*, contract codes 100/200/300) and EPA rotating panels to estimate intensive and extensive labor-supply elasticities.
  - In `M15`, formalized life-cycle structural transportability equations mapping finite-horizon RCT treatment effects into permanent compensated wage ($\varepsilon^c$) and income ($\eta$) elasticities.

### `SYN-01-09` · Privacy-Preserving Payroll Clearing, Inembargabilidad, and Algorithmic Due Process
- **Contributing Issues:** `LW-01-03` (major)
- **Target Files:**
  - `plan/modules/M12-administration-delivery.md`
- **Summary of Changes:**
  - Restricted employer monthly payroll clearing to the uniform individual adult UBR credit via an algorithmic, privacy-preserving **Numerical Tax Code** (*Código de Retención Sintético*), protecting sensitive family/disability data from employer HR departments under GDPR Art. 9 and LOPDGDD (`boe-lopdgdd-2018`).
  - Established statutory *inembargabilidad* under Art. 607 LEC and Art. 44 TRLGSS (`boe-trlgss-2015`), and prohibited automated administrative tax/bank debt set-offs under Arts. 71–73 LGT (`boe-lgt-2003`).
  - Embedded algorithmic due-process protections under LPAC Art. 41 (`boe-lpac-2015`) and GDPR Art. 22 requiring mandatory human review before payment suspension.

### `SYN-01-10` · Cross-Module Coherence & Systematic D-005 Pilot Tier Comparisons
- **Contributing Issues:** `RT-01-06` (major), `PF-01-04` (major), `LE-01-03` (major), `MA-01-04` (major), `MA-01-05` (major), and unanimous panel feedback on `D-005`
- **Target Files:**
  - `plan/00-scope.md`
  - `plan/modules/M02-benefit-design.md`
  - `plan/modules/M05-housing-rent-capture.md`
  - `plan/modules/M09-distribution-poverty-euromod.md`
  - `plan/modules/M11-political-economy.md`
  - `plan/modules/M14-gender-care-health.md`
  - `plan/modules/M17-transition-risks-stress-tests.md`
  - Section 6 ("Pilot implications") across all 17 modules
- **Summary of Changes:**
  - Harmonized child equivalence weights (40% of adult UBR) across `00-scope.md` and `M02` with an explicit affine schedule.
  - In `M05`, incorporated boundary quasi-experiments on *Bono Alquiler Joven* and *Ley 12/2023 por el derecho a la vivienda* (`boe-vivienda-2023`) to identify local rent-supply elasticities.
  - In `M09`, linked `M05` rental pass-through into EUROMOD to compute post-rent real equivalized disposable income across tenure cells, distinguishing anchored from floating poverty.
  - In `M14`, formalized a Chiappori collective household model (`chiappori-1992-collective`) and integrated female-skewed clerical displacement projections.
  - In `M17`, replaced raw labor-share triggers with an AIReF-certified composite index and added an Automatic Fiscal Stabilization Surcharge on upper IRPF brackets.
  - In every single module (`M01` through `M17`), Section 6 ("Pilot implications") was revised to explicitly contrast **Municipal**, **Regional** (*Régimen Común* vs. *Régimen Foral*), and **National** options per `D-005`.

---

## Sources Added and Verified
A total of 27 verified sources were added to `plan/sources.yaml` across iterations, with 100% verified over HTTP:
- Academic and institutional: `albanesi-2023-ai-europe`, `bentolila-2012-dual-spain`, `gali-monacelli-2005-soe`, `almunia-lopez-rodriguez-2019-eti`, `borusyak-2022-shift-share`, `chiappori-1992-collective`.
- Statutory & Constitutional: `boe-rdl-32-2021-reforma-laboral`, `boe-rd-789-2022-incentivo-imv`, `boe-ley-dependencia-2006`, `boe-loepsf-2012`, `boe-ley-financiacion-ccaa-2009`, `boe-concierto-vasco-2002`, `boe-convenio-navarra-1990`, `boe-iva-1992`, `boe-sociedades-2014`, `tc-stc-158-2021-imv`, `tc-stc-19-2024-imv-foral`, `boe-trlgss-2015`, `boe-rdl-2-2024-desempleo`, `boe-lgt-2003`, `boe-lopdgdd-2018`, `boe-lpac-2015`, `boe-extranjeria-2000`, `boe-lbrl-1985`.
- EU Law & Governance: `eu-reg-2024-1263-fiscal-framework`, `eu-dir-2006-112-vat`, `eu-dir-2004-38-free-movement`.
