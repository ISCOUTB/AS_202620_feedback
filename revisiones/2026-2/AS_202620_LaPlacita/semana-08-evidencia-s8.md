# Semana 8 · Despliegue reproducible, CI y observabilidad · LaPlacita

> Revisión definitiva: hash `b03a79783e5675b6251d14af5edee077de86e3bd`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `b03a797` en `origin/master` (2026-09-27T19:00:57-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |
| URL de despliegue | no consultada: fila diferida por decisión docente (se entrega por Moodle) |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. | No verificado | El repo sí declara una URL pública: README.md:247 y `docs/semana-08.md:26` citan `https://laplacita-app.graymoss-fdd72159.canadacentral.azurecontainerapps.io` (Azure Container Apps). No se abrió. |
| Health check consultable | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. | No verificado | `app/api/v1/health/route.js:5-7` implementa `GET /api/v1/health`; `src/health.js:5-7` devuelve `{ status: 'ok' }`. No se consultó el endpoint desplegado. |
| Infraestructura como código versionada en el repositorio | `Dockerfile:1-17` (multi-stage Node 22 + `.next/standalone`), `next.config.mjs:2-4` (`output: 'standalone'`) y `.github/workflows/ci.yml:1-57`. | Cumple | La imagen de producción y el pipeline están versionados; no hay descriptor específico del proveedor (se construye con el Dockerfile). |
| El entorno se puede recrear siguiendo el README | `README.md` §«Cómo ejecutar» / «Guía paso a paso»: Node 22, `npm install`, `npm run dev`, `npm test`, `npm run build`/`npm start`. | Cumple | Requisitos previos declarados y comando único de arranque. |
| Pipeline en verde sobre la rama principal | Run `36360634637` sobre `b03a797` en `master`: `completed/success`. Jobs `test` y `contract-test` verdes; `sonar` es informativo (`continue-on-error`, `ci.yml:43-44`). | Cumple | https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/36360634637 |
| Logs estructurados | `src/logger.js:6-16` emite una línea JSON por evento con `ts, level, service, route, tiendaId, pedidoId, mensaje`; ejemplo real en `docs/semana-08.md` §5.2. | Cumple | El PIN y la tarjeta nunca se registran; `tests/observabilidad.test.js` cubre la forma de la línea. |
| Métrica consultable asociada a un escenario de calidad | `src/metricas.js:3-5` asocia contadores a ESC-01 (`pedidosCreados`), ESC-03/A-06 (`pinesRechazados`, `pinesBloqueados`) y ESC-04 (`pagosConfirmados`); expuestos en `app/api/v1/metricas/route.js:5-9`. | Cumple | La asociación métrica↔escenario está en el propio código y en `docs/semana-08.md` §5.2.1. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example:1-5` versiona solo la plantilla; `ci.yml:49` usa `secrets.SONAR_TOKEN`; no hay `.env` versionado ni coincidencias de credenciales (`git grep` y `ls-files`). | Cumple | El despliegue toma las variables del portal de Azure (ADR-0009). |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/semana-08.md` §6 con supuestos S-1…S-5, cálculo por pieza y ruptura ×36; tabla de dimensiones en `docs/adr/0009-despliegue-azure.md`. | Cumple | Total estimado 0 USD/mes; la dimensión más estrecha son las 2 M solicitudes/mes. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42-template-EN.md` §7: diagrama Mermaid + tabla con API Next.js, pipeline, ámbito local, persistencia y ubicación de cada pieza. | Cumple | Una caja por pieza y dónde corre cada una. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/arc42-template-EN.md` §2, RES-06: tope de 5 USD/mes en capa gratuita o de prueba, sin tarjeta asociada. | Cumple | Restricción económica explícita que gobierna el despliegue. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0009-despliegue-azure.md` (Azure vs AWS, capa gratuita verificada), `docs/adr/0010-analisis-sonarcloud.md` (SonarCloud vs solo ESLint) y `docs/adr/0011-base-de-datos-universidad.md` (servidor UTB vs Neon). | Cumple | Un ADR por plataforma; ADR-0003 queda sin modificar y es precisado por estos tres. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia y observaciones | Estado |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_LaPlacita`, clonado sin autenticación. | Cumple |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`. | Cumple |
| Estado calificado identificable | `origin/master` `b03a797`, 2026-09-27T19:00:57-05:00, anterior al cierre. | Cumple |
| Nombres de ADR según la convención | `docs/adr/0001`…`0011` cumplen `NNNN-titulo-en-kebab-case.md`. | Cumple |
| ADR aceptados no reescritos | ADR-0003 (aceptado en `745e799`, 2026-08-30; editado en `95ec841`, 2026-09-06), ADR-0009 (aceptado en `9452e43`, 2026-09-25; editado en `4f38051`, 2026-09-27) y ADR-0010 (aceptado en `c46fd36`, 2026-09-24; editado en `c99f542`, 2026-09-27) fueron editados sin reemplazo declarado. | No cumple |
| `docs/ia.md` al día para la semana | Entradas del 27/09/2026 (despliegue, métricas, correcciones), con propuestas rechazadas y su motivo. | Cumple |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Hay configuración (`sonar-project.properties`) y run de CI público, pero `sonar` es `continue-on-error` y no se aporta la URL pública del Quality Gate: falta la tercera evidencia de CONTRATO §8. | No cumple |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones sin coincidencias, sin `.env` versionado. | Cumple |
| Contribución de todos los integrantes | Cuatro identidades por persona: Jorge 64, Samuel 34, Isaza 18+11 (mismo correo), Mateo 19+1. | Cumple |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `b03a797` en `origin/master` (coincide con el estado calificado).
- **Veredicto:** ficha S8 completa (10/10 graduables), con dos no conformidades transversales.
- Resumen: en el cierre el equipo ya desplegó en Azure Container Apps, con IaC (Dockerfile + CI), observabilidad (logger JSON y `/api/v1/metricas` ligados a ESC-01/03/04), costos con supuestos y ruptura, arc42 §7 y §2 (RES-06) y un ADR por plataforma. El pipeline del hash elegible está en verde. Siguen abiertos el Quality Gate público de SonarCloud y las ediciones de ADR aceptados.
- No hay commits posteriores al cierre en `origin/master`.

## Recuento y nota sugerida

10 de 10 criterios graduables Cumple.

**Propuesta provisional al docente — `nota = 1 + 4 × (10/10) = 5.0`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- «URL del sistema accesible desde fuera de la red de la universidad» y «Health check consultable»: pendientes de calificar (URL por Moodle).
- URL pública del análisis de SonarCloud y estado del Quality Gate.
- Correcciones de ADR aceptados: ADR-0003, ADR-0009 y ADR-0010 editados sin reemplazo declarado.

## Hallazgos para la planilla

- Mejora sustancial frente a la preliminar (3/12 → 10/10 graduables): despliegue documentado, observabilidad y gestión de costos incorporados.
- El pipeline del hash calificado quedó en verde (run `36360634637`); antes fallaba.
- SonarCloud sigue como job informativo (`continue-on-error`); sin URL pública de Quality Gate.
- ADR-0003, ADR-0009 y ADR-0010 tienen ediciones posteriores a su aceptación (trazabilidad, evidencia de despliegue y un enlace, respectivamente) sin reemplazo declarado.
- `docs/ia.md` crece durante la semana y registra rechazos con motivo técnico.
