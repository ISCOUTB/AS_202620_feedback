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
| Contrato en formato ejecutable versionado en el repositorio | `contracts/openapi/v1.json` en el árbol de f10fd01 (2026-09-20T23:01:13-05:00); ADR-0004 lo describe como OpenAPI 3.1 versionado. | Cumple | El contenido del archivo no se aporta, así que no se pudo leer la versión ni las rutas internas. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | Se esperaba `paths` y `components.schemas` de `contracts/openapi/v1.json`; solo hay la tabla de endpoints en prosa de `docs/api/inventrack-contrato.md` §3 y el mapa de errores §4. | No verificado | Falta citar el fragmento del archivo con esquemas de respuesta (haría falta el JSON o su volcado). |
| Correspondencia entre el contrato y la API implementada | Se esperaban dos rutas del contrato localizadas en `app/productos/infrastructure/router.py` y `app/inventario/infrastructure/router.py` y una ruta del código en el contrato; no se aporta el contenido de routers ni del JSON. | No verificado | Haría falta citar ruta:línea en el router y la ruta homóloga en el contrato. |
| Versión de la API declarada y con historial | ADR-0004 declara `info.version: 0.1.0` y `docs/api/inventrack-contrato.md` §8 declara «1.0.0»; no se aporta `git log -- contracts/openapi/v1.json`. | No verificado | Dos fuentes del propio repositorio declaran versiones distintas y no hay historial git citado del contrato. |
| Prueba de contrato presente | `tests/contract/test_openapi_contract.py` en el árbol de f10fd01, descrito en ADR-0004 como comparación con `app.openapi()`. | Cumple | Ninguna. |
| El pipeline ejecuta la prueba de contrato | Existe `.github/workflows/test.yml`, pero no se aporta su contenido ni runs_ci; ADR-0004 afirma un paso «Validate versioned API contract» sin URL de run. | No verificado | Comando anotado: `grep -rniE 'contract\|openapi' .github/workflows/` y URL del run asociado al hash revisado. |
| Evidencia de que la prueba falla ante un cambio incompatible | ADR-0004 narra una verificación manual (quitar el `503` documentado produce `AssertionError`), sin run en rojo, commit ni diff que lo reproduzca. | No verificado | Sin runs_ci en la evidencia; haría falta la URL del run fallido o el commit del cambio incompatible. |
| ADR de la estrategia de integración ligado a un escenario | `docs/adr/0003-integracion-productos-inventario-via-puertos-de-aplicacion.md`: decisión síncrona vía puertos, alternativa de eventos descartada y consecuencias de acoplamiento, ligada a ESC-01 y ESC-02. | Cumple | Ninguna. |
| arc42 sección 6 con los flujos de interacción | El contenido aportado de `docs/arc42/arc42-template-EN.md` se corta antes de la sección 6; el índice del README menciona «6 · Runtime View» sin citar el texto. | No verificado | Haría falta la ruta:línea de la sección 6 con los flujos de interacción. |
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
- Resumen: Proyecto evaluado en su punta actual de `origin/main`: f10fd01 (2026-09-20T23:01:13-05:00), dentro del cierre. Cumple 7 de 8 criterios transversales; la ficha de la semana queda en 4 de 10 porque buena parte de la evidencia exigida (contenido del contrato, correspondencia con el código, ejecución en CI y resultado del análisis estático) no es citable con lo aportado.

Pendientes que siguen abiertos:
- SonarCloud deshabilitado en el workflow desde el commit d7045d8 y sin URL pública de Quality Gate.
- Contrato sin evidencia de ejecución en CI ni de fallo ante cambio incompatible.
- Versión del contrato contradictoria entre ADR-0004 y el documento de API.
- Esquemas del contrato y correspondencia con los routers sin verificar.
- Sección 6 de arc42 sin evidencia citable.

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Esquemas de datos y rutas internas de `contracts/openapi/v1.json` (no se aporta el archivo).
- Correspondencia contrato–API en `app/productos/infrastructure/router.py` y `app/inventario/infrastructure/router.py` (no se aporta el código de los routers).
- Historial git del contrato: `git log --format='%h %cI %s' -- contracts/openapi/v1.json`.
- Ejecución de la prueba de contrato en el pipeline: `grep -rniE 'contract|openapi' .github/workflows/` y URL del run del hash f10fd01.
- Run en rojo o commit del cambio incompatible que hizo fallar la prueba.
- Sección 6 del arc42 (`docs/arc42/06*` o la sección Runtime View del archivo entregado).

## Hallazgos para la planilla

- Entrega a tiempo: el hash calificado f10fd01 (2026-09-20T23:01:13-05:00) es el HEAD de `origin/main` y es anterior al cierre.
- `contracts/openapi/v1.json` está versionado, pero su contenido no fue aportado: no se pudieron comprobar rutas, esquemas ni la versión interna.
- Contradicción de versión del contrato: ADR-0004 dice `0.1.0` y `docs/api/inventrack-contrato.md` §8 dice `1.0.0`.
- No hay runs de CI en la evidencia ni URL de análisis público: la ejecución de la prueba de contrato queda sin comprobar.
- El análisis de SonarCloud fue deshabilitado en el workflow antes del cierre (commit `d7045d8`), dejando pendiente una comprobación transversal.
- La afirmación de que la prueba falla ante un cambio incompatible está solo narrada en ADR-0004, sin run en rojo ni commit reproducible.
- El C4 nivel 2 sí etiqueta protocolo y formato en todas las flechas.
- El ADR-0003 justifica la integración síncrona frente a la alternativa de eventos, atada a ESC-01 y ESC-02.
