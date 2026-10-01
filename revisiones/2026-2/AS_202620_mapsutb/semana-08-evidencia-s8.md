# Evidencia S8 · mapsutb

> Revisión definitiva: hash `8cfe458141159c9663f543d7cf31faf240432214`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `8cfe4581` en `origin/master` (2026-09-27T16:35:57-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Comprobación | 2026-10-01 (auditoría local sobre clon público efímero) |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `README.md:106` declara `https://mapsutb.web.app/`; no se abrió. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. |
| Health check consultable | `.github/workflows/deploy.yml:54-58` genera `health.json` con el commit desplegado y `:73` verifica que responde 200; `README.md:108`. No se consultó. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El health es estático (`status`, `commit`, `desplegado`). |
| Infraestructura como código versionada en el repositorio | `.github/workflows/deploy.yml`, `firebase.json`, `.firebaserc`, `infra/Dockerfile`, `infra/docker-compose.yml`, `infra/nginx.conf`. | Cumple | El entorno público (Firebase Hosting, plan Spark) y el alternativo (nginx) están descritos como código. |
| El entorno se puede recrear siguiendo el README | `README.md` "Recrear el entorno público desde cero" (proyecto Firebase, cuenta de servicio, secrets, `Run workflow`, comprobación) y "Recrear el entorno en el servidor del laboratorio (Docker)". | Cumple | Distingue arranque local de despliegue público y da el procedimiento completo. |
| Pipeline en verde sobre la rama principal | URL del último run y su conclusión | Cumple | Consulta sin autenticar a `actions/runs?head_sha=8cfe458141159c9663f543d7cf31faf240432214`: 104 runs del hash, todos `success`. Disparados por `push`: `CI` #31 (`2026-09-27T21:36:01Z`) https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/36352317301 y `Despliegue web (Firebase Hosting)` #6 https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/36352317306. Los crons `Sonda de disponibilidad (métrica Escenario 6)` (87 ejecuciones) y `Sincronizar hallazgos de Sonar a GitHub Issues` (15) también concluyeron `success`. Ningún run del commit en `failure`/`cancelled`. | Solo workflows disparados por `push`/`schedule` sobre `master`; los de reversión son manuales. |
| Logs estructurados | `lib/core/log.dart`: una línea JSON por evento (`ts`, `nivel`, `evento` + campos); en Docker, nginx escribe una línea JSON por petición (`docs/arc42/07_deployment_view.adoc:99`). | Cumple | Configuración propia de logging, con campos y ejemplo documentado. |
| Métrica consultable asociada a un escenario de calidad | `docs/adr/0008-metrica-disponibilidad-sonda-actions.md` y `README.md:162`: `disponibilidad_pct` y `latencia_p95_ms` ligados al **Escenario 6** (≥ 99 % y p95 < 1 s/7 días), publicados en `resumen.json`. | Cumple | La sonda horaria mide la URL y el health, y agrega la métrica del escenario. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example`; `.github/workflows/deploy.yml:42-44` usa `${{ secrets.GOOGLE_MAPS_API_KEY }}`, `GA_MEASUREMENT_ID`, `GA_API_SECRET` y `:64` `FIREBASE_SERVICE_ACCOUNT`; sin `.env` versionado. | Cumple | La key de Google se restringe por referrer/paquete y no viaja en el despliegue público sin tarjeta. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/costos.md`: supuestos de volumen (2 000 visitantes, 6 000 visitas/mes), costo por pieza, total USD 0 y puntos de ruptura (≈120 visitas nuevas/día en Hosting, 3 333 visitas/mes en Static Maps). | Cumple | Parte del volumen del escenario y marca el primer quiebre de cada capa gratuita. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07_deployment_view.adoc`: diagrama de infraestructura y tabla "Una caja por pieza y dónde se ejecuta" (Firebase Hosting, health, app en el cliente, CI, SonarCloud, sonda, métrica, secretos, APIs externas, nginx). | Cumple | — |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02_architecture_constraints.adoc`: "Límite de costo: USD 0 al mes" y "Sin tarjeta: ninguna pieza puede exigir una cuenta personal con tarjeta". | Cumple | Restricciones organizacionales con su motivo y consecuencia. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0007-hosting-web-firebase-hosting.md` (Firebase vs. GitHub Pages vs. laboratorio), `0008-metrica-...`, `0009-secretos-...`, `0010-reversion-sitio-web.md`. | Cumple | Cada decisión de plataforma tiene su ADR con alternativa y capa gratuita verificada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon público sin autenticación de `ISCOUTB/AS_202620_mapsutb`. | Cumple | — |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` en `8cfe4581`. | Cumple | arc42 en `.adoc` y algunos `.md`; el artefacto existe donde está. |
| Estado calificado identificable | `origin/master`, `8cfe4581`, 2026-09-27T16:35:57-05:00. | Cumple | Hay commits posteriores al cierre (ver overall). |
| Nombres de ADR según la convención | Diez ADR `NNNN-titulo-en-kebab-case.md` (0001–0010). | Cumple | — |
| ADR aceptados no reescritos | El ADR 0001 se editó varias veces después de aceptarse (28–31/08/2026, commits `1e370a0`–`3e8335c`) y lo admite en una nota de trazabilidad; el ADR 0005 se editó el 2026-09-25 (`3343425`), después de su aceptación. | No cumple | La nota reconoce que los cambios de alcance se hicieron editando el ADR en vez de crear uno nuevo. |
| `docs/ia.md` al día para la semana | Cambios del 2026-09-25, 26 y 27, con entradas de S8 y la columna de rechazados y su motivo. | Cumple | El archivo crece dentro del periodo revisado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `sonar-project.properties`; `.github/workflows/ci.yml` invoca el scanner y la acción de Quality Gate (falla el pipeline si el gate falla); el run #31 del hash revisado concluye `success`; `README.md:110` publica el panel de SonarCloud. | Cumple | El Quality Gate verde queda ligado al run de CI del estado calificado. |
| Sin credenciales en el repositorio ni en el historial | Barridos de claves y tokens sin coincidencias; sin `.env` versionado. | Cumple | — |
| Contribución de todos los integrantes | `shortlog -sne` consolidado por correo: `CarlosManrique-1397` (53), `i-matallana` (41+2, dos correos), `charly`/`charlygz21` (26+25+22+2, mismo correo) y `nerlis-otero` (22). | Cumple | Cuatro personas = cuatro integrantes declarados. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `f1b3fe4` (`origin/master`).
- **Commits posteriores al cierre (no cambian la matriz):**
  - `f1b3fe4` · 2026-10-01T09:11:56-05:00 · `feat(herramientas): registro de coordenadas en campo para el grafo peatonal`.
- Entre el cierre y la punta, el equipo siguió mejorando el despliegue (CI y despliegue en verde para la punta) y subió la primera versión de coordenadas para el grafo peatonal.
- El sistema está desplegado como sitio estático en Firebase Hosting con health, logs JSON, métrica de disponibilidad, secretos fuera del código, arc42 §7/§2, ADR de plataforma y cálculo de costo. La deuda del taller (ruteo y tour) sigue declarada como pendiente.

## Recuento y nota sugerida

**10 de 10 criterios graduables Cumple.**

**Propuesta provisional al docente — `nota = 1 + 4 × (10/10) = 5.0`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- Las dos filas de despliegue (URL y health) quedan pendientes de calificar por la entrega de la URL en Moodle.
- Dejar de reescribir ADR aceptados: registrar los cambios como ADR nuevos y marcar el anterior como reemplazado (no conformidad transversal).
- El taller de despliegue (reversión) se evaluó aparte en la ficha del taller, no en esta matriz.

## Hallazgos para la planilla

- El estado S8 cambió respecto a la punta de S7 (`5e2fdd5`): aparecen despliegue público en Firebase Hosting, health, IaC, logs, métrica, secretos, costo y cuatro ADR nuevos.
- El CI del estado calificado pasa a verde; la puntuación de la ficha sube de 2/12 (preliminar) a 10/10 graduables. La fila de pipeline ahora cita el run `CI` #31 de `8cfe458` y el `Despliegue web` #6, en vez de una página de búsqueda.
- Se mantiene abierto el hallazgo de ADR aceptados reescritos, pese a la nota de trazabilidad del ADR 0001.
