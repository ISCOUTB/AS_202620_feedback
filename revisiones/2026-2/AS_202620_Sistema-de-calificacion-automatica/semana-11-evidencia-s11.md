# AS_202620_Sistema-de-calificacion-automatica · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/tree/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado:** S11 definitiva al cierre indicado; nota propuesta para decisión docente.
**Repositorio público:** https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica
**Rama principal:** origin/master
**Commit evaluado:** `98a9dcc8f22c77ac5d0dfcea4055865e7727a21e` (2026-10-18T22:40:44-05:00)
**Enlace inmutable:** https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/tree/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e
**Cierre S11 exclusivo:** 2026-10-19T05:00:00Z (19 de octubre, 00:00 Colombia).
**Observación S12:** 2026-10-19T21:35:00Z (19 de octubre, 16:35 Colombia).
**Actividad:** 31 commits principales en intervalo S11 [2026-10-12T05:00Z, 2026-10-19T05:00Z); 0 después del cierre y hasta observación. No son conteos de personas ni una rúbrica de volumen.

## Alcance y método

Selección por fecha de commit en la rama principal remota; no por tags, ramas de PR ni archivos de Moodle. Inspección estática de documentación y código en clon efímero público, y consulta pública de resultados de GitHub Actions. No se ejecutó código, tests, contenedores ni scripts del equipo; no se abrieron PDFs ni se consultaron datos personales reales. Las rutas y líneas de las matrices corresponden al hash indicado; la nota no suma la matriz transversal.

## Matriz semanal (9 criterios)

| # | Criterio | Estado | Evidencia técnica | Observación y límite |
|---|---|---|---|---|
| 1 | Integración principal identificada en código | Cumple | `docs/evidencia/modos-de-fallo.md:25-29; backend/infraestructura/cola.py:102-152` | API→Redis→worker principal; LLM y navegador como integraciones adicionales. |
| 2 | Tabla de modos de fallo: no responde, tarde, duplicado | Cumple | [docs/evidencia/modos-de-fallo.md:46-58](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/evidencia/modos-de-fallo.md#L46-L58) | Tabla completa de modos, con pérdida tras BLPOP y límites temporales. |
| 3 | Mitigación explícita para cada modo | Cumple | [docs/evidencia/modos-de-fallo.md:84-94](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/evidencia/modos-de-fallo.md#L84-L94) | Mitigaciones construidas y pendientes separadas; no se exige Streams/XACK ahora. |
| 4 | Mitigaciones coherentes con implementación o pendientes declarados | Cumple | `backend/infraestructura/cola.py:48-50,74-90,120-152; backend/worker/main.py:54-95; docs/evidencia/modos-de-fallo.md:158-174` | Timeouts por rol, SET NX EX y fail-open existen. Deduplicación por 7 días y pérdida tras consumo no son exactly-once. |
| 5 | Idempotencia/saga diseñada o inaplicabilidad argumentada | Cumple | [docs/evidencia/modos-de-fallo.md:101-154](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/evidencia/modos-de-fallo.md#L101-L154) | Dedup worker actual y diseño de duplicado de carga pendiente; no saga distribuida justificado. |
| 6 | ADR evalúa extracción con criterios | Cumple | [docs/adr/0017-no-extraer-ningun-modulo-del-monolito-todavia.md:52-100](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/adr/0017-no-extraer-ningun-modulo-del-monolito-todavia.md#L52-L100) | Cuatro alternativas y criterios concretos; costo, almacenamiento, despliegue y medición. |
| 7 | No extraer como alternativa explícita | Cumple | [docs/adr/0017-no-extraer-ningun-modulo-del-monolito-todavia.md:88-100](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/adr/0017-no-extraer-ningun-modulo-del-monolito-todavia.md#L88-L100) | No extraer ahora explícito, con umbrales para revisión. |
| 8 | arc42 §11 actualizado | Cumple | [docs/arc42/arc42-template-ES.md:1756-1787](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/arc42/arc42-template-ES.md#L1756-L1787) | Riesgos R22–R25 y mitigaciones; reconoce worker sin acuse y efectos de premarcar. |
| 9 | Aspectos actualizados con trazabilidad | Cumple | [docs/aspectos.md:315-338](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/aspectos.md#L315-L338) | Cadena de aspecto, integración, pruebas y ADR actualizada. |

**Recuento: 9/9. Nota propuesta: 5.0/5.0**, mediante 1 + 4 × (9/9). Propuesta al docente, quien fija la nota final en Moodle.

## Matriz transversal del CONTRATO (9 criterios)

| # | Criterio | Estado | Evidencia y límites |
|---|---|---|---|
| 1 | Identidad, convención y visibilidad | Cumple | https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica; clon público sin autenticación y consulta pública actions/runs HTTP 200. |
| 2 | Estructura mínima | Cumple | `git ls-tree -r --name-only 98a9dcc8f22c77ac5d0dfcea4055865e7727a21e`: README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. |
| 3 | Estado calificado identificable | Cumple | origin/master, `98a9dcc8f22c77ac5d0dfcea4055865e7727a21e`, fecha 2026-10-18T22:40:44-05:00; selección anterior al cierre S11 o a observación S12, respectivamente. |
| 4 | Nombres de ADR | Cumple | Listado `docs/adr/` en 98a9dcc8f22c sin archivos fuera de NNNN-titulo-en-kebab-case.md. |
| 5 | ADR aceptados no reescritos | No verificado | No se completó contraste histórico de cada ADR con su estado de aceptación; no se infiere inmutabilidad del nombre correcto. |
| 6 | Registro IA al día | Cumple | [docs/ia.md:305-337](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/ia.md#L305-L337); entrada S11 con aceptaciones y rechazos técnicos, commit anterior al cierre dentro del periodo. |
| 7 | CI, scanner y Quality Gate públicos | No cumple | .github/workflows/ci.yml:1-77 no invoca scanner SonarCloud; falta la terna pública requerida. Runs concretos en sección siguiente. |
| 8 | Sin secretos actuales e históricos | No verificado | Barrido estático de firmas de alta confianza en `98a9dcc8f22c77ac5d0dfcea4055865e7727a21e` sin coincidencias de credenciales típicas. No se completó barrido de todo el historial y todas las formas de secretos: no se certifica ausencia. No se reproducen valores. |
| 9 | Aporte de todos los integrantes | No verificado | Historial principal y 31 commits S11 inspeccionados; no se completó consolidación persona↔alias↔padrón y membresía para todos. Un commit o cuenta no equivale a una persona. No se publican identidades. |

## CI citable y evidencia de ejecución

- CI: **success**, https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/39195829181.
- Workflow .github/workflows/ci.yml:52-60 incluye pruebas S11 y suite; no se ejecutó software del equipo en la auditoría.
- Un run global verde acredita el workflow reportado, no cada escenario descrito, una prueba en producción ni un scanner ausente. No se inventan logs de jobs ni ejecuciones propias.

## Overall: coherencia, producto y límites

- S11 completa con límites honestos: API 2 s, socket worker 10 s, BLPOP 5 s, marca NX 7 días y sin retry oculto.
- Worker actualmente consume y registra, no ejecuta OMR/calificación; PostgreSQL está previsto sin uso por esos componentes. C4 lo declara en tabla aunque las cajas puedan parecer producto terminado.
- Los archivos de medición y pruebas son evidencia del equipo; esta auditoría solo inspeccionó código/configuración y resultados CI públicos, sin ejecutar suites.
- R22/R23 reconocen pérdida después de BLPOP o de marcar visto antes del procesamiento; el plan futuro es válido para S11, no garantía de entrega durable hoy.

## Qué cerrar a continuación

- Mantener trazabilidad de las mitigaciones pendientes y añadir pruebas antes de presentarlas como garantías operativas.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
