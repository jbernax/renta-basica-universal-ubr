---
id: M03
title: Fiscal financing and tax-transfer integration
status: draft
locked: false
depends_on: [M01, M02, M07, M09, M16]
covers: [F03]
feeds_chapters: [4]
last_iteration: 2
---
# M03 · Fiscal financing and tax-transfer integration

## 1. Why this matters
Gross cost is the most frequent critique of UBR in Spain: paying €900/month to ~40 million adults and €360/month to ~8 million minors implies a gross outlay near €466 billion (~30% of Spanish GDP). However, economic feasibility depends on **status-quo budget neutrality**—ensuring that total post-reform tax revenues fund 100% of existing public services (health, education, general administration, totaling ~€125B/year in IRPF collections [@boe-irpf-2006]) PLUS gross UBR outlays minus genuinely abolished non-contributory cash transfers (`M07`), after integrating UBR into IRPF, folding regressive tax allowances, and reforming consumption and capital taxes [@hoynes-rothstein-2019; @saez-2002-optimal-transfers]. Crucially, under severe AI displacement (Scenario S2, $\Delta s_L = -7.0$ pp), the baseline tax system suffers an endogenous 11.55% of GDP revenue collapse (~€173B/year); M03 therefore cannot assume static baseline receipts, but must directly close the macro-micro fiscal loop using M01's counterfactual post-displacement earnings distributions.

## 2. Research questions
- **RQ-M03-01**: What progressive IRPF marginal rate schedule ($t \in [38\%, 52\%]$) and status-quo breakeven income percentile achieve full budget neutrality in Spain for Tiers A, B, and C once the IRPF *mínimo personal y familiar* (Arts. 56–61 LIRPF), the earned-income reduction (Art. 20 LIRPF), and joint-filing allowances (Art. 84 LIRPF) are integrated alongside the `M07` Dual-Pillar pension offset, when accounting for the S2 11.55% GDP baseline revenue contraction?
  - *Hypothesis:* Enforcing strict status-quo budget neutrality (preserving baseline €125B IRPF public financing) on counterfactual post-displacement earnings places the net-disposable-income breakeven point ($T_{\text{new}} - T_{\text{old}} = \text{UBR}$) at the 82nd–86th percentile of individual gross income (~€38,000–€44,000/year) under Tier B (€900/month), requiring a consolidated net financing requirement of 4.8–6.2% of GDP from base broadening and `M16` corporate automation surplus taxes to bridge the labor tax base contraction.
- **RQ-M03-02**: How do behavioural taxable income elasticities (ETI), corporate profit-sheltering under *Ley 27/2014* [@boe-sociedades-2014], and QUAIDS-estimated consumption shifts from IVA base broadening [@boe-iva-1992] affect revenue yields across AI scenarios S1–S3?
  - *Hypothesis:* Unifying the dual IRPF general and savings bases without corporate anti-deferral triggers corporate shelter leakage of 12–18% of high-income capital yields into holding companies, requiring an anti-deferral minimum tax under *Ley 27/2014* calibrated to Spanish ETI parameters [@almunia-lopez-rodriguez-2019-eti].

## 3. State of knowledge
Public finance theory establishes that a universal demogrant financed by a progressive income tax is economically equivalent to a Negative Income Tax of equal net schedule [@saez-2002-optimal-transfers; @ghatak-maniquet-2019]. Microsimulation studies using EUROMOD [@sutherland-figari-2013-euromod] show that gross-cost estimates overstate net fiscal burden by a factor of 4 to 6 [@hoynes-rothstein-2019]. However, naive models that equate $T_{\text{new}} = \text{UBR}$ with breakeven double-count pre-existing income tax revenue; true net cost must maintain pre-reform financing for general public services [@saez-2002-optimal-transfers]. Empirical estimates of the elasticity of taxable income in Spain confirm significant bunching at tax bracket kinks that must be incorporated into second-round behavioral yields [@almunia-lopez-rodriguez-2019-eti].

## 4. Spain context & data sources
- **Tax Law & Statutory Reductions:** *Ley 35/2006 del IRPF* [@boe-irpf-2006] (Art. 20 *reducción por rendimientos del trabajo*, Arts. 56–61 *mínimos personales y familiares*, Art. 84 *tributación conjunta*), *Ley 37/1992 del IVA* [@boe-iva-1992], and *Ley 27/2014 del Impuesto sobre Sociedades* [@boe-sociedades-2014].
- **Territorial Financing Framework:** *Ley 22/2009 de Financiación de las CCAA* [@boe-ley-financiacion-ccaa-2009] (50% ceded IRPF/IVA tranches), Basque *Concierto Económico* (*Ley 12/2002* [@boe-concierto-vasco-2002]), and Navarre *Convenio Económico* (*Ley 28/1990* [@boe-convenio-navarra-1990]).
- **Microdata:** IEF/AEAT *Panel de Hogares* (linked tax-census panel including non-filers), *Muestra de Declarantes de IRPF* (for top 5% Pareto fitting), and INE *Encuesta de Presupuestos Familiares* (EPF, for QUAIDS indirect tax simulation).

## 5. Methods & identification
1. **Consolidated Public Accounts Fiscal Bridge & Macro-Micro Loop:** Specify the general-government budget equation evaluated directly on counterfactual post-displacement earnings distributions from `M01`:
   $$\Delta \text{Balance} = \Delta \text{IRPF}_{\text{AEAT+CCAA}} + \Delta \text{IVA} + \text{Savings}_{\text{INSS}}(\text{M07}) + \text{AI/Capital}_{\text{M16}} - \text{Gross UBR} - \text{Baseline Tax Erosion}_{\text{S1-S3}}(\text{M01}) = 0$$
   Abolish LIRPF Arts. 20, 56–61, and 84, integrating UBR as an individual non-taxable transfer while taxing all other income from the first euro. In S2, the 11.55% of GDP baseline labor tax erosion is compensated by shifting the fiscal mix toward corporate automation surplus levies (`M16`), carbon/environmental taxes, and net wealth taxation.
2. **Behavioral ETI & Corporate Shelter Model:** Incorporate empirical Spanish ETI estimates ($\varepsilon_{\text{ETI}} \in [0.15, 0.45]$) from Almunia & Lopez-Rodriguez [@almunia-lopez-rodriguez-2019-eti] and simulate corporate holding-company shielding under *Ley 27/2014* with an anti-deferral minimum tax.
3. **QUAIDS Consumption Demand & Constant-Tax CPI:** Estimate a Quadratic Almost Ideal Demand System on EPF microdata to model price-elastic consumer demand under IVA base broadening [@boe-iva-1992], linking indexation to constant-tax CPI (IPC-IC) to prevent mechanical fiscal self-indexation (`M02`).

## 6. Pilot implications
- **Municipal Tier:** Municipal pilots cannot test income tax financing directly (limited to local fees/IBI), serving primarily to evaluate local liquidity and public service usage.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** In *Régimen Común*, test adjusting the 50% regional IRPF tariff under *Ley 22/2009* [@boe-ley-financiacion-ccaa-2009] paired with contractual top-up clawbacks; in *Régimen Foral* (Basque Country / Navarre), enact the full joint IRPF withholding schedule under autonomous tax laws (*Normas Forales del IRPF* / *Convenio Navarro* [@boe-concierto-vasco-2002; @boe-convenio-navarra-1990]).
- **National Tier:** Full AEAT monthly withholding clearing across all brackets and pension offset coordination with the Social Security budget.

## 7. Risks, counterarguments & open issues
- **Counterargument (Middle-Decile Effective Rate Hikes):** Middle-income earners (deciles 6–8) face higher marginal IRPF rates. *Mitigation:* Report transparent pre- and post-UBR net disposable income curves, showing that deciles 1–6 gain substantially and decile 7 remains net-neutral ($\pm 2\%$) while shifting financing to capital and AI rents (`M16`).

## 8. Deliverables & effort
- Consolidated Administraciones Públicas Gross-to-Net Fiscal Bridge Table (Tiers A/B/C $\times$ Scenarios S1/S2/S3).
- Statutory IRPF Reform Schedule & QUAIDS IVA Yield Model for Chapter 4. (Effort: 8 person-weeks).
