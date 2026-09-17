# semana-07-evidencia-s7 · DinamikUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `265e652` en `origin/master` (2026-09-13T23:29:49-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol de 265e652 no contiene ningún archivo .yaml/.json de openapi/swagger/asyncapi ni .proto. | No cumple | Se esperaba el contrato ejecutable versionado; no aparece en el listado completo del commit. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | Sin archivo de contrato en 265e652, no hay rutas ni esquemas que citar. | No cumple | No verificable por ausencia total del artefacto. |
| Correspondencia entre el contrato y la API implementada | El código expone routers en backend/app/estudiantes/router.py y backend/app/requisitos/router.py, pero no existe contrato contra el cual contrastarlos. | No cumple | Falta el lado contrato de la comparación en ambos sentidos. |
| Versión de la API declarada y con historial | No hay archivo de contrato, por lo que no existe campo de versión ni historial git del contrato. | No cumple | El comando git log del contrato no puede ejecutarse sin ruta de contrato. |
| Prueba de contrato presente | backend/tests/ solo contiene test_estudiantes.py, test_main.py y test_requisitos.py en 265e652. | No cumple | No hay prueba de contrato (ni dredd, pact, schemathesis ni equivalente) en el árbol. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/ci.yml en el árbol, pero no se aportó su contenido ni runs_ci del commit 265e652. | No verificado | Haría falta la línea del workflow que invoca la prueba y la URL del run; sin prueba de contrato en el repo, no hay nada que invocar. |
| Evidencia de que la prueba falla ante un cambio incompatible | No se aportó run en rojo ni evidencia del cambio incompatible que rompiera la prueba. | No verificado | Queda como pregunta de sustentación según la ficha. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/ contiene 0001-seleccion-monolito-modular, 0002-seleccion-tecnologia-backend-frontend y 0003-seleccion-motor-de-base-de-datos en 265e652. | No cumple | Ninguno decide síncrono vs asíncrono contra un escenario de calidad ni enuncia la alternativa descartada y su acoplamiento. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06-runtime-view.md en 265e652 describe los escenarios 6.1 (consulta de progreso), 6.2 (control de acceso) y 6.3 (corrección de requisito) paso a paso. | Cumple | Los flujos citan los bloques de 05-building-block-view.md y los escenarios Q-01/Q-02/Q-03. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/contenedores.puml existe en el árbol de 265e652, pero no se aportó su contenido. | No verificado | Haría falta el .puml o su render para comprobar que cada flecha lleva protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible:true, repo AS_202620_DinamikUTB en la organización ISCOUTB, rama origin/master en 265e652. | Cumple | Cuatro identidades git consolidadas por autor compartido coinciden con los cuatro integrantes declarados. |
| Estructura mínima | En 265e652 existen docs/arc42/01..12, docs/adr/0001-0003, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Sin desviaciones de ruta; los ADR siguen la convención NNNN-kebab-case. |
| Estado del repositorio calificado | 265e652 con fecha 2026-09-13T23:29:49-05:00 sobre origin/master, anterior al cierre 2026-09-21T05:00:00Z. | Cumple | commits_tardios_post_cierre vacío: la punta revisada es la calificada. |
| Convenciones de ADR | docs/adr/0001-seleccion-monolito-modular.md, 0002-seleccion-tecnologia-backend-frontend.md y 0003-seleccion-motor-de-base-de-datos.md con contexto, opciones, decisión, consecuencias y trazabilidad. | Cumple | Numeración y títulos que enuncian la decisión; los tres están marcados como Aceptado. |
| La tabla de aspectos | docs/aspectos.md existe en el árbol de 265e652, pero no se aportó su contenido. | No verificado | No se puede comprobar las ocho columnas ni que cada eslabón sea navegable. |
| Registro de uso de IA | docs/ia.md existe y acumula 17 commits entre 2026-08-09 y 2026-09-13, sin contenido aportado. | No verificado | Falta ver la columna de lo rechazado y su motivo técnico. |
| README | README.md en 265e652 declara requisitos previos, comando único start.bat y secciones de pytest, flutter test y flutter analyze. | Cumple | Documenta arranque y prueba con un solo comando desde la raíz. |
| Pipeline y análisis estático | Existen .github/workflows/ci.yml y sonar-project.properties en 265e652, pero sin contenido de workflow, sin runs_ci y sin URL pública de SonarCloud. | No verificado | Faltan las tres evidencias exigidas: línea del scanner, run exitoso y análisis con Quality Gate. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `265e652bb3c34c6b90d6d8c1e70db4d75e20a18e 2026-09-13T23:29:49-05:00 Create proguard-rules.pro`
- **Veredicto**: con pendientes
- Resumen: En la punta 265e652 de origin/master (2026-09-13, anterior al cierre 2026-09-21) el proyecto sostiene su base documental y de pruebas unitarias, pero la entrega de la semana 7 no está: no hay contrato ejecutable, ni prueba de contrato, ni ADR de integración, y la evidencia de SonarCloud no es auditable.

Pendientes que siguen abiertos:
- Contrato OpenAPI/AsyncAPI/proto versionado con rutas y esquemas
- Prueba de contrato integrada al pipeline
- Demostración de que la prueba de contrato falla ante cambio incompatible
- ADR de estrategia de integración (síncrono vs asíncrono)
- Etiquetado de protocolo y formato en el C4 nivel 2
- Contenido verificable de docs/aspectos.md y docs/ia.md
- Evidencia pública del análisis estático con Quality Gate

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- El pipeline ejecuta la prueba de contrato: no se aportó .github/workflows/ci.yml ni runs_ci; se requiere la línea del workflow y la URL del run.
- Evidencia de que la prueba falla ante cambio incompatible: no hay run en rojo ni registro del cambio; queda como pregunta de sustentación.
- C4 nivel 2 con protocolo y formato en cada flecha: solo consta docs/c4/contenedores.puml; hace falta su contenido o render.
- Tabla de aspectos: hace falta el contenido de docs/aspectos.md para verificar las ocho columnas navegables.
- Registro de uso de IA: hace falta el contenido de docs/ia.md, en especial lo rechazado y su motivo.
- Pipeline y análisis estático: faltan la línea del scanner en el workflow, la URL del run exitoso y la URL pública del análisis con Quality Gate.

## Hallazgos para la planilla

- No existe archivo OpenAPI, AsyncAPI ni proto en 265e652.
- No hay ADR de estrategia de integración; solo estilo, stack y motor de datos.
- No existe prueba de contrato en backend/tests ni evidencia de invocación desde el pipeline.
- Sin run en rojo ni cambio incompatible documentado: la prueba no puede demostrar que falla.
- docs/aspectos.md y docs/ia.md existen pero su contenido no fue aportado.
- Sin secretos ni .env versionados en HEAD.
- Cuatro identidades git consolidadas coinciden con los cuatro integrantes declarados.
- La entrega se subió antes del cierre (2026-09-13 vs cierre 2026-09-21) y no hay commits posteriores.
