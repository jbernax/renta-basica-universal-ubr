---
id: M10
title: Multi-level pilot and causal evaluation design
status: draft
locked: false
depends_on: [M02, M05, M06, M08, M12, M15]
covers: [F11]
feeds_chapters: [7]
last_iteration: 3
---
# M10 · Multi-level pilot and causal evaluation design

## 1. Why this matters
Past basic income trials worldwide have suffered from four fundamental methodological limitations: (i) dispersed individual-level randomization that inherently cannot detect general-equilibrium effects on local rents, prices, or wages [@egger-2022-ge-kenya; @banerjee-niehaus-suri-2019; @hoynes-rothstein-2019]; (ii) severe spatial interference and SUTVA violations when clusters are defined as porous urban census tracts without buffer zones and daily commuting weight matrices [@baird-2018-interference; @ine-movilidad-telefonia]; (iii) clawback arms that create concave kinks without estimating missing mass or providing convex disregard kinks [@kleven-2016-bunching; @saez-2010-bunching]; and (iv) administrative tax secrecy barriers under Spanish law that trigger differential attrition in control groups [@boe-lgt-2003; @boe-lopdgdd-2018]. Following `D-005`, this module establishes a statistically powered, pre-registered multi-level Spanish pilot architecture comparing **Municipal**, **Regional (Régimen Común vs. Régimen Foral)**, and **National** experimental options, linked directly to administrative registers with SUTVA commuting buffers and bunching econometrics.

## 2. Research questions
- **RQ-M10-01**: How can a two-stage randomized spatial saturation design with mobile-phone commuting weight matrices ($W_{\text{mobility}}$) and geographic buffer zones jointly identify partial-equilibrium behavioral responses and local general-equilibrium spillovers (rental pass-through `M05`, reservation wage bargaining `M08`, and local retail multipliers `M04`) while satisfying SUTVA?
  - *Hypothesis:* Randomizing across $J = 70$ spatial clusters (bounded in metropolitan areas by Functional Urban Areas with $\ge 80\%$ internal commuting self-containment, and in non-metropolitan zones by small municipalities of 1,500–5,000 residents with $\ge 2\text{--}5$ km buffer zones and mobile mobility weights per Baird et al. [@baird-2018-interference], Egger et al. [@egger-2022-ge-kenya], Duflo et al. [@duflo-2007-randomization], and INE [@ine-movilidad-telefonia], $N \approx 20,000$ participants) provides 80% statistical power ($\alpha = 0.05$) under two-stage saturation variance math to detect a $\ge 1.2$ hour/week labor supply adjustment and a $\ge 2.8\%$ local rental pass-through differential evaluated via Synthetic Difference-in-Differences (SDID, Arkhangelsky et al. [@arkhangelsky-2021-sdid]) on 100% census-linked deposit registries (*fianzas*).
- **RQ-M10-02**: How can an experimental pilot identify labor-supply substitution elasticities without violating Constitutional equal treatment (Art. 14 CE) or tax legality (Art. 31.1 CE), while estimating responses around both convex and concave budget kinks?
  - *Hypothesis:* Structuring an initial labor income disregard ($Y_{\text{disregard}} = \text{€}3,000\text{--}\text{€}5,000/\text{year}$) followed by randomized benefit phase-out rates ($0\%$, $38\%$, and $50\%$ clawback bounded at the gross grant envelope) creates a true convex kink with excess mass for Saez [@saez-2010-bunching] and Chetty et al. [@chetty-2011-bunching; @chetty-2012-bounds] bunching estimators, while formalizing a missing-mass estimator at the upper concave phase-out boundary $Y^* = \text{UBR}/\tau_{\text{clawback}}$ per Kleven [@kleven-2016-bunching], cleanly identifying compensated wage and income elasticities ($\varepsilon^c, \eta$) in full compliance with constitutional law.
- **RQ-M10-03**: What legal, technical, and fiscal architecture ensures continuous register linkage across AEAT, TGSS, and decentralized regional health services without violating tax secrecy (Art. 95 LGT) or inducing differential control attrition?
  - *Hypothesis:* A statutory habilitation provision under Art. 95.1.k LGT [@boe-lgt-2003], paired with cryptographic HMAC-SHA256 salted hashing, an unconditional Evaluation Participation Stipend (€250–€300/year) for control participants, and a bifurcated healthcare data spine (Tier 1 centralized INSS temporary disability *bajas IT* registers; Tier 2 bilateral regional agreements under *Ley 16/2003* [@ley-16-2003-sns]), achieves >95% continuous register-linkage completion across treated and control arms.

## 3. State of knowledge
Landmark trials—OpenResearch [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health], GiveDirectly Kenya [@egger-2022-ge-kenya], Finland [@kangas-2021-finland], Stockton SEED [@west-2024-seed], and Barcelona's B-MINCOME [@todeschini-bmincome-2020]—demonstrate that linking national administrative registers eliminates differential survey attrition on earnings and employment. Furthermore, two-stage randomized saturation [@egger-2022-ge-kenya; @banerjee-niehaus-suri-2019] is statistically indispensable for disentangling displacement and price spillovers from individual treatment effects. However, Baird et al. [@baird-2018-interference] and Duflo et al. [@duflo-2007-randomization] establish that unless saturation clusters enforce geographic buffer zones and account for daily commuting flows, spatial spillovers violate the Stable Unit Treatment Value Assumption (SUTVA). Spain's decentralized institutional context requires bifurcating centralized tax/labor registers from regional health microdata (*Ley 16/2003* [@ley-16-2003-sns]).

## 4. Spain context & data sources
- **Spanish Precedents:** Barcelona B-MINCOME (2017–2019 [@todeschini-bmincome-2020]), Catalonia's saturation blueprint, and the Ministry of Inclusion's 34 randomized social-itinerary IMV pilots coordinated by CEMFI and J-PAL Europe [@inclusion-cemfi-jpal-2024].
- **Administrative Register Spine & Data Linkage Protocol:** Continuous, anonymized microdata linkage via DNI/NIE across:
  - *Seguridad Social* (TGSS daily affiliation, contract modalities 100/200/300, and *bases de cotización* in MCVL).
  - *Agencia Tributaria* (AEAT) and Basque/Navarrese Foral Treasuries (monthly *retenciones* Modelo 111, annual IRPF Modelo 100). Enabled by a model statutory provision under Art. 95.1.k *Ley General Tributaria* (LGT [@boe-lgt-2003]) and *Ley Orgánica 3/2018* (LOPDGDD [@boe-lopdgdd-2018]) using HMAC-SHA256 salted pseudonymization.
  - *Servicio Público de Empleo Estatal* (SEPE) unemployment registers and benefit claims.
  - *Bifurcated Health Architecture:* Tier 1 centralized INSS *Incapacidad Temporal* (IT) administrative registers (daily sickness duration and psychiatric diagnoses); Tier 2 bilateral research convenios under *Ley 16/2003* [@ley-16-2003-sns] with pilot regional health services (CatSalut, SERMAS, Osakidetza) for primary care consultations and psychotropic prescription invoicing (with INE ECV/ENSE health modules as administrative fallbacks).
  - *Fianzas de Alquiler* Registries (INCASÒL in Catalonia, IVIMA in Madrid, AVRA in Andalusia) for 100% census linkage of transaction-level lease contracts and executed rents.
  - *Mobility Matrix:* MITMA/INE *Estudio de la Movilidad con Telefonía Móvil* [@ine-movilidad-telefonia] providing origin-destination commuting matrices ($W_{\text{mobility}}$).

## 5. Methods & identification
1. **Two-Stage Spatial Saturation with Commuting Flow Weights & Power Math:**
   - Define $J = 70$ clusters (35 treated, 35 control) stratified by private rental density (>35%). In metropolitan areas, boundaries are aligned with Functional Urban Areas (FUAs) with $\ge 80\%$ internal commuting self-containment; in non-metropolitan areas, clusters are separated by $\ge 2\text{--}5$ km buffer zones.
   - Specify a continuous spatial spillover exposure estimator per Egger et al. [@egger-2022-ge-kenya] and Baird et al. [@baird-2018-interference]:
     $$Y_{ic} = \alpha + \beta_1 T_{ic} + \beta_2 \text{Cash}_c + \gamma \sum_j W_{cj} \cdot \text{Cash}_j + X'_{ic} \delta + \varepsilon_{ic}$$
     where $W_{cj}$ denotes normalized daily commuting flows from INE's mobile telephony study [@ine-movilidad-telefonia].
   - Compute MDE using two-stage saturation variance equations (Baird et al. [@baird-2018-interference]) and evaluate rent pass-through via Synthetic Difference-in-Differences (SDID, Arkhangelsky et al. [@arkhangelsky-2021-sdid]) on 100% census-linked deposit records (*fianzas* in INCASÒL/IVIMA/AVRA).
   - Conduct inference using wild cluster bootstrap and randomization inference to guard against small-sample cluster over-rejection [@egger-2022-ge-kenya].
2. **Convex Disregard & Missing-Mass Bunching Econometrics:**
   - Randomly assign treated participants to three clawback structures with an initial labor income disregard ($Y_{\text{disregard}} = \text{€}3,000\text{--}\text{€}5,000/\text{year}$ per RD 789/2022 and RDL 2/2024):
     - *Arm A (Pure UBR / 0% clawback):* Full €900/month cash transfer with standard baseline IRPF.
     - *Arm B (Moderate clawback / 38%):* €900/month reduced by 38c per euro of earnings above $Y_{\text{disregard}}$, bounded at zero grant ($Y^* = \text{€}28,421/\text{year}$).
     - *Arm C (High clawback / 50%):* €900/month reduced by 50c per euro of earnings above $Y_{\text{disregard}}$, bounded at zero grant ($Y^* = \text{€}21,600/\text{year}$).
   - Estimate excess mass bunching at the convex disregard kink ($Y_{\text{disregard}}$) per Saez [@saez-2010-bunching] and Chetty et al. [@chetty-2011-bunching], and estimate missing mass at the concave phase-out ceiling $Y^*$ per Kleven [@kleven-2016-bunching].
3. **Register Linkage & Control Retention Protocol:**
   - Pay an unconditional Evaluation Participation Stipend (€250–€300/year) to control participants to eliminate differential attrition.
   - Net 36-month pilot budget: €480M gross transfers + €35M administration/data spine - €220M clawback/benefit offsets = €295M net (~€98M/year), funded through dedicated R&D innovation appropriations in the State General Budget (*PGE*).

## 6. Pilot implications
- **Municipal Tier:** Feasible for localized testing of subjective well-being, health, and local consumption multipliers, but legally prohibited from altering IRPF withholdings or national social security registers; highly vulnerable to local cross-border shopping without spatial buffer zones.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común* (e.g. Catalonia, Andalusia, Valencia), regional pilots must coordinate with the State Ministry of Inclusion and AEAT to secure register access under Art. 95.1.k LGT, and cannot modify the state portion of IRPF.
  - In *Régimen Foral* (Basque Country or Navarre), regional governments possess comprehensive tax and social protection competence under the *Concierto Económico*, providing the optimal constitutional testbed for testing integrated tax-transfer clawbacks and unified payroll clearing (`M12`).
- **National Tier:** Staggered cohort rollout across whole sectors displaced by AI (`M01`), providing macroeconomic macro-closure evaluation (`M04`) and testing full national AEAT automated clearing without territorial leakages.

## 7. Risks, counterarguments & open issues
- **Counterargument (Finite-Horizon Bias):** A 36-month pilot cannot replicate permanent-income life-cycle responses (such as fertility, long-term educational retraining, or career abandonment) [@hoynes-rothstein-2019]. *Mitigation:* Explicitly model the finite-horizon transition mathematically separating windfall income effects from Frisch intertemporal substitution (`M15`), and communicate a 6-month post-pilot step-down ramp to participants to prevent welfare cliffs.
- **Counterargument (Control Group Resentment & Attrition):** Non-treated controls in saturated clusters experience survey fatigue and drop out. *Mitigation:* Guarantee register linkage via the Art. 95 LGT statutory protocol, minimize survey burden, and provide the annual €250–€300 participation stipend.

## 8. Deliverables & effort
- Comprehensive Pre-Analysis Plan (PAP) registered on AEA RCT Registry with statistical power calculations, buffer-zone coordinates, and mock analysis scripts.
- Multi-Tier Pilot Technical Blueprint and Inter-Administrative Data-Linking Protocol (INSS-AEAT-TGSS-SNS). (Effort: 7 person-weeks).
