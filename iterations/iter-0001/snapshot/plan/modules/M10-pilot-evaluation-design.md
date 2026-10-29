---
id: M10
title: Multi-level pilot and causal evaluation design
status: draft
locked: false
depends_on: [M02, M05, M06, M08, M12, M15]
covers: [F11]
feeds_chapters: [7]
last_iteration: 0
---
# M10 · Multi-level pilot and causal evaluation design

## 1. Why this matters
Past basic income pilots worldwide have suffered from three recurrent methodological limitations: (i) dispersed individual randomization that cannot detect general-equilibrium effects on local rents, prices, or wages [@egger-2022-ge-kenya; @hoynes-rothstein-2019]; (ii) testing only gross windfall transfers without the tax-financing clawback; and (iii) reliance on high-attrition self-reported surveys [@kangas-2021-finland]. Following `D-005`, this module designs a rigorous, pre-registered multi-level Spanish pilot architecture comparing **Municipal**, **Regional (Común vs. Foral)**, and **National** experimental options.

## 2. Research questions
- **RQ-M10-01**: How can a two-stage randomized saturation design in Spain jointly identify partial-equilibrium behavioral responses (individual labor supply, health, consumption) and local general-equilibrium spillovers (rental pass-through `M05`, wage bargaining `M08`, local multipliers `M04`)?
  - *Hypothesis:* Combining Arm 1 (dispersed individual RCT across 60 municipalities, $N = 5,000$ treated, $N = 10,000$ control) with Arm 2 (cluster-randomized 80–100% universal saturation in 6 matched municipal/comarcal units vs. 12 synthetic/matched controls, $N \approx 15,000$ treated) achieves 80% statistical power ($\alpha = 0.05$) to detect a $\ge 1.5$ hour/week labor supply shift and a $\ge 3.5\%$ local rental pass-through differential.
- **RQ-M10-02**: How can a regional or national pilot incorporate a **Net-Tax / Clawback Treatment Arm** to measure real-world elasticity to the combined UBR + IRPF marginal tax schedule (`M03`)?
  - *Hypothesis:* Running a dedicated arm in a *régimen foral* community (Basque Country or Navarre) or under a State IRPF delegation where treated middle-income participants receive UBR alongside adjusted monthly withholding rates ($t = 45\%$) provides the first causal estimate in Europe of net tax-transfer labor elasticity.

## 3. State of knowledge
Recent landmark trials—OpenResearch [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health], GiveDirectly's village-saturation experiment in Kenya [@egger-2022-ge-kenya], Finland's nationwide register-linked RCT [@kangas-2021-finland], Stockton SEED [@west-2024-seed], and Barcelona's B-MINCOME [@todeschini-bmincome-2020]—demonstrate that linking administrative registers eliminates differential attrition on employment and tax outcomes, while cluster saturation is indispensable for capturing general equilibrium. Catalonia's 2021–2023 Office for the Basic Income Pilot Plan (*Oficina del Pla Pilot per Implementar la Renda Bàsica Universal*) designed a hybrid individual + municipal saturation blueprint that was halted solely by parliamentary budget veto (`M11`).

## 4. Spain context & data sources
- **Spanish Precedents:** B-MINCOME (Barcelona 2017–2019, 1,000 vulnerable households across 4 modalities in Eix Besòs [@todeschini-bmincome-2020]), Catalonia's designed saturation protocol, and the Ministry of Inclusion's 34 IMV inclusion-itinerary RCTs.
- **Administrative Register Spine:** Continuous linkage via DNI/NIE to Seguridad Social (INSS/TGSS daily affiliation & contribution bases), AEAT/Foral tax filings, SEPE unemployment records, SNS primary-care/mental-health electronic records, and INCASÒL/autonomous rental deposit registries.

## 5. Methods & identification
1. **Three-Tier Comparative Pilot Blueprint (`D-005`):**
   - *Option 1 (Municipal Tier):* Urban/rural pair (e.g. metropolitan Barcelona/Madrid district + rural Castile/Extremadura municipality), duration 36 months, testing Tier A (€600) vs. Tier B (€900).
   - *Option 2 (Regional Tier):* Parallel *Régimen Común* (Catalonia saturation + individual RCT) and *Régimen Foral* (Basque Country / Navarre net-tax IRPF integration arm).
   - *Option 3 (National Phase-In Cohort):* Staggered national rollout by birth-cohort or AI-displaced sector (`M17`) evaluated via regression discontinuity and difference-in-differences.
2. **Power, MDE & Budget Calculator:** Derive exact sample sizes, ICC adjustments, MDEs, and net fiscal pilot budgets (€180M–€450M over 3 years, co-financeable via EU ESF+ social innovation funds).

## 6. Pilot implications
- **Ethics & Post-Pilot Cliff (`ethics_equity`):** Pre-commit to a 6-month tapered step-down transition after month 36 plus a binding legal guarantee (`M06`, `M07`) that no participant loses prior entitlement to IMV, RGI/RGC, or disability benefits.
- **Pre-Registration:** Register complete Pre-Analysis Plan (PAP) at the AEA RCT Registry before baseline randomization.

## 7. Risks, counterarguments & open issues
- **Counterargument (Hawthorne & Horizon Bias):** Participants know a 3-year pilot is temporary, attenuating permanent-income responses (such as career switches or fertility/migration) relative to a permanent law [@hoynes-rothstein-2019]. *Mitigation:* Stratify horizon expectations and combine 3-year RCT estimates with structural parameters from permanent Spanish pension/disability discontinuities (`M08`).

## 8. Deliverables & effort
- Complete Pre-Analysis Plan (PAP) Template, Power/MDE Tables, and Budget Envelopes for Municipal, Regional, and National pilots.
- Administrative Data-Linking Protocol (INSS-AEAT-INE-SNS) for Chapter 7. (Effort: 7 person-weeks).
