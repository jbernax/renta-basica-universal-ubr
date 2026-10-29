# Review Synthesizer Guidance (`synthesizer`)

## Purpose
After all specialist reviewers in `iterations/iter-NNNN/reviews/*.yaml` have passed `python -m ubr reviews check`, synthesize their findings into `iterations/iter-NNNN/synthesis.md` before applying any edits to `plan/`.

## Synthesis Rules
1. **Deduplicate & Cluster:** Group overlapping issues raised by multiple reviewers (e.g. `PF-01-02` and `RT-01-01` both flagging IRPF clawback consistency) into a single actionable change item that lists all contributing issue IDs.
2. **Resolve Conflicts Explicitly:** If two reviewers disagree (e.g. `social-policy` recommends higher individual benefit while `macroeconomist` warns of inflationary demand), do not silently pick one—resolve the conflict by turning the trade-off into an explicit parameterized research question or scenario comparison in the plan.
3. **Respect Locks:** Check `plan/decisions.md` and `locked: true` modules. Any proposal that would modify a locked file or contradict a human decision must **not** be applied; instead, write it to `iterations/iter-NNNN/proposals-for-human.md` with its rationale and source citations.
4. **Rank & Cap Changes:** Rank candidate changes by:
   - Severity (`critical` > `major` > `minor`)
   - Cross-panel agreement (issues flagged by ≥2 reviewers)
   - Expected rubric impact divided by edit complexity
   Cap the selected changes at `cycle.max_changes_per_iteration` (from `harness/config.yaml`, default 15) to avoid noisy wholesale rewrites.
5. **Traceability:** Every selected change in `synthesis.md` must list:
   - Proposal ID (`SYN-<iter:02d>-<seq:02d>`)
   - Source review issue IDs (e.g. `[RT-01-01, PF-01-02]`)
   - Target file(s) in `plan/`
   - Exact edit summary and any new verified entries to add to `plan/sources.yaml`.
