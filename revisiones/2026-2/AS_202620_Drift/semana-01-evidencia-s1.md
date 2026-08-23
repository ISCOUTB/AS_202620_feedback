# Evidencia S1 · Drift

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `b7ec296c740891ded6120c7efb8c0f77869dfd56` · 2026-08-09T22:59:42-05:00 · «Fix formatting of checklist in aspectos.md» |
| Cierre | 2026-08-10T05:00:00Z (domingo 9 de agosto medianoche, UTC-5) |
| Comandos principales ejecutados | `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only b7ec296c`; `git show b7ec296c:docs/...`; `git shortlog -sne b7ec296c`; `git grep` de secretos |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | Clon público sin autenticación OK; `revisiones/2026-2/_meta/lsremote.txt` | Cumple | `AS_202620_Drift`, público. |
| Integrantes del equipo con acceso | `git shortlog -sne b7ec296c` | No verificado | Historial S1 con 2 identidades de 4: `maufern4ndez` (7) y `lmpdiaz12` (4). Jerry Daniel Buelvas Mejia y Joshua David Reyes Leones no aparecen en S1 (sí en S2 como `JerryDBM` y `JoshuaR01`/`JoshXX`). Sin API no se comprueba la lista de colaboradores en S1. |
| Equipo de 3 o 4 personas | EQUIPOS.md, fila Drift | Cumple | 4 integrantes declarados. |
| Ficha del problema con usuarios y alcance | `docs/ficha_problema.md` en `b7ec296c` | Cumple | Usuarios declarados (los «jugadores», de forma implícita, sin sección propia) y alcance en «Propuesta de solución» (comparar precios, historial, rendimiento en PC). |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `docs/ficha_problema.md` y README | No cumple | No hay tensiones de calidad; solo un aspecto priorizado (mantenibilidad) en `docs/aspectos.md`, sin enfrentamiento entre atributos. |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `b7ec296c` | No cumple | El aspecto (mantenibilidad) está descrito en prosa: no usa la tabla de 8 columnas del curso y no hay ID de aspecto. |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` en `b7ec296c` (commits `b3a8522`…`73e51a0`, 2026-08-09) | Cumple | Propósito, uso actual de ChatGPT y herramientas previstas con contenido real. |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `git ls-tree -r --name-only b7ec296c` | No cumple | `docs/arc42/` no existe en el árbol S1. |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree -r --name-only b7ec296c` | No cumple | No existen en el árbol S1 (sin `.gitkeep`; observación de montaje). |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt` OK; clon sin autenticación OK | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | `git ls-tree -r --name-only b7ec296c` | No cumple | 3 de 6: `README.md`, `docs/aspectos.md`, `docs/ia.md`. Faltan `docs/arc42/`, `docs/adr/`, `docs/c4/`. |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` | Cumple | Hash `b7ec296c…` con `%cI` 2026-08-09T22:59:42-05:00. |
| Nombres de ADR según la convención | sin `docs/adr/` | Cumple (vacuo) | Sin ADR todavía. |
| ADR aceptados no reescritos | sin ADR | Cumple (vacuo) | Ídem. |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia.md` | Cumple | 4 commits del 2026-08-09 dentro del periodo. Sin entradas de rechazos (pendiente). |
| Sin credenciales en el repositorio ni en el historial | `git grep` (regex §9), `.env`, `git log -S'BEGIN PRIVATE KEY'` | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | `git shortlog -sne b7ec296c` | No verificado | 2 identidades de 4 en S1 (Jerry y Joshua ausentes). Su acceso en S1 no es comprobable sin API. |

## Recuento de criterios

- Ficha: **4 de 9** criterios Cumple.

## No verificado / pendientes

- Acceso de Jerry Daniel Buelvas Mejia y Joshua David Reyes Leones en la semana 1 (requiere lista de colaboradores o matrícula; ambos aparecen en S2).

## Hallazgos para la planilla

- Sin tensiones de calidad en la ficha (se pedían dos).
- `docs/aspectos.md` en prosa, no la tabla de 8 columnas (se arrastra hasta S2).
- Estructura sin montar en S1 (sin arc42, adr, c4).
- Dos de los cuatro integrantes sin commits en S1.
