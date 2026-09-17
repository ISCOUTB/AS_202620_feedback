# semana-07-evidencia-s7 · Recobra

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `47fb44b` en `origin/master` (2026-09-13T16:58:53-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol HEAD 47fb44b sin ningún archivo openapi/swagger/asyncapi (.yaml/.json) ni .proto; solo existe el cliente mobile/lib/api/recobra_api.dart y controllers Nest. | No cumple | No hay contrato de API que citar; se esperaba archivo ejecutable en el repo. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No existe el archivo de contrato; no hay fragmento de rutas/esquemas que citar en HEAD 47fb44b. | No cumple | Sin contrato no hay paths ni schemas de respuesta que verificar. |
| Correspondencia entre el contrato y la API implementada | El código expone POST/GET /publicaciones y GET /health (README.md secciones Endpoints), pero no hay contrato contra el que contrastar dos rutas de ida y una de vuelta. | No cumple | Imposible comprobar desincronización sin contrato. |
| Versión de la API declarada y con historial | No hay archivo de contrato, por lo que no hay campo de versión ni salida de git log -- <ruta del contrato>. | No cumple | Se esperaba campo de versión (info.version o similar) e historial git del contrato. |
| Prueba de contrato presente | Árbol 47fb44b solo contiene specs unitarios y e2e (src/**/*.spec.ts, test/publicaciones*.e2e-spec.ts); ningún archivo de prueba de contrato. | No cumple | Se esperaba prueba tipo schemathesis/dredd/pact o equivalente. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml existe pero no se observa invocación de contrato (contract/dredd/schemathesis/pact/prism/spectral); no se aporta URL de run. | No cumple | Se esperaba la línea del workflow que invoca la prueba y el run correspondiente. |
| Evidencia de que la prueba falla ante un cambio incompatible |  | No verificado | Haría falta curl actions/runs filtrando conclusion!=success o captura del fallo; queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0001-estilo-arquitectonico.md, 0002-arquitectura-y-stack.md y 0003-reto-corte1-stack-obligatorio.md tratan estilo, stack y reto de corte 1; ninguno decide síncrono vs. asíncrono contra un escenario. | No cumple | ADR-0003 cita S5 pero sobre el reto de stack, no sobre estrategia de integración. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42.md, sección '## 6. Vista de ejecución' describe el flujo crear (pasos 1-5) y el flujo consultar GET /publicaciones/:id. | Cumple | La sección existe y describe los flujos; el resto del arc42 aparece truncado en §10. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/C4-C2.md: la flecha app→api lleva 'Llama (HTTP/JSON)', pero usuario→app 'Usa (UI)', api→store 'vía puerto PublicacionRepository' y las planeadas (auth/notif) no llevan protocolo ni formato. | No cumple | No todas las flechas del nivel 2 están etiquetadas con protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_Recobra en org ISCOUTB, visible=true; historial con 5 cuentas: Cconde31, vylrir, Fernando Isacc Conde Herrera, MiguelJacome, Steamlinker. | Cumple | 5 cuentas autoras frente a 4 integrantes declarados; pertenencia a la organización no verificable y Steamlinker no se mapea por parecido de nombre. |
| Estructura mínima | Presentes docs/arc42/arc42.md, docs/adr/0001-0003, docs/c4/C4-C1..C3, docs/aspectos.md, docs/ia.md y README.md en HEAD 47fb44b. | Cumple | arc42 unificado en un archivo; documento visible truncado en §10 (no se ven §7, §8, §11, §12). |
| Estado del repositorio calificado | origin/master, hash 47fb44b con fecha 2026-09-13T16:58:53-05:00, anterior al cierre 2026-09-21T05:00:00Z. | Cumple | Rama principal declarada master; se califica ese commit. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md, 0002-arquitectura-y-stack.md, 0003-reto-corte1-stack-obligatorio.md cumplen NNNN-kebab-case; ADR-0001 marcada 'Reemplazada por ADR-0002'. | Cumple | Los títulos enuncian la decisión; cada ADR incluye contexto, alternativas, decisión y consecuencias. |
| Tabla de aspectos | docs/aspectos.md con las 8 columnas (ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia) y filas A1-A4 con enlaces. | Cumple | La fila A3 tiene celdas sin enlace (aspecto planeado), posible hueco según semana. |
| Registro de uso de IA | docs/ia.md con columna de lo rechazado y su motivo (p. ej. rechazo de FastAPI/NextJS y de desactivar Sonar); 8 commits sobre el archivo. | Cumple | Registro crece a lo largo del semestre. |
| README | README.md: 'Cómo levantar el backend' (npm install && npm run start, Node 18+), 'Cómo levantar el cliente Flutter' y 'Cómo correr las pruebas' (npm test, npm run test:e2e, flutter test). | Cumple | El backend arranca con un solo comando; el cliente requiere pasos propios. |
| Pipeline y análisis estático | Existen sonar-project.properties y .github/workflows/ci.yml, pero no se aportan runs_ci ni URL pública del Quality Gate. | No verificado | Faltan la línea del scanner, el run exitoso del hash y la URL de SonarCloud; comando: curl -s "https://api.github.com/repos/ISCOUTB/AS_202620_Recobra/actions/runs?per_page=5". |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `47fb44bb7c5cca9b1c7a6d020649a086600ee619 2026-09-13T16:58:53-05:00 Rename file to 'restricciones_justificadas.md'`
- **Veredicto**: con pendientes
- Resumen: A HEAD de origin/master (47fb44b, 2026-09-13) el proyecto no incorpora contrato de API, prueba de contrato ni ADR de integración; C4 nivel 2 y arc42 quedan incompletos, por lo que la entrega S7 no está cubierta.

Pendientes que siguen abiertos:
- Contrato OpenAPI/AsyncAPI en formato ejecutable versionado
- Prueba de contrato y su invocación en el pipeline
- Evidencia de fallo de la prueba ante cambio incompatible
- ADR de estrategia de integración (síncrona/async)
- Flechas del C4 nivel 2 con protocolo y formato
- Secciones de arc42 faltantes (7, 8, 11, 12)
- Evidencia auditable de CI y Quality Gate de SonarCloud

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Fallo de la prueba de contrato ante cambio incompatible: sin run rojo ni evidencia aportada; haría falta curl a actions/runs o captura.
- Ejecución de CI y Quality Gate de SonarCloud: sin runs_ci ni URL pública; comando curl a actions/runs.
- Pertenencia a la organización ISCOUTB de cada cuenta autora: no verificable con los datos disponibles.

## Hallazgos para la planilla

- No existe archivo OpenAPI/AsyncAPI/proto en el árbol: el contrato de la API no está versionado.
- No se encontró prueba de contrato ni invocación de la misma en el workflow.
- No hay ADR de estrategia de integración (síncrona o asíncrona) ligado a un escenario.
- C4-C2 tiene flechas sin protocolo ni formato (UI, persistencia y relaciones planeadas).
- arc42 se ve truncado en §10; no se observan §7, §8, §11 ni §12.
- docs/ia.md documenta un Quality Gate fallido corregido, pero no se aporta run que lo pruebe.
- Hay 5 cuentas autoras frente a 4 integrantes declarados; no se atribuye por parecido de nombre.
- docs/no-conformidades.md deja abierto un token de Coveralls recuperable del historial.
- docs/checklist-entrega-manual.md sugiere que el push se hizo después de preparar el corte.
