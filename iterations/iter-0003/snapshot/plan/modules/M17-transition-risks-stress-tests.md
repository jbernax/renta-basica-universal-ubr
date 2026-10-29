---
id: M17
title: Transition path, scenario triggers, and tail-risk stress tests
status: draft
locked: false
depends_on: [M01, M03, M04, M05, M07, M10, M11, M16]
covers: [F17]
feeds_chapters: [8]
last_iteration: 2
---
# M17 · Transition path, scenario triggers, and tail-risk stress tests

## 1. Why this matters
Transitioning overnight from Spain's fragmented, means-tested welfare system to a universal Tier B or Tier C cash transfer would generate severe macroeconomic friction, inflationary risks, and fiscal deficit spikes. Conversely, an open-ended pilot without statutory scale-up rules risks political abandonment (`M11`). A state-of-the-art research plan must establish a phased, reversible **Transition Roadmap** governed by independent macroeconomic triggers, automatic fiscal and housing circuit-breakers (`M03`, `M05`), and adversarial tail-risk stress tests. Crucially, transition governance must fully respect the constitutional Principle of Tax Legality (Arts. 31.3 and 134.7 CE [@boe-ce-1978]) and the statutory organic mandate of AIReF under *Ley Orgánica 6/2013* [@boe-lo-6-2013-airef], ensuring that technical certifications lead to expedited democratic ratification rather than unlawful administrative tax delegation.

## 2. Research questions
- **RQ-M17-01**: What phased sequencing—from Phase 0 (unification and automatic individualization of IMV + CAPI) to Phase 1 (Multi-Level Pilot `M10` and Tier A €600 floor under S1), Phase 2 (Tier B €900 poverty-line UBR under S2), and Phase 3 (Tier C €1,200 AI-dividend UBR under S3)—minimizes transition costs while maintaining structural fiscal balance?
  - *Hypothesis:* A state-contingent roadmap governed by an AIReF-certified **Cyclically and Terms-of-Trade-Adjusted Composite Displacement Index** ($I_{\text{AI},t}$) informing a statutory Fast-Track Parliamentary Ratification Protocol under Art. 86 CE keeps the structural primary balance within $\pm 0.35\%$ of GDP throughout the transition while ensuring zero real disposable income loss for vulnerable cohorts via the `M07` guarantee.
- **RQ-M17-02**: How can immediate fiscal and housing circuit-breakers—specifically the **Housing Pass-Through Circuit-Breaker** (`M05`) and the **Fast-Track Fiscal Stabilization Surcharge**—cool short-run demand shocks and preserve fiscal stability under *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] without waiting for multi-year public housing construction?
  - *Hypothesis:* When local rental index growth exceeds core CPI by >3.0 pp in stressed zones (ZMRT), triggering immediate regulatory/fiscal levers (temporary revocation of LIRPF Art. 23.2 landlord tax deductions from 50% to 0%, emergency extension of price caps to seasonal/room rentals, and municipal *tanteo y retracto* acquisitions) suppresses rent pass-through by >65% within two quarters. Coupling this with an expedited countercyclical IRPF surcharge stabilizes aggregate demand under Art. 86 CE decree-laws without violating Tax Legality.

## 3. State of knowledge
Macroeconomic stabilization theory emphasizes that rule-based automatic stabilizers substantially outperform discretionary interventions, which suffer from implementation lags [@auclert-rognlie-straub-2024; @kaplan-moll-violante-2018-hank]. Under technological uncertainty, state-contingent policy schedules indexed to verified structural shifts in national factor shares are strictly superior to fixed-calendar dates [@korinek-suh-2024; @cazzaniga-imf-2024]. In Spain's constitutional order, however, Articles 31.3 and 134.7 CE strictly prohibit delegating the establishment or modification of tax rates to executive agencies or independent authorities without parliamentary enactment (*Principio de Legalidad Tributaria*). AIReF's mandate under *Ley Orgánica 6/2013* [@boe-lo-6-2013-airef] is strictly non-binding and evaluative ('comply or explain'). Therefore, triggers must operate as mandatory statutory fast-tracks for legislative ratification. In housing, empirical literature confirms that public housing construction lags (4–7 years) cannot solve short-run cash-transfer rent capture, necessitating immediate fiscal-deduction and regulatory circuit-breakers [@garcia-montalvo-2023-rent-controls; @jofre-monseny-2023-rent-control].

## 4. Spain context & data sources
- **Independent Fiscal Governance:** *Autoridad Independiente de Responsabilidad Fiscal* (AIReF, statutory evaluation mandate under *Ley Orgánica 6/2013* [@boe-lo-6-2013-airef]), Banco de España, and INE National Accounts.
- **Constitutional & Fiscal Statutes:** *Constitución Española* (Arts. 31.3, 86, 134.7 CE [@boe-ce-1978]), *Ley Orgánica 2/2012 de Estabilidad Presupuestaria* (LOEPSF [@boe-loepsf-2012]), reformed EU fiscal framework (*Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework]), and *Ley 12/2023 por el derecho a la vivienda* [@boe-vivienda-2023].

## 5. Methods & identification
1. **The AIReF Technical Certification & Fast-Track Protocol ($I_{\text{AI},t}$):**
   - AIReF audits and certifies the multi-variable composite displacement index:
     $$I_{\text{AI},t} = \omega_1 \Delta \tilde{s}_{L,t} + \omega_2 u_{\text{cognitive},t} + \omega_3 \left(\frac{\Delta \text{EBE}_{\text{tech},t}}{\text{GDP}_t}\right)$$
     where $\Delta \tilde{s}_{L,t}$ is the cyclically adjusted labor share, $u_{\text{cognitive},t}$ is cognitive occupational displacement (`M01`), and $\Delta \text{EBE}_{\text{tech},t}$ is automation operating surplus (`M16`).
   - Trigger bands: $I_{\text{AI}} < 1.0 \implies \text{Phase 1 (Tier A)}$; $1.0 \le I_{\text{AI}} < 2.5 \implies \text{Phase 2 (Tier B)}$; $I_{\text{AI}} \ge 2.5 \implies \text{Phase 3 (Tier C)}$.
   - Upon certification, the statute mandates the Government to enact a Royal Decree-Law (*Real Decreto-ley* under Art. 86 CE) within 30 days submitted to the *Congreso de los Diputados* for immediate ratification, guaranteeing full compliance with Arts. 31.3 and 134.7 CE.
2. **The Housing Pass-Through Circuit-Breaker (`M05`):**
   - If quarterly rental index growth exceeds core CPI by >3.0 pp in designated *zonas de mercado residencial tensionado* (ZMRT), an immediate emergency package activates by statutory mandate:
     (i) Dynamic revocation of LIRPF Art. 23.2 landlord rental income deductions (dropping from 50% to 0% for non-compliant landlords),
     (ii) Statutory extension of price ceilings to seasonal (LAU Art. 3.2) and room rentals (CC Art. 1554),
     (iii) Fast-track municipal preferential acquisition rights (*tanteo y retracto*) on corporate-owned residential assets.
3. **Compound Tail-Risk Stress-Test Battery:**
   - *Stress 1 (Energy Stagflation + S2 AI Displacement):* 50% energy import price shock combined with $-7.0$ pp labor share collapse.
   - *Stress 2 (High-Income Tax Evasion Surge):* Elasticity of taxable income (ETI) doubling to $e = 0.50$ among the top 1% of earners.
   - *Stress 3 (Metropolitan Housing Supply Bottleneck):* Inelastic rental supply ($\varepsilon_s = 0.10$) accelerating rent pass-through to $45\%$ in Madrid and Barcelona.
   - *Stress 4 (Sovereign Debt Selloff):* 150 bps widening in Spain's 10-year sovereign bond spread under rising ECB policy rates.

## 6. Pilot implications
- **Municipal:** Valuable for field-testing local operational disconfirmation criteria (e.g. municipal registration bottlenecks or local service utilization spikes), but lacks the macroeconomic scale to evaluate national sovereign spreads, cyclically adjusted labor-share triggers, or currency-union inflation dynamics.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común*, regional debt limits under LOEPSF [@boe-loepsf-2012] require pilot funding to be structurally neutral; stress-testing must account for regional debt sustainability under CPFF oversight.
  - In *Régimen Foral* (Basque Country / Navarre), autonomous borrowing powers and the *Cupo* mechanism provide insulation against central budgetary freezes, allowing for high-stress experimental stability.
- **National:** The only jurisdictional level where the full AIReF composite trigger framework, the Fast-Track Parliamentary Ratification Protocol under Art. 86 CE, and EU fiscal rule compliance under *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] can be stress-tested against sovereign debt markets.

## 7. Risks, counterarguments & open issues
- **Counterargument (Democratic Deficit of Algorithmic Triggers):** Entrusting benefit levels and tax surcharges to automated mathematical formulas removes democratic accountability and violates Tax Legality (Arts. 31.3 and 134.7 CE). *Mitigation:* Under the reformed design, AIReF operates strictly within its organic evaluative mandate (LO 6/2013 [@boe-lo-6-2013-airef]) as an independent auditor issuing non-binding Technical Transition Reports. Concrete tax rates and benefit phase transitions are enacted via fast-track Royal Decree-Laws under Art. 86 CE and formally ratified by the *Congreso de los Diputados*.
- **Counterargument (Inflationary Inertia):** Cash transfers could create persistent wage-price spirals in a booming economy. *Mitigation:* The expedited countercyclical fiscal surcharge and the immediate Housing Circuit-Breaker act in real time to absorb excess purchasing power from high-income deciles and prevent rental inflation.

## 8. Deliverables & effort
- State-Contingent Transition Roadmap and AIReF Composite Trigger Certification Protocol.
- Quantitative Tail-Risk Stress-Test Suite and Disconfirmation Matrix for Chapter 8. (Effort: 5 person-weeks).
