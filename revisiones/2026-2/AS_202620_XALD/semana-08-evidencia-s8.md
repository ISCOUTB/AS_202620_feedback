# Evidencia S8 · XALD

> Revisión definitiva: hash `f90f28d3e3b0fe3da81d71b8cc9d9d10bdf07491`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `f90f28d3` en `origin/master` (2026-09-27T21:56:48-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación | 2026-10-01 (auditoría local sobre clon público efímero) |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `README.md:5` declara `https://xald-backend.onrender.com`; no se abrió. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El README registra una comprobación propia (2026-09-27 21:19 COT, `http=200`). |
| Health check consultable | `backend/app/main.py:93` define `GET /health` → `{"status":"ok"}`; `render.yaml:8` `healthCheckPath: /health`. No se consultó. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. La ruta existe en código y el Blueprint la usa como sonda. |
| Infraestructura como código versionada en el repositorio | `render.yaml` (Blueprint: servicio Docker, plan Free, health check, `envVars`), `backend/Dockerfile` (python:3.12-slim + uvicorn) y `.env.example`. | Cumple | El entorno desplegado está descrito como código, no como pasos manuales. |
| El entorno se puede recrear siguiendo el README | `README.md` §4 "Cómo recrear el entorno desplegado" (cuenta Render, New → Blueprint sobre `master`, `XALD_API_KEY`, Deploy Hook, push). | Cumple | Procedimiento reproducible de 5 pasos con el mismo `render.yaml`. |
| Pipeline en verde sobre la rama principal | Run `Android CI` de `master` para `f90f28d3`, conclusión `success` (2026-09-28T02:56:50Z): https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/36371759708 | Cumple | Único workflow que corre sobre `master`; jobs `build-and-test`, `backend-tests` y `deploy-backend`. |
| Logs estructurados | `backend/app/main.py:17-35` clase `FormatoJSON` (una línea JSON por evento con `timestamp`, `nivel`, `evento` y campos); ejemplo en `README.md:51` (`ruta`, `codigo`, `duracion_ms`). | Cumple | `backend/Dockerfile` apaga el access-log de uvicorn (`--no-access-log`). |
| Métrica consultable asociada a un escenario de calidad | `backend/app/main.py:40-52` define `xald_sync_conflictos_resueltos_total` (Prometheus) ligada a **ESC-05** (resolución LWW); `README.md:73`. | Cumple | La métrica nombra el escenario y la restricción RT-05. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example` (sin valores); `render.yaml` declara `XALD_API_KEY` con `sync: false`; `backend/app/main.py:58` la lee de `os.environ`; `.github/workflows/ci.yml:67,71` usa `${{ secrets.RENDER_DEPLOY_HOOK }}`. | Cumple | Sin `.env` versionado ni credenciales reales en el árbol. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/arc42/07-Deployment View.md:34-53` "7.2 Costo Mensual": supuesto de 50 usuarios y ~7 500 transacciones/mes, costo por pieza, fuentes fechadas y punto de ruptura (Render 750 h, Gemini ~300 usuarios). | Cumple | El cálculo sale del volumen del escenario, no solo del catálogo. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07-Deployment View.md:7-31`: diagrama y tabla con Aplicación Android, Backend XALD en Render y Gemini API, cada uno con su ubicación y forma de despliegue. | Cumple | Sección antes vacía; ahora completa (infra + costo). |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02-Architecture constraints.md:21` RO-02 (costo $0) y `:23` RO-03 (sin tarjeta). | Cumple | Ambas como restricciones organizacionales con origen. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0008-plataforma-de-despliegue.md` (Render, alternativas Heroku/AWS/Fly/Railway descartadas, capa gratuita verificada), `0009-distribucion-app.md`, `0010-observabilidad.md`. | Cumple | Un ADR por pieza decidida, cada uno con alternativa y verificación de capa gratuita. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon público sin autenticación de `ISCOUTB/AS_202620_XALD`. | Cumple | — |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` en `f90f28d3`. | Cumple | — |
| Estado calificado identificable | `origin/master`, `f90f28d3`, 2026-09-27T21:56:48-05:00. | Cumple | Último commit ≤ cierre; sin commits posteriores. |
| Nombres de ADR según la convención | Diez ADR `NNNN-titulo-en-kebab-case.md` (0001–0010). | Cumple | — |
| ADR aceptados no reescritos | Los ADR 0001–0005 recibieron una edición el 2026-09-27 (fecha de aprobación), después de aceptados y sin reemplazo declarado: `efcc390` (0001), `44c6096` (0002), `6b7d514` (0003), `a660a64` (0004), `86c48ca` (0005). | No cumple | Procede de la regla de no editar un ADR aceptado; ningún ADR declara reemplazo de otro. |
| `docs/ia.md` al día para la semana | Último cambio `809ea69` (2026-09-27T15:51), con entradas de la Semana 8 y columna de rechazados poblada. | Cumple | El archivo crece dentro del periodo revisado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | El workflow `ci.yml` no invoca el scanner de SonarCloud ni existe `sonar-project.properties`; no hay URL pública de análisis con Quality Gate. | No cumple | Faltan la línea del scanner y la URL pública del Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | Barridos de claves y tokens sin coincidencias materiales; sin `.env` versionado. | Cumple | — |
| Contribución de todos los integrantes | `shortlog -sne` con cuatro identidades consolidadas: `dilanbejarano011` (186), `colmenares2007-crypto` (94), `xaviergarciadiaz20-commits` (64), `axeljruiz717-hash` (58). | Cumple | Cuatro identidades = cuatro integrantes declarados. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `f90f28d3` (`origin/master`), la misma del estado calificado.
- No hay commits posteriores al cierre en `origin/master`.
- El proyecto pasó de un esqueleto Android a un backend desplegado en Render con IaC (`render.yaml`, `Dockerfile`), health check, logs JSON, métrica Prometheus ligada a ESC-05, ADR de plataforma/observabilidad, arc42 §7 con costo y §2 con la restricción de tarjeta. El CI corre en verde sobre `master`.
- Sigue pendiente el análisis estático con SonarCloud (el CI no lo invoca) y se conservan los `__pycache__` versionados en `backend/app/`.

## Recuento y nota sugerida

**10 de 10 criterios graduables Cumple.**

**Propuesta provisional al docente — `nota = 1 + 4 × (10/10) = 5.0`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- Las dos filas de despliegue (URL y health) quedan pendientes de calificar por la entrega de la URL en Moodle.
- Integrar el scanner de SonarCloud al pipeline y publicar la URL del análisis con el Quality Gate (no conformidad transversal).
- Dejar de reescribir ADR aceptados: registrar los cambios como ADR nuevos y marcar el anterior como reemplazado.
- Retirar `backend/app/__pycache__/*.pyc` del control de versiones.

## Hallazgos para la planilla

- El estado S8 cambió por completo respecto a la punta de S7 (`62a0d15`): aparecen infraestructura, despliegue, observabilidad, costo y tres ADR de plataforma.
- La puntuación de la ficha sube de 2/12 (preliminar) a 10/10 graduables.
- El pipeline transversal retrocede: sigue sin análisis estático auditable; además, la fila de ADR aceptados no reescritos pasa a No cumple por las ediciones del 2026-09-27.
