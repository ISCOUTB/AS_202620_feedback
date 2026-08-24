# Feedback S3 · EnAgenda

Qué está bien: recuperaron la documentación de S3. La sección 4 ya elige la estrategia (monolito modular) con límites y consecuencias, el ADR 0001 es una decisión de estilo aceptada con contexto, tres alternativas con motivo, decisión y consecuencias, hay matriz comparativa propia y `aspectos.md` ya usa la tabla de 8 columnas.

Qué falta (antes del corte 1, semana 5):

1. El esqueleto no existe: el ADR promete `src/` con 6 módulos y pruebas en `tests/`, y el repositorio solo tiene un script demo en `docs/` y un `main.py` que importa un módulo que no existe. El README no documenta comando de arranque ni de prueba.
2. Construyan el esqueleto real con la estructura del ADR, una prueba en verde y el comando único en el README.
3. Renombren el ADR a `0001-usar-monolito-modular.md` (sin espacio, y con el nombre de lo que decide); arreglen los enlaces internos rotos.
4. La matriz debe comparar fila por fila contra sus escenarios EC-01…EC-05.
5. Enlacen el ADR desde la columna ADR de `aspectos.md` y desde los escenarios que lo motivan.
6. Todos los integrantes deben aparecer en el historial de la semana.
