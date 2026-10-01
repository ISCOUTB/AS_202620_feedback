# semana-08-evidencia-s8 · Clubs UTB

> Revisión definitiva: hash `652f78b`, última revisión ≤ cierre (2026-09-28T05:00:00Z) en `origin/master`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `652f78b7` en `origin/master` (2026-09-27T23:39:11-05:00) |
| Cierre | 2026-09-28T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| URL del sistema accesible desde fuera de la red de la universidad | código de respuesta y tiempo, con la hora de la comprobación | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. El repositorio no declara URL pública: `README.md:140` solo cita `http://localhost:8000/health` y `docs/arc42/07_vista_de_despliegue.md:9-17` nombra Azure Container Apps y Supabase como entorno, sin URL. No se abre ninguna URL en esta pasada. |
| Health check consultable | ruta y código de respuesta | No verificado | Pendiente de calificar: la URL del despliegue se entrega por Moodle y no está disponible en esta pasada. Ruta de health en el código: `backend/src/linkclub/adapters/inbound/api/health_router.py:10` (`@router.get("/health")`); `README.md:140` la cita solo contra `localhost`. No se consulta en esta pasada. |
| Infraestructura como código versionada en el repositorio | rutas de los archivos de infraestructura | Cumple | `backend/Dockerfile:1` (imagen FastAPI no-root) e `infra/terraform/provider.tf:1`, `infra/terraform/resource.tf:1`, `infra/terraform/settings.tf:1` más `infra/terraform/.terraform.lock.hcl`, que describen el proyecto Supabase como código. |
| El entorno se puede recrear siguiendo el README | sección del README con el procedimiento | No cumple | `README.md:121-150` (§7) solo documenta el arranque local del backend (`venv`, `pip install`, `uvicorn`) y del frontend (`flutter run`); no menciona `backend/Dockerfile` ni `infra/terraform/`, así que el entorno desplegado no se puede recrear siguiendo el README. |
| Pipeline en verde sobre la rama principal | URL del último run y su conclusión | No cumple | En el último push a `origin/master` (runs del 2026-09-28T04:39Z) ambos workflows concluyeron `failure`: `backend-tests.yml` (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/36378631444) y `contrato.yml` (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/36378632136). |
| Logs estructurados | archivo de configuración y ejemplo de línea | No cumple | El grep de configuración de logging (`structlog|winston|pino|logback|serilog|logging.config|json.*formatter|import logging|getLogger|basicConfig`) sobre `backend/` no devuelve coincidencias, y `backend/src/linkclub/main.py:1-18` no configura registro ni emite campos estructurados. |
| Métrica consultable asociada a un escenario de calidad | nombre de la métrica y escenario al que corresponde | No cumple | `backend/requirements.txt:8` declara `prometheus-fastapi-instrumentator==6.1.0`, pero no se usa en el código: no hay instrumentación, ni ruta `/metrics`, ni nombre de métrica, ni escenario asociado. |
| Secretos fuera del código y tomados del entorno o del almacén | `.env.example`, referencias a secretos en el workflow | Cumple | `backend/.env.example:1-5` declara `SUPABASE_URL` y `SUPABASE_KEY` como marcadores; no hay ningún `.env` versionado; el barrido no encontró credenciales reales (solo `infra/terraform/resource.tf:14` `database_password = "placeholder"`) y el token de Terraform se toma de un archivo local `access-token` que está en `.gitignore:6`. |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita | documento con volumen supuesto y cálculo | Cumple | `docs/arc42/07_vista_de_despliegue.md:42-43` parte de un volumen propio (2.000 MAU, 160.000 consultas SQL/mes, ~50 MB) y fija el punto de ruptura de la capa gratuita en 500 MB / 50.000 MAU; superarlo cuesta $25/mes (Plan Pro). No es solo el catálogo del proveedor. |
| arc42 sección 7 con una caja por pieza y dónde se ejecuta | `docs/arc42/07*` | Cumple | `docs/arc42/07_vista_de_despliegue.md:9-17` tiene una tabla con una fila por pieza (app móvil, API, BD/Auth, pipeline) y su «Entorno de Despliegue»; `:20-38` añade el diagrama de despliegue por piezas. |
| Límite de costo y restricción de tarjeta recogidos en la sección 2 | `docs/arc42/02*` | Cumple | `docs/arc42/02_restricciones.md:33-34` recoge F1 «Costo Cero Mensual» y F2 «Sin tarjeta de crédito obligatoria» como restricciones financieras justificadas. |
| Un ADR por decisión de plataforma, con alternativa descartada | archivos de `docs/adr/` de esta semana | No cumple | Solo existe `docs/adr/0004-despliegue-base-de-datos.md:1-58`, que decide la BD (Supabase) con alternativa B descartada, pero está en estado «Propuesto»; la plataforma de la API que declara `docs/arc42/07_vista_de_despliegue.md:11` (Azure Container Apps) no tiene ADR. Falta un ADR por decisión de plataforma. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB`, clon anónimo con `--filter=blob:none` exitoso; rama `origin/master`. | Cumple | El repositorio responde sin autenticación y su nombre sigue `AS_202620_<PROYECTO>`. |
| Estructura mínima presente | El árbol contiene `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del apartado 2 existen. |
| Estado calificado identificable | `652f78b7` en `origin/master`, `2026-09-27T23:39:11-05:00`, anterior al cierre 2026-09-28T05:00:00Z. | Cumple | No hay commits posteriores al cierre: la punta actual coincide con el hash calificado. |
| Nombres de ADR según la convención | `docs/adr/0003- integacion rest openapi.md` (espacio inicial, no kebab-case) y `docs/adr/0003-API.md` junto a `0003` duplicado; `0004-despliegue-base-de-datos.md` sí cumple. | No cumple | Dos archivos rompen la convención `NNNN-titulo-kebab-case.md` y duplican el número 0003. |
| ADR aceptados no reescritos | ADR-0001 aceptado en `2c316f4` (2026-08-23) y editado en `c6c46e3` (2026-08-30, «correción de feedback»); ADR-0002 editado en `e0eaca4` (2026-09-20) tras `743cc1f` (2026-09-13). | No cumple | Las ediciones son posteriores a la aceptación y no declaran un ADR de reemplazo (contrato §4). |
| `docs/ia.md` al día para la semana | Último commit sobre `docs/ia.md`: `78579b6` (2026-09-27), dentro del periodo de S8, con la fila S8 y su columna de motivo. | Cumple | El registro incluye qué se rechazó y por qué. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No existe `sonar-project.properties` ni invocación del scanner en los workflows; `backend-tests.yml` y `contrato.yml` fallan en el último push a `origin/master`. | No cumple | No conformidad del §8: falta la configuración del scanner, un run exitoso y la URL pública del análisis con Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | Barrido de patrones sobre el hash sin credenciales reales (solo `placeholder` y la referencia a `access-token`); ningún `.env` versionado; `git log -S"BEGIN PRIVATE KEY"` y `-S"service_role"` sin coincidencias; `grep` de JWT `eyJ...` sin coincidencias. | Cumple | `infra/terraform.tfstate` está versionado pero es un archivo vacío (0 bytes): no contiene estado ni secretos. El patrón de `.gitignore` (`infra/terraform/*.tfstate`) no cubre esa ruta, conviene corregirlo. |
| Contribución de todos los integrantes | `shortlog -sne` consolidado por correo idéntico: Zavod Dev 73, Josh Ortega + Josh4OP (mismo correo) 29, Luis-Salas-Reyes 9, deortahollman-star 9 y Luis Daniel 5. | Cumple | Los cuatro integrantes declarados tienen commits; `Zavod Dev` se atribuye a Diego Andrés Ramos con reserva (no se consolida por parecido de nombre), y 「Luis Daniel」 aparece con un segundo correo que no se fusiona con `Luis-Salas-Reyes`. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subió tarde o corrigió entregas anteriores, aquí se nota.

- **Punta actual revisada**: `652f78b76198ca854f7b3e79b910506e65ee4418 2026-09-27T23:39:11-05:00 feat(infra): importar proyecto Supabase LinkClub con Terraform`
- **Veredicto**: con pendientes
- **Commits posteriores al cierre**: ninguno; la punta actual coincide con el hash calificado.
- Resumen: la entrega S8 llegó parcialmente. Hay infraestructura versionada (Dockerfile + Terraform), vista de despliegue en arc42 §7 con una caja por pieza, restricciones de costo y tarjeta en §2, estimación de costo con volumen propio y punto de ruptura, y secretos fuera del código. Pero no hay URL pública declarada, los dos workflows de la rama están en rojo, no hay logs estructurados ni métrica instrumentada ligada a un escenario, no se puede recrear el entorno desplegado desde el README, y falta un ADR por decisión de plataforma (solo hay uno para la BD y está en estado «Propuesto»). Se arrastran además los problemas de nombres y duplicados de ADR y las ediciones de ADR aceptados.

Pendientes que siguen abiertos:
- Desplegar y publicar la URL pública con la hora y el código de respuesta de `/health`.
- Poner en verde los workflows `backend-tests.yml` y `contrato.yml` sobre `origin/master`.
- Añadir configuración de logs estructurados con una línea de ejemplo.
- Instrumentar una métrica consultable ligada a un escenario de calidad.
- Documentar en el README la recreación del entorno desplegado (Dockerfile/Terraform).
- Escribir un ADR de plataforma para el hosting de la API con alternativa descartada.
- Corregir los nombres y el número duplicado de los ADR 0003 y dejar de editar ADR aceptados.

## Recuento y nota sugerida

**5 de 10 criterios graduables** (la matriz de la ficha tiene 12 filas; las 2 filas de despliegue quedan pendientes de calificar en esta pasada).

**Propuesta provisional al docente — `nota = 1 + 4 × (5/10) = 3.0`**; quedan 2 filas de despliegue pendientes de calificar y la nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL del sistema desde fuera de la red: No verificado por decisión docente (la URL se entrega por Moodle y no está disponible). El repositorio no declara URL pública.
- Health check: No verificado por decisión docente. La ruta existe en `backend/src/linkclub/adapters/inbound/api/health_router.py:10`.
- Runs de CI y de contrato: ambos workflows fallan en el último push; no hay run verde que citar.
- Logs estructurados y métrica: no hay evidencia en el árbol; no es una comprobación que exija ejecutar el sistema.

## Hallazgos para la planilla

- La entrega S8 llegó parcial: IaC (Dockerfile + Terraform), arc42 §7, restricciones §2 y estimación de costo con supuestos y punto de ruptura; el resto no.
- No hay URL pública declarada ni en el README ni en arc42 §7.
- Los workflows `backend-tests.yml` y `contrato.yml` concluyen `failure` en el último push a `origin/master`.
- No hay configuración de logs estructurados ni métrica instrumentada ligada a un escenario (la dependencia `prometheus-fastapi-instrumentator` está declarada pero sin uso).
- El README no documenta la recreación del entorno desplegado a partir del Dockerfile/Terraform.
- `docs/adr/` conserva dos archivos 0003 (uno con espacio en el nombre) y duplica el número; el ADR-0004 de plataforma está en estado «Propuesto» y no cubre el hosting de la API.
- ADR-0001 y ADR-0002 se editaron después de aceptados sin ADR de reemplazo.
- `infra/terraform.tfstate` está versionado como archivo vacío y el patrón de `.gitignore` no cubre esa ruta.
