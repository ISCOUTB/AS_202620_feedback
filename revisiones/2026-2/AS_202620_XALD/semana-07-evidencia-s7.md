# semana-07-evidencia-s7 · XALD

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `364ac5b` en `origin/master` (2026-09-17T15:43:54-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.yaml con `openapi: 3.1.0`, presente en el árbol de 364ac5b (2026-09-17). | Cumple | Es especificación legible por máquina versionada en docs/api/, no prosa. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.yaml: `paths: /transacciones` con requestBody `$ref TransaccionDTO` y respuesta 202 `$ref RespuestaSincronizacion`, más `components.schemas` con TransaccionDTO, RespuestaSincronizacion y OrigenDatosEnum. | Cumple | El DTO declara 7 campos requeridos con tipos, formato y ejemplo. |
| Correspondencia entre el contrato y la API implementada | El contrato solo declara POST /transacciones (docs/api/openapi.yaml) mientras el flujo de sincronización documentado usa POST /api/v1/sync (docs/arc42/06-Runtime view.md, escenario 6.3); el único backend del árbol es backend_xald/index.js y su contenido no se aporta. | No cumple | Se buscaron rutas del contrato en el código y rutas del código en el contrato: no se pudo trazar ninguna en ninguno de los dos sentidos. |
| Versión de la API declarada y con historial | docs/api/openapi.yaml declara `info.version: 1.0.0`; el bundle no incluye el historial del archivo. | No verificado | Falta `git log --format='%h %cI %s' -- docs/api/openapi.yaml` para ver el versionado real. |
| Prueba de contrato presente | Árbol de 364ac5b: solo existen XALDAPP/app/src/test/java/com/proyecto/xald/Cortevertical.kt, Entornotest.kt, ExampleUnitTest.kt, ValidacionModulosTest.kt y los Example*Test por módulo; ninguna prueba valida docs/api/openapi.yaml. | No cumple | Se esperaba un archivo de prueba de contrato (validación OpenAPI, schemathesis, pact, dredd) y no hay ninguno. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/ci.yml, pero no hay prueba de contrato que invocar y el bundle no aporta el contenido del workflow ni el grep de 'contract\|dredd\|schemathesis\|pact\|prism\|spectral\|openapi'. | No cumple | Sin prueba de contrato en el repositorio, el pipeline no puede ejecutarla. |
| Evidencia de que la prueba falla ante un cambio incompatible | El bundle no incluye runs_ci y no se aporta run en rojo ni artefacto del cambio incompatible. | No verificado | Queda como pregunta de sustentación: hace falta la URL del run fallido o la evidencia del cambio que rompe el contrato. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0001-patron-offline-first.md descarta el cliente-servidor síncrono y liga la integración asíncrona a ESC-01 y ESC-05 con sus riesgos de acoplamiento; docs/adr/0007-contratos-por-modulo.md evalúa alternativas descartadas y consecuencias de acoplamiento. | Cumple | ADR-0007 traza a la auditoría de la semana 6 más que a un ESC numerado; el anclaje a escenario lo aporta ADR-0001. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06-Runtime view.md: escenarios 6.1 a 6.4 con diagramas de secuencia Mermaid y descripción paso a paso. | Cumple | El extracto aportado está truncado al final de 6.4; conviene confirmar el cierre del archivo. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/c2.md existe en el árbol, pero el bundle no incluye su contenido. | No verificado | Se necesita el diagrama del nivel 2; la tabla de contexto técnico de docs/arc42/03 sí etiqueta protocolo y formato, pero no es el C2. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_XALD, `visible: true`, organización ISCOUTB; el historial registra 4 cuentas (dilanbejarano011, colmenares2007-crypto, xaviergarciadiaz20-commits, axeljruiz717-hash), tantas como integrantes declarados. | Cumple | Todas las cuentas del historial pertenecen a la organización y hay actividad de las cuatro. |
| Estructura mínima | En 364ac5b existen docs/adr/, docs/c4/, docs/arc42/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | docs/arc42/04-Solution Strategy sin extensión .md y faltan las secciones 07 y 11 de arc42. |
| Estado del repositorio que se califica | origin/master en 364ac5b, 2026-09-17T15:43:54-05:00, anterior al cierre 2026-09-21T05:00:00Z. | Cumple | Entrega temprana y sin commits posteriores al cierre. |
| Convenciones de ADR | docs/adr/0001..0007 con nombres NNNN-kebab-case.md; ADR-0007 incluye contexto, opciones evaluadas, decisión, consecuencias y trazabilidad. | Cumple | ADR-0005 sigue 'En revisión' y ADR-0007 declara puntos abiertos. |
| Tabla de aspectos | docs/aspectos.md existe en 364ac5b, pero el bundle no incluye su contenido. | No verificado | Hace falta ver las 8 columnas (ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia) y que las celdas sean navegables. |
| Registro de uso de IA | ia_log muestra 12 commits sobre docs/ia.md entre 2026-08-07 y 2026-09-13, pero no se aporta el contenido. | No verificado | No se puede verificar qué se aceptó y qué se rechazó con su motivo técnico. |
| README | README.md describe la app, el comando de arranque/pruebas (`gradlew.bat test`) y los requisitos previos (JDK 17, Android SDK). | Cumple | El comando documentado ejecuta pruebas y no arranca la app; incluye rutas locales con "<user>". |
| Pipeline y análisis estático | Existe .github/workflows/ci.yml, pero el bundle no aporta contenido del workflow ni runs_ci, y no hay sonar-project.properties en el árbol. | No verificado | Para Cumple faltan la línea del scanner, la URL del run y la URL pública del análisis con Quality Gate; la revisión de secretos no halló coincidencias ni .env versionados. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `364ac5bddd020fc5edda5b56e70aaa666c287306 2026-09-17T15:43:54-05:00 Revise OpenAPI documentation for financial sync API`
- **Veredicto**: con pendientes
- Resumen: A HEAD (origin/master, 364ac5b, 2026-09-17) el proyecto está bien estructurado y documentado, con contrato OpenAPI 3.1.0 ejecutable, 7 ADR y arc42; sin embargo la prueba de contrato y su ejecución en el pipeline no existen, la correspondencia contrato↔código no se demuestra y SonarCloud no es auditable. Quedan además pendientes anteriores sin cerrar: ADR-0005 en estado 'En revisión', el punto abierto de ADR-0007 sobre la ubicación de ReceptorSmsBancario y las secciones 07 y 11 de arc42 ausentes.

Pendientes que siguen abiertos:
- Prueba de contrato inexistente y sin ejecución en el pipeline.
- Sin evidencia de fallo de la prueba ante un cambio incompatible.
- Correspondencia contrato↔código no trazada (/transacciones vs /api/v1/sync).
- SonarCloud sin configuración, run ni URL pública del análisis.
- C4 nivel 2, docs/aspectos.md y docs/ia.md sin contenido verificable en la evidencia.
- ADR-0005 en revisión y punto abierto de ADR-0007 (ReceptorSmsBancario).
- Secciones 07 y 11 de arc42 ausentes.

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- C4 nivel 2: falta el contenido de docs/c4/c2.md con cada flecha etiquetada con protocolo y formato.
- docs/aspectos.md: falta la tabla con sus 8 columnas y celdas navegables.
- docs/ia.md: falta el contenido, en particular la columna de lo rechazado y su motivo.
- Historial del contrato: falta `git log --format='%h %cI %s' -- docs/api/openapi.yaml`.
- CI y SonarCloud: faltan runs_ci (nombre, conclusion, URL) y la URL pública del análisis con Quality Gate.

## Hallazgos para la planilla

- El contrato existe y está modelado con esquemas completos, pero no hay ninguna prueba de contrato en el repositorio.
- El único endpoint del contrato no se puede trazar al código y el flujo documentado usa otra ruta (POST /api/v1/sync).
- No hay runs de CI citables ni evidencia pública de SonarCloud.
- Sin prueba de contrato no es posible demostrar que falle ante un cambio incompatible.
- Documentación arc42 y ADRs extensos, con ADR-0007 que cierra las violaciones detectadas en la semana 6.
- Sin secretos ni archivos .env versionados.
- Entrega temprana: el hash calificado es anterior al cierre y no hay commits posteriores.
