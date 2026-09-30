# Re-read unread evidence for the S7 evaluation

## Objective

Re-decide every S7 row that was published as "No verificado" without reading an artifact that
was present and readable in the student repository at the graded revision, then recompute the
affected teams' counts and suggested scores. Verify, for every team touched, that the graded
revision really is the last commit at or before the S7 cutoff.

## Problem and rationale

The automated S7 pass evaluated from a truncated repository digest: `evaluar-semana.py` cuts
documents to 9000/5000 chars, the tree to 400 items, `CONTRATO.md` to 8000 and the whole payload
to 95000. When an artifact did not fit, the model wrote "No verificado — no se aportó el
contenido" instead of fetching it with `git show <hash>:<path>`. That contradicts `CONTRATO.md`
§13: "No se usa para evitar decidir: si la evidencia está y se puede leer, hay que pronunciarse",
and §12: "El repositorio es la entrega".

A second, independent defect surfaced while mapping: three S7 reports were published with
pre-cutoff revisions (`TAIA` `0a12f0c` 17-sep, `Verifacts` `635f9b7` 16-sep, `TRACTAR` `7cfb872`
31-ago, against the 21-sep cutoff). Their graded state may not be the state at the cutoff, so no
row can be corrected before the eligible revision is confirmed.

## Scope and constraints

- Cutoff: `2026-09-21T05:00:00Z`. Eligible revision: last commit at or before the cutoff on
  `origin/master` or `origin/main`. Never tags. Never another branch.
- Rows to correct (type A: repo-readable artifact that was not read), 8 teams, 37 rows:
  AudioShare 6, Drift 6, ElMapita 6, TAIA 6, Clubs_UTB 5, DinamikUTB 4, Verifacts 3, LostVault 1.
- Type B rows (Actions run URL, public SonarCloud URL and Quality Gate, sustentación) are out of
  scope. At most one unauthenticated `actions/runs` call per team may corroborate them; never use
  an ambient authenticated session, and on 403 continue without the API and record it.
- The "No cumple" rows already published stay: evidence supports them. Rows of the 15 teams with
  no type A rows are not touched.
- Ephemeral clones under `C:\Users\jairo\AppData\Local\Temp\opencode\`, deleted when the team is
  done. Never execute student code. Never write to student repositories.
- `resumen-s7.md` and `estado-s7.json` are updated by the orchestrator, never by writers.
- TDD: not applicable (static academic review artifacts). Checks are structural and content-based.
- Delivery: local commits only. No push; publication is the instructor's decision.

## Tasks

- [ ] T1 — Drift (6 rows) and ElMapita (6 rows).
  - Route: delegated writer; writer trigger fires (report, planilla and feedback files per team).
  - Acceptance: every type A row re-decided with `hash:ruta` citation, count recomputed, report
    marked as a post-cutoff updated revision, eligible revision confirmed.
- [ ] T2 — AudioShare (6 rows) and TAIA (6 rows).
  - Acceptance: same, plus TAIA's eligible revision resolved and corrected if stale.
- [ ] T3 — Clubs_UTB (5), DinamikUTB (4), Verifacts (3), LostVault (1).
  - Acceptance: same, plus Verifacts' eligible revision resolved and corrected if stale.
- [ ] T4 — Freshness audit of the 15 untouched teams.
  - Route: delegated; mapping trigger fires (23 repositories).
  - Acceptance: per team, published hash versus eligible revision, with the list of teams whose
    graded state must be re-evaluated before publishing.
- [ ] T5 — Consolidate `resumen-s7.md` and `estado-s7.json`.
  - Route: orchestrator; single writer for the shared files.
- [ ] T6 — Independent verification and local commit.
  - Acceptance: freshly re-read rows match the repositories, counts and scores reconcile, no
    personal emails, `git diff --check` clean.

## Checks

- Re-read each corrected row against its repository at the recorded revision.
- Recompute `n/m` and `1 + 4 × (n/m)` from the published matrix, not from the narrative.
- Confirm every corrected report names the revision it was decided at.
- Confirm no student repository was modified and no clone survives.
- `git diff --check` and the email scan required by `AGENTS.md`.

## Progress

- Mapping complete: 37 type A rows across 8 teams; 13 reports still carry raw pipeline output.
- Defect found: TAIA, Verifacts and TRACTAR were published with pre-cutoff revisions.

## Verification evidence

Pending.

## Next step

Run T1.
