# semana-07-evidencia-s7 · Calificación automática

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `a47d5bd` en `origin/master` (2026-09-13T23:21:55-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol de a47d5bd: no aparece ningún archivo openapi/swagger/asyncapi (.yaml/.json) ni .proto; solo backend/api/main.py y docs/arc42/arc42-template-ES.md. | No cumple | Se esperaba un archivo de contrato ejecutable versionado; se revisó el árbol completo del commit calificado y no existe. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | Sin archivo de contrato en el árbol de a47d5bd; no hay rutas ni esquemas que citar. | No cumple | No se puede citar fragmento alguno porque el contrato no existe en el repositorio. |
| Correspondencia entre el contrato y la API implementada | El README describe POST /examenes/{id}/hojas y /health en backend/api/main.py, pero no hay contrato contra el cual contrastarlas. | No cumple | La API existe en código; falta el contrato que permita verificar la correspondencia en ambos sentidos. |
| Versión de la API declarada y con historial | No hay archivo de contrato en a47d5bd, por lo que no existe campo de versión ni git log del contrato. | No cumple | Se esperaba versión declarada en el propio contrato o en su ruta; no se encontró. |
| Prueba de contrato presente | backend/tests/ contiene test_arranque, test_carga_hojas, test_durabilidad_recepcion, test_encolado, test_fronteras, test_modulos_importables y test_recepcion; ninguna prueba de contrato. | No cumple | Se esperaba una prueba de contrato (dredd, schemathesis, pact, prism o equivalente); no aparece en el árbol. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml existe, pero no hay prueba de contrato que invocar; no se aporta run que la ejecute. | No cumple | Se esperaba la línea del workflow que invoca la prueba y la URL del run; no hay ninguna de las dos. |
| Evidencia de que la prueba falla ante un cambio incompatible | No hay runs de CI en la evidencia aportada ni prueba de contrato que pueda fallar; no se aporta evidencia del cambio incompatible. | No verificado | Queda como pregunta de sustentación: se esperaba un run en rojo o la evidencia del cambio incompatible que hizo fallar la prueba. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0002-procesar-calificacion-de-forma-asincrona.md: escenario EC-03/EC-04, alternativa A (síncrona) descartada con su consecuencia de acoplamiento y alternativa C (servicio aparte) descartada por RNF-07. | Cumple | El ADR justifica la estrategia asíncrona contra escenarios concretos y registra las alternativas descartadas. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42-template-ES.md declara en su encabezado que las secciones 1 a 6 están escritas, pero el contenido aportado se corta antes de la sección 6 y no se puede citar el flujo. | No verificado | Se esperaba docs/arc42/06* con los flujos descritos; el extracto disponible no permite confirmarlo ni negarlo. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/doc-c4.md existe en el árbol, pero no se aporta su contenido; ADR-0006 menciona relaciones 3 y 4 del Nivel 2 sin mostrar el diagrama. | No verificado | Se esperaba el diagrama de nivel 2 con cada flecha etiquetada con protocolo y formato; no se pudo comprobar. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Sistema-de-calificacion-automatica en la organización ISCOUTB, visible; autores scp1109, josueacademico17-source, SusanaRosales y Mariadelmar-restrepo en el historial. | Cumple | Los cuatro integrantes declarados aparecen como autores en el historial del repositorio. |
| Estructura mínima | Árbol de a47d5bd: docs/adr/ con 0001 a 0007, docs/arc42/, docs/c4/doc-c4.md, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Se cumple la estructura mínima; el C4 vive en docs/c4/ y el arc42 en docs/arc42/. |
| Qué estado del repositorio se califica | Rama principal origin/master; hash calificado a47d5bd con fecha 2026-09-13T23:21:55-05:00, anterior al cierre 2026-09-21T05:00:00Z. | Cumple | El commit calificado es el último de master anterior al cierre y no hay commits posteriores al cierre. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md a 0007-declarar-los-contextos-delimitados-y-la-regla-de-dueno-unico.md, todos con nombre NNNN-kebab-case; 0001 marcado como reemplazado por 0002 sin editarse. | Cumple | Los nombres siguen la convención y el ADR reemplazado conserva su contenido con enlace al sustituto. |
| La tabla de aspectos | docs/aspectos.md existe en el árbol, pero no se aporta su contenido para comprobar las ocho columnas y la navegabilidad de cada eslabón. | No verificado | Se esperaba la tabla con ID, Aspecto, Requisito, C4, ADR, Código, Pruebas y Evidencia; el extracto no la incluye. |
| Registro de uso de IA | docs/ia.md existe y su historial muestra nueve commits entre 2026-08-07 y 2026-09-13, pero no se aporta el contenido con lo aceptado y lo rechazado. | No verificado | El archivo crece a lo largo del semestre; falta ver la columna de lo rechazado y su motivo técnico. |
| README | README.md describe el sistema, el arranque con 'docker compose up' y cómo se prueba con pytest (47 pruebas) y flutter test (6 pruebas). | Cumple | Declara requisitos previos (Docker con Compose) y el comando único de arranque. |
| Pipeline y análisis estático | .github/workflows/ci.yml existe, pero no se aportan runs de CI ni URL pública de SonarCloud con Quality Gate para a47d5bd. | No verificado | Se esperaba la línea del workflow que invoca el scanner, la URL del run exitoso y la URL pública del análisis; no se aportó ninguna. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `a47d5bd660abb2d220071430f869e8ee8ee17bd2 2026-09-13T23:21:55-05:00 docs: corregir el estado del C4 y registrar la decision del nombre`
- **Veredicto**: con pendientes
- Resumen: El proyecto avanza en documentación arquitectónica y en el corte vertical A-01, pero en la punta actual de master no existe contrato de API ejecutable ni prueba de contrato en el pipeline, que son el objeto de la semana 7.

Pendientes que siguen abiertos:
- Contrato de API en formato ejecutable versionado en el repositorio.
- Prueba de contrato ejecutada por el pipeline y evidencia de que falla ante un cambio incompatible.
- Evidencia auditable de SonarCloud (workflow, run exitoso y URL pública con Quality Gate).
- Verificación de la tabla de aspectos, el registro de IA, la sección 6 del arc42 y el C4 nivel 2.

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Evidencia de que la prueba de contrato falla ante un cambio incompatible: no hay runs ni evidencia aportada; haría falta un run en rojo o el registro del cambio incompatible.
- arc42 sección 6 con los flujos de interacción: el extracto se corta antes de la sección 6; haría falta el contenido de docs/arc42/06*.
- C4 nivel 2 con protocolo y formato en cada flecha: docs/c4/doc-c4.md no se aporta; haría falta el diagrama con las etiquetas.
- Tabla de aspectos: docs/aspectos.md no se aporta; haría falta su contenido con las ocho columnas.
- Registro de uso de IA: docs/ia.md no se aporta; haría falta el contenido con lo aceptado y lo rechazado.
- Pipeline y análisis estático: sin runs de CI ni URL pública de SonarCloud; haría falta la línea del workflow, el run exitoso y el Quality Gate.

## Hallazgos para la planilla

- No existe archivo de contrato OpenAPI, AsyncAPI ni proto en el commit calificado a47d5bd.
- No hay prueba de contrato en backend/tests/ ni invocación de contrato en .github/workflows/ci.yml.
- No se aporta ningún run de CI ni evidencia de que una prueba de contrato pueda fallar.
- El ADR-0002 justifica la estrategia asíncrona contra EC-03 y EC-04 con alternativas descartadas.
- No se aportan runs de CI ni URL pública de SonarCloud para el hash revisado.
- No hay commits posteriores al cierre en la rama master.
