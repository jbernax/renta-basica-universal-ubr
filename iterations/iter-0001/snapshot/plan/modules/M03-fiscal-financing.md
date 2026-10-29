---
id: M03
title: Fiscal financing and tax-transfer integration
status: draft
locked: false
depends_on: [M01, M02, M07, M09, M16]
covers: [F03]
feeds_chapters: [4]
last_iteration: 0
---
# M03 · Fiscal financing and tax-transfer integration

## 1. Why this matters
Gross cost is the most frequent critique of UBR in Spain: paying €900/month to ~40 million adults and €360/month to ~8 million minors implies a gross outlay near €466 billion (~30% of Spanish GDP). However, economic feasibility depends on **net redistributive transfer**—the amount moved from net contributors to net recipients after integrating UBR with IRPF [@boe-irpf-2006], folding redundant cash benefits (`M07`), and reforming consumption and capital taxes [@hoynes-rothstein-2019; @saez-2002-optimal-transfers].

## 2. Research questions
- **RQ-M03-01**: What is the static and behavioral net fiscal cost of UBR Tiers A, B, and C in Spain once the IRPF *mínimo personal y familiar* and replaced cash transfers are integrated into a unified progressive tax schedule?
  - *Hypothesis:* Integrating Tier B (€900/month) into IRPF reduces the net financing requirement from ~30% of GDP (gross) to 4.5–5.8% of GDP (net), with the zero-net-transfer breakeven occurring between the 65th and 72nd percentile of individual gross income.
- **RQ-M03-02**: As AI displacement erodes labor income under scenarios S2 and S3 (`M01`), what combination of IRPF dual-base unification (taxing *renta del ahorro* at progressive *renta general* rates), IVA base broadening, and `M16` AI/capital levies closes the fiscal gap with minimal efficiency loss?
  - *Hypothesis:* Unifying IRPF savings and general tax bases plus reclassifying super-reduced/reduced IVA exemptions (compensated ex ante by UBR for lower deciles) finances Tier A/B under S1–S2, while S3 requires at least 3.0% of GDP from `M16` capital/AI-rent taxes.

## 3. State of knowledge
Public finance theory establishes that a universal demogrant financed by a linear or progressive income tax is fiscally equivalent to a Negative Income Tax of equal net transfer schedule [@saez-2002-optimal-transfers; @ghatak-maniquet-2019]. Microsimulation studies using EUROMOD [@sutherland-figari-2013-euromod] show that gross-cost estimates overstate fiscal burden by a factor of 4 to 6 because they count self-financed tax clawbacks on middle and upper deciles as new net expenditure [@hoynes-rothstein-2019; @van-parijs-vanderborght-2017].

## 4. Spain context & data sources
- **Tax Law & Bases:** *Ley 35/2006 del IRPF* [@boe-irpf-2006] (general vs. savings base, *mínimos personales y familiares*, autonomous vs. state brackets) and *LOFCA* [@boe-lofca-1980].
- **Microdata:** IEF/AEAT *Muestra de Declarantes de IRPF* (>2.5 million tax records), *Panel de Hogares* (linked AEAT + INE + Catastro), and INE *Encuesta de Presupuestos Familiares* (EPF, for IVA incidence by decile).

## 5. Methods & identification
1. **Joint IRPF-UBR Microsimulation:** In EUROMOD-Spain + IEF IRPF Muestra, abolish current IRPF personal/family allowances, make UBR non-taxable but tax all other earned and capital income from the first euro at calibrated marginal schedules ($t \in [38\%, 52\%]$).
2. **Consumption Tax Incidence (EPF-EUROMOD Link):** Match EPF expenditure shares to ECV households to simulate eliminating regressive IVA tax expenditures whose distributional purpose is superseded by UBR.
3. **Dynamic S1–S3 Stress Test:** Apply `M01` wage-bill compression vectors to project IRPF and Social Security revenue loss and solve for revenue-neutral tax rates.

## 6. Pilot implications
- **Municipal:** Cannot test tax financing (municipalities only control IBI/local fees).
- **Regional:** A *régimen foral* pilot (Basque Country / Navarre) can legally enact the exact IRPF withholding schedule to test net-taxpayer behavioral responses; a *régimen común* pilot can only adjust the 50% regional IRPF tariff or simulate clawbacks contractually.
- **National:** Full AEAT monthly withholding (*retenciones*) + UBR clearing.

## 7. Risks, counterarguments & open issues
- **Counterargument (High Marginal Tax Rates & Tax Evasion):** Marginal IRPF rates near 45–50% from the first euro of earned income could depress formal labor supply or increase underground activity (*economía sumergida*). *Mitigation:* Estimate taxable income elasticities (ETI) on Spanish IRPF bunching points and shift financing toward consumption (IVA) and AI/capital rents (`M16`).

## 8. Deliverables & effort
- Full Gross-to-Net Fiscal Bridge Table (Tiers A/B/C $\times$ Scenarios S1/S2/S3).
- Statutory IRPF Tariff Reform Schedule & Revenue Decomposition for Chapter 4. (Effort: 8 person-weeks).
