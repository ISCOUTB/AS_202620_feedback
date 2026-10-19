# AS_202620_Sistema-de-calificacion-automatica · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/tree/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado:** S12 PRELIMINAR, avance observado; NO cierre ni nota definitiva.
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
| 1 | Tabla operación→garantía de consistencia real | No cumple | `docs/evidencia/modos-de-fallo.md:46-58; docs/arc42/arc42-template-ES.md:1334-1375` | Tabla de fallos no es tabla de operaciones con garantías de consistencia; falta esta entrega. |
| 2 | Dos operaciones contrastadas con implementación | No cumple | `backend/infraestructura/cola.py:102-152; backend/worker/main.py:54-95` | Se verificaron envío y consumo, pero no dos operaciones vinculadas a garantías de consistencia declaradas; procesamiento/calificación aún previstos. |
| 3 | Diseño de caché: qué/dónde/cuánto | No cumple | `docs/arc42/arc42-template-ES.md:1334-1375; docs/evidencia/modos-de-fallo.md:101-128` | TTL de marca de deduplicación no sustituye caché de lectura ni decisión explícita de no cachear. |
| 4 | Política de invalidación tras escritura | No cumple | `backend/infraestructura/cola.py:120-137; docs/evidencia/modos-de-fallo.md:115-128` | No hay política tras escritura de datos de examen/carga. No se afirma que borrar la marca NX sea una invalidación adecuada: cumple otra finalidad. |
| 5 | Garantías y supuestos de eventos, si existen | Cumple | `docs/evidencia/modos-de-fallo.md:48-51,101-113; docs/adr/0016-acotar-la-espera-de-la-cola-y-hacer-idempotente-al-worker.md:123-128` | Entrega por BLPOP sin ack, pérdida posible y deduplicación limitada documentadas; fail-open puede permitir repetidos. Garantías/límites reales, no exactly-once. |
| 6 | ADR de decisión de datos más costosa de revertir | No cumple | [docs/adr/0017-no-extraer-ningun-modulo-del-monolito-todavia.md:52-151](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/adr/0017-no-extraer-ningun-modulo-del-monolito-todavia.md#L52-L151) | ADR de extracción y límites de cola; no elección de datos con mayor costo de reversión. |
| 7 | Argumento y costo comparativo de reversión | No cumple | [docs/adr/0017-no-extraer-ningun-modulo-del-monolito-todavia.md:119-151](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/adr/0017-no-extraer-ningun-modulo-del-monolito-todavia.md#L119-L151) | Condiciones de extracción no comparan costos de migrar decisiones de datos. |
| 8 | C4 nivel 2 con almacenes/brokers y tecnología | Cumple | [docs/c4/doc-c4.md:147-338](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/c4/doc-c4.md#L147-L338) | Redis, PostgreSQL y almacén local separados, tecnologías en relaciones/tabla; distingue construido de previsto. |
| 9 | arc42 §8 con consistencia y caché | No cumple | [docs/arc42/arc42-template-ES.md:1334-1375](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/arc42/arc42-template-ES.md#L1334-L1375) | Resiliencia sí, estrategia de consistencia y caché completa no. |

**Recuento: 2/9. Nota propuesta: 1.9/5.0**, mediante 1 + 4 × (2/9). Solo diagnóstico PRELIMINAR; no sustituye evaluación al cierre de S12.

## Matriz transversal del CONTRATO (9 criterios)

| # | Criterio | Estado | Evidencia y límites |
|---|---|---|---|
| 1 | Identidad, convención y visibilidad | Cumple | https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica; clon público sin autenticación y consulta pública actions/runs HTTP 200. |
| 2 | Estructura mínima | Cumple | `git ls-tree -r --name-only 98a9dcc8f22c77ac5d0dfcea4055865e7727a21e`: README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. |
| 3 | Estado calificado identificable | Cumple | origin/master, `98a9dcc8f22c77ac5d0dfcea4055865e7727a21e`, fecha 2026-10-18T22:40:44-05:00; selección anterior al cierre S11 o a observación S12, respectivamente. |
| 4 | Nombres de ADR | Cumple | Listado `docs/adr/` en 98a9dcc8f22c sin archivos fuera de NNNN-titulo-en-kebab-case.md. |
| 5 | ADR aceptados no reescritos | No verificado | No se completó contraste histórico de cada ADR con su estado de aceptación; no se infiere inmutabilidad del nombre correcto. |
| 6 | Registro IA al día | No cumple | [docs/ia.md:305-337](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/docs/ia.md#L305-L337); registro hasta S11; no actualización del registro durante ventana S12. El contenido anticipado se reconoce en la matriz semanal, sin inventar una nueva entrada. |
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

- Tabla de fallos no es tabla de operaciones con garantías de consistencia; falta esta entrega.
- Se verificaron envío y consumo, pero no dos operaciones vinculadas a garantías de consistencia declaradas; procesamiento/calificación aún previstos.
- TTL de marca de deduplicación no sustituye caché de lectura ni decisión explícita de no cachear.
- No hay política tras escritura de datos de examen/carga. No se afirma que borrar la marca NX sea una invalidación adecuada: cumple otra finalidad.
- ADR de extracción y límites de cola; no elección de datos con mayor costo de reversión.
- Condiciones de extracción no comparan costos de migrar decisiones de datos.
- Resiliencia sí, estrategia de consistencia y caché completa no.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
