---
id: M04
title: Macroeconomic dynamics, inflation, and Eurozone constraints
status: draft
locked: false
depends_on: [M01, M03, M05, M16]
covers: [F05]
feeds_chapters: [5]
last_iteration: 1
---
# M04 · Macroeconomic dynamics, inflation, and Eurozone constraints

## 1. Why this matters
Spain is a medium-sized open economy inside the Eurozone: it cannot devalue its currency or instruct the Banco de España to monetize fiscal deficits, and it is bound by the EU's reformed fiscal governance framework (*Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework]) and domestic fiscal rules (*Ley Orgánica 2/2012*, LOEPSF [@boe-loepsf-2012]). A state-of-the-art plan must demonstrate that UBR stabilizes domestic demand during an AI-driven wage contraction without igniting non-tradable inflation, sovereign spread widening, or violating the multi-annual Net Primary Expenditure path [@kaplan-moll-violante-2018-hank; @auclert-rognlie-straub-2024; @gali-monacelli-2005-soe].

## 2. Research questions
- **RQ-M04-01**: In a small-open-economy currency-union HANK model with sticky prices and heterogeneous hand-to-mouth households, under what combinations of AI supply shocks (`M01`) and tax financing (`M03`, `M16`) does UBR stabilize aggregate demand while keeping core non-tradable inflation within $\pm 0.3$ pp of the ECB target?
  - *Hypothesis:* When UBR is 100% tax-financed under S1 and S2, the aggregate demand multiplier from redistributing toward high-MPC bottom deciles (+0.8 to +1.4% GDP) is counterbalanced by AI-driven marginal-cost reductions in tradable and digital services, preserving competitiveness—provided local urban rent capture (`M05`) is constrained.
- **RQ-M04-02**: How does the multi-annual Net Primary Expenditure Ceiling under *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] constrain the UBR rollout, and how must gross outlays be legally paired with Discretionary Revenue Measures (*Medidas Discrecionales de Ingresos*, MDI) to avoid triggering an Excessive Deficit Procedure?
  - *Hypothesis:* By formally netting gross UBR outlays against simultaneous discretionary IRPF/IVA/corporate revenue reforms (`M03`, `M16`) in the annual Stability Programme, net expenditure growth remains strictly within European Commission ceilings and prevents Bonos-Bund sovereign spread widening beyond baseline levels ($\le 85$ bps).

## 3. State of knowledge
Heterogeneous-Agent New Keynesian (HANK) models demonstrate that redistribution from low-MPC wealthy savers to high-MPC liquidity-constrained households generates robust balanced-budget multipliers [@kaplan-moll-violante-2018-hank; @auclert-rognlie-straub-2024]. In a currency union without national monetary sovereignty [@gali-monacelli-2005-soe], inflation differentials generate real-interest-rate (Walters) dynamics: domestic inflation lowers the real borrowing rate in the short term, but subsequently erodes terms-of-trade competitiveness and raises sovereign risk premia if debt sustainability is questioned [@eu-reg-2024-1263-fiscal-framework; @boe-loepsf-2012].

## 4. Spain context & data sources
- **Household Balance Sheets & Wealth:** Banco de España *Encuesta Financiera de las Familias* (EFF) for liquid/illiquid wealth distribution and hand-to-mouth shares.
- **Macro Accounts & External Sector:** INE *Contabilidad Nacional Trimestral*, Input-Output tables and Figaro inter-country tables (for import propensity by COICOP category and NACE sector), and AIReF / Banco de España fiscal projections.
- **Fiscal Governance:** *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] and *Ley Orgánica 2/2012 de Estabilidad Presupuestaria y Sostenibilidad Financiera* (LOEPSF [@boe-loepsf-2012]).

## 5. Methods & identification
1. **Small-Open-Economy Currency-Union HANK Model:** Formalize a two-sector (tradables vs. non-tradables/housing) HANK model calibrated to Spanish EFF wealth deciles and EPF consumption shares [@kaplan-moll-violante-2018-hank; @gali-monacelli-2005-soe]. Specify the ECB area-wide Taylor rule (Spain weight 10%), fixed nominal exchange rate, and endogenous Bonos-Bund spread as a function of debt-to-GDP and structural primary deficit.
2. **Dual External Leakage Accounting:** Quantify two distinct leakage channels in the Balance of Payments: (i) household consumption import leakage (high in electronics and energy; low in domestic services/food) and (ii) corporate B2B imports of foreign AI compute, cloud subscriptions, and software royalties.
3. **Four-Stage Micro-Macro Iteration (`methods.md`):** Execute the Gauss-Seidel fixed-point loop between EUROMOD (`M03`, `M09`) and HANK (`M04`) to ensure macro equilibrium prices, wages, and GDP feed back into tax-benefit revenues until convergence within $\pm 0.05\%$ of GDP.

## 6. Pilot implications
- **Municipal Tier:** High-saturation municipal pilots (`M10`) allow direct measurement of local non-tradable price responses and service multipliers, though external leakage is higher at the municipal boundary than at the national border.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** In *Régimen Común*, regional debt limits are governed by the *Fondo de Liquidez Autonómica* (FLA) and LOEPSF [@boe-loepsf-2012]; in *Régimen Foral* (Basque Country / Navarre), autonomous borrowing capacity and separate bilateral debt targets allow evaluating regional deficit-neutrality rules.
- **National Tier:** Embed macroeconomic circuit-breakers (`M17`) that pause nominal UBR step-ups if domestic core non-tradable inflation exceeds the Eurozone average by >1.5 pp.

## 7. Risks, counterarguments & open issues
- **Counterargument (Current-Account Deterioration):** Increased household liquidity could leak into imported consumer goods and foreign digital services, worsening Spain's net international investment position (NIIP). *Mitigation:* Calibrate sector-specific import propensities and evaluate how UBR-financed human capital and local service demand stimulate domestic value-added.

## 8. Deliverables & effort
- Calibrated Open-Economy Currency-Union HANK Codebase & S1–S3 Impulse Response Functions.
- EU Fiscal Governance Compliance Memo (Regulation 2024/1263 & LOEPSF) for Chapter 5. (Effort: 7 person-weeks).
