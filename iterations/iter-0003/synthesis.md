# Synthesis of Review Findings — Iteration 0003 (`iter-0003`)

## Panel Overview & Metareview
Iteration 0003 convened the full panel of 9 specialist reviewer personas:
1. `labor-economist`
2. `public-finance`
3. `macroeconomist`
4. `spanish-eu-law`
5. `social-policy`
6. `evaluation-methodologist`
7. `housing-economist`
8. `political-economist`
9. `red-team`

The panel returned 40 concrete issues across economic, legal, econometric, spatial, and administrative dimensions. All 9 reviews passed schema and cross-reference validation (`.venv/bin/python -m ubr reviews check iter-0003` exited 0 with 0 errors, 0 warnings).

Below is the structured synthesis grouping these 40 findings into 9 unified, actionable, and non-conflicting proposals (`SYN-03-01` through `SYN-03-09`) mapped to exact files, sections, and modules.

---

## Synthesis Proposals

### `SYN-03-01` · Macro-Micro Accounting & Fiscal Realism: Disentangling Baseline Revenue Losses from GDP Ratios
- **Contributing Issues:** `RT-03-03` (critical), `MA-03-01` (critical), `PF-03-04` (major).
- **Primary Modules:** `M01`, `M03`, `METHODS`.
- **Core Diagnosis:** A fundamental accounting error was identified in `M01`, `M03`, and `METHODS`: an 11.55% *relative* drop in labor tax receipts under S2 (a 7 pp drop in labor share applied to Spain's ~39% average tax wedge) was erroneously transcribed as an "11.55% of GDP revenue collapse (~€173B/year)". In reality, on Spain's €1,500B GDP, a 7 pp drop in labor share represents a €105B contraction in gross wages; with a 39% tax wedge (IRPF + Social Security), the baseline revenue erosion is ~2.7% of GDP (~€40.5B/year). This ~2.7% loss harmonizes perfectly with `M16`'s ~1.9% of GDP employer payroll loss and validates `M03`'s 4.8–6.2% of GDP net financing requirement under decile 84 breakeven.
- **Actionable Edits:**
  1. In `M01` (RQ-M01-02), `M03` (RQ-M03-01), and `METHODS` (Section 1 & 2), correct the arithmetic: distinguish between relative labor-base compression and percentage points of GDP. Under S1: $\Delta \text{Rev}_{\text{base}} \approx -0.98\%$ of GDP; under S2: $\Delta \text{Rev}_{\text{base}} \approx -2.73\%$ of GDP; under S3: $\Delta \text{Rev}_{\text{base}} \approx -5.85\%$ of GDP.
  2. In `M03`, provide the fully balanced consolidated *Administraciones Públicas* accounting bridge explicitly itemizing baseline tax erosion (-2.73% GDP), gross Tier B outlays (-30.0% GDP), existing non-contributory welfare savings (+0.95% GDP), contributory pension offsets (+5.8% GDP net of tax shield), net corporate surplus and AI compute excises (+2.8% GDP), IRPF restructuring (+22.5% GDP), and consumption/wealth yields (+0.7% GDP).
  3. In `METHODS` (Section 3), expand the dynamic macro-micro closure equation to include endogenous sovereign debt service feedback ($\Delta (r_t - g_t) D_{t-1}$) under EU Regulation 2024/1263 Net Primary Expenditure rules.

---

### `SYN-03-02` · Foreign AI Compute Tax Enforcement & Domestic B2B Reverse-Charge Architecture
- **Contributing Issues:** `RT-03-01` (critical / `JD-02-01`), `PF-03-02` (critical).
- **Primary Modules:** `M16`, `M03`.
- **Core Diagnosis:** Origin-based Net Operating Surplus taxes and Spain's current Digital Services Tax (*Ley 4/2020*, yielding <€300M/year and explicitly exempting B2B cloud/enterprise software) fail to capture foreign AI foundation model providers (OpenAI, Anthropic, Microsoft, Google, AWS) who lack a physical Permanent Establishment (PE) under OECD Double Taxation Treaties (CDIs Arts. 5, 7, and 12). Spanish enterprises deduct these foreign compute subscriptions, actively eroding domestic taxable surplus. Furthermore, frontloading Sovereign Fund equity purchases (1.0–1.2% GDP) during peak S2 displacement worsens the primary fiscal deficit.
- **Actionable Edits:**
  1. In `M16` (Section 5) and `M03` (Section 5), formulate a domestic B2B tax enforcement architecture:
     - Enact a Destination-Based AI Compute and Inference Withholding / Reverse-Charge Mechanism (*Impuesto Especial sobre Capacidad y Computación de IA*, *IECA*) under *Ley 58/2003* (LGT) and *RDLeg 5/2004* (TRIRNR).
     - Under *Ley 27/2014* (LIS, Art. 15), condition corporate income tax deductibility of foreign compute and API expenses on domestic withholding certificate compliance.
     - Codify a statutory "Virtual Permanent Establishment / Significant Digital Presence" threshold aligned with EU COM(2018) 147 final and OECD Pillar One Amount A / Pillar Two Directive (EU) 2022/2523.
  2. In `M16`, replace rigid annual Sovereign Fund accumulation targets with a counter-cyclical Windfall Accumulation Rule (funding activated only when corporate gross operating surplus exceeds 120% of sectoral historical norms).

---

### `SYN-03-03` · Spatial Commuting Mobility Spillover Closure & Two-Stage Saturation Econometrics
- **Contributing Issues:** `RT-03-02` (critical / `JD-02-02`), `EM-03-02` (critical).
- **Primary Modules:** `M10`, `METHODS`.
- **Core Diagnosis:** Static 2–5 km buffer zones in integrated metropolitan and peri-urban areas fail to satisfy SUTVA because daily commuting and consumer shopping routinely span 15–30 km. Furthermore, `M10`'s MDE formula applied a standard one-stage cluster RCT variance formula, underestimating standard errors in two-stage saturation designs (Baird et al. 2018), while thin rural rental markets (~10–15 lease contracts/cluster over 3 years) lack statistical power to identify rental pass-through.
- **Actionable Edits:**
  1. In `M10` (Section 5) and `METHODS` (Section 4), incorporate an empirical mobility weight matrix ($W_{\text{mobility}}$) based on MITMA/INE's *Estudio de la Movilidad con Telefonía Móvil*, specifying a continuous spatial spillover exposure estimator:
     $$Y_{ic} = \alpha + \beta_1 T_{ic} + \beta_2 \text{Cash}_c + \gamma \sum_j W_{cj} \cdot \text{Cash}_j + X'_{ic} \delta + \varepsilon_{ic}$$
  2. Redefine metropolitan cluster boundaries along Functional Urban Areas (FUAs / *Áreas Urbanas Funcionales* INE) with internal commuting self-containment $\ge 80\%$.
  3. Replace the one-stage MDE formula with Baird et al. (2018) two-stage saturation variance equations, stratify clusters by private rental density (>35%), mandate 100% census linkage of regional tenancy deposit registries (INCASÒL, IVIMA, AVRA), and pre-specify Synthetic Difference-in-Differences (SDID, Arkhangelsky et al. 2021).

---

### `SYN-03-04` · Non-Convex Kink Resolution & Missing-Mass Econometric Correction
- **Contributing Issues:** `EM-03-01` (critical), `EM-03-04` (major).
- **Primary Modules:** `M10`, `M08`, `M15`, `METHODS`.
- **Core Diagnosis:** Bounding UBR clawback at zero net grant causes marginal clawback rates to drop from 38%–50% to 0%, creating a *concave (non-convex) kink* in the budget set ($\Delta \tau < 0$). Standard bunching theory (Saez 2010; Kleven 2016) proves that agents never bunch at concave kinks; concave kinks generate missing mass (a hole). Furthermore, `M15`'s structural transportability equation inverted Frisch elasticity by pairing it with marginal utility of wealth rather than transitory wage variation, and ignored labor demand rationing.
- **Actionable Edits:**
  1. In `M10` (RQ-M10-02, Section 5) and `M08` (Section 5), introduce an initial labor income disregard ($Y_{\text{disregard}} = \text{€}3,000\text{--}\text{€}5,000/\text{year}$, aligned with RD 789/2022 and RDL 2/2024 CAE) before clawback begins. This creates a true convex kink with excess mass for Saez (2010) and Chetty et al. (2011) bunching estimators, while formalizing a missing-mass estimator at the upper phase-out ceiling $Y^*$.
  2. In `M15` (Section 5) and `METHODS` (Section 4), correct the structural life-cycle hours decomposition:
     $$\Delta \ln h_{it} = \varepsilon^{\text{Frisch}} \Delta \ln w_{it}^{\text{transitory}} + \varepsilon^c \Delta \ln w_i^{\text{permanent}} + \eta \Delta Y_{it}^{\text{unearned}} + \zeta_{\text{rationing}} \cdot P_{\text{disp}, \text{CNO-11}} + e_{it}$$
     incorporating Bargain, Orsini, & Peichl (2014) labor demand rationing corrections based on task displacement vectors from `M01`.

---

### `SYN-03-05` · Fiscal Federalism Reconciliation: Common Regime VFI, Cession Adjustments, and Foral Clearing
- **Contributing Issues:** `LW-03-01` (critical), `PF-03-01` (critical), `PE-03-03` (major), `RT-03-05` (major).
- **Primary Modules:** `M06`, `M03`, `M11`.
- **Core Diagnosis:** `M06` committed a category error by applying the Foral concept of "carga no asumida" to the Common Regime under *Ley 22/2009*. Ceding 50% of IRPF/IVA collections under *Ley 22/2009* while the Central State funds 100% of UBR creates an unearned regional windfall and a central structural deficit. In addition, Basque and Navarrese *Haciendas Forales* hold exclusive direct-tax jurisdiction under the *Concierto Económico* (*Ley 12/2002*) and *Convenio Económico* (*Ley 28/1990*), meaning State AEAT cannot administer IRPF credits in Foral territories.
- **Actionable Edits:**
  1. In `M06` (Section 5.1) and `M03` (Section 5.1), strictly bifurcate territorial financing:
     - **Foral Regimes:** Classify UBR as a non-assumed power (*carga no asumida*) strictly within the *Comisión Mixta del Concierto* and *Comisión Coordinadora del Convenio*. Specify the bilateral clearing algorithm adjusting the *Cupo* base ($I_{\text{Cupo}} = 6.24\%$) and *Aportación* ($I_{\text{Aportación}} = 1.6\%$) to hold Basque and Navarrese budgets fiscally neutral without net outflows.
     - **Common Regime (15 CCAA):** Enact statutory amendments to *LOFCA* (Art. 13) and *Ley 22/2009* establishing a *Fondo de Compensación UBR* or negative *Fondo de Suficiencia Global* inside the *Fondo de Garantía de Servicios Públicos Fundamentales* (FGSPF) within the *Consejo de Política Fiscal y Financiera* (CPFF), recapturing regional minimum income savings (~€1.5B–€2.0B) for social housing and SAAD dependency care.
  2. Codify the bilateral tax harmonization mechanism under Art. 6 *Ley 12/2002* and Art. 7 *Ley 28/1990* via model *Normas Forales* and *Leyes Forales* enacted by Foral Parliaments (Juntas Generales and Parlamento de Navarra).

---

### `SYN-03-06` · Social Security Pension Accrual Continuity, Disability Tax-Shield, and Debt Immunity
- **Contributing Issues:** `LW-03-02` (critical), `SP-03-01` (critical), `SP-03-02` (critical), `LW-03-03` (major).
- **Primary Modules:** `M07`, `M12`.
- **Core Diagnosis:** Under Art. 273.2 TRLGSS, SEPE pays the employer's Social Security retirement contribution during contributory unemployment. Offsetting SEPE benefits down to UBR terminates this statutory contribution for displaced workers under 52, leaving severe contribution gaps (*lagunas de cotización*, Art. 209 TRLGSS) that permanently depress future retirement pensions by 20–40%. Furthermore, contributory permanent disability pensions (*Incapacidad Permanente Absoluta*, Art. 7.f LIRPF) risk losing their tax exemption. In `M12`, absolute inembargabilidad violates child support (Art. 608 LEC), while failing to shield recipients from internal Social Security administrative offsets (Art. 53 TRLGSS) for past IMV overpayments (*cobros indebidos*). Also, `M12` misattributed automated acts to *Ley 39/2015* Art. 41 instead of *Ley 40/2015* Art. 41 (LRJSP).
- **Actionable Edits:**
  1. In `M07` (Section 5.1), codify an explicit statutory Contribution Continuity Guarantee (*Garantía de Mantenimiento de Bases de Cotización por Desempleo*) under Art. 273 TRLGSS, mandating SEPE to maintain retirement contributions throughout unemployment regardless of UBR cash offset, and establish a universal *Crédito Cotizatorio Básico por Transición Tecnológica* maintaining continuous pension accrual at 100% of SMI base for displaced workers.
  2. In `M07` (Tier 2 & 3), guarantee that contributory pensions for *Incapacidad Permanente Absoluta* and *Gran Invalidez* retain their complete statutory tax exemption under Art. 7.f LIRPF, or receive an automatic refundable *Complemento por Discapacidad Contributiva*.
  3. In `M12` (Section 2 & 5.2), amend the inembargabilidad protocol to explicitly incorporate the Art. 608 LEC child-support exception, enact statutory immunity from internal TGSS/AEAT administrative offsets (Art. 53 TRLGSS / Arts. 71–73 LGT) for retroactive non-fraudulent IMV debts, and correct statutory citations to Art. 41 *Ley 40/2015* (LRJSP) and Art. 82 *Ley 39/2015* (LPAC).

---

### `SYN-03-07` · Housing Competence Asymmetries, Rental Nowcasting, and Spatial Immobility Frictions
- **Contributing Issues:** `HE-03-01` (critical), `HE-03-02` (major), `HE-03-03` (major), `HE-03-04` (major).
- **Primary Modules:** `M05`, `M09`, `M13`, `M17`.
- **Core Diagnosis:** Conditioning rent caps and tax deductions on regional ZMRT declarations under *Ley 12/2023* collides with regional boycotts (Madrid, Andalusia, Balearic Islands, Valencia) under exclusive regional housing competence (Art. 148.1.3 CE, STC 79/2024). SERPAVI official rental indices have 12–18 month reporting lags. Poverty metrics omit After-Housing-Cost (AHC) distributions and corporate landlord (SOCIMI / non-resident IRNR) leakage. Rural spatial sorting ignores thin rural rental stock (<10%) and dual-earner co-location frictions (Costa & Kahn 2000).
- **Actionable Edits:**
  1. In `M05` (Section 5.1) and `M17` (Section 5), decouple federal tax conditionality and circuit-breakers from regional ZMRT declarations: establish an Objective Federal Fiscal Benchmark under State tax powers (Art. 149.1.14 CE) conditioning LIRPF Art. 23.2 reductions on MIVAU SERPAVI reference price indices wherever rent-to-income exceeds 30%.
  2. In `M17` and `M05`, specify a High-Frequency Rental Nowcasting Spine (monthly tenancy deposits, scraped portal APIs with <= 30-day latency), and establish a *Fondo de Estabilización Residencial* (FER) under ICO liquidity with statutory exemption from LOEPSF expenditure limits for emergency municipal preemption (*tanteo y retracto*).
  3. In `M09`, formally mandate dual reporting of Before-Housing-Cost (BHC) and After-Housing-Cost (AHC) Foster-Greer-Thorbecke poverty ($P_0, P_1, P_2$) and AHC Gini in EUROMOD-Spain, disaggregating landlord ownership into physical persons, SOCIMIs (0% CIT under Ley 11/2009), and non-resident owners (TRIRNR).
  4. In `M13`, model joint household utility with secondary-earner career disruption penalties (Costa & Kahn 2000) and pair UBR with a *Programa de Movilización de Vivienda Rural Vacía* (ICO zero-interest loans).

---

### `SYN-03-08` · Constitutional Tax Legality, Bicameral Override, and Tripartite Employer Dialogue
- **Contributing Issues:** `PE-03-01` (critical), `PE-03-02` (critical), `PE-03-04` (major), `LW-03-04` (critical).
- **Primary Modules:** `M17`, `M11`, `M13`.
- **Core Diagnosis:** `M17`'s proposal to delegate tax surcharges via *Real Decreto-ley* under Art. 86 CE upon AIReF certification directly violates the constitutional Principle of Tax Legality (Arts. 31.1 & 31.3 CE, STC 73/2017, STC 78/2020). `M11` lacks an organic override strategy for the Senate's absolute veto over expenditure ceilings under LOEPSF Art. 15, and ignores employer associations (CEOE/CEPYME). In `M13`, abolishing the IRPF personal allowance leaves resident taxpayers during waiting periods taxed from euro 1, violating the constitutional subsistence minimum (Art. 31.1 CE, STC 214/1994). Also, marginal EU workers under Art. 45 TFEU require a calibrated definition of genuine employment (Case 66/85 *Lawrie-Blum*, Case C-14/09 *Genc*).
- **Actionable Edits:**
  1. In `M17` (Section 5), excise unconstitutional decree-law tax surcharge delegation; replace with a statutory automatic stabilizer enacted in advance by Ordinary/Organic Law with rigid mathematical rate formulas, or expedited parliamentary urgency (*tramitación de urgencia*, Art. 93 Reglamento del Congreso).
  2. In `M11` (Section 5), detail the organic legislative pathway in Congress to amend LOEPSF Art. 15.6 by absolute majority to restore congressional override over the Senate veto; embed CEOE/CEPYME in social dialogue.
  3. In `M13` (Section 5), codify a Default Non-Refundable Mínimo Personal y Familiar in *Ley 35/2006* for taxpayers in UBR waiting periods; define "effective and genuine employment" with objective Social Security thresholds for EU workers under Art. 45 TFEU / Regulation 492/2011; establish an unconditional child subsistence safe-harbor under Art. 39 CE.

---

### `SYN-03-09` · Labor Market Institutions, Assistential Reforms (RDL 2/2024), and Healthcare Register Bifurcation
- **Contributing Issues:** `LE-03-01` (critical), `LE-03-02` (critical), `LE-03-03` (major), `LE-03-04` (major), `RT-03-04` (major), `RT-03-06` (minor), `EM-03-03` (major), `SP-03-03` (major), `SP-03-05` (major).
- **Primary Modules:** `M08`, `M01`, `M14`, `M10`, `M02`.
- **Core Diagnosis:** `M08` lacked the *Real Decreto-ley 2/2024* assistential reform and *Complemento de Apoyo al Empleo* (CAE); `M01` omitted statutory SMI gross cost floors (€1,740/mo per RD 145/2024) and *descuelgues salariales* (Art. 82.3 ET); `M14` omitted SAAD professional care substitution risks; `M10`/`M14` relied on a centralized SNS healthcare database that does not exist (devolved to 17 CCAA under Ley 14/1986); and `M02` single-parent bonus required invasive cohabitation policing.
- **Actionable Edits:**
  1. In `M08` and EUROMOD, integrate RDL 2/2024 and CAE phase-out; in `M01`, formalize the statutory SMI gross labor cost floor ($W_{\text{floor}} = \text{SMI} \times (1 + \tau_{\text{SS}}^{\text{emp}})$) and collective bargaining opt-outs (Art. 82.3 ET).
  2. In `M14` and `M07`, establish a *Garantía de No-Sustitución de Servicios Profesionales de Cuidados* under *Ley 39/2006*.
  3. In `M10` and `M14`, bifurcate healthcare data into Tier 1 centralized INSS *Incapacidad Temporal* (IT) sickness leave records and Tier 2 bilateral agreements with pilot regional health services (CatSalut, SERMAS, Osakidetza) under *Ley 16/2003*, with INE ECV/ENSE as fallback.
  4. In `M02`, replace status-contingent single-parent bonus with parity-modulated child allowances ($\alpha_{\text{child1}} = 0.50$, $\alpha_{\text{child}\ge 2} = 0.35\text{--}0.40$).
