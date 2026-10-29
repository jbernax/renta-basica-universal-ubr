---
id: M13
title: Territorial purchasing power, internal mobility, and residency rules
status: draft
locked: false
depends_on: [M02, M03, M05, M06, M12]
covers: [F14]
feeds_chapters: [5, 6]
last_iteration: 3
---
# M13 · Territorial purchasing power, internal mobility, and residency rules

## 1. Why this matters
Spain exhibits a 35–45% divergence in regional purchasing power parity (PPP) and housing rental costs between congested metropolitan centers (Madrid, Barcelona, Palma, San Sebastián) and depopulated rural provinces (*España vaciada*: Soria, Teruel, Cuenca, Zamora) [@boe-vivienda-2023]. A nationally uniform nominal UBR (€900/month) functions as a massive structural equalizing force—delivering a high real living standard in rural areas—while raising fundamental challenges regarding internal migration, spatial sorting, urban housing absorption (`M05`), and external migration residency criteria under EU law (`M06`).

## 2. Research questions
- **RQ-M13-01**: Should Spain's baseline UBR be paid as a strictly uniform nominal transfer nationwide, or modulated across autonomous communities by regional purchasing power parity indices?
  - *Hypothesis:* A uniform nominal national floor (anchored in basic constitutional equality under Art. 149.1.1 CE [@boe-ce-1978] and preventing mechanical capitalization into urban land rents `M05`) is welfare-superior to price-indexed national transfers; Autonomous Communities seeking to alleviate metropolitan living costs can fund supplementary housing allowances from own-source regional taxes (`M03`, `M06`).
- **RQ-M13-02**: How can statutory residency rules balance fiscal sustainability with the constitutional requirement of **Tax-Benefit Symmetry** (Art. 31.1 CE, STC 214/1994 [@stc-214-1994-minimo-existencial]), EU free movement (Art. 45 TFEU; Regulation (EU) No 492/2011 [@eu-regulation-492-2011]), and the CJEU *Schumacker* doctrine for cross-border workers?
  - *Hypothesis:* For EU workers under Art. 45 TFEU, establishing an objective Social Security affiliation threshold ($\ge 10\text{--}12$ hours/week or $\ge 25\%$ of SMI, conforming to CJEU Case 66/85 *Lawrie-Blum* [@cjeu-c-66-85-lawrie-blum] and Case C-14/09 *Genc* [@cjeu-c-14-09-genc]) paired with a pro-rata tapering schedule for sub-threshold employment satisfies EU non-discrimination. Resident taxpayers serving waiting periods retain a **Default Non-Refundable Mínimo Personal y Familiar** under *Ley 35/2006*, preventing unconstitutional taxation from euro 1 (STC 214/1994 [@stc-214-1994-minimo-existencial]), while all resident minors receive an unconditional child allowance safe-harbor under Art. 39 CE.
- **RQ-M13-03**: To what extent does a portable, uniform UBR overcome historical Spanish labor immobility frictions (homeownership lock-in, 6–10% regional ITP transfer taxes, and dual-earner co-location frictions [@costa-kahn-2000-power-couples]) to induce relocation toward *España vaciada*?
  - *Hypothesis:* Incorporating regional housing tenure, ITP frictions [@antolin-bover-1997-migration], and dual-earner career coordination penalties [@costa-kahn-2000-power-couples] reveals that cash portability alone yields modest relocation (2.5–3.8%); pairing UBR with rural housing mobilization (*Programa de Movilización de Vivienda Rural Vacía* via ICO zero-interest loans) and regional ITP exemptions increases 5-year net migration to municipalities under 10,000 inhabitants by 6.2–8.5% across S2 and S3.

## 3. State of knowledge
Spatial equilibrium theory (Roback-Moretti frameworks) demonstrates that uniform national cash transfers encourage geographic decentralization toward lower-cost regions with higher amenities, whereas cost-of-living adjustments trap low-income households in congested cities and are captured by landlords [@fack-2006-housing-benefits; @diamond-mcquade-qian-2019-rent]. Cash-transfer trials confirm that portable grants increase residential flexibility [@bartik-2024-openresearch]. In Spain, however, inter-provincial migration is historically constrained by high owner-occupancy rates, 6–10% regional transaction taxes (*Impuesto sobre Transmisiones Patrimoniales*, ITP), thin rural rental markets, and dual-career co-location frictions [@antolin-bover-1997-migration; @costa-kahn-2000-power-couples]. In external migration, EU law establishes that EU workers who pursue "effective and genuine" economic activities cannot be denied social and tax advantages (Regulation (EU) 492/2011 [@eu-regulation-492-2011]; *Lawrie-Blum* [@cjeu-c-66-85-lawrie-blum]; *Genc* [@cjeu-c-14-09-genc]; *Schumacker* [@cjeu-c-279-93-schumacker]), while economically inactive arrivals may be subject to proportional waiting periods under Directive 2004/38/EC [@eu-dir-2004-38-free-movement].

## 4. Spain context & data sources
- **Spatial & Mobility Microdata:** INE *Estadística de Variaciones Residenciales* (EVR, tracking all inter-municipal changes of residence), *Padrón Municipal Continuo*, regional PPP indices, and Ministry of Housing (MIVAU) municipal rental price indexes (*Sistema Estatal de Referencia de Precios de Alquiler*).
- **Residency, Labor, and Tax Spine:**
  - *Ley Orgánica 4/2000 sobre derechos y libertades de los extranjeros en España* (LOEX [@boe-extranjeria-2000], legal residency authorizations and *arraigo* mechanisms).
  - *Ley 19/2021* [@boe-imv-2021] (IMV 1-year legal residency threshold and exceptions for minors, trafficking victims, and domestic violence survivors).
  - *Ley 35/2006 del IRPF* (LIRPF Art. 9 on fiscal residency: >183 days or center of economic interests in Spain) and *RDLeg 5/2004 del IRNR*.
  - Constitutional Court doctrine on the *mínimo existencial* (STC 214/1994 [@stc-214-1994-minimo-existencial]) and child protection (Art. 39 CE [@boe-ce-1978]).
  - Regulation (EU) No 492/2011 [@eu-regulation-492-2011] and Directive 2004/38/EC [@eu-dir-2004-38-free-movement].
  - CJEU Case 66/85 (*Lawrie-Blum* [@cjeu-c-66-85-lawrie-blum]), Case C-14/09 (*Genc* [@cjeu-c-14-09-genc]), and Case C-279/93 (*Schumacker* [@cjeu-c-279-93-schumacker]).

## 5. Methods & identification
1. **The Tax-Benefit Symmetry, EU Worker Threshold, and Schumacker Protocol:**
   - Formalize the legal-economic rule: Any resident individual earning taxable income subject to Spanish IRPF who is subjected to the reformed tax tariff (`M03`) receives the UBR tax credit from month one.
   - For EU workers claiming Art. 45 TFEU rights and Regulation (EU) 492/2011 [@eu-regulation-492-2011], establish an objective threshold of "effective and genuine employment" defined by Social Security registration for at least 10–12 hours/week or earnings $\ge 25\%$ SMI (Case 66/85 *Lawrie-Blum* [@cjeu-c-66-85-lawrie-blum]; Case C-14/09 *Genc* [@cjeu-c-14-09-genc]), paired with a pro-rata tapering schedule for marginal part-time workers.
   - Extend the pro-rata credit to frontier and seasonal workers paying IRNR who earn $\ge 75\%$ of global income in Spain per CJEU *Schumacker* [@cjeu-c-279-93-schumacker].
   - **Default Non-Refundable Allowance:** Resident taxpayers during statutory waiting periods retain a default non-refundable *mínimo personal y familiar* in *Ley 35/2006*, guaranteeing that baseline income up to €5,550 is zero-taxed (STC 214/1994 [@stc-214-1994-minimo-existencial]).
   - **Child Safe-Harbor:** All children residing in Spain receive the child allowance component (`M02`) immediately upon registration in the municipal *Padrón*, grounded in the absolute constitutional protection of minors under Art. 39 CE [@boe-ce-1978].
   - Inactive non-contributing arrivals (non-working EU citizens without comprehensive sickness insurance or non-EU third-country nationals) remain subject to a 24-month continuous legal residency requirement before drawing the non-contributory cash component, conforming to CJEU Case C-333/13 *Dano*.
2. **Spatial Discrete-Choice Location Model with Immobility & Dual-Earner Frictions:**
   - Formulate a structural discrete-choice model across Spain's 8,131 municipalities following Antolín & Bover [@antolin-bover-1997-migration] and Costa & Kahn [@costa-kahn-2000-power-couples]. Joint household utility:
     $$U_{ijt} = \alpha [w_{1jt}(1 - \tau) + w_{2jt}(1 - \tau) + 2 \cdot \text{UBR} - r_{jt}] + \beta A_j - \delta d_{ij} - \kappa \cdot \text{ITP}_j - \theta \cdot \text{Owner}_i - \lambda \cdot \text{DualCareerLoss}_{ijt} + \varepsilon_{ijt}$$
     where $r_{jt}$ is local rent (`M05`), $A_j$ captures local public capital (broadband, primary healthcare, schooling), $\text{ITP}_j$ is the regional conveyance tax rate (6–10%), $\text{Owner}_i$ captures owner-occupancy lock-in, and $\lambda$ estimates the career penalty when moving to a thin rural labor market.
   - Model the mitigating effect of the *Programa de Movilización de Vivienda Rural Vacía* (ICO zero-interest rehabilitation loans) and regional ITP exemptions on rural housing absorption.

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
- Comprehensive Spatial Equilibrium Simulation and Demographic Mobility Atlas for Spain (incorporating dual-career co-location frictions).
- Model Statutory Text on Residency Qualifications, Tax-Benefit Symmetry, Default Non-Refundable Allowance, Child Safe-Harbor, and Anti-Fraud Controls for Chapters 5 and 6. (Effort: 4 person-weeks).
