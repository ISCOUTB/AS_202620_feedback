# semana-07-evidencia-s7 · InvenTrack

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `81ebeab` en `origin/main` (2026-09-17T23:00:46-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | contracts/openapi/v1.json presente en el árbol del commit 81ebeab de origin/main. | Cumple | El archivo existe y está versionado; no se aportó su contenido, así que no se pudo validar que sea OpenAPI legible. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | Se esperaba el fragmento con paths y components/schemas de contracts/openapi/v1.json; el archivo no se incluyó en la evidencia. | No verificado | El ADR-0004 afirma que la prueba compara metadatos, rutas, parámetros y esquemas, pero es una afirmación sobre el contrato, no el contrato. |
| Correspondencia entre el contrato y la API implementada | Se buscaron dos rutas del contrato en app/productos/infrastructure/router.py y app/inventario/infrastructure/router.py y una ruta del código en el contrato; no se aportó el contenido ni de los routers ni del contrato. | No verificado | Sin ambos archivos citables no puede descartarse desincronización en ninguno de los dos sentidos. |
| Versión de la API declarada y con historial | La ruta contracts/openapi/v1.json sugiere versión v1, pero no se aportó el campo de versión interno ni la salida de git log sobre ese archivo. | No verificado | Falta `git log --format='%h %cI %s' -- contracts/openapi/v1.json` para ver el historial del contrato. |
| Prueba de contrato presente | tests/contract/test_openapi_contract.py en el árbol de 81ebeab; ADR-0004 describe que compara contracts/openapi/v1.json con app.openapi(). | Cumple | La ruta de la prueba se cita; su contenido no se aportó. |
| El pipeline ejecuta la prueba de contrato | Se esperaba la línea del workflow en .github/workflows/test.yml (grep de contract/schemathesis/pact/prism/spectral) y la URL del run; no se aportó el contenido del workflow ni runs_ci. | No verificado | Sin run citado no puede confirmarse que la prueba se ejecute en CI y no solo que el archivo exista. |
| Evidencia de que la prueba falla ante un cambio incompatible | Se buscó un run en rojo en el historial de Actions y evidencia aportada por el equipo del cambio incompatible; no se incluyó ninguna de las dos. | No verificado | Queda como pregunta de sustentación: una prueba que pasa siempre no prueba nada. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0003-integracion-productos-inventario-via-puertos-de-aplicacion.md: Contexto liga ESC-01 y ESC-02 y el apartado de Alternativas evalúa cuatro opciones, incluida la de eventos descartada por complejidad. | Cumple | Justifica la llamada síncrona por puertos frente a eventos y frente a fusionar módulos. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42-template-EN.md está en el árbol y el README indexa '6 · Runtime View' con diagramas de secuencia, pero el fragmento aportado está truncado antes de esa sección. | No verificado | Harían falta los flujos de interacción citables (por ejemplo, el registro concurrente de movimientos). |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/containers.md, diagrama Mermaid: 'Dueno -- HTTPS --> Web', 'Web -- "HTTPS/REST" --> Api', 'Api -- SMTP --> Notif', 'Api -- "Repositorios / futuro SQL" --> Db'. | No cumple | Varias flechas llevan protocolo, pero ninguna declara formato de datos y la flecha API–Persistencia usa un mecanismo, no protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_InvenTrack en la organización ISCOUTB, visible: true, rama principal origin/main; autores consolidados por identificador de cuenta repetido: Jose Vargas (2 alias), Esteban Peluffo (1), Felix Taborda (3 alias) y Javier Carta (1) = 4 identidades. | Cumple | Las cuatro identidades consolidadas coinciden con los cuatro integrantes declarados. |
| Estructura mínima | En 81ebeab: README.md, docs/adr/, docs/c4/, docs/arc42/, docs/aspectos.md y docs/ia.md. | Cumple | El arc42 vive en un único docs/arc42/arc42-template-EN.md en lugar de archivos por sección: desviación de forma, no ausencia del artefacto. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md, 0002-control-concurrencia-memoria-inventario.md, 0003-integracion-productos-inventario-via-puertos-de-aplicacion.md y 0004-contrato-api-versionado-openapi.md, todos en NNNN-kebab-case y con el título enunciando la decisión. | Cumple | El ADR-0004 no incluye sección de trazabilidad y no se aportó git log de los ADR para verificar que ninguno se reescribió tras aceptarse. |
| La tabla de aspectos | docs/aspectos.md: dos filas (ASP-01, ASP-02) con las ocho columnas del curso y enlaces a requisito, C4, ADR, código, pruebas y evidencia. | Cumple | Celdas navegables, sin huecos visibles en las dos filas. |
| Registro de uso de IA | docs/ia.md con seis entradas entre 2026-08-08 y 2026-09-13 y columna 'Rechazado / motivo' con motivos técnicos. | Cumple | El archivo acumula 12 commits entre 2026-08-09 y 2026-09-13, es decir, crece a lo largo del semestre. |
| README | README.md describe el sistema, incluye 'Cómo ejecutar el esqueleto' en el índice, y ADR-0001 cita el comando único `python -m uvicorn app.main:app --reload`. | Cumple | El fragmento aportado está truncado y no se observa una sección dedicada a cómo se prueba. |
| Pipeline y análisis estático | Existen .github/workflows/test.yml y sonar-project.properties, pero no hay línea del workflow que invoque el scanner, ni run exitoso citado, ni URL pública del análisis; docs/ia.md (2026-09-13) registra que el paso de SonarCloud se retiró del workflow hasta confirmar el secreto. | No cumple | Faltan las tres evidencias exigidas por el contrato: configuración e invocación, run exitoso del hash revisado y URL pública con estado del Quality Gate. |
| Secretos | Barrido del historial sin coincidencias de credenciales y sin archivos .env versionados (envs_versionados: []). | Cumple | Sin hallazgos de secretos en el estado revisado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `81ebeabe12386ad45a886aa1eb6331acc66130ac 2026-09-17T23:00:46-05:00 feat: agregar contrato OpenAPI versionado`
- **Veredicto**: con pendientes
- Resumen: En la punta actual de origin/main (81ebeab, 2026-09-17, sin commits posteriores al cierre) existen el contrato OpenAPI, la prueba de contrato y los ADR de integración y de versionado del contrato, pero no hay evidencia de ejecución en CI, no hay prueba de que la prueba falle ante cambios incompatibles, el análisis de SonarCloud quedó fuera del pipeline y el C4 nivel 2 no declara formato en sus flechas.

Pendientes que siguen abiertos:
- SonarCloud sin ejecución, sin run asociado y sin URL pública con Quality Gate (paso retirado del workflow).
- Ejecución de la prueba de contrato en el pipeline sin run citado.
- Evidencia de que la prueba de contrato falla ante un cambio incompatible.
- C4 nivel 2 sin formato de datos en las flechas.
- Módulos usuarios, proveedores y alertas sin código (VIO-02 diferido por diseño).

## Recuento y nota sugerida

3 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 2.2 = 1 + 4 × (3/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contrato OpenAPI: contenido, rutas y esquemas de contracts/openapi/v1.json (no se aportó el archivo).
- Correspondencia contrato–código: faltan dos rutas del contrato localizadas en el código y una ruta del código presente en el contrato.
- Versión de la API declarada en el archivo y git log del contrato.
- Ejecución de la prueba de contrato en el pipeline: línea de .github/workflows/test.yml y URL del run del hash revisado.
- Run en rojo o evidencia aportada de que la prueba falla ante un cambio incompatible.
- arc42 sección 6: los flujos de interacción no son visibles en el fragmento aportado.

## Hallazgos para la planilla

- El contrato contracts/openapi/v1.json y su prueba existen, pero no se aportó el contenido de ninguno de los dos, así que no se pueden citar rutas ni esquemas.
- No hay ningún run de CI citado: no puede confirmarse que el pipeline ejecute la prueba de contrato.
- No hay evidencia de que la prueba de contrato falle ante un cambio incompatible, que es el diferenciador del segundo corte.
- El análisis de SonarCloud quedó fuera del workflow según el registro de IA, por lo que no hay URL pública ni Quality Gate.
- El C4 nivel 2 etiqueta protocolos (HTTPS, SMTP) pero ningún formato de datos en sus flechas.
- La evidencia no registra commits posteriores al cierre ni nuevos respecto del cierre anterior; el hash calificado (81ebeab, 2026-09-17) es anterior al cierre 2026-09-21T05:00:00Z.
- Cuatro identidades de git consolidadas coinciden con los cuatro integrantes declarados del equipo.
