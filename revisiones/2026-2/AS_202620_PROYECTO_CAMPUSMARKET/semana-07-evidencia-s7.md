# semana-07-evidencia-s7 · CampusMarket

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `c53ee32` en `origin/master` (2026-09-18T21:11:48-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | c53ee32: `contracts/openapi-v1.json` presente en el árbol del repo. | Cumple | Archivo JSON OpenAPI 3.1.0, no prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | README S7 declara esquemas `HealthResponse`, `PublicacionCreate`, `Publicacion`, `ErrorResponse`, `HTTPValidationError`, `ValidationError`. | Cumple | Los esquemas están listados junto a las rutas del contrato. |
| Correspondencia entre el contrato y la API implementada | README coteja `POST /publicaciones` y `GET /publicaciones` con `backend/app/publicaciones/router.py`, y `GET /health` con `backend/app/main.py`. | Cumple | Dos rutas contrato→código y una código→contrato quedan citadas. |
| Versión de la API declarada y con historial | README declara OpenAPI 3.1.0 y API 1.0.0; el contrato entra en el commit 485249a «Implementar contrato OpenAPI y prueba de contrato S7». | Cumple | Historial reproducible con `git log -- contracts/openapi-v1.json`. |
| Prueba de contrato presente | c53ee32: `backend/tests/test_contrato_openapi.py` en el árbol y citado en ADR-0003 §8 contra `contracts/openapi-v1.json`. | Cumple | La prueba compara el contrato versionado con el esquema generado por FastAPI. |
| El pipeline ejecuta la prueba de contrato | El README reproduce el paso `python -m pytest backend/tests/test_contrato_openapi.py -q` y cita el run 35291809164 (success) sobre 5bedc833. | No verificado | No hay runs_ci en la evidencia ni contenido de `.github/workflows/backend-tests.yml`; el run citado no corresponde al hash revisado c53ee32. |
| Evidencia de que la prueba falla ante un cambio incompatible | El README cita un run en rojo en `https://github.com/Nnigarp/.../actions/runs/34934077733` y existe `docs/evidencias/fallo-contrato-s7-2026-09-15.md`. | No verificado | El run en rojo está en un fork personal y no se aportó el contenido del archivo de evidencia. |
| ADR de la estrategia de integración ligado a un escenario | `docs/adr/0003-usar-integracion-sincrona-http-json.md`: escenario EC-06, alternativa asíncrona evaluada y descartada con sus consecuencias. | Cumple | Explícita el acoplamiento temporal como costo asumido. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/06-vista-ejecucion.md` (§6.1–6.3) describe creación, consulta y persistencia no disponible con diagramas de secuencia. | Cumple | Los flujos nombran router, service, repository y los códigos HTTP esperados. |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/c4/02-contenedores.puml` y `docs/c4/02-contenedores.md` están en el árbol de c53ee32. | No verificado | No se aportó el contenido del diagrama; no se puede comprobar que cada flecha indique protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo `AS_202620_PROYECTO_CAMPUSMARKET` en la organización ISCOUTB, visible:true, en el hash c53ee32. | Cumple | Identidades git consolidadas: Nnigarp (alias unidos por el mismo ID 115980006), camilixo92 y Carulla-sd = 3, igual al número de integrantes declarados. |
| Estructura mínima | c53ee32 contiene `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Sin desviaciones de rutas en los artefactos mínimos. |
| Convenciones de ADR | `docs/adr/0001-usar-monolito-modular.md` a `0004-migrar-persistencia-a-mysql.md` siguen NNNN-titulo-en-kebab-case. | Cumple | Los ADR incluyen contexto, alternativas, decisión y consecuencias. |
| Tabla de aspectos | `docs/aspectos.md` existe en c53ee32 y el README lo referencia como trazabilidad de aspectos. | No verificado | No se aportó su contenido; no se pueden verificar las ocho columnas ni que cada eslabón sea navegable. |
| Registro de uso de IA | `docs/ia.md` existe y acumula commits hasta c53ee32 (21 entradas de fecha en el historial). | No verificado | Falta el contenido para comprobar la columna de lo rechazado y su motivo técnico. |
| README | `README.md` declara qué es, requisitos previos, arranque con `scripts/run_s4.ps1` / `run_s4.sh` y pruebas con pytest. | Cumple | El arranque de un solo comando exige MySQL ya disponible y variables de entorno configuradas. |
| Pipeline y análisis estático | .sonarcloud.properties y `.github/workflows/backend-tests.yml` existen en c53ee32. | No verificado | Falta la línea del workflow que invoca el scanner y la URL pública del análisis con estado del Quality Gate. |
| Secretos | Las tres coincidencias de la búsqueda leen `CAMPUSMARKET_DB_PASSWORD` desde el entorno; `envs_versionados` está vacío. | Cumple | Sin credenciales embebidas ni `.env` versionado; no se detecta incidente. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `c53ee320c755299fb5d30b14ec4465a29142b0bf 2026-09-18T21:11:48-05:00 docs: registrar cierre y validacion final de S7`
- **Veredicto**: con pendientes
- Resumen: En HEAD c53ee32 (origin/master, 2026-09-18T21:11:48-05:00) la ficha S7 cumple 7 de 10 criterios: contrato ejecutable con esquemas, correspondencia con la API, versión con historial, prueba presente, ADR de integración y arc42 sección 6. Quedan sin verificar la ejecución del pipeline sobre el hash revisado, el fallo de la prueba ante cambio incompatible y el etiquetado del C4 nivel 2; la matriz transversal no acredita SonarCloud y no se aportó el contenido de aspectos, IA ni del diagrama de contenedores.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Migración de persistencia SQLite→MySQL documentada en `docs/adr/0004-migrar-persistencia-a-mysql.md` (fechado 2026-09-16) como corrección posterior al cierre de S5, fuera del plazo de esa entrega.
- Saneamiento de S7 mediante el merge 5bedc83 (2026-09-17, PR #42 desde una rama de revisor) y los commits de documentación 3ca4535 y c53ee32 (2026-09-18).
- commits_post_cierre está vacío y no se aportó diff_desde_cierre: no se observan cambios posteriores al cierre de esta actividad.

Pendientes que siguen abiertos:
- Acreditar SonarCloud: línea del scanner en el workflow y URL pública del análisis con estado del Quality Gate.
- Aportar la URL del run de CI sobre el hash revisado y del run en rojo del repositorio de la organización.
- Dejar revisable el contenido de `docs/aspectos.md` y `docs/ia.md`.
- Aportar `docs/c4/02-contenedores.puml` con protocolo y formato en cada flecha.

## Recuento y nota sugerida

7 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución del pipeline sobre c53ee32: haría falta la URL del run en el repo de la organización o el bloque runs_ci con nombre, conclusión y URL.
- Fallo de la prueba de contrato ante cambio incompatible: haría falta el run en rojo del repo de la organización o la evidencia aportada con su contenido.
- Etiquetas de protocolo y formato en cada flecha del C4 nivel 2: haría falta el contenido de `docs/c4/02-contenedores.puml`.
- SonarCloud auditable: haría falta la línea del workflow que invoca el scanner y la URL pública del análisis con Quality Gate.
- Contenido de `docs/aspectos.md` y `docs/ia.md`: haría falta el texto para comprobar columnas, enlaces y la columna de lo rechazado.

## Hallazgos para la planilla

- El contrato OpenAPI 3.1.0 está versionado en `contracts/openapi-v1.json` con versión de API 1.0.0 e historial desde 485249a.
- La prueba de contrato existe y ADR-0003 la declara como verificación del contrato.
- No hay runs_ci en la evidencia: la ejecución del pipeline se apoya solo en texto del README y en un run de 5bedc833, no del hash revisado.
- El run en rojo que probaría el fallo de la prueba está en un fork personal, no en el repositorio de la organización.
- No se aportó el contenido de `docs/aspectos.md`, `docs/ia.md` ni `docs/c4/02-contenedores.puml`.
- No aparece URL pública de SonarCloud con Quality Gate ni línea del scanner en el workflow.
- `docs/arc42/` tiene dos archivos numerados 10 (`10-arbol-de-utilidad.md` y `10-escenarios-de-calidad.md`).
- La persistencia se migró de SQLite a MySQL (ADR-0004, 2026-09-16) como corrección posterior a una observación docente.
