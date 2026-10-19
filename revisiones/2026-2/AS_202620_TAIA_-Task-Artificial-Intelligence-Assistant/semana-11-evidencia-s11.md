# AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/tree/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado:** S11 definitiva al cierre indicado; nota propuesta para decisión docente.
**Repositorio público:** https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant
**Rama principal:** origin/main
**Commit evaluado:** `e755759bd80ef94ffe809cc6ceee0c1d2a0044c6` (2026-10-18T15:43:53-05:00)
**Enlace inmutable:** https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/tree/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6
**Cierre S11 exclusivo:** 2026-10-19T05:00:00Z (19 de octubre, 00:00 Colombia).
**Observación S12:** 2026-10-19T21:35:00Z (19 de octubre, 16:35 Colombia).
**Actividad:** 24 commits principales en intervalo S11 [2026-10-12T05:00Z, 2026-10-19T05:00Z); 1 después del cierre y hasta observación. No son conteos de personas ni una rúbrica de volumen.

## Alcance y método

Selección por fecha de commit en la rama principal remota; no por tags, ramas de PR ni archivos de Moodle. Inspección estática de documentación y código en clon efímero público, y consulta pública de resultados de GitHub Actions. No se ejecutó código, tests, contenedores ni scripts del equipo; no se abrieron PDFs ni se consultaron datos personales reales. Las rutas y líneas de las matrices corresponden al hash indicado; la nota no suma la matriz transversal.

## Matriz semanal (9 criterios)

| # | Criterio | Estado | Evidencia técnica | Observación y límite |
|---|---|---|---|---|
| 1 | Integración principal identificada en código | Cumple | `docs/modos_fallo_s11.md:13-22; backend/app/modules/ai/adapters/outbound/gemini_llm.py:95-108,154-180` | Gemini es integración principal del caso conversacional, por adaptador HTTP. |
| 2 | Tabla de modos de fallo: no responde, tarde, duplicado | Cumple | [docs/modos_fallo_s11.md:31-36,61-63](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/docs/modos_fallo_s11.md#L31-L36) | No respuesta, demora y duplicado; distingue Telegram secundario. |
| 3 | Mitigación explícita para cada modo | Cumple | [docs/modos_fallo_s11.md:69-85](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/docs/modos_fallo_s11.md#L69-L85) | Timeout y recuperación frente a Gemini; pendientes de Telegram declarados con diseño. |
| 4 | Mitigaciones coherentes con implementación o pendientes declarados | Cumple | `backend/app/modules/ai/adapters/outbound/sqlalchemy_conversation_store.py:54-75; docs/modos_fallo_s11.md:95-165` | Reclamo FOR UPDATE corta la doble confirmación; pérdida si falla escritura posterior está declarada. No se atribuye idempotencia de envío Telegram. |
| 5 | Idempotencia/saga diseñada o inaplicabilidad argumentada | Cumple | [docs/modos_fallo_s11.md:95-165,169-221](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/docs/modos_fallo_s11.md#L95-L165) | Diseño e implementación de reclamo; notificación pendiente y saga distribuida no aplicable hoy con argumento. |
| 6 | ADR evalúa extracción con criterios | Cumple | [docs/adr/0008-mantener-monolito-sin-extraer-modulos.md:42-100](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/docs/adr/0008-mantener-monolito-sin-extraer-modulos.md#L42-L100) | Compara módulos candidatos y criterios técnicos/operativos. |
| 7 | No extraer como alternativa explícita | Cumple | [docs/adr/0008-mantener-monolito-sin-extraer-modulos.md:53-100](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/docs/adr/0008-mantener-monolito-sin-extraer-modulos.md#L53-L100) | No extraer explícito y elegido, con condiciones para reevaluar. |
| 8 | arc42 §11 actualizado | Cumple | [docs/arc42/11-riesgos-y-deudas-tecnicas.md:139-162](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/docs/arc42/11-riesgos-y-deudas-tecnicas.md#L139-L162) | Fallos parciales y mitigaciones pendientes consignados. |
| 9 | Aspectos actualizados con trazabilidad | Cumple | [docs/aspectos.md:19-21](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/docs/aspectos.md#L19-L21) | Trazabilidad de A03/A04/A05 a evidencia y código. |

**Recuento: 9/9. Nota propuesta: 5.0/5.0**, mediante 1 + 4 × (9/9). Propuesta al docente, quien fija la nota final en Moodle.

## Matriz transversal del CONTRATO (9 criterios)

| # | Criterio | Estado | Evidencia y límites |
|---|---|---|---|
| 1 | Identidad, convención y visibilidad | Cumple | https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant; clon público sin autenticación y consulta pública actions/runs HTTP 200. |
| 2 | Estructura mínima | Cumple | `git ls-tree -r --name-only e755759bd80ef94ffe809cc6ceee0c1d2a0044c6`: README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. |
| 3 | Estado calificado identificable | Cumple | origin/main, `e755759bd80ef94ffe809cc6ceee0c1d2a0044c6`, fecha 2026-10-18T15:43:53-05:00; selección anterior al cierre S11 o a observación S12, respectivamente. |
| 4 | Nombres de ADR | Cumple | Listado `docs/adr/` en e755759bd80e sin archivos fuera de NNNN-titulo-en-kebab-case.md. |
| 5 | ADR aceptados no reescritos | No cumple | docs/ia.md:964-995 declara actualización de ADR-0003 existente para cambiar decisión de despliegue, sin ADR sucesor; debe preservarse la decisión aceptada y enlazar reemplazo. |
| 6 | Registro IA al día | Cumple | [docs/ia.md:816-995](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/e755759bd80ef94ffe809cc6ceee0c1d2a0044c6/docs/ia.md#L816-L995); entrada S11 con aceptaciones y rechazos técnicos, commit anterior al cierre dentro del periodo. |
| 7 | CI, scanner y Quality Gate públicos | No cumple | .github/workflows/ci.yml:1-120 incluye pytest y controles propios, pero no scanner ni Quality Gate SonarCloud verificable. Runs concretos en sección siguiente. |
| 8 | Sin secretos actuales e históricos | No verificado | Barrido estático de firmas de alta confianza en `e755759bd80ef94ffe809cc6ceee0c1d2a0044c6` sin coincidencias de credenciales típicas. No se completó barrido de todo el historial y todas las formas de secretos: no se certifica ausencia. No se reproducen valores. |
| 9 | Aporte de todos los integrantes | No verificado | Historial principal y 24 commits S11 inspeccionados; no se completó consolidación persona↔alias↔padrón y membresía para todos. Un commit o cuenta no equivale a una persona. No se publican identidades. |

## CI citable y evidencia de ejecución

- CI S11: **success**, https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39164635628.
- CD S11: **success**, https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39164766522.
- CI usa PostgreSQL 17 en pruebas; no basta para fechar/verificar la versión de producción. Runs actuales corresponden al hash posterior solo para avance.
- Un run global verde acredita el workflow reportado, no cada escenario descrito, una prueba en producción ni un scanner ausente. No se inventan logs de jobs ni ejecuciones propias.

## Overall: coherencia, producto y límites

- La idempotencia de confirmación sí está implementada antes del corte y tiene pruebas concurrentes declaradas. La entrada IA anterior que la decía pendiente fue superada por la entrada 019.
- El reclamo de acción se confirma antes de escribir la tarea: se acepta explícitamente pérdida ante ese segundo fallo. No equivale a una transacción integral.
- Enviar notificaciones con push_sent_at/reintentos sigue pendiente según evidencia; crear su registro idempotentemente no garantiza el envío una sola vez.
- Único commit principal posterior al cierre cambia backend/Dockerfile; no completa artefactos S12. CD verde no comprueba revisión final desplegada ni disponibilidad real.

## Qué cerrar a continuación

- Mantener trazabilidad de las mitigaciones pendientes y añadir pruebas antes de presentarlas como garantías operativas.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
