---
id: M02
title: Benefit design, eligibility, and parameter architecture
status: draft
locked: false
depends_on: [M03, M07, M09]
covers: [F02]
feeds_chapters: [3]
last_iteration: 3
---
# M02 · Benefit design, eligibility, and parameter architecture

## 1. Why this matters
Small changes in benefit architecture—individual versus household unit, adult versus minor amounts, age thresholds, and indexation rules—determine whether UBR eliminates poverty and intra-household dependency or becomes fiscally unviable [@van-parijs-vanderborght-2017; @hoynes-rothstein-2019]. In Spain, where the *Ingreso Mínimo Vital* (IMV) suffers from complex household-unit assessments, cohabitation verification penalties, and severe non-take-up (56% for baseline IMV, 70% for CAPI [@boe-imv-2021; @airef-opinion-imv-2023]), strict adherence to the unconditional individual entitlement principle (`D-001`) is essential.

## 2. Research questions
- **RQ-M02-01**: How do strictly individual UBR schedules (Tier A: €600 adult / €300 first child / €240 subsequent; Tier B: €900 adult / €450 first child / €360 subsequent; Tier C: €1,200 adult / €600 first child / €480 subsequent, incorporating a parity-modulated child scale $\alpha_{\text{child1}} = 0.50, \alpha_{\text{child}\ge 2} = 0.40$) compare against household-equivalized means-tested schedules in eliminating child poverty without creating cohabitation penalties, when paired with the `M07` No-Loser Guarantee and disability supplements?
  - *Hypothesis:* An individual Tier B UBR (€900/adult) paired with parity-modulated child allowances (€450 for the first child, €360 for subsequent minors) holds single parents completely harmless against IMV 22% single-parent bonuses and CAPI baselines [@boe-imv-2021; @ayala-2025-child-poverty] purely through individual child entitlements, avoiding intrusive domestic cohabitation surveillance (*policía de la convivencia*), while a tiered *Complemento Universal por Discapacidad* (+25% to +100% per RD 888/2022 [@boe-rd-888-2022-discapacidad; @puig-segura-2021-discapacidad]) eliminates horizontal inequities across family structures.
- **RQ-M02-02**: What indexation formula—essential-basket CPI, headline CPI, or constant-tax CPI (*Índice de Precios de Consumo a Impuestos Constantes*, IPC-IC) capped by nominal GDP-per-capita growth—best preserves real living standards across S1–S3 without triggering unlegislated fiscal drag or fiscal self-indexation under `M03`?
  - *Hypothesis:* Indexing UBR benefits to IPC-IC capped by nominal per-capita GDP growth, synchronized with statutory adjustments to `M03` IRPF marginal rate brackets, prevents fiscal self-indexation during IVA base-broadening phases while guaranteeing an untaxable subsistence floor.

## 3. State of knowledge
Theoretical public economics demonstrates that unconditional individual transfers avoid the high marginal effective tax rates (METRs) and invasive monitoring costs of means-tested programs, at the cost of higher gross fiscal outlays that must be recouped through progressive taxation [@ghatak-maniquet-2019; @saez-2002-optimal-transfers; @van-parijs-vanderborght-2017]. Empirical evidence from Spanish minimum income schemes shows that household-level means testing penalizes young adult emancipation, disincentivizes shared housing, and creates severe administrative exclusion [@airef-opinion-imv-2023; @todeschini-bmincome-2020].

## 4. Spain context & data sources
- **Poverty & Living Standards Benchmarks:** INE *Encuesta de Condiciones de Vida* (ECV) AROPE thresholds (60% and 40% of median equivalized disposable income across Spain and by Autonomous Community).
- **IMV Statutory Baseline:** *Ley 19/2021* [@boe-imv-2021] guaranteed amounts, *Complemento de Ayuda para la Infancia* (CAPI), and disability provisions under *Real Decreto 888/2022* [@boe-rd-888-2022-discapacidad].
- **Demographics:** INE *Censo de Población* and *Padrón Continuo* (adult/minor age cohorts, household size distributions).

## 5. Methods & identification
1. **Parametric Dominance Grid in EUROMOD-Spain:** Simulate a $3 \times 3$ design grid in EUROMOD [@sutherland-figari-2013-euromod] testing Tiers A/B/C $\times$ child equivalence schedules ($\alpha_{\text{flat}} = 0.40$ vs. parity-modulated $\alpha_{\text{child1}} = 0.50, \alpha_{\ge 2} = 0.40$ per Ayala et al. [@ayala-2025-child-poverty]) with individual adulthood anchored strictly at age 18. Model the absorption of LIRPF Art. 58 descendant deductions and direct disbursement of child UBR to legal custodians, combined with the three-tiered *Complemento por Discapacidad* (+25%, +50%, +100%) to measure cohabitation penalty rates and disposable income gains across household types.
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
