# Retroalimentación publicable · EnAgenda (S3)

Qué está bien: la sección 4 ya elige el monolito modular con límites y consecuencias, el ADR es una decisión de estilo aceptada con alternativas motivadas y `aspectos.md` ya usa la tabla de 8 columnas.

Qué corregir antes del corte 1 (semana 5):
1. El esqueleto prometido no existe: creen `src/` con los módulos del ADR (eventos, invitaciones, tareas, agenda, presupuesto, panel, compartido) y retiren los scripts sueltos de `docs/` (`main.py` importa un módulo inexistente).
2. Documenten en el README el comando único de arranque y agreguen una prueba en verde: el ADR promete `tests/` y hoy no hay ninguna.
3. Renombren el ADR a algo como `0001-usar-monolito-modular.md`: el nombre actual tiene espacio, no pasa el filtro y ya no corresponde a lo que decide; arreglen los enlaces internos rotos.
4. La matriz comparativa no referencia los escenarios EC-01…EC-05: pongan una fila por escenario del árbol de utilidad.
5. Hagan alcanzable el ADR: la columna ADR de `aspectos.md` sigue «Pendiente» y `10-requisitos-de-calidad .md` no lo enlaza.
6. Repartan la contribución: en S3 faltó un integrante en el historial (2 de 3).
