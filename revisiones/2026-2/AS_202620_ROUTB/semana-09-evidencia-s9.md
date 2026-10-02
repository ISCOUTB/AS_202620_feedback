> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · ROUTB

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `eae667ef4339d3e8e89461b1e5f865a08eb21d10` en `origin/master` (2026-09-27T21:58:06-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

La punta actual **no tiene commits posteriores a S8**: coincide exactamente con el hash calificado de
S8 (`eae667e`) y su fecha es del 2026-09-27. Esta pasada **no tiene corte**: se califica la punta
actual del 2026-10-01, no un commit anterior a un cierre. El periodo S9 (`eae667e..origin/master`)
está vacío: el equipo no empujó ninguna porción nueva. Bajo CONTRATO §12, la evidencia previa es
línea base y **no se recalifica por existir**: las filas que describen la entrega S9 quedan en No
cumple (o No verificado) por ausencia de artefacto del periodo, citando el artefacto anterior solo
como contexto. La fila de credenciales y la matriz transversal se deciden sobre el estado en la
punta.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | Contexto (semanas anteriores): `docs/ia.md` (entradas S5–S8) documenta construcción asistida del módulo `backend/app/modules/trips/` (control atómico de cupos, ADR-0003) y de observabilidad/despliegue; commits `e9d337c` (S5), `78200a6` y `b0426fa` (S8). | No cumple | El periodo S9 (`eae667e..origin/master`) no tiene commits: no hay porción nueva construida en esta evidencia. El artefacto citado es línea base (CONTRATO §12): se cita como contexto pero no satisface la fila. |
| Cadena completa navegable para esa porción | `docs/aspectos.md` filas 1–5 enlazan C4, ADR, código, pruebas y evidencia de las piezas previas; la fila 5 llega a `arc42/07_vista_de_despliegue.md` y `evidencia/costo_mensual.md`. No hay fila que corresponda a una porción de S9. | No cumple | La cadena de la línea base está completa, pero no describe una porción del periodo S9; no hay aspecto nuevo que recorrer. |
| ADR con la decisión argumentada por el equipo | Contexto (semanas anteriores): ADR-0003 (control atómico de cupos), ADR-0004 (integración síncrona REST, con alternativa asíncrona descartada) y ADR-0005/0006 (Render/Supabase, con alternativas descartadas) argumentan con restricciones del proyecto. | No cumple | No hay ADR del periodo S9 para la porción de esta evidencia; los citados son de S5–S8: línea base que no se recalifica por existir (CONTRATO §12). |
| Prueba que falla ante el defecto que cubre | Contexto (semanas anteriores): ADR-0003 y `docs/ia.md` (Semana 7, 2026-09-19) documentan la salida real de `pytest` en rojo ante la ruta `/trips/` eliminada; la prueba de concurrencia mide 20 intentos sobre 4 cupos. | No verificado | No hay run en rojo, prueba de mutación ni procedimiento documentado del periodo S9; el artefacto citado es de S7. Queda como pregunta para la sustentación (CONTRATO §13). |
| Medición del escenario asociado | Contexto (semanas anteriores): `docs/evidencia/metricas-escenario-calidad.md` y ADR-0003 registran la medición de latencia (p95) del escenario de rendimiento. | No cumple | Sin medición publicada en el periodo S9; la medición citada es línea base (S5/S8). |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | Contexto (semana anterior): `docs/ia.md` incluye la entrada «Semana 8» (2026-09-24) con lo aceptado y lo rechazado (nubes mayores, Fly.io, Railway, secretos en el repositorio) y su motivo técnico. | No cumple | La última entrada es del 2026-09-24; no hay entrada del periodo S9. Línea base que no satisface la fila (CONTRATO §12). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | El barrido `(INSERT INTO\|UPDATE \|\.save\(\|\.create\(\|repository\.)` sobre el código de la punta no devuelve coincidencias y no existe documento de auditoría de erosión en `docs/`. | No cumple | Falta la auditoría exigida por la ficha, con hallazgos, ubicación y corrección, del periodo S9. |
| Dependencias propuestas verificadas en su registro oficial | El diff del periodo contra el hash de S8 (`eae667e`) sobre `backend/requirements.txt`, `frontend/pubspec.yaml` y demás manifiestos está vacío: no hay dependencias añadidas en el periodo ni, por tanto, verificación que citar. | No cumple | Sin dependencias nuevas respecto de S8; no hay lista ni comprobación en npm/PyPI. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido del contrato sobre la punta: coincidencias solo en identificadores y datos de prueba (`backend/app/modules/auth/infrastructure/schemas.py:6` `password: str`; `backend/tests/test_trips_flow.py:18` `hashed_password="hash"`); sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. No aparece `docs/` en el barrido. | Cumple | Sin credenciales reales; los aciertos son nombres de campo y valores de prueba. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No hay componente generativo en el sistema (búsqueda de `openai\|anthropic\|gemini\|llm\|gpt\|generativ` sin coincidencias en el código) ni un ADR que decida no incorporarlo; el único uso de IA es como apoyo de construcción. | No cumple | La ausencia de decisión no es la decisión de no hacerlo; falta el ADR que lo justifique si esa es la posición del equipo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_ROUTB`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre `AS_202620_ROUTB` conforme y visibilidad pública. |
| Estructura mínima presente | En `eae667e`: `docs/arc42/` (01–12), `docs/adr/` (0001–0006), `docs/c4/context.md`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2. |
| Estado calificado identificable | `eae667ef4339d3e8e89461b1e5f865a08eb21d10` en `origin/master`, commit del 2026-09-27T21:58:06-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual, que coincide con el hash de S8. |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md` … `docs/adr/0006-base-de-datos-supabase.md`. | Cumple | Los seis cumplen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | `git log --follow`: ADR-0001 creado `1ed002b` y editado `a94a1a3` (2026-08-30); ADR-0002 creado `e9d337c` y editado `53ed7c3` (2026-09-19); ADR-0003 creado `e9d337c` y editado `f706aa6` (2026-09-06); ADR-0005 y ADR-0006 creados `78200a6`/`35d088c` y editados `b0426fa` (2026-09-25). Ninguna edición declara un ADR de reemplazo. | No cumple | CONTRATO §4 prohíbe editar un ADR aceptado sin declarar reemplazo; las ediciones son posteriores a la aceptación y no hay ADR sucesor. |
| `docs/ia.md` al día para la semana | Historial de `docs/ia.md`: la última modificación es del 2026-09-24 (`78200a6`), dentro de la ventana de S8. No hay commits sobre el archivo en el periodo S9. | No cumple | El registro no tiene entrada de la semana S9; no se actualizó en el periodo revisado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Único run del hash revisado: [CI ROUTB 36371840003](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/36371840003), conclusión `success`. Existe `sonar-project.properties`, pero `.github/workflows/ci.yml` no invoca el scanner y no hay URL pública de análisis ni Quality Gate. | No cumple | El CI está en verde, pero falta la evidencia de SonarCloud exigida por el contrato §8. |
| Sin credenciales en el repositorio ni en el historial | Barrido del contrato y `git log -S` sin coincidencias de claves reales; sin `.env` versionado; `backend/.env.example` con placeholders. | Cumple | Sin credenciales; coincidencias solo en identificadores y datos de prueba. |
| Contribución de todos los integrantes | `git shortlog -sne eae667e`: `MKeinerrr` 53 más 2 con un segundo correo institucional (consolidado), `diegobrr999-commits` 6, `juliandmanjarrez-tech` 3, `junior14700` 2. | Cumple | Cuatro identidades para cuatro integrantes; aporte concentrado en un integrante, ya señalado en planilla. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `eae667ef4339d3e8e89461b1e5f865a08eb21d10 2026-09-27T21:58:06-05:00 Semana 8 - ROUTB` (`origin/master`)
- **Veredicto**: sin trabajo nuevo de S9; base previa con deudas abiertas
- Resumen: la rama `master` no se movió desde S8 (`eae667e`). El repositorio conserva la base de S8:
  infraestructura como código (`render.yaml`, `backend/Dockerfile`, `docker-compose.yml`), logs JSON,
  métrica ligada al escenario, secretos por configuración del proveedor, estimación de costo, arc42
  §7 con Render/Supabase, ADR-0005/0006 y CI en verde (run 36371840003). Esa base es línea base bajo
  CONTRATO §12 y no satisface las filas de S9. Para esta evidencia faltan la porción nueva con IA y
  su cadena, la medición del periodo, la prueba que falle ante el defecto del periodo, la auditoría de
  erosión, la verificación de dependencias y la decisión sobre el componente generativo. Se mantienen
  las no conformidades transversales: ADR aceptados editados sin reemplazo y SonarCloud sin invocación
  en el pipeline.

Pendientes que siguen abiertos:
- Sin commits de S9: la punta es la de S8.
- Sin porción S9, sin prueba del periodo y sin extracto de `docs/ia.md` del periodo: por CONTRATO §12
  las filas 1, 3, 5 y 6 quedan en No cumple y la fila 4 en No verificado.
- Sin auditoría de erosión ni verificación de propiedad de datos del periodo.
- Sin dependencias nuevas que verificar en el periodo.
- Sin ADR sobre el componente generativo.
- SonarCloud sin invocación en el workflow ni URL pública del Quality Gate (pendiente desde S6).
- ADR-0001, 0002, 0003, 0005 y 0006 editados después de aceptarse sin declarar reemplazo.

## Recuento y nota sugerida

**1 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

Bajo CONTRATO §12, el único criterio que se resuelve sobre el estado en la punta es el barrido de
credenciales; las demás filas describen la entrega S9, cuyo periodo (`eae667e..origin/master`) está
vacío: la evidencia previa es línea base y no se recalifica por existir.

## No verificado / pendientes

- Prueba que falla ante el defecto: **No verificado**. No hay run en rojo, prueba de mutación ni
  procedimiento documentado del periodo S9; la evidencia de `pytest` en rojo citada en ADR-0003 es de
  S7. Queda como pregunta de sustentación.
- Medición del escenario en el periodo: sin resultado contrastado con umbral de S9.
- Auditoría de erosión: no existe artefacto que la documente.
- Dependencias del periodo: el diff contra S8 está vacío, no hay nada que comprobar en los registros.
- Componente generativo: no hay componente ni ADR de no incorporarlo.

## Hallazgos para la planilla

- La punta de `origin/master` (`eae667e`, 2026-09-27) es idéntica al hash calificado de S8: el periodo S9 está vacío.
- Aplicado CONTRATO §12: sin artefacto del periodo, solo el barrido de credenciales queda en Cumple.
- La cadena de `docs/aspectos.md` (filas 1–5) sigue completa para la línea base, pero no describe una porción de S9.
- CI del hash revisado en verde (run 36371840003), pero sin SonarCloud ni Quality Gate.
- ADR-0001, 0002, 0003, 0005 y 0006 editados después de aceptarse sin declarar reemplazo (fila transversal en No cumple).
- Sin auditoría de erosión y sin decisión sobre el componente generativo, exigidas por la evidencia S9.
