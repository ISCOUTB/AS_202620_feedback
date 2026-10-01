# Semana 8 · Despliegue reproducible, CI y observabilidad · LostVault

> Revisión definitiva: hash `4a9ecc944731d0af243724b26a08d5deee22d7e3`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/main`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `4a9ecc94` en `origin/main` (2026-09-27T23:52:06-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |
| URL de despliegue | no consultada: fila diferida por decisión docente (se entrega por Moodle) |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. | No verificado | El repo declara la URL pública `https://backend-nu-self-91.vercel.app` en `docs/arc42/07_vista_despliegue.md:14` y `docs/despliegue/evidencias-profesor.md:10` (Vercel Hobby). El README no la declara. No se abrió. |
| Health check consultable | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. | No verificado | `backend/main.py:173-176` implementa `GET /health` → `{"status":"ok"}`. No se consultó el endpoint desplegado. |
| Infraestructura como código versionada en el repositorio | `backend/Dockerfile:1-17`, `docker-compose.yml:1-17` (servicio backend con healthcheck) e `infra/terraform/main.tf` (proveedor Vercel). | Cumple | El `backend/vercel.json` que citan arc42 §7 y `infra/terraform/README.md` no existe en el hash calificado; la IaC sí está cubierta por Dockerfile, Compose y Terraform. |
| El entorno se puede recrear siguiendo el README | `README.md` §«Instalar / Ejecutar el corte vertical / Analizar y probar»: `flutter pub get`, `flutter run -d chrome`, `flutter analyze`, `flutter test`. | Cumple | Reproduce la app local; el backend se documenta aparte en `backend/DEPLOY_VERCEL.md`. |
| Pipeline en verde sobre la rama principal | Runs `36379490154` (Flutter checks), `36379490092` (Backend checks) y `36379489990` (Build, con SonarCloud + Quality Gate) sobre `4a9ecc94`, todos `completed/success`. | Cumple | https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/36379489990 |
| Logs estructurados | `backend/main.py:27-46`: `JsonFormatter` que emite JSON con `time, level, message` + `request_id, endpoint, method, status_code, duration_ms` (`measure_latency`, `main.py:104-129`); ejemplo en `docs/despliegue/evidencias-profesor.md` §3. | Cumple | `test_api.py` prueba que el token JWT nunca aparece en logs. |
| Métrica consultable asociada a un escenario de calidad | `GET /metrics` (`backend/main.py:179-187`) devuelve `p95_ms` por endpoint; `docs/despliegue/estimacion-costo-mensual.md` §2 liga el p95 de `GET /objects` al escenario de rendimiento (95 % ≤ 2 s, 200 concurrentes). | Cumple | En producción el p95 sale `null` (el estado no acumula entre invocaciones serverless); la limitación está declarada en arc42 §7 y el cálculo se prueba en un mismo proceso. |
| Secretos fuera del código y tomados del entorno o del almacén | `backend/.env.example:1-3` (plantilla); `backend/main.py:50-55` lee `JWT_SECRET` del entorno y falla al arrancar si falta; `build.yml` usa `secrets.SONAR_TOKEN`; no hay `.env` versionado. | Cumple | Los patrones detectados por `git grep` son lecturas de variables de entorno, no credenciales embebidas. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/despliegue/estimacion-costo-mensual.md` §3: supuestos de volumen (~6.000 invocaciones/mes), cuota gratuita de Vercel Hobby verificada y punto de cruce (1 M invocaciones/mes). | Cumple | Resultado estimado 0 USD/mes; se declara el plan Pro ($20/mes) como salida al agotar la capa gratuita. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07_vista_despliegue.md`: tabla por pieza (sitio, API, base de datos, archivos, trabajos programados, pipeline) con su ubicación real. | Cumple | Distingue lo desplegado de lo planeado y declara la limitación de estado en memoria. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02_restricciones.md`: «Sin infraestructura propia con presupuesto… servicios de nivel gratuito». | Cumple | El límite de costo (cero/capa gratuita) está en §2; la condición «sin tarjeta» se explicita en ADR-0003 y en la estimación, no se repite en §2. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0003-plataforma-despliegue-vercel.md`: decisión de Vercel con alternativas descartadas (servidor de laboratorio, Render/Fly.io) y capa gratuita verificada. | Cumple | Un ADR para la decisión de plataforma de la API; no agrupa otras piezas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia y observaciones | Estado |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_LostVault`, clonado sin autenticación. | Cumple |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`. | Cumple |
| Estado calificado identificable | `origin/main` `4a9ecc94`, 2026-09-27T23:52:06-05:00, anterior al cierre. | Cumple |
| Nombres de ADR según la convención | `docs/adr/000.3-despliegue-busqueda-lostvault.md` no cumple `NNNN-titulo-en-kebab-case.md` (el propio ADR-0003 reconoce el typo de numeración). | No cumple |
| ADR aceptados no reescritos | ADR-0001 (aceptado; editado en `edd78d7`, 2026-08-24) y ADR-0002 (aceptado en `c91a71e`, 2026-09-20; editado en `b561576`, 2026-09-27) fueron editados sin reemplazo declarado. | No cumple |
| `docs/ia.md` al día para la semana | Actualizado en `5a96601` (2026-09-27) con lo aceptado y lo rechazado (Vercel y Render, entre otros). | Cumple |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Hay `sonar-project.properties`, el workflow invoca el scanner y el run del hash calificado está en verde con el paso de Quality Gate, pero el repo no aporta la URL pública del análisis/Quality Gate (`evidencias-profesor.md` §8 solo remite a `sonarcloud.io`). | No cumple |
| Sin credenciales en el repositorio ni en el historial | `git grep` sin credenciales reales (solo lecturas de `JWT_SECRET`/`var.vercel_api_token`), sin `.env` versionado. | Cumple |
| Contribución de todos los integrantes | Cuatro personas consolidadas: Roy 45+1, Fausto-4 33+2+1 (mismo correo), Shamara 17+4, Kiefer 9+2 (mismo correo). | Cumple |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `a5faf6a` en `origin/main` (2026-09-28T00:11:11-05:00).
- **Commits posteriores al cierre:** `ccad9ad` (2026-09-28T00:09:52-05:00, «Update DEPLOY_VERCEL.md with Swagger UI documentation») y `a5faf6a` (2026-09-28T00:11:11-05:00, «Revise Swagger UI documentation section»). No cambian la matriz.
- **Veredicto:** ficha S8 completa (10/10 graduables), con tres no conformidades transversales.
- Resumen: el equipo desplegó la API en Vercel, documentó la vista de despliegue real, añadió logs JSON, el endpoint `/metrics` ligado al escenario de rendimiento, IaC (Dockerfile/Compose/Terraform), estimación de costos con punto de ruptura y un ADR de plataforma. Los pendientes son el URL público del Quality Gate y las convenciones/ediciones de ADR.

## Recuento y nota sugerida

10 de 10 criterios graduables Cumple.

**Propuesta provisional al docente — `nota = 1 + 4 × (10/10) = 5.0`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- «URL del sistema accesible desde fuera de la red de la universidad» y «Health check consultable»: pendientes de calificar (URL por Moodle).
- URL pública del análisis de SonarCloud y estado del Quality Gate.
- Convención de nombres del ADR `000.3` y ediciones de ADR-0001/ADR-0002 sin reemplazo declarado.
- `backend/vercel.json` citado por arc42 §7 y Terraform no existe en el repositorio.

## Hallazgos para la planilla

- Mejora sustancial frente a la preliminar (4/12 → 10/10 graduables): despliegue en Vercel, IaC, observabilidad y costos incorporados.
- El pipeline del hash calificado está en verde (Flutter, Backend y Build con SonarCloud).
- `docs/adr/000.3-despliegue-busqueda-lostvault.md` incumple la convención de nombres de ADR.
- ADR-0001 y ADR-0002 tienen ediciones posteriores a su aceptación sin reemplazo declarado.
- El p95 de `/metrics` no acumula en producción (estado en memoria de una función serverless); la limitación está declarada, no ocultada.
- `backend/vercel.json` se cita como IaC clave pero no existe en el hash calificado.
- Hay dos commits posteriores al cierre (documentación); no afectan la matriz.
