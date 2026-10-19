# AS_202620_Recobra · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_Recobra/tree/15e39a1bffec7c0383f90b2a38c2a9304e2b2052) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado:** S12 PRELIMINAR, avance observado; NO cierre ni nota definitiva.
**Repositorio público:** https://github.com/ISCOUTB/AS_202620_Recobra
**Rama principal:** origin/master
**Commit evaluado:** `15e39a1bffec7c0383f90b2a38c2a9304e2b2052` (2026-10-18T12:41:29-05:00)
**Enlace inmutable:** https://github.com/ISCOUTB/AS_202620_Recobra/tree/15e39a1bffec7c0383f90b2a38c2a9304e2b2052
**Cierre S11 exclusivo:** 2026-10-19T05:00:00Z (19 de octubre, 00:00 Colombia).
**Observación S12:** 2026-10-19T21:35:00Z (19 de octubre, 16:35 Colombia).
**Actividad:** 26 commits principales en intervalo S11 [2026-10-12T05:00Z, 2026-10-19T05:00Z); 0 después del cierre y hasta observación. No son conteos de personas ni una rúbrica de volumen.

## Alcance y método

Selección por fecha de commit en la rama principal remota; no por tags, ramas de PR ni archivos de Moodle. Inspección estática de documentación y código en clon efímero público, y consulta pública de resultados de GitHub Actions. No se ejecutó código, tests, contenedores ni scripts del equipo; no se abrieron PDFs ni se consultaron datos personales reales. Las rutas y líneas de las matrices corresponden al hash indicado; la nota no suma la matriz transversal.

## Matriz semanal (9 criterios)

| # | Criterio | Estado | Evidencia técnica | Observación y límite |
|---|---|---|---|---|
| 1 | Tabla operación→garantía de consistencia real | Cumple | `docs/adr/0020-consistencia-entre-publicaciones-y-reclamaciones.md:15-20,64-67; src/application/use-cases/reclamaciones.ts:85-140,170-188` | Tabla de crear/rechazar/aprobar/entregar y sus dos escrituras, con garantía eventual común explícita y desfases permitidos. |
| 2 | Dos operaciones contrastadas con implementación | Cumple | `src/application/use-cases/reclamaciones.ts:85-126,170-188; src/application/use-cases/reconciliar-reclamaciones.ts:50-74` | Aprobar y entregar aceptan pasos separados; reintento retoma y reconciliador repara. No se adjudica transacción fuerte entre contextos. |
| 3 | Diseño de caché: qué/dónde/cuánto | No cumple | `docs/modulo-datos.md:1-54; docs/arc42/arc42.md:275-284` | No estrategia de caché con objeto/ubicación/duración ni no-caché justificado. |
| 4 | Política de invalidación tras escritura | No cumple | `docs/adr/0020-consistencia-entre-publicaciones-y-reclamaciones.md:44-67; docs/arc42/arc42.md:275-284` | Reconciliar tablas no es invalidar caché. Falta decidir lecturas de publicaciones/estados tras aprobar o entregar; no se prueba un fallo de caché actualmente desplegada. |
| 5 | Garantías y supuestos de eventos, si existen | Cumple | [docs/adr/0024-conciliacion-de-avisos.md:12-27,41-64](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/adr/0024-conciliacion-de-avisos.md#L12-L27) | Eventos locales no durables con pérdida reconocida; conciliación de avisos cada 5 minutos, ventana 3 días y lote acotado. No se promete exactly-once ni recuperación ilimitada. |
| 6 | ADR de decisión de datos más costosa de revertir | No cumple | `docs/adr/0020-consistencia-entre-publicaciones-y-reclamaciones.md:44-81; docs/adr/0024-conciliacion-de-avisos.md:20-64` | ADR útiles de consistencia y avisos, pero ninguno designa y compara la decisión de datos más costosa de revertir. |
| 7 | Argumento y costo comparativo de reversión | No cumple | [docs/adr/0020-consistencia-entre-publicaciones-y-reclamaciones.md:64-81](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/adr/0020-consistencia-entre-publicaciones-y-reclamaciones.md#L64-L81) | Costo y trade-off parciales; falta argumento comparativo de la mayor reversión. |
| 8 | C4 nivel 2 con almacenes/brokers y tecnología | Cumple | [docs/c4/C4-C2.md:15,30-31](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/c4/C4-C2.md#L15) | PostgreSQL 16 como almacén propio; se señala desalineación residual: texto ya persiste coincidencias pero caja aún menciona memoria. |
| 9 | arc42 §8 con consistencia y caché | No cumple | [docs/arc42/arc42.md:275-284,350-359](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/arc42/arc42.md#L275-L284) | Información de consistencia quedó en riesgos; §8 no recoge ambas estrategias. |

**Recuento: 4/9. Nota propuesta: 2.8/5.0**, mediante 1 + 4 × (4/9). Solo diagnóstico PRELIMINAR; no sustituye evaluación al cierre de S12.

## Matriz transversal del CONTRATO (9 criterios)

| # | Criterio | Estado | Evidencia y límites |
|---|---|---|---|
| 1 | Identidad, convención y visibilidad | Cumple | https://github.com/ISCOUTB/AS_202620_Recobra; clon público sin autenticación y consulta pública actions/runs HTTP 200. |
| 2 | Estructura mínima | Cumple | `git ls-tree -r --name-only 15e39a1bffec7c0383f90b2a38c2a9304e2b2052`: README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. |
| 3 | Estado calificado identificable | Cumple | origin/master, `15e39a1bffec7c0383f90b2a38c2a9304e2b2052`, fecha 2026-10-18T12:41:29-05:00; selección anterior al cierre S11 o a observación S12, respectivamente. |
| 4 | Nombres de ADR | Cumple | Listado `docs/adr/` en 15e39a1bffec sin archivos fuera de NNNN-titulo-en-kebab-case.md. |
| 5 | ADR aceptados no reescritos | No cumple | docs/ia.md:102 y el registro de enmiendas ADR-0011 reconocen ediciones históricas a ADR aceptados. Enlaces sucesores reparan trazabilidad, no borran el incumplimiento previo. |
| 6 | Registro IA al día | No cumple | [docs/ia.md:65-79,103,120](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/ia.md#L65-L79); registro hasta S11; no actualización del registro durante ventana S12. El contenido anticipado se reconoce en la matriz semanal, sin inventar una nueva entrada. |
| 7 | CI, scanner y Quality Gate públicos | No cumple | .github/workflows/ci.yml:38-63 declara scanner con continue-on-error y chequeo posterior. El run global es exitoso, pero faltan evidencia del scanner exitoso y análisis/QG público de esta revisión: no conformidad documental según CONTRATO §8, no afirmación de fallo probado del scanner ni del Quality Gate. Runs concretos en sección siguiente. |
| 8 | Sin secretos actuales e históricos | No verificado | Barrido estático de firmas de alta confianza en `15e39a1bffec7c0383f90b2a38c2a9304e2b2052` sin coincidencias de credenciales típicas. No se completó barrido de todo el historial y todas las formas de secretos: no se certifica ausencia. No se reproducen valores. |
| 9 | Aporte de todos los integrantes | No verificado | Historial principal y 26 commits S11 inspeccionados; no se completó consolidación persona↔alias↔padrón y membresía para todos. Un commit o cuenta no equivale a una persona. No se publican identidades. |

## CI citable y evidencia de ejecución

- CI: **success**, https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/39150751474.
- CI exitoso; no se reprodujeron pruebas ni se midió producción.
- Un run global verde acredita el workflow reportado, no cada escenario descrito, una prueba en producción ni un scanner ausente. No se inventan logs de jobs ni ejecuciones propias.

## Overall: coherencia, producto y límites

- S11 sustantiva: idempotencia, límites de BD y no extracción con criterios; los planes no implementados se separan de lo construido.
- Avance S12 ya integrado antes del corte: ADR-0020 y reconciliadores; no inventar commits durante el lunes por tener contenido anticipado.
- docs/modos-de-fallo.md:56-58,86 conserva frases antiguas (única escritura y sin cuentas); el código actual compara autor y existen reclamaciones. docs/modos-de-fallo.md:50 sobre avisos debe leerse con ADR-0024, que ya implementa conciliación acotada.
- Eventos de coincidencias/avisos no equivalen a un broker durable. La recuperación de avisos no demuestra recuperación de todos los eventos perdidos.

## Qué cerrar a continuación

- No estrategia de caché con objeto/ubicación/duración ni no-caché justificado.
- Reconciliar tablas no es invalidar caché. Falta decidir lecturas de publicaciones/estados tras aprobar o entregar; no se prueba un fallo de caché actualmente desplegada.
- ADR útiles de consistencia y avisos, pero ninguno designa y compara la decisión de datos más costosa de revertir.
- Costo y trade-off parciales; falta argumento comparativo de la mayor reversión.
- Información de consistencia quedó en riesgos; §8 no recoge ambas estrategias.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
