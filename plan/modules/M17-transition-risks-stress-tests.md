---
id: M17
title: Transition path, scenario triggers, and tail-risk stress tests
status: draft
locked: false
depends_on: [M01, M03, M04, M05, M07, M10, M11, M16]
covers: [F17]
feeds_chapters: [8]
last_iteration: 3
---
# M17 · Transition path, scenario triggers, and tail-risk stress tests

## 1. Why this matters
Transitioning overnight from Spain's fragmented, means-tested welfare system to a universal Tier B or Tier C cash transfer would generate severe macroeconomic friction, inflationary risks, and fiscal deficit spikes. Conversely, an open-ended pilot without statutory scale-up rules risks political abandonment (`M11`). A state-of-the-art research plan must establish a phased, reversible **Transition Roadmap** governed by independent macroeconomic triggers, automatic fiscal and housing circuit-breakers (`M03`, `M05`), and adversarial tail-risk stress tests. Crucially, transition governance must fully respect the constitutional Principle of Tax Legality (Arts. 31.3 and 134.7 CE [@boe-ce-1978]) and Constitutional Court doctrine prohibiting the delegation or establishment of tax surcharges via decree-law (STC 73/2017 [@stc-73-2017]; STC 78/2020 [@stc-78-2020]). Technical certifications by AIReF under *Ley Orgánica 6/2013* [@boe-lo-6-2013-airef] must trigger pre-enacted statutory automatic stabilizers or expedited parliamentary bills (*urgencia parlamentaria*) rather than unconstitutional administrative tax decrees.

## 2. Research questions
- **RQ-M17-01**: What phased sequencing—from Phase 0 (unification and automatic individualization of IMV + CAPI) to Phase 1 (Multi-Level Pilot `M10` and Tier A €600 floor under S1), Phase 2 (Tier B €900 poverty-line UBR under S2), and Phase 3 (Tier C €1,200 AI-dividend UBR under S3)—minimizes transition costs while maintaining structural fiscal balance?
  - *Hypothesis:* A state-contingent roadmap governed by an AIReF-certified **Cyclically and Terms-of-Trade-Adjusted Composite Displacement Index** ($I_{\text{AI},t}$) triggering pre-legislated statutory rate schedules and fast-track parliamentary urgency (Art. 93 Reglamento del Congreso) keeps the structural primary balance within $\pm 0.35\%$ of GDP throughout the transition while ensuring zero real disposable income loss for vulnerable cohorts via the `M07` guarantee, in full compliance with STC 73/2017 [@stc-73-2017].
- **RQ-M17-02**: How can immediate fiscal and housing circuit-breakers—specifically the **Housing Pass-Through Circuit-Breaker** (`M05`) and statutory demand-cooling stabilizers—suppress short-run inflationary shocks under *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] without relying on boycotted regional declarations?
  - *Hypothesis:* When high-frequency rental nowcasting registers annualized rent growth exceeding core CPI by >3.0 pp in urban markets (rent-to-income >30%), triggering an immediate **Objective Federal Fiscal Benchmark** (withdrawing LIRPF Art. 23.2 landlord tax deductions from 50% to 0% under State tax powers Art. 149.1.14 CE, independent of regional ZMRT declarations under STC 79/2024 [@stc-79-2024-vivienda]) and activating the *Fondo de Estabilización Residencial* (FER) for municipal preemption (*tanteo y retracto*) suppresses rental inflation by >65% within two quarters.

## 3. State of knowledge
Macroeconomic stabilization theory emphasizes that rule-based automatic stabilizers substantially outperform discretionary interventions, which suffer from implementation lags [@auclert-rognlie-straub-2024; @kaplan-moll-violante-2018-hank]. Under technological uncertainty, state-contingent policy schedules indexed to verified structural shifts in national factor shares are strictly superior to fixed-calendar dates [@korinek-suh-2024; @cazzaniga-imf-2024]. In Spain's constitutional order, Articles 31.3 and 134.7 CE strictly prohibit delegating the establishment or modification of tax rates to executive agencies or independent authorities (*Principio de Legalidad Tributaria*), and the Constitutional Court has firmly established that *Real Decretos-leyes* cannot alter the essential elements of the tax system or introduce tax surcharges (STC 73/2017 [@stc-73-2017]; STC 78/2020 [@stc-78-2020]). AIReF's mandate under *Ley Orgánica 6/2013* [@boe-lo-6-2013-airef] is strictly non-binding and evaluative. Therefore, triggers must operate via pre-enacted statutory formulas or fast-track parliamentary consideration. In housing, empirical literature confirms that public housing construction lags (4–7 years) cannot solve short-run cash-transfer rent capture, necessitating high-frequency nowcasting and federal fiscal circuit-breakers [@garcia-montalvo-2023-rent-controls; @jofre-monseny-2023-rent-control; @khametshin-2024-rental].

## 4. Spain context & data sources
- **Independent Fiscal Governance:** *Autoridad Independiente de Responsabilidad Fiscal* (AIReF, statutory evaluation mandate under *Ley Orgánica 6/2013* [@boe-lo-6-2013-airef]), Banco de España, and INE National Accounts.
- **Constitutional & Fiscal Statutes:** *Constitución Española* (Arts. 31.3, 134.7, 149.1.14 CE [@boe-ce-1978]), jurisprudence of the Constitutional Court on tax legality (STC 73/2017 [@stc-73-2017]; STC 78/2020 [@stc-78-2020]), *Ley Orgánica 2/2012 de Estabilidad Presupuestaria* (LOEPSF [@boe-loepsf-2012]), and reformed EU fiscal framework (*Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework]).
- **Housing Jurisprudence & Market Spine:** *Ley 12/2023 por el derecho a la vivienda* [@boe-vivienda-2023], STC 79/2024 on regional housing competence [@stc-79-2024-vivienda], Banco de España rental market evidence [@khametshin-2024-rental], and regional tenancy deposit registries (INCASÒL, IVIMA, AVRA).

## 5. Methods & identification
1. **The AIReF Technical Certification & Statutory Fast-Track Protocol ($I_{\text{AI},t}$):**
   - AIReF audits and certifies the multi-variable composite displacement index:
     $$I_{\text{AI},t} = \omega_1 \Delta \tilde{s}_{L,t} + \omega_2 u_{\text{cognitive},t} + \omega_3 \left(\frac{\Delta \text{EBE}_{\text{tech},t}}{\text{GDP}_t}\right)$$
     where $\Delta \tilde{s}_{L,t}$ is the cyclically adjusted labor share, $u_{\text{cognitive},t}$ is cognitive occupational displacement (`M01`), and $\Delta \text{EBE}_{\text{tech},t}$ is automation operating surplus (`M16`).
   - Trigger bands: $I_{\text{AI}} < 1.0 \implies \text{Phase 1 (Tier A)}$; $1.0 \le I_{\text{AI}} < 2.5 \implies \text{Phase 2 (Tier B)}$; $I_{\text{AI}} \ge 2.5 \implies \text{Phase 3 (Tier C)}$.
   - Upon certification, pre-legislated statutory adjustment formulas activate automatically, or the Government tables a fast-track statutory bill under expedited parliamentary urgency (*urgencia parlamentaria*, Art. 93 Reglamento del Congreso), ensuring absolute fidelity to Arts. 31.3 and 134.7 CE and STC 73/2017 [@stc-73-2017].
2. **The High-Frequency Housing Pass-Through Circuit-Breaker (`M05`):**
   - Ingest data from the High-Frequency Rental Nowcasting Spine (monthly tenancy deposits and scraped listing APIs with $\le 30$-day latency [@khametshin-2024-rental]).
   - If annualized rental inflation exceeds core CPI by >3.0 pp in urban markets where rent-to-income exceeds 30%, activate the **Objective Federal Fiscal Benchmark** under Art. 149.1.14 CE:
     (i) Revocation of LIRPF Art. 23.2 landlord rental income deductions (dropping from 50% to 0% for non-compliant landlords, independent of regional ZMRT declarations under STC 79/2024 [@stc-79-2024-vivienda]),
     (ii) Extension of price ceilings to seasonal (LAU Art. 3.2) and room rentals,
     (iii) Mobilize municipal liquidity under the *Fondo de Estabilización Residencial* (FER) via ICO credit lines, with statutory exemption from LOEPSF expenditure limits for emergency municipal preemption (*tanteo y retracto*).
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
- **National:** The only jurisdictional level where the full AIReF composite trigger framework, the pre-enacted statutory tax stabilizers, and EU fiscal rule compliance under *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] can be stress-tested against sovereign debt markets.

## 7. Risks, counterarguments & open issues
- **Counterargument (Democratic Deficit and Tax Legality Infringement):** Entrusting tax rates to executive decree-laws violates the Principle of Tax Legality (Arts. 31.3 and 134.7 CE; STC 73/2017 [@stc-73-2017]; STC 78/2020 [@stc-78-2020]). *Mitigation:* Under the reformed design, executive decree-law tax surcharges are strictly excised. AIReF operates solely within its evaluative mandate (LO 6/2013 [@boe-lo-6-2013-airef]) issuing technical audit reports that trigger pre-enacted statutory mathematical schedules or expedited congressional votes under Art. 93 Reglamento del Congreso.
- **Counterargument (Regional Boycott of Housing Controls):** Autonomous communities governed by opposition parties refuse to declare ZMRTs (STC 79/2024 [@stc-79-2024-vivienda]). *Mitigation:* The circuit-breaker bypasses regional declarations by conditioning federal IRPF landlord deductions on an Objective Federal Fiscal Benchmark governed by State tax authority (Art. 149.1.14 CE).

## 8. Deliverables & effort
- State-Contingent Transition Roadmap and AIReF Composite Trigger Certification Protocol (STC 73/2017 Compliant).
- Quantitative Tail-Risk Stress-Test Suite and High-Frequency Housing Circuit-Breaker Blueprint for Chapter 8. (Effort: 5 person-weeks).
