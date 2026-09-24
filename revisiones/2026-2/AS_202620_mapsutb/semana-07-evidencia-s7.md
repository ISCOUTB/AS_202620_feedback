# Evidencia S7 · mapsutb

> Auditoría local definitiva del informe automático. Se corrigieron discrepancias materiales al leer el código, el workflow y la única consulta permitida de `actions/runs`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `5e2fdd5` en `origin/master` (2026-09-20T21:15:28-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | `docs/api/apis-externas.openapi.yaml:1-25` declara OpenAPI 3.0.3 y comienza las rutas de las APIs externas. | Cumple | Contrato de consumidor versionado. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | `docs/api/apis-externas.openapi.yaml:25-180` cubre Geocoding, Static Maps y Measurement Protocol con parámetros, respuestas y esquemas. | Cumple | Incluye tipos, campos requeridos y estructuras de respuesta. |
| Correspondencia entre el contrato y la API implementada | `lib/adapters/geocoding_adapter.dart:27`, `static_map_adapter.dart:32` y `analytics_adapter.dart:37` usan exactamente `/maps/api/geocode/json`, `/maps/api/staticmap` y `/mp/collect`, las tres rutas del OpenAPI. | Cumple | También se comprobó que no hay otra ruta HTTP en esos adaptadores fuera del contrato. |
| Versión de la API declarada y con historial | `info.version` es `1.0.0`; el contrato se creó en `080c058` (2026-09-20T20:41:35-05:00). | Cumple | Versión e historial verificables. |
| Prueba de contrato presente | `test/geocoding_adapter_contract_test.dart`, `test/static_map_adapter_contract_test.dart` y `test/analytics_adapter_contract_test.dart`. | Cumple | Las pruebas usan `MockClient` y verifican rutas, formatos y degradación sin red real. |
| El pipeline ejecuta la prueba de contrato | `.github/workflows/ci.yml:27-29` ejecuta `flutter test --coverage`, que descubre los tres archivos `*_contract_test.dart`; run de `5e2fdd5` en `master`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/35553589365 | Cumple | El run corresponde al hash calificado. |
| Evidencia de que la prueba falla ante un cambio incompatible | `2f8f9ea` introdujo de forma deliberada un cambio incompatible y su run falló: https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/35553376615. `5e2fdd5` revirtió ese cambio y volvió a verde. | Cumple | Secuencia roja y reversión verificables. |
| ADR de la estrategia de integración ligado a un escenario | `docs/adr/0005-integracion-apis-externas.md:39-133` compara integración síncrona con eventos, adopta request/response y la liga al Escenario 3 de disponibilidad. | Cumple | Incluye alternativa descartada y consecuencias de acoplamiento. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/06_runtime_view.md` documenta trazar ruta, geocodificar, registrar analítica y pérdida de disponibilidad con diagramas de secuencia. | Cumple | Cubre éxito y degradación. |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/arc42/05_building_block_view.md` y `docs/c4/C2.md` etiquetan HTTPS/JSON, HTTPS/PNG, Dart/objetos y SDK nativo. | Cumple | La evidencia está duplicada entre arc42 y C4, pero es verificable. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon sin autenticación de `ISCOUTB/AS_202620_mapsutb`. | Cumple | — |
| Estructura mínima presente | En `5e2fdd5` existen las seis rutas mínimas del contrato. | Cumple | arc42 mezcla `.adoc` y `.md`, pero la estructura está presente. |
| Estado calificado identificable | `origin/master`, `5e2fdd594ced94f748cd50962fe8bfc71e8c2cf9`, 2026-09-20T21:15:28-05:00. | Cumple | Último commit anterior o igual al cierre. |
| Nombres de ADR según la convención | Cinco ADR `0001-...md` a `0005-...md` en kebab-case. | Cumple | — |
| ADR aceptados no reescritos | `docs/adr/0001-patrones-de-diseno.md` registra múltiples reescrituras entre el 23 de agosto y el 11 de septiembre sin ADR de reemplazo. | No cumple | El historial aceptado no se preservó de forma inmutable. |
| `docs/ia.md` al día para la semana | Último cambio `3d4b0c9` del 2026-08-30. | No cumple | No hay entrada del trabajo S7 ni sus rechazos técnicos. |
| Pipeline, SonarCloud y Quality Gate públicos | El CI de `5e2fdd5` está verde, pero ese workflow no ejecuta scanner; `sonar-project.properties` y el sincronizador de issues no prueban análisis ni Quality Gate. | No cumple | Falta URL pública del análisis y run del scanner. |
| Sin credenciales en el repositorio ni en el historial | Barrido de patrones y `.env` versionados sin coincidencias materiales. | Cumple | Las claves de prueba son literales `test-key`, no secretos. |
| Contribución de todos los integrantes | `shortlog` consolidado muestra cuatro personas; se unificaron los alias `charly`/`charlygz21` e `i-matallana` con dos correos. | Cumple | Coincide en cantidad con los cuatro integrantes declarados. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `7048021965cf483d29ef199c57d50a914953ac55` (2026-09-22T10:10:19-05:00).
- Después del cierre se agregó una invocación explícita de las pruebas de contrato y SonarCloud al CI (`23637a3`), además del ADR 0006 y el mapa de contextos.
- El run de `23637a3` fue exitoso, pero el run más reciente de la punta `7048021` falló: https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/35745455578. Es una corrección tardía y no cambia la matriz S7.
- Continúan abiertas la reescritura del ADR 0001 y la falta de registro de IA actualizado.

## Recuento y nota sugerida

**10 de 10 criterios Cumple.**

**Nota sugerida (propuesta al docente, publicada por decisión del profesor): 5.0 = 1 + 4 × (10/10).** La nota final la fija el profesor en Moodle.

## No conformidades y pendientes

- Preservar los ADR aceptados y registrar cambios mediante ADR de reemplazo.
- Actualizar `docs/ia.md` con el trabajo S7, lo rechazado y su motivo técnico.
- Restablecer el CI de la punta y publicar el análisis SonarCloud con su Quality Gate.

## Hallazgos para la planilla

- La auditoría corrige el S7 automático de 7/10 a 10/10: correspondencia, ejecución en CI y prueba roja sí eran verificables.
- Las no conformidades transversales no cambian el recuento de la ficha.
