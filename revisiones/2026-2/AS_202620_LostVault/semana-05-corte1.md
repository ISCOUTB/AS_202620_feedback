# semana-05-corte1 · LostVault

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `952af8f` en `origin/main` (2026-08-30T22:13:14-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/main, hash 952af8f, 2026-08-30T22:13:14-05:00, anterior al cierre 2026-09-07T05:00:00Z | Cumple | Rama principal main identificada y commit calificado anterior al cierre. |
| correcciones.md existe en la raíz del estado calificado | Árbol de 952af8f no incluye correcciones.md; incluye REVISION_CORREGIDA.md | No cumple | El archivo exigido no existe en la raíz del estado calificado. |
| Correcciones trazables y contrastadas | No hay correcciones.md en 952af8f; REVISION_CORREGIDA.md no es el archivo exigido | No cumple | No se puede contrastar trazabilidad de hallazgos S1-S4 sin el índice exigido. |
| S1 al día: equipo, problema y repositorio | docs/ficha_problema.md en 952af8f; README.md describe LostVault; integrantes en historial | Cumple | Problema, población y propuesta documentados; repositorio en ISCOUTB/AS_202620_LostVault. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/10_requisitos_calidad.md y docs/arc42/02_restricciones.md en 952af8f | Cumple | Cuatro escenarios medibles y restricciones técnicas, organizativas y legales documentadas. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-estilo-arquitectonico.md y docs/arc42/04_estilo_arquitectonico.md en 952af8f | Cumple | ADR 0001 con contexto, alternativas, consecuencias y trazabilidad; estrategia por escenario. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ secciones 01-06, 09, 10 y glosario; docs/c4/contexto.mmd, c4_contexto.png y C4 nivel 2.jpg; lib/features/claims/application/claim_object_use_case.dart en 952af8f | Cumple | Documentación arc42 presente, C4 con contexto y nivel 2, corte vertical AS-03 implementado. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta flutter run -d chrome y flutter test; lib/main.dart y claim_object_use_case.dart; test/claim_object_use_case_test.dart, test/widget_test.dart y test/architecture_structure_test.dart en 952af8f | Cumple | Corte AS-03 atraviesa UI, caso de uso, contratos públicos e infraestructura in-memory; pruebas automatizadas presentes. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/flutter.yml existe en 952af8f; runs_ci disponibles son posteriores al cierre (2026-09-07T20:51Z en adelante) | No verificado | No hay run de CI asociado al hash 952af8f o anterior al corte; se requiere run del commit calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md en 952af8f con fila AS-03 enlazada a escenario, ADR, código, pruebas y evidencia | Cumple | Cadena aspecto-requisito-C4-ADR-código-pruebas navegable para AS-03; otras filas marcan pendientes explícitos. |
| PDF u otro adjunto exigido por el aula | No hay adjunto en el repositorio; la entrega del PDF se hace en Moodle | No verificado | Se requiere el documento entregado en el aula para verificar. |
| Sustentación del corte | No hay evidencia de sesión de sustentación en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_LostVault visible; integrantes en shortlog: Roy Gonzalez, Fausto-4, shamarallorente-blip, Jose Faustino España, weller-rar, Shamara Llorente Tapias | Cumple | Nombre y organización correctos; identidades consolidadas por nombre visible. |
| Estructura mínima | README.md, docs/arc42/, docs/adr/0001-estilo-arquitectonico.md, docs/c4/, docs/aspectos.md y docs/ia.md en 952af8f | Cumple | Estructura mínima presente; se anota desviación menor: docs/c4/C4 nivel 2.jpg con espacios en el nombre. |
| Estado del repositorio que se califica | origin/main, hash 952af8f, fecha 2026-08-30T22:13:14-05:00, anterior al cierre 2026-09-07T05:00:00Z | Cumple | Commit calificado identificado; commits posteriores se registran en overall. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md en 952af8f; nombre cumple patrón NNNN-titulo-en-kebab-case.md; ADR con contexto, alternativas, consecuencias y trazabilidad | Cumple | Un ADR aceptado y no reescrito; cumple convención. |
| Tabla de aspectos | docs/aspectos.md en 952af8f con columnas ID, Aspecto, Prioridad, Justificación, Tensión, Escenario, Medida, Decisión, Implementación y Pruebas; fila AS-03 completa y navegable | Cumple | AS-03 trazable hasta pruebas; AS-01, AS-02 y AS-04 declaran pendientes explícitos. |
| Registro de uso de IA | docs/ia.md en 952af8f; último cambio edd78d7 2026-08-24T16:29:45-05:00; registra S1, S2, S3 con aceptado y rechazado | Cumple | Incluye herramienta, aceptación y rechazo con motivo técnico. |
| README | README.md en 952af8f documenta qué es, requisitos, flutter pub get, flutter run -d chrome, flutter analyze y flutter test | Cumple | Arranque con un comando y pruebas documentadas. |
| Pipeline y análisis estático | .github/workflows/flutter.yml en 952af8f ejecuta flutter analyze y flutter test; runs_ci disponibles son posteriores al cierre y no corresponden al hash calificado | No verificado | No hay evidencia de ejecución CI del commit 952af8f; se requiere run asociado al hash o anterior al corte. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `c0c17c1e9c3387ac915767cd706e8b785a3deadf 2026-09-07T16:46:16-05:00 Change build target from Windows to Web`
- **Veredicto**: con pendientes
- Resumen: El proyecto entero a HEAD conserva la documentación y el corte vertical de 952af8f; los cambios posteriores al cierre solo agregan build.yml y sonar-project.properties. Sigue pendiente correcciones.md y la evidencia de CI del commit calificado.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Se agregaron .github/workflows/build.yml y sonar-project.properties en commits posteriores al cierre (37eb409, 847adca, 6e48599, 5c3cf21, 5ed88e6, c0c17c1), sin resolver el pendiente de correcciones.md.

Pendientes que siguen abiertos:
- correcciones.md en la raíz del estado calificado.
- Run de CI asociado al hash calificado o anterior al corte.
- Cortes ejecutables y mediciones de AS-01, AS-02 y AS-04.

## Recuento y nota sugerida

7 de 12 criterios Cumple.

## No verificado / pendientes

- Pipeline y pruebas respaldan el estado calificado: falta run de CI del commit 952af8f o anterior al cierre.
- PDF u otro adjunto exigido por el aula: depende de Moodle.
- Sustentación del corte: depende de sesión docente.
- Pipeline y análisis estático (transversal): falta run de CI del commit calificado.

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado 952af8f.
- REVISION_CORREGIDA.md no sustituye al archivo exigido correcciones.md.
- No hay run de CI asociado al hash calificado 952af8f; los runs disponibles son posteriores al cierre.
- Commits posteriores al cierre agregan build.yml y sonar-project.properties sin afectar la matriz del corte.
- Nombre de archivo docs/c4/C4 nivel 2.jpg contiene espacios, desviación menor de estructura.
- AS-01, AS-02 y AS-04 quedan pendientes de corte ejecutable y medición, declarado en docs/aspectos.md.
- Commits posteriores al cierre (no calificados): c0c17c1 2026-09-07T16:46:16-05:00 Change build target from Windows to Web; 5ed88e6 2026-09-07T16:40:30-05:00 Update build.yml; 5c3cf21 2026-09-07T16:34:55-05:00 Refactor build workflow to remove Flutter setup; 6e48599 2026-09-07T16:10:53-05:00 Add Flutter setup and build steps to workflow; 847adca 2026-09-07T15:51:35-05:00 Add sonar-project.properties for SonarCloud configuration
