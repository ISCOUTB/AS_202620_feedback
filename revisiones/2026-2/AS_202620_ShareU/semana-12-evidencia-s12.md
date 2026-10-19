# AS_202620_ShareU · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_ShareU/tree/39508608eae4c1a56a5e4fc11a055bf6afb2c003) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado:** S12 PRELIMINAR, avance observado; NO cierre ni nota definitiva.
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
| 1 | Tabla operación→garantía de consistencia real | No cumple | [docs/arc42/arc42.md:328-362](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L328-L362) | No tabla operación→garantía. |
| 2 | Dos operaciones contrastadas con implementación | No cumple | `app/busqueda/service.py:75-84; docs/arc42/arc42.md:328-362` | Búsqueda leída, sin dos operaciones contrastadas con garantías declaradas. |
| 3 | Diseño de caché: qué/dónde/cuánto | No cumple | [docs/arc42/arc42.md:386-396](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L386-L396) | Caché futura en riesgos, sin qué/dónde/cuánto ni justificación de no usarla. |
| 4 | Política de invalidación tras escritura | No cumple | [docs/arc42/arc42.md:386-396](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L386-L396) | Falta invalidación tras cambiar documentos o sus metadatos. No se declara un fallo probado de una caché inexistente. |
| 5 | Garantías y supuestos de eventos, si existen | No cumple | `docs/arc42/arc42.md:222-255; docs/adr/0004-integracion-sincrona-y-asincrona.md:53-88` | Correo/outbox previsto sin garantía elegida y supuestos concretos de entrega. |
| 6 | ADR de decisión de datos más costosa de revertir | No cumple | `docs/adr/0001-estilo-arquitectonico.md:1-110; docs/arc42/arc42.md:363-385` | No ADR de la decisión de datos más costosa de revertir. |
| 7 | Argumento y costo comparativo de reversión | No cumple | [docs/arc42/arc42.md:363-385](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L363-L385) | No argumento comparativo/costo de reversión de esa decisión. |
| 8 | C4 nivel 2 con almacenes/brokers y tecnología | Cumple | [docs/c4/nivel2.mmd:14-15](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/c4/nivel2.mmd#L14-L15) | SQLite representado como almacén propio con tecnología; almacenamiento adicional es previsto. No se cuenta outbox futuro como broker implementado. |
| 9 | arc42 §8 con consistencia y caché | No cumple | [docs/arc42/arc42.md:328-362](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/arc42/arc42.md#L328-L362) | §8 no reúne las estrategias de consistencia y caché. |

**Recuento: 1/9. Nota propuesta: 1.4/5.0**, mediante 1 + 4 × (1/9). Solo diagnóstico PRELIMINAR; no sustituye evaluación al cierre de S12.

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

- No tabla operación→garantía.
- Búsqueda leída, sin dos operaciones contrastadas con garantías declaradas.
- Caché futura en riesgos, sin qué/dónde/cuánto ni justificación de no usarla.
- Falta invalidación tras cambiar documentos o sus metadatos. No se declara un fallo probado de una caché inexistente.
- Correo/outbox previsto sin garantía elegida y supuestos concretos de entrega.
- No ADR de la decisión de datos más costosa de revertir.
- No argumento comparativo/costo de reversión de esa decisión.
- §8 no reúne las estrategias de consistencia y caché.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
