---
id: M17
title: Transition path, scenario triggers, and tail-risk stress tests
status: draft
locked: false
depends_on: [M01, M03, M04, M05, M07, M10, M11, M16]
covers: [F17]
feeds_chapters: [8]
last_iteration: 0
---
# M17 · Transition path, scenario triggers, and tail-risk stress tests

## 1. Why this matters
Moving from Spain's current welfare state directly to a full Tier B/C Universal Basic Rent overnight would create severe administrative, fiscal, and macroeconomic friction. Conversely, an open-ended pilot with no statutory scale-up rules risks political stalling (`M11`). A state-of-the-art research plan must specify a reversible, rule-governed **Phased Transition Roadmap** with quantitative macroeconomic triggers linking `M01` AI displacement indicators to benefit and tax tiers, alongside automatic fiscal and inflation circuit-breakers (`M04`, `M05`).

## 2. Research questions
- **RQ-M17-01**: What staged sequencing—from Phase 0 (automatic individualization and take-up reform of IMV + CAPI + IRPF refundable credits) to Phase 1 (Multi-Level Pilot `M10` + Tier A €600 floor under S1), Phase 2 (Tier B €900 poverty-line UBR under S2), and Phase 3 (Tier C €1,200 AI-dividend UBR under S3)—minimizes transitional welfare losses and fiscal deficit spikes?
  - *Hypothesis:* A four-phase rule-based rollout anchored to observable quarterly indicators (EPA cognitive-displacement index, labor-share $\Delta s_L$, and net fiscal neutrality) keeps the structural primary balance within $\pm 0.4\%$ of GDP throughout the transition while guaranteeing zero welfare losses via the `M07` supplement.
- **RQ-M17-02**: Which automatic statutory circuit-breakers (core non-tradable inflation gap vs. Eurozone, urban rental pass-through index, and Bonos-Bund sovereign spread) effectively bound tail risks without undermining household income certainty?
  - *Hypothesis:* Pre-committing to symmetric indexation rules—where nominal UBR step-ups pause or redirect into social housing supply (`M05`) if domestic non-tradable CPI exceeds the Eurozone average by $>1.5$ pp or urban rent pass-through exceeds $20\%$—prevents inflationary spirals while preserving the nominal cash floor.

## 3. State of knowledge
Mechanism design for macroeconomic stabilization emphasizes rule-based automatic stabilizers over discretionary legislative packages, which suffer from recognition and implementation lags [@auclert-rognlie-straub-2024; @kaplan-moll-violante-2018-hank]. Scenario planning for transformative AI [@korinek-suh-2024; @cazzaniga-imf-2024] highlights high uncertainty over arrival speed, making state-contingent policy schedules (policies indexed to realized labor-share and task-displacement thresholds) strictly superior to fixed-calendar commitments.

## 4. Spain context & data sources
- **Institutional Governance & Fiscal Watchdogs:** *Autoridad Independiente de Responsabilidad Fiscal* (AIReF, statutory mandate under *Ley Orgánica 6/2013* to audit fiscal sustainability and evaluate IMV), Banco de España, INE quarterly national accounts, and the *Consejo de Política Fiscal y Financiera* (CPFF).

## 5. Methods & identification
1. **State-Contingent Policy Rule Specification:** Define formal mathematical trigger functions mapping quarterly INE/Seguridad Social indicators $(\Delta s_{L,t}, u_{\text{AI},t}, \pi_{\text{NT},t}, \text{Spread}_t)$ to the active UBR tier and `M03`/`M16` tax parameters.
2. **Adversarial Tail-Risk Stress Testing:** Subject the integrated EUROMOD (`M03`, `M09`) + HANK (`M04`) pipeline to four compound stress scenarios:
   - *Stress 1 (Stagflationary Energy/Geopolitical Shock + S2):* Imported energy price spike coinciding with AI displacement.
   - *Stress 2 (Capital Flight / Tax Evasion Surge):* High-income taxable income elasticity (ETI) double the baseline estimate.
   - *Stress 3 (Metropolitan Rent Surge):* Urban rental supply elasticity half the baseline (`M05`).
   - *Stress 4 (Asymmetric Regional Shock):* Severe service-sector displacement in Madrid/Catalonia alongside tourism boom in coastal regions.

## 6. Pilot implications
- **Pre-Committed Scale-Up & Disconfirmation Criteria (`counterarguments`):** Specify exact quantitative thresholds from the `M10` pilot that either **confirm** readiness for Phase 2 scale-up (e.g. formal labor participation drop $<3$ pp, rent pass-through $<15\%$, net administrative take-up $>95\%$) or **disconfirm** a design feature and trigger mandatory redesign.

## 7. Risks, counterarguments & open issues
- **Counterargument (Time-Inconsistency & Political Manipulation of Triggers):** Governments may override fiscal circuit-breakers before elections. *Mitigation:* Vest trigger certification in AIReF as an independent statutory fiscal council under Organic Law.

## 8. Deliverables & effort
- Phased Implementation Roadmap (Phase 0 to Phase 3) & AIReF Trigger Certification Charter.
- Four-Scenario Tail-Risk Stress-Test Matrix & Disconfirmation Criteria Table for Chapter 8. (Effort: 5 person-weeks).
