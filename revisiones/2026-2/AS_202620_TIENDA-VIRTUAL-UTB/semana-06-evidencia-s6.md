# semana-06-evidencia-s6 · Tienda virtual UTB

> Excepción docente: la ventana de S6 no tuvo actividad en la rama principal (el último commit
> anterior al cierre siguió siendo el del corte anterior). Por indicación expresa del docente, la
> matriz de S6 se evalúa sobre la **punta actual de la rama principal**, de modo que incluye
> trabajo de semanas posteriores. Es una excepción: no es comparable con el resto de la pasada de
> S6 y la nota sigue siendo una propuesta al docente.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `bc38c9bab2830e8f2c855c0e36542d849565955e` en `origin/main` (2026-09-28T10:22:29-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Estado histórico al cierre de S6 | `3d732d7` (sin actividad en la ventana de S6) |
| Regla aplicada | excepción docente: se califica la punta actual |
| Revisor | revisión manual de evidencias públicas |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | `docs/bounded-contexts.md:26-76`: diagrama Mermaid de contextos (Identidad, Catálogo, Inventario, Pedidos) y lectura que tipifica la relación (Identidad como upstream; dependencias hacia Inventario y Pedidos). | Cumple | Declara el sentido upstream/downstream y marca las colaboraciones aún no implementadas. |
| Tabla módulo a datos con dueño único por entidad | `docs/bounded-contexts.md:78-101`: tabla «módulos con dueño único» (contexto, módulo, rol dueño, tablas que posee, contrato público y estado). | Cumple | Cada tabla declara un único contexto dueño; `shared/database.py` se declara transversal, no contexto. |
| La tabla cubre las entidades que existen en el código | `backend/app/modules/catalog/models.py:9-17` define `Product` (`catalog_products`); la tabla lo lista como propiedad de `catalog` y distingue las tablas previstas (inventario, identidad, pedidos) como objetivo. | Cumple | La única entidad implementada queda cubierta; las demás se declaran objetivo, no implementadas. |
| No conformidades de propiedad de datos detectadas sobre el código actual | `docs/violaciones-s6.md:28-34` enumera V1–V7 con entidad, módulo dueño esperado y ubicación observada (`archivo:línea`). V1 (dueño de `existencias`) es la no conformidad central. | Cumple | Cada violación cita archivo y línea del código actual. |
| Plan de corrección por no conformidad | `docs/violaciones-s6.md:28-34` asigna a cada violación una acción concreta y una prioridad (P1–P3), con un plan resumido por fases. | Cumple | El plan asocia acción y prioridad a cada violación. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | `docs/arc42/arc42-template-EN.md:538-567`: §8 contiene persistencia/propiedad, configuración, datos mockeados y pruebas, pero ni el mapa ni el lenguaje ubicuo; estos viven en `docs/bounded-contexts.md:103` y §8 no lo enlaza (búsqueda de `bounded`/`ubiquitous` en `docs/arc42` sin coincidencias). | No cumple | Los artefactos existen, pero en otro documento; §8 no recoge ni enlaza el mapa ni el lenguaje ubicuo. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | Sin reajuste de límites: `docs/bounded-contexts.md` ya existía en el hash S5 `3d732d7` (commit `20ab43f`, ancestro verificado) y no cambió; el diff de `docs/c4/` frente a S5 solo añade notas de despliegue. | Cumple | Al no cambiar los límites no se exige C3 ni ADR de reajuste; el nivel 3 se declara en arc42 (Building Block View, Level 2). |
| Aspectos relacionables con los contextos del mapa | `docs/aspectos.md:4-8` liga `existencias` al contexto `inventory` y a `docs/violaciones-s6.md`; las filas AC-01–AC-04 nombran los módulos del mapa. | Cumple | Los contextos del mapa quedan relacionados con filas de aspectos. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB`, público; clon anónimo correcto en `bc38c9b`. | Cumple | La rama principal declarada por el remoto es `main`. |
| Estructura mínima presente | Árbol de `bc38c9b`: `README.md`, `docs/arc42/arc42-template-EN.md`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`. | Cumple | El arc42 es un único archivo con nombre distinto al de la plantilla: desviación de ruta/nombre, no ausencia. |
| Estado calificado identificable | `origin/main`, `bc38c9bab2830e8f2c855c0e36542d849565955e`, 2026-09-28T10:22:29-05:00. | Cumple | Excepción docente: se usa la punta actual. Existe un `master` obsoleto (2026-08-09) que no se usa como estado. |
| Nombres de ADR según la convención | `docs/adr/0001-monolito-modular.md` … `0006-infra-como-codigo-terraform.md`. | Cumple | Numeración y kebab-case conformes. |
| ADR aceptados no reescritos | `git log --follow`: ADR-0001 editado en `e8ae57d` (2026-08-31) y ADR-0002 en `befb0bc` (2026-09-27) tras aceptarse, sin sucesor declarado. | No cumple | Un ADR aceptado se reescribió en lugar de crear uno nuevo. |
| docs/ia.md al día para la semana | `docs/ia.md` incluye la entrada del 2026-09-06 (evidencia S6) con lo usado y lo descartado con motivo (commit `20ab43f`). | Cumple | El registro S6 está presente y documenta descartes. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `.github/workflows/tests.yml` deja el job `sonarcloud` condicionado a `SONAR_TOKEN`; sin run del scanner ni URL pública del Quality Gate. La consulta `actions/runs` del hash devuelve 328 runs, los recientes del cron `Keep-alive`. | No cumple | Falta la triple evidencia de §8; el listado de runs está inundado por keep-alive. |
| Sin credenciales en el repositorio ni en el historial | `git grep` §9 solo encuentra `var token` (SVG) en un HTML de terceros (`docs/openapi/contratos-tienda-virtual.html`); sin `.env` versionado (`.env.example` sí). | Cumple | Sin credenciales reales; las coincidencias son falsos positivos de un visor de terceros. |
| Contribución de todos los integrantes | `git shortlog -sne`: 4 identidades consolidadas (`Jasen` + `Jasen Yukopila` = 1, RAZOR7150, pxtroniwnl, shalom-A26) para 4 integrantes. | Cumple | Contribución repartida a lo largo del semestre. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `bc38c9bab2830e8f2c855c0e36542d849565955e` · 2026-09-28T10:22:29-05:00.
- **Veredicto**: con pendientes.
- La punta actual conserva los entregables de S6 (`docs/bounded-contexts.md`, `docs/violaciones-s6.md`, `docs/aspectos.md` y entrada S6 en `docs/ia.md`) y suma el contrato de API, la prueba de contrato, el despliegue en Vercel/Render/Neon y la infraestructura con Terraform de semanas posteriores.
- Lo que sigue abierto: integrar mapa y lenguaje ubicuo en arc42 §8; ADR aceptados reescritos; evidencia pública de SonarCloud con Quality Gate.

Pendientes que siguen abiertos:

- Integrar el mapa de contextos y el lenguaje ubicuo en arc42 §8 (o enlazarlos desde allí).
- No reescribir ADR aceptados: crear uno nuevo y marcar el anterior como reemplazado.
- Ejecutar el scanner y publicar el Quality Gate de SonarCloud del hash revisado.

## Recuento y nota sugerida

**7 de 8 criterios** Cumple.

**Nota sugerida preliminar (propuesta al docente; excepción docente): 4.5 = 1 + 4 × (7/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- No se ejecutó código del equipo; toda la revisión es estática sobre archivos versionados.
- El «verde» del pipeline no se pudo discriminar: la consulta `actions/runs` del hash devuelve 328 ejecuciones, en su mayoría del cron `Keep-alive`, y el job de SonarCloud queda condicionado al token.

## Hallazgos para la planilla

- La evidencia S6 está completa salvo la integración del mapa y el lenguaje ubicuo en arc42 §8.
- Los entregables de S6 se commitean en el estado previo al corte 1 (`20ab43f`, 2026-09-06) y se conservan en la punta actual.
- ADR-0001 y ADR-0002 reescritos tras aceptarse, sin sucesor.
- SonarCloud sin evidencia auditable (scanner condicionado a token, sin Quality Gate público).
- Existe un `master` obsoleto (2026-08-09): la rama calificada es `main`.
