# AS_202620_PROYECTO_CAMPUSMARKET · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/tree/a237dd2f22b02bb547f87a07d15b6d31ea0dc758) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado:** S11 definitiva al cierre indicado; nota propuesta para decisión docente.
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
| 1 | Integración principal identificada en código | Cumple | `docs/evidencias/evidencia-s11-2026-10-18.md:7-11; frontend/campusmarket/lib/publicaciones/publicaciones_api.dart:34-64` | POST de publicación Flutter→FastAPI→MySQL y límites de espera reales. |
| 2 | Tabla de modos de fallo: no responde, tarde, duplicado | Cumple | [docs/evidencias/evidencia-s11-2026-10-18.md:13-19](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/evidencias/evidencia-s11-2026-10-18.md#L13-L19) | Tabla distingue no respuesta, demora y duplicado; añade caída de BD y compensación de archivos. |
| 3 | Mitigación explícita para cada modo | Cumple | [docs/evidencias/evidencia-s11-2026-10-18.md:15-19](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/evidencias/evidencia-s11-2026-10-18.md#L15-L19) | Cada modo tiene mitigación y estado; se aceptan expresamente los pendientes con plan. |
| 4 | Mitigaciones coherentes con implementación o pendientes declarados | Cumple | `docs/evidencias/evidencia-s11-2026-10-18.md:25-31; backend/app/publicaciones/repository.py:143-199` | Rollback/commit implementados; Idempotency-Key y pruebas T1–T7 declaradas pendientes, no se atribuyen a producción. |
| 5 | Idempotencia/saga diseñada o inaplicabilidad argumentada | Cumple | [docs/evidencias/evidencia-s11-2026-10-18.md:25-33](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/evidencias/evidencia-s11-2026-10-18.md#L25-L33) | Diseño de clave por usuario y operación, hash de contenido, colisión y repetición; saga distribuida no aplica al monolito actual. |
| 6 | ADR evalúa extracción con criterios | Cumple | [docs/adr/0021-mantener-catalogo-en-el-monolito-modular.md:16-33](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/adr/0021-mantener-catalogo-en-el-monolito-modular.md#L16-L33) | Compara conservar, HTTP y eventos con costo, consistencia y escalamiento. |
| 7 | No extraer como alternativa explícita | Cumple | [docs/adr/0021-mantener-catalogo-en-el-monolito-modular.md:16-29](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/adr/0021-mantener-catalogo-en-el-monolito-modular.md#L16-L29) | No extraer Catálogo es alternativa evaluada y decisión válida. |
| 8 | arc42 §11 actualizado | Cumple | [docs/arc42/11-riesgos-y-deuda-tecnica.md:28-35](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/arc42/11-riesgos-y-deuda-tecnica.md#L28-L35) | Registra riesgos y deuda S11, incluidas pruebas aún no ejecutadas. |
| 9 | Aspectos actualizados con trazabilidad | Cumple | [docs/aspectos.md:41-42](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/aspectos.md#L41-L42) | ASP-13/14 enlazan evidencia, decisiones, código y pruebas pendientes. |

**Recuento: 9/9. Nota propuesta: 5.0/5.0**, mediante 1 + 4 × (9/9). Propuesta al docente, quien fija la nota final en Moodle.

## Matriz transversal del CONTRATO (9 criterios)

| # | Criterio | Estado | Evidencia y límites |
|---|---|---|---|
| 1 | Identidad, convención y visibilidad | Cumple | https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET; clon público sin autenticación y consulta pública actions/runs HTTP 200. |
| 2 | Estructura mínima | Cumple | `git ls-tree -r --name-only a237dd2f22b02bb547f87a07d15b6d31ea0dc758`: README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. |
| 3 | Estado calificado identificable | Cumple | origin/master, `a237dd2f22b02bb547f87a07d15b6d31ea0dc758`, fecha 2026-10-18T23:51:37-05:00; selección anterior al cierre S11 o a observación S12, respectivamente. |
| 4 | Nombres de ADR | Cumple | Listado `docs/adr/` en a237dd2f22b0 sin archivos fuera de NNNN-titulo-en-kebab-case.md. |
| 5 | ADR aceptados no reescritos | No cumple | docs/arc42/11-riesgos-y-deuda-tecnica.md:12 reconoce reescrituras de ADR aceptados; deuda histórica que no se borra con S11. |
| 6 | Registro IA al día | Cumple | [docs/ia.md:522-539](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/docs/ia.md#L522-L539); entrada S11 con aceptaciones y rechazos técnicos, commit anterior al cierre dentro del periodo. |
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

- Mantener trazabilidad de las mitigaciones pendientes y añadir pruebas antes de presentarlas como garantías operativas.
- Resolver y documentar la evidencia pública de SonarCloud/Quality Gate y las verificaciones transversales aún abiertas.
