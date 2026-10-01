# semana-08-evidencia-s8 · ElMapita

> Revisión definitiva: hash e5c3ac6, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/main`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `e5c3ac6` en `origin/main` (2026-09-27T16:26:27-06:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

El estado cambió respecto de la pasada temprana: el commit calificado pasó de `afae3be`
(2026-09-20) a `e5c3ac6` (2026-09-27), que incorpora `render.yaml`, `backend/Dockerfile`,
observabilidad (`nestjs-pino` y Prometheus), `docs/adr/0004-despliegue-render-docker.md` y
`correcciones.md`. No hay commits posteriores al cierre.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | El repositorio no declara una URL pública concreta: `README.md` no publica ninguna y `docs/arc42/arc42-template-EN.md:508` sigue listando «Host: Cloud Run / Render / VPS»; el runbook de `docs/adr/0004-despliegue-render-docker.md:121-126` usa el marcador `https://<nombre-del-servicio>.onrender.com`. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. No se abrió ni se consultó ninguna URL. |
| Health check consultable | La ruta existe en el código: `backend/src/health.controller.ts:14` `@Controller('health')`, `:20` `@Get()` y `:80` `throw new ServiceUnavailableException(checks)` cuando Supabase no está sano; `render.yaml:17` la usa como `healthCheckPath: /health`. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. No se consultó ninguna URL. |
| Infraestructura como código versionada en el repositorio | `render.yaml:13` `runtime: docker`, `:16` `plan: free`; `backend/Dockerfile` multi-stage (Node 22) que construye y sirve la API; `.github/workflows/ci.yml:161` `docker build`. | Cumple | Blueprint de Render más Dockerfile; describe el entorno, no pasos manuales. |
| El entorno se puede recrear siguiendo el README | `README.md:92` «Inicio Rápido», `:94` prerrequisitos, `:132`/`:137` `scripts/dev.sh` y `scripts/dev.ps1`, `:162` `npm run test`. | Cumple | Documenta el arranque local; el entorno público se cubre en el runbook de ADR-0004, no en el README. |
| Pipeline en verde sobre la rama principal | Run `CI` de `e5c3ac6`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/36355303177 (2026-09-27T22:26:36Z). | Cumple | Último run sobre `main` en el hash revisado; incluye backend, contract, secrets, docker, frontend y quality-gate. |
| Logs estructurados | `backend/src/shared/observability/logger.module.ts:2` `nestjs-pino`, `:7` `pinoHttp`, `:9` JSON crudo en producción, `:11` pretty solo en desarrollo y `:18` `redact: ['req.headers.authorization']`. | Cumple | Configuración versionada; en producción emite una línea JSON por request con método/ruta/status/latencia. |
| Métrica consultable asociada a un escenario de calidad | `backend/src/shared/observability/metrics.module.ts:11` `PrometheusModule` en `path: 'metrics'`, `:18` histograma `http_request_duration_seconds` y `:19` ligado a **EC-01** (rutas de edificio y de piso). | Cumple | La métrica nombra el escenario EC-01 y las operaciones que mide; consultable en `/metrics`. |
| Secretos fuera del código y tomados del entorno o del almacén | `backend/.env.example` versionado con placeholders; `render.yaml:24-30` `sync: false` para `FRONTEND_URL`, `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY` y `SUPABASE_ANON_KEY`; `.github/workflows/ci.yml:53-55` (y otros) referencian `secrets.SUPABASE_*`; sin `.env` versionado. | Cumple | Sin credenciales reales; `.gitleaksignore` documenta dos falsos positivos históricos. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/adr/0004-despliegue-render-docker.md:89` «Estimación de costo mensual», `:93-99` tabla por pieza con punto de cruce: Render Starter $7/mes y Supabase Pro $25/mes bajo supuestos de tráfico (<100 peticiones/día). | Cumple | Volumen supuesto, costo por pieza y punto de ruptura; el total pasa a $7/mes si el cold start rompe el p95 de EC-01. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42-template-EN.md:485` «Vista de despliegue»; diagrama en `:489-512` con caja de dispositivos cliente, servidor NestJS en contenedor y Supabase Cloud gestionado. | Cumple | Hay una caja por pieza y su ubicación; el host del backend sigue listado como «Cloud Run / Render / VPS» (`:508`) y conviene fijarlo a Render según ADR-0004. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/arc42-template-EN.md:51-60`: la sección 2 solo enumera RES-01…RES-04 (académica, GPS, red y rendimiento); no incluye límite de costo ni la restricción de «sin tarjeta». | No cumple | La estimación económica vive en ADR-0004, no como restricción en la sección 2. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0004-despliegue-render-docker.md:37-42`: elige Render y descarta Fly.io, Railway y el servidor del laboratorio; `:93-96` verifica la capa gratuita. | Cumple | Un ADR de plataforma con alternativas, consecuencias y punto de cruce de costo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_ElMapita`, clonado sin autenticación; rama principal `origin/main`. | Cumple | Nombre `AS_202620_ElMapita` conforme y visibilidad pública. |
| Estructura mínima presente | En `e5c3ac6`: `docs/arc42/`, `docs/adr/` (0001-0004), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2; arc42 en un único archivo y C4 en Markdown más PNG. |
| Estado calificado identificable | `e5c3ac6ecb598c8e126aaa091cce9af01fe818c4` en `origin/main`, último commit ≤ cierre (2026-09-28T05:00:00Z): `2026-09-27T16:26:27-06:00 url 27-09-2026`. | Cumple | Coincide con el estado revisado; no hay commits posteriores al cierre. |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico-propuesto.md`, `0002-restriccion-rendimiento-compatibilidad-dispositivos.md`, `0003-contrato-openapi-versionado.md` y `0004-despliegue-render-docker.md`. | Cumple | Los cuatro cumplen `NNNN-titulo-en-kebab-case.md`; el directorio contiene además un `.gitkeep`. |
| ADR aceptados no reescritos | ADR-0001 declara `status: Accepted` (2026-08-22) y fue editado en `07b36f4` (2026-08-30T23:31:03-05:00) sin declarar reemplazo; ADR-0003 se editó en `9ee88c5` (2026-09-27T00:57:42-06:00) después de crearse en `afae3be` (2026-09-20). | No cumple | El contrato §4 prohíbe editar un ADR aceptado sin reemplazo declarado; ninguna de las dos ediciones lo declara. |
| `docs/ia.md` al día para la semana | Historial de `docs/ia.md` con commits del periodo, incluido el del hash revisado `e5c3ac6` (2026-09-27) y el seguimiento de la sesión S08 en `166ce9e`. | Cumple | El registro crece durante la semana y documenta rechazos con su motivo técnico. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `.github/workflows/ci.yml` corre en verde (run 36355303177), pero no existe `sonar-project.properties` ni un paso `sonar` en el workflow; no hay URL pública de análisis ni Quality Gate. | No cumple | Falta la evidencia de SonarCloud exigida por el contrato §8. |
| Sin credenciales en el repositorio ni en el historial | Barrido con coincidencias solo en tipos y datos de prueba; sin `.env` versionado; `backend/.env.example` con placeholders; `.gitleaksignore` documenta dos falsos positivos. | Cumple | Sin credenciales reales; un token de plantilla NestJS quedó en el historial, se eliminó y está en el allowlist. |
| Contribución de todos los integrantes | `git shortlog -sne e5c3ac6`: `RobotDRMX` 26, `Rodrigo Vazquez Rico` 4, `dgarza2705` 1. | No cumple | Diego Rosales Garza (`dgarza2705`) y Rodrigo Vazquez Rico quedan identificados; Angel Fabian Gutierrez Gomez no tiene ningún commit atribuible en todo el historial. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `e5c3ac6ecb598c8e126aaa091cce9af01fe818c4 2026-09-27T16:26:27-06:00 url 27-09-2026`
- **Veredicto**: con pendientes
- Resumen: la punta actual coincide con el estado calificado (no hay commits posteriores al cierre). La entrega S8 quedó mayormente cubierta: infraestructura como código (`render.yaml` + `backend/Dockerfile`), CI en verde con `quality-gate`, logs estructurados con pino, métrica `http_request_duration_seconds` ligada a EC-01, secretos vía `render.yaml`/`secrets.*`/gitleaks, estimación de costo con supuestos y punto de ruptura, y ADR-0004 por la decisión de plataforma. Siguen abiertos la evidencia de SonarCloud, el límite de costo y la condición de tarjeta en arc42 §2, las ediciones de ADR aceptados y la contribución de un integrante.

Pendientes que siguen abiertos:
- URL del despliegue y su comprobación (fila diferida por decisión docente).
- Health check consultable con código de respuesta (fila diferida por decisión docente).
- arc42 §2 sin límite de costo ni restricción de tarjeta.
- SonarCloud sin configuración, run ni Quality Gate públicos (pendiente desde S6).
- ADR-0001 y ADR-0003 editados después de aceptarse sin declarar reemplazo.
- Angel Fabian Gutierrez Gomez sin commits atribuibles en el historial.

## Recuento y nota sugerida

9 de 10 criterios graduables Cumple.

**Propuesta provisional al docente: 4.6 = 1 + 4 × (9/10).** Quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL del sistema accesible desde fuera de la red universitaria: fila diferida; no se abrió ninguna URL. El repositorio no declara una URL pública concreta.
- Health check consultable: fila diferida; la ruta `/health` existe en `backend/src/health.controller.ts:14,20` y `render.yaml:17`, pero no se consultó por estar diferida la URL.
- arc42 §2 (costo y tarjeta): la sección no recoge el límite de costo ni la restricción de tarjeta.
- SonarCloud: sin configuración del scanner ni invocación en el workflow, por lo que la fila transversal queda en No cumple.
- ADR aceptados editados: ADR-0001 (`07b36f4`) y ADR-0003 (`9ee88c5`) sin reemplazo declarado.
- Contribución: un integrante declarado no aparece en el historial.

## Hallazgos para la planilla

- Infraestructura como código versionada en `render.yaml` y `backend/Dockerfile`; el CI construye la imagen (`ci.yml:161`).
- Último run de CI sobre `main` en el hash revisado en verde: run 36355303177.
- Logs estructurados con `nestjs-pino` (`logger.module.ts:2,7,18`) y métrica Prometheus `http_request_duration_seconds` ligada a EC-01 (`metrics.module.ts:18-19`).
- ADR-0004 decide plataforma con alternativas descartadas y estimación de costo con punto de ruptura; la estimación no está recogida como restricción en arc42 §2.
- SonarCloud sigue ausente: fila transversal en No cumple.
- ADR-0001 y ADR-0003 editados después de aceptarse sin declarar reemplazo: fila transversal en No cumple.
- Historial de contribución concentrado: un integrante sin commits atribuibles.
- El commit calificado `e5c3ac6` es anterior al cierre y no hay commits posteriores.
