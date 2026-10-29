---
id: M05
title: Housing market pass-through and landlord rent capture
status: draft
locked: false
depends_on: [M02, M04, M10, M13]
covers: [F06]
feeds_chapters: [5]
last_iteration: 0
---
# M05 · Housing market pass-through and landlord rent capture

## 1. Why this matters
Housing is the single largest threat to the real welfare impact of a cash UBR in Spain. In metropolitan areas with rigid housing supply and high tourist/seasonal rental pressure (Madrid, Barcelona, Málaga, Balearic and Canary Islands), an unconditional increase in tenant disposable income risks being partially captured by landlords through higher rents [@fack-2006-housing-benefits], converting a public transfer into private land rent.

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
1. **Historical Pass-Through Identification:** Estimate local rental pass-through elasticities in Spain using spatial variation in IMV/CAPI rollouts [@boe-imv-2021] and regional minimum incomes interacted with municipal topographic and regulatory supply constraints (Saiz-style elasticity proxy from Catastro + municipal urban plans).
2. **Spatial Equilibrium Simulation:** Link `M05` rental supply elasticities with `M13` internal migration choices to model equilibrium rent paths in Madrid/Barcelona vs. *España vaciada*.

## 6. Pilot implications
- **Municipal:** High-saturation census tracts in `M10` must track matched landlord-tenant contract registries (*fianzas de alquiler* deposited in INCASÒL / IVIMA) to measure real-time rent pass-through against control tracts.
- **Regional:** Compare pass-through in regions applying *Ley 12/2023* stressed-zone caps (Catalonia) versus non-applying regions.
- **National:** Pair national UBR rollout with a statutory social-housing co-investment rule.

## 7. Risks, counterarguments & open issues
- **Counterargument (UBR Fuels Urban Rent Inflation):** Critics argue in-kind housing provision should precede cash UBR. *Mitigation:* Quantify the exact pass-through threshold and test whether portable UBR reduces metropolitan crowding by making lower-cost municipalities economically viable (`M13`).

## 8. Deliverables & effort
- Municipal Rental Supply Elasticity & Pass-Through Risk Map for Spain.
- Housing Policy Complementarity Simulation for Chapter 5. (Effort: 5 person-weeks).
