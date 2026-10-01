# Semana 8 · Despliegue reproducible, CI y observabilidad · CampusMarket

> Revisión definitiva: hash `784d788`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `784d788` en `origin/master` (2026-09-27T23:50:19-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

El estado cambió respecto de la pasada preliminar: el commit calificado pasó de
`c53ee32` (2026-09-18) a `784d788` (2026-09-27), que incorpora el despliegue
público (GitHub Pages + Azure App Service + Azure MySQL), `infra/main.bicep`,
observabilidad, los ADR-0005 a ADR-0008, la evidencia S8 y el README de
operación. No hay commits posteriores al cierre.

## Matriz de la ficha

Las dos filas de despliegue quedan **diferidas** por decisión docente: la URL se
entrega por Moodle y no está disponible en esta pasada. No se abrió, consultó ni
sondeó ninguna URL.

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | código de respuesta y tiempo, con la hora de la comprobación | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio declara la URL pública del frontend en `README.md:124` (`https://nnigarp.github.io/AS_202620_PROYECTO_CAMPUSMARKET/`) y la del backend en `README.md:128` (`https://campusmarket-s8-api-nilver.azurewebsites.net`), replicadas en `docs/arc42/07-vista-despliegue.md:20-28` y `docs/arc42/02-restricciones.md` (R-08). No se abre ninguna URL en esta pasada. |
| Health check consultable | ruta y código de respuesta | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. Ruta de salud en el código: `backend/app/main.py:60` (`@app.get("/health")`) y `:65` (`health_check`), que consulta `database_is_available()` y devuelve `503` si MySQL no responde. Declarada en `README.md:132`. No se consulta en esta pasada. |
| Infraestructura como código versionada en el repositorio | rutas de los archivos de infraestructura | Cumple | `infra/main.bicep:1` declara App Service Plan, Web App, MySQL Flexible Server, la base `campusmarket`, configuración y reglas de acceso; `.github/workflows/backend-tests.yml:1` es el pipeline versionado. Describe el entorno desplegado, no pasos manuales. |
| El entorno se puede recrear siguiendo el README | sección del README con el procedimiento | Cumple | `README.md:407-503` documenta la reproducción local (requisitos, variables MySQL, `pip install -r backend/requirements.txt`, arranque del backend/Flutter y `flutter build web --release` con `CAMPUSMARKET_API_BASE_URL`); `README.md:530` en adelante documenta el redespliegue con `git archive` + `az webapp deploy` y los checks posteriores. |
| Pipeline en verde sobre la rama principal | URL del último run y su conclusión | Cumple | Run `Pruebas del backend` sobre `master` en el hash `784d788`, conclusión `success` (2026-09-28T04:50:22Z, antes del cierre): https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/36379371983. |
| Logs estructurados | archivo de configuración y ejemplo de línea | Cumple | `backend/app/observability.py:117` arma `log_entry` con `timestamp`, `level`, `event`, `request_id`, `method`, `path`, `status_code` y `duration_ms`, y `:128-130` lo emite con `json.dumps`. Ejemplo real en `README.md:629-641`. |
| Métrica consultable asociada a un escenario de calidad | nombre de la métrica y escenario al que corresponde | Cumple | `backend/app/observability.py:73` declara `scenario_id: "EC-01"` (rendimiento, ventana de `GET /publicaciones`, umbral 2000 ms) y la expone en `backend/app/main.py:52` (`/ops/metrics/ec01`). El README acota que es un proxy del backend, no la medición extremo a extremo. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example`, referencias a secretos en el workflow | Cumple | `infra/main.bicep:11` marca `@secure() mysqlAdministratorPassword`; la configuración viaja por App Settings y variables `CAMPUSMARKET_DB_*`; no hay ningún `.env` versionado y el barrido de credenciales sobre el hash solo devuelve `os.environ[...]` (no valores). |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | documento con volumen supuesto y cálculo | Cumple | `docs/arc42/02-restricciones.md:304` (R-11) parte de supuestos de carga (tres integrantes, concurrencia baja, sin alta disponibilidad), desglosa GitHub Pages / App Service F1 / MySQL `Standard_B1ms` y fija el punto de ruptura; `README.md` recoge la estimación (~USD 14.71/mes de MySQL antes de créditos académicos). |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07*` | Cumple | `docs/arc42/07-vista-despliegue.md:89-116` dibuja una caja por pieza (Frontend, Backend API, Persistencia) y su columna «Ejecuta en» (GitHub Pages, Azure App Service, Azure MySQL). |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02*` | Cumple | `docs/arc42/02-restricciones.md:304` (R-11, límite económico y punto de ruptura) y `:387` (R-12, «No dependencia de tarjeta bancaria personal»), ambas en la sección 2. |
| Un ADR por decisión de plataforma, con alternativa descartada | archivos de `docs/adr/` de esta semana | Cumple | Un ADR por pieza: `docs/adr/0006-publicar-frontend-flutter-web-en-github-pages.md`, `0007-desplegar-api-fastapi-en-azure-app-service.md` y `0008-desplegar-mysql-en-azure-flexible-server.md`, cada uno con su alternativa descartada (servir Flutter desde App Service; servidor de laboratorio; MySQL autogestionado) y la capa gratuita/beneficio verificado. `0005` conserva la decisión global de despliegue por pieza. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET`, clon anónimo con `--filter=blob:none` exitoso; rama `origin/master`. | Cumple | Responde sin autenticación y el nombre sigue `AS_202620_<PROYECTO>`. |
| Estructura mínima presente | El árbol contiene `docs/arc42/`, `docs/adr/` (0001-0008), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2. |
| Estado calificado identificable | `784d788` en `origin/master`, `2026-09-27T23:50:19-05:00`, último commit ≤ cierre (2026-09-28T05:00:00Z): `Merge pull request #44 from ISCOUTB/S8-cierre-evidencia`. | Cumple | No hay commits posteriores al cierre; la punta actual coincide con el hash calificado. |
| Nombres de ADR según la convención | `0001-usar-monolito-modular.md` … `0008-desplegar-mysql-en-azure-flexible-server.md`. | Cumple | Los ocho pasan el filtro `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | ADR-0002 aceptado el 2026-09-05 (`77e1323`) y editado el 2026-09-06 en `d72d6ac`, `3bb84a9` y `04fe631`; ADR-0003 aceptado el 2026-09-15 (`485249a`) y editado el 2026-09-16 en `df72b1c`; ADR-0005 aceptado el 2026-09-27 (`39f0952`) y reescrito el mismo día en `0e2b85b` (+411/-207). | No cumple | El contrato §4 prohíbe editar un ADR aceptado sin declarar un ADR de reemplazo; ninguna de esas ediciones lo declara. Solo ADR-0001, 0004, 0006, 0007 y 0008 tienen un único commit. |
| `docs/ia.md` al día para la semana | `083bcc3` (2026-09-27) registra el uso de IA de S8 con la columna de lo rechazado y su motivo (p. ej. rechazo de un health check que solo comprueba que FastAPI esté vivo). | Cumple | El archivo crece dentro del periodo y documenta rechazos técnicos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `.sonarcloud.properties:1-4` existe, pero `.github/workflows/backend-tests.yml` no contiene ningún paso que invoque el scanner de Sonar; no se aporta la URL pública del análisis con estado del Quality Gate para el hash revisado. | No cumple | El README afirma «Quality Gate: Passed» sin la evidencia del §8 (línea del workflow + URL pública del análisis). Un badge o una afirmación no prueban que SonarCloud haya corrido sobre el hash. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de credenciales sobre el hash sin coincidencias reales (solo `os.environ`/`secrets.*`); ningún `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | El password de CI (`campusmarket_ci`) es un valor de prueba contenido en el propio workflow, no una credencial de producción. |
| Contribución de todos los integrantes | `shortlog -sne 784d788` consolidado por identidad de correo idéntica: `nilver-garcia` y `Nnigarp` comparten la misma dirección (193), `camilixo92` 26, `Carulla-sd` 19. | Cumple | Los tres integrantes declarados tienen commits. La identidad `Nnigarp en Github`, con otra dirección, no se consolida por parecido de nombre, pero es irrelevante: los tres están representados. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `784d788` — `2026-09-27T23:50:19-05:00 Merge pull request #44 from ISCOUTB/S8-cierre-evidencia`.
- **Veredicto**: al día (sin pendientes de la ficha salvo las dos filas de despliegue diferidas).
- **Commits posteriores al cierre**: ninguno; la punta actual coincide con el hash calificado.
- Resumen: la entrega S8 sí llegó y está completa. Infraestructura versionada (`infra/main.bicep`), REPL reproducibilidad en README, CI en verde sobre `master`, logs JSON con campos, métrica `/ops/metrics/ec01` ligada a EC-01, secretos vía parámetro `@secure()`/App Settings, estimación de costo con supuestos y punto de ruptura, arc42 §7 con una caja por pieza y §2 con el límite de costo y la restricción de tarjeta, y un ADR por decisión de plataforma (0006/0007/0008) con alternativa descartada. Transversalmente siguen abiertos SonarCloud (sin scanner en el workflow ni URL pública del análisis) y la edición de ADR aceptados (0002/0003/0005).

Pendientes que siguen abiertos:
- Comprobación externa de la URL y del health check (filas diferidas por decisión docente).
- Acreditar SonarCloud con la línea del scanner en el workflow y la URL pública del análisis con Quality Gate.
- No editar ADR aceptados: los ajustes a ADR-0002, ADR-0003 y ADR-0005 debieron ir en un ADR nuevo o declarar el reemplazo.

## Recuento y nota sugerida

**10 de 10 criterios graduables Cumple** (la matriz de la ficha tiene 12 filas; las 2 filas de despliegue quedan pendientes de calificar en esta pasada).

**Propuesta provisional al docente — `nota = 1 + 4 × (10/10) = 5.0`**; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL del sistema desde fuera de la red: No verificado por decisión docente; el repositorio la declara en `README.md:124/128`. No se abrió ninguna URL.
- Health check: No verificado por decisión docente; la ruta existe en `backend/app/main.py:60,65`. No se consultó.
- SonarCloud: `.sonarcloud.properties` sin invocación del scanner en el workflow y sin URL pública del análisis con Quality Gate: fila transversal No cumple.
- ADR aceptados editados: ADR-0002 (`d72d6ac`, `3bb84a9`, `04fe631`), ADR-0003 (`df72b1c`) y ADR-0005 (`0e2b85b`) sin reemplazo declarado.

## Hallazgos para la planilla

- La entrega S8 cumple los 10 criterios graduables: despliegue público documentado, IaC (Bicep), CI verde, observabilidad, secretos, costos y ADR por plataforma.
- SonarCloud sigue sin evidencia auditable: hay `.sonarcloud.properties`, pero ningún paso `sonar` en `.github/workflows/backend-tests.yml` ni URL pública del análisis con Quality Gate (pendiente desde S6).
- ADR-0002, ADR-0003 y ADR-0005 fueron editados después de su aceptación sin declarar un ADR de reemplazo.
- No hay commits posteriores al cierre: la punta actual coincide con el hash calificado.
