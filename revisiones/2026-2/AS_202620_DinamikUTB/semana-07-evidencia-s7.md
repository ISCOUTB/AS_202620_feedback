# semana-07-evidencia-s7 · DinamikUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `5e6fa73` en `origin/master` (2026-09-20T23:57:27-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

> Revisión actualizada tras el cierre: se leyeron en el repositorio, en el hash 5e6fa73, las filas que la pasada automática había dejado como No verificado.

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.json en el árbol de 5e6fa73, con `openapi: 3.1.0` y 4 rutas. | Cumple | Es especificación OpenAPI real, no prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.json: components.schemas con EstudianteOut, RequisitoOut, RequisitoEstadoUpdate, HTTPValidationError y ValidationError, con `required` y tipos. | Cumple | Las respuestas 200 referencian esquemas de datos. |
| Correspondencia entre el contrato y la API implementada | backend/tests/test_contrato.py compara `contrato_guardado == app.openapi()`; rutas del contrato en backend/app/estudiantes/router.py y backend/app/requisitos/router.py. | Cumple | La comparación cubre ambos sentidos; run verde 35553215099. |
| Versión de la API declarada y con historial | `docs/api/openapi.json` declara `"info": {"title": "DinamikUTB API", "version": "0.1.0"}`, y `git log --format='%h %cI %s' -- docs/api/openapi.json` sobre 5e6fa73 muestra `b05a5ac 2026-09-20T16:45:17-05:00 Exportar y versionar el contrato OpenAPI generado por FastAPI`. | Cumple | El contrato tiene versión declarada y un único commit de versionado (b05a5ac), del mismo día del cierre; no hay evolución previa registrada. |
| Prueba de contrato presente | backend/tests/test_contrato.py, con backend/scripts/export_openapi.py para regenerar el contrato. | Cumple | La prueba existe y está versionada. |
| El pipeline ejecuta la prueba de contrato | `.github/workflows/ci.yml:29-30`, paso «Run tests» con `run: pytest` en el job `backend-tests` (`working-directory: backend`), que con `testpaths = ["tests"]` (`backend/pyproject.toml:16`) recolecta `backend/tests/test_contrato.py`; run 35551548541 en rojo sobre `test_el_contrato_versionado_coincide_con_la_api_real` y run 35553215099 en verde con 11 pruebas. | Cumple | Workflow leído en 5e6fa73: la prueba de contrato se ejecuta por recolección de pytest, sin paso `continue-on-error`. |
| Evidencia de que la prueba falla ante un cambio incompatible | docs/api/evidencia-prueba-contrato.md: commit f7c17b9 añade `creditos` sin regenerar el contrato y el run 35551548541 sale rojo con AssertionError en tests/test_contrato.py:19. | Cumple | Es la prueba en rojo exigida por el laboratorio. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0004-comunicacion-sincrona-frontend-backend.md: comunicación síncrona HTTP, alternativa de mensajería descartada y trazabilidad a Q-01. | Cumple | Documenta el acoplamiento temporal como consecuencia negativa. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/06-runtime-view.md` describe tres flujos de interacción con pasos numerados y trazados a requisitos y escenarios: 6.1 consulta del progreso de graduación (RF-01/RF-02, Q-01/Q-03), 6.2 control de acceso a información académica (RF-05, Q-02) y 6.3 corrección de un requisito por el coordinador (RF-07); además advierte qué parte está implementada y qué es diseño previsto. | Cumple | No es la plantilla vacía: los tres flujos están escritos y ligados a requisitos y escenarios de calidad. |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/c4/contenedores.puml` es el nivel 2 en C4-PlantUML; las relaciones que cruzan el límite llevan protocolo y formato: `Rel(frontend, backend, "Consume la API", "HTTP/JSON")` (`:20`) y `Rel(backend, database, "Lee y escribe información", "SQL, vía SQLAlchemy (ORM)")` (`:21`). | Cumple | Las tres flechas persona→frontend (`:17-19`) describen la interacción («Interactúa con la interfaz») sin protocolo ni formato; el etiquetado se cumple en las relaciones contenedor↔contenedor y contenedor↔base de datos, que son las que cruzan un límite tecnológico. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_DinamikUTB público; 7 identidades de autor que, consolidadas, dan 4 contribuyentes, coincidentes con los 4 integrantes declarados. | Cumple | Varias cuentas por persona; no se atribuye por parecido de nombre. |
| Estructura mínima | docs/arc42/ con las 12 secciones, docs/adr/0001 a 0004, docs/c4/contenedores.puml, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Sin desviaciones relevantes; el C4 está como código. |
| Estado del repositorio que se califica | Rama principal origin/master; hash calificado 5e6fa73 del 2026-09-20T23:57:27-05:00, anterior al cierre 2026-09-21T05:00:00Z. | Cumple | Existe un commit posterior al cierre (8a5ae13), registrado en overall. |
| Convenciones de ADR | docs/adr/0001-seleccion-monolito-modular.md a docs/adr/0004-comunicacion-sincrona-frontend-backend.md siguen NNNN-kebab-case con contexto, alternativas, decisión, consecuencias y trazabilidad. | Cumple | Los cuatro nombres siguen la convención del contrato §4; los archivos existen en el árbol de 5e6fa73. |
| ADR aceptados no reescritos | Los cuatro ADR declaran `status: Aceptado` (línea 4). Historial hasta 5e6fa73: ADR-0001 se creó en `3d5aad8` (2026-08-23T04:00:05-05:00) y se editó en `15d38f9` (2026-09-01T01:01:30-05:00, añade la sección 10 «Trazabilidad»); ADR-0002 se creó en `842cab5` (2026-08-30T21:24:55-05:00) y se editó en `bc70d93` (2026-09-01T01:03:13-05:00, añade la sección 9 «Trazabilidad»); ADR-0003 se creó en `934b774` y se editó en `33952d5` (2026-09-06T23:21:38-05:00). Ningún ADR declara que otro lo reemplace. | No cumple | CONTRATO §4 prohíbe editar un ADR aceptado. Las ediciones de ADR-0001 y ADR-0002 son adiciones de contenido (trazabilidad) posteriores a la aceptación, no meras correcciones de formato o enlaces, y no hay reemplazo declarado. ADR-0004 (`15555f4`, 2026-09-20) sí tiene un único commit. |
| Registro de uso de IA | Historial de docs/ia.md con 19 commits entre 2026-08-09 y 2026-09-20 (último aa35148); contenido leído: documenta rechazos con motivo, p. ej. «Rechazado parcialmente» por sobrecarga visual (línea 15), «Rechazado» del glosario por definiciones genéricas (línea 26) y «Rechazado por ahora» del lock file por prioridad de tiempo (línea 38). | Cumple | La columna de lo rechazado existe y cita el motivo; no solo los usos aceptados. |
| Pipeline y análisis estático | .github/workflows/ci.yml y sonar-project.properties existen, pero los commits 1ffe3e2 y 5e6fa73 documentan un bloqueo de permisos en la migración de SonarCloud a CI. | No cumple | Se esperaba run que invoque el scanner y URL pública del análisis con Quality Gate; no se aportó ninguna. |
| Sin credenciales en el repositorio ni en el historial | `git grep -nI -E "(api[_-]?key|secret|password|token|passwd)"` sobre 5e6fa73 solo devuelve la referencia `${{ secrets.SONAR_TOKEN }}` en `.github/workflows/ci.yml:67` y menciones de «token» en prosa de `docs/`. `git ls-tree` no lista ningún `.env` versionado y `git log -S'BEGIN PRIVATE KEY'` no devuelve commits. | Cumple | Sin coincidencias reales de credenciales; `secrets.SONAR_TOKEN` es una referencia a un secreto de GitHub, no un valor almacenado en el repositorio. |
| Contribución de todos los integrantes | `git shortlog -sne 5e6fa73` da 7 filas que, consolidadas por correo registrado idéntico, corresponden a 4 personas: una agrupa tres firmas del mismo correo (144 commits) y las otras suman 45, 26 y 11. Coinciden con los 4 integrantes declarados en EQUIPOS.md. | Cumple | Consolidación por correo idéntico, nunca por parecido de nombre; el desbalance de aportes se anota en la planilla. |
| Tabla de aspectos | `docs/aspectos.md` presenta las ocho columnas del contrato más «Escenario de calidad» (`ID · Aspecto · Requisito · Escenario de calidad · C4 · ADR · Código · Pruebas · Evidencia`), pero en A-02 a A-08 las columnas C4, Código, Pruebas y Evidencia están en «Pendiente», y en A-01 la Evidencia también. | No cumple | Las ocho columnas existen, pero las celdas «Pendiente» no llevan a ninguna parte y el contrato las cuenta como huecos. |
| README | README.md describe el sistema, el arranque con un solo comando (`start.bat`) y las pruebas (`pytest`, `flutter test`, `flutter analyze`). | Cumple | Declara requisitos previos (Python 3.12, Flutter, Git, Chrome). |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `8a5ae134a33c202febdc06fe95d01d2d4bae2ad8 2026-09-21T00:01:43-05:00 Update ci.yml`
- **Veredicto**: con pendientes
- Resumen: Releídas en el repositorio las filas que la pasada automática había dejado como No verificado, en la punta de origin/master (5e6fa73, con un commit posterior al cierre 8a5ae13) la entrega de S7 está resuelta: contrato OpenAPI con esquemas y versión declarada con historial, prueba de contrato demostrada en rojo, ADR de integración con alternativa descartada, arc42 §6 con tres flujos de interacción y C4 nivel 2 con protocolo y formato en las relaciones que cruzan límites. Quedan sin resolver el análisis estático en SonarCloud y la tabla de aspectos, con las ocho columnas presentes pero celdas «Pendiente».

Resuelto tarde (corregido despues del cierre, ahora al dia):
- YAML de ci.yml corregido en 31350f1 el mismo día del cierre, tras el experimento del contrato.
- Bloqueo de permisos de SonarCloud documentado como hallazgo en 1ffe3e2 y 5e6fa73 en vez de resolverse.
- Commit 8a5ae13 'Update ci.yml' posterior al cierre (2026-09-21T00:01:43-05:00).

Pendientes que siguen abiertos:
- SonarCloud: run que invoque el scanner y URL pública del análisis con Quality Gate.
- Tabla de aspectos con las ocho columnas navegables y sin celdas «Pendiente» (A-02 a A-08 y la evidencia de A-01).

## Recuento y nota sugerida

10 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 5.0 = 1 + 4 × (10/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Tabla de aspectos (docs/aspectos.md): No cumple; tiene las ocho columnas, pero A-02 a A-08 y la evidencia de A-01 quedan en «Pendiente».
- SonarCloud: sigue sin run que invoque el scanner ni URL pública con Quality Gate (fila transversal).
- Línea de .github/workflows/ci.yml que invoca la prueba: citada en la fila correspondiente (`run: pytest`, línea 30); la URL del run queda como corroboración externa.

## Hallazgos para la planilla

- SonarCloud sigue sin ejecución auditable: los propios commits registran un bloqueo de permisos en lugar de la URL del análisis.
- La prueba de contrato se demuestra en rojo con f7c17b9 y el run 35551548541, y en verde tras el revert con 31350f1 y el run 35553215099.
- El contrato `docs/api/openapi.json` declara la versión 0.1.0 y tiene un único commit de versionado (b05a5ac, 2026-09-20): versionado, sin evolución previa registrada.
- arc42 sección 6 describe tres flujos de interacción reales (6.1-6.3) trazados a requisitos y escenarios de calidad.
- El C4 nivel 2 (`docs/c4/contenedores.puml`) etiqueta con protocolo y formato las relaciones frontend→backend (HTTP/JSON) y backend→base de datos (SQL); las flechas persona→frontend solo describen la interacción.
- docs/aspectos.md: No cumple; las ocho columnas están, pero A-02 a A-08 y la evidencia de A-01 quedan en «Pendiente».
- Hubo un error de sintaxis YAML en ci.yml que venía afectando el pipeline y se corrigió en 31350f1.
- El commit 8a5ae13 ('Update ci.yml') queda posterior al cierre, dos minutos después del límite.
- Commits posteriores al cierre (no calificados): 8a5ae13 2026-09-21T00:01:43-05:00 Update ci.yml
