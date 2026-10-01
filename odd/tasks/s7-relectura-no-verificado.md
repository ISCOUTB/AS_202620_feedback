# Re-read unread evidence for the S7 evaluation

## Objective

Re-decide every S7 row that was published as "No verificado" without reading an artifact that
was present and readable at the graded revision, then recompute the affected teams' counts and
suggested scores. Verify, for every team touched, that the graded revision really is the last
commit at or before the S7 cutoff.

## Problem and rationale

The automated S7 pass evaluated from a truncated repository digest: `evaluar-semana.py` cuts
documents to 9000/5000 chars, the tree to 400 items, `CONTRATO.md` to 8000 and the whole payload
to 95000. When an artifact did not fit, the model wrote "No verificado — no se aportó el
contenido" instead of fetching it with `git show <hash>:<path>`. That contradicts `CONTRATO.md`
§13: "No se usa para evitar decidir: si la evidencia está y se puede leer, hay que pronunciarse",
and §12: "El repositorio es la entrega".

The mirror defect appeared during verification: nine rows published as "Cumple" whose own
observation admitted that the artifact had not been read. That inflates scores instead of
lowering them, and it was corrected in the same pass.

## Scope and constraints

- Cutoff: `2026-09-21T05:00:00Z`. Eligible revision: last commit at or before the cutoff on
  `origin/master` or `origin/main`. Never tags. Never another branch.
- Rows corrected (type A: repo-readable artifact that was not read), 8 teams, 37 rows:
  AudioShare 6, Drift 6, ElMapita 6, TAIA 6, Clubs_UTB 5, DinamikUTB 4, Verifacts 3, LostVault 1.
  Outcome: 31 became Cumple, 6 became No cumple.
- Type B rows (Actions run URL, public SonarCloud URL and Quality Gate, sustentación) stayed out
  of scope. At most one unauthenticated `actions/runs` call per team was used to corroborate.
- The published "No cumple" rows were kept: evidence supports them.
- Ephemeral clones only, under the temp directory, deleted per team. No student code was executed.
- `resumen-s7.md` and `estado-s7.json` were updated by the orchestrator, never by writers.
- TDD: not applicable (static academic review artifacts).
- Delivery: local commits only. No push; publication is the instructor's decision.

## Criterion interpretation fixed during this work

"C4 nivel 2 con protocolo y formato en cada flecha": arrows from a **person to a container** are
tolerated (they describe human interaction). Protocol and format are required on every arrow that
crosses a technological boundary (container to container, container to external system, container
to database). Applied uniformly to AudioShare, ElMapita, Drift, DinamikUTB, Clubs_UTB and
LostVault.

## Tasks

- [x] T1 — Drift (6 rows) and ElMapita (6 rows). Drift 5/10 → 10/10; ElMapita 4/10 → 8/10.
- [x] T2 — AudioShare (6 rows) and TAIA (6 rows). AudioShare 5/10 → 9/10; TAIA 6/10 → 10/10.
- [x] T3 — Clubs_UTB (5), DinamikUTB (4), Verifacts (3), LostVault (1). Clubs_UTB 6/10 → 8/10;
      DinamikUTB 7/10 → 10/10; Verifacts 8/10 → 10/10; LostVault stays 7/10.
- [x] T4 — Freshness audit of the 15 untouched teams. All 15 published hashes equal the eligible
      revision; no graded state needed re-evaluation. The earlier suspicion about TAIA, Verifacts
      and TRACTAR was wrong: their revision dates are old because the teams did not push, not
      because the reports were stale.
- [x] T5 — Consolidate `resumen-s7.md` and `estado-s7.json`.
- [x] T6 — Independent verification. Found the mirror defect and a leaked student name.
- [x] T7 — Re-read the nine "Cumple" rows that admitted not reading (IA records in ElMapita,
      Drift and DinamikUTB; Verifacts and TAIA ADR rows; TAIA contract correspondence; ElMapita
      wording). No state changed; every observation is now backed by `ruta:línea`.
- [x] T8 — Publication of the corrected week (`779284b..792e5db` on `master`).
- [x] T9 — Repair the closed-week guard in `informes_definitivos()`: it counted a report as
      definitive only when it contained the literal `Revision automatica definitiva`, which local
      audits rewrite. It now counts published reports and leaves the mode to `estado-<id>.json`.
      Verified: 23 of 23 for S7.
- [x] T10 — Fix the transversal matrix size. The pipeline prompt demanded "exactly 8 rows" while
      `CONTRATO.md` §11 has 9, so published reports dropped standard rows. Prompt and count fixed,
      and the missing rows were added to Verifacts, TAIA, ElMapita, DinamikUTB and TRACTAR.
- [x] T11 — Give the evidence digest an explicit budget. Criterion-deciding documents enter first
      with their own quota, everything left out is published in `documentos_omitidos`, the payload
      no longer silently truncates, and the prompt forbids writing "no se aportó" because of a
      digest cut. Verified against Drift, ElMapita and TRACTAR: the six deciding groups
      (contract, workflows, arc42 §6, C4 level 2, aspectos, ia) all arrive and the payload fits.
- [x] T12 — Register the §11 non-conformities found by reading: three accepted ADRs edited without
      a declared replacement (Verifacts, TAIA, ElMapita; four in DinamikUTB) and incomplete
      contribution (Verifacts, ElMapita, TRACTAR).
- [x] T13 — Record the TRACTAR repository rename (`AS_202620_TRACTAR` redirects to
      `AS_202620_UTB_TRACKER`) and correct its self-contradictory identity charge.
- [x] T14 — Hygiene: remove personal names from three reports and the ElMapita feedback.

## Checks

- Re-read each corrected row against its repository at the recorded revision.
- Recompute `n/m` and `1 + 4 × (n/m)` from the published matrix, not from the narrative.
- Confirm every corrected report names the revision it was decided at.
- Confirm no student repository was modified and no clone survives.
- `git diff --check` and the email scan required by `AGENTS.md`.

## Progress

- Mapping complete: 37 type A rows across 8 teams; 13 reports still carried raw pipeline output.
- All 37 rows re-decided and 9 mirror rows re-read.
- Counts recomputed from the published matrices by script, not by hand: 8 teams moved, 7 upward.
  Class average 4.0 → 4.4. No graded revision changed for any of the 23 teams.

## Verification evidence

- Orchestrator spot checks with its own clones: Drift `backend/tests/test_contract.py` is
  schemathesis against the OpenAPI contract and `ci.yml` boots the API on the contract port before
  running it; TAIA `_assert_contract_matches` compares `paths`/`components`/`info` and ships
  `test_incompatible_change_is_detected`; AudioShare `npm run verify` → `vitest run` executes
  `contract.test.ts` and `ci.yml` has the SonarCloud step; DinamikUTB and Clubs_UTB C4 diagrams
  read line by line.
- Eligible revision confirmed by `git rev-list -1 --before=2026-09-21T05:00:00Z` for Drift,
  ElMapita, AudioShare, TAIA, Verifacts, LostVault, Clubs_UTB, DinamikUTB, uniTeam, Recobra,
  CampusMarket and TRACTAR.
- Independent verifier: recomputed all 23 matrices from the files (no discrepancy against
  `resumen-s7.md`), checked report/planilla/feedback coherence, and re-read four rows against the
  repositories (Clubs_UTB pipeline and correspondence, DinamikUTB arc42 §6, Verifacts pipeline,
  ElMapita arc42 §6): all four sustained.
- Hygiene: email scan clean, `git diff --check` clean, `.atl/` untracked and not staged.

## Pipeline defects fixed in this work

All four share one origin: the evaluation read a silently truncated digest.

1. Closed-week guard: `informes_definitivos()` matched a literal header that local audits rewrite.
   It now counts published reports; the definitive mode lives in `estado-<id>.json`.
2. Transversal matrix: the prompt asked for "exactly 8 rows" while §11 has 9, so reports dropped a
   standard row. The nine names are now listed literally in the prompt.
3. Digest budget: criterion-deciding documents enter first with their own quota; the payload is no
   longer cut mid-JSON; leftovers are published in `documentos_omitidos`; the prompt forbids reading
   a budget cut as "the team did not provide it".
4. Tree truncation is now flagged as `arbol_truncado`, so an absence in a truncated tree cannot be
   reported as "No cumple".

Not tested end to end: there is no local LLM key, so these changes were verified by compiling the
script and exercising the new functions against real repositories, not by a full pipeline run.

## Open items

- The same sweep has not been done for S8 or later weeks; the prompt that caused it is now fixed
  only going forward.
- `EQUIPOS.md` and the README still use the old TRACTAR repository name, which now redirects.

## Next step

Report the corrected scoreboard and the pipeline changes; await the next week's decision.
