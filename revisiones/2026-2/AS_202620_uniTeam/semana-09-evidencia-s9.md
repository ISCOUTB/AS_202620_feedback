> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · uniTeam

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `0f3da0f36f8cd7b829106667de88a56a1bc81f54` en `origin/master` (2026-09-27T22:52:09-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

La punta actual **no tiene commits posteriores a S8**: coincide exactamente con el hash calificado de
S8 (`0f3da0f3`) y su fecha es del 2026-09-27. Esta pasada **no tiene corte**: se califica la punta
actual. El periodo S9 (`0f3da0f3..origin/master`) está vacío: el equipo no empujó ninguna porción
nueva. Bajo CONTRATO §12, la evidencia previa es línea base y **no se recalifica por existir**: las
filas que describen la entrega S9 quedan en No cumple (o No verificado) por ausencia de artefacto del
periodo, citando el artefacto anterior solo como contexto. La fila de credenciales y la matriz
transversal se deciden sobre el estado en la punta.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | Contexto (semana anterior): `docs/ia.md` (entradas hasta el 2026-09-28) registra el trabajo asistido de S8: funcionalidades de tareas, flujo de estados, interfaz Kanban y correcciones detectadas por revisión de IA; el sistema está desplegado en cuatro piezas. | No cumple | El periodo S9 (`0f3da0f3..origin/master`) no tiene commits: no hay porción nueva construida en esta evidencia. El artefacto citado es de S8 y es línea base (CONTRATO §12): se cita como contexto pero no satisface la fila. |
| Cadena completa navegable para esa porción | Contexto: `docs/aspectos.md` y `docs/c4/nivel2-contenedores.md` describen escenarios y métricas de S8 (ESC-01/ESC-03). | No cumple | No hay cadena de una porción S9 que recorrer. |
| ADR con la decisión argumentada por el equipo | Contexto (semanas anteriores): `docs/adr/0001`…`0012` con alternativas; `0007`–`0011` son de plataforma (S8) y `0012-publicar-el-flujo-de-estados-desde-el-dominio.md` es de S8. | No cumple | No hay ADR del periodo S9 para la porción de esta evidencia. Los ADR citados son línea base que no se recalifica por existir (CONTRATO §12). |
| Prueba que falla ante el defecto que cubre | Contexto (semana anterior): S8 aportó `test/test_autenticacion.py` y el workflow `CI`, pero el run de CI del hash revisado está en rojo. | No verificado | No hay run en rojo, prueba de mutación ni procedimiento documentado del periodo S9 para la porción de esta evidencia; queda como pregunta para la sustentación (CONTRATO §13). |
| Medición del escenario asociado | No hay resultado de escenario del periodo S9: la punta no cambió desde S8 y no se publicó una medición nueva contra umbral. | No cumple | Sin medición en el periodo. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | Contexto (semana anterior): `docs/ia.md`, última modificación `0f3da0f` (2026-09-27T22:52:09), con entradas del 2026-09-27/28 y correcciones detectadas por IA. | No cumple | El registro no tiene entrada del periodo S9; la última es de S8. Línea base que no satisface la fila (CONTRATO §12). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | No se encontró auditoría de erosión en `docs/`: el barrido `erosión\|límite de contexto\|propiedad de datos` no devuelve coincidencias. | No cumple | Falta la auditoría exigida por la ficha. |
| Dependencias propuestas verificadas en su registro oficial | El diff del periodo contra el hash de S8 (`0f3da0f3..origin/master`) está vacío: no hay dependencias añadidas en el periodo ni, por tanto, verificación que citar. | No cumple | Sin dependencias nuevas respecto de S8; no hay lista ni comprobación en el registro oficial. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido del contrato sobre la punta: las coincidencias son nombres de parámetros y variables (`app/api/seguridad.py:103`, `web/lib/api.ts`, `scripts/medir_esc01.py`), no credenciales reales; el workflow de CI genera la contraseña de MySQL de un solo uso; sin `.env` versionado. | Cumple | Sin credenciales reales; el despliegue usa la configuración del proveedor. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No aparece un conjunto de evaluación con costo y latencia, ni un ADR que decida no incorporar un componente generativo. | No cumple | La ausencia de decisión no es la decisión de no hacerlo; falta el ADR que lo justifique si esa es la posición del equipo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_uniTeam`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre `AS_202620_uniTeam` conforme y visibilidad pública. |
| Estructura mínima presente | En `0f3da0f3`: `docs/arc42/`, `docs/adr/` (0001-0012), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2; `docs/adr/` incluye `.gitkeep`. |
| Estado calificado identificable | `0f3da0f36f8cd7b829106667de88a56a1bc81f54` en `origin/master`, commit del 2026-09-27T22:52:09-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual. Coincide con el hash de S8; no hay commits posteriores. |
| Nombres de ADR según la convención | `docs/adr/0001-*` … `0012-*`, todos `NNNN-titulo-en-kebab-case.md`; el único elemento fuera del patrón es el marcador de carpeta `.gitkeep`, que no es un ADR. | Cumple | Doce ADR conformes. |
| ADR aceptados no reescritos | El ADR `0011-mantener-la-api-despierta-con-un-sondeo-externo.md` se creó en `369b0d9` (2026-09-27T20:09) y se editó en `0f3da0f` (2026-09-27T22:52) tras su aceptación, sin declarar que ese ADR fuera reemplazado. | No cumple | El contrato §4 prohíbe editar un ADR aceptado; el resto de ADR conserva un solo commit. |
| `docs/ia.md` al día para la semana | Historial de `docs/ia.md`: última modificación `0f3da0f` (2026-09-27T22:52:09), dentro de la ventana de S8. No hay commits sobre el archivo en el periodo S9. | No cumple | El registro no tiene entrada de la semana S9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `sonar-project.properties` y `.github/workflows/ci.yml:175` invocan el scanner con espera del Quality Gate (`-Dsonar.qualitygate.wait=true`), pero en el hash revisado el **CI falla**: [36375435263](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/36375435263) y [36379268907](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/36379268907), ambos `failure`. Las 15 corridas de «Comprobación del despliegue» del mismo hash son mixtas (varias en `failure`). | No cumple | Un Quality Gate que no termina en un run exitoso no es evidencia auditable del estado calificado; el CI del hash revisado está en rojo. |
| Sin credenciales en el repositorio ni en el historial | `git grep` del contrato sin credenciales reales; sin `.env` versionado; el workflow de CI genera la contraseña de MySQL por ejecución. | Cumple | Sin credenciales; las coincidencias son identificadores de código. |
| Contribución de todos los integrantes | `git shortlog -sne`: seis grupos de identidades — `Julio Cesar Emiliani` (20), `super-gremlin` (15), `Ian Novoa` (12), `JuanB`/`JuanBustamante` (10+4, misma cuenta), `Daniel Manjarres Herrera` (7), `DaniGamer0907` (1) — para cuatro integrantes declarados. | No verificado | Seis identidades no se reducen a cuatro personas sin la confirmación del docente; no se atribuyen cuentas por parecido de nombre. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `0f3da0f36f8cd7b829106667de88a56a1bc81f54` (2026-09-27T22:52:09-05:00) (`origin/master`)
- **Veredicto**: sin trabajo nuevo de S9; base de S8 con el CI en rojo y la contribución sin cerrar
- Resumen: la rama `master` no se movió desde S8 (`0f3da0f3`). El repositorio conserva la base de S8:
  despliegue en cuatro piezas (sitio estático, API Docker, MySQL gestionado, Auth0) con IaC, health que
  comprueba la base, logs JSON, métricas ligadas a ESC-01/ESC-03, secretos fuera del código, arc42 §7/§2
  y ADR de plataforma. Esa base es línea base bajo CONTRATO §12 y no satisface las filas de S9. Punto
  débil de la punta: el CI del hash revisado está en rojo (incluido el Quality Gate), y la contribución
  por integrante sigue sin poder atribuirse. Para esta evidencia faltan la porción nueva con IA y su
  cadena, la prueba del periodo, la medición, la auditoría de erosión, la verificación de dependencias
  y la decisión sobre el componente generativo.

Pendientes que siguen abiertos:
- Sin commits de S9: la punta es la de S8.
- Sin porción S9, sin prueba del periodo y sin extracto de `docs/ia.md` del periodo: por CONTRATO §12
  las filas 1, 2, 3, 5, 6, 7 y 8 pasan a No cumple y la fila 4 a No verificado.
- CI del hash revisado en rojo (`36375435263`, `36379268907`), incluido el Quality Gate.
- Sin medición contra umbral de ningún escenario en el periodo.
- Sin auditoría de erosión del periodo.
- Sin dependencias nuevas que verificar en el periodo.
- Sin evaluación ni ADR sobre el componente generativo.
- ADR 0011 editado tras su aceptación sin declarar reemplazo (fila transversal en No cumple).
- Contribución por integrante sin atribución confirmada (seis identidades para cuatro personas).

## Recuento y nota sugerida

**1 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

Bajo CONTRATO §12, el único criterio que se resuelve sobre el estado en la punta es el barrido de
credenciales; las demás filas describen la entrega S9, cuyo periodo (`0f3da0f3..origin/master`) está
vacío: la evidencia previa es línea base y no se recalifica por existir.

## No verificado / pendientes

- Prueba que falla ante el defecto: **No verificado**. No hay run en rojo, prueba de mutación ni
  procedimiento documentado del periodo S9; queda como pregunta de sustentación.
- Contribución de todos los integrantes: **No verificado**. Hace falta la confirmación del docente
  para atribuir las seis identidades a las cuatro personas declaradas.
- Medición de escenarios: sin medición del periodo.
- Auditoría de erosión: no existe artefacto del periodo.
- Dependencias del periodo: el diff contra S8 está vacío, no hay nada que comprobar en los registros.
- Componente generativo: no hay evaluación ni ADR del periodo.
- CI del hash revisado en rojo.

## Hallazgos para la planilla

- La punta de `origin/master` (`0f3da0f3`, 2026-09-27) es idéntica al hash calificado de S8: el periodo S9 está vacío.
- Aplicado CONTRATO §12: sin artefacto del periodo, las filas 1, 2, 3, 5, 6, 7, 8 y 10 quedan en No cumple y la fila 4 en No verificado; solo el barrido de credenciales queda en Cumple.
- El CI del hash revisado falla (`36375435263`, `36379268907`), incluido el Quality Gate: la fila transversal de pipeline sigue en No cumple.
- ADR 0011 editado el 2026-09-27 tras su aceptación, sin declarar reemplazo.
- Contribución: seis identidades de correo para cuatro integrantes; no se atribuyen por parecido de nombre.
- Sin auditoría de erosión y sin decisión sobre el componente generativo, exigidas por la evidencia S9.
