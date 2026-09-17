# semana-07-evidencia-s7 · Drift

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `430b9a0` en `origin/master` (2026-09-15T11:27:22-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol de 430b9a0 (2026-09-15) sin ningún archivo openapi/swagger/asyncapi (.yaml/.json) ni .proto; se buscó con ls-tree -r --name-only HEAD con patrón (openapi\|swagger\|asyncapi).(ya?ml\|json)$\|.proto$ y no hay coincidencias. | No cumple | No hay artefacto de contrato que citar; la API solo se describe en prosa en docs/arc42/arc42_8_conceptos_transversales.md (sección 8.9). |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No existe el archivo del contrato en el árbol de 430b9a0, por lo que no hay rutas ni esquemas de respuesta que citar. | No cumple | Se esperaba un fragmento del contrato con paths y schemas; no se encontró ningún archivo de especificación. |
| Correspondencia entre el contrato y la API implementada | La API real documentada en prosa (GET /games/search?q=<consulta>, docs/arc42/arc42_8_conceptos_transversales.md §8.9, y el endpoint de compatibilidad citado en docs/c4/componentes.md) no tiene contrato contra el cual contrastar. | No cumple | No se puede verificar ninguno de los dos sentidos (contrato→código, código→contrato) porque falta el contrato. |
| Versión de la API declarada y con historial | Sin archivo de contrato en 430b9a0 no hay campo de versión ni salida posible de git log -- <ruta del contrato>. | No cumple | Se esperaba campo de versión (en el archivo o en la ruta) y su historial en git. |
| Prueba de contrato presente | backend/tests/ solo contiene steam_fixtures.py, test_health.py, test_search_games.py y test_compatibility.py; ninguna prueba de contrato (pact, schemathesis, dredd, prism). | No cumple | Se esperaba una ruta de prueba de contrato; no se encontró ninguna en el árbol de 430b9a0. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml existe en el árbol, pero no se aportó su contenido ni runs_ci, y no existe artefacto de contrato ni prueba de contrato que el workflow pueda invocar (ver filas anteriores). | No cumple | Se esperaba la línea del workflow que invoca la prueba y la URL del run; no hay ninguno de los dos. |
| Evidencia de que la prueba falla ante un cambio incompatible | No se aportaron runs_ci ni evidencia del equipo de un cambio incompatible que pusiera la prueba en rojo; en la evidencia del repositorio no hay bloque de ejecuciones de Actions. | No verificado | Queda como pregunta de sustentación: aportar el run en rojo o el cambio incompatible y su resultado (curl a /actions/runs filtrando conclusion != success). |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/ contiene 0001-adoptar-arquitectura-hexagonal.md, 0002-adoptar-nextjs-fastapi-arquitectura-hexagonal.md y 0003-reajuste-contextos-dominio.md; ninguno decide síncrono vs asíncrono ni evalúa la alternativa descartada con consecuencias de acoplamiento frente a un escenario de calidad. | No cumple | ADR-0003 ajusta contextos delimitados, no la estrategia de integración; el escenario E2 de mantenibilidad no se usa para justificar síncrono/async. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42_6_Vista_Ejecucion.md en 430b9a0: tres flujos con diagramas de secuencia (6.1 búsqueda y comparación, 6.2 fallo de fuente externa, 6.3 estimación de compatibilidad) y explicación numerada de cada paso. | Cumple | Cada flujo declara su escenario asociado y los bloques coinciden con la sección 5. |
| C4 nivel 2 con protocolo y formato en cada flecha | El árbol incluye docs/c4/contenedores.md, pero su contenido no se aportó; el nivel 2 de docs/arc42/arc42_5_vista_bloques.md (§5.2.1 y §5.2.2) etiqueta las flechas con «puerto de salida» y nombres de API, sin protocolo ni formato explícitos. | No verificado | Hace falta el contenido del diagrama de contenedores para comprobar protocolo (HTTP/REST) y formato (JSON) en cada flecha. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | AS_202620_Drift visible en la organización ISCOUTB, rama principal origin/master, HEAD 430b9a0 (2026-09-15); autores consolidados: JerryDBM (77 commits), JoshuaR01 (61), lmpdiaz12 (61) y maufern4ndez (57), que corresponden a los 4 integrantes declarados. | Cumple | Las variantes Sherry, JoshXX, Luis Mario Perez Diaz y Mauricio Andres Fernandez Espinosa consolidan con las cuentas anteriores por identidad de autor, no por parecido de nombre; los 4 integrantes aparecen en el historial. |
| Estructura mínima | En HEAD 430b9a0 existen docs/arc42/ (secciones 1-6, 8, 9, 10, 12), docs/adr/ (0001-0003), docs/c4/ (contexto, contenedores, componentes), docs/aspectos.md, docs/ia.md y README.md. | Cumple | Los nombres de arc42 usan guiones bajos y mayúsculas distintas de la plantilla y aún faltan las secciones 7 y 11; es desviación de forma, no ausencia. |
| Convenciones de ADR | Los tres archivos siguen NNNN-titulo-en-kebab-case.md y enuncian la decisión; ADR-0001 está marcado como «Reemplazado por ADR-0002» y ADR-0003 incluye contexto, tres opciones evaluadas, decisión y consecuencias. | Cumple | Trazabilidad incompleta: ADR-0001 y ADR-0003 dejan el commit «pendiente» y los enlaces de trazabilidad de ADR-0003 apuntan a rutas inexistentes en el árbol. |
| Tabla de aspectos | docs/aspectos.md en 430b9a0: tabla con las ocho columnas (ID · Aspecto · Requisito · C4 · ADR · Código · Pruebas · Evidencia) y filas E1-E5 con enlaces a C4, ADR, archivos de código y evidencias. | Cumple | La fila E2 declara explícitamente que la prueba de sustitución del adaptador está pendiente. |
| Registro de uso de IA | docs/ia.md existe y crece a lo largo del semestre: 27 entradas de git log entre 2026-08-09 y 2026-09-13 (última 5f7fa4c), pero no se aportó su contenido. | No verificado | Se verificó existencia y mantenimiento por historial; falta el texto para comprobar para qué se usó, qué se aceptó y qué se rechazó con su motivo. |
| README | README.md de 430b9a0 describe qué es DRIFT, requisitos previos (Python 3.12+, Node 22+), comando único de arranque `python scripts/start.py` y cómo se prueba (pytest, npm run build, k6 run scripts/k6_baseline.js). | Cumple | Cita «8 pruebas aprobadas» y «compilación aprobada» como validación local, sin enlace a un run de CI que lo respalde. |
| Pipeline y análisis estático | Existen .github/workflows/ci.yml y sonar-project.properties, pero no se aportó la línea del workflow que invoca el scanner, ni la URL de un run exitoso, ni la URL pública del análisis con estado del Quality Gate; el README indica que el análisis «se ejecutará en GitHub Actions cuando el equipo realice un push autorizado». | No cumple | Faltan las tres evidencias exigidas desde S6; badge o configuración sin ejecución no cuentan. |
| Secretos | En HEAD 430b9a0: sin coincidencias del grep de patrones (AKIA, claves privadas, ghp_, sk-, xox, password/secret/token) y lista de .env versionados vacía. | Cumple | Mantener la revisión tras cada push, porque el repositorio es público. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `430b9a0cf7c2c9effde4b983e0ca256082f77f1d 2026-09-15T11:27:22-05:00 Revise performance testing details in README`
- **Veredicto**: con pendientes
- Resumen: En la punta actual de master (430b9a0, 2026-09-15, rama origin/master, estado calificado en modo early) el proyecto tiene arquitectura hexagonal implementada, ADR, arc42 con flujos de interacción y documentos transversales presentes, pero la entrega de la semana 7 no aporta contrato ejecutable, ni prueba de contrato, ni ADR de estrategia de integración, y no hay runs_ci que respalden pipeline ni SonarCloud.

Pendientes que siguen abiertos:
- Contrato OpenAPI/AsyncAPI versionado (S7)
- Prueba de contrato ejecutada por el pipeline (S7)
- Evidencia de que la prueba de contrato falla ante un cambio incompatible (S7)
- ADR de estrategia de integración síncrona o asíncrona (S7)
- Evidencia pública de SonarCloud con Quality Gate, pendiente desde S6
- C4 nivel 2 con protocolo y formato en cada flecha
- Trazabilidad de ADR-0001 y ADR-0003 (commit y enlaces pendientes)
- Prueba de sustitución del adaptador para E2, declarada pendiente en docs/aspectos.md

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución del pipeline y del análisis estático: no hay runs_ci ni URL pública de SonarCloud; comprobar con ls .github/workflows/ y curl a /repos/ISCOUTB/AS_202620_Drift/actions/runs más la URL del análisis con Quality Gate.
- Fallo de la prueba de contrato ante un cambio incompatible: no hay run en rojo ni evidencia del equipo; aportar el run o el cambio incompatible aplicado.
- Contenido de docs/c4/contenedores.md (C4 nivel 2): no aportado; hace falta leer el diagrama para verificar protocolo y formato en cada flecha.
- Contenido de docs/ia.md: no aportado; falta verificar la columna de lo rechazado y su motivo técnico.
- Contenido de .github/workflows/ci.yml: no aportado; hace falta la línea que invoca pruebas y scanner.
- Contenido de docs/c4/componentes.md y backend/app/main.py más allá de los extractos: no permiten contrastar rutas del código con un contrato inexistente.

## Hallazgos para la planilla

- No existe contrato OpenAPI/AsyncAPI/proto en el árbol de 430b9a0: la API solo está descrita en prosa.
- No hay ninguna prueba de contrato en backend/tests/ ni comando de contrato identificado en el pipeline.
- No se aportaron runs_ci: no se puede verificar la ejecución del pipeline ni del scanner de SonarCloud.
- Sin evidencia de que una prueba de contrato falle ante un cambio incompatible del proveedor.
- Ningún ADR decide la estrategia de integración síncrona o asíncrona frente a un escenario de calidad.
- La sección 6 de arc42 sí documenta tres flujos de interacción con diagramas de secuencia y explicación paso a paso.
- La tabla de aspectos tiene las ocho columnas y trazabilidad E1-E5, con E2 aún pendiente de prueba.
- Trazabilidad de ADR-0001 y ADR-0003 con commit pendiente y enlaces a rutas inexistentes.
