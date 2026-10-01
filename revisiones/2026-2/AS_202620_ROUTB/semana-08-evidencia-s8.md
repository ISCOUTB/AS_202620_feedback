# semana-08-evidencia-s8 · ROUTB

> Revisión definitiva: hash eae667e, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `eae667e` en `origin/master` (2026-09-27T21:58:06-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

El estado cambió respecto de la pasada temprana: el commit calificado pasó de `35d088c`
(2026-09-23) a `eae667e` (2026-09-27). La punta de `origin/master` coincide con el hash revisado:
no hay commits posteriores al cierre. La nueva entrega incorpora la métrica ligada a un escenario
(`docs/evidencia/metricas-escenario-calidad.md`), separa las decisiones de plataforma en ADR 0005
(Render) y 0006 (Supabase), actualiza arc42 §7 con una caja por plataforma y publica URL y health
check en el README. Las dos filas de despliegue quedan diferidas por decisión docente.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | `README.md:105` declara `https://as-202620-routb.onrender.com` como URL base. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. No se abrió ni se consultó ninguna URL. |
| Health check consultable | La ruta existe en el código: `backend/app/main.py:61` `@app.get("/health")`; `render.yaml:9` la usa como `healthCheckPath: /health`. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. La ruta está declarada, pero no se consultó por estar diferida la URL. |
| Infraestructura como código versionada en el repositorio | `render.yaml:1` (Blueprint con `runtime: docker`, `:7` `plan: free`), `backend/Dockerfile` y `docker-compose.yml`; `.github/workflows/ci.yml` construye la imagen en el job `build`. | Cumple | Describe el entorno, no pasos manuales. |
| El entorno se puede recrear siguiendo el README | `README.md:99` «Despliegue en la nube», `:126` «Pasos para recrear el entorno desde cero» (Supabase, migraciones, Render, variables y verificación). | Cumple | Procedimiento documentado con requisitos y artefactos versionados. |
| Pipeline en verde sobre la rama principal | Run `CI ROUTB` de `eae667e` en `master`, conclusión `success`: https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/36371840003 (2026-09-28T02:58:09Z). | Cumple | Único workflow sobre `master`; todos sus runs en el periodo concluyen `success`, incluido el del hash revisado. |
| Logs estructurados | `backend/app/main.py:30` `structured_logging_middleware` escribe un objeto JSON por petición con `timestamp`, `method`, `path`, `status_code`, `duration_ms` y `client_ip` (`:33-43`). | Cumple | Configuración versionada; `:43` `logger.info(json.dumps(log_entry))`. |
| Métrica consultable asociada a un escenario de calidad | `docs/evidencia/metricas-escenario-calidad.md:7` «Escenario de calidad asociado» (Rendimiento, `GET /trips/`, p95 < 3,99 s); `:161` umbral con medición p95 y su fuente. | Cumple | Nombra la métrica, el escenario y el umbral; ligada a arc42 §10.2. |
| Secretos fuera del código y tomados del entorno o del almacén | `render.yaml:12,14` `sync: false` para `DATABASE_URL` y `JWT_SECRET_KEY`; `backend/.env.example` versionado con placeholders; `docker-compose.yml` toma literales por `${...}`. Sin `.env` versionado. | Cumple | Los valores reales viven en el panel de Render; sin credenciales en el repositorio. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/evidencia/costo_mensual.md:3` «Supuestos de volumen y carga», `:36` «Análisis de punto de ruptura de la capa gratuita» con umbral de Render (750 h, RAM) y Supabase (500 MB). | Cumple | Volumen supuesto (500 usuarios, 150.000 req/mes), costo por pieza y punto de ruptura. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07_vista_de_despliegue.md:19-24` cajas Render y Supabase con «Dónde funciona»; `:51` tabla pieza → plataforma → decisión. | Cumple | Representa las plataformas reales (Render, Supabase), no servidores genéricos. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02_restricciones_de_arquitectura.md:65-66`: costo recurrente $0.00 USD y sin asociación de tarjetas de crédito. | Cumple | Ambas restricciones como restricciones comerciales y de alcance. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/0005-render-plataforma-de-despliegue.md` (Render; descarta Railway, Fly.io y nubes mayores; capa gratuita verificada) y `docs/adr/0006-base-de-datos-supabase.md` (Supabase; descarta Firestore/MongoDB, Render PostgreSQL y VPS; capa gratuita verificada). | Cumple | Una decisión por plataforma, cada una con alternativa descartada y free tier verificado. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_ROUTB`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre `AS_202620_ROUTB` conforme y visibilidad pública. |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/` (0001-0006), `docs/c4/context.md`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Las seis rutas del contrato §2. |
| Estado calificado identificable | `eae667ef4339d3e8e89461b1e5f865a08eb21d10` en `origin/master`, último commit ≤ cierre: `2026-09-27T21:58:06-05:00 Semana 8 - ROUTB`. | Cumple | Coincide con el estado revisado; sin commits posteriores al cierre. |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md` … `docs/adr/0006-base-de-datos-supabase.md`. | Cumple | Todos cumplen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | Los seis declaran `## Estado` «Aceptado». `git log --follow`: ADR-0001 creado `1ed002b` (2026-08-23) y editado `a94a1a3` (2026-08-30); ADR-0002 creado `e9d337c` (2026-09-05) y editado `53ed7c3` (2026-09-19); ADR-0003 creado `e9d337c` y editado `f706aa6` (2026-09-06); ADR-0005 creado `35d088c` (2026-09-23) y editado `b0426fa` (2026-09-25); ADR-0006 creado `78200a6` (2026-09-24) y editado `b0426fa` (2026-09-25). ADR-0004 tiene un único commit (`53ed7c3`). Ninguna edición declara un ADR de reemplazo. | No cumple | CONTRATO §4 prohíbe editar un ADR aceptado sin declarar reemplazo. Las ediciones son posteriores a la aceptación y no hay ADR sucesor. |
| `docs/ia.md` al día para la semana | `docs/ia.md` incluye la sección «Semana 8» (fecha 2026-09-24) con herramienta, contexto, qué se aceptó y qué se rechazó y por qué. | Cumple | El registro crece dentro del periodo y documenta los rechazos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `.github/workflows/ci.yml` corre en verde (run 36371840003), y existe `sonar-project.properties`, pero el workflow no invoca el scanner y no hay URL pública del análisis ni estado de Quality Gate. | No cumple | Falta la evidencia de SonarCloud exigida por el contrato §8; el enlace genérico del README a SonarCloud no la acredita. |
| Sin credenciales en el repositorio ni en el historial | Barrido con coincidencias solo en identificadores y datos de prueba (`token`, `password`); sin `.env` versionado; `backend/.env.example` con placeholders; sin claves privadas en el historial. | Cumple | Sin credenciales reales. |
| Contribución de todos los integrantes | `git shortlog -sne eae667e`: `MKeinerrr` 53 más 2 con un segundo correo institucional (consolidado), `diegobrr999-commits` 6, `juliandmanjarrez-tech` 3, `junior14700` 2. | Cumple | Cuatro identidades para cuatro integrantes; aporte concentrado en un integrante, ya señalado en planilla. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `eae667ef4339d3e8e89461b1e5f865a08eb21d10 2026-09-27T21:58:06-05:00 Semana 8 - ROUTB`.
- **Veredicto:** sin pendientes en la matriz graduable; quedan 2 filas de despliegue diferidas.
- **Resumen:** la punta actual coincide con el estado calificado (no hay commits posteriores al cierre). La entrega S8 cubre las diez filas graduables: infraestructura como código (`render.yaml`, `backend/Dockerfile`, `docker-compose.yml`), procedimiento de recreación en el README, CI en verde sobre `master`, logs estructurados en JSON, métrica ligada al escenario de rendimiento, secretos por configuración del proveedor, estimación de costo con punto de ruptura, arc42 §7 con Render/Supabase, restricciones de costo y tarjeta en §2 y un ADR por plataforma (0005 Render, 0006 Supabase). Siguen abiertos la evidencia pública de SonarCloud y las ediciones de ADR aceptados.

Pendientes que siguen abiertos:
- URL del despliegue y su comprobación externa (fila diferida por decisión docente).
- Health check con código de respuesta (fila diferida por decisión docente).
- SonarCloud sin invocación en el workflow ni URL pública del Quality Gate (pendiente desde S6).
- ADR 0001, 0002, 0003, 0005 y 0006 editados después de aceptarse sin declarar reemplazo.

## Recuento y nota sugerida

10 de 10 criterios graduables Cumple.

**Propuesta provisional al docente: 5.0 = 1 + 4 × (10/10).** Quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL del sistema accesible desde fuera de la red universitaria: fila diferida; no se abrió ninguna URL. El README declara `https://as-202620-routb.onrender.com`.
- Health check consultable: fila diferida; la ruta `/health` existe en `backend/app/main.py:61` y `render.yaml:9`, pero no se consultó por estar diferida la URL.
- SonarCloud: sin invocación del scanner en el workflow ni URL pública del Quality Gate, por lo que la fila transversal queda en No cumple.
- ADR aceptados editados: 0001 (`a94a1a3`), 0002 (`53ed7c3`), 0003 (`f706aa6`), 0005 y 0006 (`b0426fa`) sin reemplazo declarado.

## Hallazgos para la planilla

- Infraestructura como código versionada en `render.yaml`, `backend/Dockerfile` y `docker-compose.yml`; CI construye la imagen.
- Último run de CI sobre `master` en el hash revisado en verde: run 36371840003.
- Logs estructurados en JSON (`backend/app/main.py:30-43`) y métrica de latencia ligada al escenario de rendimiento (`docs/evidencia/metricas-escenario-calidad.md:7-12`).
- Secretos por `sync: false` en `render.yaml` y `.env.example`; Compose sin literales tras la corrección.
- Costo mensual con supuestos y punto de ruptura; arc42 §7 con Render/Supabase y §2 con costo $0 y sin tarjeta.
- ADR 0005 y 0006 separan las decisiones de plataforma con alternativas desestimadas y capa gratuita verificada.
- SonarCloud sigue ausente: fila transversal en No cumple.
- ADR aceptados editados sin reemplazo declarado: fila transversal en No cumple.
- El commit calificado `eae667e` es anterior al cierre y no hay commits posteriores.
