# Review Synthesis — Iteration 0001 (`iter-0001`)

## Overview & Panel Consensus
The five specialist reviewers (`labor-economist`, `public-finance`, `macroeconomist`, `spanish-eu-law`, and `red-team`) completed comprehensive audits of the initial research plan. The panel recognized the strong foundation of Plan v0—specifically its parameterization of AI displacement scenarios (S1–S3), integration of EUROMOD microsimulation and open-economy HANK macroeconomics, and multi-level pilot ambition—while identifying critical arithmetic, legal, and causal-identification gaps that must be resolved to achieve state-of-the-art rigor.

All candidate changes have been synthesized, deduplicated, and ranked into 10 high-leverage proposals (`SYN-01-01` to `SYN-01-10`), capped at `max_changes_per_iteration: 15`. No proposals violate human-locked decisions in `plan/decisions.md`.

---

## Synthesized Proposals

### `SYN-01-01` · Status-Quo Fiscal Neutrality & Dual-Pillar Pension Integration
- **Contributing Issues:** `RT-01-01` (critical), `RT-01-02` (critical), `PF-01-01` (critical), `LW-01-02` (critical)
- **Target Files:** `plan/modules/M03-fiscal-financing.md`, `plan/modules/M07-welfare-benefit-integration.md`, `plan/modules/M09-distribution-poverty-euromod.md`
- **Actions:**
  1. In `M03`, resolve the UBI accounting fallacy by establishing an explicit **Status-Quo Budget Neutrality Constraint**: total post-reform IRPF revenues must cover 100% of baseline public services (~€125B/year) PLUS gross UBR outlays minus genuinely abolished non-contributory benefits (`M07`). Distinguish the gross zero point ($T_{\text{new}} = \text{UBR}$) from the net disposable income breakeven point ($T_{\text{new}} - T_{\text{old}} = \text{UBR}$), updating breakeven income percentiles and net financing requirements accordingly.
  2. In `M07`, correct the order-of-magnitude error in contributory pension top-ups: distinguish total retained contributory pensions (~5.5–6.0% of GDP above the UBR floor) from the incremental tax-neutrality compensation supplement (<0.6% of GDP).
  3. Replace the 100% pension offset with a **Dual-Pillar Contributory Architecture** that preserves marginal returns to Social Security contributions and incorporates an explicit **Complemento de Neutralidad Fiscal** in EUROMOD so no pensioner suffers a post-IRPF disposable income loss. Preserve Art. 280 TRLGSS retirement contribution credits for displaced workers aged 52+.
  4. In `M03`, explicitly fold LIRPF Art. 20 (earned-income reduction) and Art. 84 (joint-filing reduction) into the integrated tariff and specify the consolidated Administraciones Públicas fiscal bridge.

### `SYN-01-02` · Constitutional Competence, EU Free Movement, and Tax-Benefit Symmetry
- **Contributing Issues:** `LW-01-01` (critical), `LW-01-04` (critical), `PF-01-01` (critical)
- **Target Files:** `plan/modules/M06-constitutional-eu-law.md`, `plan/modules/M13-migration-territory-residency.md`
- **Actions:**
  1. In `M06`, replace the Annex X Regulation 883/2004 SNCB classification with a bifurcated EU-law architecture distinguishing economically active EU workers/self-employed (entitled to immediate pro-rata IRPF tax credit integration under Art. 45 TFEU and Directive 2004/38/EC) from economically inactive persons and third-country entrants.
  2. In `M06`, replace prose case references with formal, verified citations to the actual *Tribunal Constitucional* IMV competence judgments: STC 158/2021 (BOE-A-2021-17107) and STC 19/2024 (BOE-A-2024-3941). Integrate the statutory revenue-sharing mechanics for the 50% ceded regional IRPF under *Ley 22/2009* and the Basque *Concierto Económico* (*Ley 12/2002*).
  3. In `M13`, establish a binding **Tax-Benefit Symmetry Principle**: any legal resident subject to Spanish IRPF under Art. 9 LIRPF must either receive the UBR credit pro-rata or retain an equivalent refundable *mínimo personal y familiar* so subsistence income is never taxed under Art. 31.1 CE. Restrict the 12–36 month waiting periods strictly to economically inactive non-contributing entrants.

### `SYN-01-03` · Multi-Level Pilot Redesign & Experimental Power Calibration
- **Contributing Issues:** `RT-01-03` (critical)
- **Target Files:** `plan/modules/M10-pilot-evaluation-design.md`
- **Actions:**
  1. Expand the cluster-saturation design from 18 units to $J = 60\text{–}80$ spatial clusters (e.g. 30–40 treated vs. 30–40 matched control census-tract groups or small municipalities) to achieve genuine 80% statistical power for general-equilibrium rent pass-through and wage spillovers using randomization inference and wild cluster bootstrap.
  2. Replace the legally unviable randomized tax-increase arm with a randomized **Benefit Phase-Out / Clawback Rate Arm** (testing 0% vs. 38% vs. 50% marginal clawback rates capped at the gross grant amount so no participant pays more tax than baseline IRPF), cleanly identifying compensated substitution elasticities.
  3. Reconcile the 36-month pilot budget (€432M–€648M gross before phase-out clawbacks) without relying on EU ESF+ grants for middle-income transfers.

### `SYN-01-04` · Spanish Labor Institutions, Collective Bargaining, and AI Shock Mapping
- **Contributing Issues:** `LE-01-01` (critical), `MA-01-03` (major), `RT-01-05` (major)
- **Target Files:** `plan/modules/M01-ai-labor-displacement.md`, `plan/methods.md`
- **Actions:**
  1. In `M01` and `methods.md`, separate gross US O*NET task exposure from net equilibrium employment and wage-bill displacement in Spain, incorporating ESCO/PIAAC task weights, ETICCE firm-size adoption thresholds, and Acemoglu-Restrepo cost-saving parameters.
  2. Model how binding sectoral collective bargaining (*convenios colectivos* with *ultraactividad* under *Real Decreto-ley 32/2021*) and statutory SMI floors channel AI shocks into intermittent open-ended contract inactivity (*pases a inactividad de fijos discontinuos* in MCVL) and ERTE/RED hours adjustments rather than uniform wage cuts.
  3. Define complete macroeconomic scenario vectors pairing S1–S3 labor-share shifts with explicit TFP growth bands and domestic vs. foreign AI-rent splits. Clarify shift-share IV identification bounds per Borusyak, Hull, & Jaravel (2022).

### `SYN-01-05` · Eurozone Open-Economy HANK Block & Fiscal Rules Compliance
- **Contributing Issues:** `MA-01-01` (critical)
- **Target Files:** `plan/modules/M04-macroeconomics-eurozone.md`
- **Actions:**
  1. Formalize the small-open-economy currency-union HANK model with a fixed nominal exchange rate, area-wide ECB Taylor-rule weight, terms-of-trade competitiveness channel, and endogenous Bonos-Bund sovereign spread transmission.
  2. Embed compliance with the reformed EU fiscal governance framework under *Regulation (EU) 2024/1263* and Spain's *Ley Orgánica 2/2012* (LOEPSF), specifying how gross UBR outlays are legally netted against Discretionary Revenue Measures (MDI) to respect the Net Primary Expenditure Ceiling.
  3. Model dual external leakage in the Balance of Payments: household consumption imports by decile plus B2B imports of foreign AI and cloud compute services.

### `SYN-01-06` · Iterative Micro-Macro General-Equilibrium Closure Protocol
- **Contributing Issues:** `MA-01-02` (major), `PF-01-05` (major), `LE-01-05` (major)
- **Target Files:** `plan/methods.md`, `plan/modules/M03-fiscal-financing.md`, `plan/modules/M04-macroeconomics-eurozone.md`
- **Actions:**
  1. Specify an explicit four-stage **Iterative Micro-Macro Closure Protocol** linking EUROMOD-Spain (`M03`/`M08`/`M09`) and the Spanish open-economy HANK model (`M04`):
     - Stage 1: `M01` CNO-11 displacement and wage-bill shocks mapped to micro-records via MCVL transition matrices.
     - Stage 2: EUROMOD iterates with `M08` labor supply and `M03` ETI to solve for the consolidated revenue-neutral tax schedule.
     - Stage 3: Decile net transfers and marginal tax wedges fed into HANK to solve for equilibrium wages, non-tradable/housing inflation, and real GDP.
     - Stage 4: HANK equilibrium price and income vectors feed back into EUROMOD via a Gauss-Seidel fixed-point loop until the structural primary balance converges within $\pm 0.05\%$ of GDP.

### `SYN-01-07` · Factor-Neutral AI Rent Capture & EU VAT Directive Compliance
- **Contributing Issues:** `RT-01-04` (major), `PF-01-03` (major)
- **Target Files:** `plan/modules/M16-ai-rent-capture-sovereign-fund.md`
- **Actions:**
  1. Redesign the domestic AI factor-neutral contribution as a direct levy on accounting Net Operating Surplus (*Excedente Bruto de Explotación* net of depreciation) without invoice-credit deduction—modeled on the CJEU-upheld Italian IRAP framework (Case C-475/03)—to guarantee compliance with Article 401 of EU VAT Directive 2006/112/EC.
  2. Explicitly deduct S2/S3 baseline Social Security payroll tax losses from gross corporate yields to avoid double-counting.
  3. Revise `RQ-M16-02` to distinguish the ~15–20% of GDP accumulated endowment stock at year 15 from its sustainable annual real dividend payout (~0.5–0.8% of GDP/year).

### `SYN-01-08` · Baseline Welfare-Trap Calibration with RD 789/2022 & Transportable Elasticities
- **Contributing Issues:** `LE-01-02` (critical), `LE-01-04` (major)
- **Target Files:** `plan/modules/M08-labor-supply-behavior.md`, `plan/modules/M15-international-evidence.md`
- **Actions:**
  1. In `M08`, incorporate *Real Decreto 789/2022* (the statutory IMV employment-incentive disregard) into the baseline METR/PTR schedule, contrasting its delayed annual clawback against UBR's real-time monthly clearing.
  2. Specify exact MCVL variables (bases de cotización, contract type codes 100/200/300) and EPA rotating panel flows to estimate separate intensive/extensive elasticities by gender, age, and AI exposure.
  3. In `M15`, specify structural decomposition equations mapping finite-horizon RCT treatment effects into permanent compensated wage ($\varepsilon^c$) and income ($\eta$) elasticities.

### `SYN-01-09` · Privacy-Preserving Payroll Clearing, Inembargabilidad, and Algorithmic Due Process
- **Contributing Issues:** `LW-01-03` (major)
- **Target Files:** `plan/modules/M12-administration-delivery.md`
- **Actions:**
  1. Restrict employer monthly payroll clearing to the uniform individual UBR credit via a privacy-preserving numerical tax code (preventing employers from inferring protected employee vulnerability or disability supplements under GDPR Art. 9 and LOPDGDD).
  2. Incorporate an explicit statutory shield against debt attachment (*inembargabilidad* under Art. 607 LEC and Art. 44 TRLGSS) and automatic tax/bank debt set-offs (Arts. 71–73 LGT).
  3. Embed due-process rules under *Ley 39/2015* Art. 41 and GDPR Art. 22 requiring human review and a non-suspensive hearing before pausing any payment.

### `SYN-01-10` · Cross-Module Coherence & Systematic D-005 Pilot Tier Comparisons
- **Contributing Issues:** `RT-01-06` (major), `PF-01-04` (major), `LE-01-03` (major), `MA-01-04` (major), `MA-01-05` (major), and unanimous panel feedback on `D-005`
- **Target Files:** `plan/00-scope.md`, `plan/modules/M02-benefit-design.md`, `plan/modules/M05-housing-rent-capture.md`, `plan/modules/M09-distribution-poverty-euromod.md`, `plan/modules/M14-gender-care-health.md`, `plan/modules/M17-transition-risks-stress-tests.md`, and Section 6 across all reviewed modules
- **Actions:**
  1. Harmonize minor benefit schedules across `00-scope.md` and `M02` with an explicit affine child schedule anchored in EUROMOD.
  2. In `M09`, link `M05` rental pass-through vectors into EUROMOD to compute real post-rent equivalized disposable income across housing tenure cells.
  3. In `M14`, specify a Chiappori-style collective household model and integrate S1–S3 female-skewed clerical shock projections.
  4. In `M17`, replace raw labor-share triggers with an AIReF-certified composite index and add an Automatic Fiscal Stabilization Surcharge on upper IRPF brackets to cool short-run demand without construction lags.
  5. Ensure Section 6 ("Pilot implications") in all updated modules explicitly contrasts **Municipal**, **Regional** (*Régimen Común* vs. *Régimen Foral*), and **National** options per `D-005`.
