# AS_202620_ROUTB · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_ROUTB/tree/1bd9425e2675bd7531426b6e31e78546b3e55f2e) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado:** S12 PRELIMINAR, avance observado; NO cierre ni nota definitiva.
**Repositorio público:** https://github.com/ISCOUTB/AS_202620_ROUTB
**Rama principal:** origin/master
**Commit evaluado:** `1bd9425e2675bd7531426b6e31e78546b3e55f2e` (2026-10-18T16:39:27-05:00)
**Enlace inmutable:** https://github.com/ISCOUTB/AS_202620_ROUTB/tree/1bd9425e2675bd7531426b6e31e78546b3e55f2e
**Cierre S11 exclusivo:** 2026-10-19T05:00:00Z (19 de octubre, 00:00 Colombia).
**Observación S12:** 2026-10-19T21:35:00Z (19 de octubre, 16:35 Colombia).
**Actividad:** 2 commits principales en intervalo S11 [2026-10-12T05:00Z, 2026-10-19T05:00Z); 0 después del cierre y hasta observación. No son conteos de personas ni una rúbrica de volumen.

## Alcance y método

Selección por fecha de commit en la rama principal remota; no por tags, ramas de PR ni archivos de Moodle. Inspección estática de documentación y código en clon efímero público, y consulta pública de resultados de GitHub Actions. No se ejecutó código, tests, contenedores ni scripts del equipo; no se abrieron PDFs ni se consultaron datos personales reales. Las rutas y líneas de las matrices corresponden al hash indicado; la nota no suma la matriz transversal.

## Matriz semanal (9 criterios)

| # | Criterio | Estado | Evidencia técnica | Observación y límite |
|---|---|---|---|---|
| 1 | Tabla operación→garantía de consistencia real | No cumple | `docs/arc42/08_conceptos_transversales.md:22-28,92-109; docs/adr/0017-decision-extraccion-modulo-requests.md:17-68` | Hay afirmaciones ACID, pero no tabla operación→garantía para operaciones reales. |
| 2 | Dos operaciones contrastadas con implementación | Cumple | `backend/app/modules/requests/application/manage_request.py:31-147,152-206; docs/evidencia/resiliencia-y-modos-de-fallo.md:125-143` | Aceptar y rechazar usan cambios condicionados y commit; aceptación reserva cupos con control transaccional. Es evidencia local, no garantía sobre crear solicitud concurrente. |
| 3 | Diseño de caché: qué/dónde/cuánto | Cumple | `docs/adr/0010-geocodificacion-y-cache.md:25-27; backend/app/shared/geocode/service.py:41-70` | Caché de geocodificación normalizada en PostgreSQL, TTL 7 días configurado; lectura con expiración y upsert. |
| 4 | Política de invalidación tras escritura | No cumple | `docs/adr/0010-geocodificacion-y-cache.md:25-27; backend/app/shared/geocode/service.py:46-70,193-224` | TTL/upsert no explican invalidación por cambio de fuente, parámetros geográficos o escritura relevante. No es caché de cupos: no se inventa una reserva incorrecta por este caché. |
| 5 | Garantías y supuestos de eventos, si existen | Cumple | `docs/adr/0013-notificaciones-push-fcm.md:18-29; backend/app/modules/requests/application/manage_request.py:135-147` | Push posterior al commit, no bloqueante: best effort con REST como fuente de verdad y resincronización. No garantiza entrega exactamente una vez. |
| 6 | ADR de decisión de datos más costosa de revertir | No cumple | `docs/adr/0017-decision-extraccion-modulo-requests.md:17-68; docs/adr/0010-geocodificacion-y-cache.md:1-46` | Decisiones de extracción/geocodificación existentes no identifican la de datos más costosa de revertir. |
| 7 | Argumento y costo comparativo de reversión | No cumple | [docs/adr/0017-decision-extraccion-modulo-requests.md:61-68](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/adr/0017-decision-extraccion-modulo-requests.md#L61-L68) | Consecuencias generales, sin comparación de reversión de datos. |
| 8 | C4 nivel 2 con almacenes/brokers y tecnología | Cumple | [docs/c4/context.md:44-80](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/c4/context.md#L44-L80) | Nivel 2 separa PostgreSQL y servicios externos con tecnología. |
| 9 | arc42 §8 con consistencia y caché | No cumple | [docs/arc42/08_conceptos_transversales.md:22-28,92-109](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/arc42/08_conceptos_transversales.md#L22-L28) | Hay ACID y degradación con cache, no estrategia integrada de consistencia e invalidación. |

**Recuento: 4/9. Nota propuesta: 2.8/5.0**, mediante 1 + 4 × (4/9). Solo diagnóstico PRELIMINAR; no sustituye evaluación al cierre de S12.

## Matriz transversal del CONTRATO (9 criterios)

| # | Criterio | Estado | Evidencia y límites |
|---|---|---|---|
| 1 | Identidad, convención y visibilidad | Cumple | https://github.com/ISCOUTB/AS_202620_ROUTB; clon público sin autenticación y consulta pública actions/runs HTTP 200. |
| 2 | Estructura mínima | Cumple | `git ls-tree -r --name-only 1bd9425e2675bd7531426b6e31e78546b3e55f2e`: README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. |
| 3 | Estado calificado identificable | Cumple | origin/master, `1bd9425e2675bd7531426b6e31e78546b3e55f2e`, fecha 2026-10-18T16:39:27-05:00; selección anterior al cierre S11 o a observación S12, respectivamente. |
| 4 | Nombres de ADR | Cumple | Listado `docs/adr/` en 1bd9425e2675 sin archivos fuera de NNNN-titulo-en-kebab-case.md. |
| 5 | ADR aceptados no reescritos | No verificado | Historial de todos los ADR aceptados no contrastado íntegramente contra su primera aceptación; no se certifica inmutabilidad por un solo log. |
| 6 | Registro IA al día | No cumple | [docs/ia.md:146-162](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/ia.md#L146-L162); registro hasta S11; no actualización del registro durante ventana S12. El contenido anticipado se reconoce en la matriz semanal, sin inventar una nueva entrada. |
| 7 | CI, scanner y Quality Gate públicos | No cumple | .github/workflows/ci.yml:78-83 imprime un marcador Sonar; no invoca scanner real ni acredita Quality Gate público. Runs concretos en sección siguiente. |
| 8 | Sin secretos actuales e históricos | No verificado | Barrido estático de firmas de alta confianza en `1bd9425e2675bd7531426b6e31e78546b3e55f2e` sin coincidencias de credenciales típicas. No se completó barrido de todo el historial y todas las formas de secretos: no se certifica ausencia. No se reproducen valores. |
| 9 | Aporte de todos los integrantes | No verificado | Historial principal y 2 commits S11 inspeccionados; no se completó consolidación persona↔alias↔padrón y membresía para todos. Un commit o cuenta no equivale a una persona. No se publican identidades. |

## CI citable y evidencia de ejecución

- CI ROUTB: **success**, https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39168805661.
- Run exitoso de la rama y hash evaluados; no equivale a verificación manual del despliegue.
- Un run global verde acredita el workflow reportado, no cada escenario descrito, una prueba en producción ni un scanner ausente. No se inventan logs de jobs ni ejecuciones propias.

## Overall: coherencia, producto y límites

- PR 51 está antes del cierre. Los planes 2027 de mitigación se reconocen como planes; no se exige implementarlos todos para S11.
- La carrera de creación concurrente es un hallazgo de inspección estática, no una falla reproducida en esta revisión.
- Persiste un riesgo de privacidad de la línea base: backend/app/modules/trips/infrastructure/router.py:32-50,99-114,130-139 admite autenticación opcional y serializa campos de pasajeros. No se consultaron viajes ni datos reales; no se da por resuelto ni se afirma explotación observada.
- La caché verificada almacena geocodificación, no disponibilidad de cupos.

## Qué cerrar a continuación

- Hay afirmaciones ACID, pero no tabla operación→garantía para operaciones reales.
- TTL/upsert no explican invalidación por cambio de fuente, parámetros geográficos o escritura relevante. No es caché de cupos: no se inventa una reserva incorrecta por este caché.
- Decisiones de extracción/geocodificación existentes no identifican la de datos más costosa de revertir.
- Consecuencias generales, sin comparación de reversión de datos.
- Hay ACID y degradación con cache, no estrategia integrada de consistencia e invalidación.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
