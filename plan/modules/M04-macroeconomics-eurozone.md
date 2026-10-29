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
