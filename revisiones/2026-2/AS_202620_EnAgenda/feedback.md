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

El equipo ha avanzado en documentación arquitectónica: ADR, C4 y sección 10 están bien. Sin embargo, faltan completar secciones 9 y 12 de arc42, agregar código fuente con corte vertical, documentar arranque en README, completar la fila de aspectos y configurar CI. Revisar el ADR para incluir trazabilidad completa. El registro de IA es ejemplar.
