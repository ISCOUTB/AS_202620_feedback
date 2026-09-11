# Retroalimentación publicable · InvenTrack

## Semana 1 · Equipo, problema y repositorio

Buen arranque: la ficha del problema está bien escrita, con usuarios y alcance claros, y el registro de IA ya nombra la herramienta y el uso concreto. El repositorio es público y correcto.

Para cerrar la semana: declaren en la ficha las dos tensiones de calidad enfrentadas (hoy solo está el aspecto de consistencia), conviertan `aspectos.md` a la tabla de ocho columnas del curso, y monten `docs/arc42/` con la plantilla más `docs/adr/` y `docs/c4/` (suban contenido o un `.gitkeep`, git no guarda carpetas vacías). Revisen también que los cuatro integrantes tengan acceso al repositorio: el historial de la semana solo muestra a una persona.

## Semana 2 · S2

La documentación de la semana 2 está completa y trazable: secciones 1, 2, 3 y 10 del arc42 con contenido real, 5 escenarios con medida numérica, árbol de utilidad priorizado y C4 de contexto en Mermaid. Para próximas entregas, usen archivos por sección (01-objetivos.md, 02-restricciones.md, etc.) y activen el pipeline con pruebas para que la evidencia quede en los runs. El registro de IA y la tabla de aspectos van bien encaminados.
## Semana 3

Qué está bien: entrega completa: ADR 0001 con contexto, alternativas y consecuencias, matriz comparativa por escenario, esqueleto modular con arranque documentado, enlaces del ADR desde `aspectos.md` y ESC-01, `docs/ia.md` al día y CI en verde.

Qué corregir antes del corte 1 (semana 5):
1. Ratifiquen el ADR 0001 como «aceptado» (hoy dice «propuesto, pendiente de ratificación») y ajusten el título para que enuncie la decisión.
2. Mantenimiento: conserven el pipeline en verde en cada entrega y sigan enlazando cada decisión desde su aspecto y su escenario.

## Semana 4 · S4

Buen avance en documentación, C4 y estructura del esqueleto: el arc42, los diagramas y la organización por módulos son sólidos. Para completar la semana 4, redacten las secciones 5 y 6 con la interpretación de los diagramas, inicien el glosario y hagan que la fila de aspectos apunte a una prueba real del corte vertical. Cuiden las convenciones de ADR: un archivo por decisión real y con nombre estandarizado. Aunque los commits posteriores al cierre corrigen varios vacíos, esas correcciones no cuentan para la entrega de la semana.
## Semana 5 · CORTE1

El repositorio muestra una base arquitectónica sólida: arc42, C4, ADR, aspectos e IA bien documentados, con corte vertical y pruebas en CI. Para el corte, recuerden que correcciones.md debe estar en la raíz en el commit anterior al cierre; en esta entrega se añadió después. Integren SonarCloud al pipeline para cumplir el contrato. Revisen que cada hallazgo de S1-S4 quede respondido con evidencia contrastable. Distribuyan más equitativamente las contribuciones y mantengan la trazabilidad navegable.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Ya tienen la etiqueta `corte-1` sobre un commit anterior al cierre: bien.

El diagnóstico, el ADR y el reporte de medición del reto de concurrencia están redactados con un nivel técnico muy alto: identifican síntoma, causa raíz y riesgo, comparan tres alternativas con sus ventajas y desventajas, y presentan una tabla de resultados con cifras concretas. El registro de uso de IA también quedó completo, con un rechazo explícito y bien argumentado.

Pero hay un problema serio que hay que resolver antes de la sustentación: revisando el código del repositorio, el mecanismo que describen en el ADR (un lock por SKU) no aparece en ningún archivo. Los módulos de inventario no cambiaron entre la entrega anterior y esta etiqueta — solo se agregó una prueba nueva y la documentación. Las cifras de latencia que reportan tampoco tienen, en el repositorio, ningún código que las calcule. La prueba que sí existe pasa, pero no porque haya un mecanismo de exclusión mutua: simplemente verifica que el stock final quede correcto.

Antes de sustentar, implementen de verdad el mecanismo que describieron (o documenten honestamente cuál es el estado real) y agreguen el código que efectivamente mida la latencia que están reportando. Traigan también, si la tienen, una cifra de línea base real (antes del cambio), no solo la afirmación de que el problema existía.

## Semana 6 · S6

La entrega de esta semana no incorporó los artefactos solicitados: no hay mapa de contextos, tabla módulo a datos, ni lista de violaciones con plan de corrección. El commit evaluado solo renombra un archivo de feedback. Se recomienda priorizar la auditoría sobre el código actual: revisar qué módulos escriben cada entidad (por ejemplo, el verificador de movimientos en productos) y documentar el recorrido. La sección 8 de arc42 debe incluir lenguaje ubicuo y el mapa de contextos. El C4 nivel 3 sigue pendiente desde semanas anteriores. La documentación existente (ADR, aspectos, IA, README) está bien estructurada; falta el contenido de la semana.
