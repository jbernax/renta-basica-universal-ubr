# Cross-Cutting Methodological Architecture (`methods.md`)

This document specifies the five core analytical pillars linking the 17 modules (`M01`–`M17`) into a closed, internally consistent research pipeline.

## 1. Task-Based AI Exposure & Labor-Share Projections (`M01`, `M08`, `M16`)
- **Occupational Mapping:** Crosswalk US O*NET task exposure indices (Eloundou et al. $\beta$-exposure [@eloundou-2024-gpts], Felten AIOE [@felten-2021-aioe], Webb patent-task overlap [@webb-2020-ai], and ILO Gen-AI scores [@gmyrek-ilo-2023]) to ISCO-08 and Spain's 3-digit *Clasificación Nacional de Ocupaciones* (CNO-11) using INE *Encuesta de Población Activa* (EPA) microdata.
- **Task Displacement vs. Reinstatement Model:** Calibrate an Acemoglu-Restrepo task-allocation framework [@acemoglu-restrepo-2019; @acemoglu-2024-macro-ai] to Spanish sectoral production functions (Contabilidad Nacional, INE) and administrative social security histories (*Muestra Continua de Vidas Laborales*, MCVL) to derive scenario paths **S1**, **S2**, and **S3** [@korinek-suh-2024; @cazzaniga-imf-2024].

## 2. Static & Behavioral Tax-Benefit Microsimulation (`M02`, `M03`, `M07`, `M09`, `M14`)
- **EUROMOD-Spain Backbone:** Implement UBR Tiers A, B, and C inside EUROMOD-Spain [@sutherland-figari-2013-euromod] running on INE's *Encuesta de Condiciones de Vida* (ECV) cross-validated with the *Instituto de Estudios Fiscales* (IEF) / AEAT *Muestra de Declarantes de IRPF* and *Panel de Hogares*.
- **Joint Tax-Transfer Schedule:** Simulate abolishing the current IRPF *mínimo personal y familiar* [@boe-irpf-2006] and replacing means-tested cash benefits (`M07`, subject to a strict **No-Loser Guarantee** for disability and high-need households) with a unified marginal rate schedule, computing exact gross vs. net fiscal cost, decile winners/losers, Gini, S80/S20, and AROPE poverty impacts.
- **Behavioral Labor-Supply Module:** Embed discrete-choice structural labor supply elasticities (intensive and extensive margins calibrated from Spanish MCVL/ECV and experimental literature [@saez-2002-optimal-transfers; @vivalt-2024-openresearch; @jones-marinescu-2022]) to compute second-round revenue and poverty effects.

## 3. Open-Economy HANK General-Equilibrium Closure (`M03`, `M04`, `M05`, `M16`, `M17`)
- **Heterogeneous-Agent New Keynesian (HANK) Model for Spain:** Build a small-open-economy monetary-union HANK model [@kaplan-moll-violante-2018-hank; @auclert-rognlie-straub-2024] calibrated to Spanish liquid/illiquid wealth distributions (Banco de España *Encuesta Financiera de las Familias*, EFF) and decile-specific marginal propensities to consume (MPCs).
- **Tradable vs. Non-Tradable & Housing Sector Split:** Separate tradable goods (Eurozone price-taking, import leakage) from non-tradable services and inelastic urban rental housing (`M05` [@fack-2006-housing-benefits; @diamond-mcquade-qian-2019-rent]) to quantify when UBR acts as a non-inflationary demand stabilizer (offsetting AI wage compression in S2/S3) versus when it triggers domestic shelter/service inflation or sovereign spread widening.

## 4. Multi-Level Experimental & Quasi-Experimental Identification (`M05`, `M08`, `M10`, `M15`)
- **Two-Stage Randomized Saturation Design:** Combine individual-level randomization (identifying partial-equilibrium labor, health, and consumption responses [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health]) with municipality/census-tract cluster saturation variation (identifying local general-equilibrium rent pass-through, wage bargaining, and consumption multipliers [@egger-2022-ge-kenya; @todeschini-bmincome-2020]).
- **Simulated Net-Tax Arm in Foral / Regional Pilots:** Where regional fiscal competence allows (e.g. Basque Country / Navarre or State-delegated IRPF pilot), test both net-recipient and tax-clawback arms to overcome the classic pilot flaw of testing unfinanced transfers [@hoynes-rothstein-2019; @kangas-2021-finland].

## 5. Constitutional, Statutory, and Political-Economy Veto Analysis (`M06`, `M11`, `M12`, `M13`)
- **Doctrinal & Competence Stress-Test:** Map every statutory reform required across the Spanish Constitution [@boe-ce-1978], LOFCA [@boe-lofca-1980], Ley del IRPF [@boe-irpf-2006], Ley del IMV [@boe-imv-2021], and EU Regulation 883/2004 [@eu-reg-883-2004].
- **Conjoint Survey & Coalition Modeling:** Pair CIS public-opinion microdata with a pre-registered conjoint survey experiment testing multidimensional UBR packages (benefit level, tax source, residency rule, AI-dividend framing) across Spanish partisan and territorial cleavages.
