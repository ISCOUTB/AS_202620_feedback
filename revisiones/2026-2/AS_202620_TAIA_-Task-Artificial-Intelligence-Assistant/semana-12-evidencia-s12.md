# AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/tree/eb4d915c00024c8e7c5c03536a0d979a9c0a88f6) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado:** S12 PRELIMINAR, avance observado; NO cierre ni nota definitiva.
**Repositorio público:** https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant
**Rama principal:** origin/main
**Commit evaluado:** `eb4d915c00024c8e7c5c03536a0d979a9c0a88f6` (2026-10-19T14:12:09-05:00)
**Enlace inmutable:** https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/tree/eb4d915c00024c8e7c5c03536a0d979a9c0a88f6
**Cierre S11 exclusivo:** 2026-10-19T05:00:00Z (19 de octubre, 00:00 Colombia).
**Observación S12:** 2026-10-19T21:35:00Z (19 de octubre, 16:35 Colombia).
**Actividad:** 24 commits principales en intervalo S11 [2026-10-12T05:00Z, 2026-10-19T05:00Z); 1 después del cierre y hasta observación. No son conteos de personas ni una rúbrica de volumen.

## Alcance y método

Selección por fecha de commit en la rama principal remota; no por tags, ramas de PR ni archivos de Moodle. Inspección estática de documentación y código en clon efímero público, y consulta pública de resultados de GitHub Actions. No se ejecutó código, tests, contenedores ni scripts del equipo; no se abrieron PDFs ni se consultaron datos personales reales. Las rutas y líneas de las matrices corresponden al hash indicado; la nota no suma la matriz transversal.

## Matriz semanal (9 criterios)

| # | Criterio | Estado | Evidencia técnica | Observación y límite |
|---|---|---|---|---|
| 1 | Tabla operación→garantía de consistencia real | No cumple | `docs/arc42/08-conceptos-transversales.md:1-170; docs/modos_fallo_s11.md:95-221` | No tabla operación→garantía fuerte/eventual/nombrada. |
| 2 | Dos operaciones contrastadas con implementación | Cumple | `backend/app/modules/ai/adapters/outbound/sqlalchemy_conversation_store.py:54-75; backend/app/modules/reminders/adapters/outbound/sqlalchemy_reminder_repository.py:63-89; docs/modos_fallo_s11.md:95-193` | Reclamar confirmación y crear notificación usan transacciones y bloqueo del registro correspondiente. No son transacción única con escribir tarea o enviar Telegram. |
| 3 | Diseño de caché: qué/dónde/cuánto | No cumple | [docs/arc42/08-conceptos-transversales.md:1-170](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/eb4d915c00024c8e7c5c03536a0d979a9c0a88f6/docs/arc42/08-conceptos-transversales.md#L1-L170) | No diseño de caché de lectura ni justificación de no necesitarla. Expiración de pending_action es una regla funcional, no este diseño. |
| 4 | Política de invalidación tras escritura | No cumple | [docs/arc42/08-conceptos-transversales.md:1-170](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/eb4d915c00024c8e7c5c03536a0d979a9c0a88f6/docs/arc42/08-conceptos-transversales.md#L1-L170) | Falta política tras editar/completar tareas; no se afirma una caché implementada ni un fallo observado. |
| 5 | Garantías y supuestos de eventos, si existen | Cumple | [docs/modos_fallo_s11.md:203-221](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/eb4d915c00024c8e7c5c03536a0d979a9c0a88f6/docs/modos_fallo_s11.md#L203-L221) | Monolito con persistencia local y llamadas síncronas; no flujo con broker actual que requiera ack/reentrega. Propuesta futura de avisos no se acredita como entrega garantizada. |
| 6 | ADR de decisión de datos más costosa de revertir | No cumple | [docs/adr/0008-mantener-monolito-sin-extraer-modulos.md:42-140](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/eb4d915c00024c8e7c5c03536a0d979a9c0a88f6/docs/adr/0008-mantener-monolito-sin-extraer-modulos.md#L42-L140) | ADR de no extracción no selecciona la decisión de datos más costosa de revertir. |
| 7 | Argumento y costo comparativo de reversión | No cumple | [docs/adr/0008-mantener-monolito-sin-extraer-modulos.md:98-140](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/eb4d915c00024c8e7c5c03536a0d979a9c0a88f6/docs/adr/0008-mantener-monolito-sin-extraer-modulos.md#L98-L140) | Falta comparación y costo de reversión de esa elección de datos. |
| 8 | C4 nivel 2 con almacenes/brokers y tecnología | No cumple | [docs/c4/C4-C2.md:21](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/eb4d915c00024c8e7c5c03536a0d979a9c0a88f6/docs/c4/C4-C2.md#L21) | El contenedor de base de datos no anota tecnología PostgreSQL en este nivel. Debe actualizarse, no inferirse de CI o del repositorio SQL. |
| 9 | arc42 §8 con consistencia y caché | No cumple | [docs/arc42/08-conceptos-transversales.md:1-170](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/eb4d915c00024c8e7c5c03536a0d979a9c0a88f6/docs/arc42/08-conceptos-transversales.md#L1-L170) | §8 no consolida consistencia y caché. |

**Recuento: 2/9. Nota propuesta: 1.9/5.0**, mediante 1 + 4 × (2/9). Solo diagnóstico PRELIMINAR; no sustituye evaluación al cierre de S12.

## Matriz transversal del CONTRATO (9 criterios)

| # | Criterio | Estado | Evidencia y límites |
|---|---|---|---|
| 1 | Identidad, convención y visibilidad | Cumple | https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant; clon público sin autenticación y consulta pública actions/runs HTTP 200. |
| 2 | Estructura mínima | Cumple | `git ls-tree -r --name-only eb4d915c00024c8e7c5c03536a0d979a9c0a88f6`: README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. |
| 3 | Estado calificado identificable | Cumple | origin/main, `eb4d915c00024c8e7c5c03536a0d979a9c0a88f6`, fecha 2026-10-19T14:12:09-05:00; selección anterior al cierre S11 o a observación S12, respectivamente. |
| 4 | Nombres de ADR | Cumple | Listado `docs/adr/` en eb4d915c0002 sin archivos fuera de NNNN-titulo-en-kebab-case.md. |
| 5 | ADR aceptados no reescritos | No cumple | docs/ia.md:964-995 declara actualización de ADR-0003 existente para cambiar decisión de despliegue, sin ADR sucesor; debe preservarse la decisión aceptada y enlazar reemplazo. |
| 6 | Registro IA al día | No cumple | [docs/ia.md:816-995](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/eb4d915c00024c8e7c5c03536a0d979a9c0a88f6/docs/ia.md#L816-L995); registro hasta S11; no actualización del registro durante ventana S12. El contenido anticipado se reconoce en la matriz semanal, sin inventar una nueva entrada. |
| 7 | CI, scanner y Quality Gate públicos | No cumple | .github/workflows/ci.yml:1-120 incluye pytest y controles propios, pero no scanner ni Quality Gate SonarCloud verificable. Runs concretos en sección siguiente. |
| 8 | Sin secretos actuales e históricos | No verificado | Barrido estático de firmas de alta confianza en `eb4d915c00024c8e7c5c03536a0d979a9c0a88f6` sin coincidencias de credenciales típicas. No se completó barrido de todo el historial y todas las formas de secretos: no se certifica ausencia. No se reproducen valores. |
| 9 | Aporte de todos los integrantes | No verificado | Historial principal y 24 commits S11 inspeccionados; no se completó consolidación persona↔alias↔padrón y membresía para todos. Un commit o cuenta no equivale a una persona. No se publican identidades. |

## CI citable y evidencia de ejecución

- CI S11: **success**, https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39164635628.
- CD S11: **success**, https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39164766522.
- CI actual: **success**, https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39308975710.
- CD actual: **success**, https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39309238475.
- CI usa PostgreSQL 17 en pruebas; no basta para fechar/verificar la versión de producción. Runs actuales corresponden al hash posterior solo para avance.
- Un run global verde acredita el workflow reportado, no cada escenario descrito, una prueba en producción ni un scanner ausente. No se inventan logs de jobs ni ejecuciones propias.

## Overall: coherencia, producto y límites

- La idempotencia de confirmación sí está implementada antes del corte y tiene pruebas concurrentes declaradas. La entrada IA anterior que la decía pendiente fue superada por la entrada 019.
- El reclamo de acción se confirma antes de escribir la tarea: se acepta explícitamente pérdida ante ese segundo fallo. No equivale a una transacción integral.
- Enviar notificaciones con push_sent_at/reintentos sigue pendiente según evidencia; crear su registro idempotentemente no garantiza el envío una sola vez.
- Único commit principal posterior al cierre cambia backend/Dockerfile; no completa artefactos S12. CD verde no comprueba revisión final desplegada ni disponibilidad real.

## Qué cerrar a continuación

- No tabla operación→garantía fuerte/eventual/nombrada.
- No diseño de caché de lectura ni justificación de no necesitarla. Expiración de pending_action es una regla funcional, no este diseño.
- Falta política tras editar/completar tareas; no se afirma una caché implementada ni un fallo observado.
- ADR de no extracción no selecciona la decisión de datos más costosa de revertir.
- Falta comparación y costo de reversión de esa elección de datos.
- El contenedor de base de datos no anota tecnología PostgreSQL en este nivel. Debe actualizarse, no inferirse de CI o del repositorio SQL.
- §8 no consolida consistencia y caché.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
