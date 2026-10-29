---
id: M10
title: Multi-level pilot and causal evaluation design
status: draft
locked: false
depends_on: [M02, M05, M06, M08, M12, M15]
covers: [F11]
feeds_chapters: [7]
last_iteration: 1
---
# M10 · Multi-level pilot and causal evaluation design

## 1. Why this matters
Past basic income trials worldwide have suffered from three fundamental methodological limitations: (i) dispersed individual-level randomization that inherently cannot detect general-equilibrium effects on local rents, prices, or wages [@egger-2022-ge-kenya; @banerjee-niehaus-suri-2019; @hoynes-rothstein-2019]; (ii) testing only gross windfall transfers without the behavioral clawback or tax-financing schedule; and (iii) severe attrition in self-reported survey outcomes [@kangas-2021-finland; @bartik-2024-openresearch]. Following `D-005`, this module establishes a statistically powered, pre-registered multi-level Spanish pilot architecture comparing **Municipal**, **Regional (Régimen Común vs. Régimen Foral)**, and **National** experimental options, linked directly to administrative registers.

## 2. Research questions
- **RQ-M10-01**: How can a two-stage randomized spatial saturation design in Spain jointly identify partial-equilibrium behavioral responses (individual labor supply, physical and mental health, consumption) and local general-equilibrium spillovers (rental pass-through `M05`, reservation wage bargaining `M08`, and local retail multipliers `M04`)?
  - *Hypothesis:* Expanding saturation clusters to $J = 60\text{–}80$ spatial units (30–40 treated vs. 30–40 matched control census-tract groups or small municipalities with $N \approx 20,000$ total participants) provides 80% statistical power ($\alpha = 0.05$) via wild cluster bootstrap and randomization inference to detect a $\ge 1.2$ hour/week labor supply adjustment and a $\ge 3.0\%$ local rental pass-through differential without degrees-of-freedom compression.
- **RQ-M10-02**: How can an experimental pilot identify labor-supply substitution elasticities without violating Constitutional equal treatment (Art. 14 CE) or tax legality (Art. 31.1 CE) through arbitrary randomized tax hikes?
  - *Hypothesis:* Randomizing an explicit **Benefit Phase-Out / Clawback Rate Arm** ($0\%$ clawback / pure UBR, $38\%$ clawback, and $50\%$ clawback) where clawbacks are strictly deducted from the experimental grant envelope (so no participant ever pays more than their baseline statutory IRPF liability) cleanly identifies compensated wage and income elasticities ($\varepsilon^c, \eta$) in full compliance with constitutional law.
- **RQ-M10-03**: What is the realistic net fiscal envelope of a 36-month pilot, and how can financing be structured without relying on EU ESF+ funds for non-vulnerable universal cohorts?
  - *Hypothesis:* A 36-month pilot with $N = 20,000$ participants requires a gross cash budget of €432M–€648M (€144M–€216M/year), reduced by 35–45% via clawbacks and automatic benefit consolidation, funded through dedicated national/regional R&D appropriations and active labor-market funds rather than earmarked ESF+ anti-poverty envelopes.

## 3. State of knowledge
Landmark trials—OpenResearch [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health], GiveDirectly's village-saturation experiment in Kenya [@egger-2022-ge-kenya], Finland's nationwide register-linked trial [@kangas-2021-finland], Stockton SEED [@west-2024-seed], and Barcelona's B-MINCOME [@todeschini-bmincome-2020]—demonstrate that linking national administrative registers eliminates differential survey attrition on earnings and employment. Furthermore, two-stage randomized saturation [@egger-2022-ge-kenya; @banerjee-niehaus-suri-2019] is statistically indispensable for disentangling displacement and price spillovers from individual treatment effects. Catalonia's 2021–2023 Office for the Basic Income Pilot Plan designed a hybrid individual and municipal saturation blueprint, providing valuable operational protocols despite its legislative delay (`M11`).

## 4. Spain context & data sources
- **Spanish Precedents:** Barcelona B-MINCOME (2017–2019, 1,000 vulnerable households across 10 Besòs neighborhoods testing conditional vs. unconditional transfers [@todeschini-bmincome-2020]), Catalonia's saturation protocol blueprint, and the Ministry of Inclusion's 34 randomized social-itinerary IMV pilots.
- **Administrative Register Spine:** Continuous, anonymized microdata linkage via DNI/NIE across:
  - *Seguridad Social* (TGSS daily affiliation, contract modalities 100/200/300, and *bases de cotización* in MCVL).
  - *Agencia Tributaria* (AEAT) and Basque/Navarrese Foral Treasuries (monthly *retenciones* Modelo 111, annual IRPF Modelo 100).
  - *Servicio Público de Empleo Estatal* (SEPE) unemployment registers and benefit claims.
  - *Sistema Nacional de Salud* (SNS) electronic clinical records (primary care consultations, psychotropic prescriptions, sick leave *bajas IT*).
  - *Fianzas de Alquiler* Registries (INCASÒL in Catalonia, IVIMA/AEMA in Madrid, and regional equivalents) for transaction-level lease contracts and executed rents.

## 5. Methods & identification
1. **Two-Stage Spatial Saturation & Cluster Power:**
   - Group Spain's ~36,000 census tracts (*secciones censales*) into $J = 70$ balanced clusters (35 treated clusters, 35 control clusters across 4 urban/metropolitan and 4 peri-urban/rural provinces).
   - In treated clusters, randomly assign high saturation (80% of adult residents receive UBR Tier B) or moderate saturation (40% receive UBR Tier B) to identify local general-equilibrium pass-through on residential rents (`M05`) and local non-tradable goods prices (`M04`).
   - Conduct inference using wild cluster bootstrap and randomization inference to guard against small-sample cluster over-rejection [@egger-2022-ge-kenya].
2. **Benefit Phase-Out Arm for Elasticity Identification:**
   - Randomly assign treated participants to three clawback structures:
     - *Arm A (Pure UBR / 0% clawback):* Full €900/month cash transfer with standard baseline IRPF.
     - *Arm B (Moderate clawback / 38%):* €900/month cash transfer reduced by 38 cents per euro of gross earnings, bounded at zero net grant.
     - *Arm C (High clawback / 50%):* €900/month cash transfer reduced by 50 cents per euro of gross earnings, bounded at zero net grant.
   - This variation identifies the compensated substitution elasticity $\varepsilon^c$ and income elasticity $\eta$ without exposing any citizen to unconstitutional discriminatory taxation.
3. **Budget Envelope & Financing Structure:**
   - Total 36-month pilot envelope: €480M gross transfers + €35M administration and data spine = €515M total.
   - Net outlays after clawback recoveries and existing benefit offsets (IMV, RGI, regional rents): €295M over 3 years (~€98M/year).
   - Financed via dedicated R&D innovation allocations from the State General Budget (*PGE*), Regional innovation funds, and private research foundations, strictly avoiding misclassification under EU ESF+ poverty-alleviation quotas.

## 6. Pilot implications
- **Municipal:** Feasible for localized testing of subjective well-being, health, and local consumption multipliers, but legally prohibited from altering IRPF withholdings or national social security registers; highly vulnerable to local cross-border shopping and municipal residential sorting.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común* (e.g. Catalonia, Andalusia, Valencia), regional pilots must coordinate with the State Ministry of Inclusion and AEAT to secure register access, and cannot modify the state portion of IRPF.
  - In *Régimen Foral* (Basque Country or Navarre), regional governments possess comprehensive tax and social protection competence under the *Concierto Económico*, providing the optimal constitutional testbed for testing integrated tax-transfer clawbacks and unified payroll clearing (`M12`).
- **National:** Staggered cohort rollout across whole sectors displaced by AI (`M01`), providing macroeconomic macro-closure evaluation (`M04`) and testing full national AEAT automated clearing without territorial leakages.

## 7. Risks, counterarguments & open issues
- **Counterargument (Finite-Horizon Bias):** A 36-month pilot cannot replicate permanent-income life-cycle responses (such as fertility, long-term educational retraining, or career abandonment) [@hoynes-rothstein-2019]. *Mitigation:* Explicitly model the finite-horizon transition mathematically in pre-registered structural models (`M15`) and communicate the 6-month post-pilot step-down ramp to participants to prevent welfare cliffs.
- **Counterargument (Ethical Compensation Cliff):** Abruptly terminating payments at month 36 creates adverse health and income shocks for low-income participants. *Mitigation:* Legally guarantee automatic reinscription into IMV or regional minimum incomes without waiting periods upon pilot conclusion (`M07`).

## 8. Deliverables & effort
- Comprehensive Pre-Analysis Plan (PAP) registered on AEA RCT Registry with statistical power calculations and mock data analysis scripts.
- Multi-Tier Pilot Technical Blueprint and Inter-Administrative Data-Linking Protocol (INSS-AEAT-TGSS-SNS). (Effort: 7 person-weeks).
