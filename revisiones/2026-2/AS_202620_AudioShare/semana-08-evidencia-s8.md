# semana-08-evidencia-s8 · AudioShare

> Revisión definitiva: hash `e4789d8`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `e4789d88` en `origin/master` (2026-09-27T23:49:01-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | código de respuesta y tiempo, con la hora de la comprobación | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio declara la URL pública: `README.md:153` (`https://audioshare-api.icypond-27a6987e.canadacentral.azurecontainerapps.io`), replicada en `docs/despliegue.md:94` y en `docs/adr/0004-despliegue-api-azure-vs-laboratorio.md:123`. No se abre ninguna URL en esta pasada. |
| Health check consultable | ruta y código de respuesta | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. Ruta de health en el código: `src/app.ts:327` (`app.get("/health", ...)`), declarada en `README.md:154` (`Health check: /health`). No se consulta en esta pasada. |
| Infraestructura como código versionada en el repositorio | rutas de los archivos de infraestructura | Cumple | `Dockerfile:1` (producción multi-etapa con HEALTHCHECK), `docker-compose.yml:1` (servicios + volumen `audioshare-data`), `.github/workflows/publish-image.yml:1` (build y push de la imagen). La infraestructura describe el entorno desplegado, no solo el devcontainer. |
| El entorno se puede recrear siguiendo el README | sección del README con el procedimiento | Cumple | `README.md:80-90` documenta el arranque local con `npm run dev` (instalación y tests en `README.md:73-104`); `README.md:151-160` remite a `docs/despliegue.md` para recrear el entorno desplegado (`docker compose up -d --build` y el alta en Azure Container Apps). El procedimiento de despliegue vive en el documento enlazado, no inline. |
| Pipeline en verde sobre la rama principal | URL del último run y su conclusión | No cumple | En el último push a `origin/master` (runs del 2026-09-28T04:48:32Z) el workflow **Flutter** concluyó `failure`: https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/36379253148. Los workflows `CI` (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/36379253187) y `Publicar imagen` (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/36379253129) sí concluyeron `success`. El pipeline no está en verde. |
| Logs estructurados | archivo de configuración y ejemplo de línea | Cumple | `src/shared/logger.ts:1-31` emite una línea JSON por evento con `level`, `msg`, `ts` y campos extra; el ejemplo está en el propio encabezado (`src/shared/logger.ts:11`). Uso real: `src/app.ts:80` (`log.info("room.created", ...)`), `src/app.ts:206` (`log.info("room.play", ...)`) y `src/server.ts:8` (`log.info("server.started", ...)`). |
| Métrica consultable asociada a un escenario de calidad | nombre de la métrica y escenario al que corresponde | Cumple | `src/shared/metrics.ts:18-40` expone `rooms_created_total`, `play_events_total` y `last_play_receiver_count`, declarando `aspecto: "A-01"` y `escenarios_relacionados: ["EC-01", "EC-04"]`; ruta consultable en `src/app.ts:339` (`/metrics`). El archivo explica que es un proxy operacional, no la medición en ms de EC-01. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example`, referencias a secretos en el workflow | Cumple | `.env.example:1-4` declara las variables; no hay ningún `.env` versionado; el barrido de credenciales sobre el hash no encontró coincidencias. El workflow toma los valores del almacén: `publish-image.yml:17-19` (`secrets.DOCKERHUB_USERNAME`, `secrets.DOCKERHUB_TOKEN`) y `ci.yml:23` (`secrets.SONAR_TOKEN`). |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | documento con volumen supuesto y cálculo | Cumple | `docs/costos-mensuales.md:8-20` parte del volumen de EC-01/EC-04 (500 salas/mes, 3 receptores, ~1.8 MB/mes de NDJSON) y calcula costo por alternativa; `docs/costos-mensuales.md:44-50` identifica el punto de ruptura: `minReplicas: 1` (`docs/costos-mensuales.md:47`) consume ~1.296.000 vCPU-s/mes y rompe el tramo gratis por ~7×. No es el catálogo del proveedor. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07*` | Cumple | `docs/arc42/src/07_deployment_view.adoc:13-24` tiene una tabla con una fila por pieza (API, cliente Web, cliente Android) y su columna «Dónde se ejecuta» (`:14`); el resto de la sección mapea `Dockerfile`/`docker-compose.yml` al despliegue. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02*` | Cumple | `docs/arc42/src/02_architecture_constraints.adoc:9-13` fija «Presupuesto máximo del proyecto: $0 (R-01)», exige que al menos una alternativa funcione sin tarjeta y aclara que Azure for Students tampoco exige tarjeta. |
| Un ADR por decisión de plataforma, con alternativa descartada | archivos de `docs/adr/` de esta semana | Cumple | `docs/adr/0004-despliegue-api-azure-vs-laboratorio.md:1-131` decide la plataforma de despliegue de la API (Azure Container Apps) con alternativas A (servidor del laboratorio) y B (Azure) evaluadas, descarta explícitamente Render Free (`:81`) y documenta la capa gratuita verificada y sus restricciones (`:32`, `:86-110`). Estado `aceptado` (`:3`). |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_AudioShare`, clon anónimo con `--filter=blob:none` exitoso; rama `origin/master`. | Cumple | El repositorio responde sin autenticación y su nombre sigue `AS_202620_<PROYECTO>`. |
| Estructura mínima presente | El árbol contiene `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Desviación de formato: arc42 está en AsciiDoc (`.adoc`) y falta la sección 11; el resto de rutas existen. |
| Estado calificado identificable | `e4789d88` en `origin/master`, `2026-09-27T23:49:01-05:00`, anterior al cierre 2026-09-28T05:00:00Z. | Cumple | No hay commits posteriores al cierre: la punta actual coincide con el hash calificado. |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md`, `0002-estrategia-integracion.md`, `0003-transicion-a-flutter.md`, `0004-despliegue-api-azure-vs-laboratorio.md`. | Cumple | Los cuatro siguen `NNNN-titulo-kebab-case.md`. |
| ADR aceptados no reescritos | ADR-0001 aceptado en `924d133` (2026-09-04) y editado después en `453710f` y `354f1f5` (2026-09-21, actualiza referencias a ADR-0003 y a C4); ADR-0003 aceptado (fecha 2026-09-20) y editado en `d11f39a` (2026-09-25). | No cumple | Ninguna de las ediciones posteriores declara un ADR de reemplazo: el contrato §4 prohíbe editar un ADR aceptado. |
| `docs/ia.md` al día para la semana | Último commit sobre `docs/ia.md`: `5a6d73b` (2026-09-20); el documento cierra en «actualizado durante la semana 7». | No cumple | El registro tiene contenido y rechazos con motivo hasta S7, pero no se actualizó dentro del periodo de S8. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `sonar-project.properties:1-6` (configuración y `sonar.organization=cardonavincent26`); `ci.yml:17-23` invoca el scanner con `SONAR_TOKEN`; el run `CI` concluyó `success` (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/36379253187). | No cumple | Falta la URL pública del análisis con estado del Quality Gate (tercera evidencia del §8) y la organización de SonarCloud no es `isco-utb`; además el workflow `Flutter` de la rama está en rojo. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de credenciales sobre el hash sin coincidencias (solo `secrets.*` como referencia de workflow); ningún `.env` versionado; `git log -S"BEGIN PRIVATE KEY"` sin coincidencias. | Cumple | No se encontraron credenciales reales. |
| Contribución de todos los integrantes | `shortlog -sne` consolidado: Elian Daniel Perea Vanegas 60, cardonavincent26-design 59, Yeiver Andrés Vergel Pérez 41, Santiago Adolfo Camacho Hernández 37. | Cumple | Cuatro identidades para cuatro integrantes declarados; la atribución de `cardonavincent26-design` a Vincent Cardona es presunta (no se consolida por parecido de nombre). |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subió tarde o corrigió entregas anteriores, aquí se nota.

- **Punta actual revisada**: `e4789d887fe59b2ace65bd1d2680f79758db5b54 2026-09-27T23:49:01-05:00 S8: URL desplegada en Azure, evidencia de health y restricciones de la suscripción`
- **Veredicto**: con pendientes
- **Commits posteriores al cierre**: ninguno; la punta actual coincide con el hash calificado.
- Resumen: la entrega S8 sí llegó y está bien documentada: infraestructura versionada, README y `docs/despliegue.md` con el procedimiento, logs JSON con campos, métrica ligada a A-01/EC-01/EC-04, secretos fuera del código, estimación de costo con supuestos y punto de ruptura, arc42 §7 y §2, y un ADR-0004 de plataforma con alternativa descartada. Lo que impide el pleno es que el workflow **Flutter** de la rama principal está en rojo en el último push y que no hay URL pública del análisis de SonarCloud con Quality Gate; también quedan dos ADR aceptados editados sin reemplazo y `docs/ia.md` sin entrada de S8.

Pendientes que siguen abiertos:
- Poner en verde el workflow `Flutter` sobre `origin/master`.
- Publicar la URL pública del análisis de SonarCloud con su Quality Gate (y alinear la organización, hoy `cardonavincent26`).
- Actualizar `docs/ia.md` con el uso de IA de S8.
- No editar ADR aceptados: los ajustes a ADR-0001 y ADR-0003 debieron ir en un ADR nuevo.

## Recuento y nota sugerida

**9 de 10 criterios graduables** (la matriz de la ficha tiene 12 filas; las 2 filas de despliegue quedan pendientes de calificar en esta pasada).

**Propuesta provisional al docente — `nota = 1 + 4 × (9/10) = 4.6`**; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL del sistema desde fuera de la red: No verificado por decisión docente (la URL se entrega por Moodle y no está disponible). El repositorio la declara en `README.md:153`.
- Health check: No verificado por decisión docente. La ruta existe en `src/app.ts:327` y se declara en `README.md:154`.
- Run en verde del workflow `Flutter`: falla en el último push a `origin/master` (run 36379253148).
- SonarCloud: falta la URL pública del análisis y el estado del Quality Gate para el hash revisado.

## Hallazgos para la planilla

- El workflow `Flutter` concluye `failure` en cada push reciente a `origin/master`; `CI` y `Publicar imagen` sí están en verde.
- `sonar-project.properties` apunta a la organización de SonarCloud `cardonavincent26`, no a `isco-utb` como pide el CONTRATO §8, y no se aporta la URL pública con Quality Gate.
- ADR-0001 y ADR-0003 fueron editados después de su aceptación sin declarar un ADR de reemplazo.
- `docs/ia.md` no tiene entrada de la semana 8.
- `docs/arc42` sigue en AsciiDoc y sin la sección 11.
- La entrega de despliegue sí está versionada: `Dockerfile`, `docker-compose.yml`, `publish-image.yml`, `docs/despliegue.md` y ADR-0004 con la alternativa descartada y la capa gratuita verificada.
