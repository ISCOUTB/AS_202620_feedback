# semana-07-evidencia-s7 · TAIA

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `3c2ae72` en `origin/main` (2026-09-16T21:40:14-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.json en 3c2ae72 (2026-09-16T21:40:14-05:00), con "openapi": "3.1.0". | Cumple | Archivo JSON de especificación versionado en docs/api/, no prosa; se cumple formato ejecutable. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.json: paths /academic/tasks, /academic/tasks/{task_id}, /users con responses que referencian components/schemas (TaskResponse, TaskCreateRequest, TaskUpdateRequest, ErrorResponse, UserResponse, LoginResponse). | Cumple | Hay esquemas de datos referenciados ($ref), no solo una lista de rutas. |
| Correspondencia entre el contrato y la API implementada | Se revisó el árbol de 3c2ae72: existen backend/app/modules/academic/adapters/inbound/api.py, backend/app/modules/usuario/adapters/inbound/api.py y backend/tests/test_api_contract.py, pero no se aportó su contenido. | No verificado | Se esperaba localizar dos rutas del contrato en el código y una ruta del código en el contrato; sin el contenido no puede cotejarse. |
| Versión de la API declarada y con historial | docs/api/openapi.json declara "version": "1.0.0" y docs/api/README.md la repite; no se aportó la salida de git log del archivo de contrato. | No verificado | La versión está declarada; falta el historial (git log -- docs/api/openapi.json) para confirmar el versionado en git. |
| Prueba de contrato presente | backend/tests/test_api_contract.py en 3c2ae72; docs/api/README.md indica que contiene test_incompatible_change_is_detected. | Cumple | La prueba existe en el árbol del commit calificado; su contenido no se aportó. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml existe en 3c2ae72 pero no se aportó su contenido ni la URL de ningún run (runs_ci vacío). | No verificado | Se esperaba la línea del workflow que invoca la prueba; comando: grep -rniE 'contract\|schemathesis\|pact\|prism\|openapi' .github/workflows/. |
| Evidencia de que la prueba falla ante un cambio incompatible | docs/evidencia_s7_contract_failure.txt y tools/demo_contract_break.py en 3c2ae72; docs/api/README.md describe la comprobación test_incompatible_change_is_detected que espera AssertionError. | Cumple | Es evidencia aportada por el equipo (no hay run en rojo público); la incompatibilidad se prueba con aserción en memoria, sin dejar el pipeline en rojo. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0002-estrategia-integracion-api-sincrona.md: secciones Escenario de calidad (S1, S3, S4), Opciones A/B/C, Decisión (HTTP síncrono + JSON + OpenAPI 3.1), Consecuencias y Trazabilidad a contrato, prueba y CI. | Cumple | Incluye alternativa descartada (mensajería/eventos y HTTP sin contrato) y su efecto de acoplamiento. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06-vista-de-ejecucion.md con 6.1–6.6: registro, login, autenticación, vinculación Telegram, registro y consulta de tareas, con secuencia y errores por flujo. | Cumple | Los flujos describen pasos, actores y respuestas HTTP. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/C4-C2.md existe en el árbol de 3c2ae72, pero no se aportó su contenido. | No verificado | Se esperaba ver cada flecha del nivel 2 etiquetada con protocolo (HTTP, webhook) y formato (JSON). |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant en la organización ISCOUTB, visibilidad pública, con historial de autores. | Cumple | 7 identidades de git para 4 integrantes declarados; hay variantes del mismo nombre visible (dos entradas con igual nombre y distinto dominio, y dos variantes de un mismo nombre), que se consolidan sin atribuir cuentas a personas por parecido. |
| Estructura mínima | En 3c2ae72: README.md, docs/arc42/ (01–12 más índice), docs/adr/0001-estilo-arquitectonico.md y docs/adr/0002-estrategia-integracion-api-sincrona.md, docs/c4/C4-C1.md, C4-C2.md, C4-C3.md, docs/aspectos.md, docs/ia.md. | Cumple | Ninguna ruta se desvía de la estructura mínima del contrato. |
| Estado del repositorio que se califica | Rama principal origin/main, hash 3c2ae72 con fecha 2026-09-16T21:40:14-05:00, anterior al cierre 2026-09-21T05:00:00Z; commits_tardios_post_cierre vacío. | Cumple | No hay commits posteriores al cierre en la rama principal. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md y docs/adr/0002-estrategia-integracion-api-sincrona.md: nombres NNNN-kebab-case y contenido con contexto, opciones evaluadas, decisión, consecuencias y trazabilidad. | Cumple | No se aportó el listado de nombres inválidos ni git log --follow para detectar reescrituras de ADR aceptados. |
| La tabla de aspectos | docs/aspectos.md existe en 3c2ae72, pero no se aportó su contenido. | No verificado | Se esperaba una fila por aspecto con las ocho columnas ID · Aspecto · Requisito · C4 · ADR · Código · Pruebas · Evidencia, con cada eslabón navegable. |
| Registro de uso de IA | docs/ia.md con 10 entradas de historial entre 2026-08-07 (76d4a91) y 2026-09-16 (7b32b3f), en crecimiento a lo largo del semestre. | Cumple | El historial muestra crecimiento sostenido; no se aportó el contenido, por lo que no se pudo comprobar la columna de lo rechazado y su motivo. |
| README | README.md describe el sistema, requisitos previos (Python 3.14 y pip install -r backend/requirements.txt), arranque con un comando (.\run.bat en 127.0.0.1:8000) y pruebas (pytest backend/tests). | Cumple | Declara el health check /health y la documentación interactiva en /docs. |
| Pipeline y análisis estático | .github/workflows/ci.yml existe en 3c2ae72, pero no se aportó su contenido ni URLs de runs, y no hay archivo de configuración de Sonar en el árbol. | No verificado | Se esperaban la línea del workflow que invoca el scanner, la URL del run exitoso y la URL pública del análisis con Quality Gate; comando: curl API de actions/runs y ls .github/workflows/. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `3c2ae726cec42371a88dbf28ff9a2f7bade43b46 2026-09-16T21:40:14-05:00 Merge pull request #15 from ISCOUTB/val`
- **Veredicto**: al dia
- Resumen: En la punta actual de origin/main (3c2ae72, 2026-09-16) el proyecto presenta los artefactos centrales de la semana 7: contrato OpenAPI 3.1 versionado en docs/api/, ADR de integración síncrona con alternativas descartadas, prueba de contrato en backend/tests/ y sección 6 de arc42 con flujos; quedan sin verificar la ejecución en CI, SonarCloud, la correspondencia fina contrato↔código y el contenido de aspectos y C4 nivel 2.

Pendientes que siguen abiertos:
- Comprobar que el pipeline ejecuta la prueba de contrato (contenido de ci.yml y URL del run).
- Aportar análisis SonarCloud público con Quality Gate para el hash revisado.
- Cotejar rutas del contrato con el código implementado.
- Publicar el contenido de docs/aspectos.md y docs/c4/C4-C2.md.
- Aportar el historial de git del archivo de contrato.

## Recuento y nota sugerida

6 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.4 = 1 + 4 × (6/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correspondencia contrato↔código: falta el contenido de los adaptadores inbound y de backend/tests/test_api_contract.py; se requería situar dos rutas del contrato en el código y una ruta del código en el contrato.
- Historial del contrato: falta 'git -C "$DIR" log --format='%h %cI %s' -- docs/api/openapi.json'.
- Ejecución de la prueba de contrato en CI: falta el contenido de .github/workflows/ci.yml y la URL del run; comando: grep -rniE 'contract|schemathesis|pact|openapi' .github/workflows/.
- Run en rojo ante cambio incompatible: no se aportó ejecución fallida, solo evidencia documental y script de demostración.
- SonarCloud: sin sonar-project.properties, sin línea del scanner y sin URL pública del análisis; comando: curl -s "https://api.github.com/repos/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs?per_page=5".
- Contenido de docs/aspectos.md (ocho columnas por aspecto) y de docs/c4/C4-C2.md (protocolo y formato en cada flecha).

## Hallazgos para la planilla

- El contrato es OpenAPI 3.1 con version 1.0.0 y operationId de estilo FastAPI, coherente con un contrato exportado de la aplicación.
- Los responses referencian components/schemas (TaskResponse, TaskCreateRequest, ErrorResponse y otros), por lo que hay esquemas de datos y no solo endpoints.
- No se aportó ningún run de CI: no puede comprobarse que el pipeline ejecute la prueba de contrato ni que bloquee la integración.
- No hay rastro auditable de SonarCloud: ni archivo de configuración del análisis, ni URL pública con Quality Gate.
- La evidencia de incompatibilidad se apoya en archivos del repositorio y un script de demo, sin ejecución en rojo del pipeline.
- El escaneo de secretos solo marca nombres de variables y campos (api_key, token, password): no apareció credencial real ni .env versionado.
- docs/aspectos.md y docs/c4/C4-C2.md existen en el commit calificado, pero su contenido no fue aportado para revisión.
- Sin commits posteriores al cierre en origin/main y sin commits nuevos respecto del cierre anterior.
