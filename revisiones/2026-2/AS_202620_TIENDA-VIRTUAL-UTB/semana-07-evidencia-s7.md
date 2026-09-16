# semana-07-evidencia-s7 · Tienda virtual UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `dea5bc9` en `origin/main` (2026-09-15T09:52:53-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol de dea5bc9 truncado: solo se listan .dockerignore, .github/workflows/tests.yml, .gitignore y .security-tools/… hasta fastapi/dependencies/models.py. | No verificado | Se esperaba una ruta openapi/asyncapi/proto; el listado recibido no permite ver docs/ ni la raíz, así que no se confirma presencia ni ausencia (haría falta `git ls-tree -r --name-only HEAD`). |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No se aporta fragmento del contrato ni archivo de especificación en el árbol visible de dea5bc9. | No verificado | Sin el archivo abierto no se puede comprobar versión de especificación, paths ni schemas de respuesta. |
| Correspondencia entre el contrato y la API implementada | No hay en la evidencia rutas del contrato ni rutas del código (el árbol entregado es casi todo .security-tools/…). | No verificado | Se necesitan dos rutas del contrato localizadas en el código y una ruta del código presente en el contrato. |
| Versión de la API declarada y con historial | Sin ruta de contrato no se puede ejecutar `git log --format='%h %cI %s' -- <ruta>` sobre dea5bc9. | No verificado | Falta el campo de versión (info.version o versión en la ruta) y su historial de cambios. |
| Prueba de contrato presente | El árbol visible de dea5bc9 no muestra rutas de tests propias; solo .github/workflows/tests.yml. | No verificado | Árbol truncado: se esperaba algo tipo tests/contract/… o *contract*test*; buscar con `ls-tree` completo y grep de contract\|dredd\|schemathesis\|pact\|prism\|spectral. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/tests.yml, pero no se aporta su contenido ni ningún run de CI (runs_ci ausente en la evidencia). | No verificado | Se esperaba la línea del workflow que invoca la prueba y la URL del run; sin runs ni contenido del YAML no se puede afirmar ejecución. |
| Evidencia de que la prueba falla ante un cambio incompatible | No hay runs en la evidencia ni documento del equipo con el cambio incompatible que rompió el contrato. | No verificado | Criterio decisivo competente/sobresaliente; queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | No se ve docs/adr/000N-*.md en el árbol de dea5bc9 (listado truncado). | No verificado | Se necesita el ADR con escenario de calidad, alternativa descartada y consecuencias de acoplamiento. |
| arc42 sección 6 con los flujos de interacción | No se ve docs/arc42/06* en el árbol de dea5bc9. | No verificado | Falta comprobar que los flujos de interacción están descritos. |
| C4 nivel 2 con protocolo y formato en cada flecha | No se ve diagrama de nivel 2 en docs/c4/ ni en docs/arc42/ dentro del árbol recibido. | No verificado | Se esperaba cada flecha etiquetada con protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_TIENDA-VIRTUAL-UTB, organización ISCOUTB, "visible": true, hash dea5bc9; historial con 4 cuentas consolidadas (RAZOR7150, pxtroniwnl, Jasen/Jasen Yukopila y shalom-A26). | Cumple | El número de cuentas coincide con los 4 integrantes declarados, pero la pertenencia a la organización no se verifica con esta evidencia. |
| Estructura mínima | El árbol recibido de dea5bc9 está truncado y solo muestra .security-tools/… junto a .github/workflows/tests.yml y .gitignore. | No verificado | Haría falta el listado completo con docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md. |
| Convenciones de ADR | No aparece ningún docs/adr/NNNN-*.md en la porción visible del árbol de dea5bc9. | No verificado | Se requiere `ls docs/adr \| grep -Ev '^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$'` y `git log --follow` por ADR. |
| Tabla de aspectos | No se ve docs/aspectos.md en el árbol recibido. | No verificado | Debe comprobarse la cadena aspecto→requisito→C4→ADR→código→pruebas→evidencia sin celdas huecas. |
| Registro de uso de IA | No se ve docs/ia.md en el árbol recibido, ni su historial en git. | No verificado | Falta la columna de lo rechazado y por qué, que es la que se evalúa. |
| README | README.md no aparece en la porción visible del árbol de dea5bc9 (listado cortado antes de la raíz). | No verificado | Se debe verificar el arranque con un solo comando y los requisitos previos declarados. |
| Pipeline y análisis estático | Solo consta .github/workflows/tests.yml; no hay runs_ci en la evidencia ni línea del scanner de SonarCloud ni URL pública del análisis. | No verificado | Para Cumple harían falta el YAML con el scanner, el run exitoso del hash revisado y el enlace público del Quality Gate en isco-utb. |
| Secretos | El escaneo de dea5bc9 solo devuelve coincidencias dentro de .security-tools/python/Lib/site-packages/… (p. ej. dea5bc9:.security-tools/python/Lib/site-packages/psycopg2/__init__.py:99), todas de dependencias vendorizadas. | Cumple | No se hallan credenciales ni .env en código propio; conviene retirar el entorno Python completo del repositorio por ruido en todos los escaneos. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `dea5bc9590612d894c9c68a06c72cfb57efcdb9a 2026-09-15T09:52:53-05:00 s7 borrador`
- **Veredicto**: con pendientes
- Resumen: En la punta de origin/main (dea5bc9, 2026-09-15) solo es verificable la identidad del repositorio y la ausencia de credenciales en código propio; contrato, prueba de contrato, ADR, documentación y CI/SonarCloud no son comprobables con la evidencia aportada porque el árbol llega truncado y no hay runs.

Pendientes que siguen abiertos:
- Contrato ejecutable con rutas y esquemas, versionado e historial
- Prueba de contrato y su invocación desde el workflow, con URL del run
- Evidencia de que la prueba falla ante un cambio incompatible
- ADR de estrategia de integración con alternativa descartada
- arc42 sección 6 y C4 nivel 2 con protocolo y formato por flecha
- Evidence de SonarCloud: configuración, run del scanner y Quality Gate público
- Listado completo de archivos y retiro del entorno Python vendorizado

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contrato ejecutable versionado: falta lista completa de archivos (openapi/swagger/asyncapi/proto) en HEAD.
- Rutas y esquemas del contrato: falta el contenido del archivo de especificación.
- Correspondencia contrato↔API: faltan rutas citadas en ambos sentidos.
- Versión de la API e historial: falta el campo de versión y `git log` del archivo.
- Prueba de contrato: falta su ruta en el árbol completo.
- Ejecución de la prueba en el pipeline: falta contenido de .github/workflows/tests.yml y la URL del run.
- Fallo de la prueba ante cambio incompatible: faltan run en rojo o evidencia del equipo.
- ADR de integración: falta docs/adr/000N-*.md con alternativa descartada.
- arc42 sección 6: falta docs/arc42/06*.
- C4 nivel 2: falta el diagrama con protocolo y formato por flecha.
- Estructura mínima, aspectos, IA y README: el árbol recibido no llega a esas rutas.
- SonarCloud: faltan configuración, run del scanner y URL pública del Quality Gate.

## Hallazgos para la planilla

- El repositorio versiona un entorno Python completo en .security-tools/… (miles de archivos), lo que contamina cualquier grep de contrato, pruebas o secretos.
- El árbol de dea5bc9 entregado está truncado, de modo que docs/, la raíz y cualquier archivo OpenAPI quedan fuera de la evidencia.
- No se aporta ningún run de CI (runs_ci ausente): no se puede citar workflow, conclusión ni URL.
- Las 4 cuentas del historial consolidan a 4 contribuyentes, coherente en número con los integrantes declarados; la adscripción a la organización no es verificable aquí.
- El commit evaluado es del 2026-09-15, anterior al cierre del 2026-09-21, en modo early.
