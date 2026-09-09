# semana-03-evidencia-s3 · Clubs UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `5bf86ea` (2026-08-23T23:05:10-05:00) |
| Cierre | 2026-08-24T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | docs/arc42/04_estrategia_de_solucion.md en commit 5bf86ea | Cumple | Explica la estrategia hexagonal ligada a la disponibilidad y menciona tácticas específicas para los escenarios. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | docs/arc42/matriz_comparativa_estilos.md en commit 5bf86ea | Cumple | Compara capas, monolito modular y hexagonal contra los escenarios U1-U3 y C1-C3. |
| docs/adr/0001-*.md con el nombre de la convención | docs/adr/0001-hexagonal.md en commit 5bf86ea | Cumple | Existe el archivo ADR, aunque el nombre no es kebab-case estricto. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | docs/adr/0001-hexagonal.md en commit 5bf86ea | Cumple | Contiene secciones de Contexto, Alternativas, Decisión y Consecuencias. |
| Alternativas descartadas con su motivo | docs/adr/0001-hexagonal.md apartado Alternativas en commit 5bf86ea | Cumple | Capas y monolito modular se descartan con justificación. |
| ADR alcanzable desde docs/aspectos.md y desde el escenario que lo motiva | docs/aspectos.md y docs/arc42/10_requisitos_de_calidad.md en commit 5bf86ea | No cumple | Ninguno de los dos enlaza al ADR. |
| Arranque con un solo comando documentado en el README | README.md en commit 5bf86ea | No cumple | No hay sección de arranque ni comando único documentado al cierre. |
| Prueba automatizada en verde | backend/tests/test_health.py existe en commit 5bf86ea; runs_ci vacío | No verificado | No hay pipeline ni run que demuestre la prueba en verde. |
| Estructura de paquetes correspondiente al estilo del ADR | backend/src/linkclub/{domain,application,adapters} en commit 5bf86ea | Cumple | Coherente con puertos y adaptadores declarados en el ADR. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo ISCOUTB/AS_202620_Clubs_UTB, commit 5bf86ea | Cumple | Nombre, organización y visibilidad correctos. |
| Estructura mínima | docs/C4/contexto.md y docs/adr/.temp en commit 5bf86ea | No cumple | docs/C4 está en mayúscula y hay un archivo .temp en docs/adr. |
| Estado del repositorio que se califica | commit 5bf86ea 2026-08-23T23:05:10-05:00 | Cumple | Último commit antes del cierre. |
| Convenciones de ADR | docs/adr/0001-hexagonal.md | No cumple | El nombre no es kebab-case con patrón NNNN-titulo. |
| La tabla de aspectos | docs/aspectos.md en commit 5bf86ea | No cumple | No tiene las 8 columnas ni enlaces navegables. |
| Registro de uso de IA | docs/ia.md en commit 5bf86ea | No cumple | Solo describe usos posibles, no registros concretos con aceptado/rechazado. |
| README | README.md en commit 5bf86ea | No cumple | No documenta arranque ni pruebas. |
| Pipeline y análisis estático | runs_ci vacío y sin workflow al cierre | No verificado | No hay evidencia de ejecución de CI ni SonarCloud. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `4ede977c7cccc335d878019ce06cba2e23cf76d2 2026-09-06T22:41:55-05:00 quite el C2 y lo reemplaze con el C3`
- **Veredicto**: con pendientes
- Resumen: La entrega S3 en el commit 5bf86ea cumple parcialmente: tiene ADR, matriz comparativa y estructura hexagonal, pero no documenta arranque, no evidencia prueba en verde y la trazabilidad está rota. A HEAD se agregaron README operativo, CI y correcciones de estructura, pero hay pendientes de semanas anteriores aún sin resolver.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- README con arranque y pruebas documentado después del cierre (commits 7017270, 91323d6).
- Workflow .github/workflows/backend-tests.yml añadido tras el cierre.
- docs/C4 renombrado a docs/c4 y docs/aspectos.md actualizado después del cierre.
- Corrección de nombres de archivos y enlaces en docs (commits 46c7fa3, 993f51d).

Pendientes que siguen abiertos:
- docs/aspectos.md aún sin las 8 columnas del contrato ni enlace al ADR.
- docs/ia.md sin registros concretos de uso de IA.
- ADR con nombre fuera de la convención kebab-case.
- Sin evidencia de que la prueba automatizada esté en verde en CI.
- Archivo basura docs/adr/.temp aún presente.

## Recuento y nota sugerida

6 de 9 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.7 = 1 + 4 × (6/9).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Prueba automatizada en verde: no hay run de CI; comando pendiente: pytest backend/tests.
- Pipeline y análisis estático: no hay runs_ci ni workflow al cierre.

## Hallazgos para la planilla

- ADR no enlazado desde docs/aspectos.md ni desde los escenarios de calidad.
- README sin comando de arranque al cierre.
- Prueba sin evidencia de ejecución en CI.
- Nombre del ADR no sigue la convención kebab-case.
- docs/aspectos.md no cumple las 8 columnas.
- docs/ia.md es declarativo, sin usos concretos.
- docs/C4 en mayúscula y archivo .temp en docs/adr.
- Correcciones importantes subieron después del cierre s3.
- Commits posteriores al cierre (no calificados): 4ede977 2026-09-06T22:41:55-05:00 quite el C2 y lo reemplaze con el C3; 4cfcfb6 2026-09-06T18:58:18-05:00 Agregación de endpoint get y post para el corte vertical; 91323d6 2026-08-30T23:21:56-05:00 Correción de parrafo en sección 6.1 y corrección del readme; 01ae5f5 2026-08-30T22:41:40-05:00 Merge branch 'master' of https://github.com/ISCOUTB/AS_202620_Clubs_UTB; cae56d6 2026-08-30T22:41:36-05:00 .
