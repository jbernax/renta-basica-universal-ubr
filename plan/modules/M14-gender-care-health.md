---
id: M14
title: Gender, unpaid care, disability, and health outcomes
status: locked
locked: true
depends_on: [M01, M02, M07, M08, M09, M10]
covers: [F15]
feeds_chapters: [3, 7]
last_iteration: 3
---
# M14 · Gender, unpaid care, disability, and health outcomes

## 1. Why this matters
Spanish women perform over two-thirds of unpaid domestic and care work, face persistent gender wage and pension gaps, and are disproportionately concentrated in administrative, clerical, customer-facing, and paralegal occupations that face the highest gross exposure to generative AI displacement under Scenarios S1–S3 (`M01`). Furthermore, traditional means-tested safety nets like the IMV [@boe-imv-2021] assess and transfer benefits to a single household representative (*titular*), reinforcing intra-household economic dependency and trapping secondary earners in poverty. Persons with disabilities face substantial non-discretionary economic extra costs (€3,500–€10,000/year [@puig-segura-2021-discapacidad]) that cannot be met by baseline cash transfers alone. By establishing strictly individual, unconditional cash entitlements (`D-001`) paired with dedicated disability supplements, UBR fundamentally alters intra-household bargaining power, care valuation, disability equity, and population mental health [@miller-2024-openresearch-health; @west-2024-seed; @cherchye-2012-collective].

## 2. Research questions
- **RQ-M14-01**: How does an individual, unconditional UBR (`M02`) reshape intra-household bargaining power, resource allocation, and time use between paid work and unpaid care in Spain when modeled within a discrete-choice collective household framework [@chiappori-1992-collective; @cherchye-2012-collective]?
  - *Hypothesis:* In an estimated discrete-choice collective household model [@cherchye-2012-collective] on INE *Encuesta de Empleo del Tiempo* (EET) and ECV microdata that explicitly accommodates female non-participation corner solutions, individual UBR transfers raise female sharing rules by 8–15 percentage points in low-to-middle income couples, expanding personal non-housing consumption and reducing secondary-earner financial dependence without lowering overall female labor-force attachment.
- **RQ-M14-02**: How will gender-asymmetric AI labor displacement across S1–S3 interact with UBR, the tiered **Complemento Universal por Discapacidad** under *Real Decreto 888/2022* [@boe-rd-888-2022-discapacidad], and the *Ley 39/2006* (SAAD [@costa-font-2022-saad]) system to prevent care re-familialization?
  - *Hypothesis:* Without statutory safeguards, cash transfers risk inducing informalization of eldercare; establishing an explicit statutory **Garantía de No-Sustitución de Servicios Profesionales** under *Ley 39/2006* [@costa-font-2022-saad] ensures that UBR is strictly additive to professional in-kind care services. For individuals with disabilities, adding a statutory disability supplement (+25% for 33–64%, +50% for 65–74%, +100% for $\ge 75\%$ per RD 888/2022) fully covers empirical extra living costs [@puig-segura-2021-discapacidad] without distorting labor participation.
- **RQ-M14-03**: What are the causal impacts of unconditional monthly income security on clinical mental health (anxiety, depression, sleep disorders) and healthcare utilization within the Spanish National Health System (*Sistema Nacional de Salud*, SNS [@ley-16-2003-sns])?
  - *Hypothesis:* Consistent with Finland [@kangas-2021-finland], Barcelona B-MINCOME [@todeschini-bmincome-2020], Stockton [@west-2024-seed], and the 34 Ministry of Inclusion / CEMFI / J-PAL RCT evaluations [@inclusion-cemfi-jpal-2024], UBR significantly reduces self-reported psychological distress (PHQ-9/GHQ-12) by 0.22–0.35 standard deviations and improves sleep quality. Following OpenResearch findings [@miller-2024-openresearch-health], physical clinical biomarker impacts and aggregate healthcare expenditure reductions are treated as exploratory secondary hypotheses rather than guaranteed fiscal savings.

## 3. State of knowledge
A substantial body of international evidence demonstrates that mental health gains, stress alleviation, and subjective wellbeing improvements are the most immediate and statistically significant outcomes of unconditional cash transfers [@kangas-2021-finland; @todeschini-bmincome-2020; @west-2024-seed; @inclusion-cemfi-jpal-2024]. However, rigorous multi-year clinical trials (notably OpenResearch, Miller et al. 2024 [@miller-2024-openresearch-health]) show that unconditional cash does not yield statistically significant reductions in total healthcare expenditures or hospitalizations in the medium term, cautioning against premature fiscal cost-offset assumptions. In gender economics, collective household models [@chiappori-1992-collective; @cherchye-2012-collective] establish that individual control over non-labor income determines intra-household Pareto weights. In care economics, Costa-Font et al. [@costa-font-2022-saad] demonstrate that cash-for-care transfers under Spain's SAAD (*Ley 39/2006*) often substitute for formal professional care, locking informal female caregivers into home care unless statutory non-substitution walls are erected. In disability economics, Puig-Segura et al. [@puig-segura-2021-discapacidad] document that Spanish households with disabled members require 20–45% higher baseline income to achieve equal living standards.

## 4. Spain context & data sources
- **Time-Use & Household Microdata:** INE *Encuesta de Empleo del Tiempo* (EET) paired with INE *Encuesta de Condiciones de Vida* (ECV), tracking intra-household sharing of unpaid domestic care, eldercare, and childcare across family types.
- **Experimental & Clinical Microdata:** Microdata from the 34 Ministry of Inclusion / CEMFI / J-PAL social inclusion RCTs [@inclusion-cemfi-jpal-2024], Ministry of Health *Base de Datos Clínicos de Atención Primaria* (BDCAP) linked via CIP, and pharmaceutical consumption registers (DDD of anxiolytics and antidepressants).
- **Disability & Care Framework:** *Ley 39/2006 de Promoción de la Autonomía Personal y Atención a las personas en situación de dependencia* (SAAD [@costa-font-2022-saad]), *Real Decreto 888/2022* on disability degree certification [@boe-rd-888-2022-discapacidad], and *Ley 16/2003 de cohesión y calidad del Sistema Nacional de Salud* [@ley-16-2003-sns].

## 5. Methods & identification
1. **Discrete-Choice Collective Household Structural Estimation:**
   - Specify a discrete-choice collective household model following Cherchye et al. [@cherchye-2012-collective] that explicitly handles female non-participation corner solutions and joint labor-supply decisions:
     $$\max_{h_m, h_f, c_m, c_f} \mu(\mathbf{w}, \mathbf{y}, \mathbf{z}) U_m(c_m, 1 - h_m) + [1 - \mu(\mathbf{w}, \mathbf{y}, \mathbf{z})] U_f(c_f, 1 - h_f)$$
     subject to $c_m + c_f \le w_m h_m + w_f h_f + 2 \cdot \text{UBR} - T(w_m h_m, w_f h_f)$, with $h_f \in \{0, 20, 40\}$.
   - Estimate the Pareto sharing rule $\mu$ using Spanish EET and ECV data, quantifying how unconditional individual entitlement shifts intra-household bargaining weights.
2. **SAAD Professional Care Non-Substitution Protocol:**
   - Formulate statutory language for *Ley 39/2006* [@costa-font-2022-saad] guaranteeing that UBR receipt cannot be offset against SAAD professional services (residential, day-care, and home telecare hours), prohibiting regional administrations from demoting professional service allocations to informal cash allowances (*PECE*).
3. **Universal Disability Supplement Design:**
   - Calibrate the *Complemento Universal por Discapacidad* to the extra costs estimated by Puig-Segura et al. [@puig-segura-2021-discapacidad], structuring an additive cash supplement (+25%, +50%, +100% of baseline UBR) linked to certified medical degrees under RD 888/2022 [@boe-rd-888-2022-discapacidad].
4. **Bifurcated Health Evaluation Protocol (`M10`):**
   - In the randomized pilot, evaluate mental health and primary care utilization through the bifurcated architecture: Tier 1 centralized INSS *Incapacidad Temporal* (IT) administrative registers; Tier 2 bilateral research agreements with pilot regional health services under *Ley 16/2003* [@ley-16-2003-sns] (CatSalut, SERMAS, Osakidetza) for primary care consultations and psychotropic prescription invoicing.

## 6. Pilot implications
- **Municipal:** Feasible for evaluating local mental health and municipal social services utilization, but cannot address macro-level gender-wage dynamics or national pension entitlements; local pilots can assess community care cooperatives and respite care services.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común*, regional governments manage the SAAD dependency system and the regional health service (*Servicio de Salud*), providing a comprehensive institutional setting to evaluate health-card (BDCAP) primary-care utilization and dependency co-payments.
  - In *Régimen Foral* (Basque Country / Navarre), regional governments operate both unified health systems (Osakidetza, Osasunbidea) and autonomous foral tax systems, enabling direct evaluation of how individual tax credits interact with regional family allowances.
- **National:** Provides the definitive framework for eliminating gender pension gaps (`M07`), integrating individual UBR into national IRPF clearing (`M12`), and aligning SAAD statutory care entitlements nationwide without regional coverage disparities.

## 7. Risks, counterarguments & open issues
- **Counterargument (Secondary Earner Labor-Market Detachment):** Unconditional basic income might incentivize low-wage mothers to withdraw from formal employment, aggravating career penalties. *Mitigation:* Evidence from OpenResearch [@bartik-2024-openresearch] and Stockton [@west-2024-seed] indicates that female labor reductions are modest and primarily channeled into infant care and education; furthermore, pairing UBR with guaranteed universal 0–3 public childcare and equal, non-transferable parental leave prevents gendered withdrawal.
- **Counterargument (Disability Cost Substitution):** Fiscal authorities might attempt to replace SAAD disability benefits with UBR. *Mitigation:* Explicitly mandate by statute that all SAAD dependency benefits (Grades I, II, III) and the *Complemento Universal por Discapacidad* (+25% to +100%) remain fully additive on top of UBR (`M07`).

## 8. Deliverables & effort
- Collective Household Discrete-Choice Intra-Household Welfare Simulation and Gender AI Displacement Atlas.
- SAAD Professional Care Non-Substitution Statutory Draft and SNS Bifurcated Health Evaluation Protocol for Chapters 3 and 7. (Effort: 4 person-weeks).
