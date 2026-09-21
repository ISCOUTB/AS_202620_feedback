# semana-07-evidencia-s7 · XALD

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `62a0d15` en `origin/master` (2026-09-20T23:25:16-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/openapi.yaml (openapi: 3.1.0) presente en el árbol del commit 62a0d15 (2026-09-20T23:25:16-05:00). | Cumple | Es especificación ejecutable, no prosa; se complementa con docs/api/contrato.md. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | docs/api/openapi.yaml: paths /transacciones (POST) con requestBody $ref TransaccionDTO y responses 202/400 con RespuestaSincronizacion; components.schemas TransaccionDTO (7 campos required tipados), RespuestaSincronizacion y OrigenDatosEnum. | Cumple | Los esquemas incluyen tipos, formatos, longitudes y valores de ejemplo. |
| Correspondencia entre el contrato y la API implementada | docs/api/contrato.md §3 (matriz Contrato↔Código): POST /api/v1/transacciones ↔ @app.post en backend/app/main.py; TransaccionDTO, RespuestaSincronizacion y OrigenDatosEnum ↔ backend/app/dtos.py (commit 62a0d15). | Cumple | El contrato declara un solo endpoint; la correspondencia se apoya en la matriz del propio equipo y no se contrastó línea a línea main.py/dtos.py, que no vienen en la evidencia. |
| Versión de la API declarada y con historial | docs/api/openapi.yaml info.version 1.0.0; git log del archivo en commits_nuevos_desde_cierre_anterior: b7ca7f7 (2026-09-20T23:03) y 73de849 (2026-09-20T23:18) 'Update openapi.yaml'; historial v1.0.0 (2026-09) en docs/api/contrato.md §4. | Cumple | Historial corto y concentrado en el día del cierre. |
| Prueba de contrato presente | Se revisó el árbol completo de 62a0d15 y no aparece archivo de prueba de contrato (sin coincidencias de contract/pact/dredd/schemathesis); docs/api/contrato.md §4 y §6 mencionan validación con @redocly/cli dentro de GitHub Actions. | No verificado | Hace falta el contenido de .github/workflows/ci.yml para saber si la validación vive solo como comando del workflow; se esperaba una ruta de prueba versionada. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/ci.yml en el árbol de 62a0d15, pero no se aporta su contenido ni runs_ci; docs/api/contrato.md §6 cita un run en Actions que no es auditable desde el informe. | No verificado | Comando a repetir: grep -rniE 'contract\|dredd\|schemathesis\|pact\|prism\|spectral\|openapi\|redocly' .github/workflows/ y citar nombre, conclusion y URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | docs/api/contrato.md §7: captura del CI en rojo tras cambiar el tipo de entrada de los DTOs y texto que describe el experimento (commit 62a0d15). | Cumple | La evidencia es una captura embebida (user-attachments), no auditable desde el informe y sin run en rojo citado; queda como pregunta de sustentación. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0007-contratos-por-modulo.md: opciones evaluadas (comunicación directa vs contratos con orquestación centralizada), decisión síncrona por interfaces públicas, riesgo de acoplamiento de :app y su mitigación. | Cumple | No enlaza explícitamente ningún ESC de la sección 10; su justificación se apoya en la auditoría de la semana 6 y en docs/aspectos.md. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06-Runtime view.md: escenarios 6.1 a 6.4 con pasos numerados y diagramas de secuencia Mermaid (ESC-01, ESC-02, ESC-05, ESC-03), actualizada en 62a0d15. | Cumple | El archivo contiene texto de instrucciones de copia/pegar y aparece truncado; conviene limpiarlo. |
| C4 nivel 2 con protocolo y formato en cada flecha | Solo se dispone de la ruta docs/c4/c2.md en el árbol de 62a0d15; su contenido no viene en la evidencia. | No verificado | Se esperaba el diagrama de contenedores con cada flecha etiquetada con protocolo y formato; hace falta el contenido del C2 para comprobarlo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_XALD público ('visible': true); historial con cuatro cuentas (186, 83, 54 y 38 commits), mismo número que los cuatro integrantes declarados. | Cumple | No se atribuyen cuentas a personas por parecido de nombre; el acrónimo del repo corresponde al proyecto XALD. |
| Estructura mínima | En 62a0d15: README.md, docs/arc42/01..12, docs/adr/0001..0007, docs/c4/c1..c4, docs/aspectos.md y docs/ia.md. | Cumple | docs/arc42/07-Deployment View.md está vacío, así que la estructura existe pero esa sección no está desarrollada. |
| Convenciones de ADR | docs/adr/0001..0007 con nombres NNNN-titulo-en-kebab-case.md; ADR-0007 incluye contexto, opciones evaluadas, decisión, consecuencias y trazabilidad (commit 62a0d15). | Cumple | ADR-0005 declara estatus APROBADA pero su propia trazabilidad dice 'en revisión'. |
| La tabla de aspectos | docs/aspectos.md existe y fue actualizada en fcf0089 (2026-09-20T22:52), pero su contenido no viene en la evidencia. | No verificado | Hace falta el archivo para verificar las ocho columnas (ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia) y que ninguna celda quede hueca. |
| Registro de uso de IA | docs/ia.md con 13 entradas de historial entre 2026-08-07 y 2026-09-20 (último c450b4f), pero sin contenido en la evidencia. | No verificado | Hace falta el archivo para comprobar qué se rechazó y con qué motivo técnico. |
| README | README.md declara qué es el sistema, requisitos previos (JDK 17, Android SDK), comando único de pruebas (.\XALDAPP\gradlew.bat -p XALDAPP test) y salida esperada. | Cumple | El arranque exige exportar JAVA_HOME y ANDROID_HOME manualmente y la evidencia de ejecución es una captura. |
| Pipeline y análisis estático | Existe .github/workflows/ci.yml pero sin contenido; no hay runs_ci; no hay sonar-project.properties en el árbol; docs/api/contrato.md §6 enlaza a un run de GitHub y no a una URL de sonarcloud.io. | No verificado | Faltan las tres evidencias que exige el contrato (configuración, línea del workflow que invoca el scanner, run exitoso y URL pública del análisis con Quality Gate). |
| Secretos | Búsqueda de patrones de credenciales en HEAD sin coincidencias, sin .env versionados y sin claves privadas en el historial. | Cumple | Sí se versionan archivos backend/app/__pycache__/*.pyc: es higiene del repositorio, no un secreto. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `62a0d1540c9f4ae9d4df611b3a20286e8d7c1a76 2026-09-20T23:25:16-05:00 Update 06-Runtime view.md`
- **Veredicto**: con pendientes
- Resumen: A HEAD de la rama principal (62a0d15, origin/master, 2026-09-20T23:25:16-05:00, anterior al cierre) el proyecto aporta contrato OpenAPI 3.1.0 ejecutable, ADRs, arc42 1-12, C4 y ausencia de secretos; quedan pendientes la prueba de contrato versionada y ejecutada con run citable, la evidencia auditable de SonarCloud, la verificación del C2, de aspectos.md y de ia.md, y la sección 7 de arc42 vacía.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- c450b4f 2026-09-20T22:40:25-05:00 Update ia.md
- fcf0089 2026-09-20T22:52:52-05:00 Update aspectos.md
- b7ca7f7 2026-09-20T23:03:41-05:00 y 73de849 2026-09-20T23:18:48-05:00 Update openapi.yaml
- 62a0d15 2026-09-20T23:25:16-05:00 Update 06-Runtime view.md

Pendientes que siguen abiertos:
- Prueba de contrato no localizada ni invocada con evidencia de run
- SonarCloud sin las tres evidencias auditables
- docs/arc42/07-Deployment View.md vacío
- docs/c4/c2.md sin verificar protocolo y formato en cada flecha
- docs/aspectos.md y docs/ia.md sin contenido verificable
- ADR-0005 con estatus inconsistente entre encabezado y trazabilidad
- Archivos __pycache__ (.pyc) versionados

## Recuento y nota sugerida

7 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Prueba de contrato: no se localizó su ruta en el árbol; falta el contenido de .github/workflows/ci.yml.
- Ejecución del pipeline sobre el contrato: sin runs_ci; comando anotado: grep -rniE 'contract|dredd|schemathesis|pact|prism|spectral|openapi|redocly' .github/workflows/.
- C4 nivel 2: falta el contenido de docs/c4/c2.md para verificar protocolo y formato en cada flecha.
- Tabla de aspectos: falta el contenido de docs/aspectos.md.
- Registro de uso de IA: falta el contenido de docs/ia.md para revisar lo rechazado.
- SonarCloud: faltan archivo de configuración, línea del workflow, run exitoso y URL pública con Quality Gate.

## Hallazgos para la planilla

- El contrato OpenAPI 3.1.0 está versionado, con versión declarada y esquemas completos, y alineado 1:1 con el único endpoint del backend.
- No se localizó archivo de prueba de contrato en el árbol; la validación parece vivir solo en el workflow, cuyo contenido no se aportó.
- La evidencia de que la prueba falla es una captura embebida, sin run en rojo citable ni commit del cambio incompatible.
- No hay evidencia auditable de SonarCloud: falta configuración y URL pública de análisis, y el enlace citado no apunta a sonarcloud.io.
- docs/arc42/07-Deployment View.md está vacío.
- docs/arc42/06-Runtime view.md contiene instrucciones de copia/pegar y aparece truncado.
- Se versionan archivos __pycache__ (.pyc) en backend/app/.
- Cinco commits el día del cierre (2026-09-20), ninguno posterior al cierre.
- ADR-0007 documenta la corrección de las siete violaciones de la auditoría de la semana 6 con una prueba anti-regresión.
