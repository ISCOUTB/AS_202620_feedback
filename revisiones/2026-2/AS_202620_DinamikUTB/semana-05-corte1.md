# semana-05-corte1 · DinamikUTB

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión preliminar del 2026-09-03. No existe la etiqueta `corte-1`; se calificó el último commit anterior al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado calificado | sin etiqueta `corte-1`; último commit ≤ cierre: `f89564fd616716b9dbfa0769ed1e38b606a12713` (`2026-09-06T23:35:03-05:00`, *Create correcciones.md*) |
| Cierre | `2026-09-07T05:00:00Z` |
| Comandos ejecutados | `git tag --list` (vacío); `git log --until=... HEAD`; `git ls-tree -r --name-only`; `git log --format=...` completo; `git log --diff-filter=A -- docs/adr/`; lectura de `docs/adr/0003-*.md`, `docs/aspectos.md`, `docs/ia.md`; `git grep` de secretos (exit 1); `git shortlog -sne`; `curl .../actions/runs?per_page=15` (1 llamada) |
| Restricción asignada | No disponible en el kit ni citada explícitamente como tal en el repositorio. |

El equipo incluye `correcciones.md` en la raíz del commit calificado; se adjudica en la sección dedicada más abajo.

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| 1. Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` sin salida | **No cumple** | Se calificó el último commit ≤ cierre: `f89564fd`, `2026-09-06T23:35:03-05:00`. |
| 2. PDF de dos páginas | No hay PDF en el repositorio | **No verificado** | Debe comprobarse en Moodle. |
| 3. Impacto de la restricción en requisitos, C4 y código | `docs/adr/0003-seleccion-motor-de-base-de-datos.md` formaliza una decisión que `02-architecture-constraints.md` (§2.1) ya dejaba como "pendiente" desde S2/S3 (elegir SQL o NoSQL) | **No cumple** | El ADR-0003 resuelve una brecha documental de la línea base (motor de BD ya usado desde S4), no diagnostica una restricción nueva asignada externamente para este corte. |
| 4. Línea base medida y verificable | Ningún escenario Q-01…Q-08 reporta una medición real antes del cambio; ADR-0003 discute alternativas cualitativamente, sin cifra de partida | **No cumple** | — |
| 5. ADR del reto | ADR-0003 sí tiene contexto, alternativas (SQLite/PostgreSQL/MySQL/NoSQL), factores, decisión, consecuencias y trazabilidad completa | **No cumple** | Cumple el formato competente de un ADR, pero no responde a una restricción nueva asignada: formaliza el motor ya implementado desde el corte vertical de S4. |
| 6. Cambio implementado extremo a extremo | El motor SQLite ya estaba implementado desde S4 (`backend/app/core/database.py`); ADR-0003 no introduce cambio de código, solo documentación | **No cumple** | No hay commit de código nuevo asociado al ADR-0003. |
| 7. Límites C4 conservados | `docs/c4/contenedores.puml` ya reflejaba `ContainerDb` (SQLite) antes de ADR-0003 | **No verificado** | No hay cambio de código que contrastar contra el C4. |
| 8. Prueba que cubre el cambio, en verde en pipeline | `curl .../actions/runs`: `f89564fd` success (`2026-09-07T04:35:05Z`, antes del cierre) | **No cumple** | El run verde cubre la suite existente (backend/frontend), no una prueba nueva del reto: no hay cambio de código que probar. |
| 9. Resultado contrastado con umbral | Sin medición reportada | **No cumple** | — |
| 10. Cadena de trazabilidad navegable | `docs/aspectos.md` tiene 9 columnas (`ID…Evidencia`); siguiendo A-08 ("Historial de cambios"): llega a Q-08, ADR-0003 (parcial), pero Código/Pruebas/Evidencia = "Pendiente" | **No cumple** | La cadena se rompe en Código/Pruebas/Evidencia para el aspecto que cita el ADR-0003. |
| 11. Salida de IA con motivo técnico, de este corte | `docs/ia.md`: entrada `06/09/2026` "Formalizar la decisión del motor de base de datos..." con validación **Aceptado**, referida al ADR-0003 de este corte | **Cumple** | Hay una entrada fechada dentro de la ventana de S5, referida al trabajo de este corte, con motivo técnico. |
| 12. Sustentación del reto | — | **No verificado** | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| a. Repositorio en la organización, convención y público | Clon anónimo exitoso de `github.com/ISCOUTB/AS_202620_DinamikUTB` | **Cumple** | — |
| b. Estructura mínima | `git ls-tree` en `f89564fd`: `README.md`, `docs/arc42/` (12 secciones), `docs/adr/` (3 ADR), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` presentes | **Cumple** | — |
| c. Estado calificado identificable | Sin etiqueta; `f89564fd`, `2026-09-06T23:35:03-05:00` | **No cumple** | Falta la etiqueta `corte-1`. |
| d. Nombres de ADR según convención | `0001-seleccion-monolito-modular.md`, `0002-seleccion-tecnologia-backend-frontend.md`, `0003-seleccion-motor-de-base-de-datos.md` | **Cumple** | — |
| e. ADR aceptados no reescritos | ADR-0003 declara explícitamente que no reemplaza ni modifica 0001/0002 | **Cumple** | — |
| f. `docs/ia.md` al día para la semana | Entrada de `06/09/2026` sobre ADR-0003 | **Cumple** | — |
| g. Sin credenciales | `git grep` con la regex del contrato: exit 1; sin `.env` versionado | **Cumple** | — |
| h. Contribución de todos los integrantes | `git shortlog -sne f89564fd`: JuanchisV/404Vargas/Juan José Vargas (misma persona) 104, Daniel-dev02/LUIS DANIEL (misma persona) 37, gillianisperez-prog 23, Eramirezr 7 | **Cumple** | 4 identidades consolidadas para 4 integrantes; distribución muy desigual (Juan José Vargas concentra ~60% de los commits), anotar para sustentación. |

## Estado global del proyecto (overall · HEAD)

HEAD coincide con el estado calificado (`f89564fd`). El proyecto tiene una línea base madura (arc42 completo, 3 ADR bien formados, C4, pipeline verde, `docs/ia.md` con entradas hasta este corte) y el equipo usó la ventana de S5 para **formalizar deuda documental de la línea base** (ADR-0003 sobre el motor de BD) en lugar de responder a una restricción nueva. No se creó la etiqueta `corte-1`. El último commit del estado calificado es precisamente la creación de `correcciones.md`.

## Correcciones del equipo

`correcciones.md` (raíz del commit calificado) no contradice ninguna fila de la revisión preliminar de **este corte** (semana-05-corte1): es una autoevaluación del propio equipo sobre las semanas **S1 a S4**, marcando en bloque "Cumple" para cada punto, sin citar evidencia verificable más allá de rutas de archivo, y sin mencionar la restricción asignada a este corte ni ninguna fila de la matriz de corte1. Además, la ficha es explícita en que **S1-S4 son línea base y no se recalifican por existir**: su nota ya está puesta y no corresponde reabrirla aquí.

| Corrección (agrupada) | Adjudicación | Justificación |
|---|---|---|
| S1 (5 puntos: tensión de calidad, ficha en Markdown, contribución, ia.md, estructura) | **Rechazada** | Corresponde a la semana 1, ya calificada y fuera de alcance de esta revisión; el archivo no cita evidencia nueva, solo afirma "Cumple". |
| S2 (5 puntos: enlaces de escenarios, condiciones de carga, ia.md, C4 nivel 1, contribución) | **Rechazada** | Mismo motivo: semana ya calificada; autoafirmación sin evidencia verificable citada en el propio archivo. |
| S3 (6 puntos: tácticas, matriz comparativa, aspectos con ADR, trazabilidad, ia.md, contribución) | **Rechazada** | Mismo motivo. |
| S4 (7 puntos, incluyendo "existencia de etiqueta" y "commits post-cierre") | **Rechazada** | Mismo motivo; además el punto S4-06 ("existencia de un tag") es contradicho por la evidencia real: no existe ninguna etiqueta en el repositorio, ni siquiera al cierre de S5. |
| "Elementos implementados" (14 filas: C4, arc42, ADR-0001/0002, ia.md, aspectos, backend, frontend, pruebas, start.bat) | **Rechazada como corrección al corte1** | Estos elementos ya se evaluaron en S1-S4; no aportan evidencia sobre la restricción nueva de S5, que sigue sin diagnóstico, ADR ni medición propios. |

No hay ninguna corrección en el archivo dirigida específicamente a una fila de la matriz de `semana-05-corte1` publicada preliminarmente (por ejemplo, no se disputa "no cumple" en línea base medida, ADR del reto o pipeline en verde para el cambio); por eso todas las filas del archivo se adjudican como fuera de alcance de esta revisión.

## Nivel de rúbrica sugerido (propuesta al docente)

| Criterio | Nivel | Puntaje | Evidencia |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia | 0,00 | ADR-0003 formaliza una decisión pendiente de la línea base, no una restricción nueva diagnosticada. |
| Alternativas y decisión | Nivel básico, sin escenario del reto | 0,00 | ADR-0003 tiene alternativas y consecuencias bien formadas, pero no está ligado a una restricción de este corte. |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | No hay cambio de código nuevo asociado a una restricción de S5. |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | Pipeline verde sobre la suite existente; sin medición ni umbral del reto. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico verificable** | | **0,00 / 4,00** | La nota final la fija Moodle. |

## Recuento

**1 de 12 criterios Cumple** (salida de IA con motivo técnico de este corte).

## No verificado

- PDF adjunto en Moodle.
- Coincidencia del diagnóstico con la restricción asignada (no disponible).
- Conservación de límites C4 (sin cambio de código que contrastar).
- Sustentación del reto.

## Hallazgos

- No existe la etiqueta `corte-1`; se calificó el último commit anterior al cierre.
- El trabajo de S5 (ADR-0003) formaliza una decisión pendiente de la línea base, no responde a una restricción nueva asignada.
- No hay medición de línea base ni resultado contra un umbral en ningún artefacto.
- `docs/ia.md` sí tiene una entrada fechada y referida a este corte (único criterio que cumple).
- `correcciones.md` es una autoevaluación de S1-S4 sin evidencia verificable citada y fuera del alcance de esta revisión (esas semanas no se recalifican).
- Distribución de commits muy concentrada en un integrante.

## Preguntas para la sustentación

1. ¿Cuál fue la restricción nueva asignada para este corte, y por qué el ADR-0003 formaliza una decisión (el motor de base de datos) que ya estaba pendiente desde S2/S3 en lugar de responder a ella?
2. ¿Cuál es la cifra de línea base medida antes de cualquier cambio de este corte, con qué herramienta y procedimiento se obtuvo?
3. ¿Por qué no se creó la etiqueta `corte-1` antes del cierre?
