# semana-07-evidencia-s7 · Drift

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `9334a03` en `origin/master` (2026-09-20T20:19:47-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

> Revisión actualizada tras el cierre: se leyeron en el repositorio, en el hash 9334a03, las filas que la pasada automática había dejado como No verificado.

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/drift/openapi.yaml (openapi: 3.1.0), docs/api/playstation/openapi.yaml (3.0.3) y docs/api/playstation/asyncapi.yaml (3.0.0), presentes en el árbol de 9334a03. | Cumple | Tres contratos ejecutables versionados; no se puntúa la cantidad de endpoints. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | En docs/api/drift/openapi.yaml: paths /, /games/search, /games/sync/playstation y /games/{game_id}/compatibility, con components.schemas GameSearchResult, CompatibilityRequest, CompatibilityResult, HealthResponse y SyncError. | Cumple | Los esquemas declaran required y properties (`components.schemas` en la línea 171); el archivo se leyó completo desde el repositorio (237 líneas). |
| Correspondencia entre el contrato y la API implementada | `backend/app/main.py` define `@app.get("/")`, `@app.get("/games/search")`, `@app.post("/games/sync/playstation")` y `@app.post("/games/{game_id}/compatibility")`, las cuatro rutas de `docs/api/drift/openapi.yaml`; `backend/tests/test_contract.py` valida ese contrato con Schemathesis desde `../docs/api/drift/openapi.yaml`. | Cumple | Dos rutas del contrato (`/`, `/games/search`) y una del código (`/games/{game_id}/compatibility`) coinciden; no hay desincronización en ningún sentido. |
| Versión de la API declarada y con historial | info.version: 1.0.0 en docs/api/drift/openapi.yaml, y sección 8 'Historial de versiones' (1.0.0 \| 2026-09-19) en docs/api/drift/contrato_API_DRIFT.md. | Cumple | `git log -- docs/api/drift/openapi.yaml` da tres commits dentro del estado calificado: f52b0ef y c4a6079 (2026-09-19) y 9f238ab (2026-09-20); 257d9ee (2026-09-27) es posterior al cierre. |
| Prueba de contrato presente | `backend/tests/test_contract.py` leído en 9334a03: usa Schemathesis desde `../docs/api/drift/openapi.yaml` contra `http://localhost:8000` con `@schema.parametrize()`. | Cumple | El comando que la invoca es `run: python -m pytest tests -q` en `.github/workflows/ci.yml:47`. |
| El pipeline ejecuta la prueba de contrato | `.github/workflows/ci.yml` instala `schemathesis==4.27.5`, levanta la API en `http://127.0.0.1:8000` y ejecuta `run: python -m pytest tests -q` desde `backend`, que recolecta `backend/tests/test_contract.py`. | Cumple | La línea que la ejecuta es `run: python -m pytest tests -q` (paso "Ejecutar pruebas unitarias y del corte vertical"); la URL del run es externa y no se corrobora en el repositorio. |
| Evidencia de que la prueba falla ante un cambio incompatible | `docs/evidencias/cambio_incompatible_evidencia.md` documenta el fallo controlado: `gpu_score` booleano aceptado con `200 OK` y resultado `1 failed, 13 passed`; los commits `6397c09` (`gpu_score: StrictInt` → `int`) y `715347d` (reversión) son el cambio incompatible y su deshacer. El run de CI `35549837357` sobre `master` existe con conclusión `failure`. | Cumple | Evidencia del fallo controlado leída en el repositorio y corroborada con el run fallido de Actions. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0004-estrategia-de-integracion.md: estado Aceptado, tres alternativas con ventajas y consecuencias, y escenario E2 de mantenibilidad con el acoplamiento descartado. | Cumple | Decide estrategia híbrida (consultas síncronas HTTP/JSON y actualización asíncrona con MySQL). |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/arc42_6_Vista_Ejecucion.md` describe tres escenarios con diagramas de secuencia Mermaid y explicación paso a paso: búsqueda y comparación de precios, fallo de una fuente externa y estimación de compatibilidad. | Cumple | Los flujos están descritos y ligados a los escenarios de calidad de `docs/escenarios.md`. |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/c4/contenedores.md`: diagrama Mermaid donde las relaciones llevan protocolo y formato (`WEB -->|"HTTP/REST + JSON"| API`, adaptadores `-->|"HTTP/REST + JSON"|` Steam y PlayStation, `USER -->|"HTTPS + interacción web"| WEB`), más la tabla de contenedores y relaciones. | Cumple | Las relaciones que cruzan el límite del proceso llevan protocolo y formato; las invocaciones internas son en proceso y el enlace a la base de datos se describe como "Persistencia de datos". |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio visible AS_202620_Drift en la organización ISCOUTB; el historial consolidado da 4 cuentas (JerryDBM/Sherry, JoshuaR01/JoshXX, lmpdiaz12 y maufern4ndez) y los 4 integrantes declarados aparecen en él. | Cumple | Consolidación por correo registrado idéntico entre alias, sin atribuir cuentas por parecido de nombre. |
| Estructura mínima | En 9334a03 existen docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | arc42 sin las secciones 7 ni 11 y con prefijo arc42_N_ en los nombres: desviación de forma, no ausencia del artefacto. |
| Estado del repositorio calificado | Rama origin/master, commit 9334a03 del 2026-09-20T20:19:47-05:00, anterior al cierre 2026-09-21T05:00:00Z; commits_tardios_post_cierre vacío. | Cumple | Único hash revisado, sin mezcla con otras ramas. |
| Convenciones de ADR | docs/adr/0001..0004 numerados en kebab-case, con contexto, opciones, decisión y consecuencias; 0001 marcado 'Reemplazado por ADR-0002' con enlace. | Cumple | 0003 y 0004 no enlazan commit o PR de implementación ('pendiente'), trazabilidad parcial. |
| Tabla de aspectos | `docs/aspectos.md`: tabla de trazabilidad arquitectónica con las columnas ID · Aspecto · Requisito · C4 · ADR · Código · Pruebas · Evidencia para E1–E5, con enlaces a C4 nivel 2, ADR-0002, rutas de código y las evidencias e1–e5. | Cumple | Ocho columnas presentes y eslabones enlazados; la prueba de sustitución del adaptador (E2) sigue declarada pendiente. |
| Registro de uso de IA | docs/ia.md con 29 entradas de git log entre 2026-08-09 y 2026-09-20 (última 0129608); contenido leído: 13 bloques «Alternativa descartada» con su motivo, p. ej. React con Vite descartado frente a Next.js (líneas 61-63) y las peticiones a la API directamente desde el frontend descartadas por acoplamiento (líneas 426-428). | Cumple | El rechazo con motivo técnico está documentado, no solo los usos aceptados. |
| README | README.md declara qué es el sistema, requisitos previos (Python 3.12, Node 22), arranque con un solo comando (python scripts/start.py) y cómo se prueba (pytest, npm run build, k6). | Cumple | No remite a pasos manuales no documentados. |
| Pipeline y análisis estático | sonar-project.properties existe en 9334a03 y el README describe el escaneo dentro de .github/workflows/ci.yml, pero no hay runs_ci ni URL pública del análisis. | No verificado | Se esperaba la línea del workflow que invoca el scanner, la URL del run exitoso y la URL pública con Quality Gate; comando anotado: curl -s https://api.github.com/repos/ISCOUTB/AS_202620_Drift/actions/runs. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `9334a03f97fc2ddb67846b8e6d229ff85898f3f1 2026-09-20T20:19:47-05:00 Update cambio_incompatible_evidencia.md`
- **Veredicto**: al dia
- Resumen: Releídas en el repositorio las filas que la pasada automática había dejado como No verificado, en la punta de origin/master (9334a03, 2026-09-20, antes del cierre) el proyecto tiene contratos ejecutables, correspondencia contrato-código, prueba de contrato presente y ejecutada por el pipeline, fallo controlado evidenciado, ADR ligado a E2, arc42-6, C4-2, tabla de aspectos de ocho columnas, estructura, README, registro de IA y ausencia de secretos. Sigue sin evidencia pública de SonarCloud ni URL del run en el repositorio.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Ninguno: commits_tardios_post_cierre está vacío y el último commit (9334a03) es anterior al cierre; los ajustes de contrato y su evidencia se registraron el 2026-09-20.

Pendientes que siguen abiertos:
- Aportar la URL pública de SonarCloud con Quality Gate y el run que invocó el scanner (fila transversal de pipeline).
- Enlazar en el repositorio la URL del run de CI, hoy solo citable como corroboración externa.

## Recuento y nota sugerida

10 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 5.0 = 1 + 4 × (10/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- SonarCloud: el README describe el escaneo y existe sonar-project.properties, pero no consta la línea del scanner en .github/workflows/ci.yml ni las URL del run y del análisis con Quality Gate.
- Run de CI: la ejecución y el fallo controlado se sostienen en el repositorio y en el run 35549837357 citado, pero la URL del run es corroboración externa.

## Hallazgos para la planilla

- Contrato OpenAPI 3.1 del backend y contratos OpenAPI/AsyncAPI de PlayStation versionados y con esquemas de datos.
- Correspondencia contrato-código verificada: las cuatro rutas del contrato están en backend/app/main.py.
- El pipeline instala Schemathesis y ejecuta la prueba de contrato; el fallo controlado está documentado y corroborado por el run 35549837357 en rojo.
- arc42 sección 6 (tres flujos), C4 nivel 2 con protocolo y formato, y tabla de aspectos con las ocho columnas: releídos y conformes.
- Sigue faltando la evidencia pública de SonarCloud con Quality Gate.
- Sin secretos ni .env versionados en el árbol revisado.
- Los cuatro integrantes declarados aparecen en el historial tras consolidar cuentas duplicadas.
- El ADR-0004 liga la estrategia de integración al escenario E2 con la alternativa descartada.
