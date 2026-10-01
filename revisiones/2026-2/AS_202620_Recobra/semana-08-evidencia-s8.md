# semana-08-evidencia-s8 · Recobra

> Revisión definitiva: hash 5c7f77b, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `5c7f77b` en `origin/master` (2026-09-27T19:55:59-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

El estado cambió respecto de la pasada temprana: el commit calificado pasó de `8f25313`
(2026-09-19) a `5c7f77b` (2026-09-27). La entrega incorpora `Dockerfile` y `render.yaml`, el
cliente Flutter, logs estructurados, el endpoint de métrica `/metrics`, los ADR 0005 (Render) y
0006 (Neon), la estimación de costo y las secciones 2 y 7 de arc42. Hay un commit posterior al
cierre (`34ab8f2`, 2026-09-28T21:39:38-05:00) que se registra solo en `overall`. Las dos filas de
despliegue quedan diferidas por decisión docente.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `README.md:88` declara `https://recobra-backend.onrender.com`. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. No se abrió ni se consultó ninguna URL. |
| Health check consultable | La ruta existe en el código: `src/salud/salud.controller.ts:3` `@Controller('health')`, `:6` `verificar()` devuelve `{ status: 'ok' }`; `render.yaml` la usa como `healthCheckPath: /health`. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. La ruta está declarada, pero no se consultó por estar diferida la URL. |
| Infraestructura como código versionada en el repositorio | `Dockerfile` multi-stage (Node 20, usuario `node` sin privilegios) y `render.yaml` (Blueprint: `runtime: docker`, `plan: free`, `healthCheckPath: /health`, `autoDeployTrigger: commit`). | Cumple | Describe el entorno, no pasos manuales; el CI valida el mismo `Dockerfile`. |
| El entorno se puede recrear siguiendo el README | `README.md:70` «Infraestructura como código», `:75` «Recrear el entorno» (`docker build`/`docker run`) y `:82` «Desplegar en Render» (Blueprint desde `render.yaml`). | Cumple | Procedimiento documentado con proveedor, variables y pasos. |
| Pipeline en verde sobre la rama principal | Run `ci` de `5c7f77b` en `master`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/36364033272 (2026-09-28T00:56:02Z). | Cumple | Único workflow sobre `master`; todos sus runs en el periodo concluyen `success`, incluido el del hash revisado. |
| Logs estructurados | `src/observabilidad/json-logger.service.ts:12` construye `{ timestamp, level, context, message, ...extra }` y `:19` emite una línea JSON por `console.log`; se inyecta en `src/main.ts:6` `new JsonLoggerService()`. | Cumple | Configuración versionada; una línea JSON por evento con campos. |
| Métrica consultable asociada a un escenario de calidad | `src/observabilidad/metricas.service.ts:6` documenta la métrica ligada al escenario S5; `:35` `escenario: 'S5 (mantenibilidad)'`; `:41` `objetivoP95Ms: 100`; expuesta en `GET /metrics` (`metricas.controller.ts:3`). | Cumple | Nombre de la métrica, escenario y umbral; consultable en `/metrics`. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example` versionado; `render.yaml` `DATABASE_URL` con `sync: false`; el código la lee de `process.env.DATABASE_URL` (`src/infrastructure/persistence/postgres-publicacion.repository.ts:22`, `src/publicaciones/publicaciones.module.ts:25`). Sin `.env` versionado. | Cumple | El valor vive en el panel de Render; sin credenciales en el repositorio ni en el historial. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/despliegue/costo-mensual.md:9` «Los cuatro números», `:29` supuestos derivados del escenario S1 y «Punto en que se rompe la capa gratuita» (750 h de Render, USD 7/mes; 0.5 GB de Neon). | Cumple | Volumen supuesto, costo por pieza ($0) y punto de ruptura. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42.md:185` «Vista de despliegue», `:192` API NestJS en Render, `:194` persistencia PostgreSQL en Neon, cliente Flutter en el dispositivo. | Cumple | Una caja por pieza con su ubicación real. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/arc42.md:42-47` «Restricciones de despliegue (S8)»: sin tarjeta de crédito/débito y límite de costo $0/mes. | Cumple | Ambas restricciones explícitas. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0005-plataforma-despliegue-backend.md` (Render; descarta Fly.io y serverless; free tier verificado) y `docs/adr/0006-plataforma-persistencia-postgresql.md` (Neon; descarta Render PostgreSQL y contenedor propio; free tier verificado). | Cumple | Una decisión por plataforma, cada una con alternativa descartada y capa gratuita verificada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_Recobra`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre `AS_202620_Recobra` conforme y visibilidad pública. |
| Estructura mínima presente | `README.md`, `docs/arc42/arc42.md`, `docs/adr/` (0001-0006), `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Las seis rutas del contrato §2; arc42 consolidado en `docs/arc42/`. |
| Estado calificado identificable | `5c7f77b3da94ed019ade4b959c723444a2ee7c02` en `origin/master`, último commit ≤ cierre: `2026-09-27T19:55:59-05:00 Corregir vitrina (bug real de CSS) y completar costo-mensual.md`. | Cumple | Coincide con el estado revisado; `34ab8f2` es posterior al cierre y solo se registra en `overall`. |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico.md` … `docs/adr/0006-plataforma-persistencia-postgresql.md`. | Cumple | Todos cumplen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | ADR-0001 declara reemplazo por ADR-0002. `git log --follow` hasta el hash revisado: ADR-0002 creado `3a82ca6` (2026-09-05, «Aceptada — 2026-09-05») y editado `f7c1a6c` (2026-09-07, +2); ADR-0003 creado `3a82ca6` y editado `f7c1a6c` (2026-09-07, +57); ADR-0006 creado `e952f5b` (2026-09-27) y editado `7fb48ad` (+9) el mismo día. ADR-0005 tiene un único commit (`81d7b8`). Ninguna edición declara reemplazo. | No cumple | CONTRATO §4 prohíbe editar un ADR aceptado sin declarar reemplazo. ADR-0001 sí declara su reemplazo, pero ADR-0002 y 0003 se editaron dos días después de aceptarse. |
| `docs/ia.md` al día para la semana | `docs/ia.md` incluye la entrada del 2026-09-26 (Evidencia S8) con lo aceptado, lo corregido y lo rechazado (Fly.io, serverless) y su motivo. | Cumple | El archivo crece dentro del periodo y documenta rechazos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `.github/workflows/ci.yml` corre en verde (run 36364033272) y existe `sonar-project.properties`, pero el workflow no invoca el scanner y no hay URL pública del análisis ni estado de Quality Gate. | No cumple | Falta la evidencia de SonarCloud exigida por el contrato §8. |
| Sin credenciales en el repositorio ni en el historial | Barrido sin coincidencias; sin `.env` versionado; `.env.example` con `PORT`; sin claves privadas en el historial. El token de Coveralls señalado en semanas previas pertenece al paquete `debug` y sigue documentado en `docs/no-conformidades.md`. | Cumple | Sin credenciales reales del equipo. |
| Contribución de todos los integrantes | `git shortlog -sne 5c7f77b`: `Cconde31` 44 + `Steamlinker` 1 (consolidado por `.mailmap`), `vylrir` 25, `Fernando Isacc Conde Herrera` 24, `MiguelJacome` 10. | Cumple | Cuatro personas para cuatro integrantes; Fernando ya no queda con contribución mínima. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `34ab8f2b62f3daf7f3005eb4f7d1b4b30e52f97e 2026-09-28T21:39:38-05:00 Unificar esquema de error del contrato y actualizar ADR-0004`.
- **Veredicto:** entrega de la semana completa en la matriz graduable; quedan 2 filas de despliegue diferidas.
- **Resumen:** la punta tiene un commit posterior al cierre (`34ab8f2`), que toca el contrato y el ADR-0004 y no se califica; no cambia la matriz. La entrega S8 cubre las diez filas graduables: `Dockerfile` y `render.yaml`, reproducción en el README, CI en verde sobre `master`, logs estructurados en JSON, métrica `/metrics` ligada al escenario S5, secreto `DATABASE_URL` por configuración del proveedor, estimación de costo con punto de ruptura, arc42 §7 con Render/Neon, restricciones de costo y tarjeta en §2 y un ADR por plataforma (0005 Render, 0006 Neon). Siguen abiertos la evidencia pública de SonarCloud y las ediciones de ADR aceptados.

Pendientes que siguen abiertos:
- URL del despliegue y su comprobación externa (fila diferida por decisión docente).
- Health check con código de respuesta (fila diferida por decisión docente).
- SonarCloud sin invocación en el workflow ni URL pública del Quality Gate (pendiente desde S6).
- ADR-0002 y ADR-0003 editados después de aceptarse sin declarar reemplazo (ADR-0006 con edición el mismo día).

## Recuento y nota sugerida

10 de 10 criterios graduables Cumple.

**Propuesta provisional al docente: 5.0 = 1 + 4 × (10/10).** Quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL del sistema accesible desde fuera de la red universitaria: fila diferida; no se abrió ninguna URL. El README declara `https://recobra-backend.onrender.com`.
- Health check consultable: fila diferida; la ruta `/health` existe en `src/salud/salud.controller.ts:3-7`, pero no se consultó por estar diferida la URL.
- SonarCloud: sin invocación del scanner en el workflow ni URL pública del Quality Gate, por lo que la fila transversal queda en No cumple.
- ADR aceptados editados: ADR-0002 y ADR-0003 (`f7c1a6c`) sin reemplazo declarado; ADR-0006 editado el mismo día de su aceptación.

## Hallazgos para la planilla

- Infraestructura como código versionada en `Dockerfile` y `render.yaml` (Blueprint con `autoDeployTrigger: commit`).
- Último run de CI sobre `master` en el hash revisado en verde: run 36364033272.
- Logs estructurados en JSON (`src/observabilidad/json-logger.service.ts:12,19`) y métrica `latencia_post_publicaciones_ms` ligada al escenario S5 (`metricas.service.ts:6,35,41`).
- Secreto `DATABASE_URL` tomado del panel de Render (`render.yaml` `sync: false`); sin credenciales en el repositorio.
- Costo mensual con supuestos y punto de ruptura; arc42 §7 con Render/Neon y §2 con costo $0 y sin tarjeta.
- ADR 0005 y 0006 separan las decisiones de plataforma con alternativas desestimadas y capa gratuita verificada.
- SonarCloud sigue ausente: fila transversal en No cumple.
- ADR-0002 y ADR-0003 editados sin reemplazo declarado: fila transversal en No cumple.
- El commit calificado `5c7f77b` es anterior al cierre; `34ab8f2` (2026-09-28T21:39:38-05:00) es posterior y no se califica.
