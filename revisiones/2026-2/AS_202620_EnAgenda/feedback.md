# Retroalimentación publicable · EnAgenda

## Semana 1 · Equipo, problema y repositorio

El montaje quedó muy bien: ficha del problema con usuarios, alcance y tres tensiones de calidad bien enfrentadas, la tabla de aspectos iniciada y un registro de IA con entradas reales, incluido lo que rechazaron y por qué. La plantilla arc42 está en Markdown y los directorios `adr/` y `c4/` existen.

Dos correcciones menores: varios archivos tienen un espacio antes de la extensión (por ejemplo `aspectos .md`, `ia .md`, el ADR `0001-… .md`); renómbrenlos a la convención para que las herramientas de revisión los encuentren. Y conviene confirmar que los tres integrantes tienen acceso al repositorio, porque el historial de la semana solo muestra a dos.

## Semana 2 · S2

La semana 2 tiene un buen avance en escenarios de calidad: cinco escenarios completos con medida numérica. Para cerrar las brechas: creen docs/arc42/01* con objetivos de negocio e interesados, clasifiquen las restricciones en técnicas, organizativas y legales, y agreguen riesgo al árbol de utilidad. La tabla de aspectos aún no traza nada: cada fila debe enlazar a su escenario. También noten que los commits posteriores al cierre sugieren que muchas correcciones se subieron tarde; procuren dejar la entrega cerrada antes de la fecha límite.
## Semana 3

Qué está bien: la sección 4 ya elige el monolito modular con límites y consecuencias, el ADR es una decisión de estilo aceptada con alternativas motivadas y `aspectos.md` ya usa la tabla de 8 columnas.

Qué corregir antes del corte 1 (semana 5):
1. El esqueleto prometido no existe: creen `src/` con los módulos del ADR (eventos, invitaciones, tareas, agenda, presupuesto, panel, compartido) y retiren los scripts sueltos de `docs/` (`main.py` importa un módulo inexistente).
2. Documenten en el README el comando único de arranque y agreguen una prueba en verde: el ADR promete `tests/` y hoy no hay ninguna.
3. Renombren el ADR a algo como `0001-usar-monolito-modular.md`: el nombre actual tiene espacio, no pasa el filtro y ya no corresponde a lo que decide; arreglen los enlaces internos rotos.
4. La matriz comparativa no referencia los escenarios EC-01…EC-05: pongan una fila por escenario del árbol de utilidad.
5. Hagan alcanzable el ADR: la columna ADR de `aspectos.md` sigue «Pendiente» y `10-requisitos-de-calidad .md` no lo enlaza.
6. Repartan la contribución: en S3 faltó un integrante en el historial (2 de 3).

## Semana 4 · S4

La entrega de la semana 4 está sólida en documentación arc42, glosario, C4 niveles 1 y 2, corte vertical y pruebas en CI. Para el primer corte, revisen la coherencia entre el C4 nivel 2 y el código real: el diagrama muestra API/Backend y Base de Datos, pero la implementación es un monolito Flask con repositorio en memoria; ajusten el diagrama o el código. Completen la celda C4 de docs/aspectos.md con rutas navegables a los diagramas. Agreguen SonarCloud al pipeline como exige el contrato. Eviten versionar archivos .pyc. Finalmente, verifiquen que las secciones 1, 4, 5 y 6 de arc42 estén completamente redactadas y sin texto de plantilla.

## Semana 5 · Primer corte

Revisión manual preliminar previa al cierre. La línea base de invitaciones tiene aplicación, pruebas y CI en verde. La respuesta al reto nuevo aún no es identificable: falta la etiqueta `corte-1`, declarar la restricción, medir el estado inicial, registrar las alternativas y la decisión en un ADR nuevo, implementar el incremento y contrastar el resultado con el umbral. Completen una fila navegable en `docs/aspectos.md` hasta código, prueba y evidencia, y registren en `docs/ia.md` una salida del corte con su decisión y motivo técnico. Alineen también el C4 de contenedores con el monolito Flask y la persistencia en memoria que existen actualmente.


## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Ya crearon la etiqueta `corte-1` sobre un commit anterior al cierre, y eso está bien: quedó un estado identificable para calificar.

Lo que falta: el trabajo de la última noche antes del cierre se dedicó a corregir observaciones de la semana 4 (arreglar el diagrama C4 para que coincida con la aplicación Flask, y enlazar la fila de aspectos), y ustedes mismos lo dejan escrito con honestidad en su documento de correcciones: no llegaron a plantear ni resolver el reto propio del primer corte. Falta identificar la restricción nueva asignada, medir cómo estaba el sistema antes de tocarlo, escribir la decisión en un ADR nuevo, hacer el cambio sobre el corte vertical existente y medir el resultado contra un umbral.

Dos cosas puntuales para corregir ya: el enlace de "Evidencia" en la fila de aspectos apunta a un archivo que no existe en el repositorio (el archivo real tiene otro nombre); y el registro de uso de IA no tiene ninguna entrada de esta semana, ni de las correcciones que sí hicieron el 6 de septiembre.

Para la sustentación: lleven claro qué restricción les tocó, qué medida inicial tomaron y con qué procedimiento, y qué cambio de código (no solo de documentación) responde a esa restricción.
