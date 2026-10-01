# Semana 8 · Despliegue reproducible, CI y observabilidad · PideUtb

> Revisión definitiva: hash `a94bf4e`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `a94bf4e` en `origin/master` (2026-09-27T20:30:08-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

El estado cambió respecto de la pasada preliminar: el commit calificado pasó de
`9db30b9` (2026-09-21) a `a94bf4e` (2026-09-27), que incorpora el despliegue en
Render, `infra/` con Terraform, `docs/evidencia-s8.md`, el ADR-0004 de
plataforma, la observabilidad y la vista de despliegue. Sí hay commits
posteriores al cierre (hasta `0393eee`, 2026-09-30, incl. la migración a
PostgreSQL); se registran en `overall` y no cambian la matriz.

## Matriz de la ficha

Las dos filas de despliegue quedan **diferidas** por decisión docente: la URL se
entrega por Moodle y no está disponible en esta pasada. No se abrió, consultó ni
sondeó ninguna URL.

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | código de respuesta y tiempo, con la hora de la comprobación | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio declara `Sitio` `README.md:13` (`https://pideutb-sitio.onrender.com`) y `API` `README.md:14` (`https://pideutb-api.onrender.com`), replicadas en `docs/evidencia-s8.md:16-23`. No se abre ninguna URL en esta pasada. |
| Health check consultable | ruta y código de respuesta | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. Ruta en el código: `backend/app/main.py:81-88` (`@app.get("/health")`, `health`) sobre las sondas de `backend/app/salud.py` (`revisar()`, que devuelve `503` si alguna dependencia cae); declarada en `README.md:15`. No se consulta en esta pasada. |
| Infraestructura como código versionada en el repositorio | rutas de los archivos de infraestructura | Cumple | `infra/render.tf` (sitio), `infra/supabase.tf` (PostgreSQL), `infra/github.tf` (protección de rama), `infra/providers.tf`, `infra/variables.tf`, `infra/outputs.tf` y `.github/workflows/ci.yml`. La API queda fuera de Terraform por límite del proveedor (plan gratuito), y la excepción está documentada con el procedimiento manual en `infra/README.md`. |
| El entorno se puede recrear siguiendo el README | sección del README con el procedimiento | Cumple | `README.md:118-141` documenta el arranque local con un solo comando (`README.md:125`) y las pruebas. La recreación del entorno público vive en `infra/README.md` (Terraform + alta manual de la API) y no está enlazada desde el README principal: hueco de enlace, no de procedimiento. |
| Pipeline en verde sobre la rama principal | URL del último run y su conclusión | Cumple | Consulta sin autenticar a `actions/runs?head_sha=a94bf4e87f84291edc11beed62df0c9d8cf57db7`: el hash calificado tiene un único run, `CI` #43, disparado por `push`, conclusión `success` (2026-09-28T01:30:11Z): https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/36366211067. Ningún run del commit quedó en `failure`/`cancelled`. |
| Logs estructurados | archivo de configuración y ejemplo de línea | Cumple | `backend/app/observabilidad.py:45` (`class FormatoJSON`) emite una línea JSON por petición y `:66` la serializa con `json.dumps`; `:174` (`configurar_logs`) la conecta a stdout. Ejemplo real en `docs/evidencia-s8.md:99-105` con `request_id`, `method`, `path`, `status` y `duration_ms`. |
| Métrica consultable asociada a un escenario de calidad | nombre de la métrica y escenario al que corresponde | Cumple | `backend/app/main.py:116-122` expone `/metricas` con p50/p95/max por operación; `docs/evidencia-s8.md:150` la liga a **ESC-02** y acota que mide la parte del presupuesto controlada por el servidor, no el escenario completo. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example`, referencias a secretos en el workflow | Cumple | `infra/variables.tf` y `infra/providers.tf:55,60,64` toman los tokens por variable (`var.render_api_key`, etc.); `infra/.gitignore` excluye `*.tfvars`, `*.tfstate`, `.terraform/`; `infra/terraform.tfvars.example:20,29,60` usa solo marcadores `XXXX`; no hay `.env` versionado y el barrido de credenciales sobre el hash no encuentra valores reales. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | documento con volumen supuesto y cálculo | Cumple | `docs/comparacion-despliegue.md:149` («Supuestos declarados»: 200 pedidos/día, 5 llamadas por pedido, 2 h de pico), `:158` («Costo mensual con el volumen estimado», total $0) y `:170-183` fija el punto de ruptura de cada capa (Vercel ≈1 920 pedidos/día; Render se rompe por latencia desde el primer día). |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07*` | Cumple | `docs/arc42/arc42.md:666` (sección 7) y `:678` (§7.1) listan las cinco piezas con su columna «Dónde corre», más topología, protocolos y deuda conocida. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02*` | No cumple | La sección 2 recoge el límite de costo (`arc42.md:122-127`, «Sin presupuesto para el proyecto», «Despliegue en Render, plan gratuito»), pero **no** la restricción de tarjeta: la frase «ninguna exige tarjeta» solo está en `docs/comparacion-despliegue.md:86,109` y en ADR-0004, fuera de la sección 2. |
| Un ADR por decisión de plataforma, con alternativa descartada | archivos de `docs/adr/` de esta semana | Cumple | `docs/adr/0004-plataforma-de-despliegue.md` decide el contenedor de proceso persistente (Render free) frente a la función sin servidor (Vercel Hobby), con la alternativa descartada, el motivo decisivo (pool de conexiones) y la capa gratuita/condición de tarjeta verificadas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_PideUtb`, clon anónimo con `--filter=blob:none` exitoso; rama `origin/master`. | Cumple | Responde sin autenticación y el nombre sigue `AS_202620_<PROYECTO>`. |
| Estructura mínima presente | El árbol contiene `docs/arc42/`, `docs/adr/` (0001-0004), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2; arc42 en un único archivo, C4 en Markdown. |
| Estado calificado identificable | `a94bf4e` en `origin/master`, `2026-09-27T20:30:08-05:00`, último commit ≤ cierre (2026-09-28T05:00:00Z): `Contrastar las proyecciones del taller contra lo medido en produccion`. | Cumple | La punta actual (`0393eee`, 2026-09-30) sí tiene commits posteriores; se registran en `overall`. |
| Nombres de ADR según la convención | `0001-estilo-arquitectonico.md`, `0002-propiedad-datos-establecimiento.md`, `0003-estrategia-integracion.md`, `0004-plataforma-de-despliegue.md`. | Cumple | Los cuatro pasan el filtro `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | ADR-0001 aceptado el 23/08/2026 (`b5f0310`) y editado el 2026-09-07 (`1b4f0f6`, se añade sección de trazabilidad) y el 2026-09-20 (`1864353`, se **reescribe el título**); ADR-0002 aceptado el 13/09/2026 (`9eda1f3`) y editado el 2026-09-20 (`1864353`, título reescrito). | No cumple | El contrato §4 prohíbe editar un ADR aceptado sin declarar un ADR de reemplazo. El propio mensaje de `1864353` dice «Los títulos de ADR 0001 y 0002 se reescriben»; ninguna edición declara reemplazo. ADR-0003 y ADR-0004 tienen un único commit. |
| `docs/ia.md` al día para la semana | El último commit que toca `docs/ia.md` en o antes del hash calificado es `356369d` (2026-09-20, contenido hasta S7). La entrada de S8 llega en `e048523` (2026-09-28T13:42-05:00), posterior al cierre. | No cumple | En el estado calificado el registro no crece dentro del periodo de S8; la entrada de la semana llegó tarde. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `sonar-project.properties` (config), `.github/workflows/ci.yml` con `sonarqube-scan-action` y `sonarqube-quality-gate-action`, y el panel público declarado en `README.md`/`docs/calidad-sonarcloud.md`. | No verificado | El job `calidad` está condicionado a `SONAR_TOKEN`, que `infra/README.md` marca como **Pendiente**, y el run citado en `docs/calidad-sonarcloud.md` corresponde a un commit anterior (`130c653`). No se pudo confirmar el estado del Quality Gate para el hash calificado desde el repositorio. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de credenciales sobre el hash sin valores reales (solo `var.*` y marcadores `XXXX`); ningún `.env` versionado; `.tfvars`/`.tfstate` excluidos por `infra/.gitignore`. | Cumple | En el estado calificado no hay credenciales. La contraseña del PostgreSQL de CI (`pruebas`) aparece solo en commits posteriores al cierre y se retira en `1744560` (2026-09-29), fuera del historial calificado. |
| Contribución de todos los integrantes | `shortlog -sne a94bf4e` consolidado con `.mailmap` por correo idéntico: `Santiago Cuesta` + `Santiago-C0` 48, `daniarriet` 26, `Ruddy` + `ruddy2000utb-droid` 10. | Cumple | Los tres integrantes declarados tienen commits atribuibles. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `0393eee` — `2026-09-30T11:25:53-05:00 Hacer que requirements.txt incluya requirements.in en vez de copiarlo`.
- **Veredicto**: con pendientes.
- **Commits posteriores al cierre** (no cambian la matriz): `0393eee`, `1e8ad51` (merge PR #11 migración a Supabase), `ed57869`, `1744560` (quita la credencial del contenedor de pruebas), `1c676e9` (migra repositorios a PostgreSQL y cierra V-09), `0441ef2`, `373817f`, `8898291`, `e048523` (registro de IA de S8), `c04bc50`.
- Resumen: la punta avanzó la migración a PostgreSQL y cerró la deuda de estado en memoria, además de retirar la credencial de CI que SonarCloud marcó y registrar la IA de S8. Nada de eso cuenta para el estado calificado. En el estado calificado la entrega S8 está mayormente cubierta (IaC con Terraform, logs JSON, métrica ligada a ESC-02, secretos por variable, costos con supuestos y punto de ruptura, arc42 §7, ADR-0004 de plataforma y README con arranque de un comando). Quedan abiertos la evidencia de costo/tarjeta en arc42 §2, el registro de IA de S8 (llegó tarde), la edición de ADR aceptados y la confirmación del Quality Gate de SonarCloud para el hash calificado (el run de CI ya quedó citado).

Pendientes que siguen abiertos:
- Comprobación externa de la URL y del health check (filas diferidas por decisión docente).
- Recoger el límite de costo **y** la restricción de tarjeta en arc42 §2, no solo en el documento de comparación.
- Actualizar `docs/ia.md` con el uso de IA de S8 dentro del periodo (la entrada llegó el 28/09, después del cierre).
- No editar ADR aceptados: los títulos de ADR-0001 y ADR-0002 se reescribieron sin declarar reemplazo.
- Acreditar el Quality Gate público de SonarCloud para el hash calificado (token `SONAR_TOKEN` marcado como pendiente; el run de CI ya quedó citado).

## Recuento y nota sugerida

**9 de 10 criterios graduables Cumple** (la matriz de la ficha tiene 12 filas; las 2 filas de despliegue quedan pendientes de calificar en esta pasada; de las 10 graduables, 1 queda No cumple).

**Propuesta provisional al docente — `nota = 1 + 4 × (9/10) = 4.6`**; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL del sistema desde fuera de la red: No verificado por decisión docente; el repositorio la declara en `README.md:13-14`. No se abrió ninguna URL.
- Health check: No verificado por decisión docente; la ruta existe en `backend/app/main.py:81-88` y `backend/app/salud.py`. No se consultó.
- SonarCloud: job condicionado a `SONAR_TOKEN`, marcado como pendiente en `infra/README.md`; sin URL del Quality Gate para el hash calificado.

## Hallazgos para la planilla

- La entrega S8 está bien documentada: Terraform para sitio/DB/rama, evidencia de despliegue con logs JSON, `/metricas` ligada a ESC-02, costos con supuestos y punto de ruptura, arc42 §7 y ADR-0004 de plataforma.
- La API queda fuera de Terraform por límite del proveedor en plan gratuito; la excepción está declarada, no oculta.
- arc42 §2 no recoge la restricción de tarjeta: la frase vive en `docs/comparacion-despliegue.md` y ADR-0004.
- `docs/ia.md` no tenía entrada de S8 en el estado calificado; la de S8 se subió el 2026-09-28, después del cierre.
- ADR-0001 y ADR-0002 fueron editados (título reescrito) después de aceptarse sin declarar reemplazo.
- Pipeline del hash calificado en verde: `CI` #43 (`success`) sobre `a94bf4e`, con URL citada; la fila pasa de No verificado a Cumple.
