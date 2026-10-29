---
id: M01
title: AI labor displacement and macroeconomic scenarios
status: draft
locked: false
depends_on: [M08, M16]
covers: [F01]
feeds_chapters: [1, 2]
last_iteration: 2
---
# M01 · AI labor displacement and macroeconomic scenarios

## 1. Why this matters
The case for a Universal Basic Rent in Spain rests on whether generative and agentic AI produce a qualitatively different labor shock than previous automation waves [@acemoglu-restrepo-2019; @eloundou-2024-gpts; @albanesi-2023-ai-europe]. If AI substitution outpaces task reinstatement across clerical, professional, and service occupations, Spain faces simultaneous compression of household wage income and erosion of the IRPF and Social Security payroll tax bases (`M03`, `M16`). Crucially, because Spanish labor institutions feature binding collective bargaining agreements and a high share of micro-enterprises, task exposure does not translate directly into downward nominal wage cuts; instead, it triggers intermittent employment inactivity and structural underemployment [@bentolila-2012-dual-spain].

## 2. Research questions
- **RQ-M01-01**: What share of Spanish full-time equivalent (FTE) employment and aggregate wage bill in 3-digit CNO-11 occupations is exposed to net displacement versus task reinstatement under AI scenarios S1, S2, and S3 once collective-bargaining wage floors and SME adoption lags are accounted for?
  - *Hypothesis:* While gross task exposure exceeds 45% in cognitive occupations, net FTE displacement in Spain is 8% in S1 ($\Delta s_L = -2.5$ pp), 20% in S2 ($\Delta s_L = -7.0$ pp), and 35% in S3 ($\Delta s_L = -15.0$ pp), with displacement concentrating in intermittent contract inactivity (*pases a inactividad de fijos discontinuos*) and non-renewal of temporary/part-time hours under *Real Decreto-ley 32/2021* [@boe-rdl-32-2021-reforma-laboral].
- **RQ-M01-02**: How do combined TFP growth trajectories, service-sector marginal-cost reductions, and outbound foreign AI-rent flows determine net payroll tax (*cotizaciones sociales*) and IRPF revenue drag across Spanish Autonomous Communities?
  - *Hypothesis:* Each 1 percentage-point drop in the labor income share reduces combined Spanish IRPF and Social Security revenues by 1.25–1.40 percentage points under S1, but expands to >1.65 percentage points under S2 and S3 as cognitive workers in service-intensive urban regions (Madrid, Catalonia) face displacement and corporate surpluses accrue to foreign-domiciled AI foundation-model providers. In Scenario S2 ($\Delta s_L = -7.0$ pp), this triggers an aggregate baseline tax revenue collapse of 11.55% of GDP (~€173B/year), requiring direct macroeconomic feedback into EUROMOD-Spain (`M03`) to finance baseline public services and UBR outlays.

## 3. State of knowledge
Task-based frameworks show that automation depresses the labor share whenever displacement effects exceed productivity and new-task reinstatement effects [@acemoglu-restrepo-2019; @acemoglu-2024-macro-ai]. Empirical studies across European economies [@albanesi-2023-ai-europe; @gmyrek-ilo-2023] indicate that while early AI was modestly employment-enhancing for highly skilled workers, generative and agentic AI directly target non-routine cognitive and administrative tasks [@eloundou-2024-gpts; @felten-2021-aioe; @webb-2020-ai; @cazzaniga-imf-2024]. In Spain's institutional context, labor-market duality and sectoral wage floors mean technological shocks adjust through contract duration, fixed-discontinuous inactivity spells, and hours reductions rather than real wage flexibility [@bentolila-2012-dual-spain; @boe-rdl-32-2021-reforma-laboral].

## 4. Spain context & data sources
- **Labor Microdata:** INE *Encuesta de Población Activa* (EPA) quarterly rotating panel (occupational flows at 3-digit CNO-11, contract type, hours, tenure).
- **Social Security Histories:** *Muestra Continua de Vidas Laborales* (MCVL, Seguridad Social) matched to AEAT Form 190 tax withholdings for longitudinal wage, contribution base, and *fijos discontinuos* inactivity trajectories.
- **Enterprise & Adoption Microdata:** INE *Encuesta sobre el uso de TIC y comercio electrónico en las empresas* (ETICCE, firm-level AI software/hardware adoption by size class) and *Encuesta Anual de Estructura Salarial* (EAES).

## 5. Methods & identification
1. **Gross Exposure vs. Net Spanish Displacement Crosswalk:** Map O*NET task scores [@eloundou-2024-gpts; @felten-2021-aioe; @webb-2020-ai] to ISCO-08 and CNO-11 using ESCO/PIAAC task weights. Scale gross occupational exposure by firm-size AI adoption rates from ETICCE and Spanish collective-bargaining coverage rates (*convenios sectoriales*) to derive net displacement hazards.
2. **Identification Strategy & Bounds:** Estimate baseline S1 displacement elasticities in MCVL/EPA using a shift-share IV design interacting pre-shock occupational exposure shares with sectoral AI software/compute investment, verifying shock-level balance and pre-trend orthogonality per Borusyak, Hull, & Jaravel [@borusyak-2022-shift-share]. For S2 and S3, bound agentic displacement using structural task-cost replacement functions [@korinek-suh-2024] rather than extrapolating historical IV trends.
3. **Macroeconomic Scenario Vectors (S1–S3):** Pair labor-share shifts ($\Delta s_L \in \{-2.5, -7.0, -15.0\}$ pp) with explicit TFP growth bands (0.5–1.8% annually), marginal-cost deflation curves in service sectors, and domestic corporate operating surplus vs. outbound foreign compute royalty splits for `M03`, `M04`, and `M16`. Explicitly output counterfactual post-displacement wage and employment distributions across CNO-11 deciles to feed EUROMOD-Spain (`M03`, `M09`), closing the macro-to-micro fiscal loop under the 11.55% of GDP baseline revenue shock.

## 6. Pilot implications
- **Municipal Tier:** Select pilot municipalities spanning high cognitive/back-office exposure (e.g. service-intensive suburban metropolitan belts) versus manufacturing/agricultural controls, tracking local employment transitions via monthly MCVL affiliation data.
- **Regional Tier (*Régimen Común* vs. *Régimen Foral*):** Compare Autonomous Communities with high service/headquarter concentration under *Régimen Común* (Madrid, Catalonia) against industrial-exporting regions under *Régimen Foral* (Basque Country / Navarre), utilizing foral corporate tax data to evaluate regional AI productivity capture.
- **National Tier:** Establish an AIReF-certified composite index (EPA cognitive displacement + MCVL contribution bases) to monitor realized displacement and inform statutory fast-track parliamentary reviews (`M17`).

## 7. Risks, counterarguments & open issues
- **Counterargument (Acemoglu Productivity Modesty):** Acemoglu [@acemoglu-2024-macro-ai] argues macroeconomic TFP gains from AI will remain below 1% over a decade, implying slow displacement. *Mitigation:* Explicitly bracket S1 (slow/moderate, consistent with Acemoglu) against S2 and S3 [@korinek-suh-2024], pre-committing UBR scale-up to observable displacement triggers rather than fixed calendar dates (`M17`).
- **Within-Occupation Task Reorganization:** CNO-11 codes may mask internal reorganization; addressed by tracking worker-level daily contribution bases in MCVL.

## 8. Deliverables & effort
- CNO-11 AI Exposure & Net Displacement Calibration Pipeline for Spain (EPA + MCVL + ETICCE).
- Complete S1–S3 Scenario Parameter Vectors for EUROMOD (`M03`, `M09`) and HANK (`M04`). (Effort: 6 person-weeks).
