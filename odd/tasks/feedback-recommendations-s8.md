# Integrar recomendaciones en feedback S8

## Objective

Publicar recomendaciones concretas y específicas de la evaluación S8 dentro del feedback semanal de los 23 equipos, sin alterar informes, matrices ni calificaciones.

## Problem and rationale

Las recomendaciones de mejora deben llegar a los estudiantes en el canal semanal de retroalimentación que ya consultan, no quedar únicamente en el análisis interno.

## Scope and constraints

- Authorized scope: append or supplement S8 feedback in `revisiones/2026-2/*/feedback.md` for all 23 teams.
- Do not change grades, evaluation matrices, reports, or README.
- Do not include names, email addresses, scores, hashes, or evaluator identity in student-facing feedback.
- Accept arc42 content in one file; recommendations must address missing content, not demand a split-file layout.
- Preserve existing feedback; add a concise S8-specific recommendation subsection.

## Route and evidence

- Route: delegated direct, because preparing edits requires reading 23 existing feedback files and writing multiple non-trivial artifacts.
- Trigger evidence: 23 weekly feedback files; one writer will inspect and update them as a single work unit.
- Delivery: feature branch `codex/feedback-recommendations-s8`; one Conventional Commit, then integrate and push to `master` under explicit user authorization.
- TDD: not applicable to passive documentation; no student code will be executed.

## Tasks

- [x] S8-FB-1: Inspect existing weekly feedback and add accurate, actionable S8 recommendations to each of 23 team files.
- [x] S8-FB-2: Verify one S8 recommendation section per team, clean diff, and no prohibited personal or grading data.
- [ ] S8-FB-3: Commit the work unit, integrate into `master`, and push the authorized update.

## Acceptance criteria

- Every one of the 23 team `feedback.md` files has specific S8 recommendations aligned with the reviewed evidence.
- Existing feedback is preserved; arc42 may be monolithic or modular.
- No evaluation artifacts or scores are changed.
- `git diff --check` passes and all 23 changes are read back.
- Commit uses Conventional Commits and contains no co-author/AI attribution.

## Applicable checks

- Read back all changed feedback files and confirm their S8 section.
- Search feedback diffs for score/hash/email patterns.
- `git diff --check`.

## Progress and evidence

- Branch created: `codex/feedback-recommendations-s8`.
- Baseline: `master` at `c44a1b5a56d8c2a8823ca2f5c48da2167bf3d31c`; worktree was clean.
- 23 target feedback files verified under `revisiones/2026-2/`.
- Final maintainer spot check: all 23 weekly sections and recommendation subsections are present; scans found no emails, hash-like identifiers, grades, or evaluator identity in added feedback. `git diff --check` passed. Native RDD status reported off; `gentle-ai review assess` could not resolve repository identity due to Access denied, so no review lifecycle was started for these passive Markdown documents.
- S8-FB-1 complete: supplemented the S8 section of all 23 feedback files with three or four concise, team-specific recommendations; no previous feedback line was removed (`git diff --numstat` showed zero deletions for every target).
- Writer checks: read back all 23 complete files; confirmed one S8 section and one recommendation subsection in each, with 3–4 new bullets; `git diff --check` passed. Search of added lines found no email addresses, scores or hash-like identifiers; a person-name pattern matched only the generic phrase `autorización docente previa`.
- S8-FB-2 complete: compared the complete S8 text in all 23 files against the reviewed evidence and harmonized eight materially inaccurate pre-existing S8 statements in eight files, only within S8, while preserving all earlier weeks. The corrections address the existing arc42 sections in ElMapita and Tienda Virtual, the deployment placeholders in EnAgenda and XALD, the need to cite rather than prejudge Drift's CI run, green CI evidence in TAIA and Sistema de calificación automática, and Verifacts' later timestamp without retroactive credit. Drift's added recommendation now asks neutrally for the chosen deployment topology without assuming existing alternatives. Readback confirmed one S8 recommendation subsection per team; `git diff --check` and scans of added feedback lines for emails, scores, hashes and personal names passed.
- Work-unit commit: `72391f1` (`docs(feedback): add S8 recommendations for all teams`), covering 23 feedback files plus this task document.

## Next step

Integrate commit `72391f1` into `master`, push under the user's explicit authorization, then record delivery evidence and close S8-FB-3.
