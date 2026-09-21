# semana-07-evidencia-s7 · PideUtb

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `557e150` en `origin/master` (2026-09-20T22:21:14-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.yaml (openapi: 3.1.0) y docs/api/asyncapi.yaml (asyncapi: 3.0.0) en 557e150 | Cumple | Ambos contratos versionados en el repositorio, no prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | openapi.yaml declara paths (/v1/pedidos, /v1/menu/items/{item_id}, /v1/pagos/intentos) y components.schemas (Pedido, ItemMenu) con required y tipos | Cumple | Las respuestas llevan content/schema, no solo un listado. |
| Correspondencia entre el contrato y la API implementada | Existen backend/app/{menu,pedidos,pagos}/router.py y tests/test_contrato_api.py, pero no se aportó el contenido de los routers | No verificado | Haría falta citar las líneas de ruta de los routers y contrastarlas con los paths del contrato. |
| Versión de la API declarada y con historial | openapi.yaml info.version 1.0.0 y docs/api/historial/openapi-1.0.0.yaml congelado | Cumple | Versión declarada y copia congelada presente; no se aportó el git log por archivo. |
| Prueba de contrato presente | backend/tests/test_contrato_api.py, test_compatibilidad_contrato.py y test_expectativas_consumidor.py en 557e150 | Cumple | Tres suites de contrato en el repositorio. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/ci.yml, pero no se aportó su contenido ni runs_ci | No verificado | Se esperaba la línea del workflow que invoca la prueba y la URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | docs/api/README.md §3 describe el procedimiento y la salida '3 failed, 71 passed, 3 skipped' | No verificado | No se aporta URL de run en rojo ni el contenido de correcciones.md; queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0003-estrategia-integracion.md con ESC-05 y las alternativas síncrona/asíncrona descartadas | Cumple | Incluye consecuencias de acoplamiento temporal y trazabilidad. |
| arc42 sección 6 con los flujos de interacción | asyncapi.yaml referencia docs/arc42/arc42.md §6.3, pero el contenido aportado se trunca en §1 | No verificado | Haría falta citar la sección 6 y sus flujos descritos. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/nivel2-contenedores.md existe y el commit ddf0364 lo etiqueta, pero no se aportó el diagrama | No verificado | Haría falta ver cada flecha etiquetada con protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_PideUtb público; autores consolidados (Santiago Cuesta, daniarriet, Ruddy) coinciden con los tres integrantes declarados en 557e150 | Cumple | Alias de una misma cuenta se consolidan; .mailmap presente. |
| Estructura mínima | docs/arc42/arc42.md, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md en 557e150 | Cumple | Rutas mínimas del contrato presentes. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md, 0002-propiedad-datos-establecimiento.md y 0003-estrategia-integracion.md con título-decisión y trazabilidad | Cumple | Numeración y kebab-case correctos; los aceptados no aparecen editados. |
| La tabla de aspectos | docs/aspectos.md existe, pero no se aportó su contenido | No verificado | Haría falta comprobar las 8 columnas y que cada celda navegue. |
| Registro de uso de IA | docs/ia.md con historial en git: 8 entradas de 2026-08-08 a 2026-09-20 | Cumple | El registro crece a lo largo del semestre. |
| README | README.md describe el sistema, el arranque con un comando y 'pytest'; declara Python 3.11+ | Cumple | Requisitos previos declarados y prueba documentada. |
| Pipeline y análisis estático | sonar-project.properties y docs/calidad-sonarcloud.md existen, pero faltan la línea del workflow, la URL del run y la URL pública de SonarCloud con Quality Gate | No verificado | El badge no cuenta como evidencia de ejecución. |
| Secretos | Único hallazgo: un comentario en sonar-project.properties:7 que menciona la palabra token; sin .env versionado | Cumple | No es una credencial; no hay nada que rotar. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `557e150fc76dc6c2460b10db399451821987b77f 2026-09-20T22:21:14-05:00 Registrar el Quality Gate en verde y el run del hash entregado`
- **Veredicto**: al dia
- Resumen: A la semana 7 el proyecto está consolidado: contrato OpenAPI 3.1 y AsyncAPI 3.0 versionados con esquemas e historial, ADR-0003 con alternativa descartada y trazabilidad, y pruebas de contrato en el repositorio; sin commits posteriores al cierre. Quedan sin verificar la correspondencia contrato–código, la ejecución y el run en rojo de la prueba, arc42 §6, el C4 nivel 2 y SonarCloud.

Pendientes que siguen abiertos:
- Correspondencia contrato–código (routers)
- Ejecución y run en rojo de la prueba de contrato
- arc42 §6 y C4 nivel 2 etiquetado
- URL pública de SonarCloud con Quality Gate
- Contenido de docs/aspectos.md

## Recuento y nota sugerida

5 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.0 = 1 + 4 × (5/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correspondencia contrato–código: faltan las líneas de ruta de backend/app/*/router.py frente a los paths de docs/api/openapi.yaml.
- Ejecución de la prueba de contrato en CI: falta la línea de .github/workflows/ci.yml y la URL del run.
- Run en rojo por cambio incompatible: falta la URL del run o el contenido de correcciones.md.
- arc42 sección 6 con flujos de interacción: falta el contenido de la sección.
- C4 nivel 2 con protocolo y formato por flecha: falta el diagrama.
- Tabla de aspectos de 8 columnas: falta el contenido de docs/aspectos.md.
- SonarCloud: faltan la línea del workflow, la URL del run y la URL pública con Quality Gate.

## Hallazgos para la planilla

- Contrato OpenAPI 3.1 y AsyncAPI 3.0 versionados con rutas y esquemas de datos completos.
- Política de versionado con reglas de compatibilidad y casos negativos documentados.
- No se aportó el contenido de los routers: la correspondencia contrato–código no se pudo comprobar.
- No se aportan runs de CI ni el contenido de ci.yml: no se verifica la ejecución de la prueba de contrato.
- No hay URL de run en rojo: falta la prueba de que la validación falla ante un cambio incompatible.
- Tres contribuyentes consolidados coinciden con los integrantes declarados.
- Sin credenciales versionadas; el único hallazgo de secretos es un comentario.
