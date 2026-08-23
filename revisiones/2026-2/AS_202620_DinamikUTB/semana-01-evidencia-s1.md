# Evidencia S1 · DinamikUTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `769f9703546060710f62c002808cb583877d496c` · 2026-08-09T21:24:49-05:00 · «Update aspectos.md» |
| Cierre | 2026-08-10T05:00:00Z (domingo 9 de agosto medianoche, UTC-5) |
| Comandos principales ejecutados | `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only 769f970`; `git show 769f970:docs/...`; `pdftotext` sobre `docs/fichadelproblema.pdf`; `git shortlog -sne 769f970`; `git grep` de secretos |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | Clon público sin autenticación OK; `revisiones/2026-2/_meta/lsremote.txt` | Cumple | `AS_202620_DinamikUTB`, público. |
| Integrantes del equipo con acceso | `git shortlog -sne 769f970` | No verificado | Historial S1 con 3 identidades de 4: `Daniel-dev02` (8), `gillianisperez-prog` (3), `JuanchisV` (1). Esteban Ramirez Rios no aparece en S1 (sí en S2 como `Eramirezr`). Sin API no se puede comprobar la lista de colaboradores en S1. |
| Equipo de 3 o 4 personas | EQUIPOS.md, fila DinamikUTB | Cumple | 4 integrantes declarados. |
| Ficha del problema con usuarios y alcance | `docs/fichadelproblema.pdf` en `769f970` (texto extraído con `pdftotext`) | Cumple | §3 «A quién afecta» declara usuarios (estudiantes de últimos semestres, coordinaciones académicas) y §6 «Alcance inicial» (un programa académico, ampliable). Observación: entregada como PDF, no en Markdown (el curso prefiere documentación revisable en el repo). |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | README «Disponibilidad vs. Consistencia»; PDF §7 «Aspecto de calidad priorizado» | No cumple | Solo una tensión declarada (consistencia > disponibilidad). Se pedían dos. |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `769f970` | Cumple | Tabla de 8 columnas con A-01…A-06: ID y Aspecto rellenos, resto «Pendiente». |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` en `769f970` (commit `ef4a691`, 2026-08-09) | Cumple | Tabla con entrada real del 09/08/2026 (herramienta, prompt, resultado, validación). |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `docs/arc42/arc42-template-EN.md` en `769f970` | Cumple | Plantilla presente y en Markdown (versión EN). |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree -r --name-only 769f970` | Cumple | `docs/adr/.gitkeep` y `docs/c4/.gitkeep` presentes. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt` OK; clon sin autenticación OK | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | `git ls-tree -r --name-only 769f970` | Cumple | Las seis rutas: `README.md`, `docs/arc42/`, `docs/adr/` (`.gitkeep`), `docs/c4/` (`.gitkeep`), `docs/aspectos.md`, `docs/ia.md`. |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` | Cumple | Hash `769f970…` con `%cI` 2026-08-09T21:24:49-05:00. |
| Nombres de ADR según la convención | `docs/adr/` solo con `.gitkeep` | Cumple (vacuo) | Sin ADR todavía. |
| ADR aceptados no reescritos | sin ADR | Cumple (vacuo) | Ídem. |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia.md` | Cumple | `ef4a691` (2026-08-09) dentro del periodo; entrada real con validación. Sin columna de rechazos todavía (pendiente). |
| Sin credenciales en el repositorio ni en el historial | `git grep` (regex §9), `.env`, `git log -S'BEGIN PRIVATE KEY'` | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | `git shortlog -sne 769f970` | No verificado | 3 identidades de 4 (falta Esteban Ramirez Rios). Su acceso en S1 no es comprobable sin API. |

## Recuento de criterios

- Ficha: **7 de 9** criterios Cumple.

## No verificado / pendientes

- Acceso de Esteban Ramirez Rios en la semana 1 (requiere lista de colaboradores o matrícula; aparece en S2 como `Eramirezr`).
- El PDF de la ficha se evaluó extrayendo su texto con `pdftotext`; no se inspeccionó su maquetación.

## Hallazgos para la planilla

- Ficha del problema en PDF (no Markdown): anotar preferencia del curso por documentación revisable en el repositorio.
- Una sola tensión de calidad declarada (se pedían dos).
- Esteban Ramirez Rios sin commits en el historial S1.
- Estructura completa desde S1 (única de los cinco equipos revisados).
- Sin entregas tardías en S1.
