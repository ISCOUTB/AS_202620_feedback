# semana-07-evidencia-s7 · AudioShare

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `0ada095` en `origin/master` (2026-09-20T23:57:20-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/contracts/openapi.yaml y docs/contracts/asyncapi.yaml presentes en el árbol de 0ada095 (2026-09-20T23:57:20-05:00). | Cumple | ADR-0002 los declara OpenAPI 3.1 y AsyncAPI 3.0, pero el volcado no incluye su contenido. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No se aportó el contenido de docs/contracts/openapi.yaml ni de docs/contracts/asyncapi.yaml en el hash 0ada095. | No verificado | Haría falta citar fragmento con openapi:, paths: y components.schemas (o channels y components.messages). |
| Correspondencia entre el contrato y la API implementada | No se incluyó src/app.ts ni el YAML de contratos en la evidencia del hash 0ada095. | No verificado | ADR-0002 menciona /rooms, /rooms/:roomId, /rooms/:roomId/receivers y /rooms/:roomId/play, pero es afirmación documental; falta contrastar con el código y con el contrato. |
| Versión de la API declarada y con historial | No se citó el campo de versión del contrato ni la salida de git log sobre docs/contracts/. | No verificado | Comando pendiente: git -C $DIR log --format='%h %cI %s' -- docs/contracts/openapi.yaml. |
| Prueba de contrato presente | tests/contract.test.ts figura en el árbol de 0ada095 y ADR-0002 lo cita como la prueba que falla ante cambio incompatible. | Cumple | No se aportó el contenido del archivo de prueba. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml existe en el árbol de 0ada095, pero no hay runs_ci ni contenido del workflow en la evidencia. | No verificado | Comando pendiente: grep -rniE 'contract\|schemathesis\|pact\|openapi' .github/workflows/ más la URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | No hay run en rojo ni evidencia aportada por el equipo en la entrega S7. | No verificado | Comando pendiente: consulta a actions/runs filtrando conclusion distinta de success; queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0002-estrategia-integracion.md descarta «Todo síncrono» y «Todo asíncrono» y adopta el híbrido ligado a EC-01, EC-03 y EC-04. | Cumple | Expone el acoplamiento temporal de cada alternativa y sus consecuencias. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/src/06_runtime_view.adoc describe creación de sala, incorporación de receptor, transmisión de audio y pausa/reanudación con diagramas de secuencia en texto. | Cumple | Los flujos nombran módulos «Salas, Sesiones, Moderación» que no coinciden con session, audio y sync del código. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/C4 Nivel 2 - Contenedores.mmd etiqueta las flechas internas como [JSON / HTTPS REST], [NDJSON / HTTP streaming] y [SQL / better-sqlite3]. | Cumple | Las dos flechas persona hacia cliente solo indican [HTTPS] sin formato y el diagrama aún muestra cliente web mientras ADR-0003 migra a Flutter. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | AS_202620_AudioShare en la organización ISCOUTB, visible: true, con 4 identidades de commit frente a 4 integrantes declarados. | Cumple | La cuenta cardonavincent26-design no se atribuye a ningún integrante por parecido de nombre; requiere confirmación del equipo. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md presentes en el árbol de 0ada095. | Cumple | arc42 está en .adoc en vez de Markdown y el template incluye src/07 y src/11, que no existen en el árbol. |
| Estado del repositorio calificado | origin/master, hash 0ada095, 2026-09-20T23:57:20-05:00, anterior al cierre de la actividad. | Cumple | Hay 8 commits posteriores al cierre que no se califican aquí y se registran en overall. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md contiene marcadores de conflicto de fusión sin resolver en el hash 0ada095 (<<<<<<< HEAD y >>>>>>> be5a6af). | No cumple | Además ese ADR aceptado fue editado después (commit post-cierre 354f1f5 «Update ADR 0001»). |
| Tabla de aspectos | docs/aspectos.md usa columnas ID, Aspecto, Escenario, Objetivo, Requisito, ADR, C4, Implementación y Pruebas, sin la columna Evidencia exigida. | No cumple | Incluye una segunda matriz de trazabilidad con encabezado y columnas distintas que duplican el contenido. |
| Registro de uso de IA | docs/ia.md existe y acumula 13 commits entre 2026-08-09 y 2026-09-20, pero el volcado no incluye su contenido. | No verificado | Falta poder citar la columna de lo rechazado y su motivo técnico. |
| README | README.md describe el sistema, el arranque con npm run dev y las pruebas (flutter test, npm test). | Cumple | Conserva marcadores de conflicto de fusión sin resolver y enlaza a docs/adr/0002-cliente-flutter-backend-modular.md, que no existe. |
| Pipeline, análisis estático y secretos | sonar-project.properties y los workflows ci.yml y flutter.yml están en el árbol; sin coincidencias de secretos ni .env versionado (solo .env.example). | No verificado | Faltan la línea del workflow que invoca el scanner, la URL del run exitoso y la URL pública del análisis en SonarCloud con Quality Gate. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `d094a5166d0af4067bfc717e4170e660aacacab1 2026-09-21T00:21:38-05:00 Update architectural decision references in documentation`
- **Veredicto**: con pendientes
- Resumen: En la punta de origin/master hay entregables reales de la semana 7 (contratos OpenAPI y AsyncAPI, tests/contract.test.ts, ADR-0002 ligado a escenarios, arc42 sección 6 y C4 nivel 2 con protocolos), pero la verificación clave no es posible: el volcado no incluye el contenido de los contratos ni de src/app.ts, no hay runs_ci citados y no hay URL pública de SonarCloud, y en el commit calificado persisten no conformidades en ADR-0001 y docs/aspectos.md.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Ocho commits posteriores al cierre 2026-09-21T05:00:00Z (=00:00-05:00): 900b3e8 (00:04:54), 628c8be (00:07:23), d01e743 (00:09:48), 354f1f5 (00:15:12), eab5775 (00:18:45), 5c72af6 (00:19:45), b83471f (00:20:25) y d094a51 (00:21:38), todos en origin/master.

Pendientes que siguen abiertos:
- Evidencia de que la prueba de contrato falla ante un cambio incompatible (run en rojo o registro del cambio).
- Línea del workflow que ejecuta la prueba de contrato y URL del run de CI.
- Evidencia pública de SonarCloud: invocación del scanner, run exitoso y Quality Gate.
- Correspondencia verificable entre rutas del contrato y rutas implementadas en el código.
- Columna Evidencia en docs/aspectos.md y limpieza de la matriz duplicada.
- Marcadores de conflicto de fusión en README y ADR-0001 y enlaces a ADR inexistentes.
- Secciones 07 y 11 de arc42 ausentes y documentación arc42 en formato .adoc.
- Verificación del contenido de docs/ia.md (qué se rechazó y por qué).

## Recuento y nota sugerida

5 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.0 = 1 + 4 × (5/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de docs/contracts/openapi.yaml y docs/contracts/asyncapi.yaml: rutas y esquemas de datos; falta citar fragmentos del YAML en 0ada095.
- Correspondencia contrato-API: faltan dos rutas del contrato localizadas en src/app.ts y una ruta del código presente en el contrato.
- Versión de la API y su historial: falta el campo de versión y la salida de git log del archivo de contrato.
- Ejecución de la prueba de contrato en el pipeline: faltan la línea del workflow y la URL del run (comando: grep -rniE 'contract|openapi' .github/workflows/).
- Run en rojo o evidencia del cambio incompatible que hizo fallar la prueba de contrato.
- SonarCloud auditable: configuración presente, pero sin URL de run exitoso ni URL pública del análisis con Quality Gate.
- Contenido de docs/ia.md: no se puede verificar qué se rechazó y por qué.

## Hallazgos para la planilla

- README.md y docs/adr/0001 quedaron con marcadores de conflicto de fusión sin resolver en el commit calificado 0ada095.
- README y arc42/09 enlazan a docs/adr/0002-cliente-flutter-backend-modular.md, ruta que no existe en el repositorio.
- docs/aspectos.md no tiene columna Evidencia y repite dos matrices de trazabilidad con columnas distintas.
- No hay runs de CI citados ni URL pública de SonarCloud; solo se ve el archivo de configuración del análisis.
- Sin coincidencias de secretos ni archivos .env versionados; únicamente .env.example.
- Ocho commits posteriores al cierre tocan README, ADR-0001, escenarios de calidad, C4 Nivel 1 y borran docs/arc42/src/08_crosscutting_concepts.adoc.
- docs/arc42 está en .adoc y el template referencia src/07 y src/11, ausentes del árbol.
- Los flujos de la sección 6 nombran módulos que no coinciden con session, audio y sync del código.
- Commits posteriores al cierre (no calificados): d094a51 2026-09-21T00:21:38-05:00 Update architectural decision references in documentation; b83471f 2026-09-21T00:20:25-05:00 Update integration strategy and add Flutter client concepts; 5c72af6 2026-09-21T00:19:45-05:00 Delete docs/arc42/src/08_crosscutting_concepts.adoc; eab5775 2026-09-21T00:18:45-05:00 Update escenarios de calidad; 354f1f5 2026-09-21T00:15:12-05:00 Update ADR 0001
