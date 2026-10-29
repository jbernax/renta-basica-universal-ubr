---
id: M05
title: Housing market pass-through and landlord rent capture
status: draft
locked: false
depends_on: [M02, M04, M10, M13]
covers: [F06]
feeds_chapters: [5]
last_iteration: 1
---
# M05 · Housing market pass-through and landlord rent capture

## 1. Why this matters
Housing is the single largest threat to the real welfare impact of a cash UBR in Spain. In metropolitan areas with rigid housing supply and high tourist/seasonal rental pressure (Madrid, Barcelona, Málaga, Balearic and Canary Islands), an unconditional increase in tenant disposable income risks being partially captured by landlords through higher rents [@fack-2006-housing-benefits], converting a public transfer into private land rent and eroding living standards for middle-decile private renters (`M09`).

## 2. Research questions
- **RQ-M05-01**: What fraction of an unconditional cash transfer (Tiers A/B) is capitalized into higher private market rents across Spanish municipalities with low versus high housing supply elasticity?
  - *Hypothesis:* In supply-inelastic stressed urban zones (*zonas de mercado residencial tensionado*) without complementary supply or rent-cap enforcement, 22–35% of the marginal income gain for bottom-decile private renters is captured by rent increases within 24 months, compared to <5% in elastic rural and mid-sized municipalities.
- **RQ-M05-02**: Which complementary housing policy package—reference rent caps under *Ley 12/2023* [@boe-vivienda-2023], rapid expansion of public social rental stock (*parque público*), or vacant-property/land-value surcharges in IBI/IRPF—most effectively suppresses rent pass-through without freezing tenant mobility?
  - *Hypothesis:* Combining UBR with automatic rural/mid-sized residential mobility portability (`M13`), vacant-unit tax surcharges, and public rental stock expansion outperforms standalone rent caps, which reduce pass-through for incumbents but shrink available rental listings [@diamond-mcquade-qian-2019-rent].

## 3. State of knowledge
Empirical evaluations of housing allowances and cash transfers demonstrate substantial incidence on rents when low-quality rental supply is inelastic: Fack [@fack-2006-housing-benefits] finds that 50–78% of French housing benefit increases were absorbed by higher rents. Conversely, rent control studies [@diamond-mcquade-qian-2019-rent] show strong protection for incumbent tenants alongside supply withdrawal via owner-occupancy or short-term conversions. Unconditional cash transfer RCTs show that liquidity enables residential moves toward opportunity or lower-cost areas [@bartik-2024-openresearch].

## 4. Spain context & data sources
- **Legal Framework:** *Ley 12/2023, por el derecho a la vivienda* [@boe-vivienda-2023] (*zonas tensionadas*, state rent reference index *SERPAVI*).
- **Datasets:** INE *Índice de Precios de la Vivienda en Alquiler* (IPVA), Ministry of Housing (MIVAU) *Sistema Estatal de Referencia del Precio del Alquiler de Vivienda*, AEAT IRPF real-estate return declarations, Dirección General del Catastro, and Idealista/Fotocasa municipal listing panels.

## 5. Methods & identification
1. **Quasi-Experimental Pass-Through Identification:** Avoid endogenous IMV rollout variation by exploiting sharp policy discontinuities in Spanish housing demand: (i) age eligibility cutoffs in the *Bono Alquiler Joven* (250 €/month cash transfer capped at age 35), (ii) geographic boundary discontinuities in *Ley 12/2023* stressed-zone declarations across bordering municipalities in Catalonia, and (iii) regional minimum-income housing supplement expansions in the Basque Country and Navarre.
2. **Spatial General Equilibrium Simulation:** Link `M05` rental supply elasticities with `M13` internal mobility choices to simulate equilibrium rent paths across Madrid/Barcelona vs. *España vaciada*, feeding rent vectors into `M09` to evaluate real post-rent disposable income.

## 6. Pilot implications
- **Municipal Tier:** Track matched landlord-tenant contract registries (*fianzas de alquiler* in INCASÒL / IVIMA) in high-saturation pilot census tracts (`M10`) to measure micro-level rent pass-through against control tracts.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** Compare pass-through in common-regime regions actively declaring stressed zones under *Ley 12/2023* (e.g. Catalonia) versus non-applying regions (e.g. Madrid), and contrast with foral tax-incentive models (e.g. Basque deducibilidad del alquiler).
- **National Tier:** Establish an automatic statutory circuit-breaker (`M17`) that redirects nominal UBR step-ups into public social housing supply if urban rent pass-through exceeds 20%.

## 7. Risks, counterarguments & open issues
- **Counterargument (UBR Fuels Urban Rent Inflation):** Critics argue in-kind housing provision should precede cash UBR. *Mitigation:* Quantify the exact pass-through threshold and test whether portable UBR reduces metropolitan crowding by making lower-cost municipalities economically viable (`M13`).

## 8. Deliverables & effort
- Municipal Rental Supply Elasticity & Pass-Through Risk Map for Spain.
- Housing Policy Complementarity Simulation for Chapter 5. (Effort: 5 person-weeks).
