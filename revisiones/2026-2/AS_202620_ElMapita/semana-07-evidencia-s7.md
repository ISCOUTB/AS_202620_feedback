# semana-07-evidencia-s7 · ElMapita

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `afae3be` en `origin/main` (2026-09-20T19:09:25-06:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público efímero |

> Revisión actualizada tras el cierre: se leyeron en el repositorio, en el hash afae3be, las filas que la pasada automática había dejado como No verificado.

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | `docs/api/openapi.v1.yaml` leído en afae3be: línea 1 `openapi: 3.1.0`, línea 5 `info.version: 1.0.0` y `paths:` en la línea 46. | Cumple | Es una especificación OpenAPI 3.1 real, versionada y leída completa desde el repositorio; no es prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | `docs/api/openapi.v1.yaml`: `openapi: 3.1.0`, `info.version: 1.0.0`, 16 operaciones y `components.schemas` con `Building`, `Floor`, `Poi`, `User`, `AuthTokens`, `SignInInput`, `UserLocation` y demás, con `required` y `properties`. | Cumple | Los esquemas de datos están declarados y referenciados desde las respuestas; el archivo llega completo. |
| Correspondencia entre el contrato y la API implementada | docs/adr/0003-contrato-openapi-versionado.md: tabla que contrasta GET /api/v1/map/buildings (contrato/frontend) con GET /api/api/v1/map/buildings (backend) y GET /health con GET /api/health. | No cumple | La desincronización por prefijo duplicado está reconocida por el propio equipo y sigue sin corregirse en el código. |
| Versión de la API declarada y con historial | Ruta docs/api/openapi.v1.yaml (v1 en el nombre), `info.version: 1.0.0` (línea 5) y commit afae3be «Contrato de API y prueba de contrato»; ADR-0003 fija la regla MAJOR/MINOR/PATCH. | Cumple | `git log -- docs/api/openapi.v1.yaml` en el estado calificado da un único commit, afae3be (2026-09-20), que introduce el archivo; el commit 30499d5 (2026-09-27) es posterior al cierre y no se califica. |
| Prueba de contrato presente | `backend/test/contract/openapi.contract-spec.ts` leído en afae3be: describe «Contrato OpenAPI v1 (docs/api/openapi.v1.yaml) vs runtime real» (línea 193) y valida las operaciones del contrato con fakes; `backend/test/jest-contract.json` la selecciona con `"testRegex": ".contract-spec.ts$"`. | Cumple | El spec y su configuración Jest están versionados y su contenido se leyó desde el repositorio. |
| El pipeline ejecuta la prueba de contrato | `.github/workflows/ci.yml` define el job `contract` con los pasos "Lint del contrato (OpenAPI 3.1 válido)" (`@redocly/cli lint`), "Generar OpenAPI real desde NestJS" y "Contrato vs runtime real (RSK-04)" con `run: npm run test:contracts`. | Cumple | El paso que ejecuta la prueba es `npm run test:contracts`, marcado `continue-on-error` mientras RSK-04 siga abierto; el pipeline la invoca igualmente. La URL del run es externa. |
| Evidencia de que la prueba falla ante un cambio incompatible | No se aportó ningún run en rojo ni evidencia del cambio incompatible introducido a propósito. | No verificado | Queda como pregunta de sustentación; una prueba que nunca falla no prueba nada. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0003-contrato-openapi-versionado.md: descarta AsyncAPI y el code-first frente a OpenAPI 3.1 y expone consecuencias de acoplamiento. | Cumple | No nombra un escenario de calidad numerado (EC-xx) de forma explícita. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/arc42-template-EN.md`, sección "# 6. Vista de tiempo de ejecución": 6.1 Carga y renderizado inicial de un edificio 3D (EC-01/EC-02), 6.2 Geolocalización en tiempo real y degradación (EC-03), 6.3 Consulta fuera de línea (EC-04) y 6.4 Autenticación y sincronización de POIs, cada uno con diagrama de flujo y pasos numerados. | Cumple | Los cuatro flujos de interacción están descritos y trazados a los escenarios de calidad. |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/c4/C4_L2_Container.md`: diagrama Mermaid `C4Container` cuyas `Rel(...)` etiquetan cada relación con protocolo y formato (`mobileApp → backendApi` "HTTPS/JSON REST", `mobileApp → supabaseStorage` "HTTPS S3 signed URL", `mobileApp → supabaseRealtime` "WSS Pub/Sub", `backendApi → supabaseDb` "PG Wire / PostgREST RLS"). | Cumple | Las relaciones se etiquetan con protocolo y formato; las de UI y caché local usan la tecnología (UI táctil, Hive, Filesystem), no un protocolo de red. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | AS_202620_ElMapita en la organización ISCOUTB, visible:true, rama origin/main (afae3be). | Cumple | Historial con 3 cuentas (RobotDRMX, Rodrigo Vazquez Rico, dgarza2705); solo una coincide nominalmente con los integrantes declarados y la pertenencia a la organización no es verificable con esta evidencia. |
| Estructura mínima | En afae3be existen docs/arc42/, docs/adr/ (0001-0003), docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Desviación de formato anotada: docs/glosario.docx, docs/CorteVertical_ElMapitaUTB.docx y docs/cortes/corte-1.pdf en lugar de Markdown revisable. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico-propuesto.md, 0002-restriccion-rendimiento-compatibilidad-dispositivos.md y 0003-contrato-openapi-versionado.md cumplen el patrón NNNN-titulo-en-kebab-case.md. | Cumple | Los tres nombres siguen la convención del contrato §4; los archivos existen en el árbol de afae3be. |
| Tabla de aspectos | `docs/aspectos.md`: tabla con las columnas ID · Aspecto · Requisito · Escenarios de calidad · C4 · ADR · Código · Pruebas · Evidencia para EC-01..EC-04, con enlaces navegables a C4 nivel 1/2, ADR-0001 y rutas de código. | Cumple | Contiene las ocho columnas del contrato más una adicional ("Escenarios de calidad"); las celdas Pruebas y Evidencia siguen marcadas "Pendiente" en las cuatro filas. |
| Registro de uso de IA | Historial de docs/ia.md con 7 commits entre 2026-08-07 y 2026-09-20, incluido afae3be; contenido leído: descarta el formato `.svg`/Mermaid «no compatibles en visores estándar» (línea 28), no elige Hexagonal pese a su mayor puntaje (línea 199) y adopta OpenAPI 3.1 «(no AsyncAPI) — la integración real es 100% REST síncrona» (línea 240). | Cumple | El registro documenta rechazos con su motivo técnico, además de los usos aceptados. |
| README | README.md describe el sistema, prerrequisitos, scripts/dev.sh y scripts/dev.ps1, y los comandos de prueba (npm run test, flutter test). | Cumple | El arranque con un solo comando depende de configurar antes backend/.env con credenciales de Supabase. |
| Pipeline y análisis estático | No hay invocación de SonarCloud: en afae3be no existe `sonar-project.properties` y el job `.github/workflows/ci.yml` no tiene ningún paso `sonar` (jobs: backend, contract, frontend, docs, quality-gate); la lista de runs confirma ejecuciones de CI pero ninguna con análisis estático. | No cumple | Se esperaban la línea del scanner, el run exitoso y la URL pública del análisis con Quality Gate; los tres faltan. La ausencia se prueba con el árbol y el workflow, sin requerir credenciales. |
| Secretos | El grep sobre afae3be solo devuelve nombres de parámetros y tipos (password: string, refresh_token) y el badge de plantilla de NestJS; envs_versionados vacío y solo backend/.env.example. | Cumple | El token del badge de plantilla en backend/README.md es un marcador, no una credencial real; conviene retirarlo igualmente. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `afae3be7c7fa2e00e311d899425149e3b954ae4f 2026-09-20T19:09:25-06:00 Contrato de API y prueba de contrato`
- **Veredicto**: con pendientes
- Resumen: Releídas en el repositorio las filas que la pasada automática había dejado como No verificado, en la punta afae3be (2026-09-20, anterior al cierre) el contrato OpenAPI 3.1 tiene rutas y esquemas, el job `contract` ejecuta la prueba, arc42 §6 describe cuatro flujos, el C4 nivel 2 etiqueta protocolo y formato y la tabla de aspectos tiene sus ocho columnas; siguen abiertos la deriva de rutas contrato-backend, la falta de evidencia de que la prueba falle y la ausencia de SonarCloud. El recuento de la ficha pasa a 8/10.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Sin envíos posteriores al cierre: commits_post_cierre vacío y el commit calificado afae3be es anterior al cierre.
- Brecha de `npm run test:contracts` prometida en ADR-0001 y nunca implementada: se cierra en afae3be con el ADR-0003, dentro del plazo de S7; el job `contract` de ci.yml ya la invoca (`continue-on-error` mientras RSK-04 siga abierto).

Pendientes que siguen abiertos:
- Deriva de rutas contrato-backend por prefijo duplicado (`/api/api/v1/...`), reconocida en ADR-0003 y no corregida.
- Evidencia de que la prueba de contrato falla ante un cambio incompatible: no hay run en rojo atribuible al contrato ni evidencia del cambio introducido.
- Evidencia de SonarCloud (configuración del scanner, run exitoso y URL pública con Quality Gate), ausente y pendiente desde S6.
- Celdas Pruebas y Evidencia de `docs/aspectos.md` marcadas "Pendiente" en las cuatro filas.
- Implementación pendiente declarada en ADR-0002 (LOD y degradación progresiva).

## Recuento y nota sugerida

8 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.2 = 1 + 4 × (8/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Fallo de la prueba ante cambio incompatible: no hay run en rojo atribuible al contrato ni evidencia del cambio introducido; queda como pregunta de sustentación.
- SonarCloud: no hay configuración del scanner en el repositorio ni invocación en el workflow, por lo que la fila transversal queda en No cumple.
- Celdas Pruebas y Evidencia de docs/aspectos.md: siguen en "Pendiente" en las cuatro filas.

## Hallazgos para la planilla

- Contrato OpenAPI 3.1 versionado en docs/api/openapi.v1.yaml (rutas y esquemas de datos) y prueba de contrato en backend/test/contract/openapi.contract-spec.ts.
- El ADR-0003 reconoce deriva de rutas: el backend expone /api/api/v1/... y el contrato/frontend usan /api/v1/... .
- El job `contract` de ci.yml ejecuta el lint del contrato y `npm run test:contracts`; sigue sin evidencia de un fallo controlado.
- arc42 §6 describe cuatro flujos de interacción y el C4 nivel 2 etiqueta protocolo y formato.
- No hay evidencia de SonarCloud (sin configuración ni invocación en el workflow: fila transversal en No cumple).
- El registro docs/ia.md crece de agosto a septiembre con 7 commits.
- No hay credenciales reales en el historial; solo nombres de parámetros y un badge de plantilla.
- Se consolidan 3 cuentas autoras; solo una coincide nominalmente con integrantes declarados.
- El commit calificado afae3be (2026-09-20T19:09:25-06:00) es anterior al cierre y no hay commits posteriores.
