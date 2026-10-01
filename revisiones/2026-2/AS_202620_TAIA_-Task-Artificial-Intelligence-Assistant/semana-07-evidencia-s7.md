# semana-07-evidencia-s7 · TAIA

> Revisión auditada localmente; el hash publicado 0a12f0c coincide con la revisión elegible (último commit ≤ 2026-09-21T05:00:00Z en origin/main) y se leyeron en el repositorio las filas que la pasada automática había dejado como No verificado.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `0a12f0c` en `origin/main` (2026-09-17T15:27:54-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | 0a12f0c docs/api/openapi.json con "openapi": "3.1.0" y bloque paths; archivo versionado en el arbol de origin/main. | Cumple | Es un contrato ejecutable, no prosa: OpenAPI 3.1 en JSON. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.json referencia $ref a TaskCreateRequest, TaskUpdateRequest, TaskResponse, UserCreateRequest, UserLoginRequest, LoginResponse, ErrorResponse y HTTPValidationError en requestBody y respuestas 200/201/401/404/409/422. | Cumple | Hay esquemas de entrada y de salida, no solo rutas. |
| Correspondencia entre el contrato y la API implementada | docs/api/openapi.json:9 `"/academic/tasks"` y :264 `"/users/login"` frente al código: backend/app/modules/academic/adapters/inbound/api.py:21 `router = APIRouter(prefix="/academic/tasks", ...)` con `@router.get("")` (:90) y `@router.post("")` (:65); backend/app/modules/usuario/adapters/inbound/api.py:39 `router = APIRouter(prefix="/users", ...)` con `@router.post("/login")` (:118-119) y `def login_user` (:126). En el sentido inverso, la ruta del código /users/me (usuario api.py:150-151 `@router.get("/me")`, `def get_current_user` :154) está en el contrato en docs/api/openapi.json:325. backend/tests/test_api_contract.py:25 compara `contract["paths"] == implementation["paths"]` y :26-27 `components`/`info`. | Cumple | Dos rutas del contrato se localizan en los routers y una ruta del código aparece en el contrato; la prueba de contrato ancla la comparación. |
| Version de la API declarada y con historial | docs/api/openapi.json:6 declara `"version": "1.0.0"`; `git log 0a12f0c --format='%h %cI %s' -- docs/api/openapi.json` muestra 2837b47 2026-09-15T20:43:43-05:00 "feat(api): add OpenAPI contract and contract tests". | Cumple | La versión está declarada y el archivo del contrato tiene historial en git. |
| Prueba de contrato presente | 0a12f0c backend/tests/test_api_contract.py presente en el arbol; docs/api/README.md la describe e incluye test_incompatible_change_is_detected. | Cumple | La prueba existe y esta enlazada desde el ADR-0002. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml:28-29 ejecuta la prueba: `run: python -m pytest backend/tests/test_api_contract.py -q`; además :25 corre `python -m pytest backend/tests` y :32-35 regeneran el cliente y verifican su sincronía con `git diff --exit-code`. Run de CI en verde corroborado sin autenticar: workflow CI sobre 4b07242 (success). | Cumple | El pipeline invoca explícitamente la prueba de contrato, no solo existe el archivo. |
| Evidencia de que la prueba falla ante un cambio incompatible | tools/demo_contract_break.py:17-22 elimina `/health` de `app.openapi()` y llama a `_assert_contract_matches` (backend/tests/test_api_contract.py:22-27, que compara `contract["paths"] == implementation["paths"]`); docs/evidencia_s7_contract_failure.txt registra el AssertionError y el código de salida 1. La prueba automatizada test_incompatible_change_is_detected (backend/tests/test_api_contract.py:43-50) hace la misma comprobación en memoria y el pipeline la ejecuta. | Cumple | La ruptura es determinista y verificable por lectura del comparador; el demo manual no corre en CI, pero la prueba equivalente sí. Nota: los números de línea del traceback del archivo de evidencia no coinciden exactamente con el hash calificado, de modo que el soporte más fuerte es la prueba automatizada que el pipeline ejecuta. |
| ADR de la estrategia de integracion ligado a un escenario | docs/adr/0002-estrategia-integracion-api-sincrona.md: contexto, escenario de calidad S1/S3/S4, opciones A/B/C con la asincrona descartada, decision, consecuencias y trazabilidad. | Cumple | Justifica sincrono frente a mensajeria y declara el costo de acoplamiento. |
| arc42 seccion 6 con los flujos de interaccion | docs/arc42/06-vista-de-ejecucion.md con recorridos 6.1 a 6.6 (registro, login, autenticacion de solicitud, vinculacion Telegram, registro y consulta de tareas). | Cumple | Cada recorrido tiene diagrama, secuencia y errores relevantes. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/C4-C2.md:24-29 etiqueta las seis flechas: BiRel(estudiante, telegram, "Telegram Bot API / JSON"), Rel(estudiante, appmovil, "HTTPS / JSON"), BiRel(telegram, api, "HTTPS / JSON"), BiRel(api, gemini, "HTTPS / JSON"), Rel(appmovil, api, "HTTPS / JSON") y Rel(api, db, "SQL/TCP 5432"). | Cumple | Cada flecha del nivel 2 lleva protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible:true; repo ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant; rama origin/main; hash 0a12f0c del 2026-09-17. | Cumple | El historial trae 7 entradas de autoria; hay entradas repetidas de una misma identidad que conviene consolidar. |
| Estructura minima | 0a12f0c contiene README.md, docs/arc42/01..12 mas arc42.md, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md. | Cumple | Estructura conforme a la ruta minima, toda la documentacion en Markdown. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md y docs/adr/0002-estrategia-integracion-api-sincrona.md presentes en el árbol de 0a12f0c y conformes a `NNNN-titulo-en-kebab-case.md`; el filtro de §4 sobre los nombres del directorio no deja residuos. | Cumple | Los dos nombres siguen la convención; ADR-0002 (:3 `## Estado`, «Aceptado») trae contexto, opciones, decisión, consecuencias y trazabilidad. |
| Tabla de aspectos | docs/aspectos.md:3 encabeza con las ocho columnas del curso (ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia); las filas A-01…A-06 (:5-10) tienen sus celdas con enlaces navegables y la fila A-07 (:12) cubre el contrato S7 con las mismas ocho columnas. | Cumple | Las ocho columnas están presentes y no hay celdas huecas. La fila A-07 queda separada por una línea en blanco de las anteriores, de modo que se renderiza como una tabla aparte; conviene unirla a la tabla principal. |
| Registro de uso de IA | docs/ia.md leído en 0a12f0c (433 líneas, 10 entradas de 2026-08-06 a 2026-09-15): cada entrada trae «Aceptado» y «Rechazado o modificado»; p. ej. :34 «Se descartó construir una aplicación exclusivamente de finanzas», :378 «Se descartó introducir un paquete compartido para el modelo `ErrorResponse`, para no alterar los límites entre módulos documentados en arc42» y :379 «Se descartó corregir únicamente los 3 problemas visibles en SonarQube». | Cumple | El registro documenta lo rechazado con su motivo técnico, no solo los usos aceptados. |
| README | README.md leído completo en 0a12f0c (251 líneas): requisitos (:171), instalación de dependencias (:178), arranque `.\run.bat` (:188), verificación GET /health (:197, :201) y pruebas pytest backend/tests (:217) y python -m pytest backend/tests/test_api_contract.py -q (:246). | Cumple | Describe el sistema, los requisitos previos y el arranque; instalar dependencias antes de run.bat es un paso previo declarado, no ausencia de reproducibilidad. |
| Pipeline y analisis estatico | .github/workflows/ci.yml es el único workflow del árbol en 0a12f0c y no contiene ningún paso de scanner (SonarCloud, SonarQube, CodeQL u otro); `git ls-tree` no devuelve sonar-project.properties ni archivo de configuración de análisis estático. | No cumple | El pipeline ejecuta pruebas y valida el cliente generado, pero no invoca análisis estático. Los runs de CI citados por la API sin autenticar terminan en success sin scanner. |
| Secretos | El grep de 0a12f0c solo devuelve nombres de parametros y lecturas os.getenv (GEMINI_API_KEY, TAIA_TELEGRAM_BOT_TOKEN, secreto JWT) y una clave de prueba; envs_versionados vacio. | Cumple | Sin credenciales reales ni .env versionado; ningun hallazgo que obligue a rotar. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `0a12f0c04df6943f1f5c39ebf8ca67400d7c6ada 2026-09-17T15:27:54-05:00 docs: adding evidence week 7`
- **Veredicto**: con pendientes
- Resumen: En 0a12f0c (origin/main, 2026-09-17, anterior al cierre del 2026-09-21) el proyecto tiene contrato OpenAPI 3.1, prueba de contrato, cliente generado, ADR-0002 de integracion sincrona y arc42 con vista de ejecucion; 10 de 10 criterios de ficha y 7 de 8 filas transversales se sostienen con evidencia citada. El unico pendiente transversal es el analisis estatico: el pipeline no invoca ningun scanner y no hay URL publica con Quality Gate.

Pendientes que siguen abiertos:
- SonarCloud y analisis estatico: el unico workflow ejecuta pruebas y valida el cliente generado, pero no invoca scanner ni existe configuracion de analisis; queda como No cumple transversal.
- Sustentacion: explicar el demo manual de ruptura de contrato y confirmar la correspondencia del archivo de evidencia con el hash calificado (los numeros de linea del traceback no coinciden exactamente).

## Recuento y nota sugerida

10 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 5.0 = 1 + 4 × (10/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

No quedan filas de la ficha en No verificado: las diez se sostienen con evidencia citada en 0a12f0c.

- SonarCloud (transversal): el workflow no invoca scanner ni existe configuracion de analisis estatico; no hay URL publica con Quality Gate que abrir.
- Sustentacion: conviene que el equipo explique el demo manual de ruptura y la correspondencia entre docs/evidencia_s7_contract_failure.txt y el estado calificado.

## Hallazgos para la planilla

- Contrato OpenAPI 3.1 ejecutable y con esquemas en docs/api/openapi.json.
- La prueba de contrato backend/tests/test_api_contract.py se ejecuta en el pipeline (ci.yml:28-29) y el comparador se apoya en test_incompatible_change_is_detected.
- docs/evidencia_s7_contract_failure.txt registra el AssertionError y el codigo de salida 1; el demo manual no corre en CI, pero la prueba equivalente si.
- ADR-0002 justifica HTTP sincrono con OpenAPI frente a mensajeria y declara las consecuencias.
- arc42 seccion 6 cubre seis recorridos con secuencia, validaciones y errores.
- C4 nivel 2 etiqueta las seis flechas con protocolo y formato.
- Pipeline sin analisis estatico: el unico workflow ejecuta pruebas y valida el cliente generado, pero no invoca SonarCloud ni otro scanner.
- Sin secretos reales; las coincidencias del grep son nombres y lecturas de entorno.
- Inmutabilidad de ADR: el ADR-0001 aceptado fue editado en `42c5b03` (2026-09-06, «add traceability section to architectural decision record for Adr-01»), que le añadió una sección «Trazabilidad» sin crear un ADR nuevo ni marcar reemplazo; incumple §4 y ya estaba registrado en la planilla de S5.
