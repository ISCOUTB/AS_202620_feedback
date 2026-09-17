# semana-07-evidencia-s7 · LaPlacita

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `90f510e` en `origin/master` (2026-09-16T23:20:13-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | openapi.yaml en la raíz del árbol de 90f510e; README y docs/aspectos.md lo citan como 'Contrato OpenAPI 3.1 (v1)'. | Cumple | La evidencia aportada no incluye el contenido del archivo, solo su ruta. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | Se buscó el contenido de openapi.yaml en el árbol de 90f510e y solo consta el nombre del archivo. | No verificado | Hace falta el fragmento con paths y components/schemas para poder evaluarlo. |
| Correspondencia entre el contrato y la API implementada | El código lista app/api/v1/*/route.js y el contrato está citado, pero sin contenido del OpenAPI no hay cruce posible. | No verificado | Falta citar dos rutas del contrato y una del código. |
| Versión de la API declarada y con historial | README declara 'v1' del contrato, pero no hay git log del archivo en la evidencia. | No verificado | Falta el campo de versión en el propio contrato y su historial de commits. |
| Prueba de contrato presente | tests/contract-openapi.test.js en el árbol de 90f510e y referenciado en docs/aspectos.md (A-07). | Cumple | — |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml está en el árbol pero sin contenido; docs/aspectos.md afirma un job 'contract-test' sin enlace a run. | No verificado | Falta la línea del workflow que invoca la prueba y la URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | docs/evidencia-fallo-contrato-s7.md documenta el cambio incompatible en crearPedido y la salida 'fail 1 / pass 22' de la suite de contrato. | Cumple | Es evidencia aportada por el equipo, reproducida localmente y sin URL de run en rojo. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0006-estrategia-integracion-sincrona.md con ESC-01..ESC-05, alternativas B (broker) y C (EventEmitter) descartadas y consecuencias de acoplamiento. | Cumple | El ADR figura como 'propuesto', no 'aceptado'. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42-template-EN.md está en el árbol, pero el fragmento visible solo llega a la sección 4. | No verificado | Hace falta el texto de §6 con los flujos de interacción. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/contenedores.md etiqueta cada flecha, por ejemplo 'HTTPS / REST API', 'HTTP REST/JSON', 'HTTPS / JSON' y 'Push / HTTPS'. | Cumple | Cada relación lleva protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_LaPlacita con visibilidad pública; en el historial se consolidan 4 nombres visibles (Jorge M. Castillo, samulssl, Isaza927/isaza927, matbuendia). | Cumple | No se atribuyen cuentas a personas por parecido de nombre; el número coincide con los 4 integrantes declarados. |
| Estructura mínima | docs/adr/, docs/arc42/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md presentes en el árbol de 90f510e. | Cumple | arc42 se entrega como arc42-template-EN.md, sin desviación de ubicación del resto. |
| Convenciones de ADR | docs/adr/0001..0007 con nombres kebab-case que enuncian la decisión y con trazabilidad a requisito, C4, commit y pruebas. | Cumple | ADR-0001 aceptado se ratifica con ADR-0002 sin editarlo. |
| La tabla de aspectos | docs/aspectos.md con filas A-01..A-07 y las columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas y Evidencia con enlaces navegables. | Cumple | Añade una columna 'Escenarios' adicional a las ocho del curso. |
| Registro de uso de IA | docs/ia.md con tabla de propósito, herramienta, resultado, rechazado y validación; git log muestra 19 entradas de actualización entre agosto y septiembre. | Cumple | En las filas visibles la columna 'Rechazado' queda en '—' sin motivo técnico registrado. |
| README | README.md con descripción, funcionalidades, documentación enlazada, sección 'Cómo ejecutar', 'Pruebas' y 'Guía paso a paso'. | Cumple | El fragmento visible no muestra un comando único de arranque. |
| Pipeline y análisis estático | sonar-project.properties y .github/workflows/ci.yml están en el árbol pero sin contenido; ADR-0003 declara el análisis de SonarCloud pendiente del secreto SONAR_TOKEN; no hay URL de run ni de análisis. | No cumple | Faltan las tres evidencias exigidas: línea del scanner, run exitoso y URL pública con Quality Gate. |
| Secretos | Búsqueda de credenciales en HEAD sin coincidencias y lista de .env versionados vacía. | Cumple | — |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `90f510ef80d848626a9987a88bac11ca71af61d9 2026-09-16T23:20:13-05:00 Correcciones S7 y organizacion de codigo/estructura`
- **Veredicto**: con pendientes
- Resumen: En 90f510e el contrato v1, la prueba de contrato, el ADR-0006 y el C4 nivel 2 están presentes, pero quedan sin verificar la correspondencia contrato-código, los esquemas, la ejecución en CI y arc42 §6, y el análisis de SonarCloud sigue sin ejecución.

Pendientes que siguen abiertos:
- SonarCloud sin URL de análisis ni Quality Gate (ADR-0003 lo declara pendiente del secreto)
- Ejecución de la prueba de contrato en el pipeline sin verificar
- Correspondencia contrato↔código sin verificar
- Esquemas y versionado/historial del contrato sin verificar
- arc42 §6 con flujos de interacción sin verificar

## Recuento y nota sugerida

5 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.0 = 1 + 4 × (5/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correspondencia contrato↔código: faltan dos paths del OpenAPI y su cruce con app/api/v1/*.
- Esquemas de datos del contrato: no consta el contenido de openapi.yaml.
- Versión e historial del contrato: falta el campo en el archivo y el git log del mismo.
- Ejecución de la prueba de contrato en el pipeline: falta el contenido de ci.yml y la URL del run.
- arc42 §6: el fragmento visible llega solo hasta la sección 4.

## Hallazgos para la planilla

- Contrato v1 versionado y prueba de contrato presente en 90f510e.
- El equipo documentó el fallo de la prueba ante un cambio incompatible, sin URL de run en rojo.
- El contenido de openapi.yaml no consta, así que no se pudo cruzar con las rutas implementadas.
- El pipeline no se pudo verificar: ci.yml sin contenido y sin runs citados.
- SonarCloud sigue sin ejecución según lo declarado en ADR-0003.
- El C4 nivel 2 etiqueta cada flecha con protocolo y formato.
- No hay commits posteriores al cierre ni secretos versionados.
