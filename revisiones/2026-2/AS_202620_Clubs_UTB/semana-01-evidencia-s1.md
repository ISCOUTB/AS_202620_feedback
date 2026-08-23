# Evidencia S1 · Clubs UTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `c92595edd1ff16f493517d99ab082932bc377f51` · 2026-08-09T13:25:24-05:00 · «Add files via upload» |
| Cierre | 2026-08-10T05:00:00Z (domingo 9 de agosto medianoche, UTC-5) |
| Comandos principales ejecutados | `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only c92595ed`; `git show c92595ed:docs/...`; `git shortlog -sne c92595ed`; `git grep` de secretos |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | Clon público sin autenticación OK; `revisiones/2026-2/_meta/lsremote.txt` | Cumple | `AS_202620_Clubs_UTB` sigue la convención y es público. |
| Integrantes del equipo con acceso | `git shortlog -sne c92595ed` | No verificado | Historial S1 con 3 identidades de 4: `Josh4OP` (1), `Luis-Salas-Reyes` (1), `Zavod Dev` (1). Hollman Jose De Orta Gonzalez no aparece en S1 (sí en S2 como `deortahollman-star`). Sin API de GitHub no se puede comprobar la lista de colaboradores en S1. |
| Equipo de 3 o 4 personas | EQUIPOS.md, fila Clubs UTB | Cumple | 4 integrantes declarados. |
| Ficha del problema con usuarios y alcance | `git ls-tree -r --name-only c92595ed` | No cumple | No existe ficha del problema en el árbol S1 (`docs/ficha_problema.md` llega el 2026-08-15). El texto del problema está en `docs/aspectos.md`, sin usuarios ni alcance. |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `docs/aspectos.md` en `c92595ed` | No cumple | No hay ninguna tensión de calidad declarada en S1. |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `c92595ed` | No cumple | El archivo es la descripción general del proyecto (problema, tecnologías, estado, autores), no la tabla de 8 columnas, y no declara ningún aspecto. |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` en `c92595ed` | Cumple | Contenido real: herramientas contempladas, usos previstos, revisión y validación por el equipo, y declaración de no incorporar IA al producto. |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `git ls-tree -r --name-only c92595ed` | No cumple | `docs/arc42/` no existe en el árbol S1. |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree -r --name-only c92595ed` | No cumple | No existen en el árbol S1 (sin `.gitkeep`; observación de montaje). |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt` OK; clon sin autenticación OK | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | `git ls-tree -r --name-only c92595ed` | No cumple | Solo `docs/aspectos.md` y `docs/ia.md`. Faltan `README.md` (renombrado a `docs/aspectos.md` en `2300453`), `docs/arc42/`, `docs/adr/` y `docs/c4/`. |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` | Cumple | Hash `c92595ed…` con `%cI` 2026-08-09T13:25:24-05:00. |
| Nombres de ADR según la convención | sin `docs/adr/` en S1 | Cumple (vacuo) | Sin ADR todavía. |
| ADR aceptados no reescritos | sin ADR | Cumple (vacuo) | Ídem. |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia.md` | Cumple | Único commit `c92595e` (2026-08-09), dentro del periodo S1. Sin entradas de usos reales ni de rechazos (no exigido en S1). |
| Sin credenciales en el repositorio ni en el historial | `git grep` (regex §9), `.env`, `git log -S'BEGIN PRIVATE KEY'` | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | `git shortlog -sne c92595ed` | No verificado | 3 identidades de 4 (falta Hollman Jose De Orta Gonzalez). Acceso del 4º no comprobable sin API. «Zavod Dev» se atribuye a Diego Andres Ramos De Avila por el correo `diegojesusyohe` y eliminación, sin confirmación oficial. |

## Recuento de criterios

- Ficha: **2 de 9** criterios Cumple.

## No verificado / pendientes

- Acceso de Hollman Jose De Orta Gonzalez en la semana 1 (requiere lista de colaboradores o matrícula).
- Atribución oficial de las cuentas `Zavod Dev` (¿Diego Andres Ramos De Avila?) y del resto contra la matrícula.

## Hallazgos para la planilla

- Ficha del problema inexistente en S1 (creada el 2026-08-15, después del cierre S1).
- `docs/aspectos.md` arrancó como un README renombrado y nunca llegó a ser la tabla de 8 columnas.
- Estructura sin montar en S1: sin `README.md` (se renombró), sin `docs/arc42/`, `docs/adr/`, `docs/c4/`.
- Hollman Jose De Orta Gonzalez sin commits en el historial S1.
- Sin entregas tardías en S1 (el trabajo de arc42 llegó entre el 08-12 y el 08-16, dentro del periodo S2).
