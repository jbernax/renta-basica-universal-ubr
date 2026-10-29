---
id: M14
title: Gender, unpaid care, disability, and health outcomes
status: draft
locked: false
depends_on: [M01, M02, M07, M08, M09, M10]
covers: [F15]
feeds_chapters: [3, 7]
last_iteration: 2
---
# M14 · Gender, unpaid care, disability, and health outcomes

## 1. Why this matters
Spanish women perform over two-thirds of unpaid domestic and care work, face persistent gender wage and pension gaps, and are disproportionately concentrated in administrative, clerical, customer-facing, and paralegal occupations that face the highest gross exposure to generative AI displacement under Scenarios S1–S3 (`M01`). Furthermore, traditional means-tested safety nets like the IMV [@boe-imv-2021] assess and transfer benefits to a single household representative (*titular*), reinforcing intra-household economic dependency and trapping secondary earners in poverty. Persons with disabilities face substantial non-discretionary economic extra costs (€3,500–€10,000/year [@puig-segura-2021-discapacidad]) that cannot be met by baseline cash transfers alone. By establishing strictly individual, unconditional cash entitlements (`D-001`) paired with dedicated disability supplements, UBR fundamentally alters intra-household bargaining power, care valuation, disability equity, and population mental health [@miller-2024-openresearch-health; @west-2024-seed].

## 2. Research questions
- **RQ-M14-01**: How does an individual, unconditional UBR (`M02`) reshape intra-household bargaining power, resource allocation, and time use between paid work and unpaid care in Spain when modeled within a collective household framework [@chiappori-1992-collective]?
  - *Hypothesis:* In an estimated Chiappori collective household model on INE *Encuesta de Empleo del Tiempo* (EET) and ECV microdata, individual UBR transfers raise female sharing rules by 8–15 percentage points in low-to-middle income couples, expanding personal non-housing consumption and reducing secondary-earner financial dependence without lowering male labor-force participation.
- **RQ-M14-02**: How will gender-asymmetric AI labor displacement across S1–S3 interact with UBR and the tiered **Complemento Universal por Discapacidad** under *Real Decreto 888/2022* [@boe-rd-888-2022-discapacidad] to prevent severe poverty feminization and offset disability extra costs?
  - *Hypothesis:* Without UBR, female-dominated clerical displacement under S2 leads to a 4.5 percentage-point increase in the female poverty risk; an individual €900/month UBR neutralizes this shock completely. For individuals with disabilities, adding a statutory disability supplement (+25% for 33–64%, +50% for 65–74%, +100% for $\ge 75\%$ per RD 888/2022) fully covers empirical extra living costs [@puig-segura-2021-discapacidad] without distorting labor participation.
- **RQ-M14-03**: What are the causal impacts of unconditional monthly income security on clinical mental health (anxiety, depression, sleep disorders) and pharmaceutical consumption within the Spanish National Health System (*Sistema Nacional de Salud*, SNS)?
  - *Hypothesis:* Consistent with Finland [@kangas-2021-finland], Barcelona B-MINCOME [@todeschini-bmincome-2020], Stockton [@west-2024-seed], and OpenResearch [@miller-2024-openresearch-health], UBR reduces moderate-to-severe psychological distress (PHQ-9/GHQ-12) by 0.22–0.35 standard deviations, lowering SNS primary care consultations and anxiolytic/antidepressant prescription costs by 9–15% among the lowest two income deciles.

## 3. State of knowledge
A substantial body of international evidence demonstrates that mental health gains, stress alleviation, and subjective wellbeing improvements are the most immediate and statistically significant outcomes of unconditional cash transfers [@kangas-2021-finland; @todeschini-bmincome-2020; @west-2024-seed; @miller-2024-openresearch-health]. In gender economics, collective household models [@chiappori-1992-collective] establish that who controls non-labor income within the couple determines Pareto weights and expenditure allocations. Traditional means-tested family benefits often trap women in abusive or unequal partnerships by conditioning transfers on joint household income, whereas universal individual transfers provide an unconditional "threat point" (outside option) that empowers exit capacity and bargaining power [@van-parijs-vanderborght-2017]. In disability economics, Puig-Segura et al. [@puig-segura-2021-discapacidad] document that Spanish households with disabled members require 20–45% higher baseline income to achieve equal living standards.

## 4. Spain context & data sources
- **Time-Use & Household Microdata:** INE *Encuesta de Empleo del Tiempo* (EET) paired with INE *Encuesta de Condiciones de Vida* (ECV), tracking intra-household sharing of unpaid domestic care, eldercare, and childcare across family types.
- **Health & Clinical Microdata:** Ministry of Health *Base de Datos Clínicos de Atención Primaria* (BDCAP) linked via personal health identification code (CIP), *Encuesta Nacional de Salud de España* (ENSE), and pharmaceutical consumption registers (DDD of anxiolytics and antidepressants).
- **Disability & Care Framework:** *Ley 39/2006 de Promoción de la Autonomía Personal y Atención a las personas en situación de dependencia* (SAAD), *Real Decreto 888/2022* on disability degree certification [@boe-rd-888-2022-discapacidad], and *Real Decreto Legislativo 1/2013* on rights of persons with disabilities.

## 5. Methods & identification
1. **Structural Collective Household Estimation:**
   - Specify a Chiappori collective household model [@chiappori-1992-collective] where household utility is $\mu(w_m, w_f, y_m, y_f, \mathbf{z}) U_m + [1 - \mu(\cdot)] U_f$.
   - Estimate the Pareto sharing rule $\mu$ as a function of individual non-labor income ($y_m, y_f$), where UBR shifts individual non-labor endowments symmetrically.
   - Simulate labor-supply and caregiving hours responses using parameters estimated on the Spanish EET and EPA rotating panels.
2. **Universal Disability Supplement Design:**
   - Calibrate the *Complemento Universal por Discapacidad* to the extra costs of disability estimated by Puig-Segura et al. [@puig-segura-2021-discapacidad], structuring an additive cash supplement (+25%, +50%, +100% of baseline UBR) linked to certified medical degrees under RD 888/2022 [@boe-rd-888-2022-discapacidad], keeping SAAD in-kind care services fully intact.
3. **Health Outcome Evaluation Protocol (`M10`):**
   - In the randomized pilot, measure biomarker and clinical endpoints (cortisol, self-reported mental health PHQ-9, sleep quality, and SNS billing records) to test the preventive health-spillover hypothesis.

## 6. Pilot implications
- **Municipal:** Feasible for evaluating local mental health and municipal social services utilization, but cannot address macro-level gender-wage dynamics or national pension entitlements; local pilots can assess community care cooperatives and respite care services.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común*, regional governments manage the SAAD dependency system and the regional health service (*Servicio de Salud*), providing a comprehensive institutional setting to evaluate health-card (BDCAP) primary-care cost offsets and dependency co-payments.
  - In *Régimen Foral* (Basque Country / Navarre), regional governments operate both unified health systems (Osakidetza, Osasunbidea) and autonomous foral tax systems, enabling direct evaluation of how individual tax credits interact with regional family allowances.
- **National:** Provides the definitive framework for eliminating gender pension gaps (`M07`), integrating individual UBR into national IRPF clearing (`M12`), and aligning SAAD statutory care entitlements nationwide without regional coverage disparities.

## 7. Risks, counterarguments & open issues
- **Counterargument (Secondary Earner Labor-Market Detachment):** Unconditional basic income might incentivize low-wage mothers to withdraw from formal employment, aggravating career penalties. *Mitigation:* Evidence from OpenResearch [@bartik-2024-openresearch] and Stockton [@west-2024-seed] indicates that female labor reductions are modest and primarily channeled into infant care and education; furthermore, pairing UBR with guaranteed universal 0–3 public childcare and equal, non-transferable parental leave prevents gendered withdrawal.
- **Counterargument (Disability Cost Substitution):** Fiscal authorities might attempt to replace SAAD disability benefits with UBR. *Mitigation:* Explicitly mandate by statute that all SAAD dependency benefits (Grades I, II, III) and the *Complemento Universal por Discapacidad* (+25% to +100%) remain fully additive on top of UBR (`M07`).

## 8. Deliverables & effort
- Collective Household Intra-Household Welfare Simulation and Gender AI Displacement Atlas.
- SNS Healthcare Cost-Offset Model and Clinical Health Evaluation Protocol for Chapters 3 and 7. (Effort: 4 person-weeks).
