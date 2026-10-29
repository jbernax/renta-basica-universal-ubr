# Research Plan Improvement Report

**Status:** `continue`

**Reasons / SOTA gates:**
- 2/3 iterations in this cycle
- 2 open critical issue(s)

## Score History

| Iteration | Weighted | Delta | Min Criterion | Open Critical | Coverage | Verified Sources |
|---|---:|---:|---:|---:|---:|---:|
| `iter-0001` | **4.65** | — | 4.40 | 0 | 100% | 100% |
| `iter-0002` | **4.81** | +0.16 | 4.70 | 2 | 100% | 100% |

## Rubric Breakdown (`iter-0002`)

| Criterion | Weight | Score | Delta |
|---|---:|---:|---:|
| Coverage of factors (`coverage`) | 0.12 | 4.80 | +0.20 |
| Research question quality (`rq_quality`) | 0.12 | 4.80 | +0.10 |
| Methodological rigor (`methodological_rigor`) | 0.14 | 4.80 | +0.20 |
| Evidence grounding (`evidence_grounding`) | 0.12 | 4.80 | +0.10 |
| Spain institutional fit (`spain_fit`) | 0.12 | 4.90 | +0.10 |
| Treatment of AI-displacement scenarios (`ai_scenarios`) | 0.08 | 4.80 | +0.30 |
| Feasibility (data, time, budget) (`feasibility`) | 0.08 | 4.70 | +0.30 |
| Internal coherence (`internal_coherence`) | 0.08 | 4.80 | +0.10 |
| Counterarguments and risks (`counterarguments`) | 0.08 | 4.80 | +0.10 |
| Ethics and equity (`ethics_equity`) | 0.06 | 4.90 | +0.10 |

## Latest Iteration Details (`iter-0002`)

### Judge Assessment

The Universal Basic Rent (Spain) research plan in Iteration 2 represents an exceptionally mature, scientifically rigorous, and institutionally grounded blueprint. Across all 10 rubric dimensions, the plan achieves a weighted score of 4.81 out of 5.0, reflecting field-defining research question design, frontier empirical and macroeconomic methodologies, and exhaustive institutional alignment with Spanish constitutional, statutory, and territorial frameworks. Key methodological and architectural strengths include the closed 4-stage micro-macro general-equilibrium pipeline linking EUROMOD-Spain and open-economy HANK; the two-stage spatial saturation pilot design with explicit MDE power calculations and bunching econometrics; the resolution of complex constitutional, foral, and EU-law hurdles (conforming to STC 158/2021, STC 19/2024, the Concierto Vasco, Directive 2004/38/EC, and the CJEU Schumacker doctrine); and an exemplary ethical architecture incorporating an inviolable No-Loser Guarantee, additive disability supplements, and last-mile administrative delivery protections. The identified critical issues represent actionable refinements for cross-border B2B compute tax enforcement and commuting-flow spillover controls rather than structural impediments. The plan stands at the threshold of academic publication readiness in leading economics and policy venues and provides an audit-ready evaluation template for Spanish fiscal and social institutions (AIReF, IEF, and the Ministries of Inclusion and Finance).

### Open Critical Issues

- **JD-02-01** (M16): Cross-border B2B compute tax enforcement vulnerability under OECD double-taxation treaties: While M16 specifies origin-based surplus taxation on domestic firms and destination digital services taxes, foreign AI foundation-model providers lacking a physical permanent establishment in Spain can contest direct corporate tax withholding on cloud compute subscriptions under existing bilateral tax treaties (CDIs modeled on OECD Arts. 7 and 12). The module should formalize a domestic B2B reverse-charge withholding mechanism under the Spanish General Tax Law to ensure collection resilience.
- **JD-02-02** (M10): Residual spatial commuting contamination across SUTVA buffer boundaries in metropolitan pilot clusters: Although M10 enforces 2–5 km geographic buffer zones and donut matching, daily inter-cluster labor commuting and consumer shopping between treated and control units in high-density metropolitan areas could still introduce indirect general-equilibrium wage or retail price spillovers. The econometric specification should explicitly incorporate a commuting-flow spatial weight matrix using mobile-phone mobility microdata (INE Estudio de Movilidad) to filter residual interference.

### Latest Changelog

# Changelog — Iteration 0002 (`iter-0002`)

## Overview
Iteration 0002 resolved critical institutional, econometric, constitutional, housing, and social-policy vulnerabilities identified across 5 specialist reviews (`social-policy`, `evaluation-methodologist`, `housing-economist`, `political-economist`, and `red-team`). A total of 9 high-leverage synthesis proposals (`SYN-02-01` through `SYN-02-09`) were executed across `plan/00-scope.md`, `plan/methods.md`, 12 factor modules (`plan/modules/M01`, `M02`, `M03`, `M05`, `M06`, `M07`, `M08`, `M09`, `M10`, `M11`, `M12`, `M13`, `M14`, `M15`, `M16`, `M17`), and `plan/sources.yaml`.

All 86 cited academic papers, statutory texts, and legal rulings are 100% machine-verified over HTTP or official gazette repositories. 100% of reference factors (F01–F17) remain covered with 0 errors and 0 warnings.

---

## Applied Changes by Proposal

### `SYN-02-01` · Macro-Micro Fiscal Loop & S2/S3 Baseline Tax Erosion
- **Contributing Issues:** `RT-02-01` (critical), `RT-02-04` (major)
- **Target Files:**
  - `plan/00-scope.md`
  - `plan/methods.md`
  - `plan/modules/M01-ai-labor-displacement.md`
  - `plan/modules/M03-fiscal-financing.md`
  - `plan/modules/M16-ai-rent-capture-sovereign-fund.md`
- **Summary of Changes:**
  - In `methods.md` and `M03`, closed the feedback loop between macroeconomic displacement and micro tax simulation: mandated that EUROMOD-Spain runs directly on counterfactual post-displacement wage and employment distributions generated by M01/HANK across S1, S2, and S3, rather than unadjusted static survey weights.
  - In `M01` and `M03`, explicitly incorporated the 11.55% of GDP baseline tax revenue collapse under S2 into the consolidated Administraciones Públicas fiscal bridge, specifying that baseline public services (~€125B/year) must be co-financed by expanding corporate automation surplus taxes (`M16`), consumption taxes, and wealth levies as the labor tax base contracts.
  - In `M16`, clarified that the Sovereign AI Dividend Fund is an intergenerational capital buffer yielding 0.5–0.8% of GDP/year, which buffers transition costs but cannot fund the entirety of Tier C, requiring broad-base corporate automation surplus taxes.
- **Sources Cited:** `acemoglu-2024-macro-ai`, `korinek-suh-2024`, `hoynes-rothstein-2019`.

### `SYN-02-02` · Spatial Saturation Buffers, SUTVA, and Clawback Kink Econometrics
- **Contributing Issues:** `EM-02-01` (critical), `EM-02-02` (critical), `RT-02-02` (critical)
- **Target Files:**
  - `plan/methods.md`
  - `plan/modules/M08-labor-supply-behavior.md`
  - `plan/modules/M10-pilot-evaluation-design.md`
- **Summary of Changes:**
  - Redefined cluster randomization units in `M10` and `methods.md` from narrow, porous urban census tracts to economically self-contained spatial units: distinct small municipalities (1,500–5,000 residents) in non-metropolitan areas and transit-bounded districts in urban zones, enforcing mandatory geographic buffer zones ($\ge 2\text{--}5$ km in rural/peri-urban settings; donut matching in urban areas) per Baird et al. (2018) and Duflo et al. (2007) to prevent SUTVA spatial contamination.
  - Formulated the explicit cluster MDE formula parameterized with Spanish empirical priors ($\rho_{\text{rent}} = 0.08$, $\rho_{\text{labor}} = 0.03$, cluster size $m \approx 285$ adults, $R^2 \approx 0.35$ from pre-trial INCASÒL/MCVL microdata).
  - Addressed the clawback threshold kink ($Y^* = \text{UBR} / \tau_{\text{clawback}}$): stratified experimental samples into baseline earnings domains and integrated a pre-registered bunching estimator (Saez 2010; Chetty et al. 2012) around $Y^*$ to estimate compensated substitution elasticities directly from excess mass, explicitly acknowledging that upper-decile tax responses are estimated quasi-experimentally via administrative IRPF panel reforms (`M08`).
- **Sources Cited:** `baird-2018-interference`, `duflo-2007-randomization`, `saez-2010-bunching`, `chetty-2012-bounds`.

### `SYN-02-03` · Administrative Register Linkage, Tax Secrecy & Last-Mile Inclusion
- **Contributing Issues:** `EM-02-03` (major), `SP-02-04` (major), `RT-02-03` (major)
- **Target Files:**
  - `plan/modules/M10-pilot-evaluation-design.md`
  - `plan/modules/M12-administration-delivery.md`
- **Summary of Changes:**
  - In `M10`, solved the tax secrecy hurdle under Art. 95 Ley General Tributaria (LGT) and LOPDGDD by designing a model statutory habilitation provision (Disposición Adicional) declaring the pilot of high public interest under Art. 95.1.k LGT. To prevent differential control group consent attrition, instituted an unconditional Evaluation Participation Stipend (€250–€300/year) for control participants, and implemented cryptographic HMAC-SHA256 salted hashing for register pseudonymization.
  - In `M12`, established the Last-Mile Social Inclusion & Public Rail Protocol: codified *Empadronamiento Social de Oficio* to bypass municipal Padrón gatekeeping for unhoused and precariously housed residents under the Technical Instructions of 17 February 2020 (BOE 2 May 2020), and created a public payment delivery rail via *Correos* and Banco de España with statutory immunity from commercial AML/KYC freezes under Ley 10/2010.
- **Sources Cited:** `boe-lgt-2003`, `boe-lopdgdd-2018`.

### `SYN-02-04` · Housing Law, LAU Tenure Lock-In, Seasonal Leases & Closed-Loop Rent Recycling
- **Contributing Issues:** `HE-02-01` (critical), `HE-02-03` (major), `HE-02-04` (critical), `RT-02-06` (minor)
- **Target Files:**
  - `plan/modules/M05-housing-rent-capture.md`
  - `plan/modules/M09-distribution-poverty-euromod.md`
  - `plan/modules/M17-transition-risks-stress-tests.md`
- **Summary of Changes:**
  - In `M05`, formulated a dual-tenure equilibrium framework modeling LAU Art. 9 mandatory 5-year lease stability for incumbent tenants vs. new contracts, and addressed contract-substitution loopholes (landlords shifting to seasonal leases under LAU Art. 3.2 or room rentals under CC Art. 1554 to bypass Ley 12/2023 caps). Conditioned LIRPF Art. 23.2 deductions on long-term habitual residence contracts adhering to reference price limits.
  - In `M09`, disaggregated households across 4 distinct housing tenure regimes (outright owners, mortgaged owners, subsidized renters, market renters) and implemented closed-loop rent recycling: aggregate landlord rent extraction is credited to landlord capital income in AEAT microdata and taxed under reformed IRPF (`M03`). Reported housing-cost overburden rates (>40% of disposable income) alongside headline poverty.
  - In `M17`, formally integrated the Housing Pass-Through Circuit-Breaker promised by `M05` (activating if quarterly rental index growth exceeds core CPI by >3.0 pp in stressed zones ZMRT). Replaced slow 4–7 year public housing construction triggers with immediate fiscal/regulatory levers: dynamic revocation of LIRPF Art. 23.2 landlord deductions (50% to 0%), emergency extension of price caps to seasonal/room rentals, and municipal fast-track *tanteo y retracto* housing acquisitions.
- **Sources Cited:** `garcia-montalvo-2023-rent-controls`, `jofre-monseny-2023-rent-control`, `boe-lau-1994`.

### `SYN-02-05` · Constitutional Tax Legality of Triggers & Bicameral Veto-Player Architecture
- **Contributing Issues:** `PE-02-01` (critical), `PE-02-02` (critical), `PE-02-03` (major)
- **Target Files:**
  - `plan/methods.md`
  - `plan/modules/M11-political-economy.md`
  - `plan/modules/M16-ai-rent-capture-sovereign-fund.md`
  - `plan/modules/M17-transition-risks-stress-tests.md`
- **Summary of Changes:**
  - In `M17`, realigned transition triggers with the constitutional Principle of Tax Legality (Arts. 31.3 and 134.7 CE) and AIReF's statutory organic mandate under Ley Orgánica 6/2013. Repositioned AIReF strictly as an independent technical auditor issuing non-binding Technological Transition Reports ('comply or explain'). Replaced automatic administrative tax surcharges with a statutory Fast-Track Parliamentary Ratification Protocol under Art. 86 CE / Reglamento del Congreso mandating government decree-laws within 30 days of trigger certification.
  - In `M11`, embedded a formal bicameral veto-player framework (Tsebelis 2002) modeling spatial equilibria across both the Congreso and the Senado (specifically addressing the Senate's absolute veto over expenditure ceilings under LOEPSF Art. 15). Detailed concessions required for pro-business regionalist swing caucuses (PNV, Junts: decentralized tax tranches, SME surplus exemptions, transition fund co-management).
  - In `M11`, formalized tripartite social dialogue under Art. 7 CE and the CES (Ley 21/1991), establishing statutory non-supplantation clauses (UBR cannot be cited by employers to depress bargained wages or SMI hikes) and social partner co-governance of automation funds.
  - In `M16`, formalized statutory anti-raiding governance for the Sovereign AI Dividend Fund: independent management under Banco de España oversight, a 3/5ths congressional supermajority requirement for capital principal drawdown, and macro-fiscal debt parity rules modeled on Ley 28/2003.
- **Sources Cited:** `tsebelis-2002-veto-players`, `boe-lo-6-2013-airef`, `vanderborght-2006-trade-unions`, `vlandas-2019-politics-ubi`, `boe-ley-28-2003-fondo-reserva`.

### `SYN-02-06` · Asymmetric Fiscal Federalism, Regional Minimum Incomes & Single-Parent Protection
- **Contributing Issues:** `SP-02-01` (critical), `PE-02-04` (major)
- **Target Files:**
  - `plan/00-scope.md`
  - `plan/modules/M02-benefit-design.md`
  - `plan/modules/M06-constitutional-eu-law.md`
  - `plan/modules/M07-welfare-benefit-integration.md`
- **Summary of Changes:**
  - In `M07`, eliminated the erroneous assumption that regional minimum incomes (RGI/RGC) are abolished as a central dividend. Instead, codified a statutory *Complemento Autonómico No Contributivo* preserving regional entitlement rights and housing supplements (PEV/PCV in Euskadi/Navarre) that exceed the national UBR floor, holding all regional recipients strictly harmless.
  - In `M02` and `M07`, introduced an explicit *Complemento Monoparental y de Primera Infancia* (+€150–€200/month) so that single-parent families (81% female-headed) receiving the 22% IMV bonus and CAPI never suffer a disposable income loss under Tier A (€600 adult + €240 child vs. €965.55 IMV+CAPI baseline).
  - In `M06`, specified the bilateral methodology for the Basque *Cupo* (6.24%) and Navarrese *Aportación* (1.6%) by classifying national UBR as a non-assumed State power (*carga no asumida*), neutralizing territorial fiscal arbitrage, and established CPFF mechanisms to hold net-contributing common-regime regions harmless in public services.
- **Sources Cited:** `beramendi-2012-inequality`, `arcelus-bade-2015-rgi`.

### `SYN-02-07` · Universal Disability Supplement & Intra-Household Hidden Poverty Metrics
- **Contributing Issues:** `SP-02-02` (major), `SP-02-03` (major)
- **Target Files:**
  - `plan/00-scope.md`
  - `plan/modules/M02-benefit-design.md`
  - `plan/modules/M07-welfare-benefit-integration.md`
  - `plan/modules/M09-distribution-poverty-euromod.md`
  - `plan/modules/M14-gender-care-health.md`
- **Summary of Changes:**
  - In `M02`, `M07`, and `M14`, established the Universal Disability Supplement (*Complemento Universal por Discapacidad*) to offset non-discretionary economic extra costs of disability (€3,500–€10,000/yr). Graded by certified disability degree under Real Decreto 888/2022 (+25% UBR for 33–64%, +50% for 65–74%, +75–100% for $\ge 75\%$), fully additive to baseline UBR and distinct from SAAD in-kind care services under Ley 39/2006.
  - In `M09`, formulated an Individualized Poverty and Intra-Household Autonomy Metric (Ponthieux 2013) in EUROMOD to capture and quantify the eradication of hidden female and youth poverty within multi-earner households, alongside an empirical non-take-up calibration protocol (56% IMV non-take-up, 70% CAPI non-take-up per official AIReF opinions).
- **Sources Cited:** `ponthieux-2013-income-pooling`, `puig-segura-2021-discapacidad`, `boe-rd-888-2022-discapacidad`, `airef-opinion-imv-2023`, `airef-opinion-imv-2024`.

### `SYN-02-08` · EU Law Coordination: Regulation 883/2004 Exportability & Schumacker Doctrine
- **Contributing Issues:** `RT-02-05` (major), `PE-02-04` (major)
- **Target Files:**
  - `plan/methods.md`
  - `plan/modules/M06-constitutional-eu-law.md`
  - `plan/modules/M13-migration-territory-residency.md`
- **Summary of Changes:**
  - In `M06`, addressed the Regulation (EC) No 883/2004 Article 7 exportability challenge: legally anchored the non-contributory cash component as general social assistance governed strictly by Directive 2004/38/EC (falling outside Regulation 883/2004 Art. 3 material scope), or pursuing a formal Annex X coordination exemption.
  - In `M06` and `M13`, extended the Tax-Benefit Symmetry architecture to seasonal and frontier EU workers subject to Spain's Non-Resident Income Tax (*Impuesto sobre la Renta de No Residentes*, IRNR) to ensure full compliance with Article 45 TFEU and the landmark CJEU *Schumacker* doctrine (Case C-279/93).
- **Sources Cited:** `cjeu-c-279-93-schumacker`, `cjeu-c-475-03-banca-popolare-irap`, `boe-extranjeria-2000`.

### `SYN-02-09` · Frisch Elasticity Decomposition & Spatial Immobility Frictions
- **Contributing Issues:** `EM-02-04` (major), `HE-02-02` (major)
- **Target Files:**
  - `plan/methods.md`
  - `plan/modules/M13-migration-territory-residency.md`
  - `plan/modules/M15-international-evidence.md`
- **Summary of Changes:**
  - In `M15`, expanded the life-cycle structural transportability framework to formally separate windfall income effects ($\eta$) from Frisch intertemporal substitution ($\varepsilon^{\text{Frisch}}$) in finite-horizon trials (MaCurdy 1981; Blundell & MaCurdy 1999), calibrating the ratio $\varepsilon^c / \varepsilon^{\text{Frisch}} \in [0.4, 0.7]$ to prevent short-run trial sabbaticals from distorting permanent labor supply projections in EUROMOD and HANK.
  - In `M13`, re-specified the spatial discrete-choice location model to incorporate Spanish immobility frictions (tenure status, 6–10% regional ITP transfer taxes, and rural healthcare/amenity capital stocks per Antolín & Bover 1997), and paired portable UBR with rural housing rehabilitation subsidies and ITP exemptions.
- **Sources Cited:** `macurdy-1981-labor-supply`, `blundell-macurdy-1999-labor-supply`, `antolin-bover-1997-migration`.

---

## Validation & Quality Verification
- **Validator Status:** `.venv/bin/python -m ubr validate` passes with `0 error(s), 0 warning(s)`.
- **Metrics Status:** `.venv/bin/python -m ubr metrics` reports:
  `modules=17 (locked=0) rqs=41 coverage=100% (17/17) cited_sources=86/86 verified=100% words=18933 citations/1k=18.59`
- **Unit Tests:** `.venv/bin/python -m pytest` passes 68/68 tests in 0.49s.
