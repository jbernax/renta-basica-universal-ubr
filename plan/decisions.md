# Human-Locked Architecture & Scope Decisions (`decisions.md`)

> **Harness Lock Notice:** This file is listed in `plan.always_locked` in `harness/config.yaml`. During an open iteration, the AI improvement loop is strictly forbidden from editing this file. If a reviewer or synthesizer believes a decision here should be revisited, it must record a proposal in `iterations/iter-NNNN/proposals-for-human.md` for human review at the next checkpoint.

## D-001 · Definition of Universal Basic Rent (UBR)
- **Status:** Locked (User confirmed, 2026-10-29)
- **Decision:** In this research program, *Universal Basic Rent* corresponds to the Spanish concept of *Renta Básica Universal* (RBU) / Universal Basic Income (UBI): an unconditional, periodic, individual cash transfer paid to all qualifying residents without means-testing or work requirements. Housing and rent-capture effects are analyzed as critical economic channels (`M05`), not as an in-kind housing voucher.

## D-002 · Execution Architecture of the Improvement Harness
- **Status:** Locked (User confirmed, 2026-10-29)
- **Decision:** The improvement loop runs natively inside Antigravity using specialist subagent reviewers and an independent judge subagent, backed by deterministic Python CLI tools (`python -m ubr`) for structural validation, source verification, metric calculation, scoring, and stopping rules. No external paid LLM API keys are required.

## D-003 · Language and Target Deliverable Format
- **Status:** Locked (User confirmed, 2026-10-29)
- **Decision:** The research plan and final academic/policy paper are written in **English**, citing Spanish legal, statistical, and institutional sources in their original designations, and the final paper will include a comprehensive **Spanish executive summary** (*Resumen Ejecutivo para decisores públicos*).

## D-004 · Human-in-the-Loop Cadence
- **Status:** Locked (User confirmed, 2026-10-29)
- **Decision:** The improvement loop runs up to $N = 3$ autonomous iterations per cycle (stopping earlier on regression, plateau, or SOTA candidacy) and then halts for human review with a consolidated changelog and score-delta report (`iterations/REPORT.md`).

## D-005 · Spain Pilot Governance Level Left Open for Comparative Analysis
- **Status:** Locked (User confirmed, 2026-10-29)
- **Decision:** Rather than pre-committing to a single administrative tier, the research plan systematically compares **Municipal** (e.g. B-MINCOME follow-on), **Regional / Autonomous Community** (both *régimen común* such as Catalonia and *régimen foral* such as the Basque Country / Navarre), and **National** (State-level building on the *Ingreso Mínimo Vital* and IRPF) pilot and implementation options across every module.

## D-006 · Conditional AI Labor-Displacement Scenarios (S1–S3)
- **Status:** Locked (Default adopted at plan approval, 2026-10-29)
- **Decision:** Rather than treating complete labor-market collapse as an unexamined premise, all modules evaluate UBR across three explicit AI labor-displacement scenarios defined in `plan/plan.yaml`: **S1** (Moderate displacement & task polarization), **S2** (Severe cognitive & service displacement), and **S3** (Structural compression of labor income).

## D-007 · IECA Domestic B2B AI Compute Reverse-Charge Withholding
- **Status:** Locked (User confirmed at Checkpoint 1, 2026-10-29)
- **Decision:** Enforce destination-based taxation of foreign AI compute, cloud GPU capacity, and API inference via the *Impuesto Especial sobre Capacidad y Computación de IA* (*IECA*) under TRIRNR and LGT, backed by conditioning corporate income tax deductibility under Art. 15 LIS on verified domestic withholding certificates.

## D-008 · Objective Federal Fiscal Housing Benchmark
- **Status:** Locked (User confirmed at Checkpoint 1, 2026-10-29)
- **Decision:** Decouple federal tax conditionality and circuit-breakers on rental income from regional ZMRT declarations under *Ley 12/2023* (bypassing regional boycotts confirmed by STC 79/2024) by establishing an Objective Federal Fiscal Benchmark on LIRPF Art. 23.2 reductions under State tax competence (Art. 149.1.14 CE).

## D-009 · Statutory Social Security Pension Accrual Continuity
- **Status:** Locked (User confirmed at Checkpoint 1, 2026-10-29)
- **Decision:** UBR benefit offsets against contributory unemployment benefits shall not terminate statutory retirement contributions; SEPE must maintain retirement contributions under Art. 273 TRLGSS, and displaced workers shall receive a universal *Crédito Cotizatorio Básico por Transición Tecnológica* guaranteeing continuous pension accrual at 100% of the SMI base.

## D-010 · Bicameral Legislative Override Strategy for Expenditure Ceilings
- **Status:** Locked (User confirmed at Checkpoint 1, 2026-10-29)
- **Decision:** The bicameral strategy shall enact an Organic Law amending LOEPSF Art. 15.6 by absolute majority in Congress to restore the general constitutional override rule (Art. 90.2 CE, STC 179/1989), neutralizing the Senate's absolute veto over fiscal stability targets and spending ceilings.

