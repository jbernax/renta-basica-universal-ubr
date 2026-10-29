---
id: M08
title: Labor supply, reservation wages, and behavioral responses
status: draft
locked: false
depends_on: [M01, M02, M03, M07, M10]
covers: [F09]
feeds_chapters: [2, 7]
last_iteration: 0
---
# M08 · Labor supply, reservation wages, and behavioral responses

## 1. Why this matters
A central objection to UBR is that an unconditional income floor will induce large reductions in labor supply, exacerbating fiscal pressures (`M03`). Conversely, in an AI-disrupted labor market (`M01`) with pervasive Spanish informality and welfare traps (`M07`), UBR may raise formal participation among welfare recipients, strengthen worker reservation wages against exploitative precarious contracts, and finance human-capital reallocation, caregiving (`M14`), and entrepreneurship [@hoynes-rothstein-2019; @vivalt-2024-openresearch].

## 2. Research questions
- **RQ-M08-01**: What are the extensive-margin (participation) and intensive-margin (hours worked) elasticities of Spanish workers by gender, age, household structure, and CNO-11 AI-exposure tier when moving from means-tested transfers (IMV/subsidios) to an IRPF-integrated UBR?
  - *Hypothesis:* Aggregate hours worked decline by less than 1.5–2.5% under Tier B, concentrated in voluntary reductions of overtime by secondary earners with young children and youth extending education, while formal extensive-margin participation among former IMV/informal workers *increases* by 3–5 percentage points due to eliminating the 100% benefit clawback.
- **RQ-M08-02**: Under AI displacement scenarios S1–S3, does UBR shorten or lengthen unemployment spells, and does it improve post-displacement occupational match quality (wage and skill upgrading via retraining and self-employment)?
  - *Hypothesis:* Unconditional liquidity increases post-displacement search duration by 3–6 weeks on average, but yields a 6–10% higher re-employment wage stability and higher survival of solo self-employment (*autónomos*) compared to liquidity-constrained displaced workers.

## 3. State of knowledge
Recent high-powered RCTs and natural experiments show small extensive-margin employment reductions from unconditional transfers: in the US OpenResearch RCT ($1,000/month for 3 years), Vivalt et al. [@vivalt-2024-openresearch] find a 1.3 hour/week reduction and a 2 pp participation effect driven by selectivity in job search and leisure, with higher educational enrollment among younger adults. In Alaska's permanent universal dividend, Jones & Marinescu [@jones-marinescu-2022] find zero aggregate employment decline because positive local demand multipliers offset individual income effects. In Finland [@kangas-2021-finland], replacing conditional unemployment benefits with an unconditional basic income increased employment days slightly once bureaucratic disincentives were removed.

## 4. Spain context & data sources
- **Labor & Longitudinal Data:** INE *Encuesta de Población Activa* (EPA longitudinal rotating panel), *Muestra Continua de Vidas Laborales* (MCVL matched with AEAT tax withholdings), and INE *Encuesta de Empleo del Tiempo* (EET).
- **Informality & Self-Employment:** RETA (*Régimen Especial de Trabajadores Autónomos*) survival cohorts and AIReF evaluations of IMV labor incentives.

## 5. Methods & identification
1. **Structural Discrete-Choice Labor Supply Model:** Estimate a random-utility discrete hours-choice model ($h \in \{0, 20, 30, 40\}$) on Spanish ECV + EPA data, separately identifying substitution elasticities ($\varepsilon^c$) and income elasticities ($\eta$) across demographic cells [@saez-2002-optimal-transfers].
2. **Bunching & RD on Existing Spanish Thresholds:** Exploit sharp kinks and notches in the IRPF tariff [@boe-irpf-2006], IMV income phase-out [@boe-imv-2021], and SEPE *subsidio para mayores de 52 años* in MCVL to estimate Spanish extensive/intensive elasticities.
3. **Transition-to-Formal-Work Hazard Model:** Model informal-to-formal and *autónomo* entry hazards when METRs drop from ~100% (IMV) to ~45% (UBR + IRPF).

## 6. Pilot implications
- **Municipal / Regional / National (`M10`):** Link pilot participants (with informed GDPR consent) directly to monthly Seguridad Social affiliation records (*vidas laborales*) and AEAT 190 withholdings so labor supply, contract type (*indefinido*, *fijo discontinuo*, *autónomo*), and wage match quality are measured without survey recall bias.

## 7. Risks, counterarguments & open issues
- **Counterargument (Tax-Financed Substitution Effect):** RCTs test windfall transfers ($+\text{income effect}$ only), whereas a permanent national UBR also raises marginal IRPF rates ($+\text{substitution effect}$ [@hoynes-rothstein-2019]). *Mitigation:* Always simulate the **combined** income + marginal-tax substitution effect in EUROMOD/structural models and include a simulated tax-rate arm in the regional pilot (`M10`).

## 8. Deliverables & effort
- Demographic Cell Matrix of Spanish Income & Substitution Elasticities ($\eta, \varepsilon^c$).
- Behavioral Labor-Supply Adjustment Module for EUROMOD (`M03`, `M09`) and Chapter 2/7. (Effort: 6 person-weeks).
