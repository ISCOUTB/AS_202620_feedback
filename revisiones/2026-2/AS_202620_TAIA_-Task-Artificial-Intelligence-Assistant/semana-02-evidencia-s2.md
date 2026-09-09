# semana-02-evidencia-s2 · TAIA

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `59590c9` (2026-08-16T19:15:15-05:00) |
| Cierre | 2026-08-17T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | docs/arc42/arc42-template-EN.md sección 'Introduction and Goals' incluye objetivos de calidad priorizados con motivación y stakeholders (hash 59590c9, 2026-08-16T19:15:15-05:00). | Cumple | Objetivos claros con interesados y métrica propuesta por objetivo. |
| arc42 sección 2 con restricciones clasificadas y justificadas | docs/arc42/arc42-template-EN.md sección 'Architecture Constraints' clasifica restricciones técnicas y organizacionales con implicación arquitectónica (hash 59590c9). | Cumple | Faltan restricciones legales en el commit calificado; se agregaron después en ffd4f5c. |
| Restricciones separadas de los requisitos | La sección 2 está separada de la tabla de requisitos RF-01..RF-10 en 'Requirements Overview' del mismo archivo (hash 59590c9). | Cumple | No se confunden restricciones con requisitos funcionales. |
| arc42 sección 3 con actores y sistemas externos | docs/arc42/arc42-template-EN.md incluye sección de contexto con actores y sistemas externos y existe docs/c4/C4-ContextoTAIA.png (hash 59590c9). | Cumple | La coherencia con el diagrama no se pudo verificar por ser imagen binaria sin código. |
| Entre 3 y 5 escenarios de calidad redactados | docs/calidad/escenarios_calidad.md contiene 5 escenarios numerados (hash 59590c9). | Cumple | Se ubican en docs/calidad en lugar de docs/arc42, pero se evalúa el contenido. |
| Cada escenario con sus seis partes y medida numérica | Escenario 5 'Sustitucion del modelo de IA' en docs/calidad/escenarios_calidad.md carece de medida numérica; 'sin tocar dominio ni casos de uso' no es cifra (hash 59590c9). | No cumple | Los escenarios 1 a 4 sí tienen medida; el 5 no cumple la condición. |
| Árbol de utilidad que prioriza por impacto y riesgo | docs/calidad/arbol_utilidad.md es una lista jerárquica plana sin prioridad, impacto ni riesgo (hash 59590c9). | No cumple | No se evidencia priorización; parece lista de atributos. |
| C4 de contexto con leyenda y flechas etiquetadas | docs/c4/C4-ContextoTAIA.png es una imagen PNG; no hay código fuente que permita verificar leyenda y flechas etiquetadas en el commit calificado (hash 59590c9). | No cumple | Se marcó no cumple por falta de evidencia textual; commits posteriores lo convierten a Mermaid. |
| Escenarios alcanzables desde la fila de su aspecto | docs/aspectos.md tiene una única fila A-01 con 'Evidencia: Pendiente' y sin enlaces a ningún escenario (hash 59590c9). | No cumple | No hay ninguna fila que enlace a docs/calidad/escenarios_calidad.md. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en ISCOUTB, público, nombre correcto e integrantes en historial | Repositorio visible ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant; autores en shortlog: val, dei0811, mark, luis20072002 (hash 59590c9). | Cumple | El nombre incluye guiones pero conserva el patrón AS_202620_<PROYECTO>. |
| Estructura mínima con README, docs/arc42, docs/adr, docs/c4, aspectos.md e ia.md | Árbol en 59590c9: existe README.md, docs/arc42/, docs/c4/, docs/aspectos.md, docs/ia.md; no existe docs/adr/. | No cumple | Falta el directorio docs/adr; docs/arc42 contiene la plantilla sin traducir. |
| Estado calificado es último commit de main/master anterior o igual al cierre | commit 59590c9 con fecha 2026-08-16T19:15:15-05:00, anterior al cierre 2026-08-17T05:00:00Z. | Cumple | No se indica rama, pero el hash revisado es el anotado en la evidencia. |
| ADR con un archivo por decisión, numerado y sin reescrituras | No existe el directorio docs/adr/ en el commit calificado 59590c9. | No cumple | El ADR 0001 aparece solo en HEAD, en commit 42c5b03 posterior al cierre. |
| docs/aspectos.md con columnas completas trazables hasta evidencia | docs/aspectos.md fila A-01: C4, ADR, Código, Pruebas y Evidencia dicen 'Pendiente' (hash 59590c9). | No cumple | Una fila con cinco huecos no es trazable. |
| docs/ia.md registra uso de IA con aceptado, rechazado y motivo | docs/ia.md entradas 001 y 002 con 'Aceptado', 'Rechazado o modificado' y verificación (hash 59590c9). | Cumple | Cumple el formato exigido y crece en commits posteriores. |
| README describe qué es, cómo se arranca con un comando y cómo se prueba | README.md en 59590c9 describe el sistema y tecnologías pero no incluye comando de arranque ni de pruebas. | No cumple | Faltan secciones de arranque y prueba en el commit calificado. |
| Pipeline ejecuta CI y análisis estático sin secretos en el repositorio | En 59590c9 no existe .github/workflows/; el grep de secretos no arrojó coincidencias. | No cumple | No hay CI en el commit calificado; el flujo se añade en commits posteriores al cierre. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `915e4996c5f252b0a35e6a0405935e665d2cfa66 2026-09-08T17:42:02-05:00 fix: harden dependency installation for SonarCloud`
- **Veredicto**: con pendientes
- Resumen: El proyecto a HEAD ha evolucionado bastante desde el cierre S2: ya existen docs/arc42/arc42.md, docs/adr/0001-estilo-arquitectonico.md, docs/c4/C4-C1.md/C4-C2.md, backend con pruebas y flujo CI; sin embargo, en la semana 2 el repositorio no cumplía los requisitos de la ficha ni del contrato.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Se agregó docs/adr/0001-estilo-arquitectonico.md en 42c5b03/2026-08-30 (posterior al cierre).
- Se completó docs/arc42/arc42.md en 1668579/2026-09-06, removiendo la plantilla.
- Se pasó C4 a Mermaid/source en 9df9d2a y 0f7f4bd (2026-08-29), posterior al cierre.
- Se corrigieron medidas de escenario y restricciones legales en ffd4f5c/2026-08-29.
- Se añadió CI en .github/workflows/ci.yml en commits 2f3ca0d/bda515c/ce99b54 (2026-09-06), posterior al cierre.

Pendientes que siguen abiertos:
- La corrección de estructura y arquitectura se ha hecho en commits posteriores, con lo cual la evidencia de la semana 2 no es defendible en el estado calificado.
- Revisar que doc de aspectos/apartados del contrato queden sincronizados en la rama principal para la próxima entrega.

## Recuento y nota sugerida

5 de 9 criterios Cumple.

## No verificado / pendientes

- C4 de contexto con leyenda y flechas etiquetadas

## Hallazgos para la planilla

- El commit calificado 59590c9 no contiene la sección 10 de arc42 como archivo propio; está dentro de arc42-template-EN.md.
- La sección 3 no se pudo contrastar con el C4 por ser imagen binaria.
- docs/aspectos.md tiene una sola fila, toda en 'Pendiente'.
- docs/calidad/escenarios_calidad.md es el único lugar con escenarios; no están dentro de docs/arc42/.
- docs/arc42/arc42-template-EN.md conserva nombre y contenido de plantilla en inglés.
- No hay ADR en el commit calificado.
- No hay pipeline CI en el commit calificado; los workflows aparecen después del cierre.
- Commits posteriores al cierre (no calificados): 915e499 2026-09-08T17:42:02-05:00 fix: harden dependency installation for SonarCloud; 3cf6bfc 2026-09-08T17:34:01-05:00 fix: lock dependencies for SonarCloud security gate; a3f4d82 2026-09-06T04:13:11-05:00 feat: update ia.md and add corrections.md based on automated evaluation feedback; c8796c7 2026-09-06T02:11:19-05:00 docs: complete arc42 architecture views; ce99b54 2026-09-06T01:47:31-05:00 ci: fix pytest root configuration
