# semana-07-evidencia-s7 · ROUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `fe266aa` en `origin/master` (2026-09-20T21:32:01-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/openapi.json presente en el árbol de fe266aa (2026-09-20T21:32:01-05:00), generado por scripts/export_openapi.py | Cumple | Formato JSON OpenAPI versionado; su contenido no se incluyó en el paquete. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/openapi.json está en el árbol pero no se aportó su contenido | No verificado | Se esperaba el fragmento con paths, components/schemas y versión; haría falta citar el JSON. |
| Correspondencia entre el contrato y la API implementada | Existen routers en backend/app/modules/*/infrastructure/router.py, pero sin el contenido de docs/openapi.json | No verificado | No se pudo contrastar dos rutas del contrato en el código ni una del código en el contrato. |
| Versión de la API declarada y con historial | No se incluyó el campo de versión de docs/openapi.json ni git log del archivo | No verificado | Se esperaba info.version y el historial; los commits 'Semana 7 - ROUTB' no se desglosan por archivo. |
| Prueba de contrato presente | backend/tests/test_openapi_contract.py en el árbol de fe266aa | Cumple |  |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml existe pero no se aportó su contenido ni runs_ci | No verificado | Se esperaba la línea que invoca la prueba y la URL del run; el README cita un run sin nombre ni conclusión. |
| Evidencia de que la prueba falla ante un cambio incompatible | docs/evidencia/deteccion-breaking-change.md y docs/evidencia/run-contract.md en el árbol, sin contenido y sin run en rojo en runs_ci | No verificado | Haría falta citar la ejecución fallida o el documento con el cambio incompatible. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0004-integracion-sincrona-rest.md cita el escenario de cupos (20 intentos sobre 4 cupos, p95 3,99 s), descarta la alternativa asíncrona y sus consecuencias de acoplamiento | Cumple |  |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06_vista_de_ejecucion.md describe registro, login y reserva con pasos y diagramas de secuencia | Cumple |  |
| C4 nivel 2 con protocolo y formato en cada flecha | Solo docs/c4/context.md en el árbol y su contenido no vino; ADR 0004 enlaza el 'C4 Nivel 2' a ese archivo | No verificado | Se esperaba el diagrama de nivel 2 con cada flecha etiquetada con protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_ROUTB público (visible=true) y 4 cuentas en el historial consolidado: MKeinerrr, diegobrr999-commits, juliandmanjarrez-tech, junior14700 | Cumple | El número de cuentas coincide con los 4 integrantes declarados; la pertenencia a la organización no se comprobó directamente. |
| Estructura mínima | docs/arc42/ (01–12), docs/adr/ (0001–0004), docs/c4/context.md, docs/aspectos.md, docs/ia.md y README.md en el árbol de fe266aa | Cumple | El C4 vive en docs/c4/ según lo permitido. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md … 0004-integracion-sincrona-rest.md siguen NNNN-kebab-case y llevan contexto, opciones, decisión, consecuencias y trazabilidad | Cumple |  |
| La tabla de aspectos | docs/aspectos.md con columnas ID, Aspecto, Requisito, Contextos relacionados, C4, ADR, Código, Pruebas, Evidencia | Cumple | Añade una columna 'Contextos relacionados' respecto a las ocho del curso; el contenido visible está truncado. |
| Registro de uso de IA | docs/ia.md con 8 entradas de ia_log entre 2026-08-07 y 2026-09-19 | Cumple | El registro crece a lo largo del semestre. |
| README | README.md con descripción, arranque por start.bat/start.sh y pruebas con pytest | Cumple |  |
| Pipeline y análisis estático | .github/workflows/ci.yml y sonar-project.properties en el árbol; no se aportó el workflow ni runs_ci; el README enlaza el dashboard de SonarCloud sin Quality Gate | No verificado | Faltan la línea del scanner, la URL del run exitoso y la URL pública del Quality Gate. |
| Secretos | git grep en fe266aa solo devuelve nombres de variables (password, token, hashed_password) sin valores; envs_versionados vacío; sin AKIA, ghp_ ni PRIVATE KEY | Cumple |  |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `fe266aab4b0019184ab0eafc996821cd0bb36f23 2026-09-20T21:32:01-05:00 Semana 7 - ROUTB`
- **Veredicto**: al dia
- Resumen: En fe266aa (2026-09-20T21:32:01-05:00), anterior al cierre y en origin/master, el contrato OpenAPI, la prueba de contrato, el ADR 0004 y la sección 6 de arc42 están versionados; el contrato transversal se cumple en 6 de 8 filas. La entrega de la semana no pudo verificarse por falta del contenido del contrato y de runs_ci: quedan sin comprobar los esquemas, la correspondencia contrato–código, la versión, la ejecución en el pipeline y la prueba que falla ante un cambio incompatible.

Pendientes que siguen abiertos:
- Contenido del contrato con rutas y esquemas
- Correspondencia contrato–código y versión de la API
- Ejecución de la prueba de contrato en el pipeline
- Run en rojo o evidencia del cambio incompatible
- C4 nivel 2 con protocolo y formato en cada flecha
- SonarCloud con run exitoso y Quality Gate público

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contrato con rutas y esquemas (contenido de docs/openapi.json)
- Correspondencia contrato–API implementada
- Versión de la API y su historial en git
- Ejecución de la prueba de contrato en el pipeline (línea del workflow y URL del run)
- Prueba que falla ante un cambio incompatible
- C4 nivel 2 con protocolo y formato en cada flecha
- SonarCloud: línea del scanner, run exitoso y Quality Gate público

## Hallazgos para la planilla

- El contrato docs/openapi.json existe y está versionado, pero su contenido no se incluyó en el paquete.
- No hay run en rojo ni documento legible que demuestre que la prueba de contrato falla ante un cambio incompatible.
- No se pudo leer ci.yml: no se verificó que el pipeline ejecute la prueba de contrato.
- No se pudo comprobar la correspondencia contrato–código ni la versión declarada de la API.
- El C4 nivel 2 no se pudo verificar: solo hay docs/c4/context.md y su contenido no vino.
- La evidencia de SonarCloud en el paquete es parcial: falta el run y el Quality Gate.
