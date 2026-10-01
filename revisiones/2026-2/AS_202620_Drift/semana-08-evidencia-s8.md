# semana-08-evidencia-s8 · Drift

> Revisión definitiva: hash 74709aa, última revisión ≤ cierre (2026-09-28T05:00:00Z) en origin/master.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `74709aa` en `origin/master` (2026-09-27T23:58:28-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

> El estado calificado se movió respecto de la pasada temprana (que revisó `9334a03`): el equipo empujó el 27 de septiembre. Se releyeron del repositorio todas las filas que la pasada preliminar había dejado como no incluidas.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `docs/evidencias/evidencia_semana8.md:15` declara `https://drift-utb-202620-g5fvchdcgpcthkeg.mexicocentral-01.azurewebsites.net`, y `docs/arc42/arc42_7_vista_despliegue.md:65` la repite para el backend. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. No se abrió ninguna URL. El repositorio sí declara una URL pública de backend. |
| Health check consultable | Ruta `GET /health` en `backend/app/main.py:90` (responde `{"status":"ok"}`); `docs/evidencias/evidencia_semana8.md:48-53` y `docs/arc42/arc42_7_vista_despliegue.md` §7.4 la documentan. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio prueba que la ruta de health existe (`backend/app/main.py:90`). |
| Infraestructura como código versionada en el repositorio | `infra/azure/main.bicep` (App Service F1 Free, Python 3.12, TLS 1.2), `infra/azure/main.parameters.json`, `deployment/vercel/` (función serverless) y `.github/workflows/master_drift-utb-202620.yml`. | Cumple | Infraestructura descrita como código en Bicep, no en pasos manuales. |
| El entorno se puede recrear siguiendo el README | README.md «Instalación» y «Comando Unico de Ejecuccion» (`python scripts/start.py`, con requisitos previos y pruebas); `infra/azure/README.md` documenta la recreación con `az deployment group create` sobre `main.bicep`. | Cumple | Arranque local con un solo comando y procedimiento de infraestructura versionado. |
| Pipeline en verde sobre la rama principal | Run `CI` sobre `master` del hash `74709aa`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/36379911184 (2026-09-28T04:58:30Z). | Cumple | Run atado al hash calificado de `master`. |
| Logs estructurados | `backend/app/infrastructure/observability.py:9` define `JsonFormatter` y `:37` `log_event`; `backend/app/main.py` emite `search_completed`/`search_failed` con campos (`duration_ms`, `results_count`, `query_length`). Ejemplo JSON en `docs/evidencias/evidencia_semana8.md`. | Cumple | El grep de la ficha no lo detecta porque usa `logging.Formatter` propio; verificado a mano. |
| Métrica consultable asociada a un escenario de calidad | `GET /metrics` en `backend/app/main.py:94`; métrica `drift_search_latency_ms` en `backend/app/infrastructure/observability.py:56`, asociada al escenario **E1 (rendimiento)** en `docs/evidencias/evidencia_semana8.md:422`. | Cumple | Métrica nombrada y ligada explícitamente a E1. |
| Secretos fuera del código y tomados del entorno o del almacén | `.github/workflows/master_drift-utb-202620.yml:40-42` usa `secrets.AZUREAPPSERVICE_CLIENTID/TENANTID/SUBSCRIPTIONID` (OIDC); `infra/azure/README.md` declara que los secretos no viven en el repositorio; sin `.env` versionado ni coincidencias del barrido. | Cumple | Los secretos se toman del almacén de GitHub. `docs/evidencias/evidencia_semana8.md:468` afirma un `.env.example` que no existe en el árbol calificado; las variables públicas están en `infra/azure/main.parameters.json`. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/evidencias/Estimacion_costos.md`: supuestos de volumen (`:3`), costo por componente `$0` (`:24-27`) y sección «Punto de ruptura de la capa gratuita» (`:29`). | Cumple | El punto de ruptura se describe de forma cualitativa (agotar el crédito de Azure for Students / límites de Vercel Hobby), sin umbral numérico de volumen. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42_7_vista_despliegue.md` con diagrama de despliegue y tabla §7.2 (`:42`) pieza/tecnología/ubicación; §7.4 describe el backend (`:65`). | Cumple | Una caja por pieza (frontend Vercel, backend Azure, CI, IaC) y su ubicación. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/arc42_2_restricciones.md:76` §2.7 «Límite de costo y restricción de tarjeta», con §2.7.1 de tarjeta (`:89`). | Cumple | Recoge el límite de costo y la condición de tarjeta. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0005-estrategia-despliegue.md` (frontend Vercel / backend Azure / Supabase) y `docs/adr/0006-despliegue-serverless-api-busqueda.md` (serverless de la búsqueda), ambos con alternativas A/B y sus desventajas. | Cumple | Un ADR por decisión de plataforma con alternativa descartada; la capa gratuita se afirma (Azure for Students, Vercel Hobby) pero no se verifica con cifras. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_Drift`, clonado sin autenticación; responde al protocolo git. | Cumple | Nombre conforme a `AS_202620_<PROYECTO>` y público. |
| Estructura mínima presente | Árbol de `74709aa`: `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Seis rutas del contrato presentes; arc42 usa prefijo `arc42_N_` (desviación de forma, no de contenido). |
| Estado calificado identificable | Rama `origin/master`; hash `74709aa` (2026-09-27T23:58:28-05:00), último ≤ cierre 2026-09-28T05:00:00Z. | Cumple | Trece commits posteriores al cierre, registrados en overall. |
| Nombres de ADR según la convención | `docs/adr/0001-adoptar-arquitectura-hexagonal.md` … `0006-despliegue-serverless-api-busqueda.md`, todos `NNNN-kebab-case.md`. | Cumple | Seis nombres conformes. |
| ADR aceptados no reescritos | `docs/adr/0002-adoptar-nextjs-fastapi-arquitectura-hexagonal.md:3` está `Aceptado` y `git log --follow` muestra ediciones posteriores a su creación (`45b5987`, 2026-08-24): `70e52e2` (2026-09-05T22:40:14-05:00) y `9488544` (2026-09-13T13:40:00-05:00), sin ADR que lo reemplace. | No cumple | CONTRATO §4 prohíbe editar un ADR aceptado. ADR-0001 sí declara reemplazo por ADR-0002, pero ADR-0002 (vigente) fue editado después de aceptarse. |
| `docs/ia.md` al día para la semana | Historial de `docs/ia.md` con entradas del periodo; última del hash calificado `74709aa` (2026-09-27T23:58:28-05:00, «Add deployment planning section»). Contenido con «Alternativa descartada» y su motivo (p. ej. documentar el despliegue solo en el README). | Cumple | Registra rechazos con motivo. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `sonar-project.properties` existe y el README menciona SonarQube Cloud, pero `.github/workflows/ci.yml` no contiene ningún paso que invoque el scanner ni referencia a `SONAR_TOKEN`; el proyecto es público con Quality Gate `OK` (consultado por API), sin run que lo relacione con el hash revisado. | No cumple | Contrato §8: falta la línea del workflow que ejecuta el scanner y el run exitoso asociado; un proyecto con Quality Gate no prueba que el análisis corra en CI. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de secretos sobre `74709aa` sin coincidencias reales; ningún `.env` versionado; el único acierto es `id-token: write` (permiso de workflow). | Cumple | Sin credenciales en el árbol revisado. |
| Contribución de todos los integrantes | `git shortlog -sne 74709aa` consolida por correo idéntico en 4 personas: `JerryDBM`+«Sherry» (115), `JoshuaR01`+`JoshXX` (99), `lmpdiaz12`+«Luis Mario Perez Diaz» (85) y `maufern4ndez`+«Mauricio Andres Fernandez Espinosa» (66). | Cumple | Coinciden con los 4 integrantes de `EQUIPOS.md`; aportes repartidos. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `8a00556` (`2026-09-30T22:34:57-05:00`, «Update links and formatting in evidencias_semana9.md»), 13 commits posteriores al cierre.
- **Veredicto**: con pendientes.
- Resumen: la punta actual de `master` conserva las piezas de S8 del hash calificado (Bicep de Azure, despliegue serverless de Vercel, observabilidad con logs JSON y `/metrics` ligado a E1, costos, arc42 §7 y §2 y ADR de plataforma) y avanza hacia S9 con evidencias nuevas. Los 13 commits posteriores al cierre son posteriores a la entrega y no cambian la matriz; algunos runs de despliegue del 1 de octubre salieron en rojo, mientras que el job `CI` siguió en verde.

Pendientes que siguen abiertos:
- ADR aceptados editados después de su aceptación (ADR-0002), sin ADR de reemplazo.
- SonarCloud: falta un paso del workflow que ejecute el scanner y el run asociado al hash revisado.
- URL y health check: quedan pendientes de calificar con la URL de Moodle.

## Recuento y nota sugerida

**10 de 10 criterios graduables.** (Las 2 filas de despliegue quedan diferidas y no entran en el recuento.)

**Propuesta provisional al docente — `nota = 1 + 4 × (10/10) = 5.0`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- URL del sistema accesible desde fuera de la red: pendiente de calificar; la evidencia declara una URL pública, pero no se abrió ninguna.
- Health check consultable: pendiente de calificar; la ruta existe en el código (`backend/app/main.py:90`).
- Sustentación: no evaluable desde el repositorio.
- Filas transversales abiertas: ADR aceptados no reescritos (No cumple) y Pipeline/SonarCloud/Quality Gate (No cumple).

## Hallazgos para la planilla

- El estado calificado cambió respecto de la pasada temprana: la definitiva usa `74709aa` (27/09), no `9334a03`.
- S8 resolvió en el repositorio IaC (Bicep de Azure + serverless de Vercel), logs JSON, `/metrics` ligado a E1, estimación de costos, arc42 §7 y §2, y ADR de plataforma.
- Se corrige el arrastre previo: ADR-0002 (vigente, aceptado) fue editado el 05/09 y el 13/09 sin ADR de reemplazo → fila transversal en No cumple.
- SonarCloud sigue sin integrarse al pipeline: no hay paso del workflow que invoque el scanner pese a existir `sonar-project.properties`; el hallazgo sigue abierto desde S6.
- `docs/evidencias/evidencia_semana8.md` afirma un `.env.example` que no existe en el árbol calificado; las variables públicas viven en `infra/azure/main.parameters.json` y los secretos en GitHub Secrets.
- URL y health check quedan pendientes de calificar por decisión docente (se entregan por Moodle).
