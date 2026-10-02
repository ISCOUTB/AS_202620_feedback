> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · XALD

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `f90f28d3e3b0fe3da81d71b8cc9d9d10bdf07491` en `origin/master` (2026-09-27T21:56:48-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

La punta actual **no tiene commits posteriores a S8**: coincide exactamente con el hash calificado de
S8 (`f90f28d3`) y su fecha es del 2026-09-27. Esta pasada **no tiene corte**: se califica la punta
actual. El periodo S9 (`f90f28d3..origin/master`) está vacío: el equipo no empujó ninguna porción
nueva. Bajo CONTRATO §12, la evidencia previa es línea base y **no se recalifica por existir**: las
filas que describen la entrega S9 quedan en No cumple (o No verificado) por ausencia de artefacto del
periodo, citando el artefacto anterior solo como contexto. La fila de credenciales y la matriz
transversal se deciden sobre el estado en la punta.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | Contexto (semanas anteriores): `docs/ia.md` documenta el uso de IA en los cinco módulos (`:app`, `:parser`, `:corefinanciero`, `:syncqueue`, `:aigemini`); el backend de Render con health, logs JSON, `/metrics` y validación de `X-API-Key` es de S8. | No cumple | El periodo S9 (`f90f28d3..origin/master`) no tiene commits: no hay porción nueva construida en esta evidencia. El artefacto citado es de S7/S8 y es línea base (CONTRATO §12): se cita como contexto pero no satisface la fila. |
| Cadena completa navegable para esa porción | Contexto: `docs/aspectos.md` tiene la tabla A-01…A-05 con C4, escenario, ADR, código y pruebas; A-04 sigue con Código y Pruebas en *Pendiente* y las columnas apuntan a la rama `experimental`, no a la rama calificada. | No cumple | No hay cadena de una porción S9 que recorrer; además la tabla base enlaza a `experimental`. |
| ADR con la decisión argumentada por el equipo | Contexto (semanas anteriores): `docs/adr/0001`…`0010` con contexto, opciones y consecuencias; `0008-plataforma-de-despliegue.md`, `0009-distribucion-app.md` y `0010-observabilidad.md` son de S8. | No cumple | No hay ADR del periodo S9 para la porción de esta evidencia. Los ADR citados son línea base que no se recalifica por existir (CONTRATO §12). |
| Prueba que falla ante el defecto que cubre | Contexto (semana anterior): S8 aportó pruebas de backend (`test_api.py`: health, métricas, 401 sin llave, 202 con llave) y una prueba de contrato Redocly en CI. | No verificado | No hay run en rojo, prueba de mutación ni procedimiento documentado del periodo S9 para la porción de esta evidencia; queda como pregunta para la sustentación (CONTRATO §13). |
| Medición del escenario asociado | No hay resultado de escenario del periodo S9: la punta no cambió desde S8 y no se publicó una medición nueva contra umbral. | No cumple | Sin medición en el periodo. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | Contexto (semana anterior): `docs/ia.md`, última modificación `809ea69` (2026-09-27T15:51); documenta aceptados y rechazados con motivo (p. ej. descarte de la `feature` CSV). | No cumple | El registro no tiene entrada del periodo S9; la última es de S8. Línea base que no satisface la fila (CONTRATO §12). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Contexto (semana anterior): `docs/adr/0007-contratos-por-modulo.md:10` y `docs/ownership-matrix.md:154` documentan la auditoría de propiedad de datos de la semana 6 (siete violaciones corregidas). | No cumple | No hay auditoría de erosión del periodo S9; el artefacto citado es de S6/S7 y es línea base. |
| Dependencias propuestas verificadas en su registro oficial | El diff del periodo contra el hash de S8 (`f90f28d3..origin/master`) está vacío: no hay dependencias añadidas en el periodo ni, por tanto, verificación que citar. | No cumple | Sin dependencias nuevas respecto de S8; no hay lista ni comprobación en el registro oficial. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido del contrato sobre la punta: sin coincidencias materiales; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | Sin credenciales reales en el árbol ni en el historial. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | El sistema declara un contexto de categorización `:aigemini` (Gemini) en C4 y en `docs/aspectos.md` (A-01/A-04), pero no aparece un conjunto de evaluación con costo y latencia ni un ADR que decida sobre su incorporación. | No cumple | No hay evaluación ni ADR del periodo; la ausencia de decisión no es la decisión de no hacerlo. Si el sistema incorpora el componente, la ficha exige su evaluación de costo y latencia. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_XALD`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre `AS_202620_XALD` conforme y visibilidad pública. |
| Estructura mínima presente | En `f90f28d3`: `docs/arc42/`, `docs/adr/` (0001-0010), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2. |
| Estado calificado identificable | `f90f28d3e3b0fe3da81d71b8cc9d9d10bdf07491` en `origin/master`, commit del 2026-09-27T21:56:48-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual. Coincide con el hash de S8; no hay commits posteriores. |
| Nombres de ADR según la convención | `docs/adr/0001-*` … `0010-*`, todos `NNNN-titulo-en-kebab-case.md`; el filtro del contrato §4 no devuelve nada. | Cumple | Diez ADR conformes. |
| ADR aceptados no reescritos | Los ADR 0001–0005 recibieron una edición de contenido el 2026-09-27 (`efcc390`, `44c6096`, `6b7d514`, `a660a64`, `86c48ca`) después de aceptados y sin declarar reemplazo. | No cumple | No conformidad de la base, aún visible en la punta: el contrato §4 prohíbe editar un ADR aceptado. |
| `docs/ia.md` al día para la semana | Historial de `docs/ia.md`: última modificación `809ea69` (2026-09-27T15:51), dentro de la ventana de S8. No hay commits sobre el archivo en el periodo S9. | No cumple | El registro no tiene entrada de la semana S9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Único workflow `.github/workflows/ci.yml`; no existe `sonar-project.properties` ni paso del scanner; no hay URL pública de análisis con Quality Gate. Run del hash revisado: [Android CI 36371759708](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/36371759708), `success`. | No cumple | El CI está en verde, pero faltan la configuración, la línea del scanner y la URL pública del Quality Gate exigidas por el contrato §8. |
| Sin credenciales en el repositorio ni en el historial | `git grep` del contrato y `git log -S` sin coincidencias de claves reales; sin `.env` versionado. | Cumple | Sin credenciales. |
| Contribución de todos los integrantes | `git shortlog -sne`: `dilanbejarano011` (186), `colmenares2007-crypto` (94), `xaviergarciadiaz20-commits` (64), `axeljruiz717-hash` (58). | Cumple | Cuatro identidades = cuatro integrantes declarados en `EQUIPOS.md`. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `f90f28d3e3b0fe3da81d71b8cc9d9d10bdf07491` (2026-09-27T21:56:48-05:00) (`origin/master`)
- **Veredicto**: sin trabajo nuevo de S9; base de S8 con deudas abiertas
- Resumen: la rama `master` no se movió desde S8 (`f90f28d3`). El repositorio conserva la base de S8:
  backend desplegado en Render descrito como código, health check, logs JSON, métrica Prometheus ligada
  a ESC-05, secretos fuera del código, ADR 0008–0010 y arc42 §7 con costo. Esa base es línea base bajo
  CONTRATO §12 y no satisface las filas de S9. Para esta evidencia faltan la porción nueva con IA y su
  cadena, una prueba que falle ante el defecto del periodo, la medición de un escenario, la auditoría
  de erosión, la verificación de dependencias y la decisión/evaluación sobre el componente generativo
  (`:aigemini`). Se mantienen no conformidades transversales ya detectadas: ADR aceptados editados sin
  reemplazo y ausencia de SonarCloud auditable.

Pendientes que siguen abiertos:
- Sin commits de S9: la punta es la de S8.
- Sin porción S9, sin prueba del periodo y sin extracto de `docs/ia.md` del periodo: por CONTRATO §12
  las filas 1, 2, 3, 5, 6, 7 y 8 pasan a No cumple y la fila 4 a No verificado.
- `docs/aspectos.md` con A-04 en Código/Pruebas *Pendiente* y enlaces a la rama `experimental`.
- Sin medición contra umbral de ningún escenario en el periodo.
- Sin auditoría de erosión del periodo.
- Sin dependencias nuevas que verificar en el periodo.
- Sin evaluación de costo/latencia ni ADR sobre el componente generativo (`:aigemini`).
- Sin SonarCloud (configuración, run y URL pública con Quality Gate), pendiente desde S6.
- ADR 0001–0005 editados después de aceptarse el 2026-09-27 sin declarar reemplazo.

## Recuento y nota sugerida

**1 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

Bajo CONTRATO §12, el único criterio que se resuelve sobre el estado en la punta es el barrido de
credenciales; las demás filas describen la entrega S9, cuyo periodo (`f90f28d3..origin/master`) está
vacío: la evidencia previa es línea base y no se recalifica por existir.

## No verificado / pendientes

- Prueba que falla ante el defecto: **No verificado**. No hay run en rojo, prueba de mutación ni
  procedimiento documentado del periodo S9; queda como pregunta de sustentación.
- Medición de escenarios: sin medición del periodo.
- Auditoría de erosión: no existe artefacto del periodo.
- Dependencias del periodo: el diff contra S8 está vacío, no hay nada que comprobar en los registros.
- Componente generativo: no hay evaluación ni ADR del periodo.
- SonarCloud auditable: pendiente desde S6.
- La punta no tiene `docs/ia.md` con entrada de S9.

## Hallazgos para la planilla

- La punta de `origin/master` (`f90f28d3`, 2026-09-27) es idéntica al hash calificado de S8: el periodo S9 está vacío.
- Aplicado CONTRATO §12: sin artefacto del periodo, las filas 1, 2, 3, 5, 6, 7, 8 y 10 quedan en No cumple y la fila 4 en No verificado; solo el barrido de credenciales queda en Cumple.
- El sistema declara un componente de categorización `:aigemini` (Gemini) sin evaluación de costo/latencia ni ADR de decisión: deuda relevante para S9.
- Sin pitidos de SonarCloud: faltan configuración, línea del scanner y URL pública con Quality Gate.
- ADR 0001–0005 editados el 2026-09-27 después de aceptados, sin declarar reemplazo (fila transversal en No cumple).
- `docs/aspectos.md` arrastra A-04 sin código ni pruebas y enlaces a la rama `experimental`.
