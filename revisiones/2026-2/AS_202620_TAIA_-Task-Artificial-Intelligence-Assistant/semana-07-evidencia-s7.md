# semana-07-evidencia-s7 · TAIA

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `5a4e8dc` en `origin/main` (2026-09-15T20:48:07-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.json (openapi 3.1.0) en el árbol del hash 5a4e8dc. | Cumple | Archivo JSON ejecutable dentro de docs/api/, versionado en git y no prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | openapi.json define paths /academic/tasks, /academic/tasks/{task_id}, /users, /users/login con $ref a components/schemas (TaskResponse, TaskCreateRequest, ErrorResponse). | Cumple | Los esquemas de respuesta y petición están referenciados; hay content application/json con schema por respuesta. |
| Correspondencia entre el contrato y la API implementada | Rutas /academic/tasks y /users/login del contrato coinciden con backend/app/modules/academic/adapters/inbound/api.py, usuario/adapters/inbound/api.py y reminders/adapters/inbound/http_controller.py; operationIds generados por FastAPI (complete_task_academic_tasks__task_id__complete_patch) y tabla de rutas del README. | Cumple | No se volcó el contenido de los api.py; la correspondencia se apoya en operationIds autogenerados, la tabla del README y backend/tests/test_api_contract.py. |
| Versión de la API declarada y con historial | info.version = 1.0.0 en docs/api/openapi.json; no se aportó git log del archivo. | No verificado | Se esperaba el historial del contrato (git log -- docs/api/openapi.json) para ver su evolución; solo consta la versión declarada. |
| Prueba de contrato presente | backend/tests/test_api_contract.py en el árbol de 5a4e8dc; docs/api/README.md describe test_incompatible_change_is_detected. | Cumple | También existen tools/demo_contract_break.py y backend/generated/taia_api_client.py como soporte del comparador. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml existe en el árbol, pero no se aportó su contenido ni runs_ci. | No verificado | Haría falta la línea del workflow que invoca pytest sobre test_api_contract.py y la URL del run; un archivo de workflow sin ejecución no basta. |
| Evidencia de que la prueba falla ante un cambio incompatible | Existe docs/evidencia_s7_contract_failure.txt y docs/api/README.md describe que el comparador lanza AssertionError, pero no se aportó el contenido del archivo ni un run en rojo. | No verificado | Se esperaba el contenido de la evidencia o la URL de una ejecución fallida; queda como pregunta de sustentación para el nivel sobresaliente. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0002-estrategia-integracion-api-sincrona.md cita S1, S3 y S4, opciones A/B/C, alternativa descartada (mensajería/eventos y HTTP sin contrato) y consecuencias de acoplamiento. | Cumple | Incluye trazabilidad a contrato, prueba, cliente generado, CI, C4-C2 y arc42 sección 6. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06-vista-de-ejecucion.md con recorridos de Usuario (registro, login, autenticación, Telegram) y Academic (registro y consulta) con secuencia y errores. | Cumple | Los flujos están descritos paso a paso con diagramas de ejecución y códigos HTTP de error. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/C4-C2.md existe en el árbol, pero no se aportó su contenido. | No verificado | Se esperaba el diagrama de contenedores con cada flecha etiquetada con protocolo y formato; los diagramas de arc42 secciones 3 y 7 no sustituyen al C4 nivel 2. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant en ISCOUTB, visible=true, rama origin/main; autores del log con 5 identidades visibles. | Cumple | luis20072002 y 'Luis Mendoza' comparten correo, por lo que cuentan como una sola identidad; no se atribuyen cuentas a personas por parecido de nombre. |
| Estructura mínima | Coexisten docs/arc42/ (12 secciones), docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md en 5a4e8dc. | Cumple | No hay desviación de rutas ni artefactos en formato no revisable. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md y docs/adr/0002-estrategia-integracion-api-sincrona.md siguen NNNN-kebab-case con contexto, opciones, decisión, consecuencias y trazabilidad. | Cumple | No se aportó git log --follow; no se puede confirmar que un ADR aceptado no haya sido reescrito. |
| La tabla de aspectos | docs/aspectos.md existe en el árbol, pero no se aportó su contenido. | No verificado | Haría falta comprobar las ocho columnas (ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia) y que cada celda sea navegable. |
| Registro de uso de IA | docs/ia.md con 9 commits entre 2026-08-07 y 2026-09-12, pero sin contenido aportado. | No verificado | Se verificó que crece; falta el contenido para comprobar la columna de lo rechazado y su motivo técnico. |
| README | README.md describe el sistema, requisitos previos (Python 3.14), arranque con .\run.bat y pruebas con pytest backend/tests. | Cumple | Un solo comando de arranque documentado; arc42 §2 advierte que el README está en UTF-16 LE, lo que puede afectar a herramientas que lo procesen. |
| Pipeline y análisis estático | .github/workflows/ci.yml presente en el árbol; no hay sonar-project.properties, ni runs_ci, ni URL pública de SonarCloud en la evidencia. | No verificado | Faltan las tres piezas exigidas desde S6: línea del workflow que invoca el scanner, URL del run exitoso y URL del análisis con Quality Gate. |
| Secretos | git grep del hash 5a4e8dc solo devuelve nombres de variables y lecturas de entorno (gemini_llm.py:95 GEMINI_API_KEY, telegram_bot_client.py:12 TAIA_TELEGRAM_BOT_TOKEN); envs_versionados vacío. | Cumple | No hay credenciales embebidas ni .env versionado; los coincidentes son falsos positivos del patrón. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `5a4e8dca1d9d8a913e3984c34e5693224bebedeb 2026-09-15T20:48:07-05:00 Merge pull request #13 from ISCOUTB/val`
- **Veredicto**: con pendientes
- Resumen: En HEAD de origin/main (5a4e8dc, 2026-09-15) el entregable S7 existe: contrato OpenAPI 3.1 con versión 1.0.0, prueba de contrato, cliente generado, ADR-0002 y secciones arc42 6 y 7. Sin embargo la evidencia no aporta el contenido del workflow, ni runs_ci, ni la URL de SonarCloud, ni el contenido de docs/c4/C4-C2.md, docs/aspectos.md, docs/ia.md y de la propia evidencia del cambio incompatible, por lo que varias filas quedan sin verificar.

Pendientes que siguen abiertos:
- Confirmar que ci.yml ejecuta backend/tests/test_api_contract.py y aportar la URL del run
- Aportar la evidencia del cambio incompatible que hace fallar la prueba (contenido o run en rojo)
- Publicar URL de SonarCloud con Quality Gate, línea del scanner y run exitoso
- Completar contenido verificable de docs/c4/C4-C2.md, docs/aspectos.md y docs/ia.md
- Registrar el historial git del contrato para sostener su versionado

## Recuento y nota sugerida

6 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.4 = 1 + 4 × (6/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- git log -- docs/api/openapi.json (historial del contrato)
- Contenido de .github/workflows/ci.yml y la línea que invoca la prueba de contrato
- runs_ci: nombre, conclusión y URL del run de la rama o hash revisados
- Contenido de docs/evidencia_s7_contract_failure.txt o URL del run en rojo
- Contenido de docs/c4/C4-C2.md (protocolo y formato en cada flecha)
- Contenido de docs/aspectos.md (ocho columnas navegables)
- Contenido de docs/ia.md (columna de lo rechazado)
- URL pública del análisis en SonarCloud con estado del Quality Gate

## Hallazgos para la planilla

- Contrato OpenAPI 3.1 versionado en docs/api/openapi.json con versión 1.0.0 y esquemas referenciados.
- Prueba de contrato presente en backend/tests/test_api_contract.py, pero su invocación desde ci.yml no se pudo verificar.
- Existe docs/evidencia_s7_contract_failure.txt, sin contenido aportado y sin run en rojo que lo respalde.
- La evidencia no incluye runs_ci: no hay nombre, conclusión ni URL de ninguna ejecución.
- docs/c4/C4-C2.md y docs/aspectos.md existen, pero su contenido no fue aportado.
- docs/ia.md crece, aunque no se cita la columna de lo rechazado.
- Cinco identidades visibles en git; dos cuentas comparten correo y se consolidan en una sola.
- Sin credenciales reales en el repositorio; los coincidentes son variables y lecturas de entorno.
- Sin commits posteriores al cierre y sin commits nuevos desde la entrega anterior.
