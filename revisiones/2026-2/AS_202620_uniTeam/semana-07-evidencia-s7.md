# Evidencia S7 · uniTeam

> Auditoría local definitiva del informe automático. Se corrigió una discrepancia material: el historial actual de `origin/master` contiene un estado S7 elegible anterior al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `1ea4aba` en el historial de `origin/master` (2026-09-18T22:21:34Z) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | `docs/api/openapi.yaml:1-9` declara OpenAPI 3.0.3, versión 0.2.0 y las rutas desde la línea 10. | Cumple | Especificación ejecutable versionada. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | `docs/api/openapi.yaml:42-489` documenta proyectos, tareas, progreso, autenticación, errores y esquemas de entrada/salida. | Cumple | Incluye restricciones, enums, códigos y referencias reutilizables. |
| Correspondencia entre el contrato y la API implementada | `app/main.py:67-78` implementa `/` y `/activo`; `app/api/rutas_proyectos.py`, `rutas_tareas.py` y `rutas_progreso.py` implementan las rutas del OpenAPI. `test/test_contrato.py` ejercita la aplicación real. | Cumple | Se contrastaron rutas en ambos sentidos. |
| Versión de la API declarada y con historial | `docs/api/openapi.yaml:5` declara `0.2.0`; el archivo se creó en `992b72b` (2026-09-18T16:40:29-05:00). | Cumple | — |
| Prueba de contrato presente | `test/test_contrato.py` contiene 325 líneas de pruebas de autenticación, validación, autorización, respuestas, paginación y auditoría; `scripts/verificar_contrato.py` verifica rutas, esquemas y respuestas. | Cumple | — |
| El pipeline ejecuta la prueba de contrato | `.github/workflows/ci.yml:44-59` valida el YAML y ejecuta `pytest -v test/test_contrato.py`; run exitoso para `1ea4aba`: https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/35401676270 | Cumple | El run exitoso es anterior al cierre. |
| Evidencia de que la prueba falla ante un cambio incompatible | Existen runs fallidos durante la construcción de S7, pero el repositorio no identifica cuál correspondió a un cambio incompatible deliberado ni enlaza una secuencia rojo→verde de contrato. | No verificado | Hace falta el cambio incompatible concreto y su run fallido. |
| ADR de la estrategia de integración ligado a un escenario | `docs/adr/0006-estilo-sincrono-con-eventos-en-proceso.md:18-114` compara tres alternativas, mantiene el modelo síncrono y lo liga a ESC-01 y ESC-04. | Cumple | Incluye condiciones explícitas de reevaluación. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/arc42-uniteam.md:260-465` contiene diagramas de secuencia para crear tareas, negar acceso, crear proyectos, asignar responsables, cambiar estado, consultar progreso y agregar miembros. | Cumple | — |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/c4/nivel2-contenedores.md:25-32` etiqueta relaciones y `:55-64` detalla protocolo y formato para cada una. | Cumple | — |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon sin autenticación de `ISCOUTB/AS_202620_uniTeam`. | Cumple | — |
| Estructura mínima presente | En `1ea4aba` existen `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | — |
| Estado calificado identificable | `origin/master`, `1ea4aba2dbc2b55631927849a4fcff0da08a1a90`, 2026-09-18T22:21:34Z. | Cumple | El commit quedó incorporado a `master` por el merge posterior `73d714c`; el protocolo de auditoría toma el último commit de su historial con fecha ≤ cierre. |
| Nombres de ADR según la convención | Seis ADR con nombres `NNNN-titulo-en-kebab-case.md`. | Cumple | — |
| ADR aceptados no reescritos | Cada ADR aparece en un único commit de creación; el ADR 0001 declara reemplazo por el 0002. | Cumple | — |
| `docs/ia.md` al día para la semana | `992b72b` actualiza el registro el 18 de septiembre con S7 y sus decisiones. | Cumple | — |
| Pipeline, SonarCloud y Quality Gate públicos | El run del hash está verde, pero el workflow no invoca scanner ni existe URL pública de análisis con Quality Gate. | No cumple | — |
| Sin credenciales en el repositorio ni en el historial | Barrido sin secretos materiales; las menciones de `token` son identificadores y los valores MySQL del CI son credenciales efímeras del servicio de prueba. | Cumple | — |
| Contribución de todos los integrantes | El historial contiene `super-gremlin`, `Ian Novoa`, `Julio Cesar Emiliani`, `JuanB`/`JuanBustamante`, `Daniel Manjarres Herrera` y `DaniGamer0907`; `EQUIPOS.md` solo asocia al equipo las cuentas `super-gremlin` e `iansx`, sin vincularlas a personas, y `iansx` no aparece. | No verificado | No se atribuyen ni consolidan identidades por parecido de nombre; hace falta confirmación docente. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `73d714ce49ee2085275755091d00f7688f4dee26` (2026-09-21T11:46:49-05:00).
- El merge que incorporó S7 a `master` ocurrió después del cierre; el contenido conserva fechas de commit anteriores al cierre y por eso aparece en el estado reconstruido por el comando del contrato.
- El run de la punta actual falló: https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/35627786409.
- Continúan abiertos SonarCloud público y la evidencia específica de que la prueba contractual falla ante un cambio incompatible.

## Recuento y nota sugerida

**9 de 10 criterios Cumple.**

**Nota sugerida (propuesta al docente, publicada por decisión del profesor): 4.6 = 1 + 4 × (9/10).** La nota final la fija el profesor en Moodle.

## No conformidades y pendientes

- Aportar un cambio incompatible concreto y el run rojo que demuestre la sensibilidad de la prueba contractual.
- Incorporar scanner, run y URL pública de SonarCloud con Quality Gate.
- Restablecer el CI de la punta de `master`.

## Hallazgos para la planilla

- La auditoría reemplaza “sin actividad” por una evaluación completa de `1ea4aba`.
- Nueve criterios cumplen; solo queda sin verificar la prueba roja ante incompatibilidad.
