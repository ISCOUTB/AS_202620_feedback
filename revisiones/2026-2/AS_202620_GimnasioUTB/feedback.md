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

## Semana 5 · CORTE1

El repositorio conserva una línea base sólida de las semanas anteriores (estructura hexagonal, ADR 0001, CI en verde, README reproducible), pero la respuesta al reto del corte 1 no está presente: falta la etiqueta corte-1, el ADR de la restricción asignada, el diagnóstico con línea base medida, la implementación del cambio, la prueba asociada y la medición contra umbral. Para el siguiente corte, etiqueten el commit, documenten el reto con alternativas y consecuencias, y actualicen docs/ia.md y docs/aspectos.md con la trazabilidad completa. La sustentación definirá la nota del quinto criterio.
