# Feedback S3 · Verifacts (para publicar en el foro)

Avances reales: el ADR 0001 tiene contexto, alternativas descartadas con motivo, decisión y consecuencias; la estructura de paquetes (`api`, `analysis`, `content`, `scoring`) es coherente con el monolito modular; la prueba de health existe y `run.py` permite arrancar. La documentación arc42 quedó organizada en carpetas y ya subieron los escenarios de calidad.

Falta antes del corte 1:
1. Respetar el cierre: 15 commits entraron después de la medianoche (borrado y recreación de documentos) y no se califican.
2. Tácticas concretas por escenario en la §4 (hoy son principios genéricos) y matriz comparativa anclada a las ramas del árbol de utilidad.
3. Enlazar el ADR desde `aspectos.md` y desde el escenario que lo motiva.
4. Documentar en el README el comando único de arranque (hoy termina en la creación del venv).
5. Título del ADR como decisión («Usar monolito modular») y estado «aceptado».
6. `docs/IA.md` debe registrar los usos de IA con aceptado/rechazado, no la estrategia del producto.
7. Urgente: que contribuyan los tres integrantes antes del corte 1.
