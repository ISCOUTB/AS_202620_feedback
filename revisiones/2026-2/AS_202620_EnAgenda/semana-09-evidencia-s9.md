> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · EnAgenda

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `2c7d77a421ab95b89dd68d696d49277e9f36a45c` en `origin/master` (2026-09-27T23:42:39-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

La punta actual **no tiene commits posteriores a S8**: coincide exactamente con el hash calificado de
S8 (`2c7d77a`) y su fecha es del 2026-09-27. Esta pasada **no tiene corte**: se califica la punta
actual del 2026-10-01, no un commit anterior a un cierre. El repositorio declara `master` como rama
principal (`origin/HEAD → origin/master`); existe además una rama `main` (`41f6517`) que es ancestro
y no se mezcla. La punta conserva los marcadores de conflicto de merge sin resolver detectados en S8.
El periodo S9 (`2c7d77a..origin/master`) está vacío: no hay porción nueva. Bajo CONTRATO §12 la
evidencia previa es línea base y **no se recalifica por existir**; por eso las filas que describen la
entrega S9 quedan en No cumple (o No verificado) por ausencia de artefacto del periodo, citando el
artefacto anterior solo como contexto. La fila de credenciales y la matriz transversal se deciden
sobre el estado en la punta.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | Contexto (semana anterior): `docs/ia.md` (entrada 30/08/2026) documenta la construcción del módulo de Invitaciones con ChatGPT; código en `src/invitaciones/{aplicacion,dominio,infraestructura}/` y `app/web.py`, con commits en el historial. | No cumple | El periodo S9 (`2c7d77a..origin/master`) no tiene commits: no hay porción nueva construida en esta evidencia. El artefacto citado es de la semana del 30/08 y es línea base (CONTRATO §12): no satisface la fila. |
| Cadena completa navegable para esa porción | Contexto (semanas anteriores): `docs/aspectos.md:3` fila A-01 enlaza C4 niveles 1-3, ADR-0001, `src/invitaciones/`, `app/web.py`, `tests/test_invitaciones.py`, `tests/test_api_invitaciones.py`, `tests/test_contrato_openapi.py` y `docs/evidencia.md`; los destinos existen. | No cumple | La fila citada no se modificó en el periodo S9 (`2c7d77a..origin/master` vacío): es línea base (CONTRATO §12) y no satisface la fila. Además la tabla carece de fila de encabezado y `docs/evidencia.md` conserva marcadores de conflicto (ver overall). |
| ADR con la decisión argumentada por el equipo | Contexto (semanas anteriores): `docs/adr/0001-usar-monolito-modular.md` compara capas, hexagonal y monolito modular con las restricciones del proyecto (equipo de 3, herramientas gratuitas, privacidad) y decide; `docs/adr/0002-estrategia-integracion-api.md` y `docs/adr/0003-desplegar-api-flask-en-render.md` argumentan con alternativas descartadas. | No cumple | No hay ADR del periodo S9 para la porción de esta evidencia. Los ADR citados son de semanas anteriores: línea base que no se recalifica por existir (CONTRATO §12). Se mantiene la observación de que ADR-0001 describe Next.js/Server Actions mientras el código es Flask y ADR-0003 deja «Decide: [COMPLETAR CON INTEGRANTES]». |
| Prueba que falla ante el defecto que cubre | No hay run en rojo, prueba de mutación ni procedimiento documentado: `docs/evidencia.md` solo registra `pytest -q → 12 passed`; la prueba de contrato (`tests/test_contrato_openapi.py`) no tiene evidencia de fallo controlado. | No verificado | Falta una de las tres evidencias que admite la ficha; queda como pregunta de sustentación. |
| Medición del escenario asociado | No hay resultado contrastado contra un umbral. `docs/evidencia.md` muestra valores de la métrica (`0` y `1`) pero no un escenario de calidad con umbral; `docs/aspectos.md` no declara escenarios EC con medida. | No cumple | Sin medición publicada en la punta. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | Contexto (semanas anteriores): `docs/ia.md` tiene columnas «Qué se rechazó o modificó» con motivos: rechazo del envío por correo por exposición de datos en repo público (08-Ago), rechazo del rol colaborador por innecesario (07-Ago), rechazo de Next.js/Server Actions (30/08). | No cumple | El extracto citado pertenece a semanas anteriores y la última entrada es del 27-Sep-2026 (S8); no hay entrada del periodo S9. Línea base que no satisface la fila (CONTRATO §12). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Contexto (semana anterior): `docs/arquitectura/contextos-y-propiedad-de-datos.md:80` «Verificación de violaciones de propiedad»: tabla con comprobaciones de escrituras fuera del contexto dueño, entidades de negocio en `compartido/` y acceso directo al repositorio, con resultado y plan de corrección. | No cumple | Es un artefacto de S6, no del periodo S9, y no está enmarcado como auditoría de generación. Bajo CONTRATO §12 la evidencia previa es línea base y no satisface la fila; no hay auditoría de erosión del periodo. |
| Dependencias propuestas verificadas en su registro oficial | El diff del periodo contra el hash de S8 (`2c7d77a`) sobre `requerimiento.txt` está vacío: no hay dependencias añadidas en el periodo ni verificación que citar. | No cumple | Sin dependencias nuevas respecto de S8; no hay comprobación en PyPI. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido del contrato sobre la punta: coincidencias solo en tokens de dominio y generación (`app/web.py:85` `token=invitacion.token`; `src/invitaciones/dominio/invitaciones.py:26` `secrets.token_urlsafe(32)`); sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | Sin credenciales reales; `.env.example` está versionado con marcadores de conflicto, no con secretos. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No hay componente generativo en el sistema ni un ADR que decida no incorporarlo; el uso de IA registrado es apoyo de construcción, no un componente de la aplicación. | No cumple | La ausencia de decisión no es la decisión de no hacerlo; falta el ADR que lo justifique. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_EnAgenda`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre `AS_202620_EnAgenda` conforme y visibilidad pública. |
| Estructura mínima presente | En `2c7d77a`: `docs/arc42/`, `docs/adr/` (0001-0003), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2. No conformidad aparte: `Dockerfile`, `docker-compose.yml`, `render.yaml`, `.dockerignore`, `.env.example` y `docs/evidencia.md` conservan marcadores de conflicto sin resolver (no afecta la presencia de las rutas exigidas). |
| Estado calificado identificable | `2c7d77a421ab95b89dd68d696d49277e9f36a45c` en `origin/master`, commit del 2026-09-27T23:42:39-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual. `master` es la rama principal declarada por el remoto; `main` es ancestro y no se mezcla. |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md`, `0002-estrategia-integracion-api.md` y `0003-desplegar-api-flask-en-render.md`. | Cumple | Los tres cumplen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | ADR-0001 nace como propuesta (`e1219bf`) y se reemplaza por la decisión de monolito modular (`c38adfb`, 2026-08-23) antes de declararse aceptado; ADR-0002 y ADR-0003 no tienen commits de reescritura posteriores a su aceptación. | Cumple | No se observa reescritura de un ADR aceptado sin reemplazo declarado. |
| `docs/ia.md` al día para la semana | Historial de `docs/ia.md`: la última modificación es del 2026-09-27 (`f7bc011`), dentro de la ventana de S8. No hay commits sobre el archivo después del cierre de S8. | No cumple | El registro no tiene entrada de la semana S9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Runs del hash revisado: [CI 36378874812](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/36378874812), conclusión `failure`, y `pages build` 36378874993. No existe configuración ni URL pública de SonarCloud. | No cumple | CI en rojo en el hash revisado y SonarCloud ausente; faltan todas las evidencias del contrato §8. |
| Sin credenciales en el repositorio ni en el historial | Barrido del contrato y `git log -S` sin coincidencias de claves reales; sin `.env` versionado. | Cumple | Sin credenciales; las coincidencias son tokens de dominio y de generación. |
| Contribución de todos los integrantes | `git shortlog -sne 2c7d77a`: `Jein-12` 70, `Daoisttl0FB3` 69 y `GabrielaMorales Cancino` 5 (mismo correo `gabimoralesc30`, se consolidan), `eliabarnedocondef10-gif` 18. | Cumple | Tres personas consolidadas por correo para tres integrantes declarados; todas con commits. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `2c7d77a421ab95b89dd68d696d49277e9f36a45c 2026-09-27T23:42:39-05:00 algo` (`origin/master`)
- **Veredicto**: sin trabajo nuevo de S9; punta con conflictos de merge sin resolver
- Resumen: la rama `master` no se movió desde S8 (`2c7d77a`). La punta sigue siendo el merge con
  marcadores de conflicto sin resolver en `.dockerignore:3`, `.env.example:1`, `Dockerfile:11`,
  `docker-compose.yml:5`, `render.yaml:3` y `docs/evidencia.md:44`, lo que deja la infraestructura
  como código inválida y el CI del hash en rojo (run 36378874812). Todas las piezas de S8 y anteriores
  (cadena de aspectos navegable, ADRs argumentados, registro de IA con rechazos motivados y
  verificación de propiedad de datos de S6) son línea base bajo CONTRATO §12 y no satisfacen las filas
  de S9. Para esta evidencia faltan la porción nueva con IA y su cadena, la prueba que falle ante el
  defecto del periodo, la medición contra umbral, la verificación de dependencias del periodo, la
  auditoría de erosión, la decisión sobre el componente generativo, una entrada de IA de la semana y
  SonarCloud.

Pendientes que siguen abiertos:
- Sin commits de S9: la punta es la de S8.
- Sin artefactos del periodo S9: por CONTRATO §12 las filas 1, 2, 3, 6 y 7 pasan a No cumple; solo el
  barrido de credenciales queda en Cumple.
- Conflictos de merge sin resolver en seis archivos de infraestructura y en `docs/evidencia.md`.
- CI del hash revisado en rojo.
- Prueba que falle ante el defecto que cubre: sin evidencia.
- Medición de escenario contra umbral: ausente.
- Sin dependencias nuevas que verificar en el periodo.
- Sin ADR sobre el componente generativo.
- Sin SonarCloud (configuración, run y URL pública con Quality Gate), pendiente desde S5/S6.
- `docs/aspectos.md` sin fila de encabezado.

## Recuento y nota sugerida

**1 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

Bajo CONTRATO §12, el único criterio que se resuelve sobre el estado en la punta es el barrido de
credenciales; las demás filas describen la entrega S9, cuyo periodo (`2c7d77a..origin/master`) está
vacío: la evidencia previa es línea base y no se recalifica por existir.

## No verificado / pendientes

- Prueba que falla ante el defecto: No verificado; no hay run en rojo, mutación ni procedimiento documentado del periodo S9. Queda como pregunta de sustentación.
- Auditoría de erosión: no hay artefacto del periodo S9; la verificación de propiedad de datos de S6 es línea base y no satisface la fila.
- Medición de escenario contra umbral: ausente.
- Dependencias del periodo: el diff contra S8 está vacío, no hay nada que comprobar en PyPI.
- Componente generativo: no hay componente ni ADR de no incorporarlo.
- Conflictos de merge sin resolver en `Dockerfile`, `docker-compose.yml`, `render.yaml`, `.dockerignore`, `.env.example` y `docs/evidencia.md`.

## Hallazgos para la planilla

- La punta de `origin/master` (`2c7d77a`, 2026-09-27) es idéntica al hash calificado de S8: el periodo S9 está vacío.
- Aplicado CONTRATO §12: sin artefacto del periodo, las filas 1, 2, 3, 6 y 7 pasan de Cumple a No cumple; solo el barrido de credenciales queda en Cumple.
- Persisten marcadores de conflicto de merge sin resolver en `.dockerignore`, `.env.example`, `Dockerfile`, `docker-compose.yml`, `render.yaml` y `docs/evidencia.md`.
- CI del hash revisado en rojo (run 36378874812); sin SonarCloud ni Quality Gate.
- `docs/aspectos.md` no tiene fila de encabezado y su cadena no enlaza una medición; `docs/evidencia.md` está corrupto por conflictos.
- Sin prueba que falle ante el defecto que cubre (No verificado, pregunta de sustentación).
- La verificación de propiedad de datos de `docs/arquitectura/contextos-y-propiedad-de-datos.md:80` (S6) es línea base: no se recalifica como auditoría de erosión de S9.
- Sin decisión sobre el componente generativo, exigida por la evidencia S9.
