# Evidencia S8 · Verifacts

> Pasada temprana actualizada el 2026-09-24. Los resultados son preliminares y pueden cambiar hasta el cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `ef48c08` en `origin/master` (2026-09-23T21:28:43-05:00) |
| Cierre previsto | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `docs/despliegue.md:1-6,32` declara las URL de API y web y registra `http=404 tiempo=0.93s` para la raíz de la API. | No verificado | El documento no deja hora para esa solicitud y esta auditoría no realizó una conexión externa al servicio; hace falta una comprobación fechada por el evaluador. |
| Health check consultable | `docs/despliegue.md:9,33` declara `GET /health` y registra `health=200`. | No verificado | La ruta y el resultado están documentados, pero falta la hora y la comprobación externa del evaluador. |
| Infraestructura como código versionada en el repositorio | `render.yaml:1-25` define `verifacts-api` y `verifacts-web`; también existen `Dockerfile` y `.dockerignore`. | Cumple | Render se configura mediante un Blueprint versionado, no mediante pasos manuales. |
| El entorno se puede recrear siguiendo el README | `README.md:404-423` documenta construcción y arranque con `docker build -t verifacts . && docker run -p 8000:8000 verifacts`. | Cumple | Reproduce el backend con el mismo Dockerfile usado por el despliegue. |
| Pipeline en verde sobre la rama principal | Para `ef48c08`, el workflow `Tests` concluyó `success`: https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/35947529324. El workflow `SonarCloud` también concluyó `success`: https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/35947529243. | Cumple | Ambos runs corresponden exactamente al estado revisado en `master`. |
| Logs estructurados | `app/observability.py:19-30` implementa `JsonFormatter`; `docs/despliegue.md:34` aporta una línea JSON con timestamp, nivel, request_id, ruta, estado y duración. | Cumple | Hay configuración y ejemplo citable. |
| Métrica consultable asociada a un escenario de calidad | `app/observability.py:94-124,136-140` expone el histograma `verifacts_http_request_duration_seconds` en `GET /metrics`; `docs/escenarios-de-calidad.md:49-54` lo vincula con Q-01. | Cumple | La medición formal de P95 sigue pendiente, pero la métrica exigida está implementada y trazada al escenario. |
| Secretos fuera del código y tomados del entorno o del almacén | Existen `.env.example` y `frontend/.env.example`, no hay `.env` versionado, y `.github/workflows/sonarcloud.yml:24` obtiene `SONAR_TOKEN` desde GitHub Secrets. | Cumple | `docs/despliegue.md:18-24` documenta las variables del proveedor. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/costos.md:14-27` supone decenas de peticiones diarias, desglosa las dos piezas y calcula USD 0/mes hasta 100 GB; `:33-35` identifica la persistencia como ruptura hacia el plan Starter. | Cumple | El precio exacto del plan pago queda sujeto a la tarifa vigente, pero el punto de ruptura está identificado. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07-despliegue.md:13-34` muestra cajas separadas para web, API y SQLite dentro de Render; `:56-78` documenta las piezas del CI. | Cumple | La vista ya coincide con `render.yaml`. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02-restricciones.md:91-104` exige costo cero y ausencia de tarjeta, y explica las consecuencias del plan gratuito. | Cumple | La restricción quedó incorporada de forma explícita. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0004-plataforma-despliegue.md:25-83` decide Render para las dos piezas, compara Terraform y AWS Lambda y documenta consecuencias de la capa gratuita. | Cumple | Es una decisión única de plataforma aplicada mediante el mismo Blueprint. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | El clon sin autenticación de `ISCOUTB/AS_202620_Verifacts` respondió correctamente. | Cumple | El hallazgo histórico de repositorio no visible ya no describe el estado actual. |
| Estructura mínima presente | En `ef48c08` existen README, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | El glosario está numerado como sección 12. |
| Estado calificado identificable | `origin/master`, `ef48c08e6fed3a1fb4c761a707617af046c08a61`, 2026-09-23T21:28:43-05:00. | Cumple | Estado preliminar elegible. |
| Nombres de ADR según la convención | Cuatro ADR con nombres `NNNN-titulo-en-kebab-case.md`. | Cumple | — |
| ADR aceptados no reescritos | El ADR 0001 registra varias modificaciones posteriores a su creación. | No cumple | Los enlaces de implementación agregados no sustituyen un ADR de reemplazo cuando cambia una decisión aceptada. |
| `docs/ia.md` al día para la semana | `docs/ia.md:22` registra el incremento del 22–23 de septiembre, incluida una alternativa descartada y su motivo. | Cumple | — |
| Tabla de aspectos completa y navegable | `docs/aspectos.md` conserva A-04 con verificación manual y reconoce una segunda verificación pendiente para A-02. | No cumple | La tabla mejoró sus enlaces, pero mantiene evidencia incompleta. |
| Pipeline, SonarCloud y Quality Gate públicos | Los dos workflows del hash están en verde y `docs/despliegue.md:37` publica el análisis, pero el propio documento declara el Quality Gate general en rojo. | No cumple | Un workflow exitoso no convierte un Quality Gate rojo en cumplimiento. |
| Sin credenciales en el repositorio ni en el historial | No hay `.env` versionado; los secretos del workflow se toman de GitHub Secrets. | Cumple | Barrido sin coincidencias materiales. |
| Contribución de todos los integrantes | El historial muestra dos identidades consolidadas y el equipo declarado tiene tres integrantes. | No cumple | No se atribuyen cuentas a personas por parecido de nombre. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `ef48c08e6fed3a1fb4c761a707617af046c08a61` (2026-09-23T21:28:43-05:00).
- Desde el informe del miércoles entraron cinco commits elegibles: incorporaron restricciones de costo, ADR de plataforma, vista de despliegue, comando Docker, registro de IA y evidencia de SonarCloud.
- El pipeline del hash actual está verde y la evidencia estática ya cubre observabilidad, costos y decisiones de plataforma.
- Siguen sin cierre verificable la URL y el health por falta de comprobación externa con hora; además, el Quality Gate publicado está rojo y falta confirmar la contribución del tercer integrante.

## Recuento y nota sugerida

**10 de 12 criterios Cumple.**

**Nota sugerida preliminar (propuesta al docente): 4.3 = 1 + 4 × (10/12).** La nota final la fija el profesor en Moodle.

## No conformidades y pendientes

- Registrar una comprobación externa de la URL y de `/health` con hora, código y tiempo.
- Corregir el Quality Gate general de SonarCloud, actualmente documentado en rojo.
- Completar la evidencia automatizada pendiente en la tabla de aspectos.
- Confirmar la contribución del tercer integrante sin inferir identidades.
- Ejecutar la medición formal del P95 de Q-01 cuando exista volumen suficiente.

## Hallazgos para la planilla

- Cinco commits posteriores al informe temprano elevan S8 de 5/12 a 10/12.
- Se verificaron runs exitosos de Tests y SonarCloud para el hash actual.
- arc42 §2 y §7, el ADR de plataforma, el comando Docker y el vínculo métrica–Q-01 ya están presentes.
- La URL y el health permanecen No verificado por falta de comprobación externa fechada.
