# semana-06-evidencia-s6 · XALD

> Revisión manual de contingencia, al no producirse JSON publicable en la pasada automática. Se inspeccionó el repositorio público sin ejecutar código. Los hashes y la nota son preliminares, propuesta al docente.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `55993cf` en `origin/master` (2026-09-13T22:06:22-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | revisión manual estática | 

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | `docs/arc42/arc42-template-EN.md` §8.1 nombra `:app`, `:parser`, `:aigemini`, `:corefinanciero`, `:syncqueue` y Backend XALD; tipifica customer-supplier y ACL. | Cumple | El mapa está incorporado en la sección 8 y nombra tanto contextos internos como frontera externa. |
| Tabla módulo a datos con dueño único por entidad | `docs/ownership-matrix.md` §3 asigna `TransaccionEntidad` a `:corefinanciero`, los DTO a sus módulos y la cola a `:syncqueue`. | Cumple | La tabla distingue persistencia, memoria y datos de tránsito. |
| La tabla cubre las entidades que existen en el código | El árbol de `55993cf` contiene `TransaccionEntidad.kt`, `PayloadSincronizacionDTO.kt`, `TransaccionProcesadaDTO.kt` y `CategoriaResultado.kt`, todos incluidos en la matriz. | Cumple | También declara el gestor interno de cola y las interfaces de los módulos. |
| No conformidades de propiedad de datos detectadas sobre el código actual | `docs/auditoriaviolaciones-semana6.md` V-01 a V-07 identifica ubicación, acoplamiento o dueño esperado; §Metodología describe el barrido de dependencias y escrituras. | Cumple | El documento conserva los hallazgos y las rutas históricas de corrección; no se ejecutaron pruebas durante esta revisión. |
| Plan de corrección por no conformidad | La misma auditoría asocia a V-01..V-07 contratos públicos, ACL, DTO de tránsito o remoción de dependencia. | Cumple | Cada fila incluye una acción y la ubicación de la solución. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | `docs/arc42/arc42-template-EN.md` §8.1 define los cinco contextos, sus términos y relaciones. | Cumple | El lenguaje ubica transacción, categorización, cola y sincronización en un contexto concreto. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | `docs/c4/c3.md` describe componentes de la app y `docs/adr/0007-contratos-por-modulo.md` formaliza los contratos por módulo. | Cumple | El reajuste queda documentado; la comparación se hizo contra el estado S5 `9bf16cf` y las rutas C4/ADR presentes en `55993cf`. |
| Aspectos relacionables con los contextos del mapa | `docs/aspectos.md` incluye columna CONTEXTO y una tabla “Cobertura de contextos” para los cinco contextos. | Cumple | A-01..A-05 se relacionan con sus contextos; algunos enlaces apuntan a `experimental`, hallazgo de trazabilidad que no borra el mapeo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio público `ISCOUTB/AS_202620_XALD`, rama `master`; historial con cuatro identidades. | Cumple | La consolidación de identidades queda sujeta a confirmación docente. |
| Estructura mínima | `55993cf` contiene `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Estructura verificable por árbol git. |
| Estado calificado identificable | Último commit de `origin/master` antes del cierre: `55993cf`, 2026-09-13T22:06:22-05:00. | Cumple | La punta actual `364ac5b` es posterior y se usa solo para overall. |
| Nombres de ADR según convención | `docs/adr/0001-...md` a `0007-contratos-por-modulo.md`. | Cumple | Se mantiene la observación histórica de un ADR aceptado reescrito. |
| Tabla de aspectos | `docs/aspectos.md` tiene trazabilidad, pero A-04 conserva Código y Pruebas como Pendiente y varios enlaces apuntan a `experimental`. | No cumple | Se esperaba evidencia navegable en la rama revisada para todas las filas; no se encontró. |
| `docs/ia.md` al día | `docs/ia.md` está presente y tuvo cambios documentales durante la ventana S6. | Cumple | Se conserva como evidencia documental, sin validar las herramientas declaradas. |
| README utilizable | `README.md` está versionado y el workflow indica el proyecto Android/Gradle. | Cumple | No se ejecutaron los comandos del README. |
| Pipeline y análisis estático | `.github/workflows/ci.yml` ejecuta `./gradlew testDebugUnitTest`, pero no contiene scanner ni URL pública de SonarCloud/Quality Gate. | No cumple | Se esperaba scanner, run citable y Quality Gate público; no se encontraron. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `364ac5b` (2026-09-17), posterior al cierre.
- **Veredicto**: con pendientes.
- Resumen: el material S6 documenta los límites y la propiedad de datos; en la punta actual aparece documentación OpenAPI posterior, pero sigue sin evidencia pública de SonarCloud y la tabla de aspectos conserva enlaces fuera de la rama evaluada y celdas pendientes.

Pendientes que siguen abiertos:

- Scanner SonarCloud, run asociado y URL pública del Quality Gate.
- Completar Código y Pruebas de A-04 y corregir enlaces de `docs/aspectos.md` que apuntan a `experimental`.

## Recuento y nota sugerida

8 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 5.0 = 1 + 4 × (8/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- No se ejecutó la suite Gradle; el archivo de workflow es evidencia de configuración, no de un run revisado.
- No se verificó una URL pública de SonarCloud ni su Quality Gate.

## Hallazgos para la planilla

- S6 entrega mapa de contextos, matriz de propiedad, auditoría y plan de corrección con evidencia documental.
- Falta análisis SonarCloud público y la tabla de aspectos mantiene celdas y enlaces no defendibles en `master`.
