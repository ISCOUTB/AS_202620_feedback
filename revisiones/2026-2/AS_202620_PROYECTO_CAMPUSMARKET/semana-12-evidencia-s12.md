# AS_202620_PROYECTO_CAMPUSMARKET · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/tree/a237dd2f22b02bb547f87a07d15b6d31ea0dc758) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado:** S12 PRELIMINAR, avance observado; NO cierre ni nota definitiva.
**Repositorio público:** https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET
**Rama principal:** origin/master
**Commit evaluado:** `a237dd2f22b02bb547f87a07d15b6d31ea0dc758` (2026-10-18T23:51:37-05:00)
**Enlace inmutable:** https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/tree/a237dd2f22b02bb547f87a07d15b6d31ea0dc758
**Cierre S11 exclusivo:** 2026-10-19T05:00:00Z (19 de octubre, 00:00 Colombia).
**Observación S12:** 2026-10-19T21:35:00Z (19 de octubre, 16:35 Colombia).
**Actividad:** 16 commits principales en intervalo S11 [2026-10-12T05:00Z, 2026-10-19T05:00Z); 0 después del cierre y hasta observación. No son conteos de personas ni una rúbrica de volumen.

## Alcance y método

Selección por fecha de commit en la rama principal remota; no por tags, ramas de PR ni archivos de Moodle. Inspección estática de documentación y código en clon efímero público, y consulta pública de resultados de GitHub Actions. No se ejecutó código, tests, contenedores ni scripts del equipo; no se abrieron PDFs ni se consultaron datos personales reales. Las rutas y líneas de las matrices corresponden al hash indicado; la nota no suma la matriz transversal.

## Matriz semanal (9 criterios)

| # | Criterio | Estado | Evidencia técnica | Observación y límite |
|---|---|---|---|---|
| 1 | Tabla operación→garantía de consistencia real | No cumple | [docs/arc42/08-conceptos-transversales.md:37-42,69-76](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/arc42/08-conceptos-transversales.md#L37-L42) | Tabla de propiedad y narrativa transaccional; falta tabla operación→garantía nombrada. |
| 2 | Dos operaciones contrastadas con implementación | Cumple | `backend/app/publicaciones/repository.py:143-199,336-383; docs/arc42/08-conceptos-transversales.md:69-76` | Crear publicación y cambiar estado confirman/retroceden transacciones MySQL locales. No prueba atomicidad conjunta SQL/archivos. |
| 3 | Diseño de caché: qué/dónde/cuánto | No cumple | [docs/arc42/08-conceptos-transversales.md:1-97](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/arc42/08-conceptos-transversales.md#L1-L97) | No diseña qué/dónde/duración de caché ni justifica prescindir de ella. |
| 4 | Política de invalidación tras escritura | No cumple | [docs/arc42/08-conceptos-transversales.md:69-76](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/arc42/08-conceptos-transversales.md#L69-L76) | Sin política tras crear/cambiar estado de publicación. No se afirma un bug de caché instalada: falta decidir si lecturas del catálogo se cachean y cómo se renuevan. |
| 5 | Garantías y supuestos de eventos, si existen | Cumple | [docs/evidencias/evidencia-s11-2026-10-18.md:31-33](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/evidencias/evidencia-s11-2026-10-18.md#L31-L33) | Declara ausencia de broker y eventos durables; flujo actual síncrono, sin prometer entrega exactamente una vez. |
| 6 | ADR de decisión de datos más costosa de revertir | No cumple | [docs/adr/0021-mantener-catalogo-en-el-monolito-modular.md:16-33](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/adr/0021-mantener-catalogo-en-el-monolito-modular.md#L16-L33) | ADR de extracción, no de la decisión de datos más costosa de revertir. |
| 7 | Argumento y costo comparativo de reversión | No cumple | [docs/adr/0021-mantener-catalogo-en-el-monolito-modular.md:31-33](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/adr/0021-mantener-catalogo-en-el-monolito-modular.md#L31-L33) | Consecuencias y condiciones de reapertura no comparan costo de reversión de datos. |
| 8 | C4 nivel 2 con almacenes/brokers y tecnología | Cumple | `docs/c4/02-contenedores.md:8-11; docs/c4/02-contenedores.puml:15-22` | Frontend, API, MySQL 8.4 y archivos identificados como piezas propias; no se inventa un broker. |
| 9 | arc42 §8 con consistencia y caché | No cumple | [docs/arc42/08-conceptos-transversales.md:69-97](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/arc42/08-conceptos-transversales.md#L69-L97) | Consistencia local parcial; falta estrategia de caché/invalidación o justificación de no usarla. |

**Recuento: 3/9. Nota propuesta: 2.3/5.0**, mediante 1 + 4 × (3/9). Solo diagnóstico PRELIMINAR; no sustituye evaluación al cierre de S12.

## Matriz transversal del CONTRATO (9 criterios)

| # | Criterio | Estado | Evidencia y límites |
|---|---|---|---|
| 1 | Identidad, convención y visibilidad | Cumple | https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET; clon público sin autenticación y consulta pública actions/runs HTTP 200. |
| 2 | Estructura mínima | Cumple | `git ls-tree -r --name-only a237dd2f22b02bb547f87a07d15b6d31ea0dc758`: README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. |
| 3 | Estado calificado identificable | Cumple | origin/master, `a237dd2f22b02bb547f87a07d15b6d31ea0dc758`, fecha 2026-10-18T23:51:37-05:00; selección anterior al cierre S11 o a observación S12, respectivamente. |
| 4 | Nombres de ADR | Cumple | Listado `docs/adr/` en a237dd2f22b0 sin archivos fuera de NNNN-titulo-en-kebab-case.md. |
| 5 | ADR aceptados no reescritos | No cumple | docs/arc42/11-riesgos-y-deuda-tecnica.md:12 reconoce reescrituras de ADR aceptados; deuda histórica que no se borra con S11. |
| 6 | Registro IA al día | No cumple | [docs/ia.md:522-539](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/ia.md#L522-L539); registro hasta S11; no actualización del registro durante ventana S12. El contenido anticipado se reconoce en la matriz semanal, sin inventar una nueva entrada. |
| 7 | CI, scanner y Quality Gate públicos | No cumple | docs/arc42/11-riesgos-y-deuda-tecnica.md:11 reconoce scanner pendiente; no se verificó la terna scanner+run+Quality Gate público. Runs concretos en sección siguiente. |
| 8 | Sin secretos actuales e históricos | No verificado | Barrido estático de firmas de alta confianza en `a237dd2f22b02bb547f87a07d15b6d31ea0dc758` sin coincidencias de credenciales típicas. No se completó barrido de todo el historial y todas las formas de secretos: no se certifica ausencia. No se reproducen valores. |
| 9 | Aporte de todos los integrantes | No verificado | Historial principal y 16 commits S11 inspeccionados; no se completó consolidación persona↔alias↔padrón y membresía para todos. Un commit o cuenta no equivale a una persona. No se publican identidades. |

## CI citable y evidencia de ejecución

- Compose: **success**, https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586404.
- Contrato S10: **success**, https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586378.
- Flujo real Web y Android: **failure**, https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586366.
- Backend: **success**, https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586343.
- Flutter: **success**, https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586312.
- La cadena anterior f2e94972f0327cd11f2c956fd894f66d779cede6 tiene flujo real exitoso en run 39198723967; no sustituye el resultado final.
- Un run global verde acredita el workflow reportado, no cada escenario descrito, una prueba en producción ni un scanner ausente. No se inventan logs de jobs ni ejecuciones propias.

## Overall: coherencia, producto y límites

- PR 56/58 y correcciones 57/59 están incorporadas antes del cierre; se evalúa el commit, no el estado viejo de una rama.
- Idempotencia es diseño pendiente. No confundir avance documental y CI con pruebas de fallos inyectados T1–T7 o despliegue público comprobado.
- La evidencia S11 conserva referencias antiguas de CI. El run de flujo real en f2e9497 fue exitoso, pero el run del hash final es fallido; Android sí fue ejecutado en la cadena anterior. No atribuir el fallo actual a un job concreto sin sus logs.
- PR 60, posterior y abierto según contexto de seguimiento, no cambia la matriz principal; revisar contradicción ADR solo cuando se integre.

- Coherencia C4: [docs/c4/02-contenedores.puml:44-53](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/c4/02-contenedores.puml#L44-L53) conserva una nota de MVP no desplegado, mientras [docs/c4/02-contenedores.md:33-49](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/c4/02-contenedores.md#L33-L49) describe topología pública; actualizar la nota histórica sin usarla como verificación de despliegue actual.

## Qué cerrar a continuación

- Tabla de propiedad y narrativa transaccional; falta tabla operación→garantía nombrada.
- No diseña qué/dónde/duración de caché ni justifica prescindir de ella.
- Sin política tras crear/cambiar estado de publicación. No se afirma un bug de caché instalada: falta decidir si lecturas del catálogo se cachean y cómo se renuevan.
- ADR de extracción, no de la decisión de datos más costosa de revertir.
- Consecuencias y condiciones de reapertura no comparan costo de reversión de datos.
- Consistencia local parcial; falta estrategia de caché/invalidación o justificación de no usarla.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
