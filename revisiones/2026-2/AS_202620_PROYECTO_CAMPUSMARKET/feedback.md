# Retroalimentación publicable · CampusMarket

## Semanas 1 y 2

## Evidencia S1

El repositorio está en la organización, es público y el README funciona como ficha del problema: declara beneficiarios, problema y objetivo general. El registro de IA ya tiene su primera entrada. Les faltó: las dos tensiones de calidad, la tabla de ocho columnas en `docs/aspectos.md` (hoy es texto), la plantilla arc42 y las carpetas `docs/adr/` y `docs/c4/` (las crearon como archivos sueltos el 11 de agosto, después del cierre). Ojo con el README: al cierre listaba dos integrantes y el equipo es de tres.

## Evidencia S2

Las restricciones están clasificadas y justificadas con origen de cada una, los cuatro escenarios tienen sus seis partes y medidas numéricas con condición de carga, el árbol de utilidad prioriza por impacto y riesgo, y el C4 de contexto está como código PlantUML con leyenda y flechas etiquetadas: muy buen trabajo. Para corregir antes del corte 1: (1) la sección 1 de arc42 lista funcionalidades, no objetivos de negocio con su interesado; (2) `docs/aspectos.md` sigue igual que en S1: pónganle la tabla de ocho columnas y enlacen cada escenario; (3) organicen la documentación en `docs/arc42/` y `docs/c4/`; (4) unifiquen el tamaño del equipo en los documentos (dicen «dos» y «tres» integrantes); (5) registren en `docs/ia.md` qué rechazaron de lo que propuso la IA; (6) repartan el historial: todo está firmado por una sola cuenta.

## Semana 3

Qué está bien: el ADR 0001 está completo y enlazado desde `aspectos.md` y EC-03, la sección 4 trae tácticas ligadas a los escenarios, la matriz comparativa evalúa los tres estilos contra su árbol de utilidad y el esqueleto backend arranca con un comando único con su prueba en CI en verde.

Qué corregir antes del corte 1 (semana 5):
1. `docs/ia.md`: quedó sin entradas de la semana 3 (17–23 ago) y sin la columna de qué se rechazó y por qué; pónganlo al día.
2. El frontend sigue siendo la plantilla Flutter por defecto: lleven en S4 los mismos módulos del backend para que la estructura del ADR quede materializada en todo el sistema.

## Semana 4 · S4

La evidencia S4 está sólida: arc42 1-6, 9, 10 y 12 redactados con contenido propio; C4 niveles 1 y 2 coherentes y versionados como código; corte vertical de publicaciones trazado desde la interfaz hasta SQLite con prueba en verde; y la fila ASP-05 de aspectos queda completa hasta Pruebas. Para el primer corte, integren SonarCloud al pipeline, enlacen cada ADR con el commit que lo implementa y añadan una medición de línea base. El arranque con un solo comando está bien documentado; conviene dejarlo verificado en un run o captura. Sigan manteniendo el registro de IA con lo rechazado y su motivo, que está bien logrado.

## Semana 5 · Primer corte

No hay etiqueta `corte-1` ni actividad de la semana 5. La base acumulada de S4 está bien estructurada: C4 como código, corte vertical Flutter → FastAPI → SQLite, prueba funcional y pipeline en verde. Ese trabajo ya corresponde a la línea base y no demuestra el reto nuevo. Antes del cierre deben documentar la restricción y su diagnóstico, medir el estado inicial, registrar el ADR del reto, aplicar el cambio, cubrirlo con una prueba en CI, contrastar el resultado con el umbral y actualizar `docs/aspectos.md` y `docs/ia.md`. Creen la etiqueta sobre el commit real del corte. También queda pendiente enlazar el ADR con su commit de implementación e integrar SonarCloud. La restricción asignada, el PDF y la sustentación quedan pendientes de verificación docente.
