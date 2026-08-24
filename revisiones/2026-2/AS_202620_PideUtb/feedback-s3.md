# Feedback S3 · PideUtb

Lo que está bien: el ADR 0001 es de los mejor armados del curso (contexto real del equipo, alternativas con motivos, decisión y consecuencias), el README documenta el comando único de arranque y las pruebas, y el esqueleto ya tiene los paquetes de dominio del monolito modular con una prueba base razonable.

Qué corregir antes del corte 1 (semana 5):

- Ligar la sección 4 de arc42 a los escenarios priorizados: tácticas concretas por ESC-01/02/03 con su medida (hoy la motivación queda a nivel de atributo).
- Rehacer la matriz comparativa con filas por escenario del árbol de utilidad: qué escenario mejora y cuál empeora con cada estilo.
- Enlazar el ADR desde `docs/aspectos.md` (y dejar la tabla de 8 columnas del curso) y desde el escenario que motiva la decisión.
- Titular el ADR con la decisión («Usar monolito modular»), no con el tema.
- Añadir un workflow `.github/workflows/` que ejecute `pytest` y aportar el run en verde.
- Regularizar la estructura (`docs/arc42/`, `docs/c4/`) y registrar en `docs/ia.md` qué se rechazó y por qué.
