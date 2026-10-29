# Project Rules (`AGENTS.md`)

These rules apply to every agent and subagent working in the **Universal Basic Rent (Spain)** research repository.

## 1. Domain & Scope Discipline
- **Universal Basic Rent (`D-001`):** Defined as an unconditional, periodic (monthly), individual cash transfer (*Renta Básica Universal*) paid to qualifying residents in Spain and integrated into the Personal Income Tax (IRPF).
- **Language (`D-003`):** All research plan modules (`plan/`) and the target paper are written in **English**. Spanish statutes, taxes, datasets, and institutions are cited by their exact Spanish designations (e.g., *Ingreso Mínimo Vital*, *Muestra Continua de Vidas Laborales*, *Régimen Foral*). The final paper includes a Spanish executive summary.
- **Scenarios (`D-006`):** Always distinguish across the three conditional AI labor-displacement scenarios defined in `plan/plan.yaml`: **S1** (Moderate polarization, $\Delta s_L = -2.5$ pp), **S2** (Severe cognitive/service displacement, $\Delta s_L = -7.0$ pp), and **S3** (Structural compression of labor income, $\Delta s_L = -15.0$ pp).
- **Pilot Tiers (`D-005`):** Every module's Section 6 ("Pilot implications") must explicitly compare **Municipal**, **Regional** (*Régimen Común* vs. *Régimen Foral*), and **National** options.

## 2. Citation & Grounding Discipline
- Every empirical, legal, or theoretical claim in `plan/**/*.md` must cite one or more keys in Pandoc/Quarto syntax: `[@source-id]` or `[@id-1; @id-2]`.
- Every cited `@source-id` must exist in `plan/sources.yaml` with a real, machine-verifiable `doi` or `url`.
- **Never fabricate citations, DOIs, or URLs.** After adding any new source to `plan/sources.yaml`, run `.venv/bin/python -m ubr sources verify` and `.venv/bin/python -m ubr validate`.

## 3. Human-Locked Files & Steering Rules
- While an iteration is open (`iterations/iter-NNNN/` exists without `scores.json`), **never modify `plan/decisions.md` or any module with `locked: true` in its YAML frontmatter**.
- If a reviewer or synthesizer identifies an improvement that requires altering a locked file or reversing a decision in `plan/decisions.md`, write the proposal to `iterations/iter-NNNN/proposals-for-human.md` instead.
- The structural validator (`.venv/bin/python -m ubr validate`) diffs locked files against `iterations/iter-NNNN/snapshot/plan/` and will fail the iteration if any locked file is touched.

## 4. Independence of the Judge
- The agent applying edits to `plan/` must **never** write `iterations/iter-NNNN/judge.yaml` itself.
- `judge.yaml` must be produced by an independent subagent following `harness/reviewers/judge.md`, evaluating only the current `plan/`, `harness/rubric.yaml`, and `harness/reference-factors.yaml` without reading `changelog.md` or prior scores.

## 5. Surgical Edits & Traceability
- Make targeted, surgical edits to `plan/modules/MXX-*.md` rather than wholesale rewrites.
- Preserve the 8 required section headings and required frontmatter fields (`id`, `title`, `status`, `locked`, `depends_on`, `covers`, `feeds_chapters`, `last_iteration`) in every module.
- Every edit applied during an iteration must be logged in `iterations/iter-NNNN/changelog.md` with its corresponding synthesis proposal ID (`SYN-NN-MM`) and reviewer issue IDs.
