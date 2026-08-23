# Evidencia S1 · TAIA

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `76d4a916972819159a2d981302c0be8b82ffde79` · `2026-08-07T03:34:26-05:00` («chore: initialize repository and project documentation») |
| Cierre S1 | `2026-08-10T05:00:00Z` (domingo 9 de agosto medianoche, Colombia) |
| Comandos principales ejecutados | `git clone --filter=blob:none --no-checkout`; `git log -1 --until`; `git ls-tree -r --name-only $HASH`; `git show $HASH:...`; `git shortlog -sne`; `git grep` (secretos); `git log --after` (tardías) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:18` (`AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant OK`); protocolo git sin autenticación | Cumple | Visible y público |
| Integrantes del equipo con acceso | `git shortlog -sne 76d4a91`: solo `val` (1 commit) | No verificado | Sin API no se listan colaboradores. Hasta el cierre solo consta una cuenta; `luis20072002` (15-ago), `dei0811` y `mark` (16-ago) aparecen en la semana siguiente |
| Equipo de 3 o 4 personas | `EQUIPOS.md:33` | Cumple | 4 integrantes declarados |
| Ficha del problema con usuarios y alcance | `docs/ficha_problema.md` en `76d4a91` | Cumple | Usuarios objetivo y alcance del MVP declarados con claridad |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `git grep -niE 'tension|tensión|calidad' 76d4a91 -- docs`: sin resultados | No cumple | La ficha no declara tensiones entre atributos de calidad |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `76d4a91` | Cumple | Tabla de 8 columnas con ID `A-01` y requisito `RF-01` |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` en `76d4a91` | Cumple | Entrada 001 (06-ago) con herramienta, aceptado, rechazado y verificación |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `docs/arc42/arc42-template-EN.md` en `76d4a91` | Cumple | Un archivo Markdown con las 12 secciones |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree -r 76d4a91`: no existen `docs/adr/` ni `docs/c4/` | No cumple | Ninguno de los dos directorios creado al cierre de S1 |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:18` | Cumple | — |
| Estructura mínima presente | `git ls-tree -r 76d4a91`: `README.md`, `docs/arc42/`, `docs/aspectos.md`, `docs/ia.md`, `docs/ficha_problema.md`; faltan `docs/adr/` y `docs/c4/` | No cumple | Estructura incompleta al cierre de S1 |
| Estado calificado identificable | `76d4a916972819159a2d981302c0be8b82ffde79` · `2026-08-07T03:34:26-05:00` | Cumple | Commit anterior al cierre, sin etiqueta |
| Nombres de ADR según la convención | No existe `docs/adr/` | Cumple | Sin ADR; filtro vacío |
| ADR aceptados no reescritos | Sin ADR | Cumple | No aplica por ausencia |
| `docs/ia.md` al día para la semana | commit `76d4a91` (07-ago) dentro del periodo; Entrada 001 con aceptado, rechazado y verificación | Cumple | — |
| Sin credenciales en el repositorio ni en el historial | `git grep` regex §9 sobre `76d4a91`: sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'`: vacío | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne 76d4a91`: 1 persona de 4 | No cumple | Solo `val` antes del cierre; los otros tres no aparecen aún |

## Recuento de criterios

- **6 de 9** criterios cumplidos en la matriz de la ficha.

## No verificado / pendientes

- Acceso de los 4 integrantes en S1: sin API no se listan colaboradores; en el historial solo consta 1 cuenta hasta el cierre.

## Hallazgos para la planilla

- Sin entregas tardías: `76d4a91` dentro del plazo; el siguiente commit es del 15-ago.
- `docs/adr/` y `docs/c4/` no existían al cierre de S1 (se crean en S2).
- Sin tensiones de calidad en la ficha del problema.
- `val` firma con dos correos (`@email.com` y `@gmail.com`): una misma persona, consolidada.
