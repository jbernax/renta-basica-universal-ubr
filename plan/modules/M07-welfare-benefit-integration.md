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
