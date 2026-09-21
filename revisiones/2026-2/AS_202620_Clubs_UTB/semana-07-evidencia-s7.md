# semana-07-evidencia-s7 · Clubs UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `dc211b8` en `origin/master` (2026-09-20T23:56:51-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.yaml:1 declara `openapi: 3.1.0` y el archivo está en el árbol del commit dc211b8. | Cumple | Es especificación ejecutable, no prosa; único contrato del repo (no hay AsyncAPI ni proto). |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.yaml define 9 rutas (/health, /clubes, /clubes/{club_id}, /clubes/{club_id}/miembros, /clubes/{club_id}/eventos, /eventos/{evento_id}, /eventos/{evento_id}/asistencia, /clubes/{club_id}/publicaciones, /publicaciones/{publicacion_id}) con responses y requestBody que referencian #/components/schemas/{Club,Evento,Membresia,Publicacion,ErrorResponse}. | Cumple | El volcado del archivo se corta antes de components/schemas, por lo que solo se citan las referencias a esquemas, no sus definiciones. |
| Correspondencia entre el contrato y la API implementada | Se esperaba cotejar backend/src/linkclub/adapters/inbound/api/health_router.py y publicacion_router.py contra docs/api/openapi.yaml; el árbol los lista pero su contenido no se volcó. | No verificado | Señal de posible desincronización: docs/api/contrato_api.md declara implementado POST /publicaciones y GET /publicaciones/{club_id}, mientras el contrato define POST /clubes/{club_id}/publicaciones y GET /publicaciones/{publicacion_id}. |
| Versión de la API declarada y con historial | docs/api/openapi.yaml declara info.version 1.0.0, docs/api/CHANGELOG.md registra '## 1.0.0 - 2026-09-20' y la ruta del contrato aparece en los commits 659b9bf y e0eaca4 (2026-09-20). | Cumple | No se aportó `git log` específico del archivo; la corrección del contrato del mismo día no subió la versión. |
| Prueba de contrato presente | backend/tests/test_contrato_openapi.py existe en el árbol de dc211b8 y el ADR 0003 lo describe verificando esquemas de respuesta y rutas del código. | Cumple | Solo se cita la ruta de la prueba; no se volcó su contenido. |
| El pipeline ejecuta la prueba de contrato | Se esperaba la línea de .github/workflows/contrato.yml que invoca la prueba y la URL del run; el workflow existe en el árbol y el ADR 0003 nombra los jobs lint-contrato, prueba-contrato y cambios-incompatibles, pero no hay YAML ni runs en la evidencia. | No verificado | Sin `runs_ci` no se puede confirmar ejecución; haría falta el contenido del workflow y la URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | Se esperaba un run en rojo del job cambios-incompatibles (oasdiff) o la evidencia aportada por el equipo; no hay runs en la evidencia ni artefacto entregado. | No verificado | Queda como pregunta de sustentación: es el criterio que separa competente de sobresaliente en este corte. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0003- integacion rest openapi.md (idéntico a docs/adr/0003-API.md) decide REST síncrono con contrato OpenAPI, descarta todo asíncrono, polling y GraphQL, y traza a U3 y C1 de docs/arc42/10_requisitos_de_calidad.md. | Cumple | Hay dos archivos con el número 0003 y el enlace citado en docs/arc42/09_decisiones_de_diseno.md (0003-integracion-rest-openapi.md) no existe en el árbol. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06_vista_de_ejecucion.md contiene diagrama de secuencia de GET /health (cliente → health_router → CheckHealthUseCase → StatusPort → InMemoryStatusAdapter) y descripción paso a paso. | Cumple | Solo documenta el flujo de health; el flujo de publicaciones, que sí tiene código, no aparece. |
| C4 nivel 2 con protocolo y formato en cada flecha | Se esperaba el diagrama de contenedores con cada flecha etiquetada con protocolo y formato; solo existe docs/c4/contexto.md y su contenido no fue volcado (el README afirma que reúne nivel 1 y 2). | No verificado | Haría falta el contenido del archivo o el diagrama de nivel 2 para comprobar el etiquetado. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_Clubs_UTB, visible: true, con historial de 6 cuentas de autor que se consolidan en al menos 4 identidades (dos cuentas comparten el mismo correo y corresponden al mismo autor). | Cumple | El README asocia los handles a los 4 integrantes; la cuenta 'Zavod Dev' no se atribuye a una persona por parecido de nombre. |
| Estructura mínima | El árbol de dc211b8 incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Faltan las secciones 07 y 11 de arc42; los ADR incumplen la convención de nombre (se registra en su fila). |
| Convenciones de ADR | docs/adr/ contiene '0003- integacion rest openapi.md' (espacio y sin kebab-case) y '0003-API.md' (número duplicado y título que no enuncia la decisión), y docs/arc42/09_decisiones_de_diseno.md enlaza ../adr/0003-integracion-rest-openapi.md, ruta inexistente. | No cumple | 0001-hexagonal.md y 0002-ajuste-contextos-publicaciones.md sí cumplen número, nombre y trazabilidad. |
| Tabla de aspectos | docs/aspectos.md existe y el ADR 0001 cita sus filas U2, C1 y C3, pero su contenido no fue volcado. | No verificado | No se pueden comprobar las 8 columnas (ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia) ni que cada celda sea navegable; el README la describe nombrando 'Escenario' en lugar de 'Evidencia'. |
| Registro de uso de IA | docs/ia.md existe y acumula 9 commits entre 2026-08-09 y 2026-09-15 (últimos d2d1450 y 1d99370), pero su contenido no fue volcado. | No verificado | No se puede comprobar la columna de qué se rechazó y por qué, que es la que se revisa primero. |
| README | README.md describe el sistema y el problema (secciones 1-2), stack, estructura, equipo y 'Cómo arrancar' con requisitos previos (Python 3.10+), venv, `uvicorn linkclub.main:app --app-dir src` y `PYTHONPATH=src pytest tests/ -v`. | Cumple | El arranque son cuatro comandos documentados, no un único comando, como pide el contrato. |
| Pipeline y análisis estático | En el árbol de dc211b8 solo hay .github/workflows/backend-tests.yml y .github/workflows/contrato.yml; no existe sonar-project.properties ni configuración equivalente y la evidencia no aporta run ni URL pública de SonarCloud con Quality Gate. | No cumple | Faltan las tres piezas exigidas (config + línea del scanner, run exitoso del hash, URL del análisis); tampoco se puede verificar que el pipeline bloquee la integración. |
| Secretos | El escaneo de secretos sobre HEAD no arrojó coincidencias y envs_versionados está vacío (ningún .env versionado). | Cumple | Sin hallazgos de credenciales en el commit revisado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `dc211b8f38c4f8d0ba0ebd13021e3181b6d573bb 2026-09-20T23:56:51-05:00 Merge pull request #2 from ISCOUTB/contrato-openapi`
- **Veredicto**: con pendientes
- Resumen: El proyecto en la punta de origin/master (dc211b8, 2026-09-20T23:56:51-05:00, anterior al cierre) entrega el contrato OpenAPI 3.1 versionado, ADR de integración con alternativas descartadas, pipeline de contrato declarado y arc42 §6; sin embargo faltan el análisis estático público con Quality Gate y la evidencia de que la prueba de contrato falla ante un cambio incompatible, y persisten pendientes de semanas anteriores (tabla de módulos desalineada, NC-01 y NC-02, ADR duplicado y con nombre fuera de convención, enlaces rotos).

Pendientes que siguen abiertos:
- Actualizar docs/arc42/tabla_modulo.md a los tres contextos vigentes (abierto en ADR 0002 y arc42 §8.3).
- Cerrar NC-01 y NC-02 de docs/arc42/lista_errores.md.
- Eliminar el ADR duplicado y renombrar 0003 según NNNN-kebab-case, corrigiendo el enlace roto.
- Aportar análisis SonarCloud público con Quality Gate y configuración en el repositorio.
- Aportar el run del workflow de contrato y la evidencia de fallo por cambio incompatible.
- Completar las secciones 07 y 11 de arc42 y verificar correspondencia contrato↔código y C4 nivel 2.

## Recuento y nota sugerida

6 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.4 = 1 + 4 × (6/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correspondencia contrato↔código: falta el contenido de health_router.py y publicacion_router.py para cotejar rutas en ambos sentidos.
- Ejecución de la prueba de contrato en el pipeline: falta el YAML de .github/workflows/contrato.yml y la URL del run.
- Fallo de la prueba ante cambio incompatible: sin run en rojo ni evidencia aportada; queda como pregunta de sustentación.
- C4 nivel 2 con protocolo y formato por flecha: falta el contenido de docs/c4/contexto.md.
- Tabla de aspectos con las 8 columnas navegables: falta el contenido de docs/aspectos.md.
- Registro de uso de IA con lo rechazado y su motivo: falta el contenido de docs/ia.md.

## Hallazgos para la planilla

- El contrato OpenAPI 3.1 (docs/api/openapi.yaml) está versionado, con 9 rutas, esquemas referenciados y CHANGELOG en SemVer.
- No hay evidencia de ejecución del workflow de contrato ni de un run en rojo provocado por un cambio incompatible.
- Existen dos ADR con el número 0003, uno con espacio en el nombre, y el enlace a 0003-integracion-rest-openapi.md está roto desde arc42 §9 y el contrato.
- No hay rastro de SonarCloud: sin archivo de configuración ni URL pública de análisis con Quality Gate.
- docs/arc42/tabla_modulo.md sigue desalineado con los tres contextos vigentes, pendiente declarado en el ADR 0002 y en arc42 §8.3.
- NC-01 (datos de clubes hardcodeados) y NC-02 (sin manejo de errores de conexión) siguen 'pendiente' en docs/arc42/lista_errores.md.
- arc42 no incluye las secciones 07 y 11.
- HEAD dc211b8 (2026-09-20T23:56:51-05:00) es anterior al cierre y no hay commits posteriores en la rama principal.
