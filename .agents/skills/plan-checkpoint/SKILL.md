---
name: plan-checkpoint
description: >-
  Conduct a human-in-the-loop review checkpoint for the Universal Basic Rent
  (Spain) research plan: present score deltas, changelogs, and locked-file
  proposals from iterations/REPORT.md, record human decisions in
  plan/decisions.md, lock approved modules, and reset the iteration checkpoint
  counter. Use when the loop pauses at a checkpoint or when the user wants to
  review progress and steer the next cycle.
---

# Plan Checkpoint Runbook

## Step 1 · Generate & Inspect the Latest Report
```bash
.venv/bin/python -m ubr report
.venv/bin/python -m ubr status
```
Read `iterations/REPORT.md` and any `iterations/iter-NNNN/proposals-for-human.md` files from the most recent cycle.

## Step 2 · Present Key Decisions to the User
Summarize concisely for the user:
1. **Score Progression:** Weighted score, delta across the cycle, weakest rubric criterion, factor coverage %, and verified sources %.
2. **Substantive Plan Changes:** Key methodological, fiscal, legal, or pilot design upgrades applied in the cycle.
3. **Open Critical Issues & Human Proposals:** Any open `critical_issues` flagged by the judge or proposals in `proposals-for-human.md` that require human approval.

## Step 3 · Apply Human Steering (Between Iterations Only)
Verify no iteration is currently open (`.venv/bin/python -m ubr status` shows `scored`, not `OPEN`). Then apply the user's feedback:
- Append new binding choices to `plan/decisions.md` (`D-007`, ...).
- For any module the user wishes to freeze, set `locked: true` and `status: locked` in `plan/modules/MXX-*.md`.
- Validate the updated plan:
  ```bash
  .venv/bin/python -m ubr validate
  ```

## Step 4 · Record Checkpoint Sign-Off
```bash
.venv/bin/python -m ubr checkpoint --note "<summary of human decisions>"
```
Commit the checkpoint updates on `research/plan-loop` with a conventional commit (`docs(plan): checkpoint after iter-NNNN`).
