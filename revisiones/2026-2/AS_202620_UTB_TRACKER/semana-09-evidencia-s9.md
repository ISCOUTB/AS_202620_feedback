> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · UTB Tracker

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` (redirige a `AS_202620_UTB_TRACKER`) |
| Estado revisado | `ae526db29b4f2d1f5981536e18438f9a62b1516d` en `origin/main` (2026-09-25T11:36:43-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

La punta actual de `origin/main` **es idéntica al hash calificado de S8** (`ae526db`, 2026-09-25):
el periodo S9 (`ae526db..origin/main`) está **vacío**, el equipo no empujó ninguna porción nueva.
Esta pasada **no tiene corte**: se califica la punta actual del 2026-10-01. Bajo CONTRATO §12 la
evidencia previa es línea base y **no se recalifica por existir**: las filas de la entrega S9 quedan
en No cumple (o No verificado) por ausencia de artefacto del periodo. La fila de credenciales y la
matriz transversal se deciden sobre el estado en la punta.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | Contexto (semanas anteriores): `docs/ia.md` (2026-08-16) registra el uso de Claude para estructura y redacción; código del esqueleto Django en `app/`. | No cumple | El periodo S9 (`ae526db..origin/main`) no tiene commits: no hay porción nueva construida en esta evidencia. El artefacto citado es de S2: línea base (CONTRATO §12). |
| Cadena completa navegable para esa porción | `docs/aspectos.md` describe `A-01`…`A-04` con varias columnas en `—`; el propio documento declara que faltan ADRs, código y pruebas. | No cumple | La cadena no llega a evidencia y no se tocó en el periodo; no satisface la fila S9. |
| ADR con la decisión argumentada por el equipo | Contexto (semanas anteriores): `docs/adr/0001-estilo-arquitectonico.md`, `0002-cambio-stack-fastapi-flutter.md` y `0003-integracion-sincrona.md`. | No cumple | No hay ADR del periodo S9; los citados son de S3/S4/S7 (línea base, CONTRATO §12). |
| Prueba que falla ante el defecto que cubre | No hay run en rojo, prueba de mutación ni procedimiento documentado del periodo en `docs/`. | No verificado | No se encontró evidencia del periodo; queda como pregunta para la sustentación (CONTRATO §13). |
| Medición del escenario asociado | No hay documento de medición ni resultado contrastado con umbral en el periodo. | No cumple | Sin medición de escenario publicada en la punta. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | El último commit sobre `docs/ia.md` es `e84871f` (2026-08-16); contiene dos filas de uso sin columna de rechazo. | No cumple | No hay extracto del periodo S9 y la evidencia histórica no documenta lo rechazado con motivo. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | El barrido `erosión\|límite de contexto\|propiedad de datos` no devuelve coincidencias en `docs/`. | No cumple | No hay auditoría de erosión del periodo. |
| Dependencias propuestas verificadas en su registro oficial | El diff del periodo contra el hash de S8 está vacío; `requirements.txt` existe pero sin cambios en el periodo. | No cumple | Sin dependencias nuevas respecto de S8; no hay lista ni comprobación en npm/PyPI que citar. |
| Sin credenciales en código, ejemplos ni documentación generada | `git grep` §9 sobre `ae526db` sin coincidencias; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` y `-S'AKIA'` sin resultados. | Cumple | Barrido limpio. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No hay componente generativo en el sistema ni un ADR que decida no incorporarlo; el barrido `generativ\|LLM\|openai\|gemini` no devuelve coincidencias en `docs/`. | No cumple | La ausencia de decisión no es la decisión de no hacerlo; falta el ADR que lo justifique si esa es la posición del equipo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | El clon sin autenticación de `ISCOUTB/AS_202620_TRACTAR` responde y redirige a `AS_202620_UTB_TRACKER`. | Cumple | Conserva el patrón `AS_202620_<PROYECTO>` y es público; `EQUIPOS.md` aún registra el nombre corto anterior. |
| Estructura mínima presente | En `ae526db`: `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Las seis rutas están presentes; arc42 vive en un único `arc42.md`. |
| Estado calificado identificable | `origin/main`, `ae526db29b4f2d1f5981536e18438f9a62b1516d`, 2026-09-25T11:36:43-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual. Coincide con el hash de S8. |
| Nombres de ADR según la convención | Tres ADR con nombres `NNNN-titulo-en-kebab-case.md`; el filtro de la convención no devuelve salida. | Cumple | — |
| ADR aceptados no reescritos | `git log --follow` de cada ADR en `ae526db` muestra un solo commit (el de creación): `5f923cd`, `e88a3d6`, `9cf1ac9`. | Cumple | No hay ediciones posteriores a la aceptación. |
| `docs/ia.md` al día para la semana | Último commit sobre el archivo: `e84871f`, 2026-08-16. Sin entradas del periodo S9. | No cumple | El registro no crece desde agosto y no documenta nada descartado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Único run del hash revisado: `UTB Tracker CI` `36161882569` en `main`, conclusión `failure`; no hay `sonar-project.properties` ni paso del scanner. | No cumple | Un pipeline en rojo es no conformidad; no se compensa con que el workflow haya arrancado. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de credenciales en `ae526db` sin coincidencias; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin resultados. | Cumple | Barrido limpio. |
| Contribución de todos los integrantes | `git shortlog -sne ae526db` consolidado por correo idéntico: Sebastián García Devoz (22, tres identidades del mismo correo) y Joriel Samir (3). | No cumple | Solo 2 de los 4 integrantes declarados aparecen; Gerónimo y Mateo no tienen commits. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `ae526db29b4f2d1f5981536e18438f9a62b1516d` 2026-09-25T11:36:43-05:00 `hotfix` (`origin/main`)
- **Veredicto**: sin trabajo nuevo de S9; pipeline en rojo y deudas de S8 abiertas
- Resumen: la punta de `main` coincide con el estado calificado de S8, así que no hay entregas
  nuevas. Los tres commits del 25 de septiembre (`dc4099d`, `6d7300c`, `ae526db`) añadieron un paso
  de despliegue por SSH al workflow y cambiaron la base de datos a `DATABASE_URL`, pero no
  versionaron infraestructura ni documentación S9; dejaron el pipeline en rojo. Sigue sin existir la
  URL pública, la IaC, los logs estructurados, la métrica con escenario, el documento de costos, la
  sección 2/7 del arc42 con límite de costo y un ADR de plataforma. `docs/ia.md` no crece desde
  agosto. La entrega S9 no existe en esta punta.

Pendientes que siguen abiertos:
- Sin commits de S9: la punta es la de S8.
- Pipeline en rojo: run `36161882569` de `UTB Tracker CI` en `main`.
- Sin porción S9, sin prueba del periodo y sin extracto de `docs/ia.md` del periodo.
- Sin medición de escenario, sin auditoría de erosión y sin ADR de no incorporar componente generativo.
- URL pública, IaC, logs, métrica, costo, arc42 §2/§7 y ADR de plataforma: sin resolver.
- Análisis estático en SonarCloud con URL pública y Quality Gate.
- Dos de los cuatro integrantes declarados sin commits en el historial.

## Recuento y nota sugerida

**1 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

Bajo CONTRATO §12, el único criterio que se resuelve sobre el estado en la punta es el barrido de
credenciales; las demás filas describen la entrega S9, cuyo periodo (`ae526db..origin/main`) está
vacío: la evidencia previa es línea base y no se recalifica por existir.

## No verificado / pendientes

- Prueba que falla ante el defecto: **No verificado**. No hay run en rojo, prueba de mutación ni
  procedimiento documentado del periodo S9. Queda como pregunta de sustentación.
- Medición de escenarios: no existe medición del periodo.
- Auditoría de erosión: no existe artefacto que la documente.
- Dependencias del periodo: el diff contra S8 está vacío.
- Componente generativo: no hay componente ni ADR de no incorporarlo.

## Hallazgos para la planilla

- La punta de `main` (`ae526db`, 2026-09-25) es idéntica al hash calificado de S8: el periodo S9 está vacío.
- El pipeline quedó en rojo (`runs/36161882569`); no se corrigió en el periodo.
- `docs/ia.md` no crece desde 2026-08-16 y no registra rechazos con motivo.
- Sin medición, sin auditoría de erosión y sin decisión sobre componente generativo.
- Dos de los cuatro integrantes declarados siguen sin commits en el historial.
- El repositorio fue renombrado a `AS_202620_UTB_TRACKER`; `EQUIPOS.md` aún lista el nombre corto anterior.
