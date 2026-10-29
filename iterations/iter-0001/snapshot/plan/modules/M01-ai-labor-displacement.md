---
id: M01
title: AI labor displacement and macroeconomic scenarios
status: draft
locked: false
depends_on: [M08, M16]
covers: [F01]
feeds_chapters: [1, 2]
last_iteration: 0
---
# M01 · AI labor displacement and macroeconomic scenarios

## 1. Why this matters
The case for a Universal Basic Rent in Spain rests on whether generative and agentic AI produce a qualitatively different labor shock than previous automation waves [@acemoglu-restrepo-2019; @eloundou-2024-gpts]. If AI substitution outpaces task reinstatement across clerical, professional, and service occupations, Spain faces simultaneous compression of household wage income and erosion of the IRPF and Social Security payroll tax bases (`M03`, `M16`).

## 2. Research questions
- **RQ-M01-01**: What share of Spanish full-time equivalent (FTE) employment and aggregate wage bill in 3-digit CNO-11 occupations is exposed to direct substitution versus complementarity under AI scenarios S1, S2, and S3?
  - *Hypothesis:* At least 28% of Spanish FTE employment and 34% of the gross wage bill reside in high-exposure cognitive and administrative clusters where agentic substitution dominates complementarity under S2 and S3.
- **RQ-M01-02**: How does task-level AI displacement translate into net payroll tax (*cotizaciones sociales*) and IRPF revenue elasticity across Spanish autonomous communities?
  - *Hypothesis:* Each 1 percentage-point AI-induced drop in the labor income share reduces combined Spanish IRPF and Social Security revenues by 1.25–1.40 percentage points under the current tax schedule, with the steepest revenue drag in service-intensive urban regions (Madrid, Catalonia).

## 3. State of knowledge
Task-based frameworks show that automation depresses the labor share whenever displacement effects exceed productivity and new-task reinstatement effects [@acemoglu-restrepo-2019; @acemoglu-2024-macro-ai]. Empirical indices of LLM and AI exposure [@eloundou-2024-gpts; @felten-2021-aioe; @webb-2020-ai] and cross-country assessments by the IMF and ILO [@cazzaniga-imf-2024; @gmyrek-ilo-2023] indicate that advanced economies face higher gross exposure than emerging markets, with clerical, financial, legal, and customer-service workers particularly vulnerable to displacement, while transition models to AGI demonstrate sharp wage compression once cognitive tasks are automated [@korinek-suh-2024].

## 4. Spain context & data sources
Spain enters the AI transition with structural unemployment near 11%, youth unemployment above 25%, and a dual labor market only partially mitigated by the 2021 labor reform. Primary datasets include:
- INE *Encuesta de Población Activa* (EPA) quarterly microdata (occupational structure at 3-digit CNO-11, hours, tenure).
- *Muestra Continua de Vidas Laborales* (MCVL, Seguridad Social) linked to tax records for longitudinal wage and contribution trajectories.
- INE *Encuesta Anual de Estructura Salarial* (EAES) and *Encuesta sobre el uso de TIC y comercio electrónico en las empresas* (firm-level AI adoption).

## 5. Methods & identification
1. **Crosswalk & Exposure Scoring:** Map O*NET task exposure scores [@eloundou-2024-gpts; @felten-2021-aioe; @webb-2020-ai] to ISCO-08 and Spanish CNO-11 using European Skills/Competences (ESCO) weights.
2. **Shift-Share & Event-Study Identification:** Estimate causal displacement elasticities in MCVL/EPA using pre-shock occupational exposure interacted with sectoral AI compute/software investment shocks (shift-share IV), controlling for firm and worker fixed effects.
3. **Scenario Calibration (S1–S3):** Feed estimated task-substitution elasticities into an Acemoglu-Restrepo sectoral model to generate quarterly paths of displaced FTEs, wage deciles, and payroll tax erosion for `M03` and `M04`.

## 6. Pilot implications
- **Municipal:** Select pilot municipalities spanning high service/back-office exposure (e.g. metropolitan Barcelona/Madrid suburbs) and manufacturing/agricultural baselines.
- **Regional:** Stratify Autonomous Community comparisons by CNO-11 cognitive exposure share.
- **National:** Define macroeconomic indicators (quarterly EPA cognitive-displacement index and Social Security contribution-to-GDP ratio) that automatically trigger transitions from S1 to S2/S3 policy tiers (`M17`).

## 7. Risks, counterarguments & open issues
- **Counterargument (Aggregate Productivity Modesty):** Acemoglu [@acemoglu-2024-macro-ai] argues five-year TFP gains from AI may be modest (~0.7%), implying slow displacement. *Mitigation:* Explicitly bracket S1 (slow/moderate, consistent with Acemoglu) against S2 and S3 [@korinek-suh-2024] rather than assuming immediate collapse.
- **Occupational Reclassification Noise:** CNO-11 codes may mask within-occupation task reorganization.

## 8. Deliverables & effort
- CNO-11 AI Exposure & Wage-Bill Dataset for Spain (R/Python pipeline on EPA + EAES).
- Chapter 2 empirical tables and S1–S3 scenario input vectors for EUROMOD (`M03`, `M09`) and HANK (`M04`). (Effort: 6 person-weeks).
