# Evidencia S8 · Verifacts

> Revisión definitiva: hash d2d7b5c, última revisión ≤ cierre (2026-09-28T05:00:00Z) en master.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `d2d7b5c3d5b64a7008c20d1aa0961d3e0c69053f` en `origin/master` (2026-09-25T16:38:43-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | código de respuesta y tiempo, con la hora de la comprobación | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio sí declara URL pública: `docs/despliegue.md:1-2` publica `https://verifacts-api.onrender.com` y `https://verifacts-web.onrender.com`. |
| Health check consultable | ruta y código de respuesta | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. La ruta existe en código: `app/api/routes.py:57` expone `GET /health`, y `render.yaml` la declara como `healthCheckPath`. |
| Infraestructura como código versionada en el repositorio | rutas de los archivos de infraestructura | Cumple | `render.yaml` define `verifacts-api` (Docker) y `verifacts-web` (Static Site); `Dockerfile`, `.dockerignore` y el prototipo `serverless-prototype/template.yaml` + `samconfig.toml` completan la IaC versionada. |
| El entorno se puede recrear siguiendo el README | sección del README con el procedimiento | Cumple | `README.md` §13.1 documenta el arranque con un único comando: `docker build -t verifacts . && docker run -p 8000:8000 verifacts`, usando el mismo `Dockerfile` del despliegue. |
| Pipeline en verde sobre la rama principal | URL del último run y su conclusión | Cumple | Para `d2d7b5c` en `master`: `Tests` concluyó `success` (runs/36192827481) y `SonarCloud` concluyó `success` (runs/36192827575). |
| Logs estructurados | archivo de configuración y ejemplo de línea | Cumple | `app/observability.py:19-40` implementa `JsonFormatter` y `configure_logging`; `docs/despliegue.md:34` aporta una línea JSON con timestamp, nivel, request_id, ruta, estado y duración. |
| Métrica consultable asociada a un escenario de calidad | nombre de la métrica y escenario al que corresponde | Cumple | `app/observability.py:94-124` expone el histograma `verifacts_http_request_duration_seconds` en `GET /metrics`; `docs/escenarios-de-calidad.md:51-54` lo vincula con Q-01 (P95 ≤ 3 s). |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example`, referencias a secretos en el workflow | Cumple | Existen `.env.example` y `frontend/.env.example`, no hay `.env` versionado, y `.github/workflows/sonarcloud.yml:24` toma `SONAR_TOKEN` de GitHub Secrets. `git grep` de credenciales limpio. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | documento con volumen supuesto y cálculo | Cumple | `docs/costos.md` supone decenas de peticiones diarias, desglosa las dos piezas y calcula $0/mes; identifica el punto de ruptura (plan Starter para persistencia; ~40 000 invocaciones/mes en el prototipo Lambda). |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07*` | Cumple | `docs/arc42/07-despliegue.md:5-56` muestra cajas separadas para web, API y SQLite dentro de Render, y §7.2 documenta las piezas del CI. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02*` | Cumple | `docs/arc42/02-restricciones.md:91-104` recoge `R-TEC-05` (costo cero y sin tarjeta) con su impacto. |
| Un ADR por decisión de plataforma, con alternativa descartada | archivos de `docs/adr/` de esta semana | Cumple | `docs/adr/0004-plataforma-despliegue.md:1-83` decide Render y descarta Terraform y AWS Lambda; `docs/adr/0005-comparacion-lambda-render.md` compara Render frente a Lambda para la API con la capa gratuita verificada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | El clon sin autenticación de `ISCOUTB/AS_202620_Verifacts` respondió correctamente. | Cumple | El hallazgo histórico de repositorio no visible ya no describe el estado actual. |
| Estructura mínima presente | En `d2d7b5c` existen `README.md`, `docs/arc42/` (11 archivos), `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Las seis rutas están presentes. |
| Estado calificado identificable | `origin/master`, `d2d7b5c3d5b64a7008c20d1aa0961d3e0c69053f`, 2026-09-25T16:38:43-05:00. | Cumple | Último commit anterior al cierre en la rama principal. |
| Nombres de ADR según la convención | Cinco ADR con nombres `NNNN-titulo-en-kebab-case.md`; el filtro de la convención no devuelve salida. | Cumple | — |
| ADR aceptados no reescritos | `git log --follow` muestra el commit `9430845` (2026-09-23, «enlazar commit de implementacion en cada ADR y corregir parrafo de aspectos.md») sobre ADR 0001-0004 después de su aceptación, sin ADR de reemplazo declarado. | No cumple | Los ADR aceptados se editaron posteriormente sin declarar un reemplazo. |
| `docs/ia.md` al día para la semana | `docs/ia.md:22` registra el incremento de despliegue del 22–23 de septiembre (commit `50568f1`), incluida la decisión rechazada del disco persistente y su motivo. | Cumple | El archivo crece dentro del periodo y documenta lo descartado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Los workflows `Tests` y `SonarCloud` del hash están en verde y `docs/despliegue.md:37` publica el análisis, pero el propio documento declara el Quality Gate general en rojo. | No cumple | Un workflow exitoso no convierte un Quality Gate rojo en cumplimiento. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de credenciales en `d2d7b5c` sin coincidencias; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` y `-S'AKIA'` sin resultados. | Cumple | Barrido limpio. |
| Contribución de todos los integrantes | `shortlog -sne` en `d2d7b5c` consolidado por correo: `PedroC1213` con 240 commits (dos correos) y `Cristian Cardeño` con 33 commits (dos correos). | No cumple | Solo 2 de los 3 integrantes declarados aparecen; el tercer integrante no tiene commits en el historial. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subió tarde o corrigió entregas anteriores, aquí se nota.

- **Punta actual revisada**: `dae98e8d322b33898dd24622b0f5fbbeca6fa5a2` 2026-09-28T22:24:54-05:00 `S9: pruebas de frontera y erosion, medicion Q-01/Q-05` (`origin/master`).
- **Veredicto**: con pendientes.
- **Commits posteriores al cierre**: numerosos commits S9 el 2026-09-28 17:35–17:51 COT y 22:22–22:24 COT (`1893548`, `a73c226`, `5ae78ac`, `6bd30b3`, `4d62f13`, `dee1e81`, `a1f2327`, `9d21d61`, `d9f4300`, `33651ec`, `3e769d6`, `015d14f`, `68ece59`, `2f8e698`, `bc07a5e`, `6b3429f`, `6196c37`, `58b6a55`, `f03a149`, `c670698`, `8538bd5`, `dae98e8`). Varios runs `Tests` de esos commits están en rojo.
- Resumen: el estado calificado (`d2d7b5c`) consolida el incremento de despliegue y observabilidad, con el prototipo serverless y su medición de cold start. La punta actual ya trabaja la semana 9; esos commits no cambian la matriz S8, pero dejan la rama con runs de `Tests` en rojo en varios de ellos.

Pendientes que siguen abiertos:
- Comprobar la URL y `/health` con la hora del evaluador en el próximo cierre (aquí diferido por decisión docente).
- Corregir el Quality Gate general de SonarCloud, documentado en rojo.
- Confirmar la contribución del tercer integrante sin inferir identidades.
- Dejar de editar ADR aceptados: los enlaces de implementación posteriores deberían ir en un ADR nuevo o en la trazabilidad, no reescribiendo el aceptado.

## Recuento y nota sugerida

**10 de 10 criterios graduables.**

**Propuesta provisional al docente — `nota = 1 + 4 × (10/10) = 5.0`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- URL del sistema y health check: diferidos por decisión docente. El repositorio declara las URL públicas en `docs/despliegue.md:1-2` y la ruta `GET /health` en `app/api/routes.py:57`; no se abrió ni se probó ningún despliegue.
- Medición formal del P95 de Q-01: la propia documentación la declara pendiente; no forma parte de las filas graduables de S8.

## Hallazgos para la planilla

- La revisión publicada cambió: el estado calificado pasó de `ef48c08` (preliminar) a `d2d7b5c`.
- Dos commits nuevos desde la preliminar: `28c1ac5` (fecha y hora de las comprobaciones de URL y health) y `d2d7b5c` (prototipo serverless + ADR-0005).
- Los dos workflows del hash calificado están en verde; el Quality Gate general de SonarCloud sigue documentado en rojo.
- arc42 §2 y §7, el ADR de plataforma (0004), el ADR comparativo (0005), el comando Docker del README, el vínculo métrica–Q-01 y el documento de costos están presentes.
- Cuatro ADR aceptados fueron editados el 2026-09-23 (`9430845`) sin ADR de reemplazo.
- El tercer integrante declarado sigue sin commits en el historial.
- Hay commits y runs S9 posteriores al cierre que no cambian esta matriz.
