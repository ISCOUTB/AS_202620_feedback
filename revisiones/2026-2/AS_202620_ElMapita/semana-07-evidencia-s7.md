# semana-07-evidencia-s7 · ElMapita

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `afae3be` en `origin/main` (2026-09-20T19:09:25-06:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.v1.yaml presente en el árbol de afae3be (2026-09-20). | Cumple | Archivo versionado en el repositorio; su contenido no se aportó para lectura. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No se incluyó el contenido de docs/api/openapi.v1.yaml; ADR-0003 describe 16 operaciones con schemas derivados del dominio, sin fragmento citable. | No verificado | Falta el fragmento del contrato con rutas y esquemas de respuesta. |
| Correspondencia entre el contrato y la API implementada | docs/adr/0003-contrato-openapi-versionado.md: tabla que contrasta GET /api/v1/map/buildings (contrato/frontend) con GET /api/api/v1/map/buildings (backend) y GET /health con GET /api/health. | No cumple | La desincronización por prefijo duplicado está reconocida por el propio equipo y sigue sin corregirse en el código. |
| Versión de la API declarada y con historial | Ruta docs/api/openapi.v1.yaml (v1 en el nombre) y commit afae3be «Contrato de API y prueba de contrato»; ADR-0003 fija la regla MAJOR/MINOR/PATCH. | Cumple | No se aporta `git log -- docs/api/openapi.v1.yaml`; el historial visible se limita al commit que lo introduce. |
| Prueba de contrato presente | backend/test/contract/openapi.contract-spec.ts y backend/test/jest-contract.json en afae3be. | Cumple | Existe el spec y su configuración Jest; su contenido no se aportó. |
| El pipeline ejecuta la prueba de contrato | Solo consta .github/workflows/ci.yml en el árbol; no se citó la línea que invoca la prueba ni ningún run de Actions. | No verificado | El ADR-0003 menciona un job `contract`, pero sin línea de workflow ni URL del run. Comando: grep -rniE 'contract\|openapi\|schemathesis' .github/workflows/. |
| Evidencia de que la prueba falla ante un cambio incompatible | No se aportó ningún run en rojo ni evidencia del cambio incompatible introducido a propósito. | No verificado | Queda como pregunta de sustentación; una prueba que nunca falla no prueba nada. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0003-contrato-openapi-versionado.md: descarta AsyncAPI y el code-first frente a OpenAPI 3.1 y expone consecuencias de acoplamiento. | Cumple | No nombra un escenario de calidad numerado (EC-xx) de forma explícita. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42-template-EN.md está en el árbol, pero no se aportó el fragmento de la sección 6. | No verificado | Comando: git show afae3be:docs/arc42/arc42-template-EN.md \| grep -ni 'runtime view\|secci[oó]n 6\|interacci'. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/C4_L2_Container.md y su PNG presentes, sin contenido aportado. | No verificado | Falta el diagrama o su fuente para comprobar que cada flecha lleva protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | AS_202620_ElMapita en la organización ISCOUTB, visible:true, rama origin/main (afae3be). | Cumple | Historial con 3 cuentas (RobotDRMX, Rodrigo Vazquez Rico, dgarza2705); solo una coincide nominalmente con los integrantes declarados y la pertenencia a la organización no es verificable con esta evidencia. |
| Estructura mínima | En afae3be existen docs/arc42/, docs/adr/ (0001-0003), docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Desviación de formato anotada: docs/glosario.docx, docs/CorteVertical_ElMapitaUTB.docx y docs/cortes/corte-1.pdf en lugar de Markdown revisable. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico-propuesto.md, 0002-restriccion-rendimiento-compatibilidad-dispositivos.md y 0003-contrato-openapi-versionado.md cumplen el patrón NNNN-titulo-en-kebab-case.md. | Cumple | No se aporta `git log --follow` para comprobar que un ADR aceptado no fue reescrito. |
| Tabla de aspectos | docs/aspectos.md existe en afae3be; no se aportó su contenido. | No verificado | No se puede comprobar las ocho columnas ni que cada eslabón sea navegable. Comando: git show afae3be:docs/aspectos.md. |
| Registro de uso de IA | Historial de docs/ia.md con 7 commits entre 2026-08-07 y 2026-09-20, incluido afae3be. | Cumple | El registro crece a lo largo del semestre; no se aportó el contenido con lo rechazado y su motivo. |
| README | README.md describe el sistema, prerrequisitos, scripts/dev.sh y scripts/dev.ps1, y los comandos de prueba (npm run test, flutter test). | Cumple | El arranque con un solo comando depende de configurar antes backend/.env con credenciales de Supabase. |
| Pipeline y análisis estático | Solo consta .github/workflows/ci.yml en el árbol; faltan la línea del scanner, el run exitoso y la URL pública de SonarCloud con Quality Gate, y no se aportó ningún runs_ci. | No verificado | Comandos: ls .github/workflows/ y curl -s https://api.github.com/repos/ISCOUTB/AS_202620_ElMapita/actions/runs?per_page=5. |
| Secretos | El grep sobre afae3be solo devuelve nombres de parámetros y tipos (password: string, refresh_token) y el badge de plantilla de NestJS; envs_versionados vacío y solo backend/.env.example. | Cumple | El token del badge de plantilla en backend/README.md es un marcador, no una credencial real; conviene retirarlo igualmente. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `afae3be7c7fa2e00e311d899425149e3b954ae4f 2026-09-20T19:09:25-06:00 Contrato de API y prueba de contrato`
- **Veredicto**: con pendientes
- Resumen: En la punta afae3be (2026-09-20, anterior al cierre) el equipo entrega contrato OpenAPI 3.1 versionado, prueba de contrato y ADR de integración, pero quedan sin resolver la deriva de rutas entre contrato y backend, la falta de evidencia de ejecución (y de fallo) de la prueba en CI y la ausencia total de evidencia de SonarCloud; 4 de 10 criterios de la ficha y 6 de 8 transversales quedan en Cumple.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Sin envíos posteriores al cierre: commits_post_cierre vacío y el commit calificado afae3be es anterior al cierre.
- Brecha de `npm run test:contracts` prometida en ADR-0001 y nunca implementada: se cierra en afae3be con el ADR-0003, dentro del plazo de S7 pero aún sin evidencia de ejecución en CI.

Pendientes que siguen abiertos:
- Deriva de rutas contrato-backend por prefijo duplicado (`/api/api/v1/...`), reconocida en ADR-0003 y no corregida.
- Evidencia de que la prueba de contrato se ejecuta en el pipeline y de que falla ante un cambio incompatible.
- Evidencia de SonarCloud (configuración del scanner, run exitoso y URL pública con Quality Gate), pendiente desde S6.
- Contenido verificable de la tabla de aspectos, de arc42 §6 y del C4 nivel 2 con protocolo y formato.
- Implementación pendiente declarada en ADR-0002 (LOD y degradación progresiva).

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Rutas y esquemas del contrato: se esperaba el fragmento de docs/api/openapi.v1.yaml; solo consta la ruta del archivo. Se requiere `git show afae3be:docs/api/openapi.v1.yaml`.
- Ejecución de la prueba de contrato en CI: se esperaba la línea del workflow y la URL del run; solo consta el nombre de ci.yml y una mención en el ADR-0003. Se requiere el listado de runs de Actions.
- Fallo de la prueba ante cambio incompatible: no hay run en rojo ni evidencia del cambio introducido. Se requiere la URL del run fallido o el registro del cambio.
- arc42 sección 6: se esperaba el fragmento con flujos de interacción; solo consta el archivo plantilla. Se requiere `git show afae3be:docs/arc42/arc42-template-EN.md`.
- C4 nivel 2: se esperaba el diagrama con protocolo y formato por flecha; no se aportó el contenido de docs/c4/C4_L2_Container.md.
- SonarCloud: se esperaban configuración del scanner, run exitoso y URL pública con Quality Gate; no se aportó ninguno de los tres.
- Tabla de aspectos: se esperaba el contenido con las ocho columnas y la cadena navegable; solo consta la existencia de docs/aspectos.md.

## Hallazgos para la planilla

- Contrato OpenAPI 3.1 versionado en docs/api/openapi.v1.yaml y prueba de contrato en backend/test/contract/openapi.contract-spec.ts.
- El ADR-0003 reconoce deriva de rutas: el backend expone /api/api/v1/... y el contrato/frontend usan /api/v1/... .
- Sin runs de Actions aportados: no se puede confirmar que el pipeline ejecute la prueba de contrato ni que exista un run en rojo.
- No hay evidencia de SonarCloud (sin configuración citada, sin run y sin URL pública con Quality Gate).
- El registro docs/ia.md crece de agosto a septiembre con 7 commits.
- No hay credenciales reales en el historial; solo nombres de parámetros y un badge de plantilla.
- Se consolidan 3 cuentas autoras; solo una coincide nominalmente con integrantes declarados.
- El commit calificado afae3be (2026-09-20T19:09:25-06:00) es anterior al cierre y no hay commits posteriores.
