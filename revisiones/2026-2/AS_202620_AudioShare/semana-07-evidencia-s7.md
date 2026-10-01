# semana-07-evidencia-s7 · AudioShare

> Revisión auditada localmente sobre el hash calificado 0ada095; se leyeron en el repositorio las filas que la pasada automática había dejado como No verificado.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `0ada095` en `origin/master` (2026-09-20T23:57:20-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/contracts/openapi.yaml y docs/contracts/asyncapi.yaml presentes en el árbol de 0ada095 (2026-09-20T23:57:20-05:00). | Cumple | Son contratos ejecutables en YAML; OpenAPI 3.1.0 y AsyncAPI 3.0.0 declarados en los propios archivos. El detalle de rutas y esquemas se cita en la fila siguiente. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/contracts/openapi.yaml:1 `openapi: 3.1.0` con rutas /health, /rooms, /rooms/{roomId}, /rooms/{roomId}/receivers, /rooms/{roomId}/play, /rooms/{roomId}/pause y /rooms/{roomId}/audio, y components.schemas (RoomState, PlayResponse, PauseResponse, AudioChunk, ErrorResponse, entre otros); docs/contracts/asyncapi.yaml:1 `asyncapi: 3.0.0` con channels (address /rooms/{roomId}/stream/{receiverId}) y components.messages (SyncStart, SyncPause, AudioChunk) en 0ada095. | Cumple | Ambos contratos declaran esquemas de datos de entrada y salida, no solo un listado de endpoints. |
| Correspondencia entre el contrato y la API implementada | Dos rutas del contrato en el código: src/app.ts:70 `app.post("/rooms"` y src/app.ts:172 `app.post("/rooms/:roomId/play"` coinciden con /rooms y /rooms/{roomId}/play. Una ruta del código en el contrato: src/app.ts:114 `app.get("/rooms/:roomId/stream/:receiverId"` corresponde al channel roomStream de docs/contracts/asyncapi.yaml:18 (address /rooms/{roomId}/stream/{receiverId}). También src/app.ts:285 (GET /rooms/:roomId) y src/app.ts:313 (GET /health) están en el contrato, en 0ada095. | Cumple | Correspondencia verificada en ambos sentidos; ADR-0002 anticipaba las mismas rutas. |
| Versión de la API declarada y con historial | docs/contracts/openapi.yaml:9 `version: 0.1.0` (y docs/contracts/asyncapi.yaml:4 `version: 0.1.0`); `git log --format='%h %cI %s' -- docs/contracts/openapi.yaml` muestra f5c46a1 2026-09-20T01:54:39-05:00 "contrato OpenAPI/AsyncAPI" en 0ada095. | Cumple | La versión está declarada en ambos contratos y el archivo está versionado en git. |
| Prueba de contrato presente | tests/contract.test.ts figura en el árbol de 0ada095 y ADR-0002 lo cita como la prueba que falla ante cambio incompatible. | Cumple | El archivo está presente y valida las respuestas reales contra los esquemas del OpenAPI; el pipeline lo ejecuta vía `npm run verify`. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml:19 ejecuta `npm run verify`; package.json:12 define `verify` como `npm run build && npm test` y package.json:11 define `test` como `vitest run`, que ejecuta tests/contract.test.ts. Run de CI en verde corroborado sin autenticar: https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/35564301065 (CI, success). | Cumple | flutter.yml es un workflow aparte para el cliente Flutter y no invoca la prueba de contrato; la prueba corre por `npm run verify`. |
| Evidencia de que la prueba falla ante un cambio incompatible | No hay run en rojo de la prueba de contrato ni evidencia aportada por el equipo en la entrega S7. | No verificado | La API sin autenticar no registra runs en rojo de la prueba de contrato (los fallos observados corresponden al workflow Flutter); no hay registro del cambio incompatible aportado por el equipo. Queda como pregunta de sustentación. |
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
| Registro de uso de IA | docs/ia.md en 0ada095 incluye la tabla «Registro del uso de IA» con la columna «Propuesta de IA rechazada y motivo» y una sección «Propuestas de IA rechazadas» con motivos técnicos (p. ej. Semana 4: «Se rechazó mantener el estado únicamente en memoria…»; Semana 7: «Se rechazaron propuestas que trasladaban directamente la estructura del proyecto web…»). `git log -- docs/ia.md` registra 5a6d73b 2026-09-20T23:24:35-05:00 "Update ia.md" dentro del periodo revisado. | Cumple | El registro está al día para la semana y documenta lo rechazado con su motivo técnico. |
| README | README.md describe el sistema, el arranque con npm run dev y las pruebas (flutter test, npm test). | Cumple | Conserva marcadores de conflicto de fusión sin resolver y enlaza a docs/adr/0002-cliente-flutter-backend-modular.md, que no existe. |
| Pipeline, análisis estático y secretos | .github/workflows/ci.yml:20 invoca el paso «SonarCloud Scan» (SonarSource/sonarqube-scan-action) con SONAR_TOKEN; sonar-project.properties define sonar.projectKey=AS_202620_AudioShare y sonar.organization=cardonavincent26. Sin coincidencias de secretos ni .env versionado (solo .env.example). | Cumple | El scanner se invoca en el workflow y la configuración está versionada; la API sin autenticar muestra runs de CI exitosos (p. ej. https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/35564301065, CI success). La URL pública del análisis en SonarCloud y su Quality Gate son evidencia externa que esta auditoría no abrió: queda como corroboración pendiente, no como ausencia del artefacto. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `e4789d887fe59b2ace65bd1d2680f79758db5b54 2026-09-27T23:49:01-05:00 S8: URL desplegada en Azure, evidencia de health y restricciones de la suscripción`
- **Veredicto**: con pendientes
- Resumen: leído el contenido en el hash calificado, el proyecto sostiene 9 de 10 criterios de ficha y las filas transversales de IA y pipeline: los contratos OpenAPI 3.1 y AsyncAPI 3.0 traen rutas y esquemas, corresponden con src/app.ts, están versionados y su prueba de contrato se ejecuta en el pipeline. Queda en No verificado únicamente la evidencia de que la prueba falle ante un cambio incompatible (no hay run en rojo ni registro del equipo), y en el commit calificado persisten no conformidades en ADR-0001 y docs/aspectos.md. La punta actual ya incluye trabajo de S8.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Ocho commits posteriores al cierre 2026-09-21T05:00:00Z (=00:00-05:00): 900b3e8 (00:04:54), 628c8be (00:07:23), d01e743 (00:09:48), 354f1f5 (00:15:12), eab5775 (00:18:45), 5c72af6 (00:19:45), b83471f (00:20:25) y d094a51 (00:21:38), todos en origin/master.

Pendientes que siguen abiertos:
- Evidencia de que la prueba de contrato falla ante un cambio incompatible (run en rojo o registro del cambio): no aparece ninguna de las dos.
- URL pública del análisis en SonarCloud y su Quality Gate: la invocación del scanner y la configuración ya se leyeron en el repositorio; falta abrir el análisis público.
- Columna Evidencia en docs/aspectos.md y limpieza de la matriz duplicada.
- Marcadores de conflicto de fusión en README y ADR-0001 y enlaces a ADR inexistentes.
- Secciones 07 y 11 de arc42 ausentes y documentación arc42 en formato .adoc.

## Recuento y nota sugerida

9 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.6 = 1 + 4 × (9/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Run en rojo o evidencia del cambio incompatible que hizo fallar la prueba de contrato: no se aportó ninguna; queda como pregunta de sustentación.
- SonarCloud: la invocación del scanner y la configuración están en el repositorio; la URL pública del análisis y su Quality Gate son evidencia externa no abierta por esta auditoría.

## Hallazgos para la planilla

- README.md y docs/adr/0001 quedaron con marcadores de conflicto de fusión sin resolver en el commit calificado 0ada095.
- README y arc42/09 enlazan a docs/adr/0002-cliente-flutter-backend-modular.md, ruta que no existe en el repositorio.
- docs/aspectos.md no tiene columna Evidencia y repite dos matrices de trazabilidad con columnas distintas.
- La invocación del scanner de SonarCloud está en ci.yml y la configuración en sonar-project.properties; falta la URL pública del análisis con su Quality Gate.
- Sin coincidencias de secretos ni archivos .env versionados; únicamente .env.example.
- Ocho commits posteriores al cierre tocan README, ADR-0001, escenarios de calidad, C4 Nivel 1 y borran docs/arc42/src/08_crosscutting_concepts.adoc.
- docs/arc42 está en .adoc y el template referencia src/07 y src/11, ausentes del árbol.
- Los flujos de la sección 6 nombran módulos que no coinciden con session, audio y sync del código.
- Commits posteriores al cierre (no calificados): d094a51 2026-09-21T00:21:38-05:00 Update architectural decision references in documentation; b83471f 2026-09-21T00:20:25-05:00 Update integration strategy and add Flutter client concepts; 5c72af6 2026-09-21T00:19:45-05:00 Delete docs/arc42/src/08_crosscutting_concepts.adoc; eab5775 2026-09-21T00:18:45-05:00 Update escenarios de calidad; 354f1f5 2026-09-21T00:15:12-05:00 Update ADR 0001
