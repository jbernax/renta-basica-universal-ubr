# Universal Basic Rent (Spain) — Research Plan & Self-Improvement Harness

This repository hosts the modular research plan and self-improvement harness for a comprehensive academic and policy monograph on implementing a **Universal Basic Rent** (*Renta Básica Universal*, UBR) in **Spain** under AI-driven labor market disruption.

---

## Repository Map

```text
.
├── AGENTS.md                        # Always-on rules for agents and subagents
├── Makefile                         # Convenience targets: setup, test, validate, metrics, sources, status, report
├── pyproject.toml                   # Python packaging for the `ubr` CLI
├── plan/                            # Research Plan (source of truth)
│   ├── plan.yaml                    # Manifest: central question, S1-S3 scenarios, module list
│   ├── decisions.md                 # Human-locked ADR log (protected during AI loop iterations)
│   ├── 00-scope.md                  # Scope, definitions, benefit Tiers A/B/C (€600/€900/€1,200)
│   ├── methods.md                   # Cross-cutting methodology (EUROMOD, HANK, RCT saturation)
│   ├── paper-outline.md             # Module-to-chapter mapping for the final monograph
│   ├── open-questions.md            # Active analytical questions for upcoming iterations
│   ├── sources.yaml                 # Machine-verified bibliography registry
│   └── modules/
│       └── M01..M17-*.md            # 17 modular factor specifications
├── harness/                         # Self-improvement harness
│   ├── config.yaml                  # Loop parameters, reviewer rotation, SOTA stopping thresholds
│   ├── rubric.yaml                  # 10 weighted evaluation criteria with 0-5 anchor descriptions
│   ├── reference-factors.yaml       # F01-F17 factor checklist for deterministic coverage tracking
│   ├── reviewers/                   # Specialist reviewer personas (9 roles + synthesizer + independent judge)
│   ├── schemas/                     # JSON Schemas for modules, sources, reviews, and judge outputs
│   └── ubr/                         # Python CLI package (`python -m ubr ...`)
├── .agents/skills/                  # Antigravity workspace skills
│   ├── improve-research-plan/       # Runbook for executing 1..N improvement iterations
│   └── plan-checkpoint/             # Runbook for human review checkpoints
├── iterations/                      # Append-only history of iterations (`iter-NNNN/`) and `REPORT.md`
└── tests/                           # 68 pytest unit tests covering all harness seams
```

---

## Quick Start

```bash
# 1. Set up the local virtualenv and install the `ubr` CLI
make setup

# 2. Run the harness unit test suite (68 tests)
make test

# 3. Validate the research plan structure, citations, dependencies, and locks
make validate

# 4. Verify all source DOIs and URLs in plan/sources.yaml
make sources

# 5. Inspect current plan metrics and iteration status
make metrics
make status
```

---

## Running the AI Self-Improvement Loop

Inside Antigravity, trigger the loop by saying **"Improve the research plan"** (or invoking the `improve-research-plan` skill):

1. **Start Iteration (`python -m ubr iteration start`):** Snapshots `plan/`, compiles `iterations/iter-NNNN/bundle.md`, and selects the specialist reviewer panel for iteration `NNNN` (5 rotating reviewers by default, always including `red-team`, and the full 9-reviewer panel every 3rd iteration).
2. **Parallel Specialist Review:** Launches parallel `research` subagents for each selected reviewer (`labor-economist`, `public-finance`, `macroeconomist`, `spanish-eu-law`, `social-policy`, `evaluation-methodologist`, `housing-economist`, `political-economist`, `red-team`), writing structured YAML critiques to `iterations/iter-NNNN/reviews/<reviewer>.yaml`.
3. **Schema Check (`python -m ubr reviews check`):** Validates all reviewer YAML outputs against `harness/schemas/review.schema.json`.
4. **Synthesis (`synthesis.md`):** Deduplicates findings, resolves cross-disciplinary conflicts into explicit research questions/scenarios, routes any locked-file suggestions to `proposals-for-human.md`, and ranks top changes (capped at `max_changes_per_iteration: 15`).
5. **Apply & Verify:** Applies surgical edits to `plan/`, logs every change in `iterations/iter-NNNN/changelog.md`, verifies new sources (`python -m ubr sources verify`), and runs `python -m ubr validate`.
6. **Independent Blind Judge (`judge.yaml`):** Launches a separate `research` subagent with `harness/reviewers/judge.md` to score the updated plan against the 0–5 anchors in `harness/rubric.yaml` without seeing the changelog or prior scores.
7. **Score & Stop-Check (`python -m ubr score && python -m ubr stop-check`):** Computes weighted scores, deltas, and deterministic metrics (`scores.json`), then evaluates stopping rules (`continue`, `checkpoint`, `plateau`, `regression`, or `sota-candidate`) and updates `iterations/REPORT.md`.

---

## How Humans Steer the Plan Between Cycles

- **Locking Decisions:** Add or edit entries in `plan/decisions.md`. The loop treats `decisions.md` as immutable.
- **Locking Modules:** Set `locked: true` (and `status: locked`) in any module's frontmatter (`plan/modules/MXX-*.md`) once you are satisfied with it.
- **Tuning Thresholds:** Adjust weights in `harness/rubric.yaml` or SOTA thresholds in `harness/config.yaml`.
- **Recording Checkpoints:** After reviewing `iterations/REPORT.md`, run `.venv/bin/python -m ubr checkpoint --note "..."` (or use the `plan-checkpoint` skill) to reset the cycle counter for the next $N$ iterations.
