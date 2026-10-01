# Evidencia S8 · uniTeam

> Revisión definitiva: hash `0f3da0f36f8cd7b829106667de88a56a1bc81f54`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `0f3da0f3` en `origin/master` (2026-09-27T22:52:09-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación | 2026-10-01 (auditoría local sobre clon público efímero) |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `README.md:20` declara API `https://uniteam-api.onrender.com/health` y sitio `https://uniteam-web.onrender.com`; no se abrió. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. |
| Health check consultable | `app/main.py:99` define `GET /health` (200 o 503 según la base de datos); `README.md:142`; `render.yaml` `healthCheckPath: /health`. No se consultó. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. La ruta existe en código y Render la usa como sonda. |
| Infraestructura como código versionada en el repositorio | `Dockerfile` (multi-destino `api`/`idp-dev`), `web/Dockerfile`, `render.yaml` (Blueprint: API Docker y sitio estático), `compose.yaml`, `.github/workflows/despliegue.yml`. | Cumple | Las cuatro piezas están descritas como código; la base y el IdP son servicios de terceros. |
| El entorno se puede recrear siguiendo el README | `README.md` y `docs/despliegue/guia.md`: `docker compose up` en local y orden de despliegue en Render con los servicios gestionados. | Cumple | El arranque local con un comando está documentado y el despliegue tiene guía. |
| Pipeline en verde sobre la rama principal | El run de `CI` sobre `master` para `0f3da0f3` concluye `failure` (2026-09-28T03:52:55Z): https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/36375435263 | No cumple | `CI` (pruebas + SonarCloud) está en rojo en el estado calificado; el workflow de comprobación del despliegue sí quedó en verde, pero no compensa al CI. |
| Logs estructurados | `app/observabilidad.py`: `FormatoJSON` escribe una línea JSON por evento con `momento`, `nivel`, `origen`, `mensaje` y campos de `extra` (`id_peticion`, `metodo`, `ruta`, `estado`, `duracion_ms`); `app/main.py` llama `configurar_registro()`. | Cumple | El access-log de uvicorn se apaga y se reemplaza por el middleware propio. |
| Métrica consultable asociada a un escenario de calidad | `app/observabilidad.py`: `uniteam_tablero_latencia_segundos` y `/metricas/esc-01` (**ESC-01**) y `uniteam_accesos_denegados_total` (**ESC-03**); `app/main.py` expone `/metricas` y `/metricas/esc-01`. | Cumple | Cada métrica nombra su escenario y el resumen compara el p95 con el umbral. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example`; `render.yaml` declara las variables con `sync: false`; `.github/workflows/ci.yml` genera la contraseña de MySQL de un solo uso; `compose.yaml` toma los valores de `.env` (defaults solo de desarrollo). | Cumple | En producción los secretos viven en la configuración de Render; sin `.env` versionado. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/despliegue/costos.md`: supuestos S1–S8 (50 usuarios, ~35 000 peticiones/mes), tamaños medidos, consumo por pieza, total 0 USD y puntos de ruptura (arranque en frío, Aiven sin SLA, horas de instancia, ancho de banda). | Cumple | Calcula desde el volumen del escenario y distingue costo de calidad de servicio. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42-uniteam.md:469-555` (§7.1 infraestructura, §7.2 "Una caja por pieza", §7.3 entornos, §7.4 operación, §7.5 secretos, §7.6 costo). | Cumple | Una caja por pieza (web, API, base de datos, identidad) con su ubicación y ADR. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/arc42-uniteam.md:87` T5: límite de 0 USD/mes y uso sin tarjeta, con verificación de que Render, Aiven y Auth0 no pidieron tarjeta. | Cumple | Restricción técnica con consecuencia arquitectónica. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0007-servir-la-aplicacion-web-como-sitio-estatico.md`, `0008-desplegar-la-api-como-contenedor-en-render.md`, `0009-usar-aiven-for-mysql-como-base-de-datos-gestionada.md`, `0010-usar-auth0-como-proveedor-de-identidad.md`, `0011-mantener-la-api-despierta-con-un-sondeo-externo.md`. | Cumple | Un ADR por pieza, con alternativas comparadas y capa gratuita. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon público sin autenticación de `ISCOUTB/AS_202620_uniTeam`. | Cumple | — |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` en `0f3da0f3`. | Cumple | `docs/adr/` incluye un `.gitkeep`. |
| Estado calificado identificable | `origin/master`, `0f3da0f3`, 2026-09-27T22:52:09-05:00. | Cumple | Último commit ≤ cierre; sin commits posteriores. |
| Nombres de ADR según la convención | Doce ADR `NNNN-titulo-en-kebab-case.md` (0001–0012). | Cumple | — |
| ADR aceptados no reescritos | El ADR 0011 se editó en `0f3da0f` (2026-09-27) después de su creación en `369b0d9` (mismo día), sin reemplazo declarado de ese ADR. | No cumple | Se modificó la sección de consecuencias de un ADR ya marcado como aceptado; el resto de ADR conserva un solo commit. |
| `docs/ia.md` al día para la semana | Entradas del 2026-09-27 y 28 con el trabajo de S8 y la columna de rechazados y su motivo. | Cumple | El archivo crece dentro del periodo revisado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `sonar-project.properties` y `.github/workflows/ci.yml` invocan el scanner con espera del Quality Gate, pero el run de CI del hash revisado está en rojo (`36375435263`); el propio repo lo declara parcial. | No cumple | Un Quality Gate que no termina en un run exitoso no es evidencia auditable del estado calificado. |
| Sin credenciales en el repositorio ni en el historial | Barridos de claves y tokens sin coincidencias; sin `.env` versionado; los defaults de `compose.yaml` son de desarrollo y el despliegue usa `render.yaml`. | Cumple | — |
| Contribución de todos los integrantes | `shortlog -sne`: `Julio Cesar Emiliani` (20), `super-gremlin` (15), `Ian Novoa` (12), `JuanB`/`JuanBustamante` (10+4, misma cuenta), `Daniel Manjarres Herrera` (7), `DaniGamer0907` (1). | No verificado | Seis grupos de identidades para cuatro integrantes; no se atribuyen cuentas por parecido de nombre y hace falta confirmación docente. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `0f3da0f3` (`origin/master`), la misma del estado calificado.
- No hay commits posteriores al cierre en `origin/master`.
- El proyecto despliega cuatro piezas (sitio estático, API Docker, MySQL gestionado y Auth0) con IaC, health, logs JSON, métricas ligadas a ESC-01/ESC-03, secretos fuera del código, arc42 §7/§2 y ADR de plataforma. El punto débil sigue siendo el CI: el run del estado calificado está en rojo, y el propio repositorio reconoce que no pudo confirmar la ejecución del scanner en los runs públicos.

## Recuento y nota sugerida

**9 de 10 criterios graduables Cumple.**

**Propuesta provisional al docente — `nota = 1 + 4 × (9/10) = 4.6`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- Las dos filas de despliegue (URL y health) quedan pendientes de calificar por la entrega de la URL en Moodle.
- Reparar el workflow `CI` en `master`: el run del estado calificado falla (incluido el Quality Gate de SonarCloud).
- No editar ADR ya aceptados: registrar el cambio como ADR nuevo y marcar el anterior como reemplazado.
- Cerrar el contraste de contribución por integrante con la confirmación docente (cuentas `super-gremlin` y `DaniGamer0907`).

## Hallazgos para la planilla

- El estado S8 cambió respecto a la punta de S7 (`1ea4aba`): aparecen despliegue real, IaC, observabilidad, secretos, costo, restricción de tarjeta y cinco ADR de plataforma.
- La fila de pipeline en verde sigue en No cumple: el CI del estado calificado está en rojo.
- La puntuación de la ficha sube de 3/12 (preliminar) a 9/10 graduables; la contribución de todos los integrantes sigue sin verificar.
