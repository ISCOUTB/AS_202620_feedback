# semana-07-evidencia-s7 · LostVault

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `9d57572` en `origin/main` (2026-09-13T22:11:29-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol de HEAD 9d57572 (2026-09-13): no aparece ningún .yaml/.json de openapi\|swagger\|asyncapi ni ningún .proto. | No cumple | Se buscó con el listado de árbol del commit calificado y no hay artefacto de contrato; solo documentación en Markdown y código Dart. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No existe archivo de contrato que citar en 9d57572; los únicos artefactos de interfaz son las carpetas public/ en Dart. | No cumple | Sin archivo de contrato no hay rutas ni esquemas que verificar. |
| Correspondencia entre el contrato y la API implementada | La API implementada es en proceso (lib/features/*/public/*.dart) y no hay contrato HTTP contra el que cotejar rutas en 9d57572. | No cumple | No se pudo tomar dos rutas del contrato ni una del código: el contrato no existe. |
| Versión de la API declarada y con historial | No hay campo de versión de API en 9d57572 ni archivo de contrato sobre el que correr git log. | No cumple | Se esperaba versión en el propio contrato o en su ruta, más historial de cambios del archivo. |
| Prueba de contrato presente | test/ en 9d57572 solo contiene architecture_structure_test.dart, claim_object_use_case_test.dart y widget_test.dart. | No cumple | Se buscó prueba de contrato tipo dredd/schemathesis/pact/prism y no hay archivo alguno. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/flutter.yml solo ejecuta flutter pub get, flutter analyze y flutter test; build.yml solo invoca el scanner. Runs verdes: https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/34801736898. | No cumple | No hay comando de contrato en ningún workflow; los runs exitosos corresponden a analyze/test y SonarQube, no a verificación de contrato. |
| Evidencia de que la prueba falla ante un cambio incompatible | Los 10 runs listados en runs_ci tienen conclusion success (p. ej. https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/34801736760). | No verificado | No hay run en rojo ni evidencia aportada del cambio incompatible; haría falta el run fallido o el commit/registro del cambio que rompe el contrato. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/ en 9d57572 solo contiene 0001-estilo-arquitectonico.md, sobre monolito modular; no hay ADR de integración síncrona o asíncrona. | No cumple | Se esperaba un ADR con escenario de calidad, alternativa descartada y consecuencias de acoplamiento. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06_vista_runtime.md (commit 9d57572, 2026-09-13) describe el flujo paso a paso de la reclamación y un diagrama de secuencia. | Cumple | El flujo cubre UI, caso de uso, contratos public/ y adaptadores in-memory. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/ contiene contexto.mmd (nivel 1) y C4 nivel 2.jpg (binario); no hay fuente revisable del nivel 2. | No verificado | No se puede comprobar el etiquetado de flechas en una imagen; haría falta el diagrama como código con protocolo y formato por flecha. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_LostVault, visible y público; autores consolidados en 9d57572: Roy Gonzalez, Fausto-4 / Jose Faustino España (misma cuenta de autoría), weller-rar / Weller, shamarallorente-blip / Shamara Llorente Tapias. | Cumple | Cuatro identidades distintas coinciden con los cuatro integrantes declarados; se consolidaron por cuenta de autoría, no por parecido de nombre. |
| Estructura mínima | Árbol de 9d57572: README.md, docs/adr/, docs/arc42/, docs/c4/, docs/aspectos.md, docs/ia.md. | Cumple | El C4 nivel 2 está como .jpg en docs/c4/ (desviación de formato, no ausencia); faltan las secciones arc42 7, 8, 11 y 12. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md sigue el patrón NNNN-kebab-case e incluye contexto, opciones, decisión, consecuencias y trazabilidad. | Cumple | El título enuncia el tema (estilo arquitectónico) más que la decisión tomada; no hay ADR reescritos ni borrados en el historial. |
| Tabla de aspectos | docs/aspectos.md usa columnas propias (Prioridad, Tensión, Medida, Decisión/compromiso) sin la columna C4 del curso, y AS-01, AS-02 y AS-04 tienen celdas 'Pendiente'. | No cumple | Solo AS-03 llega a código y pruebas; el eslabón C4 no es navegable y hay filas con huecos. |
| Registro de uso de IA | docs/ia.md con registros S1, S2 y S3, cada uno con lo aceptado y lo rechazado con motivo técnico. | Cumple | El último cambio del archivo es del 2026-08-24 (edd78d7); no crece desde S3. |
| README | README.md describe el sistema, requisitos previos, flutter pub get, flutter run -d chrome y flutter analyze / flutter test. | Cumple | El propio README admite que la evidencia de pruebas en verde se registraría después; hoy sí existen runs verdes de CI. |
| Pipeline y análisis estático | .github/workflows/flutter.yml ejecuta analyze y test (run https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/34801736898) y build.yml invoca el scanner con sonar-project.properties, pero no se aporta la URL pública del análisis ni el Quality Gate. | No cumple | De las tres evidencias exigidas faltan la URL pública del análisis en SonarCloud y el estado del Quality Gate para el hash revisado. |
| Secretos | Revisión de 9d57572: 'secretos: (sin coincidencias)' y envs_versionados vacío; no hay .env ni claves en el árbol. | Cumple | Se anota que .dart_tool/ (package_config.json, version) está versionado; no contiene credenciales pero conviene excluirlo. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `9d575727491866419d94a766599a1bea8ba34cd3 2026-09-13T22:11:29-05:00 Delete docs/ddd/tabla_modulo.md`
- **Veredicto**: con pendientes
- Resumen: El HEAD de origin/main (9d57572, 2026-09-13) conserva la línea base documental y el corte vertical de seguridad con CI verde, pero la entrega S7 no incluye contrato ejecutable, prueba de contrato ni ADR de integración, y quedan pendientes de semanas anteriores en la tabla de aspectos y en las secciones arc42 7, 8, 11 y 12.

Pendientes que siguen abiertos:
- Contrato de API en OpenAPI, AsyncAPI o proto, versionado y con rutas y esquemas.
- Correspondencia verificable entre el contrato y la API implementada.
- Versión de API declarada con historial en git.
- Prueba de contrato y su invocación en el pipeline.
- Evidencia de fallo de la prueba ante un cambio incompatible.
- ADR de estrategia de integración síncrona o asíncrona con escenario y alternativa descartada.
- C4 nivel 2 como código con protocolo y formato en cada flecha.
- URL pública del análisis de SonarCloud con Quality Gate.
- Columnas y filas pendientes de docs/aspectos.md (incluida la trazabilidad C4).
- Secciones arc42 7, 8, 11 y 12 ausentes.

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Evidencia de que la prueba de contrato falla ante un cambio incompatible: se revisaron los 10 runs de runs_ci y todos son success; falta el run en rojo o el registro del cambio incompatible.
- C4 nivel 2 con protocolo y formato en cada flecha: solo hay un .jpg binario; falta el diagrama como código para poder revisar las etiquetas.

## Hallazgos para la planilla

- No existe contrato de API en OpenAPI, AsyncAPI ni proto en el commit calificado 9d57572.
- No hay prueba de contrato ni invocación de contract testing en los workflows.
- Todos los runs de CI están en verde: no hay evidencia de que una prueba falle ante un cambio incompatible.
- El único ADR trata el estilo arquitectónico, no la estrategia de integración síncrona o asíncrona.
- La tabla de aspectos no tiene columna C4 y tres de sus filas siguen marcadas como pendientes.
- El C4 nivel 2 solo existe como imagen, sin fuente revisable ni etiquetas de protocolo y formato verificables.
- Falta la URL pública del análisis de SonarCloud con el estado del Quality Gate.
- No hay commits posteriores al cierre ni diferencias con el estado calificado.
