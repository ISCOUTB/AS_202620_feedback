# AS_202620_Recobra · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_Recobra/tree/15e39a1bffec7c0383f90b2a38c2a9304e2b2052) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado:** S11 definitiva al cierre indicado; nota propuesta para decisión docente.
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
| 1 | Integración principal identificada en código | Cumple | [docs/modos-de-fallo.md:11-16](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/modos-de-fallo.md#L11-L16) | API→PostgreSQL principal y eventos locales secundarios identificados. |
| 2 | Tabla de modos de fallo: no responde, tarde, duplicado | Cumple | [docs/modos-de-fallo.md:26-44](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/modos-de-fallo.md#L26-L44) | No respuesta, demora y repetición, distinguidos por integración. |
| 3 | Mitigación explícita para cada modo | Cumple | [docs/modos-de-fallo.md:26-50](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/modos-de-fallo.md#L26-L50) | Límites temporales, inserción idempotente y recuperación/pending con responsable arquitectónico. |
| 4 | Mitigaciones coherentes con implementación o pendientes declarados | Cumple | `src/application/use-cases/crear-publicacion.ts:32-35,66-91,119-129; docs/modos-de-fallo.md:62-75` | Clave determinista e inserción protegida implementadas. Diferenciar límites pendientes y frases antiguas sobre ausencia de cuentas/única escritura. |
| 5 | Idempotencia/saga diseñada o inaplicabilidad argumentada | Cumple | `docs/modos-de-fallo.md:62-108; docs/adr/0020-consistencia-entre-publicaciones-y-reclamaciones.md:44-67` | Creación idempotente; saga de recuperación hacia adelante entre publicación y reclamación con reintento/reconciliación. |
| 6 | ADR evalúa extracción con criterios | Cumple | [docs/adr/0012-no-extraer-emparejamiento.md:30-75](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/adr/0012-no-extraer-emparejamiento.md#L30-L75) | Alternativas con mediciones y costo operativo para Emparejamiento. |
| 7 | No extraer como alternativa explícita | Cumple | [docs/adr/0012-no-extraer-emparejamiento.md:41-75](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/adr/0012-no-extraer-emparejamiento.md#L41-L75) | No extraer explícito y elegido; conserva puertos para cambiar posteriormente. |
| 8 | arc42 §11 actualizado | Cumple | [docs/arc42/arc42.md:338-359](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/arc42/arc42.md#L338-L359) | Riesgos, consistencia y mitigaciones pendientes documentados. |
| 9 | Aspectos actualizados con trazabilidad | Cumple | [docs/aspectos.md:14,17-18](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/aspectos.md#L14) | Aspectos y evidencias enlazan fallos, idempotencia y decisiones. |

**Recuento: 9/9. Nota propuesta: 5.0/5.0**, mediante 1 + 4 × (9/9). Propuesta al docente, quien fija la nota final en Moodle.

## Matriz transversal del CONTRATO (9 criterios)

| # | Criterio | Estado | Evidencia y límites |
|---|---|---|---|
| 1 | Identidad, convención y visibilidad | Cumple | https://github.com/ISCOUTB/AS_202620_Recobra; clon público sin autenticación y consulta pública actions/runs HTTP 200. |
| 2 | Estructura mínima | Cumple | `git ls-tree -r --name-only 15e39a1bffec7c0383f90b2a38c2a9304e2b2052`: README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. |
| 3 | Estado calificado identificable | Cumple | origin/master, `15e39a1bffec7c0383f90b2a38c2a9304e2b2052`, fecha 2026-10-18T12:41:29-05:00; selección anterior al cierre S11 o a observación S12, respectivamente. |
| 4 | Nombres de ADR | Cumple | Listado `docs/adr/` en 15e39a1bffec sin archivos fuera de NNNN-titulo-en-kebab-case.md. |
| 5 | ADR aceptados no reescritos | No cumple | docs/ia.md:102 y el registro de enmiendas ADR-0011 reconocen ediciones históricas a ADR aceptados. Enlaces sucesores reparan trazabilidad, no borran el incumplimiento previo. |
| 6 | Registro IA al día | Cumple | [docs/ia.md:65-79,103,120](https://github.com/ISCOUTB/AS_202620_Recobra/blob/15e39a1bffec7c0383f90b2a38c2a9304e2b2052/docs/ia.md#L65-L79); entrada S11 con aceptaciones y rechazos técnicos, commit anterior al cierre dentro del periodo. |
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

- Mantener trazabilidad de las mitigaciones pendientes y añadir pruebas antes de presentarlas como garantías operativas.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
