# semana-07-evidencia-s7 · ElMapita

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `a22f0a4` en `origin/main` (2026-09-13T22:21:07-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Búsqueda en el árbol de a22f0a4 (git ls-tree -r --name-only HEAD): sin coincidencias para openapi\|swagger\|asyncapi.*.(ya?ml\|json)\|.proto. | No cumple | Se esperaba la ruta de un archivo de contrato versionado y no existe ninguno. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No hay archivo de contrato que citar en el árbol de a22f0a4, por lo que no hay rutas ni schemas que inspeccionar. | No cumple | Ausencia reproducible: la lista completa del árbol no incluye ningún artefacto de contrato. |
| Correspondencia entre el contrato y la API implementada | Sin contrato no se pueden localizar rutas del contrato en backend/src/modules/*/interfaces/*.controller.ts ni comprobar una ruta del código dentro del contrato. | No cumple | Faltan las dos rutas del contrato en el código y una ruta del código en el contrato. |
| Versión de la API declarada y con historial | No existe archivo de contrato, así que no hay campo de versión ni salida aplicable de git log -- <ruta del contrato>. | No cumple | Se esperaba el campo de versión en el contrato y su historial en git. |
| Prueba de contrato presente | El árbol de a22f0a4 solo tiene backend/test/app.e2e-spec.ts, backend/src/app.controller.spec.ts y frontend/test/widget_test.dart; ningún archivo de prueba de contrato. | No cumple | No aparece ninguna prueba tipo pact, dredd, schemathesis, prism o spectral. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/ci.yml, pero no se aportó su contenido ni runs_ci con nombre, conclusión y URL. | No verificado | Haría falta grep -niE 'contract\|dredd\|schemathesis\|pact\|prism\|spectral\|openapi' .github/workflows/ y la URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | No hay runs_ci en la evidencia aportada y el equipo no adjuntó la prueba del cambio incompatible que rompiera el contrato. | No verificado | Queda como pregunta de sustentación: sin run en rojo no se demuestra que la prueba sirva. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0001-estilo-arquitectonico-propuesto.md decide el estilo arquitectónico y docs/adr/0002-restriccion-rendimiento-compatibilidad-dispositivos.md el rendimiento; ninguno elige síncrono o asíncrono contra un escenario de calidad. | No cumple | Falta la alternativa de integración descartada y sus consecuencias de acoplamiento. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/arc42-template-EN.md existe, pero el contenido aportado llega solo hasta la sección 3 (contexto y alcance). | No verificado | Haría falta citar la sección 6 (ruta:línea) con los flujos de interacción descritos. |
| C4 nivel 2 con protocolo y formato en cada flecha | Existen docs/c4/C4_L2_Container.md y docs/c4/C4_L2_Container.png, pero no se aportó el diagrama ni su código para leer las etiquetas. | No verificado | Comprobar que cada flecha indica protocolo (HTTP, gRPC, SQL…) y formato (JSON, GLB…). |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo público AS_202620_ElMapita sobre origin/main, hash a22f0a4, nombre conforme a AS_202620_<PROYECTO>. | Cumple | El historial muestra 3 cuentas (RobotDRMX, Rodrigo Vazquez Rico, dgarza2705); no se atribuyen a personas por parecido de nombre. |
| Estructura mínima | El árbol de a22f0a4 incluye docs/adr/, docs/c4/, docs/arc42/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Desviaciones anotadas: .gitkeep en adr/ y c4/, documentación .docx en docs/ y un archivo temporal de Word versionado. |
| Convenciones de ADR | 0001-estilo-arquitectonico-propuesto.md y 0002-restriccion-rendimiento-compatibilidad-dispositivos.md cumplen ^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*.md$ y declaran status: Accepted. | Cumple | No se aportó git log --follow para comprobar que un ADR aceptado no se editó después. |
| Tabla de aspectos | docs/aspectos.md aparece en el árbol, pero su contenido no se incluyó en la evidencia enviada. | No verificado | Haría falta citar filas con ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia navegables. |
| Registro de uso de IA | docs/ia.md cambia en 6 commits (df1e2f7 2026-08-07 hasta a22f0a4 2026-09-13), pero no se aportó su contenido. | No verificado | Falta citar qué se rechazó y por qué, que es la columna que se revisa primero. |
| README | README.md declara qué es el sistema, prerrequisitos, arranque con scripts/dev.sh y scripts/dev.ps1 y los comandos de prueba. | Cumple | El arranque unificado exige copiar backend/.env.example a backend/.env antes de ejecutarlo. |
| Pipeline y análisis estático | Existe .github/workflows/ci.yml, pero no hay sonar-project.properties en el árbol a22f0a4 ni URL de run ni URL pública de SonarCloud con Quality Gate. | No cumple | Faltan las tres evidencias exigidas; tampoco se aportó runs_ci para verificar la ejecución de pruebas. |
| Secretos | El grep sobre a22f0a4 solo devuelve nombres de parámetros (password, token, refresh_token) y la URL de badge de ejemplo del README de NestJS; envs_versionados está vacío. | Cumple | Sin claves privadas ni .env versionado; conviene limpiar el token de ejemplo de backend/README.md para evitar ruido. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `a22f0a43f2e93730d9df5d112f03687854639ea7 2026-09-13T22:21:07-05:00 docs(ia): actualizar registro de uso de IA`
- **Veredicto**: con pendientes
- Resumen: En la punta de origin/main (a22f0a4, 2026-09-13) el proyecto no tiene contrato de API ni prueba de contrato, y tampoco son verificables el pipeline ni SonarCloud; la entrega S7 queda sin resolver y no hay commits posteriores que la corrijan.

Pendientes que siguen abiertos:
- Contrato OpenAPI/AsyncAPI/proto versionado, con rutas, esquemas y versión
- Prueba de contrato presente y ejecutada desde el workflow
- Evidencia de que la prueba falla ante un cambio incompatible
- ADR de estrategia de integración síncrona o asíncrona con alternativa descartada
- arc42 sección 6 con los flujos de interacción
- C4 nivel 2 con protocolo y formato en cada flecha
- Contenido defendible de docs/aspectos.md y docs/ia.md
- Runs de CI y análisis público de SonarCloud con estado del Quality Gate

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución de la prueba de contrato en el pipeline: falta el contenido de .github/workflows/ci.yml y la URL del run (comando: grep -niE 'contract|dredd|schemathesis|pact|prism|spectral|openapi' .github/workflows/).
- Prueba que falla ante cambio incompatible: sin runs_ci y sin evidencia aportada por el equipo (comando: curl -s https://api.github.com/repos/ISCOUTB/AS_202620_ElMapita/actions/runs?per_page=50).
- arc42 sección 6 con flujos de interacción: el contenido aportado corta en la sección 3; falta citar ruta:línea.
- C4 nivel 2 con protocolo y formato por flecha: existen los archivos, pero no se aportó el diagrama ni su código.
- Contenido de docs/aspectos.md y docs/ia.md: aparecen en el árbol pero no se incluyó su texto.

## Hallazgos para la planilla

- No existe ningún archivo OpenAPI, AsyncAPI o proto en el árbol de a22f0a4.
- No hay prueba de contrato ni evidencia de un run en rojo que demuestre que falla.
- Los ADR 0001 y 0002 cubren estilo arquitectónico y rendimiento, no la estrategia de integración.
- No se aportaron runs_ci, diff_desde_cierre ni URL pública de SonarCloud.
- Se versiona un archivo temporal de Word: docs/~$blaModulos_ElMapitaUTB.docx.
- La documentación de arquitectura aparece también en .docx (CorteVertical, TablaModulos) además del Markdown.
- El registro de IA crece a lo largo del semestre, pero su contenido no es verificable con lo aportado.
- Las coincidencias del grep de secretos son nombres de parámetros y un token de badge de ejemplo.
