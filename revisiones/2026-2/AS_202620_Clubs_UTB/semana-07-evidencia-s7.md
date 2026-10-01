# semana-07-evidencia-s7 · Clubs UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `dc211b8` en `origin/master` (2026-09-20T23:56:51-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

> Revisión actualizada tras el cierre: se leyeron en el repositorio, en el hash dc211b8, las filas que la pasada automática había dejado como No verificado.

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.yaml:1 declara `openapi: 3.1.0` y el archivo está en el árbol del commit dc211b8. | Cumple | Es especificación ejecutable, no prosa; único contrato del repo (no hay AsyncAPI ni proto). |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.yaml define 9 rutas (/health, /clubes, /clubes/{club_id}, /clubes/{club_id}/miembros, /clubes/{club_id}/eventos, /eventos/{evento_id}, /eventos/{evento_id}/asistencia, /clubes/{club_id}/publicaciones, /publicaciones/{publicacion_id}) con responses y requestBody que referencian #/components/schemas/{Club,Evento,Membresia,Publicacion,ErrorResponse}. | Cumple | El volcado del archivo se corta antes de components/schemas, por lo que solo se citan las referencias a esquemas, no sus definiciones. |
| Correspondencia entre el contrato y la API implementada | En dc211b8, `backend/src/linkclub/adapters/inbound/api/health_router.py:10` implementa `@router.get("/health")` y `backend/src/linkclub/adapters/inbound/api/publicacion_router.py:49-50,69-70` implementa `@router.post` y `@router.get` sobre `/clubes/{club_id}/publicaciones`; ambas rutas existen en `docs/api/openapi.yaml` (paths `/health` y `/clubes/{club_id}/publicaciones`) y `backend/src/linkclub/main.py` solo incluye esos dos routers, cuyas rutas figuran en el contrato. | Cumple | Cotejo en ambos sentidos sin desincronización: dos rutas del contrato (`/health`, `/clubes/{club_id}/publicaciones`) están en el código y la única ruta de código está en el contrato. El contrato se declara API-first (meta por construir); la nota de `docs/api/contrato_api.md` que aún nombra `POST /publicaciones` y `GET /publicaciones/{club_id}` es inconsistencia de esa narrativa, no del código frente al contrato. |
| Versión de la API declarada y con historial | docs/api/openapi.yaml declara info.version 1.0.0, docs/api/CHANGELOG.md registra '## 1.0.0 - 2026-09-20' y la ruta del contrato aparece en los commits 659b9bf y e0eaca4 (2026-09-20). | Cumple | No se aportó `git log` específico del archivo; la corrección del contrato del mismo día no subió la versión. |
| Prueba de contrato presente | backend/tests/test_contrato_openapi.py existe en el árbol de dc211b8 y el ADR 0003 lo describe verificando esquemas de respuesta y rutas del código. | Cumple | Solo se cita la ruta de la prueba; no se volcó su contenido. |
| El pipeline ejecuta la prueba de contrato | `.github/workflows/contrato.yml:30-34` define el job `prueba-contrato` y ejecuta la prueba con `run: pytest tests/test_contrato_openapi.py -v` (línea 34, con `PYTHONPATH: src`); el workflow además corre spectral (`:18`) y oasdiff (`:49`). | Cumple | La línea que la invoca es contrato.yml:34. La URL del run es externa: la consulta sin autenticar a `actions/runs` no devolvió ejecuciones del hash dc211b8 (las más recientes son del 2026-09-28, posteriores al cierre), así que se decide con la línea del workflow. |
| Evidencia de que la prueba falla ante un cambio incompatible | Se esperaba un run en rojo del job cambios-incompatibles (oasdiff) o la evidencia aportada por el equipo; la consulta sin autenticar a `actions/runs` no devolvió runs del hash dc211b8 ni hay artefacto entregado. | No verificado | Queda como pregunta de sustentación: es el criterio que separa competente de sobresaliente en este corte. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0003- integacion rest openapi.md (idéntico a docs/adr/0003-API.md) decide REST síncrono con contrato OpenAPI, descarta todo asíncrono, polling y GraphQL, y traza a U3 y C1 de docs/arc42/10_requisitos_de_calidad.md. | Cumple | Hay dos archivos con el número 0003 y el enlace citado en docs/arc42/09_decisiones_de_diseno.md (0003-integracion-rest-openapi.md) no existe en el árbol. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06_vista_de_ejecucion.md contiene diagrama de secuencia de GET /health (cliente → health_router → CheckHealthUseCase → StatusPort → InMemoryStatusAdapter) y descripción paso a paso. | Cumple | Solo documenta el flujo de health; el flujo de publicaciones, que sí tiene código, no aparece. |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/c4/contexto.md` reúne tres diagramas; el de nivel 2 (contenedores) está en `:22-48`. Solo `APP -->|Solicitudes JSON/HTTPS| API` (`:45`) declara protocolo y formato; las flechas persona→app (`:41-43`, «Usa») y las de la API hacia Supabase (`:46` «Valida tokens de sesión», `:47` «Lee y escribe datos») no declaran ni protocolo ni formato. | No cumple | La fila exige el nivel 2 con cada flecha etiquetada con protocolo y formato; el diagrama de contenedores existe, pero las relaciones que cruzan el límite hacia el sistema externo carecen de etiquetado. El diagrama de componentes (`:50-86`) repite el patrón y suma flechas sin protocolo ni formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_Clubs_UTB, visible: true, con historial de 6 cuentas de autor que se consolidan en al menos 4 identidades (dos cuentas comparten el mismo correo y corresponden al mismo autor). | Cumple | El README asocia los handles a los 4 integrantes; la cuenta 'Zavod Dev' no se atribuye a una persona por parecido de nombre. |
| Estructura mínima | El árbol de dc211b8 incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Faltan las secciones 07 y 11 de arc42; los ADR incumplen la convención de nombre (se registra en su fila). |
| Convenciones de ADR | docs/adr/ contiene '0003- integacion rest openapi.md' (espacio y sin kebab-case) y '0003-API.md' (número duplicado y título que no enuncia la decisión), y docs/arc42/09_decisiones_de_diseno.md enlaza ../adr/0003-integracion-rest-openapi.md, ruta inexistente. | No cumple | 0001-hexagonal.md y 0002-ajuste-contextos-publicaciones.md sí cumplen número, nombre y trazabilidad. |
| Tabla de aspectos | `docs/aspectos.md`: el encabezado es `ID · Aspecto de calidad · Escenario · Requisito (resumen) · C4 · ADR · Código · Pruebas`, sin la columna Evidencia del contrato, y las filas U1, U3, C1, C2 y C3 dejan Código y Pruebas en «Pendiente», con el ADR en «— (pendiente…)». | No cumple | No presenta las ocho columnas del contrato (falta Evidencia y aparece Escenario) y tiene celdas que no llevan a ninguna parte («Pendiente», «—»), que el contrato cuenta como huecos. |
| Registro de uso de IA | `docs/ia.md` con último commit `d2d1450` (2026-09-15T10:14:52-05:00), dentro del periodo revisado; la tabla registra lo no incorporado y su motivo, p. ej. S4: conversión a Mermaid «Se usó como prueba, no incorporado. Fue una consulta previa para validar el enfoque; el C4 nivel 2 final se construyó por otra vía». | Cumple | La entrada más reciente está rotulada S6 y no hay fila explícita de S7, pero el archivo recibió un commit dentro del periodo y documenta lo rechazado con su motivo. |
| README | README.md describe el sistema y el problema (secciones 1-2), stack, estructura, equipo y 'Cómo arrancar' con requisitos previos (Python 3.10+), venv, `uvicorn linkclub.main:app --app-dir src` y `PYTHONPATH=src pytest tests/ -v`. | Cumple | El arranque son cuatro comandos documentados, no un único comando, como pide el contrato. |
| Pipeline y análisis estático | En el árbol de dc211b8 solo hay .github/workflows/backend-tests.yml y .github/workflows/contrato.yml; no existe sonar-project.properties ni configuración equivalente y la evidencia no aporta run ni URL pública de SonarCloud con Quality Gate. | No cumple | Faltan las tres piezas exigidas (config + línea del scanner, run exitoso del hash, URL del análisis); tampoco se puede verificar que el pipeline bloquee la integración. |
| Secretos | El escaneo de secretos sobre HEAD no arrojó coincidencias y envs_versionados está vacío (ningún .env versionado). | Cumple | Sin hallazgos de credenciales en el commit revisado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `dc211b8f38c4f8d0ba0ebd13021e3181b6d573bb 2026-09-20T23:56:51-05:00 Merge pull request #2 from ISCOUTB/contrato-openapi`
- **Veredicto**: con pendientes
- Resumen: Releídas en el repositorio las filas que la pasada automática había dejado como No verificado, en la punta de origin/master (dc211b8, 2026-09-20, antes del cierre) el contrato OpenAPI 3.1 corresponde con la API implementada, el workflow de contrato invoca la prueba (`contrato.yml:34`), el registro de IA sí registró dentro del periodo con rechazos motivados, y la tabla de aspectos no cumple (sin columna Evidencia y con celdas «Pendiente»). El C4 nivel 2 no etiqueta con protocolo ni formato las flechas hacia el sistema externo. Sigue sin análisis estático público y sin run en rojo del cambio incompatible.

Pendientes que siguen abiertos:
- Aportar un run en rojo (o la evidencia del equipo) del cambio incompatible que hizo fallar la prueba.
- Publicar el análisis SonarCloud con Quality Gate y la configuración del scanner en el repositorio.
- Etiquetar con protocolo y formato las flechas del C4 nivel 2 y, en particular, las que cruzan hacia Supabase.
- Completar `docs/aspectos.md` con las ocho columnas del curso y sin celdas «Pendiente».
- Actualizar docs/arc42/tabla_modulo.md a los tres contextos vigentes (abierto en ADR 0002 y arc42 §8.3).
- Cerrar NC-01 y NC-02 de docs/arc42/lista_errores.md.
- Eliminar el ADR duplicado y renombrar 0003 según NNNN-kebab-case, corrigiendo el enlace roto.
- Completar las secciones 07 y 11 de arc42 y documentar el flujo de publicaciones en la vista de ejecución.

## Recuento y nota sugerida

8 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.2 = 1 + 4 × (8/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Evidencia de que la prueba de contrato falla ante un cambio incompatible: no hay run en rojo del hash dc211b8 ni evidencia aportada por el equipo. Queda como pregunta de sustentación (es el criterio que separa competente de sobresaliente en este corte).
- C4 nivel 2 con protocolo y formato en cada flecha: No cumple; el diagrama existe, pero varias flechas no declaran protocolo ni formato (fila de la matriz).
- Tabla de aspectos con las ocho columnas navegables: No cumple; falta la columna Evidencia y hay celdas «Pendiente» (fila transversal).

Filas releídas y resueltas en el hash dc211b8:
- Correspondencia contrato↔código: Cumple (`health_router.py:10` y `publicacion_router.py:49-50,69-70` frente a `docs/api/openapi.yaml`).
- El pipeline ejecuta la prueba de contrato: Cumple (`.github/workflows/contrato.yml:34`).
- Registro de uso de IA: Cumple (`docs/ia.md`, commit `d2d1450` del 2026-09-15 dentro del periodo, con lo rechazado y su motivo).

## Hallazgos para la planilla

- El contrato OpenAPI 3.1 (docs/api/openapi.yaml) está versionado, con 9 rutas, esquemas referenciados y CHANGELOG en SemVer.
- Correspondencia contrato↔código verificada en dc211b8: dos rutas del contrato (`/health`, `/clubes/{club_id}/publicaciones`) están en el código y la ruta de código está en el contrato; la narrativa de `docs/api/contrato_api.md` sí nombra rutas antiguas.
- `.github/workflows/contrato.yml` invoca la prueba de contrato (`pytest tests/test_contrato_openapi.py`) en la línea 34, con jobs de spectral y oasdiff; no hay run en rojo del hash dc211b8.
- El C4 nivel 2 (docs/c4/contexto.md) no etiqueta con protocolo y formato las flechas hacia Supabase: No cumple.
- docs/aspectos.md sigue sin la columna Evidencia del contrato y con celdas «Pendiente»: No cumple.
- docs/ia.md tiene un commit dentro del periodo (d2d1450, 2026-09-15) con lo rechazado y su motivo.
- Existen dos ADR con el número 0003, uno con espacio en el nombre, y el enlace a 0003-integracion-rest-openapi.md está roto desde arc42 §9 y el contrato.
- No hay rastro de SonarCloud: sin archivo de configuración ni URL pública de análisis con Quality Gate.
- docs/arc42/tabla_modulo.md sigue desalineado con los tres contextos vigentes, pendiente declarado en el ADR 0002 y en arc42 §8.3.
- NC-01 (datos de clubes hardcodeados) y NC-02 (sin manejo de errores de conexión) siguen 'pendiente' en docs/arc42/lista_errores.md.
- arc42 no incluye las secciones 07 y 11.
- HEAD dc211b8 (2026-09-20T23:56:51-05:00) es anterior al cierre y no hay commits posteriores en la rama principal.
