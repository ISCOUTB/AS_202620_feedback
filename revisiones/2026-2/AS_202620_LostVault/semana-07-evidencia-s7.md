# semana-07-evidencia-s7 · LostVault

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `7bf515f` en `origin/main` (2026-09-20T23:55:34-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/contracts/lostvault-api.yaml en el árbol de 7bf515f, con `openapi: 3.1.1`. | Cumple | Archivo YAML versionado en el repositorio, no prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | `paths:/v1/objects/{objectId}/claims` con `components.schemas.Claim` (objectId, userId, verified) y `Problem` (code con enum y message). | Cumple | Define esquemas de éxito y de error con $ref; el ejemplo 201 incluye datos. |
| Correspondencia entre el contrato y la API implementada | El contrato declara una sola ruta HTTP; en `lib/` solo hay adaptadores in-memory (in_memory_claim_service.dart, claim_object_use_case.dart) y el README declara que la prueba no requiere servidor remoto. | No cumple | No hay dos rutas del contrato localizables en el código ni ruta de código en el contrato: la frontera HTTP aún no existe. |
| Versión de la API declarada y con historial | `info.version: 1.0.0` en `docs/contracts/lostvault-api.yaml`; `git log` registra su creación en `f28f9eb` (2026-09-20T23:23:36-05:00). | Cumple | La versión y el contrato están bajo control de versiones. |
| Prueba de contrato presente | test/api_contract_test.dart en el árbol de 7bf515f. | Cumple | El README y docs/ia.md describen que exige operación, autenticación, campos y errores. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/flutter.yml, paso «Verify API consumer contract» → `flutter test test/api_contract_test.dart`; run Flutter checks success https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/35562739730 (2026-09-21T04:57:04Z). | Cumple | La prueba se invoca explícitamente además de `flutter test`. |
| Evidencia de que la prueba falla ante un cambio incompatible | Runs revisados: el único fallo es del workflow «Build» (run 35562739717, 2026-09-21T04:57:04Z), ajeno a la prueba de contrato; ningún run de «Flutter checks» aparece en rojo. | No verificado | No hay run en rojo de la prueba ni evidencia aportada del cambio incompatible; queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0002-integracion-reclamacion-api.md: decisión HTTP/JSON síncrona, alternativa de evento asíncrono descartada y costos de acoplamiento, ligada al flujo de reclamación y a 06_vista_runtime.md. | Cumple | docs/arc42/09_decisiones.md todavía solo lista el ADR 0001. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06_vista_runtime.md con pasos numerados y diagrama de secuencia UI → ClaimObjectUseCase → authentication/objects/identity_verification → ClaimService. | Cumple | Incluye caminos alternos de fallo y limitación del adaptador in-memory. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/C4 nivel 2.jpg existe en el árbol, pero es binario y no permite comprobar el etiquetado de las flechas; no hay versión .mmd del nivel 2. | No verificado | Haría falta el diagrama como código o su contenido citado para verificar protocolo y formato por flecha. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | AS_202620_LostVault en la organización ISCOUTB, visible: true; las cuatro cuentas declaradas aparecen en el historial. | Cumple | Tras consolidar por correo compartido quedan 5 cuentas: Roy Gonzalez, Fausto-4/Jose Faustino España, weller-rar/Weller, shamarallorente-blip y Shamara Llorente Tapias; las dos últimas no se consolidan por parecido de nombre. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md presentes en 7bf515f. | Cumple | arc42 solo trae secciones 1-6, 9, 10 y glosario; el C4 nivel 2 está como .jpg dentro de docs/c4/. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md y docs/adr/0002-integracion-reclamacion-api.md cumplen el patrón NNNN-kebab-case; el 0002 trae contexto, decisión, alternativa y consecuencias. | Cumple | docs/arc42/09_decisiones.md no incluye el ADR 0002 en su tabla. |
| La tabla de aspectos | docs/aspectos.md usa columnas propias sin columna C4, y las filas AS-01, AS-02 y AS-04 tienen celdas «Pendiente de…» en implementación y pruebas. | No cumple | Solo AS-03 tiene la cadena navegable; falta el eslabón C4 exigido por el contrato. |
| Registro de uso de IA | docs/ia.md con registros S1, S2, S3 y S7, cada uno con lo aceptado y lo rechazado con motivo técnico; historial de commits 2026-08-24 y 2026-09-20. | Cumple | El registro rechaza explícitamente afirmar una API remota inexistente. |
| README | README.md describe el sistema, requisitos previos, `flutter pub get`, `flutter run -d chrome` y `flutter test`. | Cumple | Incluye recorrido manual esperado del corte vertical. |
| Pipeline y análisis estático | `.github/workflows/build.yml` invoca SonarSource/sonarqube-scan-action con SONAR_TOKEN y existe `sonar-project.properties`; el run «Build» del hash calificado terminó en verde: https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/35562671796. | No cumple | Falta la URL pública del análisis en SonarCloud con el estado del Quality Gate para completar la evidencia transversal. |
| Secretos | Búsqueda de patrones de credenciales y claves sin coincidencias; `envs_versionados` vacío. | Cumple | No se encontró ningún secreto ni .env versionado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `7bf515ff4d69a386a296124f3719c31f783f9970 2026-09-20T23:55:34-05:00 Merge pull request #10 from Fausto-4/main`
- **Veredicto**: con pendientes
- Resumen: En la punta actual de origin/main (7bf515f, 2026-09-20T23:55:34-05:00) existen el contrato ejecutable, la prueba de contrato en el pipeline y el ADR de integración, pero la correspondencia contrato–código no se sostiene, no hay evidencia de que la prueba falle y falta la evidencia pública de SonarCloud con Quality Gate; no hay commits posteriores al cierre ni diferencias con el estado calificado.

Pendientes que siguen abiertos:
- Correspondencia entre el contrato y una API implementada (o aclaración explícita de que la frontera HTTP aún no existe).
- Evidencia de ejecución de la prueba de contrato en rojo ante un cambio incompatible.
- URL pública del análisis en SonarCloud con Quality Gate para el hash revisado.
- C4 nivel 2 revisable (como código) con protocolo y formato en cada flecha.
- Columna C4 y celdas completas en docs/aspectos.md para todas las filas.
- Historial git del contrato y actualización de docs/arc42/09_decisiones.md con el ADR 0002.

## Recuento y nota sugerida

7 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Fallo de la prueba de contrato ante un cambio incompatible: no hay run en rojo ni evidencia aportada; requiere un PR con cambio incompatible y el run fallido.
- Etiquetado de protocolo y formato en cada flecha del C4 nivel 2: el archivo es binario; requiere el diagrama como código o su contenido citado.
- URL pública del análisis en SonarCloud para el hash 7bf515f con Quality Gate: no aportada en la evidencia.

## Hallazgos para la planilla

- El contrato OpenAPI declara una frontera HTTP que el código no implementa: solo hay adaptadores in-memory.
- El contrato tiene una sola ruta, sin segunda ruta para contrastar contra el código.
- Ningún run de la prueba de contrato aparece en rojo, así que no se demuestra que pueda fallar.
- El C4 nivel 2 está solo como .jpg, no verificable como diagrama etiquetado.
- Falta la URL pública de SonarCloud con el estado del Quality Gate.
- El run «Build» del hash calificado terminó en verde; falta el análisis público de SonarCloud con Quality Gate.
- docs/arc42/09_decisiones.md no lista el ADR 0002 ya aceptado.
- La tabla de aspectos no tiene columna C4 y tres filas siguen con celdas pendientes.
- La última subida al repositorio ocurrió minutos antes del cierre, dentro del plazo.
