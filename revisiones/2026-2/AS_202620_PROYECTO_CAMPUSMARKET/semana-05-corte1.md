# Semana 5 · Primer corte · CampusMarket

> Revisión definitiva post-cierre — 2026-09-07. Reemplaza la revisión manual preliminar del 2026-09-03, que no pudo ver este trabajo porque se hizo después. Cierre: `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado calificado | etiqueta `corte-1` → `8044215811e53b111888f75b30fc175fb889dc56` (2026-09-06T16:05:15-05:00 / 21:05:15Z) — anterior al cierre |
| HEAD para el overall | igual al estado calificado; no hay commits posteriores a la etiqueta |
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log -1 corte-1`; `git ls-tree corte-1`; lectura de `correcciones.md`, `docs/adr/0002-manejo-bloqueo-sqlite.md`, `docs/aspectos.md`, `backend/tests/test_publicaciones_vertical.py`, `scripts/medir_bloqueo_sqlite.py`, `docs/ia.md`, `README.md`; `git log --follow` sobre ADR-0001; `git shortlog -sne HEAD`; `git grep` (secretos); una consulta a `GET /repos/.../actions/runs` |
| Revisor | agente de revisión, solo lectura; no se ejecutó código del equipo (la reproducibilidad se evaluó por documentación y por el run de CI, no reejecutando el test) |
| Alcance externo no disponible | PDF de Moodle. La restricción asignada sí quedó localizada: **R-07 — Persistencia sin nueva infraestructura durante el primer corte**, declarada por el propio equipo en `docs/arc42/02-restricciones.md` y consistente con el resto de la cadena de trazabilidad. |

## Nota

Este equipo hizo la mayor parte de su trabajo de corte 1 el 5 y 6 de septiembre, **después** de la revisión preliminar del 03/09 (que por eso encontró 0/12). Toda esa actividad es anterior al cierre `2026-09-07T05:00:00Z` y la etiqueta `corte-1` la contiene íntegra: es la primera de las cinco de este lote donde la etiqueta corresponde de verdad al trabajo del reto.

## Matriz de la ficha (evaluada sobre `corte-1` = `8044215`)

| Criterio de evaluación | Estado | Observaciones |
|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Cumple | `8044215` del 06/09 21:05Z, anterior al cierre del 07/09 05:00Z. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No verificado | El adjunto de Moodle no está disponible en el kit. |
| Impacto de la restricción localizado en requisitos, C4 y código | Cumple | R-07 en `docs/arc42/02-restricciones.md`; EC-05 en `docs/arc42/10-escenarios-de-calidad.md`; C4 Nivel 2 en `docs/c4/02-contenedores.md`; código en `backend/app/publicaciones/{repository,service,router}.py`. Cadena consistente en las cuatro capas. |
| Línea base medida y verificable antes del cambio | Cumple | `docs/evidencias/linea-base-bloqueo-sqlite-2026-09-05.md` y `docs/adr/0002-manejo-bloqueo-sqlite.md` §1 registran HTTP `500`, `7.323 s`, sin escritura parcial, con el procedimiento (bloqueo `BEGIN EXCLUSIVE` sobre SQLite) reproducido en `scripts/medir_bloqueo_sqlite.py`. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Cumple | `docs/adr/0002-manejo-bloqueo-sqlite.md`: 3 alternativas con ventajas/desventajas, fuerzas explícitas, decisión, consecuencias positivas y negativas, criterio de reconsideración cuantificado ("más del 5% de 100 intentos...") y costo de reversión declarado — cubre el nivel sobresaliente de la rúbrica. |
| Cambio implementado y ejecutable de extremo a extremo | Cumple | PR #28 y commit de integración `ff68cf2`; el arranque de un comando (`scripts/run_s4.ps1`/`.sh`) sigue documentado en el README y no cambió con el reto. |
| Límites declarados conservados tras el cambio | Cumple | El ADR declara explícitamente que la topología `Flutter → FastAPI → publicaciones → SQLite` no cambia; el cambio queda localizado en `repository.py`/`service.py`/`router.py`, sin nuevos contenedores. |
| Prueba que cubre el cambio, en verde en el pipeline | Cumple | `backend/tests/test_publicaciones_vertical.py::test_bloqueo_sqlite_degrada_controladamente_y_se_recupera` reproduce el bloqueo con `sqlite3` + `BEGIN EXCLUSIVE` y verifica HTTP 503, tiempo ≤2s, ausencia de escritura parcial y recuperación posterior. El run de GitHub Actions sobre el commit de la propia etiqueta (`80442158`) terminó en `success` el 2026-09-06T21:05:18Z: https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/34059972075 |
| Resultado contrastado con el umbral del escenario y reproducible | Cumple | Tabla comparativa línea base vs. después vs. umbral en el ADR §11 (500→503, 7.323s→1.283s frente a umbral ≤2s); `scripts/medir_bloqueo_sqlite.py` permite repetir la medición con el mismo procedimiento. |
| Cadena aspecto→requisito→C4→ADR→código→pruebas→evidencia navegable | Cumple | Fila `ASP-06` de `docs/aspectos.md` recorrida celda a celda: llega a requisito (R-07/EC-05), C4 Nivel 2, ADR-0002, cinco archivos de código, la prueba y las dos evidencias de medición. Ninguna celda queda en el vacío. |
| Salida de IA aceptada/corregida/rechazada con motivo técnico | Cumple | `docs/ia.md`, sección "Evidencia S5": entradas del 04 y 05/09 con rechazos explícitos y motivo técnico ("Se rechazó marcar elementos como saneados sin evidencia..."; "se rechazó modificar ADR-0001 solo para agregar trazabilidad posterior"). |
| Sustentación del reto | No verificado | Lo resuelve el docente en la sesión. |

**Recuento: 9 de 12** (2 No verificado por diseño — PDF y sustentación —, 0 No cumple).

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Observaciones |
|---|---|---|
| a. Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon sin autenticación de `ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` responde el 2026-09-07. |
| b. Estructura mínima presente | Cumple | `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`, `README.md` en `corte-1`, todos en minúsculas y en la ruta contractual. |
| c. Estado calificado identificable | Cumple | `corte-1` = `8044215`, y ese estado corresponde efectivamente al corte 1 (no a una semana anterior). |
| d. Nombres de ADR según la convención | Cumple | `0001-usar-monolito-modular.md` y `0002-manejo-bloqueo-sqlite.md`, ambos con título de la decisión en kebab-case. |
| e. ADR aceptados no reescritos | Cumple | `docs/adr/0001-usar-monolito-modular.md` tiene un único commit de creación (`dbdd9c4`, 23/08; `git log --follow` no muestra reescrituras); ADR-0002 es un archivo nuevo, no una edición del 0001. |
| f. `docs/ia.md` al día para la semana | Cumple | Sección "Evidencia S5" con entradas del 04 y 05/09, con lo rechazado y su motivo. |
| g. Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` con los patrones del contrato sin coincidencias en HEAD; sin `.env` versionado. |
| h. Contribución de todos los integrantes | Cumple | `git shortlog -sne HEAD` consolidado: Nilver Garcia (`nilver-garcia`/`Nnigarp`, mismo id de cuenta 115980006 — 124 commits), Camilo Martinez (`camilixo92`, 26), Joshua Tenorio (`Carulla-sd`, 19). Los tres integrantes con contribución sustantiva, no solo simbólica. |

## Estado global del proyecto (overall)

HEAD coincide con `corte-1`: no hay commits posteriores. El proyecto llega al cierre con la base S1-S4 saneada (según `correcciones.md`, contrastado con el repo) y con el reto de S5 completo de punta a punta: restricción declarada, línea base medida con procedimiento reproducible, ADR con criterio de reversión cuantificado, cambio que degrada controladamente el sistema ante la condición adversa, prueba automatizada que reproduce exactamente esa condición, medición posterior contra el umbral, y trazabilidad sin huecos en `docs/aspectos.md`. Únicas brechas: los aspectos ASP-01/ASP-02 siguen sin materializar (declarado explícitamente por el equipo, no oculto), y no se verificó de forma independiente el estado del Quality Gate en SonarCloud (solo se confirmó que `.sonarcloud.properties` existe en el árbol).

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia |
|---|---:|---:|---|
| Diagnóstico del reto | sobresaliente | 1,00 | Línea base cuantificada con procedimiento (`scripts/medir_bloqueo_sqlite.py`), localizada en R-07/EC-05/C4/código, distinguiendo el síntoma (HTTP 500 tras 7.3s) de la causa (`SQLITE_BUSY`/`SQLITE_LOCKED`) y priorizando el riesgo de contención de escritura. |
| Alternativas y decisión | sobresaliente | 1,00 | ADR-0002 con 3 alternativas, fuerzas, decisión, consecuencias, criterio de reconsideración cuantificado (`>5% de 100 intentos`) y costo de reversión explícito ("moderado", con pasos concretos). |
| Aplicación sobre el corte vertical | sobresaliente | 1,00 | Cambio de extremo a extremo (PR #28, `ff68cf2`), arranque reproducible sin alterar, límites C4 conservados, y degradación controlada explícita ante la condición adversa (HTTP 503 en vez de fallo silencioso o bloqueo indefinido). |
| Pruebas, medición y trazabilidad | sobresaliente | 1,00 | Cadena `docs/aspectos.md` navegable sin huecos, resultado contrastado con umbral y reproducible por script, y entrada de IA de S5 con rechazo justificado técnicamente. |
| Sustentación del reto | lo fija el docente | pendiente | Requiere sesión. |
| **Subtotal técnico** | | **4,00 / 4,00** | Propuesta; no es la nota total sobre 5,00 (falta el criterio de sustentación). |

## No verificado

- PDF de dos páginas de Moodle.
- Sustentación (la fija el docente en sesión).
- Estado real del Quality Gate en SonarCloud (el repo solo confirma la configuración, `.sonarcloud.properties`).

## Hallazgos

- El equipo completó el reto de corte 1 de forma sustantiva entre el 04 y el 06 de septiembre, con una etiqueta `corte-1` que sí corresponde al trabajo del corte — el único de los cinco equipos de este lote donde esto ocurre.
- El ADR-0002 alcanza el nivel sobresaliente de la rúbrica en varios criterios (dato que revisaría la decisión, costo de reversión).
- ASP-01 y ASP-02 quedan explícitamente sin materializar en `docs/aspectos.md`, lo cual es buena práctica de trazabilidad honesta y no una fila indefendible.
- Existe `correcciones.md`; ver adjudicación abajo.

## Correcciones del equipo

| Corrección | Adjudicación | Justificación |
|---|---|---|
| S1-S4 "saneadas": estructura mínima, tabla de 8 columnas, `docs/ia.md` con rechazos, contribución de los 3 integrantes | Aceptada | Verificado directamente en el árbol de `corte-1`: las rutas, la tabla de aspectos y `docs/ia.md` existen tal como se describe, y coinciden con lo que la revisión preliminar ya reconocía como fuerte para S3/S4. |
| Reto S5 completo (R-07, EC-05, ADR-0002, línea base, medición posterior, prueba, trazabilidad ASP-06) | Aceptada | Verificado con evidencia primaria: el ADR, la prueba automatizada, el script de medición y el run de CI sobre el propio commit de la etiqueta sostienen íntegramente la afirmación. |
| ADR-0001 documentado sin reescribirlo, trazabilidad añadida solo en `docs/arc42/09-decisiones.md` | Aceptada | `git log --follow` confirma un único commit para `0001-usar-monolito-modular.md`; no hay reescritura. |
| "SonarQube Cloud oficial integrado, Quality Gate: Passed" | Aceptada con reserva | Se confirmó `.sonarcloud.properties` en el árbol y que el workflow de GitHub Actions solo ejecuta pruebas (consistente con lo declarado), pero no se consultó la API de SonarCloud para verificar el estado del Quality Gate; queda como no verificado de forma independiente. |

## Preguntas para la sustentación

- ¿Cómo decidieron el timeout de `0,5 s` para SQLite y por qué ese valor deja margen suficiente frente al umbral de 2 s bajo carga real, no solo en la prueba?
- ¿Qué pasaría con ASP-01 y ASP-02 si tuvieran que materializarse en el segundo corte — ya tienen algún borrador de diseño?
- ¿Pueden mostrar en vivo el Quality Gate de SonarCloud para el proyecto oficial `ISCOUTB_AS_202620_PROYECTO_CAMPUSMARKET`?
