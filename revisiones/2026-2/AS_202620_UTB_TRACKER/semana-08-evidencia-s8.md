# semana-08-evidencia-s8 · UTB Tracker

> Revisión definitiva: hash ae526db, última revisión ≤ cierre (2026-09-28T05:00:00Z) en main.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` (redirige a `AS_202620_UTB_TRACKER`) |
| Estado revisado | `ae526db29b4f2d1f5981536e18438f9a62b1516d` en `origin/main` (2026-09-25T11:36:43-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | código de respuesta y tiempo, con la hora de la comprobación | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio no declara URL pública: `README.md:5-13` documenta solo `http://127.0.0.1:8000`. |
| Health check consultable | ruta y código de respuesta | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. En el repositorio la ruta existe: `app/routers/health.py:6` expone `GET /salud`. |
| Infraestructura como código versionada en el repositorio | rutas de los archivos de infraestructura | No cumple | No hay Dockerfile, docker-compose, `.tf/.tfvars`, `k8s/`, `helm/`, `fly.toml`, `render.yaml`, railway ni Procfile. Lo único cercano es `.github/workflows/ci.yml`, que encadena pasos de despliegue por SSH (`ci.yml:10-21`), no una descripción versionada del entorno. |
| El entorno se puede recrear siguiendo el README | sección del README con el procedimiento | No cumple | `README.md:5-13` y `run.sh` describen el arranque local de desarrollo (`./run.sh` → `127.0.0.1:8000`), no un procedimiento para recrear un entorno desplegado. No declara requisitos previos. |
| Pipeline en verde sobre la rama principal | URL del último run y su conclusión | No cumple | El run `UTB Tracker CI` sobre `ae526db` en `main` concluyó `failure`: https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/36161882569. Los tres commits nuevos (`dc4099d`, `6d7300c`, `ae526db`) tienen su run en rojo. |
| Logs estructurados | archivo de configuración y ejemplo de línea | No cumple | `git grep` de `structlog|winston|pino|logback|serilog|logging.config|json.*formatter` en `ae526db` no devuelve coincidencias; `requirements.txt` no trae librería de logging. |
| Métrica consultable asociada a un escenario de calidad | nombre de la métrica y escenario al que corresponde | No cumple | No hay endpoint `/metrics`, configuración de métricas ni documento que asocie una métrica a QS-01…QS-06. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example`, referencias a secretos en el workflow | Cumple | `app/database.py:15` toma `DATABASE_URL` de `os.environ`; `.github/workflows/ci.yml:15-19` referencia `secrets.SSH_HOST`, `secrets.SSH_USER`, `secrets.SSH_PRIVATE_KEY` y `secrets.WORK_DIR`. Sin `.env` versionado y barrido de credenciales limpio. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | documento con volumen supuesto y cálculo | No cumple | Sin documento de costos y sin mención de costo mensual en el árbol ni en `README.md`. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07*` | No cumple | `docs/arc42/arc42.md:249-278` conserva la plantilla: `Infrastructure Level 1/2` con marcadores `*\<Overview Diagram\>*`, `*\<Infrastructure Element 1\>*`, etc., sin piezas ni ubicaciones reales. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02*` | No cumple | La sección `Restricciones arquitectónicas` de `docs/arc42/arc42.md` lista restricciones técnicas, organizacionales y legales, pero ninguna recoge límite de costo ni condición «sin tarjeta». |
| Un ADR por decisión de plataforma, con alternativa descartada | archivos de `docs/adr/` de esta semana | No cumple | `docs/adr/` solo tiene `0001-estilo-arquitectonico`, `0002-cambio-stack-fastapi-flutter` y `0003-integracion-sincrona`; ninguno decide plataforma de despliegue ni verifica la capa gratuita. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | El clon sin autenticación de `ISCOUTB/AS_202620_TRACTAR` responde y redirige a `AS_202620_UTB_TRACKER`. | Cumple | El repositorio fue renombrado al nuevo nombre del proyecto; conserva el patrón `AS_202620_<PROYECTO>` y es público. `EQUIPOS.md` aún registra el nombre corto antiguo. |
| Estructura mínima presente | En `ae526db` existen `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Las seis rutas están presentes; arc42 vive en un único `arc42.md` en lugar de secciones numeradas. |
| Estado calificado identificable | `origin/main`, `ae526db29b4f2d1f5981536e18438f9a62b1516d`, 2026-09-25T11:36:43-05:00. | Cumple | Último commit anterior al cierre en la rama principal. |
| Nombres de ADR según la convención | Tres ADR con nombres `NNNN-titulo-en-kebab-case.md`; el filtro de la convención no devuelve salida. | Cumple | — |
| ADR aceptados no reescritos | `git log --follow` de cada ADR en `ae526db` muestra un solo commit (el de creación): `5f923cd`, `e88a3d6`, `9cf1ac9`. | Cumple | No hay ediciones posteriores a la aceptación. |
| `docs/ia.md` al día para la semana | Último commit sobre el archivo: `e84871f`, 2026-08-16. Sin entradas del periodo y sin rechazos con motivo. | No cumple | El registro no crece desde agosto; no documenta nada descartado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | El run `UTB Tracker CI` de `ae526db` en `main` concluyó `failure`; no hay `sonar-project.properties` ni paso del scanner ni URL pública de análisis. | No cumple | Un pipeline en rojo es no conformidad; no se compensa con que el workflow haya arrancado. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de credenciales en `ae526db` sin coincidencias; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` y `-S'AKIA'` sin resultados. | Cumple | Barrido limpio. |
| Contribución de todos los integrantes | `shortlog -sne` en `ae526db` consolidado por identidad: Sebastián García (22 commits, dos correos del mismo autor) y Joriel Samir (3 commits). | No cumple | Solo 2 de los 4 integrantes declarados aparecen; Gerónimo y Mateo no tienen commits en el historial. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subió tarde o corrigió entregas anteriores, aquí se nota.

- **Punta actual revisada**: `ae526db29b4f2d1f5981536e18438f9a62b1516d` 2026-09-25T11:36:43-05:00 `hotfix` (`origin/main`).
- **Veredicto**: con pendientes.
- **Commits posteriores al cierre**: ninguno sobre `origin/main`.
- Resumen: la punta actual coincide con el estado calificado, así que no hay entregas tardías. Los tres commits del 25 de septiembre (`dc4099d`, `6d7300c`, `ae526db`) añadieron un paso de despliegue por SSH al workflow y cambiaron la base de datos a `DATABASE_URL`, pero no versionaron infraestructura de despliegue ni documentación S8; de hecho dejaron el pipeline en rojo. La entrega S8 sigue sin existir.

Pendientes que siguen abiertos:
- URL pública del sistema accesible desde fuera de la red de la universidad.
- Infraestructura como código versionada y procedimiento de recreación del entorno.
- Pipeline en verde sobre la rama principal (hoy en rojo).
- Logs estructurados y métrica consultable asociada a un escenario de calidad.
- Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita.
- arc42 sección 7 con una caja por pieza y sección 2 con límite de costo.
- Un ADR por decisión de plataforma con alternativa descartada y capa gratuita verificada.
- Análisis estático en SonarCloud con URL pública y Quality Gate.
- Registro de uso de IA actualizado con rechazos justificados.
- Evidencia de commits de los integrantes que no aparecen en el historial.

## Recuento y nota sugerida

**1 de 10 criterios graduables.**

**Propuesta provisional al docente — `nota = 1 + 4 × (1/10) = 1.4`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- URL del sistema y health check: diferidos por decisión docente. La URL se entrega por Moodle y no está disponible en esta pasada; no se abrió ni se probó ningún despliegue. El repositorio solo prueba la ruta `/salud` en `app/routers/health.py:6`.
- Pipeline: solo se recuperaron runs del workflow `UTB Tracker CI`; no hay otro workflow sobre `main` en el estado calificado.

## Hallazgos para la planilla

- La punta de `main` (`ae526db`) coincide con el estado calificado; no hubo commits posteriores al cierre.
- El pipeline quedó en rojo (`runs/36161882569`) tras los hotfix del 25 de septiembre; el paso `Deploy via SSH` invoca `secrets.SSH_*` sin que el runner configure Python antes.
- No existe infraestructura como código ni URL pública: el README solo expone `http://127.0.0.1:8000`.
- Sin logs estructurados, sin métricas y sin documento de costos.
- arc42 §7 sigue siendo plantilla y §2 no recoge límite de costo ni condición «sin tarjeta».
- Ningún ADR trata la plataforma de despliegue.
- `docs/ia.md` no crece desde 2026-08-16 y no registra rechazos con motivo.
- El repositorio fue renombrado a `AS_202620_UTB_TRACKER`; `EQUIPOS.md` aún lista el nombre corto anterior.
- Dos de los cuatro integrantes declarados siguen sin commits en el historial.
