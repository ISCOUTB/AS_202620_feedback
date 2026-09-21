# semana-07-evidencia-s7 · DinamikUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `5e6fa73` en `origin/master` (2026-09-20T23:57:27-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.json en el árbol de 5e6fa73, con `openapi: 3.1.0` y 4 rutas. | Cumple | Es especificación OpenAPI real, no prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.json: components.schemas con EstudianteOut, RequisitoOut, RequisitoEstadoUpdate, HTTPValidationError y ValidationError, con `required` y tipos. | Cumple | Las respuestas 200 referencian esquemas de datos. |
| Correspondencia entre el contrato y la API implementada | backend/tests/test_contrato.py compara `contrato_guardado == app.openapi()`; rutas del contrato en backend/app/estudiantes/router.py y backend/app/requisitos/router.py. | Cumple | La comparación cubre ambos sentidos; run verde 35553215099. |
| Versión de la API declarada y con historial | docs/api/openapi.json declara `info.version: 0.1.0`. | No verificado | No se aportó `git log --format='%h %cI %s' -- docs/api/openapi.json`; sin esa salida no se comprueba el historial del contrato. |
| Prueba de contrato presente | backend/tests/test_contrato.py, con backend/scripts/export_openapi.py para regenerar el contrato. | Cumple | La prueba existe y está versionada. |
| El pipeline ejecuta la prueba de contrato | Run https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/35551548541 con `test_el_contrato_versionado_coincide_con_la_api_real` fallando; run 35553215099 verde con 11 pruebas. | Cumple | Runs citados en docs/api/evidencia-prueba-contrato.md; no se aportó el contenido de .github/workflows/ci.yml. |
| Evidencia de que la prueba falla ante un cambio incompatible | docs/api/evidencia-prueba-contrato.md: commit f7c17b9 añade `creditos` sin regenerar el contrato y el run 35551548541 sale rojo con AssertionError en tests/test_contrato.py:19. | Cumple | Es la prueba en rojo exigida por el laboratorio. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0004-comunicacion-sincrona-frontend-backend.md: comunicación síncrona HTTP, alternativa de mensajería descartada y trazabilidad a Q-01. | Cumple | Documenta el acoplamiento temporal como consecuencia negativa. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06-runtime-view.md existe en el árbol de 5e6fa73. | No verificado | No se aportó su contenido; falta citar los flujos de interacción descritos. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/contenedores.puml y contenedores.png en el árbol; ADR-0004 cita la relación frontend a backend como HTTP/JSON. | No verificado | Solo se confirma una flecha; falta el diagrama para verificar el etiquetado de todas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_DinamikUTB público; 7 identidades de autor que, consolidadas, dan 4 contribuyentes, coincidentes con los 4 integrantes declarados. | Cumple | Varias cuentas por persona; no se atribuye por parecido de nombre. |
| Estructura mínima | docs/arc42/ con las 12 secciones, docs/adr/0001 a 0004, docs/c4/contenedores.puml, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Sin desviaciones relevantes; el C4 está como código. |
| Estado del repositorio que se califica | Rama principal origin/master; hash calificado 5e6fa73 del 2026-09-20T23:57:27-05:00, anterior al cierre 2026-09-21T05:00:00Z. | Cumple | Existe un commit posterior al cierre (8a5ae13), registrado en overall. |
| Convenciones de ADR | docs/adr/0001-seleccion-monolito-modular.md a docs/adr/0004-comunicacion-sincrona-frontend-backend.md siguen NNNN-kebab-case con contexto, alternativas, decisión, consecuencias y trazabilidad. | Cumple | No se aportó `git log --follow` para comprobar que los ADR aceptados no se reescribieron. |
| Tabla de aspectos | docs/aspectos.md existe y los ADR enlazan anclas como ../aspectos.md#a-01 y #a-02. | No verificado | Falta el contenido; no se pueden verificar las 8 columnas ni que las celdas sean navegables. |
| Registro de uso de IA | Historial de docs/ia.md con 19 commits entre 2026-08-09 y 2026-09-20 (último aa35148). | Cumple | Crece durante el semestre; no se aportó el texto, en particular la columna de lo rechazado. |
| README | README.md describe el sistema, el arranque con un solo comando (`start.bat`) y las pruebas (`pytest`, `flutter test`, `flutter analyze`). | Cumple | Declara requisitos previos (Python 3.12, Flutter, Git, Chrome). |
| Pipeline y análisis estático | .github/workflows/ci.yml y sonar-project.properties existen, pero los commits 1ffe3e2 y 5e6fa73 documentan un bloqueo de permisos en la migración de SonarCloud a CI. | No cumple | Se esperaba run que invoque el scanner y URL pública del análisis con Quality Gate; no se aportó ninguna. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `8a5ae134a33c202febdc06fe95d01d2d4bae2ad8 2026-09-21T00:01:43-05:00 Update ci.yml`
- **Veredicto**: con pendientes
- Resumen: En la punta de origin/master (5e6fa73, con un commit posterior al cierre 8a5ae13) la entrega de S7 está mayormente resuelta: contrato OpenAPI con esquemas, prueba de contrato demostrada en rojo y ADR de integración con alternativa descartada. Quedan sin resolver el análisis estático en SonarCloud y sin verificar arc42 sección 6, C4 nivel 2, historial del contrato y tabla de aspectos.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- YAML de ci.yml corregido en 31350f1 el mismo día del cierre, tras el experimento del contrato.
- Bloqueo de permisos de SonarCloud documentado como hallazgo en 1ffe3e2 y 5e6fa73 en vez de resolverse.
- Commit 8a5ae13 'Update ci.yml' posterior al cierre (2026-09-21T00:01:43-05:00).

Pendientes que siguen abiertos:
- SonarCloud: run que invoque el scanner y URL pública del análisis con Quality Gate.
- Contenido de arc42 sección 6 y del C4 nivel 2 con protocolo y formato por flecha.
- Historial git del contrato y confirmación de la versión de la API.
- Contenido de docs/aspectos.md con sus ocho columnas navegables.

## Recuento y nota sugerida

7 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Historial git del contrato: falta `git log --format='%h %cI %s' -- docs/api/openapi.json`.
- Contenido de docs/arc42/06-runtime-view.md: solo se ve la ruta en el árbol.
- Contenido de docs/c4/contenedores.puml: no se puede verificar protocolo y formato en cada flecha.
- Contenido de docs/aspectos.md: no se pueden verificar las ocho columnas ni la navegabilidad de las celdas.
- Línea de .github/workflows/ci.yml que invoca la prueba de contrato: se infiere del run, no del workflow.

## Hallazgos para la planilla

- SonarCloud sigue sin ejecución auditable: los propios commits registran un bloqueo de permisos en lugar de la URL del análisis.
- La prueba de contrato se demuestra en rojo con f7c17b9 y el run 35551548541, y en verde tras el revert con 31350f1 y el run 35553215099.
- Hubo un error de sintaxis YAML en ci.yml que venía afectando el pipeline y se corrigió en 31350f1.
- El commit 8a5ae13 ('Update ci.yml') queda posterior al cierre, dos minutos después del límite.
- No se aportó el contenido de arc42 sección 6 ni del C4 nivel 2, solo su ruta.
- No se aportó el historial git del contrato, aunque sí su versión declarada.
- Commits posteriores al cierre (no calificados): 8a5ae13 2026-09-21T00:01:43-05:00 Update ci.yml
