# AS_202620_ShareU · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_ShareU/tree/39508608eae4c1a56a5e4fc11a055bf6afb2c003) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado:** S11 definitiva al cierre indicado; nota propuesta para decisión docente.
**Repositorio público:** https://github.com/ISCOUTB/AS_202620_ShareU
**Rama principal:** origin/master
**Commit evaluado:** `39508608eae4c1a56a5e4fc11a055bf6afb2c003` (2026-09-28T19:56:57-05:00)
**Enlace inmutable:** https://github.com/ISCOUTB/AS_202620_ShareU/tree/39508608eae4c1a56a5e4fc11a055bf6afb2c003
**Cierre S11 exclusivo:** 2026-10-19T05:00:00Z (19 de octubre, 00:00 Colombia).
**Observación S12:** 2026-10-19T21:35:00Z (19 de octubre, 16:35 Colombia).
**Actividad:** 0 commits principales en intervalo S11 [2026-10-12T05:00Z, 2026-10-19T05:00Z); 0 después del cierre y hasta observación. No son conteos de personas ni una rúbrica de volumen.

## Alcance y método

Selección por fecha de commit en la rama principal remota; no por tags, ramas de PR ni archivos de Moodle. Inspección estática de documentación y código en clon efímero público, y consulta pública de resultados de GitHub Actions. No se ejecutó código, tests, contenedores ni scripts del equipo; no se abrieron PDFs ni se consultaron datos personales reales. Las rutas y líneas de las matrices corresponden al hash indicado; la nota no suma la matriz transversal.

## Matriz semanal (9 criterios)

| # | Criterio | Estado | Evidencia técnica | Observación y límite |
|---|---|---|---|---|
| 1 | Integración principal identificada en código | Cumple | `app/busqueda/service.py:5-6,75-84; docs/arc42/arc42.md:166-212` | Búsqueda integra servicios de documentos y métricas; línea base real en código. |
| 2 | Tabla de modos de fallo: no responde, tarde, duplicado | No cumple | `docs/adr/0004-integracion-sincrona-y-asincrona.md:39-88; docs/arc42/arc42.md:386-396` | Lista genérica de indisponibilidad/timeout; no tabla de los tres modos requerida, incluido duplicado en integración real. |
| 3 | Mitigación explícita para cada modo | No cumple | [docs/adr/0004-integracion-sincrona-y-asincrona.md:39-88](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0004-integracion-sincrona-y-asincrona.md#L39-L88) | No mitigación específica por cada modo, ligada a integración implementada y su estado. |
| 4 | Mitigaciones coherentes con implementación o pendientes declarados | No cumple | `docs/adr/0004-integracion-sincrona-y-asincrona.md:20-88; docs/arc42/arc42.md:222-255` | Almacenamiento y correo se plantean a futuro; no cotejo S11 implementado/pendiente de cada mitigación. |
| 5 | Idempotencia/saga diseñada o inaplicabilidad argumentada | No cumple | [docs/adr/0004-integracion-sincrona-y-asincrona.md:170-183](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0004-integracion-sincrona-y-asincrona.md#L170-L183) | Reglas genéricas de pendientes/reintentos; falta idempotencia/saga o argumento explícito de inaplicabilidad. |
| 6 | ADR evalúa extracción con criterios | No cumple | [docs/adr/0001-estilo-arquitectonico.md:1-110](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0001-estilo-arquitectonico.md#L1-L110) | ADR inicial de estilo, no evaluación de extraer un módulo concreto con criterios. |
| 7 | No extraer como alternativa explícita | No cumple | [docs/adr/0001-estilo-arquitectonico.md:103-104](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0001-estilo-arquitectonico.md#L103-L104) | Pospone ADR si hubiera extracción; no compara explícitamente no extraer frente a alternativas en la decisión S11. |
| 8 | arc42 §11 actualizado | No cumple | [docs/arc42/arc42.md:386-396](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L386-L396) | Riesgos generales, sin modos de fallo y mitigaciones pendientes de S11. |
| 9 | Aspectos actualizados con trazabilidad | No cumple | [docs/aspectos/aspectos.md:50-56](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/aspectos/aspectos.md#L50-L56) | Trazabilidad llega a S9, no incorpora la integración/resiliencia S11. |

**Recuento: 1/9. Nota propuesta: 1.4/5.0**, mediante 1 + 4 × (1/9). Propuesta al docente, quien fija la nota final en Moodle.

## Matriz transversal del CONTRATO (9 criterios)

| # | Criterio | Estado | Evidencia y límites |
|---|---|---|---|
| 1 | Identidad, convención y visibilidad | Cumple | https://github.com/ISCOUTB/AS_202620_ShareU; clon público sin autenticación y consulta pública actions/runs HTTP 200. |
| 2 | Estructura mínima | No cumple | [docs/aspectos/aspectos.md:1](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/aspectos/aspectos.md#L1) y [docs/ia/ia.md:1](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/ia/ia.md#L1) existen pero no en ruta canónica; se evalúan, no se consideran ausentes. |
| 3 | Estado calificado identificable | Cumple | origin/master, `39508608eae4c1a56a5e4fc11a055bf6afb2c003`, fecha 2026-09-28T19:56:57-05:00; selección anterior al cierre S11 o a observación S12, respectivamente. |
| 4 | Nombres de ADR | Cumple | Decisiones Markdown de `docs/adr/` siguen NNNN-titulo-en-kebab-case.md. PDF auxiliar excluido de la comprobación y no abierto. |
| 5 | ADR aceptados no reescritos | No verificado | No se completó contraste de cada decisión aceptada con todo su historial; lista de ADR no prueba inmutabilidad. |
| 6 | Registro IA al día | No cumple | [docs/ia/ia.md:21-34](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/ia/ia.md#L21-L34); última entrada llega a S9; no registra S11/S12. |
| 7 | CI, scanner y Quality Gate públicos | No cumple | .github/workflows/tests.yml:25-32 contiene pruebas y scanner, pero el run es fallido y no se acreditó Quality Gate público de esta revisión. Runs concretos en sección siguiente. |
| 8 | Sin secretos actuales e históricos | No verificado | Barrido estático de firmas de alta confianza en `39508608eae4c1a56a5e4fc11a055bf6afb2c003` sin coincidencias de credenciales típicas. No se completó barrido de todo el historial y todas las formas de secretos: no se certifica ausencia. No se reproducen valores. |
| 9 | Aporte de todos los integrantes | No verificado | Historial principal y 0 commits S11 inspeccionados; no se completó consolidación persona↔alias↔padrón y membresía para todos. Un commit o cuenta no equivale a una persona. No se publican identidades. |

## CI citable y evidencia de ejecución

- tests.yml: **failure**, https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458.
- Último run del hash principal falla; no se adopta badge o test local declarado como sustituto.
- Un run global verde acredita el workflow reportado, no cada escenario descrito, una prueba en producción ni un scanner ausente. No se inventan logs de jobs ni ejecuciones propias.

## Overall: coherencia, producto y límites

- Principal no cambia desde 2026-09-28; cero commits en S11 y desde el cierre. Se reconoce evidencia previa útil, sin inventar entrega nueva.
- Sistema real de búsqueda y métricas, con persistencia SQLite; correo y outbox son intención documental, no implementación probada.
- No se abrieron PDFs. Artefactos en rutas alternativas se evaluaron donde están; la desviación de estructura no equivale a ausencia de documentación.

## Qué cerrar a continuación

- Lista genérica de indisponibilidad/timeout; no tabla de los tres modos requerida, incluido duplicado en integración real.
- No mitigación específica por cada modo, ligada a integración implementada y su estado.
- Almacenamiento y correo se plantean a futuro; no cotejo S11 implementado/pendiente de cada mitigación.
- Reglas genéricas de pendientes/reintentos; falta idempotencia/saga o argumento explícito de inaplicabilidad.
- ADR inicial de estilo, no evaluación de extraer un módulo concreto con criterios.
- Pospone ADR si hubiera extracción; no compara explícitamente no extraer frente a alternativas en la decisión S11.
- Riesgos generales, sin modos de fallo y mitigaciones pendientes de S11.
- Trazabilidad llega a S9, no incorpora la integración/resiliencia S11.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
