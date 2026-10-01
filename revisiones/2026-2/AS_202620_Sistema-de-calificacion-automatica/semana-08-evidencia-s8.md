# Semana 8 · Despliegue reproducible, CI y observabilidad · Calificación automática

> Revisión definitiva: hash `1f8f76dc169da96e4f668ff6894e7d51ce5be252`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `1f8f76d` en `origin/master` (2026-09-27T19:55:57-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |
| Revisión preliminar sustituida | `2269ca5` (2026-09-20T21:48:00-05:00) |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | README §«Entorno desplegado (S8)» declara `https://quantia-utb.onrender.com` y la comprobación «2026-09-27, 18:59 (−05:00) … sitio `http=200 tiempo=0,37 s`»; `docs/arc42/arc42-template-ES.md` §7 también nombra la URL. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El README fija la URL pública y la hora de comprobación (hash `1f8f76d`). |
| Health check consultable | `backend/api/main.py:75` (`@app.get("/health")`, sonda de vida) y `:85` (`@app.head("/health")`); README y §7 declaran `https://quantia-utb-api.onrender.com/health` → `200 {"status":"ok"}`. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. La ruta `/health` está versionada y probada (`backend/tests/test_arranque.py:12`). |
| Infraestructura como código versionada en el repositorio | `render.yaml` (Blueprint de Render), `docker-compose.yml`, `backend/Dockerfile`, `frontend/Dockerfile` y `.github/workflows/ci.yml` en el estado calificado. | Cumple | Describe el entorno desplegado (API, worker, Key Value, sitio) y el local (5 servicios); no es una lista de pasos manuales. |
| El entorno se puede recrear siguiendo el README | README §«Cómo se arranca» (`docker compose up`, requisitos y `.env.example`) y §«Cómo se despliega» (Blueprint de Render paso a paso, incluido el monitor de UptimeRobot). | Cumple | Un solo comando para local y procedimiento reproducible desde `render.yaml` para el despliegue. |
| Pipeline en verde sobre la rama principal | Run del hash revisado: `36364030158` (`CI`, `master`, 2026-09-28T00:55:59Z) con conclusión **success**: https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/36364030158 | Cumple | El único workflow que corre sobre `master` (`ci.yml`) termina en verde para `1f8f76d`. |
| Logs estructurados | `backend/infraestructura/registro.py`: `FormateadorJSON` y `logging.config.dictConfig` emiten una línea JSON por evento; ejemplo real en README (`{"momento": …, "evento": "lote_confirmado", "duracion_confirmacion_ms": 14.1}`). | Cumple | Configuración versionada y muestra con campos con nombre. |
| Métrica consultable asociada a un escenario de calidad | `backend/herramientas/medir_ec07.py` mide EC-07; `backend/api/main.py:145,152` emiten `lote_confirmado` con `duracion_confirmacion_ms`; `docs/evidencia/medicion-ec07.md` liga la métrica a EC-07 (≤10 s, 0 % de pérdida). | Cumple | Métrica nombrada, consultable y atada a un escenario con umbral. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example` declara variables sin credenciales reales; `render.yaml` inyecta `REDIS_URL` con `fromService`; el barrido §9, `git log -S'BEGIN PRIVATE KEY'` y `-S'AKIA'` no encuentran coincidencias; sin `.env` versionado. | Cumple | Configuración por entorno/plataforma; ningún secreto en el repositorio. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/despliegue/costo-mensual.md`: cuatro números del escenario (operaciones, tamaño, salida, horas), resultado US$0/mes y tabla de puntos de ruptura (750 h deinstancia, 6 600 visitas, 500 min de build). | Cumple | Supuestos del proyecto, no del catálogo; punto de ruptura explícito por recurso. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42-template-ES.md` §7.1: tabla de las seis piezas (sitio, API, base de datos, ficheros, cola, pipeline) con dónde se ejecuta y su ADR; diagrama Mermaid del despliegue. | Cumple | Una caja por pieza con ubicación de ejecución. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/arc42-template-ES.md` §2.2 `RNF-16`: «Costo mensual de US$0 y ninguna cuenta con tarjeta vinculada», con la restricción de capa gratuita sin tarjeta. | Cumple | Límite de costo y condición de tarjeta recogidos juntos como restricción. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0009` (API en Render Free + monitor), `0010` (sitio estático), `0011` (cola en Key Value) y `0012` (disco efímero), cada uno con alternativas descartadas y capa gratuita citada. | Cumple | Cuatro ADR de plataforma, uno por pieza decidida, con alternativa y verificación de la capa gratuita. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clonado sin autenticación desde `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica.git`. | Cumple | Organización `ISCOUTB`, nombre de la convención, visible sin credenciales. |
| Estructura mínima presente | `README.md`, `docs/arc42/arc42-template-ES.md`, `docs/adr/`, `docs/c4/doc-c4.md`, `docs/aspectos.md` y `docs/ia.md` presentes en `1f8f76d`. | Cumple | Las seis rutas del contrato están versionadas. |
| Estado calificado identificable | `origin/master`, `1f8f76d`, 2026-09-27T19:55:57-05:00, anterior al cierre; sin commits posteriores. | Cumple | Rama principal única; el hash elegible coincide con la punta. |
| Nombres de ADR según la convención | `docs/adr/0001` a `0012`, todos `NNNN-kebab-case.md`, sin archivos ajenos. | Cumple | El filtro del §4 no devuelve entradas. |
| ADR aceptados no reescritos | `ADR-0007` («Estado: aceptado», fecha 2026-09-13) se modifica después de aceptarse en `1c8bcfb` (2026-09-26, «actualizar en el 0007 dónde está la propiedad de datos»), sin ADR de reemplazo declarado. | No cumple | La edición posterior solo actualiza enlaces de documentación y no cambia la decisión; por la regla literal del §4 («un ADR aceptado no se edita»), se registra como reescritura con hash `1c8bcfb` y fecha 2026-09-26. `0001` sí está marcado como reemplazado por `0002` (declarado). |
| `docs/ia.md` al día para la semana | `docs/ia.md` crece dentro del periodo (`57e5235` 2026-09-26, `543d48f` 2026-09-27) y documenta lo aceptado y lo rechazado con motivo técnico. | Cumple | El registro incluye explícitamente decisiones descartadas y sus razones. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | El run del hash revisado (`36364030158`) está en verde, pero `.github/workflows/ci.yml` no invoca el scanner y no existe `sonar-project.properties`; solo hay un enlace a SonarCloud en el README. | No cumple | Faltan dos de las tres evidencias del §8 (configuración del análisis y línea del workflow que invoca el scanner). El equipo lo reconoce en `correcciones.md` y `docs/ia.md`: el análisis corre desde la interfaz de SonarCloud, no desde el pipeline. |
| Sin credenciales en el repositorio ni en el historial | `git grep` §9, `git log -S'BEGIN PRIVATE KEY'` y `-S'AKIA'` sin coincidencias; sin `.env` versionado. | Cumple | El repositorio no expone credenciales. |
| Contribución de todos los integrantes | `shortlog -sne 1f8f76d`: `scp1109` (83), `josueacademico17-source` (37), `SusanaRosales` (24), `Mariadelmar-restrepo` (17); cuatro cuentas para los cuatro integrantes declarados. | Cumple | Las cuatro identidades corresponden a los cuatro integrantes del equipo (`EQUIPOS.md`); el README lista cada cuenta junto a su nombre. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Se mira el repositorio entero en la punta actual de `origin/master`, no solo el estado del cierre.

- **Punta actual**: `1f8f76d` (2026-09-27T19:55:57-05:00, «docs(readme): nombrar la URL de la API en los pasos de despliegue»).
- **Commits posteriores al cierre**: ninguno.
- **Veredicto**: entrega S8 completa en la ficha; persiste la no conformidad transversal de SonarCloud.

La punta actual coincide con el estado calificado. El repositorio contiene IaC para local y nube (`docker-compose.yml`, `render.yaml`, dos `Dockerfile`), URL pública y health check declarados con hora, logs JSON, la métrica de EC-07, la estimación de costo con puntos de ruptura, arc42 §2 y §7 al día y cuatro ADR de plataforma. Queda abierto el análisis estático (no invocado por el pipeline) y una edición posterior de `ADR-0007` sin reemplazo declarado.

## Recuento y nota sugerida

**10 de 10 criterios graduables.**

**Propuesta provisional al docente — `nota = 1 + 4 × (10/10) = 5.0`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

No se aplica la fórmula sobre las 12 filas: las dos primeras («URL del sistema accesible desde fuera de la red de la universidad» y «Health check consultable») quedan diferidas por decisión docente.

## No verificado / pendientes

- Deferidas por decisión docente (no se abrieron ni probaron URLs): «URL del sistema accesible desde fuera de la red de la universidad» y «Health check consultable»; ambas dependen de la URL que se entrega por Moodle.
- SonarCloud no es auditable desde el pipeline (no invocado, sin archivo de configuración); es una no conformidad transversal, no una fila de la ficha.
- `ADR-0007` editado después de aceptarse sin reemplazo declarado (no conformidad transversal).

## Hallazgos para la planilla

- El informe preliminar evaluó `2269ca5`; el estado definitivo es `1f8f76d`, sin commits posteriores al cierre.
- IaC completa: `render.yaml`, `docker-compose.yml` y dos `Dockerfile`.
- Pipeline verde para el hash calificado (run `36364030158`), pero sin SonarCloud invocado por el workflow.
- URL pública y health check declarados con hora de comprobación; quedan pendientes de calificar por decisión docente.
- Estimación de costo con supuestos y puntos de ruptura; arc42 §2 (RNF-16) y §7 con las seis piezas y su ubicación.
- Cuatro ADR de plataforma (0009–0012) con alternativas descartadas y capa gratuita.
- `ADR-0007` editado el 2026-09-26 (`1c8bcfb`) sin reemplazo declarado; la edición solo cambia enlaces.
- Sin credenciales en HEAD ni en el historial; cuatro cuentas contribuyen en el historial.
