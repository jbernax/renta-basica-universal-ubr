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
