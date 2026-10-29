---
id: M08
title: Labor supply, reservation wages, and behavioral responses
status: locked
locked: true
depends_on: [M01, M02, M03, M07, M10]
covers: [F09]
feeds_chapters: [2, 7]
last_iteration: 3
---
# M08 · Labor supply, reservation wages, and behavioral responses

## 1. Why this matters
A central objection to UBR is that an unconditional income floor will induce large reductions in labor supply, exacerbating fiscal pressures (`M03`). Conversely, in an AI-disrupted labor market (`M01`) with pervasive Spanish informality, dual labor contracts (*fijos discontinuos* under *Real Decreto-ley 32/2021* [@boe-rdl-32-2021-reforma-laboral]), and complex welfare clawbacks under *Real Decreto 789/2022* [@boe-rd-789-2022-incentivo-imv] and the recent assistential unemployment reform under *Real Decreto-ley 2/2024* (*Complemento de Apoyo al Empleo*, CAE [@rdl-2-2024-desempleo]), UBR may raise formal participation, eliminate the poverty trap, strengthen worker reservation wages against precarious conditions, and finance human-capital reallocation and caregiving (`M14`) [@hoynes-rothstein-2019; @vivalt-2024-openresearch].

## 2. Research questions
- **RQ-M08-01**: What are the extensive-margin (participation) and intensive-margin (hours worked) elasticities of Spanish workers across gender, age, and CNO-11 AI-exposure tiers when moving from means-tested transfers—benchmarked against both the IMV employment incentive (RD 789/2022 [@boe-rd-789-2022-incentivo-imv]) and the assistential unemployment CAE under *RDL 2/2024* [@rdl-2-2024-desempleo]—to an IRPF-integrated UBR?
  - *Hypothesis:* Aggregate hours worked decline by less than 1.5–2.5% under Tier B, concentrated in voluntary reductions of overtime by secondary earners with young children and youth extending education, while formal extensive participation among former IMV/informal workers *increases* by 3–5 percentage points because UBR replaces the complex, delayed annual clawback of RD 789/2022 and CAE phase-outs with real-time monthly certainty.
- **RQ-M08-02**: Under AI displacement scenarios S1–S3, how does UBR affect unemployment search duration, intermittent contract survival (*fijos discontinuos*), and post-displacement occupational match quality?
  - *Hypothesis:* Unconditional liquidity increases post-displacement search duration by 3–6 weeks on average, but yields a 6–10% higher re-employment wage stability in MCVL records and higher survival of solo self-employment (*autónomos*) compared to liquidity-constrained displaced workers.

## 3. State of knowledge
Recent high-powered RCTs and natural experiments demonstrate modest extensive-margin employment reductions from unconditional transfers: in OpenResearch, Vivalt et al. [@vivalt-2024-openresearch] find a 1.3 hour/week reduction and a 2 pp participation drop driven by job selectivity and education. In Alaska's permanent universal dividend, Jones & Marinescu [@jones-marinescu-2022] find zero aggregate employment decline due to local demand multipliers. In Finland [@kangas-2021-finland], replacing conditional unemployment benefits with an unconditional basic income increased formal work days once bureaucratic disincentives were removed. In Spain, the post-2021 labor reform increased the share of open-ended intermittent contracts (*fijos discontinuos*), making labor-supply adjustments occur along inactivity spell duration rather than pure binary employment [@bentolila-2012-dual-spain; @boe-rdl-32-2021-reforma-laboral; @bentolila-2020-dual-labor].

## 4. Spain context & data sources
- **Labor Microdata:** INE *Encuesta de Población Activa* (EPA 6-quarter rotating longitudinal panel for gross worker flows), *Muestra Continua de Vidas Laborales* (MCVL linked to AEAT Form 190 withholdings, tracking contract codes 100/200/300, monthly *bases de cotización*, and *coeficiente de parcialidad*), and INE *Encuesta de Empleo del Tiempo* (EET).
- **Incentive Baseline:** *Real Decreto 789/2022* [@boe-rd-789-2022-incentivo-imv] (statutory IMV labor income exemption formulas), *Real Decreto-ley 2/2024* [@rdl-2-2024-desempleo] (CAE degressive phase-out schedules), and AIReF IMV evaluations [@airef-opinion-imv-2023].

## 5. Methods & identification
1. **Structural Discrete-Choice Hours Model:** Estimate a discrete-choice model ($h \in \{0, 20, 30, 40\}$) on Spanish ECV + EPA flow data, identifying separate intensive ($\varepsilon^c$) and income ($\eta$) elasticities across demographic cells (youth 18–29, prime 30–51, older workers 52+), calibrated against RD 789/2022 and RDL 2/2024 baseline METRs [@saez-2002-optimal-transfers].
2. **Convex Bunching & Missing-Mass Estimation:** Exploit sharp kinks in the IRPF withholding tariff [@boe-irpf-2006], the RD 789/2022 wage exemption limits [@boe-rd-789-2022-incentivo-imv], and the age-52 SEPE *subsidio* threshold [@boe-trlgss-2015]. In pilot evaluation (`M10`), specify an initial labor income disregard ($Y_{\text{disregard}} = \text{€}3,000\text{--}\text{€}5,000/\text{year}$) creating a true convex kink with excess mass bunching per Saez [@saez-2010-bunching] and Chetty et al. [@chetty-2011-bunching; @chetty-2012-bounds], while estimating missing mass at the upper concave phase-out ceiling $Y^* = \text{UBR}/\tau_{\text{clawback}}$ per Kleven [@kleven-2016-bunching].
3. **Sequential Shock Protocol (`methods.md`):** Ensure that `M01` involuntary AI displacement hazards (modeled on MCVL *pases a inactividad* and severance cost gradients per Bentolila et al. [@bentolila-2020-dual-labor]) are applied first to generate counterfactual market earnings before estimating second-step voluntary labor-supply adjustments in EUROMOD.

## 6. Pilot implications
- **Municipal Tier:** Measure short-run partial-equilibrium labor supply, contract choice, and informal-to-formal transitions in treated municipal zones without tax clawback.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** In *Régimen Común*, test contractual clawback incentives; in *Régimen Foral* (Basque Country / Navarre), test the full joint UBR + IRPF marginal rate schedule to identify compensated substitution elasticities.
- **National Tier:** Link pilot participants' DNI/NIE directly to monthly Seguridad Social affiliation records (*vidas laborales*) to measure daily hours, wages, and contract transitions without survey recall bias (`M10`).

## 7. Risks, counterarguments & open issues
- **Counterargument (Compounded Substitution Effect from Financing):** A permanent national UBR raises marginal IRPF rates ($+\text{substitution effect}$), unlike pure windfall RCTs. *Mitigation:* Always simulate the combined income + marginal-tax substitution effect in EUROMOD and structural models, using transported parameters from `M15`.

## 8. Deliverables & effort
- Demographic Cell Matrix of Spanish Income & Substitution Elasticities ($\eta, \varepsilon^c$).
- Behavioral Labor-Supply Module for EUROMOD (`M03`, `M09`) and Chapter 2/7. (Effort: 6 person-weeks).
