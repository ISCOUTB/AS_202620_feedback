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

## Semana 5 · CORTE1

El corte vertical A-01 está completo, con 47 pruebas de backend y 6 de frontend, y la documentación arquitectónica (arc42, C4, ADR, aspectos) está al día. El incumplimiento principal del corte es el nombre del archivo de correcciones: al cierre era correcciones_feedback.md y no correcciones.md; el renombrado llegó después. Para las próximas entregas, verifica el nombre exacto de los artefactos antes del cierre y adjunta el enlace al run de CI del commit evaluado. También conviene confirmar la organización del repositorio y entregar el PDF en el aula.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Se revisó de nuevo después del cierre, sobre la etiqueta `corte-1`, que sí existe y apunta a un commit dentro del plazo.

Qué está bien: el reto quedó resuelto por completo. Midieron el problema antes de decidir (encontraron que, cuando la cola de trabajos se cae a mitad de un lote, el sistema perdía el reporte del 100% de las hojas), compararon cuatro alternativas con argumentos técnicos reales, tomaron una decisión documentada, la implementaron sin romper el arranque de un solo comando, y volvieron a medir para comprobar que el problema quedó resuelto (0% de pérdida) dentro del tiempo permitido. También corrigieron con datos varios señalamientos de la revisión anterior sobre semanas previas (el pipeline sí corría en verde, el diagrama C4 sí estaba completo, el registro de IA sí tenía contenido).

Qué falta: todo el ejercicio del reto quedó en un solo commit muy grande, lo que dificulta ver el proceso paso a paso; en el futuro conviene dividir el trabajo en varios commits. Queda pendiente adjuntar el PDF de dos páginas en Moodle, y una de las pruebas nuevas tiene un hueco de cobertura que el propio equipo ya reconoció (una mutación que ninguna prueba detecta).

Para la sustentación: preparen cómo justifican haber trabajado sobre la deuda declarada (R-06) al no recibir la restricción de Moodle, y qué tan bien encajaría la misma solución si la restricción real resulta ser otra.

## Semana 2 · S2

La entrega de la semana 2 deja la documentación base (C4 nivel 1, contexto y restricciones) y un primer aspecto en aspectos.md, pero los escenarios de calidad y el árbol de utilidad están pendientes. Para la próxima entrega: redacten 3 a 5 escenarios completos en la sección 10 con medida numérica (cifra, unidad y condición de carga), clasifiquen las restricciones en técnicas/organizativas/legales, y hagan navegable la tabla de aspectos. Revisen también que el README diga cómo arrancar y probar, y que el registro de IA siga creciendo con cada uso. Los cambios recientes van en la dirección correcta: los ADR, el pipeline y el corte vertical de A-01 deben quedar evidenciados con sus runs. Sigan consolidando los commits de todo el equipo.
