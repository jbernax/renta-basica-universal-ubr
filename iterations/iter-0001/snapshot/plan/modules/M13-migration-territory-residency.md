---
id: M13
title: Territorial purchasing power, internal mobility, and residency rules
status: draft
locked: false
depends_on: [M02, M05, M06, M12]
covers: [F14]
feeds_chapters: [5, 6]
last_iteration: 0
---
# M13 · Territorial purchasing power, internal mobility, and residency rules

## 1. Why this matters
Spain displays a 35–45% gap in regional purchasing power parity (PPP) and rental costs between metropolitan cores (Madrid, Barcelona, San Sebastián, Palma) and depopulated rural provinces (*España vaciada*: Soria, Teruel, Cuenca, Zamora) [@boe-vivienda-2023]. A nationally uniform nominal UBR (€900/month) acts as a powerful spatial equalizer—providing a high real living standard in rural municipalities—while simultaneously raising questions about internal migration, urban housing adequacy (`M05`), and external migration residency rules (`M06`).

## 2. Research questions
- **RQ-M13-01**: Should Spain's UBR be paid as a strictly uniform nominal amount across the entire territory, or modulated by regional/municipal cost-of-living indices?
  - *Hypothesis:* A uniform nominal State UBR floor (preserving constitutional equality under Art. 149.1.1 CE [@boe-ce-1978] and avoiding capitalization into metropolitan land rents `M05`) outperforms regionally price-indexed national transfers; Autonomous Communities wishing to top up urban housing costs should finance supplements from own regional taxes (`M03`, `M06`).
- **RQ-M13-02**: To what extent does a portable, nationally uniform UBR induce voluntary residential relocation from high-rent metropolitan areas (`M05`) to mid-sized towns and rural municipalities (*España vaciada*) when remote work or AI displacement (`M01`) decouples income from big-city commuting?
  - *Hypothesis:* Under S2 and S3, a portable €900/adult UBR increases net residential retention and in-migration in municipalities under 10,000 inhabitants by 4–7% over 5 years, partially relieving metropolitan rental pressure (`M05`).

## 3. State of knowledge
Spatial equilibrium theory (Roback-Moretti frameworks) predicts that nominally uniform national transfers subsidize relocation to lower-cost, high-amenity regions, whereas cost-of-living-indexed transfers lock households into congested cities and capitalize into urban land values [@fack-2006-housing-benefits; @diamond-mcquade-qian-2019-rent]. Empirical cash-transfer studies confirm that unconditional portable transfers increase geographic mobility toward better housing and labor markets [@bartik-2024-openresearch]. Regarding external migration, welfare-magnet literature finds modest empirical effects that are effectively governed by statutory qualifying residency periods under EU Directive 2004/38/EC and Regulation 883/2004 [@eu-reg-883-2004].

## 4. Spain context & data sources
- **Spatial & Demographic Data:** INE *Estadística de Variaciones Residenciales* (EVR, inter-municipal migration flows), *Padrón Continuo*, regional PPP estimates, and MIVAU municipal housing price panels.
- **Residency & Legal Framework:** *Ley Orgánica 4/2000 sobre derechos y libertades de los extranjeros*, *Ley 19/2021* [@boe-imv-2021] (IMV requires 1 year of continuous legal residence in Spain, with exceptions for minors, trafficking victims, and gender-violence survivors), and EU Regulation 883/2004 [@eu-reg-883-2004].

## 5. Methods & identification
1. **Spatial Discrete-Choice Location Model:** Estimate a municipality choice model on EVR + MCVL data as a function of real net disposable income $(w_m + \text{UBR} - r_m)$, local public services, and AI remote-work feasibility (`M01`).
2. **Residency Eligibility Comparison:** Compare three residency rules—(R1) 12 months lawful residence (IMV baseline [@boe-imv-2021]), (R2) 24–36 months continuous lawful residence and fiscal domicile, and (R3) phased-in fractional accrual over years 1–3—evaluating fiscal cost (`M03`), EU legal validity (`M06`), and human-rights/destitution safeguards.

## 6. Pilot implications
- **Municipal / Regional (`M10`):** Include at least two low-density rural *comarcas* in the saturation pilot arm to measure demographic retention, local small-business creation, and municipal service utilization.
- **Strict Anti-Inflow Rule for Pilots:** Pilot eligibility must be locked to individuals registered in the municipal *Padrón* at least 12 months **prior** to the public announcement date of the pilot.

## 7. Risks, counterarguments & open issues
- **Counterargument (Welfare Magnet / Pull Factor):** Critics argue a €900 unconditional transfer will attract fiscally unsustainable inflows. *Mitigation:* Condition full UBR eligibility on continuous prior legal and fiscal residency (R2/R3, `M06`) with humanitarian exemptions for asylum/gender-violence cases.

## 8. Deliverables & effort
- Regional PPP Real-Value Atlas & Rural Demographic Retention Simulation.
- Statutory Residency Eligibility Specification for Chapter 5 and Chapter 6. (Effort: 4 person-weeks).
