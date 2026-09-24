# semana-07-evidencia-s7 · EnAgenda

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `849ee8c` en `origin/master` (2026-09-20T23:59:07-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.yaml:1 `openapi: 3.0.3`, presente en el árbol de 849ee8c (2026-09-20T23:59:07-05:00). | Cumple | Es especificación ejecutable, no prosa; servidor declarado http://localhost:5000. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.yaml: paths `/api/v1/invitaciones/{token}` (GET, POST) con `$ref` a components.schemas.Invitacion, RespuestaInvitacion y Error en respuestas 200/400/404. | Cumple | Los esquemas declaran tipos, campos requeridos, enum de estado y ejemplos. |
| Correspondencia entre el contrato y la API implementada | `app/web.py` implementa GET y POST en `/api/v1/invitaciones/<token>`, pero también expone `/` y `/invitacion/<token>` sin declararlos en `docs/api/openapi.yaml`. | No cumple | Hay correspondencia para las dos operaciones contratadas, pero una ruta del código no está en el contrato; la sincronización bidireccional exigida no se sostiene. |
| Versión de la API declarada y con historial | `docs/api/openapi.yaml` declara `info.version: 1.0.0`; `git log` registra su creación en `bda4116` (2026-09-20T17:40:38-05:00). | Cumple | La versión y el archivo están bajo control de versiones en el estado calificado. |
| Prueba de contrato presente | `tests/test_api_invitaciones.py` prueba respuestas funcionales de GET/POST, pero no lee ni valida `docs/api/openapi.yaml` ni sus esquemas. | No cumple | Es una prueba de API, no una prueba de contrato contra la especificación ejecutable. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml solo contiene `run: pytest -q` tras instalar dependencias; ninguna línea invoca contract/schemathesis/dredd/pact/prism/spectral/openapi. | No cumple | El run exitoso runs/35575083849 es un CI genérico de pytest, no identifica paso de contrato; se esperaba el comando de contrato en el workflow y su URL de run. |
| Evidencia de que la prueba falla ante un cambio incompatible | runs_ci de master: 10 runs listados, todos con conclusion `success` (p. ej. runs/35575083849); no hay run en rojo ni evidencia aportada por el equipo. | No verificado | Queda como pregunta de sustentación: falta la ejecución que demuestre que la prueba falla al romper el contrato. |
| ADR de la estrategia de integración ligado a un escenario | En 849ee8c el árbol solo lista docs/adr/0001-usar-monolito-modular.md; docs/adr/0002-estrategia-integracion-api.md aparece en el commit 54ecb57 (2026-09-21T02:36:10-05:00), posterior al cierre. | No cumple | El ADR-0001 trata el estilo arquitectónico, no la estrategia de integración síncrona/asíncrona con alternativa descartada. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/06-vista-de-ejecución.md` describe el flujo de respuesta a invitación, sus siete pasos, errores y correspondencia con aplicación, dominio e infraestructura. | Cumple | El documento ya tenía un flujo verificable en 849ee8c; el ajuste posterior al cierre no es necesario para cumplir esta fila. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/nivel-2-contenedores.md: `Rel(organizador, webApp, "Utiliza", "HTTP")` y `Rel(webApp, invitaciones, "Gestiona invitaciones", "Llamada interna")`, sin formato de datos. | No cumple | Solo dos flechas declaran protocolo y ninguna declara formato en el estado calificado; la modificación posterior al cierre no cambia esta fila. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio público AS_202620_EnAgenda en la organización ISCOUTB; historial de 849ee8c con tres cuentas distintas (Daoisttl0FB3, Jein-12, eliabarnedocondef10-gif) más una cuarta entrada de la misma persona que repite su dirección de contacto. | Cumple | Consolidadas las identidades, los contribuyentes coinciden con los tres integrantes declarados. |
| Estructura mínima | Árbol de 849ee8c con docs/arc42/01..12, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | C4 está en docs/c4/ y no en docs/arc42/ (desviación admisible); se versionan archivos __pycache__/*.pyc en src/ y tests/. |
| Estado del repositorio calificado | Rama principal origin/master; commit 849ee8c del 2026-09-20T23:59:07-05:00, anterior al cierre 2026-09-21T05:00:00Z. | Cumple | HEAD 6db7cd9 (2026-09-21T02:53:08-05:00) es posterior al cierre y no cambia la matriz. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md cumple el patrón NNNN-titulo-en-kebab-case y contiene contexto, alternativas, decisión, consecuencias y trazabilidad. | Cumple | El historial del ADR registra una sola revisión hasta el estado calificado. |
| La tabla de aspectos | docs/aspectos.md: fila A-01 con las ocho columnas y enlaces navegables a C4 niveles 1-3, ADR-0001, src/invitaciones/ y app/web.py, tests/test_invitaciones.py y docs/evidencia.md. | Cumple | Una sola fila con todos los eslabones navegables. |
| Registro de uso de IA | docs/ia.md con columna de lo rechazado y su motivo técnico, e historial en git con entradas del 2026-08-25 al 2026-09-13. | Cumple | La última entrada es del 2026-09-13: el registro no crece con la entrega de la semana 7. |
| README | README.md declara qué es el sistema, requisitos previos (Python 3.13, pip), instalación y arranque con `python app\web.py` y pruebas con `pytest -q`. | Cumple | El arranque es un solo comando tras instalar dependencias. |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta checkout, setup-python, pip install y `pytest -q`; no hay sonar-project.properties en el árbol ni paso de scanner SonarCloud, y no se aporta URL pública de análisis con Quality Gate. | No cumple | El run exitoso runs/35575083849 solo prueba las pruebas unitarias; el análisis estático transversal queda sin las tres evidencias exigidas. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `6db7cd98f957c757aa37aeda47a52b9e54831e12 2026-09-21T02:53:08-05:00 Update nivel-2-contenedores.md`
- **Veredicto**: con pendientes
- Resumen: En la punta de master (6db7cd9) el contrato OpenAPI 3.0.3 con esquemas está versionado y arc42 §6 ya era verificable al cierre. Siguen abiertas la sincronización bidireccional contrato-código, una prueba que valide el OpenAPI, su ejecución explícita y el fallo ante incompatibilidad; el ADR de integración y el ajuste del C4 llegaron después del cierre, y SonarCloud continúa sin evidencia pública.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 54ecb57 2026-09-21T02:36:10-05:00 Create 0002-estrategia-integracion-api.md (ADR posterior al cierre)
- 9ebd147 2026-09-21T02:46:20-05:00 Update 06-vista-de-ejecución.md
- 6db7cd9 2026-09-21T02:53:08-05:00 Update nivel-2-contenedores.md
- a02f375 2026-09-21T02:30:15-05:00 y 61cb4d0 2026-09-21T02:31:44-05:00: alta y borrado previos del mismo ADR

Pendientes que siguen abiertos:
- Prueba de contrato ejecutada por el pipeline y evidencia de su fallo ante un cambio incompatible
- Sincronizar con el contrato las rutas `/` y `/invitacion/<token>` expuestas por `app/web.py`
- SonarCloud: scanner en el workflow, run exitoso del hash y URL pública con Quality Gate
- C4 nivel 2 con protocolo y formato por flecha
- Limpieza de __pycache__ versionado

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correspondencia contrato↔código: las rutas `/` y `/invitacion/<token>` no están en el OpenAPI.
- Prueba de contrato: `tests/test_api_invitaciones.py` no valida la especificación OpenAPI.
- Fallo de la prueba ante cambio incompatible: sin run en rojo ni evidencia aportada; pregunta de sustentación.
- El ADR de integración y los ajustes de C4 posteriores al cierre no alteran el resultado definitivo de S7.
- SonarCloud: falta archivo de configuración, línea del scanner en el workflow y URL pública del análisis con Quality Gate.

## Hallazgos para la planilla

- Commit calificado 849ee8c (2026-09-20T23:59:07-05:00) dentro del cierre; HEAD 6db7cd9 (2026-09-21T02:53:08-05:00) posterior.
- docs/api/openapi.yaml es OpenAPI 3.0.3 con rutas y esquemas Invitacion, RespuestaInvitacion y Error.
- El workflow solo ejecuta `pytest -q`: sin herramienta de contrato y sin SonarCloud.
- Ningún run en rojo en la rama master: la prueba de contrato no demuestra que pueda fallar.
- El ADR de estrategia de integración (0002) se creó después del cierre en 54ecb57.
- arc42 §6 y C4 nivel 2 se actualizaron con commits posteriores al cierre (9ebd147, 6db7cd9).
- Las flechas del C4 nivel 2 usan "HTTP" y "Llamada interna" sin formato de datos.
- Identidades del historial: tres cuentas distintas y una cuarta entrada de la misma persona (misma dirección de contacto).
- Coincidencias de la búsqueda de secretos corresponden a tokens de invitación y variables locales, no a credenciales.
- Se versionan archivos generados __pycache__/*.pyc en src/ y tests/.
- Commits posteriores al cierre (no calificados): 6db7cd9 2026-09-21T02:53:08-05:00 Update nivel-2-contenedores.md; 9ebd147 2026-09-21T02:46:20-05:00 Update 06-vista-de-ejecución.md; 54ecb57 2026-09-21T02:36:10-05:00 Create 0002-estrategia-integracion-api.md; 61cb4d0 2026-09-21T02:31:44-05:00 Delete docs/adr/0002-estrategia-integracion; a02f375 2026-09-21T02:30:15-05:00  0002-estrategia-integracion
