> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · ElMapita

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `e5c3ac6ecb598c8e126aaa091cce9af01fe818c4` en `origin/main` (2026-09-27T16:26:27-06:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

La punta actual **no tiene commits posteriores a S8**: coincide exactamente con el hash calificado de
S8 (`e5c3ac6`) y su fecha es del 2026-09-27. Esta pasada **no tiene corte**: se califica la punta
actual del 2026-10-01, no un commit anterior a un cierre. El periodo S9 (`e5c3ac6..origin/main`) está
vacío: el equipo no empujó ninguna porción nueva. Bajo CONTRATO §12, la evidencia previa es línea base
y **no se recalifica por existir**: las filas que describen la entrega S9 quedan en No cumple (o No
verificado) por ausencia de artefacto del periodo, citando el artefacto anterior solo como contexto.
La fila de credenciales y la matriz transversal se deciden sobre el estado en la punta.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | Contexto (semana anterior): `docs/ia.md` (entrada 2026-09-20) documenta la construcción asistida del contrato de integración; código en `docs/api/openapi.v1.yaml`, `backend/test/contract/openapi.contract-spec.ts`, controladores de `backend/src/modules/*/interfaces/`; commits `afae3be` (creación, S7) y `9ee88c5` (cierre de RSK-04, S8). | No cumple | El periodo S9 (`e5c3ac6..origin/main`) no tiene commits: no hay porción nueva construida en esta evidencia. El artefacto citado pertenece a S7/S8 y es línea base (CONTRATO §12): se cita como contexto pero no satisface la fila. |
| Cadena completa navegable para esa porción | `docs/aspectos.md` filas `EC-01`…`EC-04`: la columna Pruebas dice «(pendiente)» y Evidencia dice «Pendiente» en las cuatro. El contrato de A-01 sí enlaza ADR-0003 y el job `contract`, pero la fila de aspectos no llega a prueba ni a medición. | No cumple | La cadena se rompe en Pruebas y en Evidencia para los cuatro escenarios. |
| ADR con la decisión argumentada por el equipo | Contexto (semanas anteriores): `docs/adr/0001-estilo-arquitectonico-propuesto.md:5` (`status: Accepted`, S3) argumenta Monolito Modular con las restricciones del proyecto (3 devs junior/medio, riesgo de lock-in de Supabase, testabilidad sin device farm); `docs/adr/0003-contrato-openapi-versionado.md` (S7/S8) y `docs/adr/0004-despliegue-render-docker.md` (S8) comparan alternativas y descartan opciones. | No cumple | No hay ADR del periodo S9 para la porción de esta evidencia. Los ADR citados son de S3/S7/S8: línea base que no se recalifica por existir (CONTRATO §12). |
| Prueba que falla ante el defecto que cubre | Contexto (semana anterior): `docs/adr/0003-contrato-openapi-versionado.md` (sección «Cierre de RSK-04», S8) cita el run en rojo [35549974182](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/35549974182) que capturó la deriva de prefijo; `docs/ia.md` (2026-09-20) registra «falla en las 16» antes del fix. | No verificado | El run en rojo citado es de S8, no del periodo S9. No hay run en rojo, prueba de mutación ni procedimiento documentado del periodo; queda como pregunta para la sustentación (CONTRATO §13). |
| Medición del escenario asociado | `docs/aspectos.md` filas `EC-01`…`EC-04`: la columna Evidencia sigue en «Pendiente»; no hay resultado contrastado contra el umbral (p95 < 5 s, ≥ 30 FPS, accuracy ≤ 15 m, offline < 5 s). | No cumple | Sin medición publicada en la punta. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | Contexto (semana anterior): `docs/ia.md` documenta rechazos con motivo técnico: H-09 clasificado como falso positivo con justificación línea por línea, descarte del formato `.svg`, descarte del catálogo de no conformidades anterior y no elección de Hexagonal pese al puntaje. | No cumple | El extracto citado pertenece a S8: la última entrada es del 2026-09-27 y no hay entrada del periodo S9. Línea base que no satisface la fila (CONTRATO §12). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | No se encontró auditoría de erosión ni verificación de propiedad de datos en `docs/`: el barrido `erosión\|límite de contexto\|propiedad de datos` no devuelve coincidencias. | No cumple | Falta la auditoría exigida por la ficha, incluidos los hallazgos con ubicación y corrección. |
| Dependencias propuestas verificadas en su registro oficial | El diff del periodo contra el hash de S8 (`e5c3ac6`) sobre `backend/package.json` y `frontend/pubspec.yaml` está vacío: no hay dependencias añadidas en el periodo ni, por tanto, verificación que citar. | No cumple | Sin dependencias nuevas respecto de S8; no hay lista ni comprobación en npm/PyPI. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido del contrato sobre la punta: coincidencias solo en tipos y datos de prueba (`backend/src/modules/auth/domain/index.ts:27` `password: string`; `backend/test/contract/openapi.contract-spec.ts:221` `password: 'clave-segura'`); sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | Sin credenciales reales; `.gitleaksignore` documenta falsos positivos históricos. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No hay componente generativo en el sistema ni un ADR que decida no incorporarlo; el único uso de IA es como apoyo de construcción, no como componente de la aplicación. | No cumple | La ausencia de decisión no es la decisión de no hacerlo; falta el ADR que lo justifique si esa es la posición del equipo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_ElMapita`, clonado sin autenticación; rama principal `origin/main`. | Cumple | Nombre `AS_202620_ElMapita` conforme y visibilidad pública. |
| Estructura mínima presente | En `e5c3ac6`: `docs/arc42/`, `docs/adr/` (0001-0004), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2; arc42 en plantilla única y C4 en Markdown más PNG. |
| Estado calificado identificable | `e5c3ac6ecb598c8e126aaa091cce9af01fe818c4` en `origin/main`, commit del 2026-09-27T16:26:27-06:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual. Coincide con el hash de S8; no hay commits posteriores. |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico-propuesto.md`, `0002-restriccion-rendimiento-compatibilidad-dispositivos.md`, `0003-contrato-openapi-versionado.md` y `0004-despliegue-render-docker.md`. | Cumple | Los cuatro cumplen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | ADR-0001 declara `status: Accepted` (2026-08-22) y fue editado en `07b36f4` (2026-08-30T23:31:03-05:00) sin declarar reemplazo; ADR-0003 se editó en `9ee88c5` (2026-09-27T00:57:42-06:00) después de crearse en `afae3be` (2026-09-20). | No cumple | El contrato §4 prohíbe editar un ADR aceptado sin reemplazo declarado; ninguna de las dos ediciones lo declara. |
| `docs/ia.md` al día para la semana | Historial de `docs/ia.md`: la última modificación es del 2026-09-27 (`e5c3ac6`), dentro de la ventana de S8. No hay commits sobre el archivo después del cierre de S8. | No cumple | El registro no tiene entrada de la semana S9; no se actualizó en el periodo revisado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Único run del hash revisado: [CI 36355303177](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/36355303177), conclusión `success`. No existe `sonar-project.properties` ni paso `sonar` en el workflow; no hay URL pública de análisis ni Quality Gate. | No cumple | El CI está en verde, pero falta la evidencia de SonarCloud exigida por el contrato §8. |
| Sin credenciales en el repositorio ni en el historial | Barrido del contrato y `git log -S` sin coincidencias de claves reales; sin `.env` versionado; `.env.example` con placeholders. | Cumple | Sin credenciales; coincidencias solo en tipos y datos de prueba. |
| Contribución de todos los integrantes | `git shortlog -sne e5c3ac6`: `RobotDRMX` 26, `Rodrigo Vazquez Rico` 4, `dgarza2705` 1. El integrante Angel Fabian Gutierrez Gomez no tiene ningún commit atribuible en todo el historial. | No cumple | Una persona de tres sin contribución visible en Git; `RobotDRMX` sigue sin atribuir. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `e5c3ac6ecb598c8e126aaa091cce9af01fe818c4 2026-09-27T16:26:27-06:00 url 27-09-2026` (`origin/main`)
- **Veredicto**: sin trabajo nuevo de S9; base previa con deudas abiertas
- Resumen: la rama `main` no se movió desde S8 (`e5c3ac6`). El repositorio conserva la base de S8:
  contrato OpenAPI versionado con prueba de contrato, ADRs con alternativas, CI en verde (run
  36355303177) y un `docs/ia.md` que crece y documenta rechazos. Esa base es línea base bajo
  CONTRATO §12 y no satisface las filas de S9. Para esta evidencia faltan la porción nueva con IA y
  su cadena, la medición de los escenarios (`aspectos.md` con Pruebas y Evidencia en «Pendiente»), la
  prueba que falle ante el defecto del periodo, la auditoría de erosión, la verificación de
  dependencias, la decisión sobre el componente generativo y la evidencia de SonarCloud. Se mantienen
  las no conformidades transversales ya detectadas: ADR aceptados editados sin reemplazo y
  contribución de un integrante ausente.

Pendientes que siguen abiertos:
- Sin commits de S9: la punta es la de S8.
- Sin porción S9, sin prueba del periodo y sin extracto de `docs/ia.md` del periodo: por CONTRATO §12
  las filas 1, 3 y 6 pasan a No cumple y la fila 4 a No verificado.
- `docs/aspectos.md` con Pruebas y Evidencia en «Pendiente» (EC-01…EC-04).
- Sin medición contra umbral de ningún escenario.
- Sin auditoría de erosión ni verificación de propiedad de datos.
- Sin dependencias nuevas que verificar en el periodo.
- Sin ADR sobre el componente generativo.
- Sin SonarCloud (configuración, run y URL pública con Quality Gate), pendiente desde S6.
- ADR-0001 (`07b36f4`) y ADR-0003 (`9ee88c5`) editados después de aceptarse sin declarar reemplazo.
- Angel Fabian Gutierrez Gomez sin commits atribuibles.

## Recuento y nota sugerida

**1 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

Bajo CONTRATO §12, el único criterio que se resuelve sobre el estado en la punta es el barrido de
credenciales; las demás filas describen la entrega S9, cuyo periodo (`e5c3ac6..origin/main`) está
vacío: la evidencia previa es línea base y no se recalifica por existir.

## No verificado / pendientes

- Prueba que falla ante el defecto: **No verificado**. No hay run en rojo, prueba de mutación ni
  procedimiento documentado del periodo S9; el run en rojo citado en ADR-0003 es de S8. Queda como
  pregunta de sustentación.
- Medición de escenarios: la columna Evidencia de `docs/aspectos.md` está en «Pendiente» para EC-01…EC-04.
- Auditoría de erosión: no existe artefacto que la documente.
- Dependencias del periodo: el diff contra S8 está vacío, no hay nada que comprobar en los registros.
- Componente generativo: no hay componente ni ADR de no incorporarlo.

## Hallazgos para la planilla

- La punta de `origin/main` (`e5c3ac6`, 2026-09-27) es idéntica al hash calificado de S8: el periodo S9 está vacío.
- Aplicado CONTRATO §12: sin artefacto del periodo, las filas 1, 3 y 6 pasan de Cumple a No cumple y la fila 4 de Cumple a No verificado; solo el barrido de credenciales queda en Cumple.
- `docs/aspectos.md` mantiene Pruebas «(pendiente)» y Evidencia «Pendiente» en los cuatro escenarios: la cadena no llega a prueba ni a medición.
- La prueba de contrato demuestra fallo controlado en S8: run histórico en rojo [35549974182](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/35549974182) citado en ADR-0003; no es evidencia del periodo S9.
- CI del hash revisado en verde (run 36355303177), pero sin SonarCloud ni Quality Gate.
- ADR-0001 y ADR-0003 editados después de aceptarse sin declarar reemplazo (fila transversal en No cumple).
- Contribución: un integrante declarado sin commits atribuibles.
- Sin auditoría de erosión y sin decisión sobre el componente generativo, exigidas por la evidencia S9.
