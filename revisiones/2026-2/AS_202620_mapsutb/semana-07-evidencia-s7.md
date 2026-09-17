# semana-07-evidencia-s7 · mapsutb

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `8aee879` en `origin/master` (2026-09-13T18:14:14-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol de HEAD 8aee879 (2026-09-13): ningún archivo OpenAPI/Swagger/AsyncAPI (.yaml/.json) ni .proto; el repositorio es una app Flutter (lib/main.dart) sin API propia. | No cumple | Se esperaba ruta de contrato ejecutable citada; se revisó el árbol completo de origin/master y no existe. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No hay archivo de contrato en el árbol de 8aee879, por lo que no hay versión de especificación, rutas ni esquemas que citar. | No cumple | Criterio dependiente del anterior: sin contrato no hay fragmento que revisar. |
| Correspondencia entre el contrato y la API implementada | El código expone solo repositorios locales (lib/repositories/zona_repository.dart, lib/services/ubicacion_service.dart) sin endpoints HTTP; no hay contrato contra el cual contrastar rutas en ninguno de los dos sentidos. | No cumple | Se esperaba localizar dos rutas del contrato en el código y una del código en el contrato; ninguna de las dos comprobaciones es posible. |
| Versión de la API declarada y con historial | No hay campo de versión de API en ningún archivo del árbol ni ruta de contrato para ejecutar git log sobre ella. | No cumple | Se esperaba campo de versión más historial en git del archivo de contrato. |
| Prueba de contrato presente | test/ contiene únicamente app_smoke_test.dart; no existe prueba de contrato (pact, schemathesis, dredd, prism o similar) en el árbol. | No cumple | Se esperaba ruta de la prueba de contrato; se revisó la carpeta test y el árbol completo. |
| El pipeline ejecuta la prueba de contrato | Workflows del árbol: .github/workflows/ci.yml y .github/workflows/sonar-sync-issues.yml; no existe prueba de contrato que invocar y no se aportó el contenido de ci.yml ni runs_ci con la línea de invocación. | No cumple | Se esperaba la línea del workflow que invoca la prueba más URL del run; no hay ninguna de las dos. |
| Evidencia de que la prueba falla ante un cambio incompatible | No existe prueba de contrato y la evidencia aportada no incluye run en rojo ni registro del cambio incompatible que la hiciera fallar. | No verificado | Motivo: falta la prueba y el run. Haría falta el run fallido o el commit del cambio incompatible documentado; queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0001 a 0004 existen, pero 0002 trata aislamiento con Adapter de Maps SDK y Geocoding y 0003 descarta realidad aumentada (alcance de producto); ninguno compara integración síncrona frente a asíncrona contra un escenario de calidad. | No cumple | Se esperaba un ADR con alternativa de integración descartada y sus consecuencias de acoplamiento; no aparece en el contenido aportado. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06_runtime_view.md en 8aee879: cuatro diagramas de secuencia (trazar ruta, geocodificar, pérdida de Maps SDK/Geocoding, ver panorámica) con pasos numerados. | Cumple | Los flujos describen componentes, adaptadores y rutas de error de forma trazable con la sección 5. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/arc42/05_building_block_view.md, diagrama C4Component (Nivel 2): flechas como Rel(usuario, ui, Interactúa) o Rel(ui, ruta, Solicita una ruta) sin protocolo ni formato; solo algunas relaciones externas anotan HTTPS y ninguna anota formato. | No cumple | docs/c4/C2.md aparece en el árbol pero su contenido no se aportó, por lo que no se pudo comprobar allí; lo verificable incumple la etiqueta protocolo/formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_mapsutb de la organización ISCOUTB, visible=true; autores consolidados por correo e identificador numérico: 4 cuentas de git distintas (dos alias charlygz21/charly comparten el mismo identificador). | Cumple | Nombre y visibilidad correctos y cuatro identidades; no se aportó la lista de membresía de la organización, no atribuible por parecido de nombre. |
| Estructura mínima | Árbol 8aee879 con README.md, docs/arc42/ (01 a 12), docs/adr/ (0001 a 0004), docs/c4/, docs/aspectos.md, docs/ia.md. | Cumple | Desviación de extensión: arc42 mezcla .adoc y .md; además lib/models/05_building_block_view.md está fuera de docs, y 07 y 08 siguen siendo plantilla. |
| Convenciones de ADR | docs/adr con 0001-patrones-de-diseno.md, 0002-patrones-de-diseno-sin-realidad-aumentada.md, 0003-descartar-realidad-aumentada.md y 0004-adoptar-monolito-como-estilo-arquitectonico.md, todos con el patrón NNNN-kebab-case. | Cumple | Los ADR traen contexto, opciones, decisión y consecuencias; la trazabilidad a commit/PR y pruebas no se ve en el contenido y 0001 menciona un cambio de alcance respecto a su versión anterior, sin git log del archivo para confirmar edición. |
| Tabla de aspectos | docs/aspectos.md existe en el árbol de 8aee879, pero la evidencia aportada no incluye su contenido. | No verificado | Motivo: no se pudo comprobar las ocho columnas ni que las celdas sean navegables. Haría falta el archivo completo; los ADR citan una fila A-01 pero no sustituyen esa verificación. |
| Registro de uso de IA | docs/ia.md con historial creciente: commits del 2026-08-09, 2026-08-23, 2026-08-28 y 2026-08-30; el ADR 0003 referencia entradas del 28 y 29/08/2026 con el proceso de la decisión. | Cumple | El historial muestra uso sostenido; la columna de lo rechazado no pudo leerse completa en el extracto aportado. |
| README | README.md declara qué es el sistema, requisitos previos (Flutter SDK, dispositivo y API key), arranque con un solo comando ./scripts/start.sh y verificación con flutter pub get && flutter test. | Cumple | Incluye estado actual con una prueba en verde; los requisitos de mapas dependen de una API key externa no versionada. |
| Pipeline y análisis estático | Existen .github/workflows/ci.yml, .github/workflows/sonar-sync-issues.yml, sonar-project.properties y scripts/sonar_to_github_issues.py, pero la evidencia no aporta runs_ci, ni la línea del workflow que invoca el scanner, ni URL pública de SonarCloud con Quality Gate. | No verificado | Motivo: sin ejecución citada no puede marcarse Cumple; un workflow que solo sincroniza issues no prueba el análisis. Haría falta el run exitoso del hash revisado y la URL del análisis. |
| Secretos | Búsqueda de patrones de credenciales (claves AWS, claves privadas, tokens ghp_/xox/sk-, pares password/secret/token/api_key) sobre HEAD sin coincidencias y sin .env versionado; la lista de archivos no muestra configuración con credenciales. | Cumple | Se recomienda no versionar .dart_tool (package_config.json y similares) por higiene, sin ser incidente de secretos. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `8aee87957c958b8602c5d964ac194d3d13752412 2026-09-13T18:14:14-05:00 Add Week 6 documentation on domain and modularity`
- **Veredicto**: con pendientes
- Resumen: En la punta actual de origin/master (8aee879, 2026-09-13) el proyecto es una app Flutter sin backend ni contrato de API: cumple 1 de 10 criterios de la ficha s7 y 6 de 8 transversales. El entregable central de la semana, contrato más prueba de contrato que falle, no existe.

Pendientes que siguen abiertos:
- Contrato de API en OpenAPI, AsyncAPI o proto, versionado y con esquemas de datos.
- Correspondencia entre contrato y API implementada.
- Prueba de contrato y su invocación en ci.yml, con run exitoso citado.
- Evidencia de que la prueba falla ante un cambio incompatible.
- ADR de estrategia de integración (síncrona o asíncrona) con alternativa descartada y consecuencias.
- C4 nivel 2 con protocolo y formato en cada flecha; revisar también docs/c4/C2.md.
- Evidencia auditable de SonarCloud: línea del scanner, run del hash revisado y URL pública con Quality Gate.
- Contenido verificable de docs/aspectos.md con las ocho columnas y celdas navegables.

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Tabla de aspectos: docs/aspectos.md presente pero sin contenido aportado para comprobar las ocho columnas.
- Pipeline y SonarCloud: sin runs_ci, sin línea del workflow que invoca el scanner y sin URL pública del análisis con Quality Gate.
- Fallo de la prueba de contrato ante cambio incompatible: la prueba no existe y no se aportó run en rojo ni commit del cambio.

## Hallazgos para la planilla

- La entrega s7 no incluye contrato de API: el sistema es una app Flutter sin backend y no hay OpenAPI, AsyncAPI ni proto en el árbol.
- No existe prueba de contrato ni ejecución de contrato en el pipeline, así que tampoco hay evidencia de que falle ante un cambio incompatible.
- Ningún ADR compara integración síncrona frente a asíncrona contra un escenario de calidad.
- arc42 sección 6 sí está desarrollada con cuatro flujos de interacción y pasos numerados.
- El C4 nivel 2 del repositorio no etiqueta protocolo y formato en sus flechas.
- La evidencia de SonarCloud no es auditable: falta el run y la URL pública con Quality Gate.
- Sin secretos detectados y README con arranque de un solo comando.
- No hay commits posteriores al cierre de s7 en origin/master; el hash evaluado es 8aee879.
