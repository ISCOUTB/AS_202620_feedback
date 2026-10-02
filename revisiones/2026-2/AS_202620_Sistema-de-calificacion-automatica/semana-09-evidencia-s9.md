> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · Calificación automática

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `1f8f76dc169da96e4f668ff6894e7d51ce5be252` en `origin/master` (2026-09-27T19:55:57-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

La punta actual **no tiene commits posteriores a S8**: coincide exactamente con el hash calificado de
S8 (`1f8f76d`) y su fecha es del 2026-09-27. Esta pasada **no tiene corte**: se califica la punta
actual del 2026-10-01, no un commit anterior a un cierre. El periodo S9 (`1f8f76d..origin/master`)
está vacío: el equipo no empujó ninguna porción nueva. Bajo CONTRATO §12, la evidencia previa es
línea base y **no se recalifica por existir**: las filas que describen la entrega S9 quedan en No
cumple (o No verificado) por ausencia de artefacto del periodo, citando el artefacto anterior solo
como contexto. La fila de credenciales y la matriz transversal se deciden sobre el estado en la
punta.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | Contexto (semanas anteriores): `docs/ia.md` documenta construcción asistida de la infraestructura de despliegue, el pipeline y la observabilidad (entrada S8, 2026-09-27), y el corte vertical A-01; código en `backend/`, `frontend/`, `render.yaml`, `docker-compose.yml`. | No cumple | El periodo S9 (`1f8f76d..origin/master`) no tiene commits: no hay porción nueva construida en esta evidencia. El artefacto citado es línea base (CONTRATO §12). |
| Cadena completa navegable para esa porción | Contexto: `docs/aspectos.md` enlaza los escenarios con ADR, código, pruebas y evidencia de la línea base (A-01, EC-07). | No cumple | La cadena de la línea base existe, pero no describe una porción del periodo S9; no hay aspecto nuevo que recorrer. |
| ADR con la decisión argumentada por el equipo | Contexto (semanas anteriores): ADR-0009 a ADR-0012 (plataformas de despliegue) y ADR-0005 (alcance del LLM) argumentan con restricciones del proyecto; ADR-0007 (contextos delimitados y dueño único). | No cumple | No hay ADR del periodo S9 para la porción de esta evidencia; los citados son de S6–S8: línea base que no se recalifica por existir (CONTRATO §12). |
| Prueba que falla ante el defecto que cubre | Contexto (semanas anteriores): `docs/evidencia/medicion-ec07.md` y `backend/herramientas/medir_ec07.py` documentan la medición de EC-07; la evidencia S7 registró una ruptura deliberada del contrato con su fallo. | No verificado | No hay run en rojo, prueba de mutación ni procedimiento documentado del periodo S9. Queda como pregunta para la sustentación (CONTRATO §13). |
| Medición del escenario asociado | Contexto: `docs/evidencia/medicion-ec07.md` liga la métrica a EC-07 (≤10 s, 0 % de pérdida) y `docs/despliegue/costo-mensual.md` documenta costos de S8. | No cumple | Sin medición publicada en el periodo S9; la medición citada es línea base. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | Contexto (semana anterior): `docs/ia.md` documenta lo aceptado, lo corregido y lo rechazado con motivo técnico (entradas de S8, última del 2026-09-27). | No cumple | La última entrada es del 2026-09-27; no hay entrada del periodo S9. Línea base que no satisface la fila (CONTRATO §12). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | El barrido `(INSERT INTO\|UPDATE \|\.save\(\|\.create\(\|repository\.)` sobre el código de la punta no devuelve coincidencias y no existe un documento de auditoría de erosión del periodo en `docs/`. | No cumple | Falta la auditoría exigida por la ficha, con hallazgos, ubicación y corrección, del periodo S9. |
| Dependencias propuestas verificadas en su registro oficial | El diff del periodo contra el hash de S8 (`1f8f76d`) sobre `backend/requirements.txt`, `frontend/pubspec.yaml` y demás manifiestos está vacío: no hay dependencias añadidas en el periodo. | No cumple | Sin dependencias nuevas respecto de S8; no hay lista ni comprobación en npm/PyPI. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido del contrato sobre la punta sin coincidencias; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | Sin credenciales reales en la punta ni en el historial. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | El sistema contempla un componente generativo: ADR-0005 «Acotar el LLM a la generación de distractores diagnósticos» (RF-11 opcional, nodo de proveedor punteado, proveedor no decidido). No hay conjunto de evaluación con resultados, costo por operación ni latencia, ni su contenedor externo con protocolo y costo en el C4 nivel 2. | No cumple | El componente existe como capacidad del sistema, así que no aplica la vía del ADR de no incorporarlo; en el periodo S9 no hay evaluación con costo y latencia. La ausencia de decisión no satisface la fila. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre conforme y visibilidad pública. |
| Estructura mínima presente | En `1f8f76d`: `README.md`, `docs/arc42/arc42-template-ES.md`, `docs/adr/` (0001–0012), `docs/c4/doc-c4.md`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Las seis rutas del contrato §2; arc42 y C4 en ruta propia. |
| Estado calificado identificable | `1f8f76dc169da96e4f668ff6894e7d51ce5be252` en `origin/master`, commit del 2026-09-27T19:55:57-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual, que coincide con el hash de S8. |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md` … `docs/adr/0012-mantener-el-almacen-en-el-disco-efimero-de-la-instancia-hasta-cerrar-r-06.md`. | Cumple | Los doce cumplen `NNNN-titulo-en-kebab-case.md`, sin archivos ajenos. |
| ADR aceptados no reescritos | `git log --follow`: ADR-0007 (creado `c0f976d`, 2026-09-13, «aceptado») se editó en `1c8bcfb` (2026-09-26) para actualizar dónde está la propiedad de datos, sin declarar un ADR de reemplazo. | No cumple | CONTRATO §4 prohíbe editar un ADR aceptado sin declarar reemplazo; la edición es posterior a la aceptación. |
| `docs/ia.md` al día para la semana | Historial de `docs/ia.md`: la última modificación es del 2026-09-27 (`543d48f`), dentro de la ventana de S8. No hay commits sobre el archivo en el periodo S9. | No cumple | El registro no tiene entrada de la semana S9; no se actualizó en el periodo revisado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Único run del hash revisado: [CI 36364030158](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/36364030158), conclusión `success`. No existe `sonar-project.properties` ni paso `sonar` en `.github/workflows/ci.yml`; solo un enlace a SonarCloud en el README. | No cumple | El CI está en verde, pero faltan dos de las tres evidencias del contrato §8 (configuración del análisis y línea del workflow que invoca el scanner). El equipo lo reconoce en `correcciones.md` y `docs/ia.md`. |
| Sin credenciales en el repositorio ni en el historial | Barrido del contrato, `git log -S'BEGIN PRIVATE KEY'` y `-S'AKIA'` sin coincidencias; sin `.env` versionado. | Cumple | El repositorio no expone credenciales. |
| Contribución de todos los integrantes | `git shortlog -sne 1f8f76d`: `scp1109` 83, `josueacademico17-source` 37, `SusanaRosales` 24, `Mariadelmar-restrepo` 17. | Cumple | Cuatro cuentas para los cuatro integrantes declarados; el README asocia cada cuenta a su nombre. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `1f8f76dc169da96e4f668ff6894e7d51ce5be252 2026-09-27T19:55:57-05:00 docs(readme): nombrar la URL de la API en los pasos de despliegue` (`origin/master`)
- **Veredicto**: sin trabajo nuevo de S9; base previa con una no conformidad transversal
- Resumen: la rama `master` no se movió desde S8 (`1f8f76d`). El repositorio conserva la base de S8:
  infraestructura como código (`render.yaml`, `docker-compose.yml`, dos `Dockerfile`), logs JSON, la
  métrica de EC-07, secretos por configuración del proveedor, estimación de costo con puntos de ruptura,
  arc42 §2 y §7, cuatro ADR de plataforma y CI en verde (run 36364030158). Esa base es línea base bajo
  CONTRATO §12 y no satisface las filas de S9. Para esta evidencia faltan la porción nueva con IA y su
  cadena, la prueba que falle ante el defecto del periodo, la medición del periodo, la auditoría de
  erosión, la verificación de dependencias y la evaluación del componente generativo con costo y
  latencia (el sistema sí contempla un LLM para distractores, ADR-0005). Se mantienen la no conformidad
  de SonarCloud y la edición de ADR-0007 sin reemplazo.

Pendientes que siguen abiertos:
- Sin commits de S9: la punta es la de S8.
- Sin porción S9, sin prueba del periodo y sin extracto de `docs/ia.md` del periodo: por CONTRATO §12
  las filas 1, 2, 3, 5, 6, 7 y 8 quedan en No cumple y la fila 4 en No verificado.
- El sistema contempla un componente generativo (ADR-0005) sin conjunto de evaluación, costo por operación ni latencia, ni contenedor externo en el C4 nivel 2.
- SonarCloud sin invocación en el workflow ni URL pública del Quality Gate (pendiente desde S6).
- ADR-0007 editado el 2026-09-26 (`1c8bcfb`) sin reemplazo declarado.

## Recuento y nota sugerida

**1 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

Bajo CONTRATO §12, el único criterio que se resuelve sobre el estado en la punta es el barrido de
credenciales; las demás filas describen la entrega S9, cuyo periodo (`1f8f76d..origin/master`) está
vacío: la evidencia previa es línea base y no se recalifica por existir.

## No verificado / pendientes

- Prueba que falla ante el defecto: **No verificado**. No hay run en rojo, prueba de mutación ni
  procedimiento documentado del periodo S9. Queda como pregunta de sustentación.
- Medición del escenario en el periodo: sin resultado contrastado con umbral de S9.
- Auditoría de erosión: no existe artefacto que la documente para el periodo.
- Dependencias del periodo: el diff contra S8 está vacío, no hay nada que comprobar en los registros.
- Componente generativo: existe como capacidad (ADR-0005) pero sin evaluación con costo y latencia.

## Hallazgos para la planilla

- La punta de `origin/master` (`1f8f76d`, 2026-09-27) es idéntica al hash calificado de S8: el periodo S9 está vacío.
- Aplicado CONTRATO §12: sin artefacto del periodo, solo el barrido de credenciales queda en Cumple.
- El sistema contempla un LLM para distractores diagnósticos (ADR-0005, RF-11 opcional, proveedor no decidido): falta su conjunto de evaluación con costo y latencia y su contenedor externo en el C4 nivel 2.
- CI del hash revisado en verde (run 36364030158), pero sin SonarCloud ni Quality Gate.
- ADR-0007 editado el 2026-09-26 (`1c8bcfb`) sin reemplazo declarado (fila transversal en No cumple).
- Cuatro integrantes contribuyen en el historial; sin credenciales en la punta ni en el historial.
