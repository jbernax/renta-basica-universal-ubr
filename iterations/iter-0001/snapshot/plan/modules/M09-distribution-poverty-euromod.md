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
