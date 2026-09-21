# semana-07-evidencia-s7 · Drift

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `9334a03` en `origin/master` (2026-09-20T20:19:47-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/drift/openapi.yaml (openapi: 3.1.0), docs/api/playstation/openapi.yaml (3.0.3) y docs/api/playstation/asyncapi.yaml (3.0.0), presentes en el árbol de 9334a03. | Cumple | Tres contratos ejecutables versionados; no se puntúa la cantidad de endpoints. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | En docs/api/drift/openapi.yaml: paths /, /games/search, /games/sync/playstation y /games/{game_id}/compatibility, con components.schemas GameSearchResult, CompatibilityRequest, CompatibilityResult, HealthResponse y SyncError. | Cumple | Los esquemas declaran required y properties; el archivo aportado está truncado (30 líneas finales). |
| Correspondencia entre el contrato y la API implementada | No se aporta el contenido de backend/app/main.py ni de backend/tests/test_contract.py en el árbol de 9334a03. | No verificado | Se esperaba citar dos rutas del contrato en el código y una del código en el contrato; sin el código no se puede comprobar la desincronización en ningún sentido. |
| Versión de la API declarada y con historial | info.version: 1.0.0 en docs/api/drift/openapi.yaml, y sección 8 'Historial de versiones' (1.0.0 \| 2026-09-19) en docs/api/drift/contrato_API_DRIFT.md. | Cumple | No se aporta el git log por archivo del contrato; el archivo sí está versionado en el commit 9334a03. |
| Prueba de contrato presente | backend/tests/test_contract.py en el árbol de 9334a03. | Cumple | No se aporta el contenido de la prueba ni el comando que la invoca. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/ci.yml en el árbol de 9334a03, pero no se aporta su contenido ni ninguna entrada de runs_ci. | No verificado | Se esperaba la línea del workflow que invoca la prueba de contrato y la URL del run; comando anotado: grep -niE 'contract\|schemathesis\|dredd\|pact\|prism\|spectral' .github/workflows/ci.yml. |
| Evidencia de que la prueba falla ante un cambio incompatible | Existe docs/evidencias/cambio_incompatible_evidencia.md y los commits 6397c09 'Prueba de Falla de incompatibilidad' y 715347d 'Volver a estado sin falla controlada' (2026-09-20), actualizados en 9334a03. | No verificado | No hay run en rojo ni el contenido del archivo; queda como pregunta de sustentación si la prueba realmente falló. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0004-estrategia-de-integracion.md: estado Aceptado, tres alternativas con ventajas y consecuencias, y escenario E2 de mantenibilidad con el acoplamiento descartado. | Cumple | Decide estrategia híbrida (consultas síncronas HTTP/JSON y actualización asíncrona con MySQL). |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42_6_Vista_Ejecucion.md existe en el árbol de 9334a03, pero su contenido no se aporta. | No verificado | Se esperaban los flujos de interacción descritos; la evidencia entregada llega truncada. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/contenedores.md existe en el árbol de 9334a03, pero su contenido no se aporta. | No verificado | Se esperaba el diagrama de contenedores con cada flecha etiquetada con protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio visible AS_202620_Drift en la organización ISCOUTB; el historial consolidado da 4 cuentas (JerryDBM/Sherry, JoshuaR01/JoshXX, lmpdiaz12 y maufern4ndez) y los 4 integrantes declarados aparecen en él. | Cumple | Consolidación por correo registrado idéntico entre alias, sin atribuir cuentas por parecido de nombre. |
| Estructura mínima | En 9334a03 existen docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | arc42 sin las secciones 7 ni 11 y con prefijo arc42_N_ en los nombres: desviación de forma, no ausencia del artefacto. |
| Estado del repositorio calificado | Rama origin/master, commit 9334a03 del 2026-09-20T20:19:47-05:00, anterior al cierre 2026-09-21T05:00:00Z; commits_tardios_post_cierre vacío. | Cumple | Único hash revisado, sin mezcla con otras ramas. |
| Convenciones de ADR | docs/adr/0001..0004 numerados en kebab-case, con contexto, opciones, decisión y consecuencias; 0001 marcado 'Reemplazado por ADR-0002' con enlace. | Cumple | 0003 y 0004 no enlazan commit o PR de implementación ('pendiente'), trazabilidad parcial. |
| Tabla de aspectos | docs/aspectos.md existe en el árbol de 9334a03, pero su contenido no se aporta. | No verificado | Se esperaba la tabla con las ocho columnas ID · Aspecto · Requisito · C4 · ADR · Código · Pruebas · Evidencia. |
| Registro de uso de IA | docs/ia.md con 29 entradas de git log entre 2026-08-09 y 2026-09-20 (última 0129608), es decir, crece a lo largo del semestre. | Cumple | No se aporta el contenido; no se pudo comprobar la columna de lo rechazado y su motivo. |
| README | README.md declara qué es el sistema, requisitos previos (Python 3.12, Node 22), arranque con un solo comando (python scripts/start.py) y cómo se prueba (pytest, npm run build, k6). | Cumple | No remite a pasos manuales no documentados. |
| Pipeline y análisis estático | sonar-project.properties existe en 9334a03 y el README describe el escaneo dentro de .github/workflows/ci.yml, pero no hay runs_ci ni URL pública del análisis. | No verificado | Se esperaba la línea del workflow que invoca el scanner, la URL del run exitoso y la URL pública con Quality Gate; comando anotado: curl -s https://api.github.com/repos/ISCOUTB/AS_202620_Drift/actions/runs. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `9334a03f97fc2ddb67846b8e6d229ff85898f3f1 2026-09-20T20:19:47-05:00 Update cambio_incompatible_evidencia.md`
- **Veredicto**: al dia
- Resumen: En la punta de origin/master (9334a03, 2026-09-20, antes del cierre) el proyecto tiene contratos ejecutables, ADR-0004 ligado a E2, estructura, README, registro de IA y ausencia de secretos; sin embargo no hay runs_ci ni URL pública de SonarCloud y la evidencia llega truncada, por lo que el pipeline, la ejecución y el fallo controlado de la prueba de contrato, arc42-6, C4-2, aspectos.md y la correspondencia contrato-código no se pudieron verificar.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Ninguno: commits_tardios_post_cierre está vacío y el último commit (9334a03) es anterior al cierre; los ajustes de contrato y su evidencia se registraron el 2026-09-20.

Pendientes que siguen abiertos:
- Aportar la línea de ci.yml que ejecuta la prueba de contrato y la URL del run.
- Aportar el registro del cambio incompatible que hizo fallar la prueba, o un run en rojo.
- Aportar la URL pública de SonarCloud con Quality Gate y el run que invocó el scanner.
- Completar la evidencia de correspondencia contrato-código (main.py frente a openapi.yaml).
- Aportar el contenido de arc42 sección 6, C4 de contenedores y docs/aspectos.md.

## Recuento y nota sugerida

5 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.0 = 1 + 4 × (5/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correspondencia contrato-código: falta el contenido de backend/app/main.py y de backend/tests/test_contract.py.
- Ejecución de la prueba de contrato en el pipeline: falta la línea de .github/workflows/ci.yml y la URL del run.
- Fallo controlado de la prueba: falta el contenido de docs/evidencias/cambio_incompatible_evidencia.md o un run en rojo.
- arc42 sección 6: falta el contenido de docs/arc42/arc42_6_Vista_Ejecucion.md.
- C4 nivel 2: falta el contenido de docs/c4/contenedores.md con las flechas etiquetadas.
- SonarCloud: faltan la línea del scanner en el workflow y las URL del run y del análisis con Quality Gate.
- Tabla de aspectos: falta el contenido de docs/aspectos.md con las ocho columnas.
- El extracto del contrato aportado se corta en la sección 2.3 y no muestra un apartado 11 con 8 criterios; la matriz transversal se armó con los criterios visibles (secciones 1 a 9).

## Hallazgos para la planilla

- Contrato OpenAPI 3.1 del backend y contratos OpenAPI/AsyncAPI de PlayStation versionados y con esquemas de datos.
- La evidencia entregada está truncada: faltan main.py, test_contract.py, ci.yml, aspectos.md, arc42-6 y c4/contenedores.md.
- No hay runs_ci: ni ejecución del pipeline ni URL pública de SonarCloud con Quality Gate.
- Los commits 6397c09 y 715347d sugieren el cambio incompatible y su reversión, pero no se aporta el registro del fallo.
- Sin secretos ni .env versionados en el árbol revisado.
- Los cuatro integrantes declarados aparecen en el historial tras consolidar cuentas duplicadas.
- El ADR-0004 liga la estrategia de integración al escenario E2 con la alternativa descartada.
