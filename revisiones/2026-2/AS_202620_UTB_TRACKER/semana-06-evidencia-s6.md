# semana-06-evidencia-s6 · TRACTAR

> Excepción docente: la ventana de S6 no tuvo actividad en la rama principal (el último commit
> anterior al cierre siguió siendo el del corte anterior). Por indicación expresa del docente, la
> matriz de S6 se evalúa sobre la **punta actual de la rama principal**, de modo que incluye
> trabajo de semanas posteriores. Es una excepción: no es comparable con el resto de la pasada de
> S6 y la nota sigue siendo una propuesta al docente.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_UTB_TRACKER` (antes `AS_202620_TRACTAR`; el URL anterior redirige aquí) |
| Estado revisado | `ae526db29b4f2d1f5981536e18438f9a62b1516d` en `origin/main` (2026-09-25T11:36:43-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Estado histórico al cierre de S6 | `7cfb872` (sin actividad en la ventana de S6) |
| Regla aplicada | excepción docente: se califica la punta actual |
| Revisor | revisión manual de evidencias públicas |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | No hay mapa de contextos delimitados en el árbol de `ae526db`. `docs/arc42/arc42.md:82-108` solo contiene contexto de negocio/técnico con el C4 nivel 1 de sistema. Búsqueda de `núcleo compartido`, `customer/supplier`, `capa anticorrupción`, `bounded context` sin coincidencias. | No cumple | Un C4 de contexto de sistema no es un mapa de contextos; no se declara tipo de relación entre contextos del dominio. |
| Tabla módulo a datos con dueño único por entidad | No existe tabla módulo→datos en el árbol. `docs/arc42/arc42.md:160-168` enumera bloques con su estado pero sin dueño de datos. Búsqueda de `módulo a datos` y `dueño único` sin coincidencias. | No cumple | Se esperaba cada entidad con un único módulo dueño; no se encontró. |
| La tabla cubre las entidades que existen en el código | `app/models.py:16,24,37` define `Usuario`, `Recurso` y `Prestamo`; ninguna tabla de propiedad cubre esas entidades. | No cumple | La tabla exigida no existe, así que no puede contrastarse con el esquema real. |
| No conformidades de propiedad de datos detectadas sobre el código actual | No hay lista de no conformidades. Además existe una no conformidad real no reportada: `app/routers/loans.py:32` (módulo `prestamos`) escribe `recurso.estado`, propiedad del módulo `recursos` (`app/models.py:24`). | No cumple | Se esperaba la lista con entidad, módulo dueño esperado y ubicación observada; no se encontró. |
| Plan de corrección por no conformidad | No hay plan de corrección asociado a no conformidades de propiedad. | No cumple | Sin lista de no conformidades no hay acción de corrección que verificar. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | `docs/arc42/arc42.md:280-294`: §8 «Cross-cutting Concepts» sigue con los marcadores de plantilla `<Concept 1>`, `<Concept 2>`, `<Concept n>`; sin lenguaje ubicuo ni mapa. | No cumple | Se esperaba §8 aplicada con lenguaje ubicuo y mapa de contextos incorporados. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | `docs/arc42/arc42.md:201-203`: «Level 3» está `(pendiente)`; no hay ADR de reajuste de límites. El único ADR nuevo frente a S5 es `docs/adr/0003-integracion-sincrona.md` (S7), que decide el estilo de integración, no un reajuste de límites. | No cumple | Sin C4 nivel 3 ni ADR del reajuste. |
| Aspectos relacionables con los contextos del mapa | `docs/aspectos.md` no tiene columna de contexto y, al no existir mapa, no hay contextos con los que relacionar sus filas; A-06 declara «C3 pendiente». | No cumple | La ficha exige que la relación con los contextos sea comprobable por escrito. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_UTB_TRACKER`, público; clon anónimo correcto en `ae526db`. El nombre sigue la convención `AS_202620_<PROYECTO>`. | Cumple | Hallazgo: el repositorio fue renombrado desde `AS_202620_TRACTAR` (que ahora redirige), aunque `EQUIPOS.md` y la carpeta de revisiones conservan el nombre antiguo. |
| Estructura mínima presente | Árbol de `ae526db`: `README.md`, `docs/arc42/arc42.md`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`. | Cumple | Las seis rutas obligatorias están presentes. |
| Estado calificado identificable | `origin/main`, `ae526db29b4f2d1f5981536e18438f9a62b1516d`, 2026-09-25T11:36:43-05:00. | Cumple | Excepción docente: se usa la punta actual en lugar del último commit ≤ cierre. |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico.md`, `0002-cambio-stack-fastapi-flutter.md`, `0003-integracion-sincrona.md`. | Cumple | Numeración y kebab-case conformes. |
| ADR aceptados no reescritos | `git log --follow` sobre cada ADR muestra un único commit de creación (`0001` en `5f923cd`, `0002` en `e88a3d6`, `0003` en `9cf1ac9`). | Cumple | Sin reescritura posterior a la aceptación. |
| docs/ia.md al día para la semana | Último cambio de `docs/ia.md` en `e84871f` (2026-08-16); sin entrada del periodo S6 ni de semanas posteriores. | No cumple | El registro no crece desde agosto y no documenta rechazos del periodo. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `.github/workflows/ci.yml` no invoca ningún scanner de SonarCloud; la consulta `actions/runs` por el hash completo devuelve 1 run, `UTB Tracker CI` en `main`, `completed`/`failure`. | No cumple | Falta la triple evidencia de §8 (scanner, run y Quality Gate públicos); además el run del hash revisado está en rojo. |
| Sin credenciales en el repositorio ni en el historial | `git grep` del patrón §9 sin coincidencias; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` vacío. | Cumple | Barridos limpios. |
| Contribución de todos los integrantes | `git shortlog -sne`: Sebastian Garcia Devoz (22 commits consolidando dos identidades de git del mismo correo, más el correo institucional) y Joriel Samir (3). Geronimo Cadena y Mateo Millán sin commits. | No cumple | 2 de 4 integrantes aparecen en el historial. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `ae526db29b4f2d1f5981536e18438f9a62b1516d` · 2026-09-25T11:36:43-05:00 · «hotfix».
- **Veredicto**: con pendientes.
- Desde el estado histórico de S6 (`7cfb872`) la rama avanzó con trabajo de semanas posteriores: contrato OpenAPI y prueba de contrato (`docs/contracts/`), ADR 0003 de integración síncrona, ampliación del C4 nivel 2 y ajustes de `app/database.py`. Nada de eso cubre los entregables de S6 (mapa de contextos, tabla módulo a datos, no conformidades y plan, arc42 §8).
- El pipeline del hash revisado concluye en `failure` y sigue sin análisis estático público.

Pendientes que siguen abiertos:

- Construir el mapa de contextos delimitados con relaciones tipificadas.
- Construir la tabla módulo a datos con dueño único y cubrir las entidades de `app/models.py`.
- Reportar las no conformidades de propiedad (p. ej. `prestamos` escribiendo `Recurso.estado`) con su plan.
- Aplicar arc42 §8 con lenguaje ubicuo y mapa, y registrar el C4 nivel 3.
- Recuperar el verde del pipeline y añadir la evidencia pública de SonarCloud.
- Incorporar al historial a los integrantes que aún no aparecen.

## Recuento y nota sugerida

**0 de 8 criterios** Cumple.

**Nota sugerida preliminar (propuesta al docente; excepción docente): 1.0 = 1 + 4 × (0/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- No se ejecutó código del equipo; toda la revisión es estática sobre archivos versionados.
- No se verificó «verde» de CI: el único run del hash revisado (`actions/runs`, 1 resultado) concluye en `failure` y no hay Quality Gate público.

## Hallazgos para la planilla

- Repositorio renombrado de `AS_202620_TRACTAR` a `AS_202620_UTB_TRACKER`; conviene actualizar `EQUIPOS.md` y la carpeta de revisiones.
- Sin entregables de S6 en la punta actual: no hay mapa de contextos, tabla módulo a datos, lista de no conformidades ni plan de corrección.
- No conformidad de propiedad no reportada: `prestamos` escribe `Recurso.estado` (`app/routers/loans.py:32`).
- arc42 §8 sigue siendo plantilla y el C4 nivel 3 está pendiente.
- `docs/ia.md` sin cambios desde 2026-08-16; pipeline del hash revisado en rojo y sin SonarCloud público.
