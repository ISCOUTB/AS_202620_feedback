# semana-07-evidencia-s7 · TAIA

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `0a12f0c` en `origin/main` (2026-09-17T15:27:54-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | 0a12f0c docs/api/openapi.json con "openapi": "3.1.0" y bloque paths; archivo versionado en el arbol de origin/main. | Cumple | Es un contrato ejecutable, no prosa: OpenAPI 3.1 en JSON. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.json referencia $ref a TaskCreateRequest, TaskUpdateRequest, TaskResponse, UserCreateRequest, UserLoginRequest, LoginResponse, ErrorResponse y HTTPValidationError en requestBody y respuestas 200/201/401/404/409/422. | Cumple | Hay esquemas de entrada y de salida, no solo rutas. |
| Correspondencia entre el contrato y la API implementada | Rutas /academic/tasks y /users/login de docs/api/openapi.json coinciden con la tabla de rutas de README.md y con los adaptadores backend/app/modules/academic/adapters/inbound/api.py y backend/app/modules/usuario/adapters/inbound/api.py; backend/tests/test_api_contract.py compara OpenAPI con la app FastAPI. | Cumple | Correspondencia comprobada por lectura documental y por el comparador de la prueba; no se aporto cita linea a linea. |
| Version de la API declarada y con historial | docs/api/openapi.json declara info.version "1.0.0"; no se aporto la salida de git log del archivo del contrato. | No verificado | Se esperaba historial del contrato; haria falta git log --format='%h %cI %s' -- docs/api/openapi.json. |
| Prueba de contrato presente | 0a12f0c backend/tests/test_api_contract.py presente en el arbol; docs/api/README.md la describe e incluye test_incompatible_change_is_detected. | Cumple | La prueba existe y esta enlazada desde el ADR-0002. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/ci.yml, pero no se aporto su contenido, ni el grep de contract\|dredd\|schemathesis\|pact\|prism\|spectral\|openapi, ni runs_ci. | No verificado | Se esperaba la linea del workflow que invoca la prueba y la URL del run; ninguno de los dos llego. |
| Evidencia de que la prueba falla ante un cambio incompatible | Existen docs/evidencia_s7_contract_failure.txt y tools/demo_contract_break.py, pero su contenido no esta en la evidencia aportada y no hay run en rojo en runs_ci (no aportado). | No verificado | Pregunta de sustentacion: haria falta el contenido del archivo de evidencia o un run fallido de CI. |
| ADR de la estrategia de integracion ligado a un escenario | docs/adr/0002-estrategia-integracion-api-sincrona.md: contexto, escenario de calidad S1/S3/S4, opciones A/B/C con la asincrona descartada, decision, consecuencias y trazabilidad. | Cumple | Justifica sincrono frente a mensajeria y declara el costo de acoplamiento. |
| arc42 seccion 6 con los flujos de interaccion | docs/arc42/06-vista-de-ejecucion.md con recorridos 6.1 a 6.6 (registro, login, autenticacion de solicitud, vinculacion Telegram, registro y consulta de tareas). | Cumple | Cada recorrido tiene diagrama, secuencia y errores relevantes. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/C4-C2.md existe en el arbol de 0a12f0c, pero su contenido no se aporto. | No verificado | Sin el diagrama no se puede comprobar que cada flecha lleve protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible:true; repo ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant; rama origin/main; hash 0a12f0c del 2026-09-17. | Cumple | El historial trae 7 entradas de autoria; hay entradas repetidas de una misma identidad que conviene consolidar. |
| Estructura minima | 0a12f0c contiene README.md, docs/arc42/01..12 mas arc42.md, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md. | Cumple | Estructura conforme a la ruta minima, toda la documentacion en Markdown. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md y docs/adr/0002-estrategia-integracion-api-sincrona.md siguen NNNN-titulo-en-kebab-case y traen contexto, opciones, decision, consecuencias y trazabilidad. | Cumple | No se aporto git log --follow, no se pudo comprobar si algun ADR aceptado fue reescrito. |
| Tabla de aspectos | docs/aspectos.md existe en 0a12f0c, pero su contenido no se aporto. | No verificado | Haria falta el archivo para verificar las ocho columnas y que no haya celdas huecas. |
| Registro de uso de IA | docs/ia.md con 10 entradas en el log aportado, de 2026-08-07 a 2026-09-16 (crecimiento sostenido). | Cumple | Con el log no se lee el contenido: la columna de lo rechazado y su motivo no queda verificada. |
| README | README.md describe el sistema, requisitos previos, arranque con run.bat y verificacion por GET /health, y pruebas con pytest backend/tests. | Cumple | El arranque depende de instalar dependencias antes de run.bat; el extracto llega truncado. |
| Pipeline y analisis estatico | .github/workflows/ci.yml presente en 0a12f0c, pero sin contenido aportado, sin linea del scanner, sin URL de run exitoso y sin URL publica de SonarCloud. | No verificado | Faltan las tres evidencias exigidas (configuracion y linea del workflow, run, Quality Gate publico). |
| Secretos | El grep de 0a12f0c solo devuelve nombres de parametros y lecturas os.getenv (GEMINI_API_KEY, TAIA_TELEGRAM_BOT_TOKEN, secreto JWT) y una clave de prueba; envs_versionados vacio. | Cumple | Sin credenciales reales ni .env versionado; ningun hallazgo que obligue a rotar. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `0a12f0c04df6943f1f5c39ebf8ca67400d7c6ada 2026-09-17T15:27:54-05:00 docs: adding evidence week 7`
- **Veredicto**: con pendientes
- Resumen: En 0a12f0c (origin/main, 2026-09-17, anterior al cierre del 2026-09-21) el proyecto tiene contrato OpenAPI 3.1, prueba de contrato, cliente generado, ADR-0002 de integracion sincrona y arc42 con vista de ejecucion; 6 de 10 criterios de ficha y 6 de 8 filas transversales se sostienen con evidencia citada, y los pendientes son la ejecucion y el fallo de la prueba de contrato, el C4 nivel 2 y SonarCloud.

Pendientes que siguen abiertos:
- Ejecucion de la prueba de contrato en el pipeline y URL del run
- Evidencia verificable de fallo ante cambio incompatible
- C4 nivel 2 con protocolo y formato en cada flecha
- Historial git del archivo de contrato
- SonarCloud: configuracion, run exitoso y URL publica con Quality Gate
- Contenido de docs/aspectos.md para validar la tabla de trazabilidad

## Recuento y nota sugerida

6 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.4 = 1 + 4 × (6/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Version de la API con historial git: falta git log del archivo docs/api/openapi.json.
- Ejecucion de la prueba de contrato en el pipeline: falta el contenido de .github/workflows/ci.yml y la URL del run.
- Fallo de la prueba ante cambio incompatible: falta el contenido de docs/evidencia_s7_contract_failure.txt o un run en rojo.
- C4 nivel 2 con protocolo y formato en cada flecha: falta el contenido de docs/c4/C4-C2.md.
- Tabla de aspectos: falta el contenido de docs/aspectos.md para verificar las ocho columnas.
- SonarCloud: faltan configuracion y linea del scanner, run exitoso y URL publica con Quality Gate.
- Ejecucion de pruebas y arranque: sin runs_ci aportados, el comando anotado es pytest backend/tests y run.bat.

## Hallazgos para la planilla

- Contrato OpenAPI 3.1 ejecutable y con esquemas en docs/api/openapi.json.
- Prueba de contrato presente en backend/tests/test_api_contract.py, pero no se aporta la linea del workflow que la invoca.
- No hay evidencia verificable de que la prueba falle ante un cambio incompatible: solo un archivo de evidencia no legible y una prueba que muta la superficie en memoria.
- ADR-0002 justifica HTTP sincrono con OpenAPI frente a mensajeria y declara las consecuencias.
- arc42 seccion 6 cubre seis recorridos con secuencia, validaciones y errores.
- C4 nivel 2 no verificable: falta el contenido de docs/c4/C4-C2.md.
- Sin runs_ci en la evidencia: no se pudo comprobar ninguna ejecucion de pipeline ni el arranque.
- Sin secretos reales; las coincidencias del grep son nombres y lecturas de entorno.
