# semana-07-evidencia-s7 · InvenTrack

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `f10fd01` en `origin/main` (2026-09-20T23:01:13-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | `contracts/openapi/v1.json` en el árbol de f10fd01 (2026-09-20T23:01:13-05:00); declara OpenAPI 3.1.0 y versión 0.1.0. | Cumple | El archivo ejecutable y sus rutas se inspeccionaron en el estado calificado. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | `contracts/openapi/v1.json` define seis paths y `components.schemas` para productos, movimientos y errores de validación. | Cumple | Las respuestas y solicitudes referencian esquemas ejecutables, no solo una lista en prosa. |
| Correspondencia entre el contrato y la API implementada | `app/productos/infrastructure/router.py` implementa POST `/productos` y DELETE `/productos/{producto_id}`; `app/inventario/infrastructure/router.py` implementa entradas, salidas y consulta, todas presentes en el contrato. | Cumple | El conjunto de paths se compara automáticamente con `app.openapi()` en la prueba contractual. |
| Versión de la API declarada y con historial | `contracts/openapi/v1.json` declara `info.version: 0.1.0`; su historial contiene `81ebeab` y `af24edb`. | Cumple | `docs/api/inventrack-contrato.md` §8 dice 1.0.0 y debe corregirse, pero la versión ejecutable sí está declarada y versionada. |
| Prueba de contrato presente | `tests/contract/test_openapi_contract.py` en el árbol de f10fd01, descrito en ADR-0004 como comparación con `app.openapi()`. | Cumple | Ninguna. |
| El pipeline ejecuta la prueba de contrato | `.github/workflows/test.yml` ejecuta `PYTHONPATH=. pytest -v tests/contract/test_openapi_contract.py` en el paso `Validate versioned API contract`. | Cumple | La prueba también entra en el `pytest -v` general del mismo workflow. |
| Evidencia de que la prueba falla ante un cambio incompatible | ADR-0004 narra una verificación manual (quitar el `503` documentado produce `AssertionError`), sin run en rojo, commit ni diff que lo reproduzca. | No verificado | Sin runs_ci en la evidencia; haría falta la URL del run fallido o el commit del cambio incompatible. |
| ADR de la estrategia de integración ligado a un escenario | `docs/adr/0003-integracion-productos-inventario-via-puertos-de-aplicacion.md`: decisión síncrona vía puertos, alternativa de eventos descartada y consecuencias de acoplamiento, ligada a ESC-01 y ESC-02. | Cumple | Ninguna. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/arc42-template-EN.md`, `Runtime View`, describe la consulta de producto y el movimiento concurrente con secuencias entre API, aplicación, dominio y persistencia. | Cumple | La sección conecta los flujos con ESC-01 y el corte ejecutable. |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/c4/containers.md`: flechas etiquetadas «HTTPS / HTML (UI)», «HTTPS / JSON (REST API)», «In-Process Memory / Objetos Python (Futuro: TCP / Wire SQL)» y «SMTP / MIME (Texto Plano)». | Cumple | Ninguna. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | `AS_202620_InvenTrack` en la organización ISCOUTB, visible=true; el historial muestra 4 identidades consolidadas por correo (Jose Vargas, Esteban Peluffo, la identidad de Felix Taborda con tres nombres visibles y jxviercarta-a11y). | Cumple | Las 4 cuentas visibles corresponden a los 4 integrantes declarados; consolidación hecha por igualdad de correo, no por parecido de nombre. |
| Estructura mínima | En f10fd01 existen `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Rutas alternas (p. ej. `contracts/openapi/`) son desviación tolerable, no ausencia. |
| Convenciones de ADR | `docs/adr/0001-…` a `0004-…` cumplen el patrón `NNNN-kebab-case.md`, con contexto, alternativas, decisión, consecuencias y trazabilidad. | Cumple | No se aporta `git log --follow` por ADR para comprobar que ninguno aceptado fue reescrito. |
| Tabla de aspectos | `docs/aspectos.md` con las 8 columnas (ID · Aspecto · Requisito · C4 · ADR · Código · Pruebas · Evidencia) y filas ASP-01 y ASP-02 con enlaces navegables. | Cumple | Ninguna. |
| Registro de uso de IA | `docs/ia.md` con 16 entradas fechadas (2026-08-08 a 2026-09-20) y columna de lo rechazado con motivo técnico. | Cumple | Crece a lo largo del semestre. |
| README | `README.md` describe el sistema y su índice incluye «Cómo ejecutar el esqueleto»; ADR-0001 cita el comando de arranque documentado allí (`python -m uvicorn app.main:app --reload`). | Cumple | La sección de pruebas no se alcanza a ver en el extracto aportado; se deduce de la suite pytest del repositorio. |
| Pipeline y análisis estático | Se esperaba la línea del workflow que invoca el scanner de SonarCloud, la URL del run exitoso y la URL pública del Quality Gate; a HEAD rige `d7045d8` «fix(ci): temporarily disable SonarCloud scan and Java setup in CI pipeline» (2026-09-20T22:27:44-05:00) y no hay runs_ci en la evidencia. | No cumple | El análisis estático está deshabilitado en la configuración vigente y no hay badge ni URL de análisis que lo sustituya. |
| Secretos | Evidencia del repositorio: «(sin coincidencias)» en el barrido de credenciales y `envs_versionados: []`. | Cumple | Ninguna. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `f10fd01147a9831e219d27217eae3165fcac0384 2026-09-20T23:01:13-05:00 refactor(docs): update architectural scenarios for consistency, availability, performance, and security measures`
- **Veredicto**: con pendientes
- Resumen: Proyecto evaluado en su punta actual de `origin/main`: f10fd01 (2026-09-20T23:01:13-05:00), dentro del cierre. Cumple 9/10 criterios de la ficha: contrato, correspondencia, prueba, ejecución en CI, ADR, arc42 §6 y C4 son verificables. Solo falta evidencia reproducible de que la prueba falla ante un cambio incompatible; transversalmente SonarCloud permanece deshabilitado.

Pendientes que siguen abiertos:
- SonarCloud deshabilitado en el workflow desde el commit d7045d8 y sin URL pública de Quality Gate.
- Evidencia reproducible de fallo de la prueba contractual ante un cambio incompatible.
- Versión del contrato contradictoria entre ADR-0004 y el documento de API.

## Recuento y nota sugerida

9 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.6 = 1 + 4 × (9/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Run en rojo o commit del cambio incompatible que hizo fallar la prueba.
- SonarCloud: el scanner está deshabilitado y no se aporta URL pública con Quality Gate para el hash revisado.

## Hallazgos para la planilla

- Entrega a tiempo: el hash calificado f10fd01 (2026-09-20T23:01:13-05:00) es el HEAD de `origin/main` y es anterior al cierre.
- `contracts/openapi/v1.json` está versionado, declara OpenAPI 3.1.0, versión 0.1.0, seis paths y esquemas reutilizables.
- Contradicción de versión del contrato: ADR-0004 dice `0.1.0` y `docs/api/inventrack-contrato.md` §8 dice `1.0.0`.
- `.github/workflows/test.yml` ejecuta explícitamente `tests/contract/test_openapi_contract.py`; no hay URL pública de SonarCloud con Quality Gate.
- El análisis de SonarCloud fue deshabilitado en el workflow antes del cierre (commit `d7045d8`), dejando pendiente una comprobación transversal.
- La afirmación de que la prueba falla ante un cambio incompatible está solo narrada en ADR-0004, sin run en rojo ni commit reproducible.
- El C4 nivel 2 sí etiqueta protocolo y formato en todas las flechas.
- El ADR-0003 justifica la integración síncrona frente a la alternativa de eventos, atada a ESC-01 y ESC-02.
