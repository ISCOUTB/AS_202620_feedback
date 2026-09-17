# semana-07-evidencia-s7 · Verifacts

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `635f9b7` en `origin/master` (2026-09-16T00:52:52-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/contracts/openapi.yaml (openapi: 3.1.0) presente en el árbol del commit 635f9b7. | Cumple | Archivo OpenAPI versionado, no prosa; cumple el formato ejecutable pedido. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/contracts/openapi.yaml: paths /health, /analysis (get/post) y /analysis/{analysis_id}; components.schemas con HealthStatus, AnalysisRequest, AnalysisResult, AnalysisSummary, ErrorBody y ValidationErrorBody. | Cumple | Los esquemas fijan tipos, enums de classification/source_type y campos requeridos. |
| Correspondencia entre el contrato y la API implementada | Rutas /health, /analysis y /analysis/{analysis_id} del contrato frente a app/api/routes.py citado en docs/arc42/06-vista-de-ejecucion.md §6.1–6.3 y fila A-05 de docs/aspectos.md. | Cumple | El paquete de evidencia no incluye el código de routes.py; la correspondencia se sustenta en la documentación que nombra los handlers. |
| Versión de la API declarada y con historial | docs/contracts/openapi.yaml declara info.version '1.0.0', repetido en docs/arc42/09-decisiones-arquitectonicas.md y docs/adr/0003-integracion-sincrona.md. | No verificado | No se aportó el historial git del contrato; haría falta git log --format='%h %cI %s' -- docs/contracts/openapi.yaml (No cumple: falta la evidencia esperada). |
| Prueba de contrato presente | tests/test_contract.py en el árbol del commit; 12 pruebas citadas en la fila A-05 de docs/aspectos.md. | Cumple | Cubre forma de la respuesta, 422 por origen doble/ausente y arreglo plano del listado. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/tests.yml existe y docs/arc42/07-despliegue.md §7.2 documenta 'python -m pytest -q'. | No verificado | Sin URL de run no se comprueba la ejecución; falta la línea del workflow y el run en verde (comando sugerido: grep -rniE 'contract\|pytest' .github/workflows/). |
| Evidencia de que la prueba falla ante un cambio incompatible | docs/aspectos.md fila A-05: renombrar score→risk_score en app/api/routes.py hace fallar 4 pruebas y revertir vuelve a 20 passed. | Cumple | Evidencia manual aportada por el equipo; no hay run en rojo citable en Actions. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0003-integracion-sincrona.md con alternativa descartada (cola asíncrona), consecuencias de acoplamiento y enlace a Q-01 y Q-05. | Cumple | El título enuncia la decisión y documenta la deuda aceptada si la URL incumple el P95. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06-vista-de-ejecucion.md con secuencias de GET /health, POST /analysis y GET /analysis(+{id}) y verificación automatizada por prueba. | Cumple | La sección 6.3 aparece truncada en la copia aportada, pero los tres flujos quedan descritos. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/02-contenedores.md etiqueta cada flecha como 'HTTP/1.1 · JSON (fetch, síncrono)', 'HTTP/1.1 · HTML (Swagger UI)' o 'Driver sqlite3 · filas SQL'. | Cumple | Leyenda explícita de protocolo · formato y estado implementado/previsto. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible:true, repo AS_202620_Verifacts en ISCOUTB; autores: PedroC1213 (219+21 commits) y Cristian Cardeño (17 commits). | No cumple | El tercer integrante declarado no aparece en el historial; solo dos cuentas de git contribuyen. |
| Estructura mínima | Árbol del commit 635f9b7 incluye docs/arc42/ (11 secciones), docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Estructura conforme a la mínima del contrato. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md, 0002-contextos-sin-cambios.md y 0003-integracion-sincrona.md, con contexto, opciones, decisión y consecuencias. | Cumple | Nombres en kebab-case con numeración; no se aportó log --follow para comprobar inmutabilidad. |
| La tabla de aspectos | docs/aspectos.md con las ocho columnas del curso (ID, aspecto, escenario, C4, ADR, código, medida, evidencia) y filas A-00 a A-05 con enlaces. | Cumple | Cada fila enlaza escenario, vista, ADR y prueba; la fila A-00 deja un marcador de CI por reemplazar. |
| Registro de uso de IA | docs/ia.md con bitácora por interacción y ia_log con cuatro commits (2026-08-18 a 2026-09-08). | Cumple | El rechazo de LLM como clasificador se menciona; el motivo no queda como columna propia. |
| README | README.md describe el sistema, el arranque (python run.py / npm run dev) y las pruebas (python -m pytest -q). | Cumple | Dos comandos para backend y frontend; el detalle del corte vertical se remite a una sección del propio README. |
| Pipeline y análisis estático | .github/workflows/tests.yml, .github/workflows/sonarcloud.yml y sonar-project.properties presentes en el árbol. | No verificado | Faltan la línea del workflow que invoca el scanner, la URL del run exitoso y la URL pública del Quality Gate. |
| Secretos | Búsqueda sobre HEAD sin coincidencias ('secretos': sin coincidencias) y envs_versionados vacío; solo frontend/.env.example. | Cumple | No hay credenciales ni .env versionados. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `635f9b7b26764de3c9636d01f4500b7c1660dfa8 2026-09-16T00:52:52-05:00 Update README with new API endpoints and usage`
- **Veredicto**: con pendientes
- Resumen: A HEAD (635f9b7, 2026-09-16, anterior al cierre del 2026-09-21) el entregable S7 está completo en el repositorio: contrato, prueba de contrato, ADR-0003, arc42 §6 y C4 L2 con protocolo y formato. Quedan sin verificar la ejecución del pipeline y el análisis en SonarCloud por falta de runs citables, y arrastran pendientes de semanas previas Q-01, Q-04 y la prueba automatizada del frontend (A-04).

Pendientes que siguen abiertos:
- Medición formal de P95 para Q-01 (docs/escenarios-de-calidad.md la declara pendiente).
- Prueba de usuario 4 de 5 para Q-04 (declarada pendiente).
- Prueba automatizada de componente para el frontend: la fila A-04 solo tiene verificación manual.
- Marcador de CI en la fila A-00 de docs/aspectos.md, que el propio documento pide reemplazar por la URL real.
- Contradicción sobre Q-03 entre docs/escenarios-de-calidad.md ('Pendiente') y docs/aspectos.md A-02 (prueba en verde).
- Evidencia de run del pipeline y URL pública de SonarCloud con Quality Gate.

## Recuento y nota sugerida

8 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 4.2 = 1 + 4 × (8/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución de la prueba de contrato en el pipeline: falta la línea del workflow y la URL del run (revisar .github/workflows/ y la pestaña Actions).
- Historial git de docs/contracts/openapi.yaml: falta git log --format='%h %cI %s' -- docs/contracts/openapi.yaml.
- SonarCloud: falta URL del run que invoca el scanner y URL pública del análisis con estado del Quality Gate.
- Arranque y pruebas locales: sin run ni salida aportada; comando anotado python -m pytest -q.

## Hallazgos para la planilla

- Contrato OpenAPI 3.1 ejecutable en docs/contracts/openapi.yaml, con esquemas de datos y versión 1.0.0.
- Prueba de contrato tests/test_contract.py presente y alineada con el arreglo plano del listado y la cabecera X-Total-Count.
- El fallo inducido del contrato se sostiene solo en una verificación manual documentada (A-05), sin run en rojo citable.
- No se aportan runs de Actions ni URL pública de SonarCloud con Quality Gate.
- El tercer integrante declarado no registra commits: solo dos cuentas aparecen en el historial.
- docs/arc42/03 y 05 describen estados desactualizados (URL y POST /analysis como pendientes) frente al código citado en §6.
- docs/escenarios-de-calidad.md marca Q-03 como 'Pendiente' mientras docs/aspectos.md A-02 afirma prueba en verde: contradicción documental.
- docs/aspectos.md indica que la columna CI de A-00 conserva un marcador [PENDIENTE] por reemplazar.
