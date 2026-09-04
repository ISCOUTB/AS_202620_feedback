# Retroalimentación publicable · EnAgenda

## Semana 1 · Equipo, problema y repositorio

El montaje quedó muy bien: ficha del problema con usuarios, alcance y tres tensiones de calidad bien enfrentadas, la tabla de aspectos iniciada y un registro de IA con entradas reales, incluido lo que rechazaron y por qué. La plantilla arc42 está en Markdown y los directorios `adr/` y `c4/` existen.

Dos correcciones menores: varios archivos tienen un espacio antes de la extensión (por ejemplo `aspectos .md`, `ia .md`, el ADR `0001-… .md`); renómbrenlos a la convención para que las herramientas de revisión los encuentren. Y conviene confirmar que los tres integrantes tienen acceso al repositorio, porque el historial de la semana solo muestra a dos.

## Semana 2 · Escenarios de calidad y restricciones

Buen trabajo en el núcleo: cinco escenarios con sus seis partes y medida numérica, árbol de utilidad con prioridades y un C4 de contexto como código con flechas etiquetadas, coherente con la sección 3.

Antes del corte 1 les conviene: (1) clasificar las restricciones (técnicas, organizativas, legales) y decir de dónde viene cada una — hoy R-03 y R-06 están redactadas como requisitos funcionales; (2) enlazar cada escenario desde su fila de aspectos (la tabla sigue con todo en «Pendiente»); (3) añadir la leyenda al diagrama C4; y (4) dar condición de carga a las medidas de EC-01 a EC-04, como ya hace EC-05.

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
