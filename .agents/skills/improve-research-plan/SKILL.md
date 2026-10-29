---
name: improve-research-plan
description: >-
  Run one or more iterations of the Universal Basic Rent (Spain) research-plan
  self-improvement loop using parallel specialist reviewer subagents, surgical
  plan edits, deterministic validation, and an independent blind judge subagent.
  Use when the user asks to improve the research plan, run an iteration, or
  advance the plan toward state of the art.
---

# Improve Research Plan Runbook

Follow these exact steps for each iteration in the current cycle (up to `cycle.iterations_per_checkpoint` in `harness/config.yaml`, unless the user specifies a single smoke-test iteration).

## Step 1 · Start the Iteration
Run from `/home/antigravity/Projects/Universal Basic Rent`:
```bash
.venv/bin/python -m ubr iteration start
```
Record the new iteration ID (`iter-NNNN`), bundle path (`iterations/iter-NNNN/bundle.md`), and the list of selected reviewers printed by the command.

## Step 2 · Launch the Specialist Reviewer Panel in Parallel
Use `invoke_subagent` with `TypeName: "research"` to launch **all selected reviewers concurrently** in a single tool call.
For each reviewer `<role>` in the selected list, instruct the subagent to:
1. Read `harness/reviewers/<role>.md`, `harness/rubric.yaml`, `harness/reference-factors.yaml`, `harness/schemas/review.schema.json`, and `iterations/iter-NNNN/bundle.md`.
2. Use `search_web` if needed to find real, verifiable DOIs or URLs for any missing literature or Spanish data/legal sources.
3. Return **only** valid YAML matching `harness/schemas/review.schema.json` with `reviewer: <role>` and `iteration: N`.

Write each subagent's returned YAML to `iterations/iter-NNNN/reviews/<role>.yaml`.

## Step 3 · Validate Reviewer Outputs
```bash
.venv/bin/python -m ubr reviews check iter-NNNN
```
If any review file fails schema or cross-reference validation, fix formatting errors or re-query that reviewer subagent via `send_message` until `reviews check` exits `0`.

## Step 4 · Synthesize Reviews
Read `harness/reviewers/synthesizer.md` and all `iterations/iter-NNNN/reviews/*.yaml` files:
1. Write `iterations/iter-NNNN/synthesis.md` clustering overlapping issues, resolving cross-reviewer trade-offs into explicit research questions or parameter comparisons, and selecting up to `max_changes_per_iteration` high-impact proposals (`SYN-NN-01`, `SYN-NN-02`, ...).
2. Any proposal that would touch `plan/decisions.md` or a `locked: true` module must be excluded from `synthesis.md` and written instead to `iterations/iter-NNNN/proposals-for-human.md`.

## Step 5 · Apply Surgical Plan Edits & Log Changelog
1. Add any newly recommended references to `plan/sources.yaml` and verify them:
   ```bash
   .venv/bin/python -m ubr sources verify
   ```
   Remove or replace any source that fails verification so cited sources remain $\ge 90\%$ verified.
2. Apply the selected `SYN-NN-*` proposals as targeted edits to `plan/modules/MXX-*.md`, `plan/00-scope.md`, `plan/methods.md`, `plan/paper-outline.md`, or `plan/open-questions.md`. Update `last_iteration: N` in the frontmatter of each modified module.
3. Write `iterations/iter-NNNN/changelog.md` mapping every `SYN-NN-*` proposal ID and source reviewer issue ID to the exact files and sections modified.

## Step 6 · Run Deterministic Validation Gate
```bash
.venv/bin/python -m ubr validate && .venv/bin/python -m ubr metrics
```
Must exit `0` with `0 error(s)`. If any error appears, fix it before proceeding.

## Step 7 · Launch Independent Blind Judge Subagent
Invoke a **fresh** `research` subagent (`invoke_subagent` with `TypeName: "research"`, `Role: "Independent Plan Judge"`):
- Instruct it to read **only** `harness/reviewers/judge.md`, `harness/rubric.yaml`, `harness/reference-factors.yaml`, `harness/schemas/judge.schema.json`, and the current files in `plan/` (`plan/plan.yaml`, `plan/00-scope.md`, `plan/methods.md`, `plan/paper-outline.md`, `plan/sources.yaml`, and `plan/modules/M01..M17-*.md`).
- Explicitly instruct it **not** to read `iterations/iter-NNNN/changelog.md`, `synthesis.md`, or any `scores.json`.
- Write its YAML output to `iterations/iter-NNNN/judge.yaml` and verify with:
  ```bash
  .venv/bin/python -m ubr reviews check iter-NNNN --judge
  ```

## Step 8 · Score, Check Stopping Rules, Commit, and Report
```bash
.venv/bin/python -m ubr score iter-NNNN
.venv/bin/python -m ubr stop-check iter-NNNN
.venv/bin/python -m ubr report
```
Stage and commit the iteration on the `research/plan-loop` branch using a conventional commit:
```bash
git add plan/ iterations/
git commit -m "docs(plan): iteration NNNN – <concise summary of modules improved>"
```
- If `stop-check` outputs `outcome: continue` and the user requested a multi-iteration cycle, loop back to **Step 1**.
- If `stop-check` outputs `checkpoint`, `plateau`, `regression`, or `sota-candidate` (or if a single iteration was requested), stop and present `iterations/REPORT.md` to the user.
