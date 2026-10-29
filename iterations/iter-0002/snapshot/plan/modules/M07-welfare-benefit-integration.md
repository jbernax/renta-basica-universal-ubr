---
id: M07
title: Interaction with existing Spanish welfare benefits
status: draft
locked: false
depends_on: [M02, M03, M06, M09, M14]
covers: [F08]
feeds_chapters: [3]
last_iteration: 1
---
# M07 · Interaction with existing Spanish welfare benefits

## 1. Why this matters
Spain operates a fragmented patchwork of contributory and non-contributory cash benefits: the state *Ingreso Mínimo Vital* (IMV [@boe-imv-2021]), 17 distinct *Rentas Mínimas Autonómicas* (such as the Basque *RGI* and Catalan *RGC* [@arcelus-bade-2015-rgi]), SEPE unemployment insurance and assistance (*subsidios por desempleo* [@boe-rdl-2-2024-desempleo]), non-contributory retirement and disability pensions (*PNC*), and contributory retirement pensions under the *Texto Refundido de la Ley General de la Seguridad Social* (TRLGSS [@boe-trlgss-2015]). A scientifically rigorous integration must resolve two fiscal and legal imperatives: (i) separating absorbed non-contributory schemes from retained contributory pensions to prevent catastrophic under-costing, and (ii) establishing an inviolable **No-Loser Guarantee** ensuring zero disposable-income loss for any pensioner, disabled person, or vulnerable household.

## 2. Research questions
- **RQ-M07-01**: How do total absorbed non-contributory transfers compare against retained contributory Social Security pensions, and what is the net fiscal cost of the statutory **Complemento de Garantía de Derechos Adquiridos** under Tiers A, B, and C across S1–S3?
  - *Hypothesis:* Under Tier B (€900/adult, €360/minor), 100% of IMV, CAPI, non-contributory pensions (PNC), and general SEPE *subsidios* are absorbed (~€14.5B/year savings). In contrast, contributory pensions above €900/month represent ~5.5–6.0% of GDP (~€90B/year) that remains funded by the contributory system under a **Dual-Pillar Architecture**, requiring an incremental tax-neutrality supplement (*Complemento de Neutralidad Fiscal*) of <0.5% of GDP (~€7.5B) to ensure zero net income loss after `M03` IRPF integration.
- **RQ-M07-02**: How can UBR absorb SEPE unemployment assistance without stripping older workers of the vital retirement pension contribution credits granted under Art. 280 TRLGSS [@boe-trlgss-2015; @boe-rdl-2-2024-desempleo] (*subsidio para mayores de 52 años*), and how does UBR alter Marginal Effective Tax Rates (METRs)?
  - *Hypothesis:* Preserving the Art. 280 TRLGSS state-paid retirement contribution credit (*cotización asimilada al alta por jubilación* at 125% of the minimum base) as an independent entitlement alongside the UBR cash transfer eliminates the participation poverty trap (lowering METRs from 80–100% under IMV to 38–46% under UBR) while fully protecting future contributory pension accrual for displaced workers aged 52+.

## 3. State of knowledge
Evaluations of Spanish minimum income schemes highlight severe horizontal inequities across Autonomous Communities, bureaucratic overlaps between INSS, SEPE, and regional social services, and poverty traps caused by benefit withdrawal upon formal job entry [@arcelus-bade-2015-rgi; @todeschini-bmincome-2020]. International trials (Finland [@kangas-2021-finland] and B-MINCOME [@todeschini-bmincome-2020]) show that removing clawbacks when taking temporary work increases formal stability. However, public finance theory warns that imposing a 100% offset on pre-existing contributory entitlements violates contributory legitimacy and triggers legal challenges [@hoynes-rothstein-2019].

## 4. Spain context & data sources
- **Benefit Registers & Budgets:** INSS statistical yearbook (IMV, PNC, and contributory pensions), SEPE unemployment benefit files (*Ley General de la Seguridad Social* [@boe-trlgss-2015] reformed by *Real Decreto-ley 2/2024* [@boe-rdl-2-2024-desempleo]), and Ministry of Social Rights annual reports on *Rentas Mínimas de Inserción*.
- **Microsimulation Spine:** EUROMOD-Spain linked to ECV and MCVL for longitudinal pension entitlement modeling.

## 5. Methods & identification
1. **Three-Tier Benefit Integration Taxonomy:**
   - *Tier 1 (Fully Absorbed Non-Contributory):* IMV, CAPI, PNC, child allowances, and general SEPE *subsidios* are extinguished and absorbed into UBR.
   - *Tier 2 (Dual-Pillar Contributory Integration):* Contributory pensions and contributory unemployment insurance use UBR as the non-taxable base floor (€600/€900/€1,200), with the Social Security system paying the remaining contributory entitlement $\max(0, B_{\text{contrib}} - \text{UBR})$ with a positive marginal contributory slope. A statutory *Complemento de Neutralidad Fiscal* is applied in EUROMOD to prevent post-IRPF disposable income losses. Older unemployed workers preserve Art. 280 TRLGSS retirement pension contribution credits.
   - *Tier 3 (Strictly Additive Non-Cash & Extra-Cost):* Severe disability and dependency allowances under *Ley 39/2006* [@boe-ley-dependencia-2006] and *grado III* invalidity supplements remain 100% additive on top of UBR (`M14`).
2. **Autonomous Community Windfall & Competence Clearing:** Because regional *Rentas Mínimas* are an exclusive competence under Art. 148.1.20 CE [@boe-ce-1978], a State UBR extinguishes regional payments indirectly via regional subsidiary rules (*carácter subsidiario*). Model a bilateral clearing formula through the CPFF / *Ley 22/2009* [@boe-ley-financiacion-ccaa-2009] and the Foral Treaties [@boe-concierto-vasco-2002; @boe-convenio-navarra-1990] to capture this €1.5–2.0B regional expenditure dividend.

## 6. Pilot implications
- **Municipal Tier:** Requires an explicit statutory safe-harbor provision in State and regional legislation so pilot cash transfers do not disqualify participants from pre-existing IMV, *Rentas Mínimas*, or SEPE *subsidios* during or after the pilot.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** In *Régimen Común*, regional governments can redirect their subsidiary minimum-income budgets (*RGC*, etc.) into pilot co-financing and social housing (`M05`); in *Régimen Foral* (Basque Country / Navarre), the *Diputaciones Forales* can integrate regional *RGI* seamlessly into the autonomous IRPF withholding system.
- **National Tier:** Complete automated clearing between INSS, SEPE, and AEAT (`M12`).

## 7. Risks, counterarguments & open issues
- **Counterargument (Contributory Alienation):** Trade unions may fear UBR undermines the contributory Bismarckian social contract. *Mitigation:* The Dual-Pillar formula preserves the positive contributory slope above UBR so every contributed euro continues to raise retirement income, while Art. 280 TRLGSS pension credits are legally preserved for displaced workers aged 52+.

## 8. Deliverables & effort
- Full Spanish Welfare Integration & Fiscal Savings Schedule across 17 Autonomous Communities.
- Dual-Pillar Contributory Pension & No-Loser Guarantee Algorithm for Chapter 3. (Effort: 5 person-weeks).
