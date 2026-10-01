# Definitive S8 evaluation

## Objective

Produce the definitive week 8 evaluation (Evidencia S8 «Despliegue reproducible, CI y
observabilidad», `arqsw:evidencia-s8`) for all 23 teams at the last commit at or before the S8
cutoff, replacing the preliminary reports that were graded against 20–23 September revisions.

## Problem and rationale

Every one of the 23 published S8 reports is preliminary (`estado-s8.json` records an early pass and
a local preliminary consolidation). Their graded revisions are from 20–23 September, before the
28 September cutoff, so the graded state will move for most teams. They also carry the defect fixed
in S7: rows marked "No verificado" because the evaluator's digest was truncated, not because the
artifact was missing.

Instructor decision for this pass: **the deployed URL is not graded yet.** It is submitted through
Moodle and is not available here, so the two deployment rows stay deferred instead of being
guessed.

## Scope and constraints

- Cutoff: `2026-09-28T05:00:00Z`. Eligible revision: last commit at or before the cutoff on
  `origin/master` or `origin/main`. Never tags. Never another branch.
- 23 teams. Ficha matrix has 12 rows; 10 are graded in this pass. Deferred with an explicit reason:
  "URL del sistema accesible desde fuera de la red de la universidad" and "Health check
  consultable". Their observations still record what the repository proves (declared public URL,
  health route with `ruta:línea`) so the second pass is cheap.
- No deployment URL is opened, curled or otherwise probed in this pass.
- Transverse matrix: the 9 rows of `CONTRATO.md` §11, with evidence.
- Provisional note: `1 + 4 × (n/10)` over the 10 gradable rows, marked as provisional because two
  deployment rows are pending. The final note is the instructor's.
- Ephemeral clones under the temp directory, deleted per team. No student code is executed. One
  unauthenticated `actions/runs` call per team at most.
- `resumen-s8.md` and `estado-s8.json` are the orchestrator's, never a writer's.
- Not in scope: the `taller-docker` deliverable (separate `idnumber`, no grade in the calendar).
- Delivery: local commits, then publication on the instructor's word.

## Tasks

- [ ] T1 — Round 1: AudioShare, Clubs_UTB, DinamikUTB, Drift, ElMapita, EnAgenda.
- [ ] T2 — Round 2: GimnasioUTB, InvenTrack, LaPlacita, LostVault, CampusMarket, PideUtb.
- [ ] T3 — Round 3: ROUTB, Recobra, ShareU, Sistema-de-calificacion-automatica, TAIA,
      TIENDA-VIRTUAL-UTB.
- [ ] T4 — Round 4: TRACTAR, Verifacts, XALD, mapsutb, uniTeam.
- [ ] T5 — Consolidate `resumen-s8.md`, `estado-s8.json` (mode definitive, so the repaired guard
      protects the week) and the README.
- [ ] T6 — Independent verification and publication.

## Checks

- Recompute `n/10` and the provisional note from each published matrix, by script.
- Confirm every report names its graded revision and the deferred rows with their reason.
- No deployment URL probed; no student code executed; no clone left behind.
- No emails in `revisiones/`; `git diff --check` clean; `.atl/` never staged.

## Method for the reviewers (follow it literally)

You may write only the assigned teams' reports in the kit. Never modify student repositories, never
execute student code, never open their deployed URLs, never commit or push.

**Instructor decision that governs this pass: the deployed URL is not graded yet.** The two
deployment rows are therefore deferred, not judged:

- "URL del sistema accesible desde fuera de la red de la universidad" and "Health check consultable"
  stay **No verificado** with this literal reason: "Pendiente de calificar: la URL del despliegue se
  entrega por Moodle y no está disponible en esta pasada".
- **Do not open, curl or probe any deployment URL.**
- In those rows' Observaciones still record what the repository proves: whether the README or arc42
  section 7 declare a public URL (and which), and whether the health route exists in code, with
  `ruta:línea`.

Read first: `fichas/semana-08-evidencia-s8.md`, `CONTRATO.md` (section 11, §12 and §13),
`EQUIPOS.md`, and each team's existing preliminary report.

Step 0 — ephemeral clone and eligible revision:

```
$DIR="C:\Users\jairo\AppData\Local\Temp\opencode\s8-<equipo>"
if (Test-Path $DIR) { Remove-Item -Recurse -Force $DIR }
git clone --filter=blob:none --no-checkout -q "https://github.com/ISCOUTB/<REPO>.git" $DIR
git -C $DIR rev-list -1 --before="2026-09-28T05:00:00Z" origin/master        # o origin/main
git -C $DIR log -1 --format="%H %cI %s" <hash elegible>
```

Read with `git -C $DIR show <hash>:<ruta>`, `ls-tree -r --name-only`, `grep -nIE '<regex>'`,
`shortlog -sne`. For the pipeline, at most ONE unauthenticated call to
`https://api.github.com/repos/ISCOUTB/<REPO>/actions/runs?per_page=10`; on failure or 403, do not
retry and record it. Delete the clone when the team is done. Never use `gh` or an authenticated
session. Never check out.

Step 1 — the 10 graded ficha rows (the other two are the deferred ones above):

1. Infrastructure as code versioned in the repository (Dockerfile, docker-compose, `.tf/.tfvars`,
   `k8s/`, `helm/`, `fly.toml`, `render.yaml`, railway, Procfile).
2. The environment can be recreated following the README.
3. Pipeline green on the main branch (last run: name, conclusion, URL).
4. Structured logs (configuration file plus a sample line with fields; regex
   `structlog|winston|pino|logback|serilog|logging\.config|json.*formatter`).
5. Queryable metric tied to a quality scenario (metric name and which scenario; a metric without a
   scenario is incomplete).
6. Secrets out of code and taken from the environment or a store (`.env.example`, `secrets.X`
   references in workflows, versioned `.env`).
7. Monthly cost estimate with assumptions and the free-tier breaking point (a document with the
   assumed volume and the calculation; the provider catalogue alone is not enough).
8. arc42 section 7 with one box per piece and where it runs (`docs/arc42/07*`).
9. Cost limit and no-card restriction in section 2 (`docs/arc42/02*`).
10. One ADR per platform decision, with the discarded alternative and the free tier verified.

Step 2 — transverse matrix: EXACTLY these nine rows, in this order, each with cited evidence:
"Repositorio en la organización, con el nombre de la convención y público", "Estructura mínima
presente", "Estado calificado identificable", "Nombres de ADR según la convención", "ADR aceptados
no reescritos", "docs/ia.md al día para la semana", "Pipeline, SonarCloud y Quality Gate públicos
(desde S6)", "Sin credenciales en el repositorio ni en el historial", "Contribución de todos los
integrantes".

- "ADR aceptados no reescritos": run `git log --follow` per accepted ADR; edited afterwards without
  a declared replacement → No cumple with hash and date (history up to the graded revision only).
- "Contribución": `shortlog -sne` consolidated by identical email (NEVER by similar name) against
  the members declared in `EQUIPOS.md`.
- "docs/ia.md al día": the file must grow inside the period and document what was rejected and why.

Step 3 — rewrite `revisiones/2026-2/<REPO>/semana-08-evidencia-s8.md`:

- Header: replace the preliminary marker with
  `> Revisión definitiva: hash <hash>, última revisión ≤ cierre (2026-09-28T05:00:00Z) en <rama>.`,
  keep "Estado revisado" with hash and date, and set `Revisor` to
  `auditoría local sobre clon público efímero`.
- Both matrices complete, plus the overall section at the current tip of the same branch, listing
  post-cutoff commits.
- "Recuento y nota sugerida": `n de 10 criterios graduables`, with:
  **propuesta provisional al docente — `nota = 1 + 4 × (n/10)`; quedan 2 filas de despliegue
  pendientes de calificar y la nota final la fija el profesor en Moodle**.
- "No verificado / pendientes" and "Hallazgos para la planilla" consistent with the matrix.
- `planilla.md`: the week's row with the provisional `n/10` and the two deferred rows.
- `feedback.md`: the week 8 section, with no names, emails, hashes or scores.

Rules: `Cumple` only with cited evidence (`ruta:línea` + hash); `No cumple` with evidence of
absence; `No verificado` only when the check needs running the system, credentials, the deferred URL
or the sustentación — **never because a readable file was not read**. Do not demand alerts or
distributed tracing (outstanding level). Do not compare deployment alternatives (that is the
workshop, graded separately). Do not accept a screenshot as a substitute for the URL. Do not touch
`resumen-s8.md`, `estado-s8.json`, or another team's reports.

Return per team, compact (no full matrices): branch and hash used; whether the published revision
changed; one line per row with the final state and a very short citation; `n/10` and the score;
files touched; anything you could not decide and why; and confirmation that the clone was deleted,
that you ran no student code and that you opened no deployment URL.

## Progress

Round 1 launched.

## Next step

Run T6, then publish the week on the instructor's word.

## Result of T6

Independent recount: 23 reports, each with exactly 12 rows and exactly 2 deferred, `n/10` and note
matching `resumen-s8.md` and every `planilla.md`; 197 of 230 gradable criteria Cumple. Headers all
mark the definitive revision. No other ficha row is left "No verificado". Repository
counter-check on four teams (GimnasioUTB, ShareU, LaPlacita, TRACTAR), 24 rows: none unsupported.

Fixes applied after verification: the deferred reason had landed in the wrong column in LaPlacita
and LostVault; GimnasioUTB and InvenTrack wrote the note with a decimal comma; and GimnasioUTB's
cost row now records that the volume, per-piece cost and breakpoint do exist in the workshop
document, which is a separate deliverable graded apart.

Known cosmetic leftovers: `.atl/` stays untracked (never staged); `EQUIPOS.md` and the README still
use the old TRACTAR repository name.
