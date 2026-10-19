# AS_202620_ROUTB · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_ROUTB/tree/1bd9425e2675bd7531426b6e31e78546b3e55f2e) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado:** S11 definitiva al cierre indicado; nota propuesta para decisión docente.
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
| 1 | Integración principal identificada en código | Cumple | [docs/evidencia/resiliencia-y-modos-de-fallo.md:25-32](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/evidencia/resiliencia-y-modos-de-fallo.md#L25-L32) | Integración Flutter→API de solicitudes de cupo localizada en código. |
| 2 | Tabla de modos de fallo: no responde, tarde, duplicado | Cumple | [docs/evidencia/resiliencia-y-modos-de-fallo.md:77-81](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/evidencia/resiliencia-y-modos-de-fallo.md#L77-L81) | Tres modos explícitos de fallo parcial. |
| 3 | Mitigación explícita para cada modo | Cumple | [docs/evidencia/resiliencia-y-modos-de-fallo.md:63-71,77-81](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/evidencia/resiliencia-y-modos-de-fallo.md#L63-L71) | Timeout y reintento visible, clave/backoff/breaker pendientes con plan 2027. La fecha futura no invalida el diseño S11. |
| 4 | Mitigaciones coherentes con implementación o pendientes declarados | No cumple | `docs/evidencia/resiliencia-y-modos-de-fallo.md:100-107; backend/app/modules/requests/application/create_request.py:58-89; backend/app/modules/requests/infrastructure/models.py:11-17` | Se presenta validación de duplicados como atomicidad/unicidad de BD; es SELECT previo seguido de INSERT, sin UNIQUE para solicitud activa. La aceptación sí controla cupos transaccionalmente; no confundir operaciones. |
| 5 | Idempotencia/saga diseñada o inaplicabilidad argumentada | Cumple | [docs/evidencia/resiliencia-y-modos-de-fallo.md:109-143](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/evidencia/resiliencia-y-modos-de-fallo.md#L109-L143) | Clave idempotente diseñada y saga distribuida no necesaria hoy; hipotética compensación explicada. |
| 6 | ADR evalúa extracción con criterios | Cumple | [docs/adr/0017-decision-extraccion-modulo-requests.md:17-68](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/adr/0017-decision-extraccion-modulo-requests.md#L17-L68) | Criterios de equipo, costo, cambios, transacción y escalabilidad para requests. |
| 7 | No extraer como alternativa explícita | Cumple | [docs/adr/0017-decision-extraccion-modulo-requests.md:24-55](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/adr/0017-decision-extraccion-modulo-requests.md#L24-L55) | Conservar monolito es opción explícita y elegida, sin obligación de extraer. |
| 8 | arc42 §11 actualizado | Cumple | [docs/arc42/11_riesgos_y_deuda_tecnica.md:24-26,45-47](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/arc42/11_riesgos_y_deuda_tecnica.md#L24-L26) | Riesgos y plan pendientes registrados; corregir sobreafirmación de unicidad de la fila 4. |
| 9 | Aspectos actualizados con trazabilidad | Cumple | [docs/aspectos.md:16](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/aspectos.md#L16) | Aspecto 10 con trazabilidad S11. |

**Recuento: 8/9. Nota propuesta: 4.6/5.0**, mediante 1 + 4 × (8/9). Propuesta al docente, quien fija la nota final en Moodle.

## Matriz transversal del CONTRATO (9 criterios)

| # | Criterio | Estado | Evidencia y límites |
|---|---|---|---|
| 1 | Identidad, convención y visibilidad | Cumple | https://github.com/ISCOUTB/AS_202620_ROUTB; clon público sin autenticación y consulta pública actions/runs HTTP 200. |
| 2 | Estructura mínima | Cumple | `git ls-tree -r --name-only 1bd9425e2675bd7531426b6e31e78546b3e55f2e`: README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. |
| 3 | Estado calificado identificable | Cumple | origin/master, `1bd9425e2675bd7531426b6e31e78546b3e55f2e`, fecha 2026-10-18T16:39:27-05:00; selección anterior al cierre S11 o a observación S12, respectivamente. |
| 4 | Nombres de ADR | Cumple | Listado `docs/adr/` en 1bd9425e2675 sin archivos fuera de NNNN-titulo-en-kebab-case.md. |
| 5 | ADR aceptados no reescritos | No verificado | Historial de todos los ADR aceptados no contrastado íntegramente contra su primera aceptación; no se certifica inmutabilidad por un solo log. |
| 6 | Registro IA al día | Cumple | [docs/ia.md:146-162](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/docs/ia.md#L146-L162); entrada S11 con aceptaciones y rechazos técnicos, commit anterior al cierre dentro del periodo. |
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

- Se presenta validación de duplicados como atomicidad/unicidad de BD; es SELECT previo seguido de INSERT, sin UNIQUE para solicitud activa. La aceptación sí controla cupos transaccionalmente; no confundir operaciones.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
