# semana-07-evidencia-s7 · LaPlacita

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `8c2e1bc` en `origin/master` (2026-09-20T22:47:32-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | `openapi.yaml` en la raíz del repo declara OpenAPI 3.1.0, versión v1, 10 paths y 11 operaciones. | Cumple | El archivo ejecutable se inspeccionó en el estado calificado. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | `openapi.yaml` define 10 paths, 11 operaciones y esquemas `Producto`, `Pedido`, solicitudes, notificaciones y errores. | Cumple | Las solicitudes y respuestas usan esquemas ejecutables con campos obligatorios y tipos. |
| Correspondencia entre el contrato y la API implementada | Los 10 paths de `openapi.yaml` tienen su `route.js` bajo `app/api/v1/`; la prueba recorre los paths y verifica esa correspondencia. | Cumple | Se contrastaron, entre otras, GET `/health`, POST `/pedidos` y las rutas de entrega. |
| Versión de la API declarada y con historial | `openapi.yaml` declara `info.version: v1`; `git log` registra su incorporación en `6314123` (2026-09-18T13:57:35-05:00). | Cumple | La versión y el contrato están bajo control de versiones. |
| Prueba de contrato presente | `tests/contract-openapi.test.js` lee `openapi.yaml`, enumera sus rutas y verifica la existencia de los handlers correspondientes. | Cumple | La prueba contrasta el contrato ejecutable con la implementación. |
| El pipeline ejecuta la prueba de contrato | `.github/workflows/ci.yml`, job `contract-test`, ejecuta `node --test tests/contract-openapi.test.js`. | Cumple | La invocación es explícita y bloquea el job `sonar` por dependencia. |
| Evidencia de que la prueba falla ante un cambio incompatible | `docs/evidencia-fallo-contrato-s7.md` documenta el cambio incompatible, comando, salida `fail 1 / pass 22` y restauración a verde. | Cumple | La evidencia aportada identifica el caso que detecta la rotura y el código de salida no exitoso. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0006-estrategia-integracion-sincrona.md con ESC-01..05, alternativas descartadas y consecuencias; ratificado por ADR-0008. | Cumple | ADR-0006 queda propuesto y ADR-0008 lo acepta. |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/arc42-template-EN.md` §6 describe cinco flujos con actor, protocolo, formato y secuencia, más una tabla de interacciones internas y externas. | Cumple | Los flujos cubren pedidos, pagos, entrega, catálogo y notificaciones. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/contenedores.md etiqueta flechas con HTTPS/REST API, HTTP REST/JSON, HTTPS/JSON. | Cumple | Cumple con etiquetado de protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_LaPlacita, visible=true; autores consolidan 4 identidades: Jorge M. Castillo, samulssl, Isaza927/isaza927, matbuendia. | Cumple | Isaza927 e isaza927 comparten correo, pero no se publica; no se atribuye por parecido de nombre. |
| Estructura mínima | Árbol incluye README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md. | Cumple | arc42 está en inglés y como template; estructura presente. |
| Estado del repositorio que se califica | origin/master HEAD 8c2e1bc, fecha 2026-09-20T22:47:32-05:00, anterior al cierre 2026-09-21T05:00:00Z. | Cumple | Sin commits post cierre en la rama. |
| Convenciones de ADR | docs/adr/0001..0008 con nombres kebab-case y campos de contexto, opciones, decisión, consecuencias y trazabilidad. | Cumple | No se aporta git log para verificar inmutabilidad; ADR-0007 menciona sección extraída de ADR-0005. |
| Tabla de aspectos | docs/aspectos.md tiene filas A-03..A-06 con requisito sin enlace y columna extra 'Escenarios' frente a las ocho columnas del contrato. | No cumple | Celdas no navegables y columna adicional. |
| Registro de uso de IA | `docs/ia.md` contiene una bitácora fechada con propuestas aceptadas, rechazadas y su validación técnica, incluida la entrega S7. | Cumple | El registro crece durante el semestre y distingue decisiones no adoptadas. |
| README | `README.md` documenta requisitos, instalación, arranque con `npm run dev` y ejecución de pruebas. | Cumple | El procedimiento local está descrito sin depender de un servicio externo. |
| Pipeline y análisis estático | sonar-project.properties existe, pero ADR-0003 dice 'análisis en vivo pendiente de SONAR_TOKEN'; no hay run URL ni URL SonarCloud con Quality Gate. | No cumple | Faltan las tres evidencias exigidas. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `8c2e1bc4a22fae593de776d7e9469ffb29c10a08 2026-09-20T22:47:32-05:00 Organización del repositorio de acuerdo a la nueva documentación complementaria`
- **Veredicto**: ficha S7 completa, con no conformidades transversales
- Resumen: Proyecto en master 8c2e1bc al cierre. Cumple 10/10 criterios de la ficha: contrato, correspondencia, prueba y ejecución, fallo incompatible reproducible, ADR, arc42 §6 y C4 están sustentados. Transversalmente siguen pendientes SonarCloud, la trazabilidad de `docs/aspectos.md` y deuda de semanas previas.

Pendientes que siguen abiertos:
- V-02 ACL Pedidos→Catálogo
- V-04 Shared Kernel tiendaId
- V-05 OHS evento notificaciones
- V-06 orquestador
- SonarCloud token y análisis
- Enlaces tabla aspectos

## Recuento y nota sugerida

10 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 5.0 = 1 + 4 × (10/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- URL pública de SonarCloud y estado del Quality Gate.
- Trazabilidad navegable de todas las filas de `docs/aspectos.md` y cierre de las deudas V-02, V-04, V-05 y V-06.

## Hallazgos para la planilla

- El contrato `openapi.yaml` contiene 10 paths, 11 operaciones y esquemas; la prueba contractual verifica su correspondencia con los handlers.
- El workflow invoca el job de contrato; la evidencia de SonarCloud sigue incompleta y no hay Quality Gate público.
- `docs/evidencia-fallo-contrato-s7.md` documenta una rotura incompatible con salida `fail 1 / pass 22` y restauración a verde.
- La tabla de aspectos presenta requisitos sin enlace en A-03..A-06 y una columna extra.
- No hay commits posteriores al cierre S7 en origin/master.
- arc42 §6 documenta cinco flujos con protocolo, formato y secuencia.
- ADR-0003 indica que SonarCloud sigue pendiente del token SONAR_TOKEN.
- La deuda V-02, V-04, V-05 y V-06 permanece abierta para Corte 2.
