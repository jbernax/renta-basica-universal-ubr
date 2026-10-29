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
