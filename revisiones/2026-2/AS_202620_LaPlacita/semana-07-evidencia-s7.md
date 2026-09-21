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
| Contrato en formato ejecutable versionado en el repositorio | openapi.yaml en la raíz del repo; docs/adr/0008 lo describe como OpenAPI 3.1 v1 con 10 paths. | Cumple | No se incluyó el contenido del archivo en el volcado. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | No se aporta fragmento de openapi.yaml; ADR-0008 menciona esquemas de request/response pero no se citan. | No verificado | Se esperaba fragmento con paths y schemas. |
| Correspondencia entre el contrato y la API implementada | Código tiene app/api/v1/*; ADR-0008 afirma 10 paths en openapi.yaml, pero no se lista el contrato. | No verificado | No se pudo contrastar dos rutas del contrato en código y una del código en contrato. |
| Versión de la API declarada y con historial | ADR-0008 declara v1; no se aporta git log de openapi.yaml. | No verificado | Historial no verificable con el volcado. |
| Prueba de contrato presente | tests/contract-openapi.test.js en el árbol del repo. | Cumple | No se evalúa su contenido. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/ci.yml y ADR-0008 menciona job contract-test, pero no hay runs_ci ni línea citada. | No verificado | Se esperaba URL del run y línea del workflow. |
| Evidencia de que la prueba falla ante un cambio incompatible | Existe docs/evidencia-fallo-contrato-s7.md; no se aporta su contenido ni run en rojo. | No verificado | Se esperaba run fallido o evidencia reproducible del cambio incompatible. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0006-estrategia-integracion-sincrona.md con ESC-01..05, alternativas descartadas y consecuencias; ratificado por ADR-0008. | Cumple | ADR-0006 queda propuesto y ADR-0008 lo acepta. |
| arc42 sección 6 con los flujos de interacción | El volcado de docs/arc42/arc42-template-EN.md solo muestra hasta §4.4; no se observa §6. | No verificado | Se esperaba la sección 6 con flujos. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/contenedores.md etiqueta flechas con HTTPS/REST API, HTTP REST/JSON, HTTPS/JSON. | Cumple | Cumple con etiquetado de protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_LaPlacita, visible=true; autores consolidan 4 identidades: Jorge M. Castillo, samulssl, Isaza927/isaza927, matbuendia. | Cumple | Isaza927 e isaza927 comparten correo, pero no se publica; no se atribuye por parecido de nombre. |
| Estructura mínima | Árbol incluye README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md. | Cumple | arc42 está en inglés y como template; estructura presente. |
| Estado del repositorio que se califica | origin/master HEAD 8c2e1bc, fecha 2026-09-20T22:47:32-05:00, anterior al cierre 2026-09-21T05:00:00Z. | Cumple | Sin commits post cierre en la rama. |
| Convenciones de ADR | docs/adr/0001..0008 con nombres kebab-case y campos de contexto, opciones, decisión, consecuencias y trazabilidad. | Cumple | No se aporta git log para verificar inmutabilidad; ADR-0007 menciona sección extraída de ADR-0005. |
| Tabla de aspectos | docs/aspectos.md tiene filas A-03..A-06 con requisito sin enlace y columna extra 'Escenarios' frente a las ocho columnas del contrato. | No cumple | Celdas no navegables y columna adicional. |
| Registro de uso de IA | docs/ia.md existe y tiene 20 commits; no se aporta su contenido. | No verificado | No se puede verificar qué se aceptó y qué se rechazó. |
| README | README.md existe y documenta arranque y pruebas, pero el volcado está truncado. | No verificado | No se evidencia un solo comando de arranque. |
| Pipeline y análisis estático | sonar-project.properties existe, pero ADR-0003 dice 'análisis en vivo pendiente de SONAR_TOKEN'; no hay run URL ni URL SonarCloud con Quality Gate. | No cumple | Faltan las tres evidencias exigidas. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `8c2e1bc4a22fae593de776d7e9469ffb29c10a08 2026-09-20T22:47:32-05:00 Organización del repositorio de acuerdo a la nueva documentación complementaria`
- **Veredicto**: con pendientes
- Resumen: Proyecto en master 8c2e1bc sin commits post cierre. Cumple 4/10 de la ficha y 4/8 transversal. Faltan evidencias de ejecución de contrato, fallo de prueba, sección 6 de arc42, SonarCloud y enlaces de aspectos; persiste deuda de semanas previas.

Pendientes que siguen abiertos:
- V-02 ACL Pedidos→Catálogo
- V-04 Shared Kernel tiendaId
- V-05 OHS evento notificaciones
- V-06 orquestador
- SonarCloud token y análisis
- Sección 6 arc42
- Evidencia de fallo de contrato
- Enlaces tabla aspectos

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido del openapi.yaml (schemas y rutas).
- Correspondencia ruta a ruta entre contrato y código.
- Historial git del archivo de contrato.
- Ejecución del job contract-test en CI y URL del run.
- Evidencia de fallo de la prueba de contrato (run en rojo o contenido de docs/evidencia-fallo-contrato-s7.md).
- Sección 6 de arc42.
- Contenido de docs/ia.md.
- Comando único de arranque en README.
- URL pública de SonarCloud y estado del Quality Gate.

## Hallazgos para la planilla

- El contrato openapi.yaml existe pero no se aportó su contenido para verificar esquemas ni rutas.
- No hay runs_ci que demuestren la ejecución del job de contrato ni el análisis de SonarCloud.
- La prueba de contrato no tiene evidencia verificable de fallo ante cambio incompatible.
- La tabla de aspectos presenta requisitos sin enlace en A-03..A-06 y una columna extra.
- No hay commits posteriores al cierre S7 en origin/master.
- La sección 6 de arc42 no se observa en el volcado.
- ADR-0003 indica que SonarCloud sigue pendiente del token SONAR_TOKEN.
- La deuda V-02, V-04, V-05 y V-06 permanece abierta para Corte 2.
