# semana-08-evidencia-s8 · Tienda virtual UTB

> Revisión definitiva: hash 858e78f9e34ee4e205bdc84982ed8b04bd0dbb0d, última revisión ≤ cierre (2026-09-28T05:00:00Z) en origin/main.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `858e78f` en `origin/main` (2026-09-27T15:36:51-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | README.md:112 declara `https://tienda-virtual-utb-acme-8eed.vercel.app` y API `https://tienda-utb-api.onrender.com`; docs/despliegue-s8.md:3-10 repite las URLs. No se abrió. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio sí prueba la declaración de una URL pública y de sus rutas operativas (README.md:112-117). |
| Health check consultable | Rutas declaradas y presentes en código: `@app.get("/health")` backend/app/main.py:67, `@app.get("/health/ready")` :73 y `@app.get("/metrics")` :91; documentadas en README.md:113-117. No se consultó. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio prueba que las rutas existen (`backend/app/main.py:67,73,91`) y el workflow `keepalive.yml` golpea `/health`. |
| Infraestructura como código versionada en el repositorio | `backend/Dockerfile`, `frontend/Dockerfile`, `compose.yaml`, `render.yaml` (blueprint de la API) y `frontend/vercel.json`. Hash `858e78f`. | Cumple | IaC real por pieza, con el entorno local en Compose y el despliegue declarado en `render.yaml`. |
| El entorno se puede recrear siguiendo el README | README.md:144-165 «Arranque local» (`cp .env.example .env` + `docker compose up --build`), con URLs de arranque y procedimiento de pruebas. | Cumple | El README documenta la recreación con un solo comando y los requisitos previos (Docker + Compose). |
| Pipeline en verde sobre la rama principal | No se recuperó ningún run de la revisión calificada. El listado de `actions/runs` de `main` (total 384) queda monopolizado por el cron `keepalive.yml` cada 10 min; con las dos llamadas permitidas (per_page=10 y per_page=100) solo se alcanzan los 100 runs más recientes, todos `Keep-alive` success sobre `bc38c9b` (posterior al cierre). | No verificado | Con el presupuesto de API de esta pasada no se alcanzó el run de `858e78f` (ni de `Pruebas` ni de `Keep-alive`), así que no hay conclusión del hash calificado que citar. Haría falta una consulta filtrada por `head_sha=858e78f…` o la vista de Actions. |
| Logs estructurados | Configuración: `JsonFormatter(logging.Formatter)` en backend/app/shared/logging.py:19 y `configure_logging()` :37; README.md lo describe (`logs JSON`) y la suite de observabilidad lo cubre. | Cumple | Una línea JSON por evento con campos estables (timestamp, level, logger, message + `extra`), sin texto libre. |
| Métrica consultable asociada a un escenario de calidad | `GET /metrics` (backend/app/main.py:91) alimentado por `ObservabilityMiddleware` (metrics.py:38) y `snapshot()` (metrics.py:91); ligada explícitamente al escenario 4 de disponibilidad (metrics.py:5 y :110-112). | Cumple | La métrica declara su escenario (`docs/escenarios-calidad.md`, escenario 4) y expone conteo, errores 5xx y latencia p50/p95 por ruta. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example` versionado (raíz); `compose.yaml:8` exige `POSTGRES_PASSWORD` vía `.env`; `render.yaml:16-18` declara `DATABASE_URL` con `sync: false` (dashboard, nunca el repo); sin `.env` versionado; barrido de secretos limpio. | Cumple | Las variables están declaradas y separadas del código y las de producción las inyecta la plataforma; `.env` está git-ignorado. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | docs/costos-despliegue.md:8 «Supuestos de volumen» (≤10 000 req/mes, ≤50 MB), :19 «Costo por pieza en el mes» y :40 «Punto de ruptura de la capa gratuita». | Cumple | Parte del volumen del escenario, costea pieza por pieza y declara el punto de ruptura de cada capa gratuita (Vercel, Render, Neon, UptimeRobot). |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | docs/arc42/arc42-template-EN.md:408 «Deployment View»; :456 «Infrastructure Level 2 — public deployment» con un diagrama por pieza (Vercel, Render, Neon, monitor) y tabla de mapeo. | Cumple | Una caja por pieza con dónde se ejecuta; se evalúa en el archivo arc42 único, desviación de ruta admitida por CONTRATO §2. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | docs/arc42/arc42-template-EN.md:119 «Architecture Constraints»; :128 restricción «Zero monthly cost and no credit card required for the deployment». | Cumple | Ambas condiciones están recogidas como restricciones con su justificación. |
| Un ADR por decisión de plataforma, con alternativa descartada | docs/adr/0003-frontend-vercel.md (Vercel vs contenedor/estático, capa gratuita verificada), 0004-api-contenedor-render.md (Render vs serverless/Fly/Railway, capa gratuita verificada) y 0005-postgres-neon.md (Neon vs Render Postgres/Supabase, capa gratuita verificada). | Cumple | Una decisión de plataforma por pieza (web, API y base de datos), cada una con alternativas descartadas y capa gratuita verificada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB`; clon anónimo OK en `858e78f`. | Cumple | Nombre con la convención y visibilidad pública verificada por clon sin autenticación. |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/` (0001-0005), `docs/c4/` (context, container), `docs/aspectos.md`, `docs/ia.md` en `858e78f`. | Cumple | Las seis rutas de CONTRATO §2 están presentes; arc42 vive en un único archivo, no en `docs/arc42/01..12` (desviación de ruta, no ausencia). |
| Estado calificado identificable | `origin/main` `858e78f` (2026-09-27T15:36:51-05:00) ≤ cierre 2026-09-28T05:00:00Z. | Cumple | Rama principal y hash anterior al cierre registrados. Existe `master` pero es residual (2026-08-09); la principal es `main` (`HEAD -> refs/heads/main`). |
| Nombres de ADR según la convención | `docs/adr/0001-monolito-modular.md` … `0005-postgres-neon.md`. | Cumple | Los cinco siguen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | `git log --follow`: ADR-0001 creado `f4602a3` (2026-08-21) y editado `e8ae57d` (2026-08-31); ADR-0002 creado `0416e62` (2026-09-15) y editado `befb0bc` (2026-09-27); ADR-0003/0004/0005 creados `9b31d8f` (2026-09-27) y editados `886825d` (2026-09-27) para registrar URLs de producción. Sin ADR sucesor declarado. | No cumple | Se editaron ADR ya aceptados sin declarar reemplazo; ya venía registrado desde S7 (ADR-0001). |
| `docs/ia.md` al día para la semana | Commits en la ventana S8: `9b31d8f` (2026-09-27) y `befb0bc` (2026-09-27); la última entrada documenta lo descartado con su motivo (p. ej. no reescribir el cuerpo del ADR-0002). | Cumple | El registro creció dentro del periodo y documenta las propuestas descartadas y su razón. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `sonar-project.properties` y `.sonarcloud.properties` existen; el job `sonarcloud` en `.github/workflows/tests.yml:44-56` está condicionado a `SONAR_TOKEN != ''`; README.md:119-120 declara una URL pública de SonarCloud, pero `docs/ia.md` (entrada del 2026-09-27) deja `SONAR_TOKEN` como pendiente. Sin run del scanner citado para el hash calificado ni estado de Quality Gate verificable. | No cumple | Faltan la segunda y la tercera evidencia que exige CONTRATO §8 (run que ejecutó el scanner para el hash revisado y URL pública con Quality Gate); falta una de las tres y se documenta como no conformidad. |
| Sin credenciales en el repositorio ni en el historial | `git grep` §9 sobre `858e78f`: solo coincidencias en un HTML de terceros (`docs/openapi/contratos-tienda-virtual.html`, variables `token` de SVG); sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | Sin credenciales reales; `.env` está git-ignorado y Compose exige la contraseña por entorno. |
| Contribución de todos los integrantes | `git shortlog -sne 858e78f` consolidado por correo: Jasen/Jasen Yukopila (12+3 = 15, mismo correo), RAZOR7150 (11), pxtroniwnl (6), shalom-A26 (2). | Cumple | Los cuatro integrantes declarados en EQUIPOS.md tienen commits. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subió tarde o corrigió entregas anteriores, aquí se nota.

- **Punta actual revisada**: `bc38c9bab2830e8f2c855c0e36542d849565955e 2026-09-28T10:22:29-05:00 Corrige la region de Render, que estaba sin verificar, y registra el estado real de las credenciales`
- **Veredicto**: con pendientes (commits posteriores al cierre)
- Resumen: la punta de `main` va cuatro commits por delante del hash calificado (`bc38c9b`, `f28563b`, `4665f80`, `4904d94`, todos del 2026-09-28), que consolidan pendientes y declaran infraestructura de producción con Terraform; no cuentan para la matriz, solo como hallazgo. En el estado calificado (`858e78f`) el equipo ya había desplegado el frontend en Vercel, la API en Render y la base en Neon, con IaC, observabilidad, costo y ADR de plataforma; el avance respecto a la preliminar (0/12) es muy grande.

Pendientes que siguen abiertos:
- Publicar/entregar la URL por Moodle para calificar las dos filas de despliegue (no se probó ninguna URL).
- Cerrar la evidencia del pipeline: el cron `keepalive.yml` inunda el listado de runs y oculta el run de la revisión; conviene citar el run del hash calificado.
- SonarCloud: configurar `SONAR_TOKEN`, ejecutar el scanner y publicar el Quality Gate del hash revisado.
- No reescribir ADR aceptados (0001 y 0002) sin declarar uno sucesor.

## Recuento y nota sugerida

**9 de 10 criterios graduables Cumple** (dos filas de despliegue quedan diferidas; la fila de pipeline queda No verificado por límite de recuperación del run).

**Propuesta provisional al docente — `nota = 1 + 4 × (9/10) = 4.6`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- «URL del sistema accesible desde fuera de la red de la universidad» y «Health check consultable»: diferidas por decisión docente; la URL se entrega por Moodle. El repositorio declara las URLs (README.md:112-117) y las rutas existen en código (`backend/app/main.py:67,73,91`), pero no se abrió ninguna.
- «Pipeline en verde sobre la rama principal»: no se recuperó ningún run de la revisión calificada dentro del presupuesto de API; el cron `keepalive.yml` (cada 10 min) monopoliza el listado y `per_page=100` solo alcanza runs post-cierre.

## Hallazgos para la planilla

- S8 con avance real: despliegue por piezas (Vercel + Render + Neon), IaC (`render.yaml`, `compose.yaml`, Dockerfiles, `frontend/vercel.json`), logs JSON, `/metrics` con escenario 4, costo con supuestos y ADR 0003/0004/0005.
- Las dos filas de despliegue quedan diferidas (URL por Moodle); no se abrió ninguna URL.
- Pipeline no verificable con el presupuesto de API: el cron `keepalive.yml` inunda `actions/runs` (384 runs; los 100 más recientes son todos keep-alive). Citar el run del hash calificado.
- Transversal: ADR-0001 (`e8ae57d`) y ADR-0002 (`befb0bc`) reescritos tras aceptarse, sin sucesor.
- Sin evidencia verificable de SonarCloud (job condicionado a `SONAR_TOKEN`); falta el Quality Gate público.
- La punta de `main` tiene cuatro commits posteriores al cierre (2026-09-28) que no entran en la matriz.
