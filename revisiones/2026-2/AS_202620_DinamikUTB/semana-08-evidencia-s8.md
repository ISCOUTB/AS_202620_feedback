# semana-08-evidencia-s8 · DinamikUTB

> Revisión definitiva: hash 287c65d, última revisión ≤ cierre (2026-09-28T05:00:00Z) en origin/master.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `287c65d` en `origin/master` (2026-09-27T23:57:31-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

> El estado calificado se movió respecto de la pasada temprana (que revisó `65202f2`): el equipo empujó el 27 de septiembre. Se releyeron del repositorio todas las filas que la pasada preliminar había dejado como no incluidas.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | README.md:319-336 declara el frontend en `https://iscoutb.github.io/AS_202620_DinamikUTB/` y el backend en `https://dinamikutb-api.onrender.com`; `docs/arc42/07-deployment-view.md:25` repite las URLs. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. No se abrió ninguna URL. El repositorio sí declara URL pública (backend Render y frontend GitHub Pages). |
| Health check consultable | Ruta `GET /health` en `backend/app/main.py:69` (ejecuta `SELECT 1` y responde `{"status":"ok"}`); `render.yaml:18` fija `healthCheckPath: /health`; README.md:329 publica la URL de health. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio prueba que la ruta de health existe (`backend/app/main.py:69`) y está declarada en `render.yaml:18`. |
| Infraestructura como código versionada en el repositorio | `render.yaml` (Blueprint: web service + Postgres, `fromDatabase`), `.github/workflows/deploy-pages.yml` (publicación del frontend Flutter) y `.github/workflows/ci.yml`. | Cumple | El entorno desplegado se describe en `render.yaml`, no en pasos manuales. |
| El entorno se puede recrear siguiendo el README | README.md «Inicio Rápido» (comando único `start.bat`) y «Cómo recrear el entorno desplegado» (README.md:344): pasos de Render (Blueprint), GitHub Pages, `.env.example` y `docs/costos.md`. | Cumple | Cubre arranque local y recreación del entorno desplegado. |
| Pipeline en verde sobre la rama principal | Run `CI` sobre `master` del hash `287c65d`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/36379851321 (2026-09-28T04:57:34Z). El workflow `.github/workflows/ci.yml` corre backend, frontend y el job `sonarcloud`. | Cumple | Run atado al hash calificado de `master`. |
| Logs estructurados | `backend/app/core/logging_config.py:6` define `JsonFormatter` (una línea JSON con `ts`, `level`, `logger`, `message` y campos extra); `backend/app/main.py` emite `http_request` con `method`, `path`, `status` y `duration_ms`. Ejemplo citado en README.md:356-357. | Cumple | El grep de la ficha (`structlog|...|logging\.config`) no lo detecta porque el archivo usa guion bajo; verificado a mano. |
| Métrica consultable asociada a un escenario de calidad | `GET /metrics` en `backend/app/main.py:78`, implementado en `backend/app/core/metrics.py:1`; asociado al escenario **Q-05 (disponibilidad)** en README.md:358 y `docs/arc42/07-deployment-view.md`. Expone `dinamikutb_http_requests_total` y `dinamikutb_http_request_duration_seconds`. | Cumple | Métrica nombrada y ligada explícitamente a Q-05. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example` versionado (`DATABASE_URL`, `CORS_ORIGINS`); `render.yaml` inyecta `DATABASE_URL` con `fromDatabase` (secreto del proveedor); `.github/workflows/ci.yml:78` usa `secrets.SONAR_TOKEN`; no hay `.env` versionado ni coincidencias del barrido de secretos. | Cumple | Variables declaradas y separadas del código; toma desde el almacén del proveedor y de GitHub Secrets. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/costos.md`: volumen supuesto derivado de Q-05 (100 concurrentes × 10 min = 6 000 peticiones), costo por pieza y punto de ruptura (frontend ~33 000 cargas/mes; backend 750 h/mes; Postgres free expira a los 30 días). | Cumple | Cálculo con supuestos propios y ruptura por pieza, no solo el catálogo del proveedor. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07-deployment-view.md` §7.1 con diagrama (Internet → GitHub Pages → Render → Postgres) y tabla `:25` con pieza, dónde corre, URL, costo y ADR. | Cumple | Una caja por pieza y su ubicación real. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02-architecture-constraints.md:56` «Límite de costo y despliegue sin tarjeta de crédito», reforzado en la tabla 2.4 (`:142`). | Cumple | Restricciones de costo cero y sin tarjeta declaradas como tales. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0005-plataforma-despliegue-backend.md` (Render), `docs/adr/0006-plataforma-despliegue-frontend.md` (GitHub Pages) y `docs/adr/0007-persistencia-render-postgres.md` (Postgres), cada uno con alternativas descartadas. | Cumple | ADR-0007 deja la fecha de verificación de la capa gratuita como `<completar>`; 0005 y 0006 sí contrastan límites concretos (750 h/mes, 100 GB). |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_DinamikUTB`, clonado sin autenticación; responde al protocolo git. | Cumple | Nombre conforme a `AS_202620_<PROYECTO>` y público. |
| Estructura mínima presente | Árbol de `287c65d`: `docs/arc42/01..12`, `docs/adr/0001..0007`, `docs/c4/*.puml`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Seis rutas del contrato presentes; `docs/api/` es material extra. |
| Estado calificado identificable | Rama `origin/master`; hash `287c65d` (2026-09-27T23:57:31-05:00), último ≤ cierre 2026-09-28T05:00:00Z. | Cumple | Un commit posterior al cierre (`d72a10a`), registrado en overall. |
| Nombres de ADR según la convención | `docs/adr/0001-seleccion-monolito-modular.md` … `0007-persistencia-render-postgres.md`, todos `NNNN-kebab-case.md`. | Cumple | Siete nombres conformes. |
| ADR aceptados no reescritos | Los siete declaran `status: Aceptado` (`docs/adr/0001..0007:4`). `git log --follow` por ADR: `0001` creado `3d5aad8` (2026-08-23) y editado `15d38f9` (2026-09-01T01:01:30-05:00); `0002` creado `842cab5` (2026-08-30) y editado `bc70d93` (2026-09-01T01:03:13-05:00); `0005` creado `8ca6482` y editado `627b10a` y `243e712` (2026-09-27); `0006` creado `62107f0` y editado `099f0ba` y `807f320` (2026-09-27). Ninguno declara reemplazo. | No cumple | CONTRATO §4 prohíbe editar un ADR aceptado. Las ediciones de ADR-0001/0002 y de ADR-0005/0006 son posteriores a su aceptación y no hay ADR que los reemplace. |
| `docs/ia.md` al día para la semana | Historial de `docs/ia.md` con entradas dentro del periodo; última `c1af95e` (2026-09-27T21:45:21-05:00). Contenido con rechazos y motivo (p. ej. «Rechazado parcialmente» por sobrecarga visual y «Rechazado por ahora» del lock file). | Cumple | Registra lo rechazado, no solo lo aceptado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `sonar-project.properties` (projectKey `ISCOUTB_AS_202620_DinamikUTB`), paso `SonarCloud Scan` en `.github/workflows/ci.yml:77-78` (`secrets.SONAR_TOKEN`), run verde `36379851321` sobre `287c65d` y proyecto público en `https://sonarcloud.io/project/overview?id=ISCOUTB_AS_202620_DinamikUTB` con Quality Gate `OK` (consultado por API pública). | Cumple | Las tres evidencias del contrato §8 presentes. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de secretos sobre `287c65d` sin coincidencias reales; ningún `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin resultados. | Cumple | La única coincidencia es `id-token: write` (permiso de workflow, no una credencial). |
| Contribución de todos los integrantes | `git shortlog -sne 287c65d` consolida por correo idéntico en 4 personas: `404Vargas`+`JuanchisV`+«Juan José Vargas Pérez» (187), `Daniel-dev02`+«LUIS DANIEL» (60), `gillianisperez-prog` (26) y `Eramirezr` (12). | Cumple | Coinciden con los 4 integrantes de `EQUIPOS.md`; desbalance anotado en la planilla. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `d72a10a` (`2026-09-28T00:09:14-05:00`, «Update README.md»), 1 commit posterior al cierre.
- **Veredicto**: al día.
- Resumen: la punta actual de `master` conserva todas las piezas de S8 revisadas en el hash calificado (render.yaml, ADR-0005/0006/0007, arc42 §7, logs JSON, `/metrics` ligado a Q-05, `.env.example` y estimación de costos). El único commit posterior al cierre solo actualiza el README; no cambia la matriz. La entrega cierra los hallazgos de S8 vigentes a excepción de la fila transversal de ADR aceptados.

Pendientes que siguen abiertos:
- No editar ADR aceptados: ADR-0001, 0002, 0005 y 0006 tienen ediciones posteriores a su aceptación sin ADR de reemplazo.
- URL y health check: quedan pendientes de calificar con la URL de Moodle.

## Recuento y nota sugerida

**10 de 10 criterios graduables.** (Las 2 filas de despliegue quedan diferidas y no entran en el recuento.)

**Propuesta provisional al docente — `nota = 1 + 4 × (10/10) = 5.0`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- URL del sistema accesible desde fuera de la red: pendiente de calificar; el README declara las URLs pública y de health, pero no se abrió ninguna.
- Health check consultable: pendiente de calificar; la ruta existe en el código (`backend/app/main.py:69`) y `render.yaml:18`.
- Sustentación: no evaluable desde el repositorio.
- Fila transversal de ADR aceptados no reescritos: No cumple, abierta.

## Hallazgos para la planilla

- El estado calificado cambió respecto de la pasada temprana: la definitiva usa `287c65d` (27/09), no `65202f2`.
- S8 resolvió todas las piezas del repositorio: IaC (`render.yaml`), logs JSON, `/metrics` ligado a Q-05, `.env.example`, costos con punto de ruptura, arc42 §7 y §2, y un ADR por decisión de plataforma.
- Se mantiene abierto el hallazgo de ADR aceptados editados después de su aceptación (ADR-0001/0002/0005/0006), sin ADR de reemplazo.
- SonarCloud ya cumple las tres evidencias del contrato §8 (config, run que invoca el scanner y Quality Gate público `OK`).
- URL y health check quedan pendientes de calificar por decisión docente (se entregan por Moodle).
