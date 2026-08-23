# Evidencia S1 · Calificación automática

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `4f6f56872fe62978d396737be30dd7520795fa36` · `2026-08-09T13:16:43-05:00` («Añadida la plantilla arc42») |
| Cierre S1 | `2026-08-10T05:00:00Z` (domingo 9 de agosto medianoche, Colombia) |
| Comandos principales ejecutados | `git clone --filter=blob:none --no-checkout`; `git log -1 --until`; `git ls-tree -r --name-only $HASH`; `git show $HASH:...`; `git shortlog -sne`; `git grep` (secretos); `git log --after` (tardías) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:17` (`AS_202620_Sistema-de-calificacion-automatica OK`); protocolo git sin autenticación | Cumple | Visible y público |
| Integrantes del equipo con acceso | `git shortlog -sne 4f6f568`: solo `scp1109` (11 commits) | No verificado | Sin API no se listan colaboradores. Hasta el cierre solo consta una cuenta; `josueacademico17-source` empuja recién el 22-ago y no hay cuentas de los otros dos integrantes |
| Equipo de 3 o 4 personas | `EQUIPOS.md:32` | Cumple | 4 integrantes declarados |
| Ficha del problema con usuarios y alcance | No hay ficha en el repositorio al cierre de S1 (`git ls-tree -r 4f6f568`) | No verificado | El README (8 líneas) describe el sistema y `docs/aspectos.md` declara usuarios por aspecto, pero no hay documento de ficha con usuarios y alcance. El equipo cita un «Informe Inicial» entregado en Moodle; haría falta ese PDF o subir la ficha al repositorio |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `docs/aspectos.md` en `4f6f568`, sección «Tensiones de calidad identificadas» | Cumple | Dos tensiones bien formuladas y enfrentadas (precisión OCR vs tolerancia a caligrafía; determinismo sintáctico vs equivalencia matemática). Observación: declaradas en `docs/aspectos.md`, no en la ficha |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` en `4f6f568`, tabla de trazabilidad | Cumple | Tabla de 8 columnas del curso con ID `A-01` y requisito `RF-01` rellenos |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` en `4f6f568` | Cumple | Entrada 1 (07-ago) con herramienta, qué se aceptó, qué se rechazó y justificación |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `docs/arc42/arc42-template-ES.md` en `4f6f568` | Cumple | Un archivo Markdown con las 12 secciones (líneas 21–200) |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree 4f6f568`: `docs/adr` y `docs/c4` como blobs vacíos (hash `8b137891`) | Cumple | Los caminos existen pero son archivos vacíos, no directorios: git no versiona directorios vacíos y el equipo los «creó» como blobs. Se anota como observación de montaje |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:17` | Cumple | — |
| Estructura mínima presente | `git ls-tree -r 4f6f568`: `README.md`, `docs/arc42/arc42-template-ES.md`, `docs/adr` (blob), `docs/c4` (blob), `docs/aspectos.md`, `docs/ia.md` | Cumple | `docs/adr` y `docs/c4` son blobs vacíos, no directorios (observación de montaje) |
| Estado calificado identificable | `4f6f56872fe62978d396737be30dd7520795fa36` · `2026-08-09T13:16:43-05:00` | Cumple | Commit anterior al cierre, sin etiqueta |
| Nombres de ADR según la convención | `docs/adr` sin contenido | Cumple | Sin ADR todavía |
| ADR aceptados no reescritos | Sin ADR | Cumple | No aplica por ausencia |
| `docs/ia.md` al día para la semana | commits `8587185` (07-ago) y `dcee1a9` (08-ago) dentro del periodo; Entrada 1 con lo aceptado, lo rechazado y su motivo | Cumple | — |
| Sin credenciales en el repositorio ni en el historial | `git grep` regex §9 sobre `4f6f568`: sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'`: vacío | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne 4f6f568`: 1 persona de 4 | No cumple | Solo `scp1109` antes del cierre; no aparecen cuentas de los otros tres integrantes |

## Recuento de criterios

- **7 de 9** criterios cumplidos en la matriz de la ficha (2 filas No verificado, sin No cumple).

## No verificado / pendientes

- Acceso de los 4 integrantes en S1: sin API no se listan colaboradores; en el historial solo consta 1 cuenta hasta el cierre.
- Ficha del problema: no está en el repositorio; haría falta el PDF del «Informe Inicial» de Moodle o subir la ficha al repo.

## Hallazgos para la planilla

- Sin entregas tardías: commit calificado `4f6f568` dentro del plazo; siguiente commit ya el 16-ago.
- Montaje con blobs vacíos en lugar de directorios para `docs/adr` y `docs/c4` (git no versiona directorios vacíos; conveniente migrar a `.gitkeep`).
- Ficha del problema fuera del repositorio (se referencia un Informe Inicial de Moodle).
- Solo 1 cuenta contribuyendo (`scp1109`); los demás integrantes no aparecen en el historial.
