# Semana 8 · Despliegue reproducible, CI y observabilidad · InvenTrack

> Revisión definitiva: hash `48aeecf94e590088b21e1c4c63dee8d2feb79f11`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `main`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `48aeecf` en `origin/main` (2026-09-27T23:48:02-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `README.md:27` declara `https://inventrack-api.onrender.com` como URL pública. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. |
| Health check consultable | `app/main.py:127` implementa `GET /health` (`{"status":"ok","service":"InvenTrack"}`); `README.md:28` declara `https://inventrack-api.onrender.com/health`. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. |
| Infraestructura como código versionada en el repositorio | `Dockerfile`, `render.yaml`, `infra/main.tf` (+ `variables.tf`, `outputs.tf`, `versions.tf`, `backend.tf`) y `.github/workflows/test.yml`. | Cumple | Terraform de `infra/` queda como prototipo histórico; `render.yaml` es la definición vigente. |
| El entorno se puede recrear siguiendo el README | README "Cómo ejecutar el esqueleto": Python 3.11, `pip install --require-hashes -r requirements.txt`, `uvicorn app.main:app`, `pytest`. | Cumple | Reproduce el backend local de extremo a extremo. |
| Pipeline en verde sobre la rama principal | Run `Run Tests` en `main` para `48aeecf9`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/36378966426. | Cumple | Ejecuta pytest con cobertura, scanner SonarCloud y la prueba contractual. |
| Logs estructurados | `app/main.py:35` define `JsonFormatter`; `app/main.py:82` emite el evento `http_request` con `method`, `path`, `status_code` y `duration_ms`. | Cumple | Una línea JSON por petición, sin credenciales ni cuerpos. |
| Métrica consultable asociada a un escenario de calidad | `app/main.py:137` expone `GET /metrics`; `app/main.py:143` publica `inventrack_http_p95_latency_seconds` "asociada al escenario ESC-04". | Cumple | Formato Prometheus, con contador y gauge p95 por método y ruta. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example` declara el entorno; `.github/workflows/test.yml:41` toma `SONAR_TOKEN` de `secrets.*`; no hay `.env` versionado. | Cumple | El `deploy.yml` de Azure (deshabilitado con `if: false`) referencia secretos, ninguno hardcodeado. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/despliegue-y-costos.md:62` estima 50.000 peticiones/mes y 0,10 GB, y `:78` fija el punto de ruptura (512 MB de RAM / ~2.000.000 de peticiones → plan Starter de 7 USD); reproducido en `docs/arc42/arc42-template-EN.md:491`. | Cumple | Supuestos, cálculo por pieza y punto de ruptura presentes. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42-template-EN.md:400` abre `# 7. Deployment View`, con 6 nodos (`:404`) y estimación financiera (`:491`). | Cumple | Diagrama Mermaid con cliente, CI, SonarCloud, Render, almacén en memoria y notificaciones. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/arc42-template-EN.md:135` (C5): sin presupuesto para servicios de pago, stack y hosting con capa gratuita. | Cumple | La restricción de "sin tarjeta" se detalla en `docs/adr/0005` y en `docs/despliegue-y-costos.md`. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0005-eleccion-plataforma-despliegue.md`: descarta Azure App Service por exigir tarjeta (`:11`–`:14`) y verifica la capa gratuita de Render (`:25`). | Cumple | Alternativa descartada y capa gratuita verificadas, con punto de ruptura propio. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | `ISCOUTB/AS_202620_InvenTrack`, clonado sin autenticación. |
| Estructura mínima presente | Cumple | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` presentes. |
| Estado calificado identificable | Cumple | `origin/main`, `48aeecf`, 2026-09-27T23:48:02-05:00. |
| Nombres de ADR según la convención | Cumple | `docs/adr/0001`…`0005` siguen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | No cumple | ADR-0002, aceptado en `80c7d0a`, fue editado en `7aae9a8`, `66116c6`, `7b0aad5` (2026-09-06) y `af24edb` (2026-09-19) sin reemplazo declarado; ADR-0004 (aceptado en `81ebeab`) acumula ediciones posteriores y ADR-0005 fue editado en `c692d9e` (2026-09-27). |
| `docs/ia.md` al día para la semana | Cumple | Entrada S8 del 2026-09-27 (`04f5e33`), con lo aceptado y lo rechazado y su motivo. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Cumple | `sonar-project.properties` + scanner en `test.yml:37`; run `36378966426` en verde; Quality Gate público `OK` (cobertura nueva 94,8 %). |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin `.env` versionado ni credenciales; las únicas coincidencias son referencias `${{ secrets.* }}`. |
| Contribución de todos los integrantes | Cumple | `shortlog -sne` consolida las cuatro personas declaradas; Jose Vargas y Felix Taborda concentran el mayor volumen y Javier Carta aporta menos commits. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `f12bba8` en `origin/main` (2026-09-30T00:41:30-05:00).
- **Commits posteriores al cierre:** `417cb69` (instrucciones de despliegue para `iscoutb.dev` con Compose/Dokploy), `f9851ba` (detalles de despliegue), `d1a6b6f` (documentación de despliegue con Dokploy), `f12bba8` (contexto técnico del arc42 y refinamiento de Render).
- **Veredicto:** con una no conformidad transversal. El estado calificado ya cubre las diez filas graduables de la ficha; tras el cierre el equipo explora una migración de plataforma (Dokploy/`iscoutb.dev`) que no forma parte del estado calificado y no altera la matriz.

## Recuento y nota sugerida

10 de 10 criterios graduables Cumple.

**propuesta provisional al docente — `nota = 1 + 4 × (10/10) = 5,0`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- URL del sistema accesible desde fuera de la red de la universidad.
- Health check consultable.

Ambas quedan pendientes de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio sí declara la URL pública (`README.md:27`–`:28`) y la ruta de salud (`app/main.py:127`), que se verificarán en la segunda pasada.

## Hallazgos para la planilla

- La entrega S8 cubre las diez filas graduables de la ficha (IaC, reproducibilidad, CI, logs estructurados, métrica con escenario, secretos, costo con punto de ruptura, arc42 §7, arc42 §2 y ADR de plataforma).
- Transversal pendiente: ADR-0002/0004/0005 editados después de su aceptación sin un ADR de reemplazo declarado; corregirlo no exige rehacer la decisión, solo dejar el registro histórico inmutable.
- La contribución sigue concentrada en dos integrantes; conviene repartir el trabajo de cara al cierre.
