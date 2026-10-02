# semana-07-evidencia-s7 · UTB Tracker

> Revisión definitiva: el hash calificado `7cfb872` coincide con la última revisión ≤ cierre (`2026-09-21T05:00:00Z`) en `origin/main`; el equipo no registró commits durante la semana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | `7cfb872` en `origin/main` (2026-08-31T12:27:23-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pasada automática, hash confirmado contra la revisión elegible |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol de 7cfb872 (2026-08-31): no hay ningún openapi/swagger/asyncapi .yaml/.json ni .proto; solo app/, tests/ y docs/. | No cumple | Se buscó con ls-tree -r --name-only HEAD; no existe el artefacto que este criterio exige. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No hay archivo de contrato que citar; app/schemas.py define modelos Pydantic pero no se publica como especificación versionada. | No cumple | La única referencia a OpenAPI es el Swagger autogenerado en /docs citado en README y ADR-0002, que no queda versionado. |
| Correspondencia entre el contrato y la API implementada | app/routers/resources.py, loans.py, users.py y health.py implementan rutas; ningún contrato las documenta ni hay ruta del contrato ausente del código. | No cumple | No hay contrato contra el cual comparar en ninguno de los dos sentidos. |
| Versión de la API declarada y con historial | No existe campo de versión ni archivo de contrato, por lo que el git log del contrato no aplica. | No cumple | Se esperaba info.version en el contrato y su historial en git. |
| Prueba de contrato presente | tests/ y app/tests/ contienen solo conftest.py, test_loans.py, test_resources.py y test_main.py; sin pact, schemathesis, dredd, prism ni spectral. | No cumple | Hay pruebas funcionales del corte vertical, no pruebas de contrato. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml ejecuta 'python -m pytest app/tests/'; el run success del hash, https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/33419672964 (2026-08-31T17:27:34Z), no tiene paso de contrato. | No cumple | Además, la carpeta tests/ (conftest, test_loans, test_resources) ni siquiera la ejecuta el workflow. |
| Evidencia de que la prueba falla ante un cambio incompatible | Los runs en rojo 33418324359 y 33373654206 son de pytest sobre app/tests, no de una prueba de contrato. | No verificado | No hay run rojo de contrato ni evidencia aportada del cambio incompatible; queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0002-cambio-stack-fastapi-flutter.md decide API REST/JSON para el cliente Flutter, descarta DRF y Flask y liga las consecuencias a QS-05 y QS-06. | Cumple | No contrasta explícitamente síncrono frente a asíncrono y la trazabilidad no enlaza commit ni PR. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42.md conserva el encabezado del template y solo cubre secciones iniciales; no hay sección 6 ni docs/arc42/06* en el árbol de 7cfb872. | No cumple | Se esperaba la vista de ejecución con los flujos de interacción descritos. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/C2.md etiqueta las flechas: 'Consume [HTTPS/JSON]' (App Móvil→API Backend), 'Lee y escribe [SQL (SQLAlchemy)]' (API Backend→Base de Datos) y 'Usa [HTTPS]' desde las personas. | Cumple | Las dos flechas persona→App Móvil declaran HTTPS sin formato de datos. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | El clon público funciona con `https://github.com/ISCOUTB/AS_202620_TRACTAR.git` por redirección: `curl -sI https://github.com/ISCOUTB/AS_202620_TRACTAR` responde `301 Moved Permanently` con `Location: https://github.com/ISCOUTB/AS_202620_UTB_TRACKER`, y ese URL responde `200 OK`; la API pública sin token confirma `Moved Permanently`. El nombre canónico actual es `ISCOUTB/AS_202620_UTB_TRACKER`. | Cumple | La cabecera y `EQUIPOS.md` lo declaran `AS_202620_TRACTAR`, pero el repositorio fue renombrado: el nombre real hoy es `AS_202620_UTB_TRACKER` y el URL declarado redirige allí. Sigue en la organización ISCOUTB, es público y conserva el patrón `AS_202620_<PROYECTO>`; es una discrepancia de nomenclatura entre el kit y el remoto, no un incumplimiento de identidad. |
| Estructura mínima | Árbol de 7cfb872: docs/arc42/arc42.md, docs/adr/0001-*.md y 0002-*.md, docs/c4/C2.md y c4_nivel1.md, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Todas las rutas mínimas están presentes en las ubicaciones esperadas. |
| Estado calificado identificable | Rama `origin/main`; `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849` con fecha `2026-08-31T12:27:23-05:00` («Fix: solved the text problem»), confirmado con `git rev-list -1 --before=2026-09-21T05:00:00Z` como el último commit ≤ cierre. | Cumple | Coincide con el estado revisado de la cabecera. Existe un commit posterior, `9cf1ac9` («S7», 2026-09-21T00:14:08-05:00), 14 minutos después del cierre: no se califica. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md y docs/adr/0002-cambio-stack-fastapi-flutter.md cumplen el patrón NNNN-kebab-case y llevan contexto, opciones, decisión y consecuencias. | Cumple | Los títulos anuncian más el tema que la decisión y la trazabilidad no enlaza commit, PR ni elementos C4. |
| ADR aceptados no reescritos | `git log --follow` de `docs/adr/0001-estilo-arquitectonico.md` da un único commit, `5f923cd` (2026-08-23T22:40:51-05:00), y el de `docs/adr/0002-cambio-stack-fastapi-flutter.md` da un único commit, `e88a3d6` (2026-08-31T03:35:36-05:00). Ambos declaran `Aceptado` (línea 5). | Cumple | El historial hasta 7cfb872 no muestra ediciones posteriores a la aceptación ni reemplazo declarado. |
| Registro de uso de IA | docs/ia.md registra dos usos del 2026-08-16 que solo describen lo usado; no hay ningún rechazo ni su motivo técnico. | No cumple | git log de docs/ia.md muestra únicamente e84871f y 74fdb96, ambos del 2026-08-16. |
| Pipeline y análisis estático | .github/workflows/ci.yml solo invoca pytest (run success 33419672964, 2026-08-31T17:27:34Z); no hay sonar-project.properties, paso del scanner ni URL pública de SonarCloud con Quality Gate. | No cumple | Faltan las tres evidencias exigidas desde S6 y no es verificable el bloqueo del pipeline cuando algo falla. |
| Secretos | Búsqueda de credenciales sobre HEAD sin coincidencias y sin archivos .env versionados. | Cumple | No hay secretos que rotar. |
| Contribución de todos los integrantes | `git shortlog -sne 7cfb872` da tres filas (13, 7 y 1 commits) que se consolidan en una sola persona y no cubren a los otros tres integrantes declarados en EQUIPOS.md: no hay ninguna cuenta atribuible a ellos. | No cumple | Todo el historial se concentra en una persona; la verificación es por el historial de git y no se atribuye por parecido de nombre. La pertenencia o el acceso de los otros tres a la organización no se puede comprobar con el protocolo git. |
| Tabla de aspectos | docs/aspectos.md presenta la tabla con las ocho columnas ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia y las filas A-01 a A-06. | Cumple | A-01 a A-05 quedan con '—' en Código, Pruebas y Evidencia; solo A-06 recorre la cadena completa. |
| README | README.md declara qué es UTB Tracker, el arranque con un solo comando (./run.sh) y cómo se prueba con pytest. | Cumple | Cita docs/arc42.md y tests/test_health.py, rutas que no coinciden con el árbol revisado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849 2026-08-31T12:27:23-05:00 Fix: solved the text problem`
- **Veredicto**: con pendientes
- Resumen: A HEAD 7cfb872 (2026-08-31), con un commit posterior al cierre, `9cf1ac9` (2026-09-21T00:14:08-05:00, catorce minutos despues del limite), que no se califica, el proyecto no incorpora el contrato de API ni la prueba de contrato de la semana 7 y arrastra pendientes transversales de semanas anteriores: SonarCloud sin evidencia auditable, sección 6 de arc42, registro de IA sin rechazos y contribución de un solo integrante. Los runs en rojo del 2026-08-30 y 2026-08-31 corresponden a pruebas funcionales, no a una prueba de contrato.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- `9cf1ac9` (2026-09-21T00:14:08-05:00, «S7») llega catorce minutos despues del cierre: no entra en el estado calificado y se registra como entrega tardia.

Pendientes que siguen abiertos:
- Contrato OpenAPI/AsyncAPI/proto versionado con rutas y esquemas de datos
- Prueba de contrato presente y ejecutada por el pipeline
- Evidencia de que la prueba de contrato falla ante un cambio incompatible
- Sección 6 de arc42 con los flujos de interacción
- SonarCloud: configuración, run del scanner y URL pública con Quality Gate
- Registro de IA con al menos un rechazo justificado
- Contribución al historial de los tres integrantes restantes
- Que el workflow ejecute la totalidad de las pruebas del repositorio

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Prueba de contrato que falle ante un cambio incompatible: haría falta la prueba invocada desde el workflow y un run en rojo o la evidencia del cambio incompatible aportado por el equipo.
- Bloqueo del pipeline ante fallo desde el segundo corte: haría falta la configuración de protección de rama o un run fallido que impida la integración.
- Pertenencia de todos los integrantes a la organización ISCOUTB: la evidencia solo muestra el historial de una identidad.

## Hallazgos para la planilla

- El HEAD 7cfb872 (2026-08-31) es anterior al cierre del 2026-09-21 y no hay commits nuevos respecto del cierre anterior.
- No existe contrato OpenAPI, AsyncAPI ni proto versionado en el repositorio.
- El pipeline no ejecuta ninguna prueba de contrato y solo corre pytest sobre app/tests/.
- Las pruebas de tests/ (conftest, test_loans, test_resources) quedan fuera del workflow de CI.
- No hay evidencia de SonarCloud: ni configuración, ni paso del scanner, ni URL del análisis con Quality Gate.
- arc42 sigue siendo el template: falta la sección 6 con los flujos de interacción.
- docs/ia.md no registra qué se rechazó ni por qué.
- Solo una identidad de autor aparece en el historial de los cuatro integrantes declarados.
- El repositorio fue renombrado: `ISCOUTB/AS_202620_TRACTAR` redirige (301) a `ISCOUTB/AS_202620_UTB_TRACKER`, que es su nombre canónico actual. Sigue siendo público y conserva el patrón `AS_202620_<PROYECTO>`, pero el nombre difiere del declarado en la cabecera y en EQUIPOS.md.
