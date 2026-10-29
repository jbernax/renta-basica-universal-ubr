---
id: M09
title: Distributional, poverty, and inequality microsimulation
status: draft
locked: false
depends_on: [M01, M02, M03, M05, M07, M08]
covers: [F10]
feeds_chapters: [4]
last_iteration: 1
---
# M09 · Distributional, poverty, and inequality microsimulation

## 1. Why this matters
Spain persistently exhibits one of the highest child poverty, anchored poverty, and disposable-income inequality (Gini and S80/S20) rates in Western Europe, driven by labor-market duality, cyclical unemployment volatility, and structurally weak, fragmented cash transfers for working-age households and children [@arcelus-bade-2015-rgi]. As AI labor displacement (`M01`) widens market-income dispersion and compresses labor shares across scenarios S1–S3, this module quantifies the exact distributional impact of UBR Tiers A, B, and C across income deciles, family structures, age cohorts, housing tenure groups, and Autonomous Communities, integrating the Status-Quo Budget Neutrality constraint (`M03`) and the Dual-Pillar pension integration (`M07`).

## 2. Research questions
- **RQ-M09-01**: What is the static and behavioral impact of UBR Tiers A, B, and C (integrated with reformed IRPF `M03`, consumption taxes, and the `M07` *Complemento de Neutralidad Fiscal*) on Spain's headline AROPE rate, severe poverty (<40% median), anchored vs. floating poverty thresholds, child poverty, Gini coefficient, and S80/S20 ratio across S1–S3?
  - *Hypothesis:* Tier B (€900/adult, €360/minor) reduces severe monetary poverty (<40% median) in Spain by >85%, cuts child monetary poverty by >72%, and lowers the disposable-income Gini coefficient by 6.2–7.5 Gini points under Scenario S2. Anchored poverty drops substantially faster than floating poverty, as the universal cash grant elevates the national median income.
- **RQ-M09-02**: Which household types, income deciles, and housing tenure cells are net winners versus net contributors under the consolidated fiscal bridge (`M03`), and what share of households in deciles 1–5 experience any disposable-income loss?
  - *Hypothesis:* Deciles 1–7 are net financial winners on average, with breakeven occurring between the 82nd and 86th gross income percentile under Tier B; the `M07` *Complemento de Neutralidad Fiscal* ensures that fewer than 0.1% of households in deciles 1–5 suffer disposable income losses.
- **RQ-M09-03**: How does housing market rent pass-through (`M05`) and indirect tax incidence (IVA and excise duties) erode nominal distributional gains when measuring real post-tax, post-housing disposable income across urban versus rural deciles?
  - *Hypothesis:* In urban rental markets with high baseline rent burdens (Madrid, Barcelona, Balearic Islands), 18–35% of the gross cash transfer to low-income tenant households is captured by landlords unless mitigated by supply-side housing mechanisms (`M05`).

## 3. State of knowledge
Tax-benefit microsimulation using EUROMOD [@sutherland-figari-2013-euromod] represents the international gold standard for counterfactual policy evaluation in Europe. Prior Spanish microsimulations document that while the 2021 *Ingreso Mínimo Vital* [@boe-imv-2021] significantly deepens support for the extreme poor who access it, persistent non-take-up exceeding 50% [@boe-imv-2021; @arcelus-bade-2015-rgi] and severe cohabitation/wealth tests leave headline child poverty and AROPE largely stagnant. Universal cash transfers fundamentally eliminate non-take-up exclusion errors (Type I errors) [@van-parijs-vanderborght-2017; @hoynes-rothstein-2019]. However, static analyses frequently omit the general-equilibrium rent-pass-through channel [@fack-2006-housing-benefits; @diamond-mcquade-qian-2019-rent] and the regressive incidence of indirect consumption taxes required for macroeconomic fiscal closure [@guerreiro-rebelo-teles-2022-robots; @korinek-suh-2024].

## 4. Spain context & data sources
- **Survey Microdata:** INE *Encuesta de Condiciones de Vida* (ECV / EU-SILC Spanish component), featuring regional oversampling across all 17 Autonomous Communities and panel rotation structure.
- **Administrative Tax & Social Security Microdata:** IEF/AEAT *Muestra de Declarantes de IRPF* (annual 2-million taxpayer panel) to eliminate ECV top-income underreporting and right-truncation, combined with the *Muestra Continua de Vidas Laborales* (MCVL) for labor history and contributory pension bases.
- **Regional Foral Microdata:** Dedicated provincial tax microdata from the Basque Provincial Treasuries (*Diputaciones Forales de Álava, Bizkaia, Gipuzkoa*) and Navarre under the *Concierto Económico* [@boe-concierto-vasco-2002] and *Convenio Económico* [@boe-convenio-navarra-1990] to capture distinct foral IRPF tariffs.
- **Expenditure & Housing Data:** INE *Encuesta de Presupuestos Familiares* (EPF), mapped to 12 COICOP consumption functions to estimate decile-specific indirect tax burdens (IVA and excise duties), matched with MITMA/INE tenancy and rent-index records (*Índice de Precios de Vivienda en Alquiler*).

## 5. Methods & identification
1. **Top-Income Calibration & Micro-Matching:** Statistically match the top 5% of gross market and capital incomes from the AEAT *Muestra de Declarantes* into ECV survey records using a parametric Pareto reweighting algorithm, ensuring exact fiscal alignment with aggregate budget revenues (`M03`).
2. **Decomposition of Poverty and Inequality:**
   - Compute Foster-Greer-Thorbecke ($P_0, P_1, P_2$) indices for both **floating poverty** (60% of contemporaneous post-reform median income) and **anchored poverty** (fixed at the real pre-reform baseline median deflated by HICP).
   - Evaluate Gini, Theil, and Atkinson indices ($\varepsilon \in \{0.5, 1.0, 2.0\}$), alongside Shorrocks-Shapley decompositions that separate the direct universal transfer effect, the benefit-integration offset (`M07`), the IRPF tariff restructure (`M03`), and labor-supply behavioral adjustments (`M08`).
3. **Post-Housing & Post-IVA Real Income Metric:** Define real equivalized disposable income $y_{i}^{\text{real}} = (y_{i}^{\text{disp}} - \Delta R_{i} - T_{i}^{\text{ind}})/\phi(k_i)$, where $\Delta R_i$ denotes landlord rent extraction modeled via `M05` pass-through elasticities ($\gamma \in [0.15, 0.45]$) for private-market tenants, $T_i^{\text{ind}}$ is the household-specific indirect tax incidence computed from EPF, and $\phi(k_i)$ is the modified OECD equivalence scale (1.0 for first adult, 0.5 for subsequent adults, 0.3/0.4 for minors).
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
