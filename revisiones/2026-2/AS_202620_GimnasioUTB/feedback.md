# Retroalimentación publicable · GimnasioUTB

## Semana 1 · Equipo, problema y repositorio

La ficha del problema está bien: usuarios, alcance y una idea concreta y acotada. El repositorio es público y tiene README, aspectos e IA iniciados.

Lo que falta antes de que se convierta en deuda: declarar en la ficha las dos tensiones de calidad enfrentadas (hoy la tensión consistencia vs. facilidad de operación está en aspectos.md), montar `docs/arc42/` con la plantilla y crear `docs/adr/` y `docs/c4/` (git no guarda carpetas vacías: suban contenido o un `.gitkeep`), y convertir `aspectos.md` a la tabla de ocho columnas del curso. Revisen además que los tres integrantes tengan acceso: el historial solo muestra a uno.

## Semana 2 · Escenarios de calidad y restricciones

Buen nivel de contenido: restricciones organizacionales y técnicas con justificación, árbol de utilidad con prioridades, y escenarios con las seis partes y medidas numéricas (destaca el escenario de rendimiento, que ya declara carga, umbral y método de medición).

Correcciones para el corte 1: (1) seleccionen entre 3 y 5 escenarios — tienen 8; (2) monten la estructura de arc42 por secciones en `docs/arc42/` en lugar de un único archivo; (3) enlacen cada escenario desde su fila de aspectos; (4) entreguen el C4 preferiblemente como código (mermaid o PlantUML) y con leyenda; (5) registren en `ia.md` cada uso con lo que aceptaron y lo que rechazaron y por qué; y (6) revisen la categoría legal de las restricciones y el dato «equipo de 4 personas» (son 3).

## Semana 3

Qué está bien: ADR 0001 completo (contexto, alternativas descartadas con motivo, decisión y consecuencias), sección 4 del arc42 con matriz comparativa ligada a los escenarios ES1/ES7/ES8, esqueleto hexagonal por módulos y CI en verde.

Qué corregir antes del corte 1 (semana 5):
1. Enlacen el ADR 0001 desde `docs/aspectos.md` y desde los escenarios ES1/ES7/ES8: hoy solo es alcanzable desde la sección 4 del arc42.
2. Conviertan `docs/aspectos.md` (aún en prosa) en la tabla ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia.
3. Repartan el arc42 en `docs/arc42/` y el C4 en `docs/c4/` (estructura mínima, arrastrada desde S1).
4. Corrijan la restricción OC5 («equipo de 4 personas»: son 3) en el arc42 y en el ADR.
5. Registren en `docs/ia.md` qué se rechazó y por qué en cada uso.

## Semana 4 · S4

La documentación de arquitectura (arc42, C4, ADR, aspectos, IA) muestra avance, pero el corte vertical que describe el README no está implementado: las carpetas del módulo aforo están vacías y no hay endpoints de aforo ni persistencia. El comando db:migrate mencionado no existe en package.json. La prueba automatizada solo cubre /health, no el recorrido completo. Revisen la trazabilidad: las celdas de aspectos y el ADR deben apuntar a archivos y commits reales. Para la próxima entrega, implementen el flujo de registro de acceso con su prueba de integración y alineen el README con los scripts reales. El C4 en código Mermaid es un buen punto de partida; mantengan esa práctica.

## Semana 5 · Primer corte

Revisión manual preliminar previa al cierre. La línea base del backend tiene corte vertical, pruebas y CI en verde. Aún no se identifica la respuesta al reto nuevo: falta la etiqueta `corte-1`, declarar la restricción, medir el estado inicial, crear el ADR del reto, implementar el incremento y contrastarlo con el umbral. La prueba concurrente con persistencia real sigue pendiente y el C4 aún presenta aplicación, base de datos y mensajería no implementadas. Ajusten `docs/aspectos.md` a la cadena de ocho columnas, registren el uso de IA del corte y conserven los ADR aceptados como registros históricos en lugar de reescribirlos.


## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Sigue sin existir la etiqueta `corte-1`: se revisó el último commit antes del cierre.

Lo bueno: el registro de uso de IA quedó al día, con una entrada de esta semana que dice claramente qué se aceptó y qué se rechazó y por qué. Y la fila de trazabilidad del escenario de aforo (S1) sigue siendo navegable de punta a punta.

Lo que falta: el trabajo antes del cierre fue limpieza de documentación (README, glosario, historial de correcciones), no una respuesta al reto propio del primer corte. No hay una restricción nueva diagnosticada, ni un ADR nuevo, ni un cambio de código, ni una medición contra un umbral.

Una alerta seria: el ADR de arquitectura hexagonal, que ya estaba aceptado desde la semana 3, fue editado en su contenido varias veces después de aceptarse (cambiaron los escenarios de calidad que cita y las consecuencias). Un ADR aceptado no se edita: si la decisión evoluciona, se escribe un ADR nuevo que reemplaza al anterior, dejando un enlace.

Para la sustentación: traigan la restricción asignada, la medida inicial del sistema antes de tocarlo, y expliquen por qué el ADR 0001 cambió de contenido después de aceptado.

## Semana 3 · S3

La entrega tiene buen ADR y un esqueleto hexagonal coherente con el estilo elegido. Sin embargo, faltó completar la sección 4 de arc42 con la matriz comparativa y las tácticas ligadas a los escenarios, y docs/aspectos.md no enlaza el ADR. Ajusten también la estructura mínima moviendo arc42 a docs/arc42/ y registren el C4 en docs/c4/. El esqueleto arranca bien y la prueba pasa, así que el foco ahora es cerrar la trazabilidad documental para que la semana 4 no arrastre estas brechas.
