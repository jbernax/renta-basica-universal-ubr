---
id: M14
title: Gender, unpaid care, disability, and health outcomes
status: draft
locked: false
depends_on: [M02, M07, M08, M09, M10]
covers: [F15]
feeds_chapters: [3, 7]
last_iteration: 0
---
# M14 · Gender, unpaid care, disability, and health outcomes

## 1. Why this matters
Spanish women perform over two-thirds of unpaid domestic and dependent-care hours, experience higher part-time employment and career interruptions, and consequently receive lower contributory pensions and unemployment benefits (`M07`). Because means-tested schemes like IMV [@boe-imv-2021] assess and pay a single household head (*titular*), they fail to guarantee financial autonomy inside the household. Paying UBR individually (`D-001`) directly alters intra-household bargaining power, financial independence for survivors of gender violence, care valuation, and population mental/physical health [@miller-2024-openresearch-health; @west-2024-seed].

## 2. Research questions
- **RQ-M14-01**: How does an individual UBR (`M02`) change the gender gap in personal disposable income, intra-household bargaining power, time allocation between paid work and unpaid care, and exit capacity from abusive partnerships in Spain?
  - *Hypothesis:* Tier B individual UBR reduces the share of cohabiting Spanish women with zero or below-poverty personal income from ~19% to 0%, increases male partner participation in unpaid care when combined with non-transferable parental leave, and significantly accelerates financial autonomy for gender-violence survivors.
- **RQ-M14-02**: What are the causal impacts of unconditional monthly income security on mental health (anxiety, depression, cortisol/sleep disorders), preventive healthcare utilization, and pharmaceutical expenditure in Spain's *Sistema Nacional de Salud* (SNS)?
  - *Hypothesis:* Consistent with Finland [@kangas-2021-finland], B-MINCOME [@todeschini-bmincome-2020], Stockton [@west-2024-seed], and OpenResearch [@miller-2024-openresearch-health], UBR reduces clinically significant psychological distress (GHQ-12 / PHQ-9) by 0.20–0.35 standard deviations and lowers primary-care mental-health and anxiolytic prescription costs by 8–14% among bottom-quintile adults.

## 3. State of knowledge
Across nearly every basic income trial, improvements in mental health, stress reduction, food security, and subjective wellbeing are the largest and most statistically robust findings [@kangas-2021-finland; @todeschini-bmincome-2020; @west-2024-seed; @miller-2024-openresearch-health]. Feminist economics emphasizes two competing gender effects of basic income: individual unconditional cash empowers women's exit options and values unpaid care [@van-parijs-vanderborght-2017], but could reinforce traditional gendered division of labor if secondary female earners reduce formal hours without accompanying public care infrastructure (*Sistema para la Autonomía y Atención a la Dependencia*, SAAD, and 0–3 early childhood education).

## 4. Spain context & data sources
- **Time-Use & Health Datasets:** INE *Encuesta de Empleo del Tiempo* (EET), *Encuesta Nacional de Salud de España* (ENSE) / *Encuesta Europea de Salud* (EESE), and Ministry of Health *Base de Datos Clínicos de Atención Primaria* (BDCAP).
- **Disability & Care Framework:** *Ley 39/2006 de Promoción de la Autonomía Personal y Atención a las personas en situación de dependencia* (SAAD) and *Real Decreto Legislativo 1/2013* on rights of persons with disabilities.

## 5. Methods & identification
1. **Individual vs. Pooled Intra-Household Microsimulation:** In EUROMOD-Spain (`M09`), compute inequality and poverty under both full income-pooling and zero/partial-sharing collective household models to measure the gender gap in individual economic security.
2. **Health & Healthcare Cost-Offset Estimation (`M10`):** In the Spanish pilot, link consented participants' SNS health-card records to measure PHQ-9/GAD-7 scores, emergency room visits, anxiolytic/antidepressant DDDs (*dosis diarias definidas*), and child birthweight/pediatric outcomes.
3. **Disability Extra-Cost Protection Audit:** Verify that all *Grado I–III* dependency and disability supplements (`M07`) remain strictly additive on top of UBR to cover conversion handicaps.

## 6. Pilot implications
- **Municipal / Regional / National (`M10`):** Stratify randomization by gender and caregiving status; forbid substituting UBR for in-kind public care services (0–3 nurseries, SAAD home care).

## 7. Risks, counterarguments & open issues
- **Counterargument (Maternal Labor Market Detachment):** Unconditional transfers could encourage low-wage mothers to exit the formal labor market permanently. *Mitigation:* Pair UBR with universal 0–3 public childcare and estimate separate female intensive/extensive elasticities in `M08` and `M10`.

## 8. Deliverables & effort
- Intra-Household Gender Autonomy & Care-Time Simulation.
- SNS Mental/Physical Health Cost-Offset & Disability Protection Protocol for Chapter 3 and Chapter 7. (Effort: 4 person-weeks).
