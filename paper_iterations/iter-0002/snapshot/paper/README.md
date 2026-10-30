# Universal Basic Rent (Spain) — Academic & Policy Monograph

This directory contains the complete, publication-grade academic and policy monograph:
**"Universal Basic Rent in an AI-Disrupted Labor Market: Institutional Design, Fiscal Architecture, and Multi-Level Pilot Evaluation for Spain"**.

---

## Structure of the Deliverable

| File | Title | Primary Topics & Empirical Foundations |
|---|---|---|
| [`monograph.md`](monograph.md) | **Complete Consolidated Monograph** | The full 16,300+ word monograph assembling the Abstract, Table of Contents, Chapters 0–8, and machine-verified bibliography. |
| [`ch00-executive-summary.md`](ch00-executive-summary.md) | **Executive Summary / *Resumen Ejecutivo*** | Bilingual (EN + ES) high-level executive summary for policymakers, summarizing core findings, fiscal bridges, and legal roadmaps. |
| [`ch01-introduction-analytical-framework.md`](ch01-introduction-analytical-framework.md) | **Introduction & Analytical Framework** | Problem statement, UBR vs. IMV vs. NIT taxonomy, lessons from international trials (Finland, OpenResearch, Kenya, SEED, B-MINCOME). |
| [`ch02-ai-shock-spain.md`](ch02-ai-shock-spain.md) | **The AI Shock in Spain** | CNO-11/EPA occupational exposure mapping, Scenarios S1–S3, counterfactual wage bills, and Social Security payroll tax erosion. |
| [`ch03-benefit-architecture-welfare-integration.md`](ch03-benefit-architecture-welfare-integration.md) | **Benefit Architecture & Welfare Integration** | Tiers A/B/C (€600/€900/€1,200), child equivalence scale ($\alpha_{\text{child}} = 0.40$), No-Loser Guarantee, dual-pillar pension integration, and Art. 273 TRLGSS accrual. |
| [`ch04-fiscal-architecture-ai-rent-capture.md`](ch04-fiscal-architecture-ai-rent-capture.md) | **Fiscal Architecture & AI Rent Capture** | Consolidated AP fiscal bridge (EUROMOD-Spain), decile distributional impacts (84th percentile breakeven), IECA compute reverse-charge (D-007), and the Sovereign AI Dividend Fund (FSTA). |
| [`ch05-macroeconomic-closure-housing-eurozone.md`](ch05-macroeconomic-closure-housing-eurozone.md) | **Macroeconomic Closure & Housing Markets** | Open-economy HANK model, Eurozone fiscal rules (Regulation EU 2024/1263 Net Primary Expenditure), dual-tenure rent pass-through, and the Objective Federal Fiscal Housing Benchmark (D-008). |
| [`ch06-constitutional-territorial-eu-legal-blueprint.md`](ch06-constitutional-territorial-eu-legal-blueprint.md) | **Constitutional, Territorial, and EU Legal Blueprint** | State competencies (Arts. 149.1.1, 149.1.14, 149.1.17 CE), TC doctrine (SSTC 158/2021, 19/2024, 79/2024, 182/2021, 73/2017), CPFF equalization, Foral Cupo integration, EU free movement (*Schumacker*, *Dano*), and digital delivery. |
| [`ch07-multi-level-pilot-causal-evaluation.md`](ch07-multi-level-pilot-causal-evaluation.md) | **Multi-Level Pilot & Causal Evaluation Design** | Multi-tier governance comparison, $J=70$ spatial cluster saturation RCT, MITMA cellular commuting gravity matrices, SDID pass-through, Saez-Chetty bunching, and AEA Pre-Analysis Plan (`AEARCTR-0014821`). |
| [`ch08-political-economy-transition-governance.md`](ch08-political-economy-transition-governance.md) | **Political Economy & Transition Governance** | Parliamentary geometry, LOEPSF Art. 15.6 Organic Reform (D-010 / STC 179/1989), CARIN deservingness framing shift (+18.6 pp approval), tripartite social dialogue, and AIReF triggers. |

---

## Verification & Citation Grounding

All 83 unique citations across the monograph resolve directly to machine-verified entries in [`plan/sources.yaml`](../plan/sources.yaml) with verified DOIs and URLs.
To verify:
```bash
.venv/bin/python -m ubr sources verify
.venv/bin/python -m ubr validate
```
