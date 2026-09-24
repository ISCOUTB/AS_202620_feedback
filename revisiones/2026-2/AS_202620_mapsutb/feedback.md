# Retroalimentación publicable · mapsutb

## Semanas 1 y 2

## Evidencia S1

El repositorio está en la organización, es público y la ficha del problema está completa: usuarios, objetivos, alcance y arquitectura propuesta. Su tabla de aspectos es de las mejores de la semana: ocho columnas, una fila con ID, aspecto y requisito, e incluso un escenario en formato de seis partes. El registro de IA incluye qué aceptaron y qué rechazaron. Les faltó montar la estructura de documentación (`docs/arc42/` con la plantilla, `docs/adr/`, `docs/c4/`) y declarar en la ficha las dos tensiones de calidad enfrentadas. Revisen también la etiqueta `corte-1`: apunta a un commit de la semana 1, y el corte aún no ha ocurrido.

## Evidencia S2

Las restricciones están bien: clasificadas por tipo y cada una justificada, y el contexto identifica con claridad actores y sistemas externos. Los cinco escenarios tienen medidas con cifra y unidad. Para corregir antes del corte 1: (1) redacten los escenarios con las seis partes (fuente, estímulo, artefacto, entorno, respuesta, medida) y condición de carga; (2) el árbol de utilidad debe priorizar por impacto y riesgo y apuntar a los escenarios (hay un enlace roto a un archivo que no existe); (3) falta el diagrama C4 de contexto como tal — una tabla no es un diagrama: háganlo como código, con leyenda y flechas etiquetadas, y guárdenlo en `docs/c4/`; (4) la sección 1 necesita objetivos de negocio asociados a su interesado, no solo atributos de calidad; (5) registren el uso de IA de esta semana; (6) organicen los archivos en `docs/arc42/` y actualicen la tabla de aspectos para enlazar cada escenario.

## Semana 3

Qué está bien: estrategia de solución ligada a los objetivos de calidad, ADR 0001 con alternativa descartada y motivo por patrón, y arranque con un solo comando documentado (`scripts/start.sh`).

Qué corregir antes del corte 1 (semana 5):
1. Escriban la matriz comparativa de los tres estilos contra el árbol de utilidad: la ficha la pide y hoy no existe en el repositorio.
2. Materialicen la estructura que declara el ADR en `lib/` (carpetas `adapters/`, `repositories/`, `strategies/`, `services/`, `features/` con `.gitkeep`): hoy solo está `main.dart`.
3. Actualicen `docs/aspectos.md` (todavía dice «Sin ADR aún») y enlacen el ADR desde el escenario que lo motiva; reparen el enlace roto en `docs/escenarios_calidad.md`.
4. Registren el uso de IA de esta semana en `docs/ia.md` y evidencien la prueba en verde (pipeline o run).
5. Contribuyan todos los integrantes (esta semana solo aparecieron tres cuentas) y regularicen `docs/arc42/` y `docs/c4/`.

## Semana 4 · S4

La documentación arc42 (secciones 1-6, 9, 10 y glosario) y los diagramas C4 están bien avanzados, y el corte vertical de zonas (interfaz → repositorio → JSON) está correctamente trazado. Para cerrar las brechas: (1) retiren los bloques de plantilla arc42help de la sección 5; (2) actualicen ficha-problema.md, escenarios_calidad.md y aspectos.md al alcance sin realidad aumentada, con una fila de aspectos defendible hasta Pruebas; (3) implementen o declaren explícitamente los contenedores de contenido panorámico y plano del campus que el C2 dibuja; (4) añadan un workflow de CI que ejecute las pruebas y deje evidencia pública en verde; (5) corrijan las rutas docs/Arc42 y docs/C4 a minúsculas; (6) registren los cambios de decisión en ADR nuevos, no editando ADR aceptados. El equipo va bien encaminado; estos ajustes son de forma y trazabilidad.

## Semana 5 · Primer corte (revisión flexible)

Por indicación docente se aceptaron las correcciones aplicadas durante la semana, aunque sean posteriores al cierre original. El corte sigue siendo el compendio de S1 a S4, sin reto ni restricción nueva. Se verificó que la ficha ya refleja el alcance sin RA, que los cinco escenarios tienen las seis partes, que las rutas de documentación fueron normalizadas y que el ADR 0004 aporta una comparación de tres estilos para justificar el monolito.

La documentación ahora declara con honestidad que el plano y las panorámicas siguen diferidos, y A-01 enlaza requisito, C4, ADR, código y prueba. El flujo de zonas puede seguirse desde la interfaz hasta el JSON local. Aún falta la evidencia verificable de ejecución: el workflow de CI ya ejecuta pruebas, pero no se encontró un run público; tampoco se ejecutó el proyecto durante la revisión. Para la sustentación, demuestren ese recorrido y expliquen cómo preservarán la historia de ADR 0001 cuando una decisión cambie.

## Semana 7 · S7

El contrato de las tres integraciones y el ADR que justifica la estrategia sincrona estan bien construidos y trazados a un escenario de calidad; esa es la base correcta. Para cerrar la semana: (1) hagan que el pipeline invoque explicitamente la prueba de contrato y compartan la URL del run; (2) conserven la corrida en rojo del cambio incompatible con su URL en lugar de revertir el commit sin dejar rastro de la ejecucion; (3) completen la evidencia de analisis estatico: linea del workflow que invoca el scanner, URL del run exitoso y URL publica del analisis con el Quality Gate; (4) suban el contenido de la tabla de aspectos con sus ocho columnas y del registro de IA con lo rechazado y su motivo; (5) unifiquen la documentacion en Markdown, retiren la copia suelta dentro de lib/ y actualicen el estado del README. Con la prueba de contrato fallando de forma reproducible, la entrega sube de nivel.
## Semana 6 · S6

El documento `dominio_y_modularidad.md` aporta un mapa de contextos, dueños de datos y no conformidades con acciones concretas. Para que la arquitectura sea defendible, llévenlo también a arc42 §8, documenten en un ADR el reajuste de límites y vinculen cada contexto con la tabla de aspectos. Añadan SonarCloud con scanner, run y Quality Gate público.

## Semana 8 · S8 (preliminar)

El README permite reproducir el entorno local y la restricción de costo cero está declarada. Las no conformidades principales son que no existe una URL pública ni un endpoint de salud, falta infraestructura como código para desplegar y el pipeline del estado revisado está en rojo. Tampoco se encontraron logs estructurados, una métrica operativa consultable, inyección segura de la clave de Google, cálculo mensual, contenido real en arc42 §7 o un ADR que compare y decida la plataforma. Para la entrega definitiva, separen claramente arranque local de despliegue reproducible y publiquen evidencia operativa verificable.
