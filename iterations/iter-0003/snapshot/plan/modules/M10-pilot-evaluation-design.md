---
id: M10
title: Multi-level pilot and causal evaluation design
status: draft
locked: false
depends_on: [M02, M05, M06, M08, M12, M15]
covers: [F11]
feeds_chapters: [7]
last_iteration: 2
---
# M10 · Multi-level pilot and causal evaluation design

## 1. Why this matters
Past basic income trials worldwide have suffered from four fundamental methodological limitations: (i) dispersed individual-level randomization that inherently cannot detect general-equilibrium effects on local rents, prices, or wages [@egger-2022-ge-kenya; @banerjee-niehaus-suri-2019; @hoynes-rothstein-2019]; (ii) severe spatial interference and SUTVA violations when clusters are defined as narrow, porous urban census tracts without buffer zones [@baird-2018-interference]; (iii) clawback arms that phase out at median earnings, creating threshold kinks without identifying upper-bracket behavioral responses; and (iv) administrative tax secrecy barriers under Spanish law that trigger differential attrition in control groups [@boe-lgt-2003; @boe-lopdgdd-2018]. Following `D-005`, this module establishes a statistically powered, pre-registered multi-level Spanish pilot architecture comparing **Municipal**, **Regional (Régimen Común vs. Régimen Foral)**, and **National** experimental options, linked directly to administrative registers with SUTVA buffers and bunching econometrics.

## 2. Research questions
- **RQ-M10-01**: How can a two-stage randomized spatial saturation design with mandatory geographic buffer zones jointly identify partial-equilibrium behavioral responses and local general-equilibrium spillovers (rental pass-through `M05`, reservation wage bargaining `M08`, and local retail multipliers `M04`) while satisfying SUTVA?
  - *Hypothesis:* Randomizing across $J = 70$ economically self-contained spatial clusters (distinct small municipalities of 1,500–5,000 residents and transit-bounded urban districts with $\ge 2\text{--}5$ km buffer zones per Baird et al. [@baird-2018-interference] and Duflo et al. [@duflo-2007-randomization], $N \approx 20,000$ participants) provides 80% statistical power ($\alpha = 0.05$) to detect a $\ge 1.2$ hour/week labor supply adjustment and a $\ge 2.8\%$ local rental pass-through differential without spatial contamination.
- **RQ-M10-02**: How can an experimental pilot identify labor-supply substitution elasticities without violating Constitutional equal treatment (Art. 14 CE) or tax legality (Art. 31.1 CE), while estimating responses around the clawback phase-out kink ($Y^*$)?
  - *Hypothesis:* Randomizing an explicit **Benefit Phase-Out / Clawback Rate Arm** ($0\%$, $38\%$, and $50\%$ clawback bounded at the gross grant envelope) paired with a pre-registered bunching estimator (Saez [@saez-2010-bunching]; Chetty et al. [@chetty-2012-bounds]) around $Y^* = \text{UBR}/\tau_{\text{clawback}}$ cleanly identifies compensated wage and income elasticities ($\varepsilon^c, \eta$) in full compliance with constitutional law, leaving upper-decile tax responses to administrative IRPF panel reforms (`M08`).
- **RQ-M10-03**: What legal, technical, and fiscal architecture ensures continuous register linkage across AEAT, TGSS, and SNS without violating tax secrecy (Art. 95 LGT) or inducing differential control attrition?
  - *Hypothesis:* A statutory habilitation provision under Art. 95.1.k LGT [@boe-lgt-2003], paired with cryptographic HMAC-SHA256 salted hashing and an unconditional Evaluation Participation Stipend (€250–€300/year) for control participants, achieves >95% continuous register-linkage completion across treated and control arms.

## 3. State of knowledge
Landmark trials—OpenResearch [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health], GiveDirectly Kenya [@egger-2022-ge-kenya], Finland [@kangas-2021-finland], Stockton SEED [@west-2024-seed], and Barcelona's B-MINCOME [@todeschini-bmincome-2020]—demonstrate that linking national administrative registers eliminates differential survey attrition on earnings and employment. Furthermore, two-stage randomized saturation [@egger-2022-ge-kenya; @banerjee-niehaus-suri-2019] is statistically indispensable for disentangling displacement and price spillovers from individual treatment effects. However, Baird et al. [@baird-2018-interference] establish that unless saturation clusters enforce geographic buffer zones, spatial spillovers violate the Stable Unit Treatment Value Assumption (SUTVA). Catalonia's 2021–2023 Office for the Basic Income Pilot Plan designed a hybrid individual and municipal saturation blueprint, providing valuable operational protocols despite its legislative delay (`M11`).

## 4. Spain context & data sources
- **Spanish Precedents:** Barcelona B-MINCOME (2017–2019 [@todeschini-bmincome-2020]), Catalonia's saturation blueprint, and the Ministry of Inclusion's 34 randomized social-itinerary IMV pilots.
- **Administrative Register Spine & Data Linkage Protocol:** Continuous, anonymized microdata linkage via DNI/NIE across:
  - *Seguridad Social* (TGSS daily affiliation, contract modalities 100/200/300, and *bases de cotización* in MCVL).
  - *Agencia Tributaria* (AEAT) and Basque/Navarrese Foral Treasuries (monthly *retenciones* Modelo 111, annual IRPF Modelo 100). Enabled by a model statutory provision under Art. 95.1.k *Ley General Tributaria* (LGT [@boe-lgt-2003]) and *Ley Orgánica 3/2018* (LOPDGDD [@boe-lopdgdd-2018]) using HMAC-SHA256 salted pseudonymization.
  - *Servicio Público de Empleo Estatal* (SEPE) unemployment registers and benefit claims.
  - *Sistema Nacional de Salud* (SNS) electronic clinical records (primary care consultations, psychotropic prescriptions, sick leave *bajas IT*).
  - *Fianzas de Alquiler* Registries (INCASÒL in Catalonia, IVIMA in Madrid, AVRA in Andalusia) for transaction-level lease contracts and executed rents.

## 5. Methods & identification
1. **Two-Stage Spatial Saturation with Buffer Zones & Power Math:**
   - Define $J = 70$ clusters (35 treated, 35 control) as economically self-contained small municipalities (1,500–5,000 residents) in non-metropolitan areas and transit-bounded urban districts, surrounded by mandatory geographic buffer zones ($\ge 2\text{--}5$ km in rural/peri-urban zones; donut matching in urban areas) per Baird et al. [@baird-2018-interference] and Duflo et al. [@duflo-2007-randomization].
   - Compute cluster Minimum Detectable Effect (MDE):
     $$\text{MDE} = (t_{\alpha/2} + t_{1-\beta}) \sqrt{\frac{\sigma^2 (1 - R^2)}{P(1-P) J m} [1 + (m - 1)\rho]}$$
     Calibrated with Spanish empirical parameters: intraclass correlation coefficients $\rho_{\text{rent}} = 0.08$ and $\rho_{\text{labor}} = 0.03$, cluster size $m \approx 285$ adults, $P = 0.5$, $J = 70$, and baseline covariate explanatory power $R^2 \approx 0.35$ from pre-trial INCASÒL/MCVL microdata, yielding 80% power at $\alpha = 0.05$ to detect a 1.2 hour/week labor adjustment and a 2.8% rent pass-through effect.
   - Conduct inference using wild cluster bootstrap and randomization inference to guard against small-sample cluster over-rejection [@egger-2022-ge-kenya].
2. **Benefit Phase-Out Arm & Bunching Econometrics:**
   - Randomly assign treated participants to three clawback structures:
     - *Arm A (Pure UBR / 0% clawback):* Full €900/month cash transfer with standard baseline IRPF.
     - *Arm B (Moderate clawback / 38%):* €900/month reduced by 38c per euro of gross earnings, bounded at zero grant ($Y^* = \text{€}28,421/\text{year}$).
     - *Arm C (High clawback / 50%):* €900/month reduced by 50c per euro of gross earnings, bounded at zero grant ($Y^* = \text{€}21,600/\text{year}$).
   - Stratify sample across baseline earnings domains and implement Saez [@saez-2010-bunching] and Chetty et al. [@chetty-2012-bounds] bunching estimators around $Y^*$ to extract compensated substitution elasticities directly from excess mass, without violating constitutional tax legality.
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
