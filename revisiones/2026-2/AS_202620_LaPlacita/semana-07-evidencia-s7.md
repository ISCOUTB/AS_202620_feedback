# semana-07-evidencia-s7 · LaPlacita

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `2c0eb01` en `origin/master` (2026-09-13T21:28:00-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | Árbol de 2c0eb01 (2026-09-13): no aparece ningún archivo openapi/swagger/asyncapi .yaml/.json ni .proto. | No cumple | Se esperaba ruta de contrato versionada; se buscó en ls-tree de HEAD y no existe. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | Sin archivo de contrato en 2c0eb01; no hay fragmento de paths/components que citar. | No cumple | Al no existir contrato no hay rutas ni esquemas de respuesta que verificar. |
| Correspondencia entre el contrato y la API implementada | Módulos en src/modules/* y app/health/route.js (GET /health) sin contraparte documentada en contrato. | No cumple | No se puede cotejar 2 rutas del contrato contra código porque el contrato no existe. |
| Versión de la API declarada y con historial | No hay archivo de contrato en 2c0eb01; no hay campo de versión ni git log del contrato. | No cumple | Se esperaba versión declarada e historial git del archivo de contrato. |
| Prueba de contrato presente | tests/ solo contiene health, modulos, corte-vertical y aislamiento; sin prueba de contrato. | No cumple | No hay prueba de contrato ni dependencia dredd/schemathesis/pact/prism en el árbol. |
| El pipeline ejecuta la prueba de contrato | .github/workflows/ci.yml es el único workflow; sin comando de contrato ni URL de run que lo ejecute. | No cumple | Se esperaba invocación en ci.yml (dredd/schemathesis/pact/prism/spectral) y URL del run. |
| Evidencia de que la prueba falla ante un cambio incompatible | No hay run en rojo de contrato ni evidencia aportada en el repositorio. | No verificado | Haría falta un run con la prueba de contrato fallando o evidencia del cambio incompatible. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0001 a 0005 tratan estilo monolito, despliegue, aislamiento y contextos; ninguno compara integración síncrona vs asíncrona contra un escenario. | No cumple | Se esperaba ADR con alternativa descartada y consecuencias de acoplamiento. |
| arc42 sección 6 con los flujos de interacción | El extracto de docs/arc42/arc42-template-EN.md (2c0eb01) se corta en §4.4. | No verificado | No hay líneas citables de §6; haría falta el archivo completo con 6.1-6.3. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/c4/contenedores.md (2c0eb01): flechas 'HTTPS / JSON', 'HTTPS / REST API', 'ORM / TCP', 'RESP / TCP', 'JSON / HTTPS', 'Push / HTTPS'. | Cumple | Cada relación del nivel 2 lleva protocolo y formato. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible=true, repo ISCOUTB/AS_202620_LaPlacita público; autores consolidados en 4 cuentas (Jorge M. Castillo; samulssl; Isaza927/isaza927; matbuendia) coincidentes con los 4 integrantes declarados. | Cumple | Isaza927 e isaza927 son la misma cuenta visible; matbuendia firma con dos correos distintos. |
| Estructura mínima | Árbol 2c0eb01: docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md. | Cumple | arc42 vive en un solo Markdown (arc42-template-EN.md), desviación menor registrada. |
| Convenciones de ADR | docs/adr/0005-reajuste-contextos-propiedad.md (aceptado 2026-09-13) contiene '## Actualización (13/09/2026)' que edita el contenido tras la aceptación. | No cumple | El contrato exige escribir otro ADR y marcar el anterior como reemplazado, no editarlo. |
| La tabla de aspectos | docs/aspectos.md con 6 filas A-01..A-06 y columnas ID/Aspecto/Requisito/Escenarios/C4/ADR/Código/Pruebas/Evidencia con enlaces navegables. | Cumple | Sin filas huérfanas; A-03 sin escenario propio enlazado. |
| Registro de uso de IA | docs/ia.md con columna 'Rechazado' y motivos técnicos (p. ej. rechazo de ampliar el C4); 18 entradas en git log hasta 2026-09-13. | Cumple | El registro crece a lo largo del semestre. |
| README | El extracto del README (2c0eb01) se corta antes de 'Cómo ejecutar' y 'Guía paso a paso'. | No verificado | No se citan el comando único de arranque ni los requisitos previos exigidos. |
| Pipeline y análisis estático | Existen .github/workflows/ci.yml y sonar-project.properties, pero no hay run del scanner ni URL pública de SonarCloud con Quality Gate; README y ADR-0003 lo declaran pendiente de SONAR_TOKEN. | No cumple | Faltan las tres evidencias exigidas: invocación, run exitoso para el hash y URL pública del análisis. |
| Secretos | Revisión de 2c0eb01: 'secretos: (sin coincidencias)' y 'envs_versionados: []'. | Cumple | Sin credenciales ni .env versionado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `2c0eb0127e0405a61b482c388677b319e219d741 2026-09-13T21:28:00-05:00 se actualiza propiedad-de-datos post V-01/V-03`
- **Veredicto**: con pendientes
- Resumen: Commit vigente 2c0eb01 (2026-09-13), anterior al cierre y sin commits posteriores; el proyecto mantiene pipeline, pruebas y documentación base, pero los entregables de la semana 7 (contrato, prueba de contrato y ADR de integración) no están y SonarCloud sigue sin evidencia pública de ejecución.

Pendientes que siguen abiertos:
- Contrato de API en formato ejecutable versionado
- Prueba de contrato invocada por el pipeline
- Evidencia de fallo de la prueba de contrato ante cambio incompatible
- ADR de estrategia de integración (síncrona o asíncrona) contra escenario
- arc42 §6 verificable en el archivo completo
- SonarCloud: invocación en workflow, run exitoso del hash y URL pública con Quality Gate
- Deuda de propiedad V-02, V-04, V-05 y V-06 (corte 2)
- Vista única del arc42 como plantilla, revisar separación por secciones

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Fallo de la prueba de contrato ante cambio incompatible: sin run en rojo ni evidencia aportada
- arc42 §6 flujos de interacción: extracto cortado en §4.4
- README: no se ve el comando único de arranque ni requisitos previos

## Hallazgos para la planilla

- No existe contrato OpenAPI/AsyncAPI/proto en el árbol del commit revisado
- No hay prueba de contrato ni invocación de contrato en el pipeline
- El ADR de integración síncrona/ascíncrona no está presente
- arc42 §6 no es verificable con el extracto disponible
- SonarCloud sigue sin evidencia pública de ejecución
- V-01 y V-03 fueron implementados el 13/09, deuda de S6 resuelta
- Residuo de deuda V-02, V-04, V-05 y V-06 declarada para corte 2
