# semana-07-evidencia-s7 · GimnasioUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `0e3aeb5` en `origin/main` (2026-09-20T23:29:29-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/openapi.yaml en HEAD 0e3aeb5, con `openapi: 3.1.0` y 3 rutas. | Cumple | Es una especificación OpenAPI versionada, no prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/openapi.yaml define components.schemas: SolicitudAcceso (enum ENTRADA/SALIDA), RespuestaAforo (aforoActual integer minimum 0), RespuestaError y RespuestaHealth. | Cumple | Hay esquemas de petición y de respuesta, no solo rutas. |
| Correspondencia entre el contrato y la API implementada | `src/server.js` implementa `/health` y monta `crearAforoRouter` en `/api/v1/aforo`; el router implementa GET `/` y POST `/acceso`, las tres rutas de `docs/openapi.yaml`. | Cumple | El contraste cubre dos rutas del contrato y la ruta de código adicional `/health`, también presente en el contrato. |
| Versión de la API declarada y con historial | `docs/openapi.yaml` declara `info.version: 1.0.0`; `git log` registra el archivo en `9f4d288` (2026-09-20T20:25:02-05:00). | Cumple | La versión y el contrato están bajo control de versiones. |
| Prueba de contrato presente | tests/contrato.test.js existe en el árbol de 0e3aeb5. | Cumple | package.json la ejecuta con `node --test` usando ajv y js-yaml. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml, paso «Prueba de contrato (docs/openapi.yaml)» → `npm run test:contrato`; run en verde https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/35561182912. | Cumple | package.json mapea test:contrato a tests/contrato.test.js. |
| Evidencia de que la prueba falla ante un cambio incompatible | Cuatro runs CI terminaron en `failure` el 2026-09-21, p. ej. https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/35550973353, pero la evidencia disponible no identifica el paso ni un cambio incompatible. | No verificado | Un run rojo genérico no prueba la sensibilidad del contrato; falta el log del paso contractual o una reproducción aportada por el equipo. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0003-comunicacion-sincrona-asincrona.md decide síncrono/asíncrono y lista consecuencias, sin sección de alternativas descartadas ni cita de escenario de calidad. | No cumple | Se esperaba alternativa descartada y vínculo a un escenario; el ADR pasa de Contexto a Decisión. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/arc42_gimnasio_utb.md` §6 contiene secuencias de registro QR y notificación, y clasifica tipo, protocolo y formato. | Cumple | Los flujos distinguen la respuesta síncrona de la notificación asíncrona. |
| C4 nivel 2 con protocolo y formato en cada flecha | `docs/c4/c4_level2.md` etiqueta las seis relaciones: interacción UI/eventos, HTTPS REST/JSON, TCP 5432/SQL y FCM Push/JSON. | Cumple | Cada flecha declara el canal y el formato de intercambio correspondiente. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_GimnasioUTB con visible:true; el historial registra PedroPambi, sebastian-caicedo y RodrigoFacioLince, los tres integrantes declarados. | Cumple | Aparecen además las identidades 'Pedro Pallares' y 'Sebastian Felipe Caicedo Acosta' (2 commits cada una), no consolidables con las anteriores sin más evidencia. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md presentes en el árbol de 0e3aeb5. | Cumple | Los C4 están en docs/c4, ruta mínima esperada; hay documentos extra (correcciones.md, contextos-delimitados.md). |
| Convenciones de ADR | docs/adr/ADR0001.md no sigue el patrón NNNN-titulo-en-kebab-case.md y repite el número 0001 con contenido distinto al de 0001-arquitectura-hexagonal.md. | No cumple | Se esperaba un archivo por decisión; hay dos ADR 0001 con escenarios distintos (ES1/ES2/ES3/ES4 frente a ES1/ES7/ES8). |
| La tabla de aspectos | docs/aspectos.md encabeza con columnas de escenario de calidad (Estímulo, Fuente, Entorno, Respuesta, Medida, Tensión) y su segunda tabla tiene 5 columnas. | No cumple | Faltan las columnas ID, C4 y Evidencia de las ocho del curso; la trazabilidad a elementos C4 y a evidencia de calidad no es navegable. |
| Registro de uso de IA | docs/ia.md con entradas por semana (8 commits entre 2026-08-08 y 2026-09-13) que indican herramienta, salida, aceptado y rechazado con motivo, p. ej. el rechazo del C4 de contexto en la semana 2. | Cumple | En las semanas 4 y 5 la columna de rechazo queda en N/A o genérica, sin motivo técnico. |
| README | README.md documenta `npm install && npm start`, `npm test` y el requisito Node ≥ 18, con aviso de que la persistencia hoy es en memoria. | Cumple | Arranque en un solo comando declarado y reproducible sin PostgreSQL. |
| Pipeline y análisis estático | .github/workflows/ci.yml solo ejecuta `npm install`, `npm run test:base` y `npm run test:contrato`; no hay sonar-project.properties en el árbol ni línea del scanner, y no se aporta URL pública de análisis ni Quality Gate. | No cumple | Se esperaba la invocación del scanner en el workflow, el run que la ejecuta y la URL del análisis en SonarCloud (organización isco-utb). |
| Secretos | Búsqueda de patrones de credenciales sin coincidencias en HEAD 0e3aeb5; solo `.env.example` versionado y ningún `.env` en git ls-files. | Cumple | No hay credenciales expuestas en el commit calificado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `0e3aeb59599b9a07b0684563aa02c29ae0f38045 2026-09-20T23:29:29-05:00 Update documentation in correcciones.md`
- **Veredicto**: con pendientes
- Resumen: En HEAD 0e3aeb5 (origin/main, 2026-09-21T04:29Z, dentro del cierre) el equipo cumple 8/10 criterios de la ficha: entrega contrato OpenAPI 3.1.0 con esquemas y correspondencia en código, prueba contractual invocada por ci.yml, arc42 §6 y C4 etiquetado. Faltan la demostración de fallo ante un cambio incompatible y completar el ADR de integración; transversalmente siguen pendientes SonarCloud, el ADR 0001 duplicado y la tabla de aspectos.

Pendientes que siguen abiertos:
- SonarCloud sin evidencia auditable (configuración, scanner en el workflow y URL del análisis con Quality Gate).
- docs/adr/0003-comunicacion-sincrona-asincrona.md sin alternativa descartada ni escenario de calidad citado.
- docs/adr/ADR0001.md duplicado y fuera de la convención de nombres.
- docs/aspectos.md sin las ocho columnas del curso (faltan C4 y Evidencia).

## Recuento y nota sugerida

8 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.2 = 1 + 4 × (8/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Detalle del fallo de contrato: falta el log del run en rojo que muestre el paso de contrato fallando ante el cambio incompatible.
- Arranque: no se ejecutó código; la evidencia disponible es el README y los runs de CI citados (no hay paso de arranque en ci.yml).

## Hallazgos para la planilla

- docs/adr/ADR0001.md duplica el número 0001 con contenido distinto y rompe la convención de nombres del contrato.
- Sin evidencia de SonarCloud: ni archivo de configuración, ni línea del scanner en ci.yml, ni URL pública del análisis con Quality Gate.
- Cuatro runs de CI en failure el 2026-09-21 entre 01:23Z y 01:27Z seguidos de runs en verde; no se aporta el log del paso fallido.
- docs/openapi.yaml declara version 1.0.0 y tres rutas con esquemas; su historial inicia en 9f4d288.
- docs/aspectos.md usa columnas de escenarios de calidad en vez de las ocho columnas del curso.
- c4_level2.md etiqueta con canal y formato las seis relaciones, incluidas las interacciones UI/eventos.
- El historial muestra 5 identidades de autor para 3 integrantes declarados.
- La entrega se cerró con el commit 0e3aeb5 a las 2026-09-21T04:29Z, 31 minutos antes del cierre.
