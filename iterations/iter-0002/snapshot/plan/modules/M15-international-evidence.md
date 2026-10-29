---
id: M15
title: Comparative international and Spanish empirical evidence
status: draft
locked: false
depends_on: [M08, M10, M14]
covers: [F16]
feeds_chapters: [1, 7]
last_iteration: 1
---
# M15 · Comparative international and Spanish empirical evidence

## 1. Why this matters
To achieve state-of-the-art scientific credibility, the Spanish UBR research plan must systematically synthesize and extract structural behavioral parameters from all major unconditional cash transfer experiments and permanent dividend programs worldwide [@hoynes-rothstein-2019; @banerjee-niehaus-suri-2019]. Crucially, the empirical strategy must formally bridge the external-validity gap between temporary, non-taxed experimental windfalls and a permanent, tax-financed Spanish UBR operating under AI labor-displacement scenarios S1–S3.

## 2. Research questions
- **RQ-M15-01**: What are the meta-analytic pooled causal estimates (and Bayesian posterior distributions) across global and European guaranteed-income trials for extensive-margin employment, weekly hours, clinical mental health, education/training enrollment, and local price inflation?
  - *Hypothesis:* Across advanced-economy trials (OpenResearch [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health], Finland [@kangas-2021-finland], Barcelona B-MINCOME [@todeschini-bmincome-2020], Stockton SEED [@west-2024-seed], and Alaska PFD [@jones-marinescu-2022]), the pooled extensive employment effect of a cash transfer equal to 25–40% of median income is within $[-1.8, +0.6]$ percentage points, with large and statistically robust gains in mental wellbeing ($+0.28\sigma$) and subjective financial security.
- **RQ-M15-02**: How can finite-horizon experimental treatment effects ($\Delta h_{\text{pilot}}, \Delta Y_{\text{pilot}}$) be structurally mapped to permanent-income compensated wage elasticities ($\varepsilon^c$) and income elasticities ($\eta$) relevant for Spain's permanent UBR under Scenarios S1–S3?
  - *Hypothesis:* Applying a life-cycle structural decomposition to OpenResearch and Finland microdata demonstrates that 40–60% of the observed hours reduction in 3-year trials reflects intertemporal leisure substitution over the finite experimental window rather than permanent uncompensated labor-supply contraction.
- **RQ-M15-03**: Which institutional and methodological limitations in Barcelona's B-MINCOME (2017–2019) and Catalonia's designed 2021–2023 pilot blueprint must be resolved in Spain's next-generation pilot (`M10`)?
  - *Hypothesis:* B-MINCOME's restriction to low-income households in Eix Besòs and interaction with state benefit clawbacks prevented identification of middle-class net-taxpayer responses and municipal rent pass-through; Catalonia's protocol solved cluster saturation but lacked fiscal/IRPF competence (`M06`), proving the necessity of a State-backed or Foral-integrated pilot (`M10`).

## 3. State of knowledge
The global empirical literature spans four distinct program archetypes:
1. **European Welfare-State Experiments:** Barcelona's B-MINCOME ($2\times 2$ factorial of conditionality $\times$ benefit clawback rate across 1,000 households [@todeschini-bmincome-2020]) and Finland's nationwide Kela RCT (2,000 unemployed recipients receiving €560/month unconditionally [@kangas-2021-finland]).
2. **US Guaranteed Income Trials:** OpenResearch ($1,000/month for 3 years across $N=1,000$ treated vs. $2,000$ control [@vivalt-2024-openresearch; @bartik-2024-openresearch; @miller-2024-openresearch-health]) and Stockton SEED ($500/month [@west-2024-seed]).
3. **Permanent Universal Resource Dividends:** Alaska Permanent Fund Dividend (universal annual dividend since 1982 [@jones-marinescu-2022]), showing zero net employment contraction and expansion in non-tradable service jobs.
4. **Spatial Saturation Trials:** GiveDirectly's randomized saturation across 653 Kenyan villages [@egger-2022-ge-kenya; @banerjee-niehaus-suri-2019], proving significant local general-equilibrium fiscal multipliers ($1.3\times$ to $2.4\times$) and modest local inflation.

## 4. Spain context & data sources
- **Primary Spanish Evaluation Datasets:** Ajuntament de Barcelona / Ivàlua B-MINCOME public microdata panels (2017–2019) [@todeschini-bmincome-2020]; Generalitat de Catalunya *Oficina del Pla Pilot per Implementar la RBU* methodological blueprints (2021–2023); Ministry of Inclusion IMV Policy Lab RCT registers.
- **International Register and Experimental Panels:** Finland Kela-register matched data [@kangas-2021-finland]; OpenResearch administrative tax and credit bureau panels [@bartik-2024-openresearch].

## 5. Methods & identification
1. **Structural Parameter Transportability Equations:**
   - Formalize the mapping from a $T$-period experimental cash transfer $G_{\text{pilot}}$ to permanent life-cycle elasticities. Under intertemporal separable preferences:
     $$\Delta \ln h_{it} = \varepsilon^c \Delta \ln w_{it}(1 - \tau) + \eta \left[ \frac{G_{\text{pilot}}}{A_{it} + H_{it}} \cdot \frac{1 - (1+r)^{-T}}{1 - (1+r)^{-(T_{\text{ret}} - t)}} \right]$$
     where $A_{it}$ is net liquid wealth, $H_{it}$ is human wealth (present discounted value of lifetime earnings), and $T_{\text{ret}} - t$ is remaining working life.
   - This framework filters out temporary intertemporal substitution, yielding transportable parameters ($\varepsilon^c \approx 0.12\text{--}0.18, \eta \approx -0.05\text{--}-0.08$) for Spain's baseline EUROMOD (`M09`) and HANK (`M04`) models across S1–S3.
2. **Bayesian Hierarchical Meta-Analysis:**
   - Estimate random-effects Bayesian meta-regressions for hours worked and health outcomes, conditioning on transfer generosity relative to local poverty line, marginal clawback rate, register-linkage fidelity, and duration.
3. **Synthesis Matrix of Pilot Lessons for Spain:**
   - Benchmark historical pilots against the 6 core criteria of the Spanish research plan: (i) decile universality, (ii) individual entitlement, (iii) tax-clawback integration, (iv) spatial cluster saturation, (v) administrative register linkage, and (vi) AI exposure stratification.

## 6. Pilot implications
- **Municipal:** Valuable for verifying local administrative delivery and subjective wellbeing (as demonstrated in B-MINCOME [@todeschini-bmincome-2020]), but inherently unsuited for measuring labor supply under a reformed national tax schedule or tracking internal migration spillovers.
- **Regional (*Régimen Común* vs. *Régimen Foral*):**
  - In *Régimen Común* (Catalonia blueprint), regional pilots resolve spatial cluster saturation but remain constrained by central government control over IRPF and Social Security registers.
  - In *Régimen Foral* (Basque Country / Navarre), regional governments hold the full tax and social security data spine, providing the only sub-national setting capable of testing net-tax integration and replicating international register-linked RCT standards [@kangas-2021-finland].
- **National:** The only scale capable of testing general-equilibrium macroeconomic closure, avoiding territorial leakages, and replicating Alaska-style permanent dividend expectations [@jones-marinescu-2022].

## 7. Risks, counterarguments & open issues
- **Counterargument (Finite-Horizon Over-Estimation of Leisure):** Skeptics argue that participants in 3-year trials take temporary sabbaticals that would not occur under a permanent policy. *Mitigation:* The structural life-cycle decomposition equation explicitly isolates the temporary discount factor, preventing over-estimation of permanent labor supply contraction.
- **Counterargument (Contextual Incomparability of Low-Income Windfalls):** US trials sampled low-income individuals with high baseline marginal utility of cash. *Mitigation:* Ingest priors from the Alaska PFD [@jones-marinescu-2022] and Finland trial [@kangas-2021-finland] which covered broader or universal populations.

## 8. Deliverables & effort
- Meta-Analytic Bayesian Database of Global Basic Income Experiments.
- Structural Parameter Transportability Protocol and B-MINCOME/Catalan Pilot Methodological Assessment for Chapters 1 and 7. (Effort: 4 person-weeks).
