---
id: M13
title: Territorial purchasing power, internal mobility, and residency rules
status: draft
locked: false
depends_on: [M02, M03, M05, M06, M12]
covers: [F14]
feeds_chapters: [5, 6]
last_iteration: 1
---
# M13 · Territorial purchasing power, internal mobility, and residency rules

## 1. Why this matters
Spain exhibits a 35–45% divergence in regional purchasing power parity (PPP) and housing rental costs between congested metropolitan centers (Madrid, Barcelona, Palma, San Sebastián) and depopulated rural provinces (*España vaciada*: Soria, Teruel, Cuenca, Zamora) [@boe-vivienda-2023]. A nationally uniform nominal UBR (€900/month) functions as a massive structural equalizing force—delivering a high real living standard in rural areas—while raising fundamental challenges regarding internal migration, spatial sorting, urban housing absorption (`M05`), and external migration residency criteria under EU law (`M06`).

## 2. Research questions
- **RQ-M13-01**: Should Spain's baseline UBR be paid as a strictly uniform nominal transfer nationwide, or modulated across autonomous communities by regional purchasing power parity indices?
  - *Hypothesis:* A uniform nominal national floor (anchored in basic constitutional equality under Art. 149.1.1 CE [@boe-ce-1978] and preventing mechanical capitalization into urban land rents `M05`) is welfare-superior to price-indexed national transfers; Autonomous Communities seeking to alleviate metropolitan living costs can fund supplementary housing allowances from own-source regional taxes (`M03`, `M06`).
- **RQ-M13-02**: How can statutory residency rules balance fiscal sustainability and anti-fraud controls with the constitutional requirement of **Tax-Benefit Symmetry** (Art. 31.1 CE) and EU free movement of workers (Art. 45 TFEU)?
  - *Hypothesis:* A statutory design that restricts 12–36 month waiting periods strictly to *economically inactive* third-country and EU entrants—while granting immediate pro-rata UBR tax credits to all economically active residents subject to Spanish IRPF under Art. 9 LIRPF—fully satisfies Art. 45 TFEU and Directive 2004/38/EC [@eu-dir-2004-38-free-movement] while eliminating unconstitutional taxation of the *mínimo existencial*.
- **RQ-M13-03**: To what extent does a portable, uniform UBR induce voluntary residential relocation from high-rent metropolitan cores (`M05`) to intermediate cities and rural municipalities (*España vaciada*) as AI displacement (`M01`) decouples income from physical office presence?
  - *Hypothesis:* Under S2 and S3, a portable €900/adult transfer increases 5-year net migration to municipalities under 10,000 inhabitants by 5.5–8.2%, revitalizing local service economies and mitigating metropolitan rental demand.

## 3. State of knowledge
Spatial equilibrium theory (Roback-Moretti frameworks) demonstrates that uniform national cash transfers encourage geographic decentralization toward lower-cost regions with higher environmental amenities, whereas cost-of-living adjustments trap low-income households in congested metropolitan areas and are heavily captured by landlords [@fack-2006-housing-benefits; @diamond-mcquade-qian-2019-rent]. Real-world cash-transfer trials confirm that portable cash grants significantly increase residential flexibility and long-distance mobility toward affordable housing [@bartik-2024-openresearch]. Regarding external migration, empirical evidence shows that welfare magnet effects are modest in scale and primarily regulated through statutory qualifying residence durations and labor-market integration criteria under EU law [@eu-dir-2004-38-free-movement; @eu-reg-883-2004].

## 4. Spain context & data sources
- **Spatial & Mobility Microdata:** INE *Estadística de Variaciones Residenciales* (EVR, tracking all inter-municipal changes of residence), *Padrón Municipal Continuo*, regional PPP indices, and Ministry of Housing (MIVAU) municipal rental price indexes (*Sistema Estatal de Referencia de Precios de Alquiler*).
- **Residency, Labor, and Tax Spine:**
  - *Ley Orgánica 4/2000 sobre derechos y libertades de los extranjeros en España* (LOEX, legal residency authorizations and *arraigo* mechanisms).
  - *Ley 19/2021* [@boe-imv-2021] (IMV 1-year legal residency threshold and exceptions for minors, trafficking victims, and domestic violence survivors).
  - *Ley 35/2006 del IRPF* (LIRPF Art. 9 on fiscal residency: >183 days or center of economic interests in Spain).
  - Directive 2004/38/EC [@eu-dir-2004-38-free-movement] (freedom of movement and equal treatment for EU workers and self-employed).

## 5. Methods & identification
1. **The Tax-Benefit Symmetry Framework:**
   - Formalize the legal-economic rule: Any resident individual earning taxable income subject to Spanish IRPF who is subjected to the reformed tax tariff (`M03`) without the personal allowance (*mínimo personal*) MUST receive the UBR tax credit from month one. Subjecting a worker to increased marginal tax rates while denying the basic transfer violates the constitutional principle of economic capacity (*capacidad económica*, Art. 31.1 CE).
   - Inactive non-contributing arrivals (non-working EU citizens without comprehensive sickness insurance or non-EU third-country nationals) are subject to a statutory 24-month continuous legal residency requirement before drawing the non-contributory cash component, strictly conforming to CJEU Case C-333/13 *Dano*.
2. **Spatial Discrete-Choice Location Model:**
   - Formulate a structural discrete-choice model across Spain's 8,131 municipalities. Utility $U_{ijt} = \alpha [w_{jt}(1 - \tau) + \text{UBR} - r_{jt}] + \beta A_j - \delta d_{ij} + \varepsilon_{ijt}$, where $r_{jt}$ is local rent (`M05`), $A_j$ captures local public infrastructure (broadband, primary healthcare, schooling), and $d_{ij}$ is moving distance.
   - Simulate counterfactual spatial equilibrium populations across S1–S3 under uniform vs. regionally indexed transfers.

## 6. Pilot implications
- **Municipal:** Highly vulnerable to strategic local cross-border shopping and municipal "welfare shopping" (*efecto llamada municipal*) unless strictly constrained. Any municipal-level pilot (such as Barcelona B-MINCOME [@todeschini-bmincome-2020]) must mandate that participants were registered in the municipal *Padrón* at least 12–24 months *prior* to the public launch date of the pilot.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común* CCAA, inter-regional migration between autonomous communities cannot be constitutionally restricted (Art. 139.2 CE), requiring regional pilots to track cross-regional mobility through the MCVL to measure inter-autonomous spillover flows.
  - In *Régimen Foral* (Basque Country / Navarre), historical residence requirements for regional minimum incomes (RGI currently requires 1–3 years of municipal registration) provide an established legal template to evaluate regional residency filtering within a constitutionally protected fiscal framework.
- **National:** Eliminates all domestic inter-regional welfare-border distortions; enforces uniform legal residency verification across the entire national frontier, seamlessly synchronizing the Ministry of the Interior (foreign residency authorizations), the AEAT (fiscal domicile), and INE *Padrón Continuo*.

## 7. Risks, counterarguments & open issues
- **Counterargument (Cross-Border Welfare Magnetism):** Critics allege that an unconditional €900 cash transfer will induce massive irregular migration flows. *Mitigation:* The dual architecture links immediate eligibility to formal fiscal registration (IRPF), while requiring 24 months of legal registered presence for economically inactive claimants. This fully complies with EU case law (*Dano*, *Alimanovic*) and preserves national fiscal stability.
- **Counterargument (Depopulation of Metropolitan Service Sectors):** Low-wage service workers in high-cost cities might relocate to rural areas, causing urban labor shortages in local non-tradable services. *Mitigation:* As shown in `M08`, reservation wage bargaining increases urban service wages, inducing wage-driven market equilibrium rather than permanent shortages.

## 8. Deliverables & effort
- Comprehensive Spatial Equilibrium Simulation and Demographic Mobility Atlas for Spain.
- Model Statutory Text on Residency Qualifications, Tax-Benefit Symmetry, and Anti-Fraud Controls for Chapters 5 and 6. (Effort: 4 person-weeks).
