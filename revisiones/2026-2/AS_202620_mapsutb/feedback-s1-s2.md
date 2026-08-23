# Retroalimentación mapsutb · S1 y S2 (para publicar en el foro)

## Evidencia S1

El repositorio está en la organización, es público y la ficha del problema está completa: usuarios, objetivos, alcance y arquitectura propuesta. Su tabla de aspectos es de las mejores de la semana: ocho columnas, una fila con ID, aspecto y requisito, e incluso un escenario en formato de seis partes. El registro de IA incluye qué aceptaron y qué rechazaron. Les faltó montar la estructura de documentación (`docs/arc42/` con la plantilla, `docs/adr/`, `docs/c4/`) y declarar en la ficha las dos tensiones de calidad enfrentadas. Revisen también la etiqueta `corte-1`: apunta a un commit de la semana 1, y el corte aún no ha ocurrido.

## Evidencia S2

Las restricciones están bien: clasificadas por tipo y cada una justificada, y el contexto identifica con claridad actores y sistemas externos. Los cinco escenarios tienen medidas con cifra y unidad. Para corregir antes del corte 1: (1) redacten los escenarios con las seis partes (fuente, estímulo, artefacto, entorno, respuesta, medida) y condición de carga; (2) el árbol de utilidad debe priorizar por impacto y riesgo y apuntar a los escenarios (hay un enlace roto a un archivo que no existe); (3) falta el diagrama C4 de contexto como tal — una tabla no es un diagrama: háganlo como código, con leyenda y flechas etiquetadas, y guárdenlo en `docs/c4/`; (4) la sección 1 necesita objetivos de negocio asociados a su interesado, no solo atributos de calidad; (5) registren el uso de IA de esta semana; (6) organicen los archivos en `docs/arc42/` y actualicen la tabla de aspectos para enlazar cada escenario.
