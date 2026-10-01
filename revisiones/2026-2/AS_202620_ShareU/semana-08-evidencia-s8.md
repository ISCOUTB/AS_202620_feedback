# Semana 8 · Despliegue reproducible, CI y observabilidad · ShareU

> Revisión definitiva: hash `332f67f726969e0c73b98dd4705aea6c37e5603b`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `332f67f` en `origin/master` (2026-09-27T23:57:16-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |
| Revisión preliminar sustituida | `532fcf6` (2026-09-21T12:26:41-05:00) |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | El README (§«Sistema desplegado») declara la tabla Frontend/Backend con marcadores `<URL Vercel>` y `<URL Render>`; `docs/arc42/arc42.md` §7.1 nombra `https://shareu-backend.onrender.com` y `https://shareu-frontend.vercel.app`. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El README (hash `332f67f`) no fija una URL real; §7.1 sí nombra los hosts. |
| Health check consultable | La ruta existe en código: `app/main.py:84-86` (`@app.get("/health")` → `{"estado": "ok"}`); el §7.3 la declara usada por Docker y Render. | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. La ruta `/health` está versionada en `app/main.py:84`. |
| Infraestructura como código versionada en el repositorio | El árbol de `332f67f` no contiene Dockerfile, `docker-compose`, `.tf/.tfvars`, `k8s/`, `helm/`, `fly.toml`, `render.yaml`, railway ni `Procfile`; solo `.github/workflows/tests.yml`. | No cumple | El README y `arc42 §7.2` citan `Dockerfile` y un Blueprint `render.yaml`, pero ninguno existe en el repositorio. `git ls-tree -r 332f67f` no lista archivos de infraestructura. |
| El entorno se puede recrear siguiendo el README | `README.md` §«Instalación»/§«Ejecución»: venv, `pip install -r requirements.txt`, `uvicorn app.main:app --reload`; §«Ejecución del frontend»: `npm install` y `npm run dev`, con `NEXT_PUBLIC_API_URL`. | Cumple | Procedimiento único y requisitos previos declarados; el documento cubre backend y frontend. La vía Docker que anuncia (`docker compose up --build`) no es reproducible porque no hay `docker-compose`, pero se declara como opcional. |
| Pipeline en verde sobre la rama principal | Último run sobre `master` para el hash revisado: run `36379843854` (`.github/workflows/tests.yml`, 2026-09-28T04:57:27Z) con conclusión **failure**: https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36379843854 | No cumple | El único workflow que corre sobre `master` en el estado calificado falla. Los runs verdes (p. ej. `35632045274`) son anteriores (`532fcf6`, 2026-09-21) y no corresponden al hash elegible. |
| Logs estructurados | `app/main.py:24` (`class _JsonFormatter`), `app/main.py:49` (`_configurar_logging`) y middleware `app/main.py:76` emiten una línea JSON por solicitud con `request_id`, `method`, `path`, `status_code`, `duration_ms`. | Cumple | Configuración de logging con formato JSON y campos con nombre; el §7.3 cita la misma ruta. |
| Métrica consultable asociada a un escenario de calidad | `app/administracion/metricas.py`: `obtener_metricas()` expone `total_busquedas` y `tasa_busquedas_sin_resultados` declarando el escenario «usabilidad — búsqueda combinada en ≤3 interacciones»; publicada en `app/administracion/router.py` (`GET /administracion/metricas`). | Cumple | Métrica con escenario explícito, consultable por HTTP; ligada a `docs/aspectos/aspectos.md`. |
| Secretos fuera del código y tomados del entorno o del almacén | `app/frontend/.env.example` declara `NEXT_PUBLIC_API_URL`; `.github/workflows/tests.yml:25-26` toma `secrets.GITHUB_TOKEN` y `secrets.SONAR_TOKEN`; `app/main.py:63` lee `os.getenv(...)`; el barrido §9 y `git log -S` no encuentran credenciales ni `.env` versionado. | Cumple | Variables de entorno separadas del código y secretos tomados de GitHub/Render/Vercel. El `.env.example` de backend que el README menciona no existe; solo está el del frontend. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | `docs/costos/estimacion-costo.md`: supuesto de volumen (5–10 usuarios, ~50 búsquedas, <5 h/mes con tráfico), costo por pieza, total US$0/mes y punto de ruptura (la persistencia exige un Postgres gestionado; 750 h de Render). | Cumple | Documento con volumen supuesto, desglose por pieza y umbral de ruptura; no es el catálogo del proveedor. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/arc42.md` §7.1: tabla con Backend (Render Free, contenedor), Frontend (Vercel Hobby), Base de datos (SQLite en el contenedor) y CI/CD (GitHub Actions), cada uno con su ubicación. | Cumple | Una caja por pieza con el lugar de ejecución declarado. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/arc42.md` §2: «**Restricción de costo:** el despliegue debe mantenerse en **USD 0/mes** y **sin tarjeta de crédito** en ningún proveedor», con enlace a la estimación. | Cumple | Ambas restricciones recogidas juntas como restricción arquitectónica. |
| Un ADR por decisión de plataforma, con alternativa descartada | `docs/adr/` contiene `0001`–`0004`, todos de arquitectura; el README y §7.2 citan ADR 0005, 0006 y 0007 de plataforma que **no existen** en el árbol. | No cumple | No hay ningún ADR de despliegue versionado; los archivos referenciados (`0005-migracion-frontend-nextjs.md`, `0006-plataforma-backend-despliegue.md`, `0007-plataforma-frontend-despliegue.md`) están ausentes. La propia `docs/ia/ia.md` (entrada 8) los da por redactados. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clonado sin autenticación desde `https://github.com/ISCOUTB/AS_202620_ShareU.git`. | Cumple | Organización `ISCOUTB`, nombre `AS_202620_ShareU`, visible sin credenciales. |
| Estructura mínima presente | `README.md`, `docs/arc42/arc42.md`, `docs/adr/`, `docs/c4/` presentes; `docs/aspectos/aspectos.md` y `docs/ia/ia.md` están en rutas distintas de las contractuales. | No cumple | `docs/aspectos.md` y `docs/ia.md` no existen en la ruta mínima; los artefactos sí están, en subcarpetas propias (desviación, no ausencia). |
| Estado calificado identificable | `origin/master`, `332f67f`, 2026-09-27T23:57:16-05:00, anterior al cierre. | Cumple | Rama principal única, hash y fecha consignados. |
| Nombres de ADR según la convención | `docs/adr/` contiene `ShareU_Trazabilida.pdf`, que no cumple `NNNN-kebab-case.md`. | No cumple | El PDF ajeno a la convención reaparece en el estado calificado (`698d1ae`, 2026-09-20). |
| ADR aceptados no reescritos | `git log --follow`: `0001` solo registra movimientos de carpeta (`8148453`, `37beb7a`, 0 inserciones/0 borrados); `0002`, `0003` y `0004` se crean en un único commit cada uno. | Cumple | Ninguna decisión aceptada se reescribe; `0001` conserva su contenido. |
| `docs/ia.md` al día para la semana | `docs/ia/ia.md` crece dentro del periodo (`b7737be` 2026-09-13, `332f67f` 2026-09-27) y registra la entrada 8 con lo aceptado y lo rechazado con motivo. | Cumple | El archivo está en la ruta desviada `docs/ia/ia.md`; se evalúa donde está. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `sonar-project.properties` y el paso `SonarSource/sonarcloud-github-action@v3` existen, pero el run del hash revisado (`36379843854`) termina en **failure**; solo hay un badge en el README. | No cumple | Falta el run exitoso que ejecute el scanner para el hash revisado y la URL pública del análisis con su Quality Gate; la única evidencia es el badge. |
| Sin credenciales en el repositorio ni en el historial | `git grep` §9 y `git log -S'BEGIN PRIVATE KEY'` sin coincidencias; sin `.env` versionado. | Cumple | El repositorio no expone credenciales. |
| Contribución de todos los integrantes | `shortlog -sne 332f67f` consolidado por identidad: cuatro grupos, uno por integrante, incluido el que antes no aparecía. | Cumple | Los cuatro integrantes declarados en `EQUIPOS.md` aparecen; Luis Carlos Corredor, antes ausente, ahora contribuye con su cuenta. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Se mira el repositorio entero en la punta actual de `origin/master`, no solo el estado del cierre.

- **Punta actual**: `3950860` (2026-09-28T19:56:57-05:00, «semana 9»).
- **Commits posteriores al cierre**: `3950860` (semana 9, evidencia S9), `c552056` (`Update layout.tsx`), `0e14454` y `21256e5` (`Update tests.yml`).
- **Veredicto**: con pendientes.

La punta actual avanza hacia S9 (métrica tras interfaz, ADR 0008/0009, capa de servicios), pero no cierra lo que S8 dejó abierto: ni `Dockerfile`, ni `render.yaml`, ni los ADR 0005–0007 aparecen en el árbol de la punta (el README y §7 siguen apuntando a archivos inexistentes). Tampoco hay una URL real en el README. El workflow de `master` sigue fallando en los runs posteriores al cierre (`36505758458`, `36480560316`, `36479877131`). La documentación de despliegue describe un entorno que el repositorio no contiene.

## Recuento y nota sugerida

**7 de 10 criterios graduables.**

**Propuesta provisional al docente — `nota = 1 + 4 × (7/10) = 3.8`; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.**

No se aplica la fórmula sobre las 12 filas: las dos primeras («URL del sistema accesible desde fuera de la red de la universidad» y «Health check consultable») quedan diferidas por decisión docente.

## No verificado / pendientes

- Deferidas por decisión docente (no se abrieron ni probaron URLs): «URL del sistema accesible desde fuera de la red de la universidad» y «Health check consultable»; ambas dependen de la URL que se entrega por Moodle.
- Los ADR de plataforma 0005, 0006 y 0007 referenciados por el README y `arc42 §7.2` no están en el repositorio; no se pueden evaluar.

## Hallazgos para la planilla

- El informe preliminar evaluó `532fcf6`; el estado definitivo es `332f67f`, que reescribe README, arc42 §2 y §7, agrega logs JSON, `GET /administracion/metricas`, `docs/costos/estimacion-costo.md` y `sonar-project.properties`.
- IaC ausente: el README y arc42 §7 describen Dockerfile, `render.yaml` y ADR 0005–0007 que no existen en el árbol (tampoco en la punta actual).
- El pipeline de `master` en el hash calificado está en rojo (run `36379843854`, failure).
- La ruta contractual `docs/aspectos.md` / `docs/ia.md` sigue sin usarse (`docs/aspectos/` y `docs/ia/`).
- Un PDF fuera de la convención (`docs/adr/ShareU_Trazabilida.pdf`) reaparece en `docs/adr/`.
- SonarCloud no es auditable: scanner presente pero sin run exitoso ni Quality Gate público.
- Contribución resuelta: los cuatro integrantes aparecen en el historial consolidado.
- Sin credenciales en HEAD ni en el historial.
