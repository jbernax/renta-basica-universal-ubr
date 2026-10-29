---
id: M05
title: Housing market pass-through and landlord rent capture
status: draft
locked: false
depends_on: [M02, M04, M10, M13]
covers: [F06]
feeds_chapters: [5]
last_iteration: 3
---
# M05 · Housing market pass-through and landlord rent capture

## 1. Why this matters
Housing is the single largest threat to the real welfare impact of a cash UBR in Spain. In metropolitan areas with rigid housing supply and high tourist/seasonal rental pressure (Madrid, Barcelona, Málaga, Balearic and Canary Islands), an unconditional increase in tenant disposable income risks being partially captured by landlords through higher rents [@fack-2006-housing-benefits; @khametshin-2024-rental], converting a public transfer into private land rent and eroding living standards for middle-decile private renters (`M09`). However, rental markets are not frictionless: tenure security under *Ley 29/1994 de Arrendamientos Urbanos* (LAU Art. 9 [@boe-lau-1994]) locks in contract terms for 5 years (7 years for corporate landlords), meaning rent capture bifurcates sharply between incumbent protected tenants and new market entrants, while landlords increasingly exploit seasonal and room rental loopholes to evade statutory rent caps [@garcia-montalvo-2023-rent-controls; @garcia-montalvo-2023-rent-control; @jofre-monseny-2023-rent-control]. Furthermore, under STC 79/2024 [@stc-79-2024-vivienda], declaring stressed zones under *Ley 12/2023* is an exclusive regional competence; widespread regional boycotts (Madrid, Andalusia, Balearic Islands) leave key urban rental markets legally unprotected unless federal tax powers (Art. 149.1.14 CE) provide an objective fiscal benchmark.

## 2. Research questions
- **RQ-M05-01**: What fraction of an unconditional cash transfer (Tiers A/B) is capitalized into higher private market rents across Spanish municipalities with low versus high housing supply elasticity, accounting for LAU Art. 9 mandatory 5-year lease stability?
  - *Hypothesis:* In supply-inelastic urban zones, rent capture on new lease contracts reaches 25–38% within 24 months per Khametshin et al. [@khametshin-2024-rental], whereas incumbent tenants on active 5-year LAU contracts face near-zero short-run pass-through until lease expiration, creating a pronounced insider-outsider tenure divergence.
- **RQ-M05-02**: Which complementary housing policy package—statutory reference rent caps under *Ley 12/2023* [@boe-vivienda-2023], an Objective Federal Fiscal Benchmark under Art. 149.1.14 CE conditioning LIRPF Art. 23.2 landlord tax deductions on MIVAU SERPAVI reference price indices wherever rent-to-income exceeds 30% (bypassing regional boycotts under STC 79/2024 [@stc-79-2024-vivienda]), or municipal *tanteo y retracto* acquisitions—most effectively suppresses rent capture without shrinking rental supply?
  - *Hypothesis:* Standalone rent caps incentivize landlords to divert up to 20% of listings into unregulated seasonal and room rentals [@garcia-montalvo-2023-rent-controls; @garcia-montalvo-2023-rent-control; @jofre-monseny-2023-rent-control]; pairing caps with an Objective Federal Fiscal Benchmark on LIRPF Art. 23.2 reductions (50% reduction conditioned on SERPAVI rent stability) and a High-Frequency Rental Nowcasting Spine suppresses rent capture by >70% across all CCAA while preserving long-term supply.

## 3. State of knowledge
Empirical evaluations of housing allowances demonstrate substantial incidence on rents when rental supply is inelastic: Fack [@fack-2006-housing-benefits] finds that 50–78% of French housing benefit increases were absorbed by higher rents. In Spain, recent empirical evaluations of the Catalan rent control regime show that price ceilings lowered negotiated rents by 4–6% for covered units but reduced private rental supply by 10–15% as landlords diverted units into exempt seasonal rentals [@garcia-montalvo-2023-rent-controls; @garcia-montalvo-2023-rent-control; @jofre-monseny-2023-rent-control; @diamond-mcquade-qian-2019-rent]. Cash transfer trials show that portable transfers facilitate out-migration to lower-cost areas [@bartik-2024-openresearch], mitigating metropolitan pressure if geographic frictions are overcome (`M13`).

## 4. Spain context & data sources
- **Legal Framework:** *Ley 12/2023, por el derecho a la vivienda* [@boe-vivienda-2023] (*zonas tensionadas*, state rent reference index *SERPAVI*), STC 79/2024 [@stc-79-2024-vivienda], *Ley 29/1994 de Arrendamientos Urbanos* (LAU [@boe-lau-1994]), and *Ley 35/2006 del IRPF* (Art. 23.2 landlord net rental yield reduction [@boe-irpf-2006]).
- **Administrative Microdata:** Mandatory regional rental deposit registries (*fianzas de alquiler obligatorias*): INCASÒL (Catalonia), IVIMA (Madrid), and AVRA (Andalusia); Ministry of Housing (MIVAU) SERPAVI panel; and AEAT IRPF real-estate return declarations.
- **High-Frequency Nowcasting:** Scraped rental listing APIs (Idealista, Fotocasa) paired with monthly tenancy deposit flows and bank transaction data with $\le 30$-day latency to overcome official index reporting lags per Khametshin et al. [@khametshin-2024-rental].

## 5. Methods & identification
1. **Quasi-Experimental Pass-Through Identification:** Exploit policy discontinuities in Spanish housing demand: (i) age eligibility cutoffs in the *Bono Alquiler Joven* (€250/month cash transfer capped at age 35), (ii) municipal border discontinuities in *Ley 12/2023* stressed-zone declarations across bordering municipalities in Catalonia [@garcia-montalvo-2023-rent-control], and (iii) regional minimum-income housing supplement expansions in the Basque Country and Navarre.
2. **Dual-Tenure Equilibrium Model & Objective Federal Benchmark:** Formulate a structural rental market model distinguishing incumbent tenants (protected by LAU Art. 9 5-year lock-in) from new listings, explicitly incorporating contract substitution into seasonal (LAU Art. 3.2) and room rentals. Model the Objective Federal Fiscal Benchmark under Art. 149.1.14 CE conditioning LIRPF Art. 23.2 reductions on verified rent-to-income $\le 30\%$ and SERPAVI compliance, decoupling anti-capture tax policy from regional ZMRT boycotts. Feed equilibrium rent vectors directly into `M09` and `M17`.

## 6. Pilot implications
- **Municipal Tier:** Track matched landlord-tenant administrative deposit microdata (INCASÒL / IVIMA / AVRA) in high-saturation pilot clusters (`M10`) against buffered control clusters, isolating the differential rent trajectory between active contracts and turnover leases.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** Compare pass-through in common-regime regions applying *Ley 12/2023* stressed zones (e.g. Catalonia) versus non-applying regions (e.g. Madrid), contrasting with Basque foral rental tax deductions.
- **National Tier:** Connect directly to the `M17` Housing Pass-Through Circuit-Breaker: if high-frequency nowcasted municipal rent indices exceed core CPI by >3.0 pp, activate immediate fiscal/regulatory levers (zeroing LIRPF Art. 23.2 landlord deductions, capping seasonal rents, and fast-tracking municipal *tanteo y retracto* acquisitions financed through a dedicated *Fondo de Estabilización Residencial*).

## 7. Risks, counterarguments & open issues
- **Counterargument (UBR Fuels Urban Rent Inflation):** Critics argue in-kind housing provision should precede cash UBR. *Mitigation:* Quantify the exact pass-through threshold and test whether portable UBR combined with seasonal-lease regulation and immediate tax conditionality protects tenant purchasing power (`M13`, `M17`).

## 8. Deliverables & effort
- Municipal Rental Supply Elasticity & Dual-Tenure Pass-Through Model for Spain.
- Housing Policy Complementarity Simulation & Regulatory Loop for Chapter 5. (Effort: 5 person-weeks).
