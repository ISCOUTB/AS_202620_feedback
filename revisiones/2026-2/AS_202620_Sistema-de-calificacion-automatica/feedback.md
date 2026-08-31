# Retroalimentación publicable · Calificación automática

## Semana 1

Excelente montaje: estructura casi completa, plantilla arc42 en Markdown, tabla de aspectos con las ocho columnas y un aspecto bien declarado, registro de IA con qué se aceptó, qué se rechazó y por qué, y dos tensiones de calidad muy bien formuladas.

Ajustes pendientes: la ficha del problema no está en el repositorio (solo se menciona el «Informe Inicial» de Moodle) — súbanla para que la entrega sea defendible desde el repo. `docs/adr/` y `docs/c4/` quedaron como archivos vacíos en lugar de directorios: conviene dejarlos como directorios con `.gitkeep`. Y la contribución sigue concentrada en una sola cuenta: los demás integrantes deben empezar a aparecer en el historial.

## Semana 2

Trabajo sobresaliente: cinco escenarios con las seis partes y medidas numéricas con condición de carga, árbol de utilidad con impacto y riesgo, secciones 1 y 3 redactadas, y C4 de contexto como código Mermaid con flecha etiquetada.

Antes del corte 1: enlacen cada escenario desde la fila de su aspecto en `docs/aspectos.md` (la tabla de trazabilidad sigue en «Pendiente»), completen las restricciones con categorías organizativas y legales (hoy son todas técnicas o de alcance), y repartan las contribuciones entre todos los integrantes, que es lo que más se va a notar en el corte.

## Semana 3

Qué está bien: la documentación quedó sólida: sección 4 con tácticas por escenario, matriz comparativa contra el árbol (§4.1), tres ADR con convención, alternativas descartadas y reemplazo correcto del 0001, y enlaces al ADR desde `aspectos.md` y desde EC-04/EC-05.

Qué corregir antes del corte 1 (semana 5):
1. Al cierre, el README seguía con el checklist «[ ] Código» sin marcar: no había comando de arranque documentado.
2. Al cierre no existían la prueba ni el pipeline, y los paquetes de los 7 módulos del ADR-0002 no estaban en el repo.
3. Para S4 traigan el esqueleto con sus módulos y el run en verde dentro del plazo de la entrega.

Ojo: parte del trabajo llegó después del cierre y no contó para esta entrega; la próxima vez asegúrense de empujar antes de la medianoche del domingo.

## Semana 4 · S4

Buen avance: el corte vertical A-01 está construido y documentado, los ADRs son sólidos y el README permite arrancar con un solo comando. Para el primer corte, completen el C4 nivel 2 con su diagrama y actualicen la tabla de niveles; la fila A-01 de aspectos.md debe enlazar un contenedor C4 real, no 'C2 pendiente'. Suban evidencia del run de CI en verde (URL) para confirmar las 34+6 pruebas. Revisen que la sección 9 del arc42 cite los ADRs y que el glosario tenga términos del dominio. El resto de la documentación se ve coherente.
