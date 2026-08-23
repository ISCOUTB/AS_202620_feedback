# Evidencia S1 · ElMapita

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `938d0206a9544e76fd77478c5a1fc98addc0af28` · 2026-08-07T21:36:01-06:00 · «correccion en aspectos» |
| Cierre | 2026-08-10T05:00:00Z (domingo 9 de agosto medianoche, UTC-5) |
| Comandos principales ejecutados | `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only 938d0206`; `git show 938d0206:docs/...`; `git cat-file -s` (ia.md); `git shortlog -sne 938d0206`; `git grep` de secretos |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | Clon público sin autenticación OK; `revisiones/2026-2/_meta/lsremote.txt` | Cumple | `AS_202620_ElMapita`, público. |
| Integrantes del equipo con acceso | `git shortlog -sne 938d0206` | No verificado | Historial S1 con una sola identidad: `RobotDRMX` (7 commits). La cuenta no es atribuible por nombre a ningún integrante de EQUIPOS.md (la correspondencia la establece el docente). Sin API no se comprueban colaboradores. |
| Equipo de 3 o 4 personas | EQUIPOS.md, fila ElMapita | Cumple | 3 integrantes declarados: Angel Fabian Gutierrez Gomez, Diego Rosales Garza, Rodrigo Vazquez Rico. |
| Ficha del problema con usuarios y alcance | `git ls-tree -r --name-only 938d0206` | No cumple | No existe ficha del problema en el árbol S1. El README declara beneficiarios (stakeholders) y describe la aplicación, pero no es la ficha de una página con problema, usuarios y alcance. |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | README y `docs/aspectos.md` en `938d0206` | No cumple | Ninguna tensión de calidad declarada; solo un aspecto (A-01) con un «tiempo de carga < 3 segundos» suelto, sin enfrentamiento entre atributos. |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `938d0206` | Cumple | Tabla de 8 columnas con A-01 (ID y Aspecto rellenos; resto «Pendiente») más descripción del aspecto. |
| `docs/ia.md` iniciado con contenido real | `git cat-file -s 938d0206:docs/ia.md` → 0 bytes | No cumple | El archivo existe desde el primer commit (`df1e2f7`) pero está vacío: sin contenido real. |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `docs/arc42/arc42-template-EN.md` (+ `images/arc42-logo.png`) | Cumple | Plantilla presente y en Markdown (versión EN). |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree -r --name-only 938d0206` | Cumple | `docs/adr/.gitkeep` y `docs/c4/.gitkeep` presentes. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt` OK; clon sin autenticación OK | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | `git ls-tree -r --name-only 938d0206` | Cumple | Las seis rutas: `README.md`, `docs/arc42/`, `docs/adr/` (`.gitkeep`), `docs/c4/` (`.gitkeep`), `docs/aspectos.md`, `docs/ia.md` (vacío, pero la ruta existe). |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` | Cumple | Hash `938d0206…` con `%cI` 2026-08-07T21:36:01-06:00. |
| Nombres de ADR según la convención | `docs/adr/` solo con `.gitkeep` | Cumple (vacuo) | Sin ADR todavía. |
| ADR aceptados no reescritos | sin ADR | Cumple (vacuo) | Ídem. |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia.md` | No cumple | Único commit `df1e2f7` (2026-08-07); el archivo está vacío (0 bytes) en el cierre S1. |
| Sin credenciales en el repositorio ni en el historial | `git grep` (regex §9), `.env`, `git log -S'BEGIN PRIVATE KEY'` | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | `git shortlog -sne 938d0206` | No verificado | Una sola identidad (`RobotDRMX`) sin atribuir a persona; no se puede establecer quién de los 3 integrantes falta sin la lista de colaboradores o la matrícula. |

## Recuento de criterios

- Ficha: **5 de 9** criterios Cumple.

## No verificado / pendientes

- Acceso de los 3 integrantes en la semana 1: el historial solo muestra `RobotDRMX`, sin atribución posible por nombre (requiere lista de colaboradores o matrícula).
- La cuenta `YOOUYII` (observada en EQUIPOS.md) nunca aparece en el historial de este repositorio.

## Hallazgos para la planilla

- `docs/ia.md` vacío desde el primer commit (se arrastra hasta S2).
- Sin ficha del problema (el README la suple parcialmente).
- Sin tensiones de calidad.
- Todo el historial S1 es de una sola cuenta no atribuible.
