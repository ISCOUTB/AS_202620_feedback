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

El proyecto está sólido: corte vertical funcional, documentación arc42/C4/ADR completa y trazabilidad de aspectos navegable, con CI en verde. Para el próximo corte: reestructuren correcciones.md como tabla por hallazgo (acción, ruta, commit/run, estado) para que cada corrección sea contrastable. Aporten evidencia de SonarCloud (URL del análisis o workflow), no solo el archivo de propiedades. Equilibren la participación en el historial. Recuerden adjuntar el PDF en Moodle y preparar la sustentación.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Ya tienen la etiqueta `corte-1` sobre un commit anterior al cierre: bien.

El diagnóstico, el ADR y el reporte de medición del reto de concurrencia están redactados con un nivel técnico muy alto: identifican síntoma, causa raíz y riesgo, comparan tres alternativas con sus ventajas y desventajas, y presentan una tabla de resultados con cifras concretas. El registro de uso de IA también quedó completo, con un rechazo explícito y bien argumentado.

Pero hay un problema serio que hay que resolver antes de la sustentación: revisando el código del repositorio, el mecanismo que describen en el ADR (un lock por SKU) no aparece en ningún archivo. Los módulos de inventario no cambiaron entre la entrega anterior y esta etiqueta — solo se agregó una prueba nueva y la documentación. Las cifras de latencia que reportan tampoco tienen, en el repositorio, ningún código que las calcule. La prueba que sí existe pasa, pero no porque haya un mecanismo de exclusión mutua: simplemente verifica que el stock final quede correcto.

Antes de sustentar, implementen de verdad el mecanismo que describieron (o documenten honestamente cuál es el estado real) y agreguen el código que efectivamente mida la latencia que están reportando. Traigan también, si la tienen, una cifra de línea base real (antes del cambio), no solo la afirmación de que el problema existía.

## Semana 6 · S6

La entrega de la semana 6 está sólida: el mapa de contextos, la tabla de propiedad de datos y la auditoría de modularidad están bien documentados y trazados. Para cerrar los pendientes: (1) verifica que la sección 8 del arc42 incluya explícitamente el lenguaje ubicuo y el mapa de contextos, y actualiza el README para reflejarlo; (2) deja evidencia de la ejecución del pipeline (enlace a un run de GitHub Actions) y decide si SonarCloud vuelve al workflow; (3) los módulos vacíos (usuarios, proveedores, alertas) deberían tener al menos una nota de estado en el mapa de contextos. El resto cumple con lo pedido.

## Semana 7 · S7

El contrato OpenAPI, sus esquemas, la correspondencia con los routers, la prueba contractual, su ejecución en el pipeline, el ADR, la vista de ejecución y el C4 están presentes y verificables. Para cerrar la única no conformidad de la ficha, conserven una evidencia reproducible de que la prueba falla ante un cambio incompatible. Unifiquen además la versión declarada en el documento de API con la versión del contrato ejecutable y mantengan SonarCloud auditable.

## Semana 8 · S8

### Recomendaciones prioritarias

- El arc42 en un solo archivo es válido y su sección 2 ya fija la ausencia de presupuesto: completen la sección 7 con el host productivo que elijan, en vez de dejar solo el entorno local.
- Publiquen URL, respuesta de salud y hora; versionen la infraestructura y el procedimiento de despliegue.
- Expongan logs estructurados y una métrica ligada a un escenario; estimen costo y punto de ruptura, y justifiquen la plataforma en un ADR.

El pipeline y SonarCloud están en verde, los secretos del análisis se toman del almacén de GitHub y el entorno local está documentado. La no conformidad central es que el hosting sigue sin decidirse: no hay URL pública, infraestructura como código, health check externo ni vista de despliegue productiva. Añadan también logs estructurados, una métrica vinculada a un escenario, la estimación mensual y el ADR de plataforma.
