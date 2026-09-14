# Primer corte S5 · DinamikUTB

> Revisión definitiva actualizada manualmente. Se reemplazan las conclusiones automáticas que
> no inspeccionaron el contenido de los entregables. S5 es un compendio S1–S4: no evalúa un reto
> ni una restricción nueva.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado calificado | `origin/master` [`72bfc7e`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/tree/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7) · 2026-09-07T22:28:37-05:00 |
| Cierre | 2026-09-10T17:00:00Z (10 de septiembre, 12:00 COT) |
| Revisor | revisión manual de evidencias públicas |

## Matriz del corte

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | `origin/master` [`72bfc7e`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7) | Cumple | Es el último commit de la rama principal antes del cierre; no se usaron etiquetas. |
| `correcciones.md` existe en la raíz del estado calificado | [`correcciones.md`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/correcciones.md) | Cumple | Está en la raíz y responde explícitamente a los hallazgos S1–S4 y al preliminar de S5. |
| Correcciones trazables y contrastadas | [`correcciones.md:31-85`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/correcciones.md#L31-L85), evidencias enlazadas abajo | Cumple | Cada fila identifica hallazgo, acción, ruta y estado; se contrastaron las rutas de S1–S4. El encabezado cita `86870bf` como estado de trabajo, pero el hash final de corte y su CI propio son `72bfc7e`. |
| S1 al día: equipo, problema y repositorio | [`README.md:24-104`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/README.md#L24-L104), [`docs/fichadelproblema.md:15-61`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/fichadelproblema.md#L15-L61) | Cumple | Problema, usuarios, alcance, objetivos y las dos tensiones de calidad están documentados en Markdown. |
| S2 al día: escenarios de calidad y restricciones | [`10-quality-requirements.md:9-115`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/arc42/10-quality-requirements.md#L9-L115), [`02-architecture-constraints.md:7-143`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/arc42/02-architecture-constraints.md#L7-L143) | Cumple | Árbol de utilidad, escenarios medibles, herramienta/carga y restricciones técnicas, organizativas y legales son verificables. |
| S3 al día: estrategia de solución y decisiones | [`04-solution-strategy.md:41-63`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/arc42/04-solution-strategy.md#L41-L63), [`ADR 0001`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/adr/0001-seleccion-monolito-modular.md) | Cumple | Compara capas, hexagonal y monolito modular contra Q-01 a Q-03, y documenta tácticas por escenario. |
| S4 al día: arc42, C4 y corte vertical | [`05-building-block-view.md:7-95`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/arc42/05-building-block-view.md#L7-L95), [`06-runtime-view.md:8-29`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/arc42/06-runtime-view.md#L8-L29), [C4 nivel 1](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/c4/contexto.puml), [nivel 2](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/c4/contenedores.puml) | Cumple | Las secciones exigidas, C4 como código, glosario y el recorrido Flutter → FastAPI → SQLite están presentes y son coherentes. |
| Corte vertical reproducible y coherente con la arquitectura | [`README.md:168-258`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/README.md#L168-L258), [`start.bat`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/start.bat), [`router.py:8-13`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/backend/app/requisitos/router.py#L8-L13) | No verificado | Hay comando único, estructura y recorrido coherente, pero no se ejecutó `start.bat` en esta revisión y el run de CI no ejercita ese script de extremo a extremo. |
| Pipeline y pruebas respaldan el estado calificado | [`ci.yml`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/.github/workflows/ci.yml), [run verde de `72bfc7e`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/34183639965), [`test_requisitos.py:36-63`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/backend/tests/test_requisitos.py#L36-L63) | Cumple | El workflow ejecuta backend y frontend; el run asociado exactamente al hash calificado finalizó en verde. |
| Trazabilidad consolidada navegable | [`docs/aspectos.md:9-18`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/aspectos.md#L9-L18) | No cumple | A-01 está parcialmente trazado, pero A-02 a A-08 conservan enlaces o columnas en «Pendiente»; no existe todavía una cadena consolidada navegable para todos los aspectos. |
| PDF u otro adjunto exigido por el aula | Repositorio público | No verificado | La entrega de Moodle no es accesible desde el repositorio. |
| Sustentación del corte | Sesión docente | No verificado | La resuelve el docente en la sustentación. |

## Seguimiento de `correcciones.md`

| Origen | Hallazgo o fila | Evidencia contrastada | Resultado |
|---|---|---|---|
| S1 | Ficha en Markdown y dos tensiones | [`fichadelproblema.md`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/fichadelproblema.md), [`README.md:139-163`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/README.md#L139-L163) | Verificada |
| S2 | Escenarios navegables, herramienta/carga y registro de IA | [`aspects.md`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/aspectos.md), [`quality requirements`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/arc42/10-quality-requirements.md), [`ia.md`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/ia.md) | Verificada |
| S3 | Matriz contra escenarios, tácticas, ADR y CI | [`strategy`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/arc42/04-solution-strategy.md), [run CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/34183639965) | Verificada |
| S4 | Índice ADR, trazabilidad y C4/corte vertical | [`decisions`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/arc42/09-architecture-decisions.md), [`runtime`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/arc42/06-runtime-view.md) | Verificada |
| S5 | Trazabilidad A-02 a A-08 | [`docs/aspectos.md:12-18`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/aspectos.md#L12-L18) | Pendiente |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con nombre convencional y público | `ISCOUTB/AS_202620_DinamikUTB` | Cumple | Accesible públicamente y con nombre conforme. |
| Estructura mínima presente | Árbol de `72bfc7e` | Cumple | Incluye README, arc42, ADR, C4, aspectos e IA. |
| Estado calificado identificable | `origin/master` `72bfc7e` | Cumple | Rama principal y hash de corte reproducibles. |
| Nombres de ADR según la convención | `docs/adr/0001-*`, `0002-*`, `0003-*` | Cumple | Los tres nombres son numerados y kebab-case. |
| ADR aceptados no reescritos | Historial de ADR 0001 | No cumple | ADR 0001 tuvo una actualización posterior a su creación y aceptación (`15d38f9`, 1 de septiembre), sin ADR sucesor que la formalice. |
| `docs/ia.md` al día | [`docs/ia.md`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7/docs/ia.md) | Cumple | Registra herramienta, resultado y decisiones aceptadas o rechazadas. |
| Sin credenciales en repositorio ni historial revisado | Escaneo del hash calificado | Cumple | Sin coincidencias del patrón de secretos del contrato. |
| Contribución de todos los integrantes | `shortlog` del hash calificado | Cumple | Las cuatro identidades declaradas aparecen; persiste concentración de trabajo, ya registrada como observación. |

## Estado global del proyecto (overall · punta actual de `master`)

- **Punta actual:** `265e652` (2026-09-13T23:29:49-05:00).
- **Cambios posteriores al cierre:** trabajo de S6, ajustes de código y configuración de SonarCloud, incluidos cambios en `08-cross-cutting-concepts.md`, módulos de estudiantes y el workflow.
- **Efecto sobre S5:** ninguno. Son cambios tardíos para el corte y no alteran la matriz anterior.

## Recuento y nota sugerida

**8 de 12 criterios Cumple.**

**Nota sugerida: 3.7 = 1 + 4 × (8/12).** Es una propuesta al docente; la nota oficial la fija el docente en Moodle.

## Pendientes

- Completar las cadenas de trazabilidad pendientes en `docs/aspectos.md`.
- Verificar en un entorno desechable el arranque completo con `start.bat`.
- Verificar el PDF de Moodle y resolver la sustentación.
- Si ADR 0001 cambia después de su aceptación, conservarlo inmutable y registrar el cambio en un ADR nuevo.
