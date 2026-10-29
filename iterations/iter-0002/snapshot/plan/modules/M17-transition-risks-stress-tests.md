---
id: M17
title: Transition path, scenario triggers, and tail-risk stress tests
status: draft
locked: false
depends_on: [M01, M03, M04, M05, M07, M10, M11, M16]
covers: [F17]
feeds_chapters: [8]
last_iteration: 1
---
# M17 · Transition path, scenario triggers, and tail-risk stress tests

## 1. Why this matters
Transitioning overnight from Spain's fragmented, means-tested welfare system to a universal Tier B or Tier C cash transfer would generate severe macroeconomic friction, inflationary risks, and fiscal deficit spikes. Conversely, an open-ended pilot without statutory scale-up rules risks political abandonment (`M11`). A state-of-the-art research plan must establish a phased, reversible **Transition Roadmap** governed by independent macroeconomic triggers, automatic fiscal circuit-breakers (`M03`, `M04`), and adversarial tail-risk stress tests.

## 2. Research questions
- **RQ-M17-01**: What phased sequencing—from Phase 0 (unification and automatic individualization of IMV + CAPI) to Phase 1 (Multi-Level Pilot `M10` and Tier A €600 floor under S1), Phase 2 (Tier B €900 poverty-line UBR under S2), and Phase 3 (Tier C €1,200 AI-dividend UBR under S3)—minimizes transition costs while maintaining structural fiscal balance?
  - *Hypothesis:* A state-contingent roadmap governed by an AIReF-certified **Cyclically and Terms-of-Trade-Adjusted Composite Displacement Index** ($I_{\text{AI},t}$) keeps the structural primary balance within $\pm 0.35\%$ of GDP throughout the transition while ensuring zero real disposable income loss for vulnerable cohorts via the `M07` guarantee.
- **RQ-M17-02**: How can automatic circuit-breakers—such as an **Automatic Fiscal Stabilization Surcharge** on upper IRPF brackets, core non-tradable inflation gaps, and Bonos-Bund sovereign spread triggers—cool short-run demand shocks and preserve fiscal stability under *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] without waiting for long-lag housing construction?
  - *Hypothesis:* Pre-committing to an automatic countercyclical IRPF surcharge (activating when domestic core inflation exceeds the Eurozone average by $>1.2$ pp or sovereign spreads widen by $>75$ bps) stabilizes aggregate demand within two quarters, shielding the macroeconomic currency-union transmission channel (`M04`).

## 3. State of knowledge
Macroeconomic stabilization theory emphasizes that rule-based automatic stabilizers substantially outperform discretionary legislative interventions, which suffer from severe legislative and implementation lags [@auclert-rognlie-straub-2024; @kaplan-moll-violante-2018-hank]. Under technological uncertainty, state-contingent policy schedules indexed to verified structural shifts in national factor shares are strictly superior to fixed-calendar dates [@korinek-suh-2024; @cazzaniga-imf-2024]. In a monetary union, tail-risk fiscal stress tests must explicitly incorporate sovereign spread dynamics and compliance with statutory expenditure ceilings (*Ley Orgánica 2/2012* LOEPSF [@boe-loepsf-2012] and EU fiscal rules [@eu-reg-2024-1263-fiscal-framework]).

## 4. Spain context & data sources
- **Independent Fiscal Governance:** *Autoridad Independiente de Responsabilidad Fiscal* (AIReF, statutory mandate under *Ley Orgánica 6/2013* to evaluate macroeconomic forecasts and public policies), Banco de España, and INE National Accounts.
- **Fiscal Framework Statutes:** *Ley Orgánica 2/2012 de Estabilidad Presupuestaria y Sostenibilidad Financiera* (LOEPSF [@boe-loepsf-2012]), reformed EU fiscal framework (*Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework]), and the *Consejo de Política Fiscal y Financiera* (CPFF).

## 5. Methods & identification
1. **The AIReF-Certified Composite Displacement Trigger ($I_{\text{AI},t}$):**
   - To prevent energy price shocks or terms-of-trade fluctuations from falsely triggering technological transition tiers, specify a multi-variable index:
     $$I_{\text{AI},t} = \omega_1 \Delta \tilde{s}_{L,t} + \omega_2 u_{\text{cognitive},t} + \omega_3 \left(\frac{\Delta \text{EBE}_{\text{tech},t}}{\text{GDP}_t}\right)$$
     where $\Delta \tilde{s}_{L,t}$ is the cyclically adjusted labor share (filtering out oil and import-price shocks via the terms of trade), $u_{\text{cognitive},t}$ is the unemployment/underemployment rate in high-AI-exposure CNO-11 occupations (`M01`), and $\Delta \text{EBE}_{\text{tech},t}$ is the corporate surplus growth in digital/automation sectors (`M16`).
   - Trigger bands: $I_{\text{AI}} < 1.0 \implies \text{Phase 1 (Tier A)}$; $1.0 \le I_{\text{AI}} < 2.5 \implies \text{Phase 2 (Tier B)}$; $I_{\text{AI}} \ge 2.5 \implies \text{Phase 3 (Tier C)}$.
2. **Automatic Fiscal Stabilization Surcharge:**
   - Define an automatic tax lever: if domestic core inflation exceeds the Eurozone average by $>1.2$ pp for two consecutive quarters or the Bonos-Bund 10-year spread exceeds 150 bps, an emergency progressive surcharge ($\Delta \tau \in [1.0\%, 3.0\%]$) activates automatically on the top two IRPF brackets and corporate surplus contributions (`M16`), curbing excess consumption demand without curtailing baseline UBR transfers.
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
- **National:** The only jurisdictional level where the full AIReF composite trigger framework, the Automatic Fiscal Stabilization Surcharge, and EU fiscal rule compliance under *Regulation (EU) 2024/1263* [@eu-reg-2024-1263-fiscal-framework] can be stress-tested against sovereign debt markets.

## 7. Risks, counterarguments & open issues
- **Counterargument (Democratic Deficit of Algorithmic Triggers):** Entrusting benefit levels and tax surcharges to automated mathematical formulas removes democratic accountability. *Mitigation:* The trigger formulas are enacted through Organic Law voted by Parliament; AIReF's role is strictly that of an independent technical certifying body (auditing calculations), with Parliament retaining the power to debate and confirm phase transitions.
- **Counterargument (Inflationary Inertia):** Cash transfers could create persistent wage-price spirals in a booming economy. *Mitigation:* The Automatic Fiscal Stabilization Surcharge acts in real time to absorb excess purchasing power from high-income deciles, preventing overheating.

## 8. Deliverables & effort
- State-Contingent Transition Roadmap and AIReF Composite Trigger Certification Protocol.
- Quantitative Tail-Risk Stress-Test Suite and Disconfirmation Matrix for Chapter 8. (Effort: 5 person-weeks).
