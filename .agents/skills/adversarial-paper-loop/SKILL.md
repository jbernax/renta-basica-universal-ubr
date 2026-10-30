---
name: adversarial-paper-loop
description: >-
  Run one or more iterations of the Universal Basic Rent (Spain) adversarial
  paper critique and error-correction loop. Deploys parallel skeptical subagents
  probing fiscal sustainability, administrative delivery, fraud/law abuse,
  labor/productivity contraction, and housing rent absorption, synthesizes
  steelmanned counter-arguments, applies surgical paper amendments, recompiles
  the publication monograph, and benchmarks progress with an independent blind judge.
---

# Adversarial Paper Critique & Refinement Runbook

Follow these exact steps for each adversarial paper improvement iteration.

## Step 1 · Start the Paper Critique Iteration
Run from `/home/antigravity/Projects/Universal Basic Rent`:
```bash
.venv/bin/python -m ubr paper critique start
```
Record the new iteration ID (`iter-NNNN`), bundle path (`paper_iterations/iter-NNNN/bundle.md`), and the list of assigned adversarial reviewers.

## Step 2 · Launch Adversarial Reviewer Panel in Parallel
Use `invoke_subagent` with `TypeName: "research"` to launch **all 5 adversarial reviewers concurrently** in a single tool call:
1. `adversarial-fiscal` (Financing, Laffer bounds, dynamic revenue leakage, compute mobility, EU fiscal framework)
2. `adversarial-implementation` (AEAT/INSS/CCAA inter-agency friction, banking/digital divide, take-up gaps, dispute backlog)
3. `adversarial-law-abuse` (Residency fraud, *Régimen Foral* arbitrage, informal economy collusion, EU free movement challenges)
4. `adversarial-productivity` (Labor supply contraction, reservation wages in essential services, human capital, Eurozone competitiveness)
5. `adversarial-housing` (Landlord rent absorption, spatial gentrification, seasonal lease loopholes)

For each reviewer `<role>`:
- Instruct it to read `harness/reviewers/<role>.md`, `harness/paper_rubric.yaml`, `harness/schemas/paper_review.schema.json`, and `paper_iterations/iter-NNNN/bundle.md`.
- Emphasize an aggressive, skeptical academic posture.
- Require valid YAML output matching `harness/schemas/paper_review.schema.json` with `reviewer: <role>` and `iteration: N`.
- Save each YAML file to `paper_iterations/iter-NNNN/reviews/<role>.yaml`.

## Step 3 · Validate Reviewer Outputs
```bash
.venv/bin/python -m ubr paper critique check iter-NNNN
```
Ensure all schema and chapter reference checks pass.

## Step 4 · Synthesize Adversarial Critiques
Read `harness/reviewers/adversarial-synthesizer.md` and all review YAMLs:
1. Identify high-leverage theoretical and empirical vulnerabilities.
2. Group them into thematic defenses (Fiscal, Implementation, Anti-Abuse, Productivity, Housing).
3. Formulate prioritized action proposals (`SYN-PAP-NN-01`, `SYN-PAP-NN-02`, ...) specifying exact chapter amendments.
4. Write `paper_iterations/iter-NNNN/synthesis.md`.

## Step 5 · Apply Surgical Amendments to Paper & Recompile
1. Edit the relevant chapter markdown files (`paper/ch00-*.md` through `paper/ch08-*.md`) to directly address the critiques, incorporate explicit counter-arguments, specify anti-abuse fail-safes, and calibrate empirical claims.
2. If new academic citations are needed, add and verify them in `plan/sources.yaml` (`.venv/bin/python -m ubr sources verify`).
3. Recompile the consolidated monograph and HTML viewer:
   ```bash
   .venv/bin/python -m ubr paper html
   ```
4. Write `paper_iterations/iter-NNNN/changelog.md` mapping every `SYN-PAP-NN-*` proposal and reviewer issue ID to modified files and sections.

## Step 6 · Launch Independent Blind Adversarial Judge
Invoke a **fresh** `research` subagent (`TypeName: "research"`, `Role: "Independent Adversarial Paper Judge"`):
- Instruct it to read **only** `harness/reviewers/adversarial-judge.md`, `harness/paper_rubric.yaml`, `harness/schemas/paper_judge.schema.json`, and the current chapters in `paper/`.
- Explicitly instruct it **not** to read `synthesis.md`, `changelog.md`, or previous judge evaluations.
- Write its output to `paper_iterations/iter-NNNN/judge.yaml`.
- Verify with:
  ```bash
  .venv/bin/python -m ubr paper critique check iter-NNNN --judge
  ```

## Step 7 · Score, Report, and Commit
```bash
.venv/bin/python -m ubr paper critique score iter-NNNN
.venv/bin/python -m ubr paper critique report
```
Stage and commit changes on the working branch:
```bash
git add paper/ paper_iterations/ harness/
git commit -m "docs(paper): adversarial critique iteration NNNN – strengthen fiscal, administrative, and legal robustness"
```
Present the updated scores and findings from `paper_iterations/REPORT.md` to the user.
