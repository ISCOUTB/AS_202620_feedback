# semana-08-evidencia-s8 · TAIA

> Revisión definitiva: hash 4b0724247c6a58f82bc6091f78ab8872d58456de, última revisión ≤ cierre (2026-09-28T05:00:00Z) en origin/main.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `4b07242` en `origin/main` (2026-09-27T23:03:53-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | README.md:9 declara `http://157.137.215.57:8000`; docs/arc42/07-vista-de-despliegue.md:7 repite la URL pública. No se abrió. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio sí prueba la declaración de una URL pública y su procedimiento de comprobación (README.md:15, :20). |
| Health check consultable | Ruta declarada y presente en código: `@app.get("/health")` en backend/app/main.py:48; documentada en README.md:10 y docs/arc42/07-vista-de-despliegue.md:8. No se consultó. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio prueba que la ruta existe (`backend/app/main.py:48`) y el workflow de CD la verifica (`.github/workflows/cd.yml`, paso «Verificar health check externo»). |
| Infraestructura como código versionada en el repositorio | `backend/Dockerfile` (CMD alembic + uvicorn); `terraform/main.tf`, `terraform/provider.tf`, `terraform/variables.tf`, `terraform/outputs.tf`; `.github/workflows/cd.yml` (build+push+deploy). Hash `4b07242`. | Cumple | IaC real: imagen Docker, adopción de la VM por Terraform y CD que publica en GHCR y despliega por SSH. |
| El entorno se puede recrear siguiendo el README | README.md:99-124 «Ejecución local» (`pip install -r backend/requirements-dev.txt`, `.\run.bat`) y README.md:127-169 «Despliegue» paso a paso (Supabase, VM OCI, secretos, push a main, rollback). | Cumple | El README documenta recreación local y despliegue; el rollback por etiqueta GHCR también está descrito. |
| Pipeline en verde sobre la rama principal | Run CI `main` `4b0724247c6a` success (2026-09-28T04:04:03Z) https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/36376147005 y run CD `main` success (2026-09-28T04:04:39Z) https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/36376186792. | Cumple | Los dos workflows que corren sobre `main` (ci.yml y cd.yml) están en verde para el hash calificado. El fallo de CD observado es de la rama `migrate_to_render`, no de `main`. |
| Logs estructurados | Configuración: `JsonFormatter(logging.Formatter)` en backend/app/shared/adapters/inbound/observability.py:33 y `configure_logging()` :47. Línea de ejemplo JSON en README.md:175. | Cumple | Emite una línea JSON por petición con `timestamp`, `level`, `event`, `method`, `route`, `status`, `duration_ms`, `user_id`; documentado en arc42 §7.4. |
| Métrica consultable asociada a un escenario de calidad | `GET /metrics` en backend/app/shared/adapters/inbound/observability.py:135; métrica `http_request_duration_p95_ms` :91 con objetivo por ruta (`AGENT_TARGET_MS=7000` para S3, CRUD<500 ms para RNF-08) :28. README.md:171-179 la liga a S3/RNF-08. | Cumple | Métrica con nombre, ventana y escenario de calidad asociado (S3 y RNF-08), no una métrica de sistema suelta. |
| Secretos fuera del código y tomados del entorno o del almacén | Lecturas desde entorno: gemini_llm.py:95 (`GEMINI_API_KEY`), telegram_bot_client.py:12 (`TAIA_TELEGRAM_BOT_TOKEN`), jwt_token_service.py:23 (`TAIA_JWT_SECRET`). `.github/workflows/cd.yml` toma `secrets.DATABASE_URL`, `secrets.TAIA_JWT_SECRET`, `secrets.GHCR_PAT`, `secrets.OCI_*` y escribe `~/taia.env` en la VM. Sin `.env` versionado. | Cumple | El repositorio no contiene credenciales y el despliegue las toma de los secretos de GitHub. Defecto: `.env.example` **no existe** pese a que README.md:105 y arc42 §7.3 lo citan, porque `.gitignore` incluye `.env.example`; el enlace del README está roto. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | docs/costo_mensual.md §1-3 (volumen supuesto: 100 estudiantes, 150 000 req/mes; costo por pieza; punto de ruptura por capa). README.md:181-183 resume 39,42 USD/mes. | Cumple | Parte del volumen del escenario (no del catálogo), cuesta pieza por pieza y declara dónde se rompe cada capa gratuita (Supabase 500 MB, cuota diaria de Gemini). |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | docs/arc42/07-vista-de-despliegue.md:13 «Infraestructura: una caja por pieza», diagrama y tabla :50 con «Pieza / Dónde se ejecuta / Qué hace / Definida en». | Cumple | Una caja por pieza (GitHub Actions, GHCR, VM OCI, Render, Supabase, Gemini, Telegram, Terraform) con su ubicación de ejecución. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | docs/arc42/02-restricciones-de-arquitectura.md:14 «Límite de costo: 0 USD al mes… la VM cuesta 39,42 USD/mes»; :15 «Tarjeta: Oracle Cloud exige registrar una tarjeta…». | Cumple | Ambas restricciones están recogidas como restricciones técnicas con su implicación arquitectónica. |
| Un ADR por decisión de plataforma, con alternativa descartada | docs/adr/0003-plataforma-despliegue-api.md (OCI vs Render Free, capa gratuita verificada) y docs/adr/0004-plataforma-base-de-datos.md (Supabase vs Postgres en VM vs Render Postgres, capa gratuita verificada), ambos del commit e2b9dfd. | Cumple | Una decisión de plataforma por pieza (API y base de datos), cada una con alternativas descartadas y capa gratuita verificada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant`; clon anónimo OK en `4b07242`. | Cumple | Nombre con la convención y visibilidad pública verificada por clon sin autenticación. |
| Estructura mínima presente | `README.md`, `docs/arc42/` (secciones 01-12 + arc42.md), `docs/adr/` (0001-0004), `docs/c4/` (C1-C3), `docs/aspectos.md`, `docs/ia.md` en `4b07242`. | Cumple | Las seis rutas de CONTRATO §2 están versionadas. |
| Estado calificado identificable | `origin/main` `4b07242` (2026-09-27T23:03:53-05:00) ≤ cierre 2026-09-28T05:00:00Z. | Cumple | Rama principal y hash anterior al cierre registrados. |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico.md`, `0002-estrategia-integracion-api-sincrona.md`, `0003-plataforma-despliegue-api.md`, `0004-plataforma-base-de-datos.md`. | Cumple | Los cuatro siguen `NNNN-titulo-en-kebab-case.md`; sin residuos en el filtro de §4. |
| ADR aceptados no reescritos | `git log --follow` de `docs/adr/0001-estilo-arquitectonico.md`: `decaa36` (creación, 2026-08-22), `4dd3925` (2026-08-29) y `42c5b03` (2026-09-06, «add traceability section»); sin ADR sucesor ni reemplazo declarado. | No cumple | Se editó un ADR aceptado tras su aceptación; ya venía registrado desde S5. ADR-0002 solo tiene su commit de creación (`2837b47`). |
| `docs/ia.md` al día para la semana | Último commit sobre `docs/ia.md` = `7b32b3f` (2026-09-16); no hay commits en la ventana S8 (posterior a 2026-09-21T05:00:00Z). | No cumple | El archivo no creció dentro del periodo de S8, aunque históricamente documenta lo rechazado con su motivo. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | CI y CD en verde sobre `main` (runs 36376147005 y 36376186792), pero no existe `sonar-project.properties`, ni step del scanner en `.github/workflows/`, ni URL pública de análisis con Quality Gate. | No cumple | Faltan la segunda y la tercera evidencia que exige CONTRATO §8; no hay análisis estático auditable. |
| Sin credenciales en el repositorio ni en el historial | `git grep` §9 sobre `4b07242`: solo nombres de parámetros/campos; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` coincide solo con `correcciones.md` (texto del propio comando de barrido), no con una clave. | Cumple | Sin secretos reales. La coincidencia del pickaxe es la regex documentada, no una credencial. |
| Contribución de todos los integrantes | `git shortlog -sne 4b07242` consolidado: val (35+2+5 = 42, dos correos + cuenta de GitHub), dei0811 (31), Luis Mendoza/luis20072002 (24+4 = 28, un solo correo), mark (3). | Cumple | Los cuatro integrantes declarados en EQUIPOS.md tienen commits; distribución desigual pero completa. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subió tarde o corrigió entregas anteriores, aquí se nota.

- **Punta actual revisada**: `4b0724247c6a58f82bc6091f78ab8872d58456de 2026-09-27T23:03:53-05:00 docs: complete deployment workshop data`
- **Veredicto**: al día
- Resumen: la punta de `origin/main` coincide con el hash calificado: no hay commits posteriores al cierre en `main`. El salto respecto a la preliminar es sustancial: con `e2b9dfd` (2026-09-27) el equipo versionó IaC (Dockerfile + Terraform), un pipeline CI/CD que construye la imagen y la despliega por SSH, logs JSON y `/metrics` ligados a S3/RNF-08, estimación de costo y ADR de plataforma 0003/0004. El trabajo posterior al cierre (rama `migrate_to_render`, runs del 2026-09-28T17:xxZ) no forma parte del estado calificado.

Pendientes que siguen abiertos:
- Publicar/entregar la URL por Moodle para calificar las dos filas de despliegue (no se probó ninguna URL).
- Versionar un `.env.example` (hoy `.gitignore` lo excluye) y corregir el enlace roto de README.md:105 y arc42 §7.3.
- No reescribir el ADR-0001 aceptado (o declarar uno sucesor).
- Registrar el uso de IA del periodo S8 en `docs/ia.md`.
- Añadir SonarCloud (configuración, run del scanner y URL pública con Quality Gate).

## Recuento y nota sugerida

**10 de 10 criterios graduables Cumple** (dos filas de despliegue quedan diferidas).

**Propuesta provisional al docente — `nota = 1 + 4 × (10/10) = 5.0`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

## No verificado / pendientes

- «URL del sistema accesible desde fuera de la red de la universidad»: diferida por decisión docente; la URL se entrega por Moodle y no está disponible. El repositorio declara `http://157.137.215.57:8000` (README.md:9) y cómo comprobarla (README.md:20), pero no se abrió.
- «Health check consultable»: diferida por la misma razón. La ruta existe en código (`backend/app/main.py:48`) y el CD la prueba, pero no se consultó su código de respuesta ni se registró hora.

## Hallazgos para la planilla

- Entrega muy completa en S8: IaC (Dockerfile + Terraform), CI/CD en verde sobre `main`, logs estructurados, `/metrics` con escenario, costo con supuestos y ADR 0003/0004 de plataforma.
- Las dos filas de despliegue quedan diferidas (URL por Moodle); no se abrió ninguna URL.
- `.env.example` no existe porque `.gitignore` lo excluye, pese a que README.md:105 y arc42 §7.3 lo citan; enlace roto.
- Transversal: el ADR-0001 aceptado se reescribió (`4dd3925` 2026-08-29 y `42c5b03` 2026-09-06) sin ADR sucesor.
- `docs/ia.md` no creció en la ventana S8 (último commit 2026-09-16).
- Sin SonarCloud: ni configuración, ni run del scanner, ni Quality Gate público.
