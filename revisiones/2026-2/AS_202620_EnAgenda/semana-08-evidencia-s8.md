# Semana 8 · Despliegue reproducible, CI y observabilidad · EnAgenda

> Revisión definitiva: hash 2c7d77a, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `2c7d77a` en `origin/master` (2026-09-27T23:42:39-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

El repositorio remoto declara `master` como rama principal (HEAD simbólico de `origin`); existe
además una rama `main` que es ancestro de `master`. El estado cambió respecto de la pasada
temprana: pasó de `6db7cd9` (2026-09-21) a `2c7d77a` (2026-09-27), que incorpora `render.yaml`,
`Dockerfile`, `docker-compose.yml`, observabilidad (`/health`, `/metrics`), `docs/adr/0003` y
`docs/despliegue/`. No hay commits posteriores al cierre.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | El repositorio no declara una URL pública concreta: `README.md` solo publica `http://127.0.0.1:5000`; `docs/arc42/07-vista-de-despliegue.md:9,30` nombra «Render Free Web Service» sin URL; `docs/despliegue/medicion-render.md` usa el marcador `https://[URL-REAL].onrender.com/health`. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. No se abrió ni se consultó ninguna URL. |
| Health check consultable | La ruta existe: `app/web.py:40` `@app.get("/health")` y `:42` responde `{"status": "ok"}, 200`; `docs/arc42/07-vista-de-despliegue.md:16` la declara y `render.yaml` la usa como `healthCheckPath: /health`. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. No se consultó ninguna URL. |
| Infraestructura como código versionada en el repositorio | `Dockerfile`, `docker-compose.yml`, `render.yaml` y `.dockerignore` están versionados, pero contienen marcadores de conflicto de merge sin resolver: `Dockerfile:11,17,21`, `docker-compose.yml:5,10,16`, `render.yaml:3,9,17`, `.dockerignore:3,11,23`. | No cumple | Los archivos existen pero son inválidos; el `docker build` del workflow falla (run 36378874812). No describen un entorno recreable. |
| El entorno se puede recrear siguiendo el README | `README.md` «Instalación» (`pip install -r requerimiento.txt`), «Ejecutar las pruebas» (`pytest -q`) y «Ejecutar la aplicación» (`python app\web.py`). | Cumple | Procedimiento local reproducible; no documenta el entorno en contenedor/despliegue y el árbol de estructura quedó desactualizado. |
| Pipeline en verde sobre la rama principal | Run `CI` de `2c7d77a`, conclusión `failure`: https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/36378874812 (2026-09-28T04:42:56Z). | No cumple | El último run de CI sobre `master` en el hash revisado está en rojo; el commit anterior `387b4b3` sí estaba en verde. |
| Logs estructurados | No hay configuración de registro: el barrido de `structlog|winston|pino|logback|serilog|logging.config|json formatter|import logging|basicConfig|dictConfig` no devuelve coincidencias y `app/web.py` usa la salida por defecto de Flask. | No cumple | `docs/arc42/07-vista-de-despliegue.md:33` y ADR-0003 afirman logs JSON, pero no hay archivo de configuración ni línea de ejemplo. |
| Métrica consultable asociada a un escenario de calidad | `app/web.py:47-55` expone `/metrics` con `enagenda_invitaciones_consultadas_total`; ADR-0003:6 la liga a «EC-03 — Observabilidad de solicitudes». | No cumple | El escenario citado no existe: `docs/arc42/10-requisitos-de-calidad.md` define EC-03 como «Actualización de respuesta de asistencia», y no hay escenario de observabilidad. Métrica sin escenario real. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example` versionado con `SECRET_KEY` y `LOG_LEVEL` (con marcadores de conflicto); sin `.env` versionado; sin credenciales reales en el barrido. | Cumple | El `.env.example` arrastra marcadores de conflicto y no hay referencias `secrets.X` en el workflow (usa un valor efímero en línea); no se hallaron credenciales reales. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/despliegue/costos.md:9-11,24` dejan «[COMPLETAR]» las solicitudes mensuales, el tamaño de respuesta y el tráfico de salida; `:29-36` sí calculan el punto de ruptura (750 h compartidas frente a ~744 h de un mes continuo). | No cumple | Faltan los supuestos de volumen; una preferencia de costo $0 no sustituye la estimación pedida. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07-vista-de-despliegue.md:26-37` «Piezas y ubicación» con API web en Render Free, módulo de invitaciones dentro del contenedor, persistencia en memoria, CI, logs, métricas y secretos. | Cumple | Una caja por pieza y dónde se ejecuta; la base de datos queda marcada como deuda técnica. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02- restricciones.md:43` R-05: herramientas gratuitas o de capa gratuita «sin exigir cuentas personales de pago». | Cumple | La restricción fija costo cero y evita depender de una cuenta de pago. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0003-desplegar-api-flask-en-render.md`: alternativas A (Render Free) y B (servidor del laboratorio) con la B descartada; `:56` decide Render y `:27` verifica costo $0 en la capa gratuita. | Cumple | El campo «Decide» quedó como `[COMPLETAR CON INTEGRANTES]`, pero la decisión y la alternativa descartada están completas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_EnAgenda`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre `AS_202620_EnAgenda` conforme y visibilidad pública. |
| Estructura mínima presente | En `2c7d77a`: `docs/arc42/`, `docs/adr/` (0001-0003), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2; varios nombres de `arc42` conservan un espacio antes de la extensión (desviación anotada desde S1). |
| Estado calificado identificable | `2c7d77a421ab95b89dd68d696d49277e9f36a45c` en `origin/master`, último commit ≤ cierre: `2026-09-27T23:42:39-05:00 algo`. | Cumple | `master` es la rama principal declarada por el remoto; `main` es ancestro y no se mezcla. Sin commits posteriores al cierre. |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md`, `0002-estrategia-integracion-api.md` y `0003-desplegar-api-flask-en-render.md`. | Cumple | Los tres cumplen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | ADR-0001 nace como propuesta (`e1219bf`, 2026-08-08) y se reemplaza por la decisión de monolito modular en `c38adfb` (2026-08-23), antes de declararse aceptado; ADR-0002 tiene un único commit y ADR-0003 se completa en `f7bc011` (2026-09-27). | Cumple | No se observa una reescritura posterior a la aceptación sin reemplazo declarado. |
| `docs/ia.md` al día para la semana | `docs/ia.md` con entrada del 27-Sep-2026 (`actualizacion`, `f7bc011`, 2026-09-27T23:33:56-05:00), que registra el uso para el despliegue y lo que se rechazó. | Cumple | El registro se actualiza durante la semana y conserva lo rechazado con su motivo. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `.github/workflows/ci.yml` corre CI sobre `master`, pero el run del hash revisado está en rojo (run 36378874812) y no existe configuración ni URL pública de SonarCloud. | No cumple | CI en rojo y SonarCloud ausente; faltan todas las evidencias del contrato §8. |
| Sin credenciales en el repositorio ni en el historial | Barrido con coincidencias solo en tokens de dominio, datos de prueba y `secrets.token_urlsafe`; sin `.env` versionado. | Cumple | Sin credenciales reales; `.env.example` presenta marcadores de conflicto. |
| Contribución de todos los integrantes | `git shortlog -sne 2c7d77a`: `Jein-12` 70, `Daoisttl0FB3` 69 y `GabrielaMorales Cancino` 5 (mismo correo que `Daoisttl0FB3`, se consolidan), `eliabarnedocondef10-gif` 18. | Cumple | Tres personas para tres integrantes declarados; todas con commits. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `2c7d77a421ab95b89dd68d696d49277e9f36a45c 2026-09-27T23:42:39-05:00 algo`
- **Veredicto**: con no conformidades graves
- Resumen: la punta actual coincide con el estado calificado (no hay commits posteriores al cierre). La semana sumó un ADR de plataforma, `render.yaml`, `Dockerfile`, `docker-compose.yml`, `/health`, `/metrics`, la vista de despliegue §7, la restricción R-05 y la documentación de despliegue. Sin embargo, el commit revisado es un merge con conflictos sin resolver en seis archivos (`Dockerfile`, `docker-compose.yml`, `render.yaml`, `.dockerignore`, `.env.example` y `docs/evidencia.md`), lo que deja la infraestructura como código inválida y el pipeline en rojo; además no hay logs estructurados, la métrica no se ata a un escenario real y la estimación de costo tiene los volúmenes en «[COMPLETAR]».

Pendientes que siguen abiertos:
- URL del despliegue y su comprobación (fila diferida por decisión docente).
- Health check consultable con código de respuesta (fila diferida por decisión docente).
- Conflictos de merge sin resolver en `Dockerfile`, `docker-compose.yml`, `render.yaml`, `.dockerignore`, `.env.example` y `docs/evidencia.md`.
- Pipeline en rojo en el hash revisado.
- Logs estructurados ausentes pese a lo que afirman §7 y ADR-0003.
- Métrica sin escenario de calidad real (ADR-0003 cita un EC-03 inexistente).
- Estimación de costo con supuestos de volumen en «[COMPLETAR]».
- SonarCloud sin configuración, run ni Quality Gate públicos (pendiente desde S5/S6).

## Recuento y nota sugerida

5 de 10 criterios graduables Cumple.

**Propuesta provisional al docente: 3.0 = 1 + 4 × (5/10).** Quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL del sistema accesible desde fuera de la red universitaria: fila diferida; no se abrió ninguna URL. El repositorio no declara una URL pública concreta.
- Health check consultable: fila diferida; la ruta `/health` existe en `app/web.py:40`, pero no se consultó por estar diferida la URL.
- Infraestructura como código inválida por marcadores de conflicto sin resolver.
- Pipeline en rojo y Sin SonarCloud: fila transversal en No cumple.
- Logs estructurados: sin configuración ni línea de ejemplo.
- Métrica: `enagenda_invitaciones_consultadas_total` sin escenario de calidad real.
- Costo: supuestos de volumen pendientes de completar.

## Hallazgos para la planilla

- El commit calificado `2c7d77a` es un merge con marcadores de conflicto sin resolver en `Dockerfile`, `docker-compose.yml`, `render.yaml`, `.dockerignore`, `.env.example` y `docs/evidencia.md`.
- CI del hash revisado en rojo: run 36378874812; el commit anterior `387b4b3` estaba en verde.
- ADR-0003 decide plataforma con alternativa descartada y capa gratuita verificada, pero cita «EC-03 — Observabilidad de solicitudes», un escenario que no existe en arc42 §10 (allí EC-03 es actualización de respuesta).
- Sin logs estructurados pese a que §7 y ADR-0003 los declaran implementados.
- `docs/despliegue/costos.md` deja en «[COMPLETAR]» los volúmenes supuestos; solo calcula el punto de ruptura de las 750 h.
- `docs/arc42/07-vista-de-despliegue.md` y R-05 están completos; la contribución de los tres integrantes queda identificada.
- El commit calificado `2c7d77a` es anterior al cierre y no hay commits posteriores.
