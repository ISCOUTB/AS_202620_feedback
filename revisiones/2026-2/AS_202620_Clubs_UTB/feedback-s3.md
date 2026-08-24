# Feedback S3 · Clubs UTB

Qué está bien: la sección 4 elige la estrategia hexagonal justificada contra la disponibilidad y la restricción T4, con tácticas nombradas (timeout, reintento, caché, índices); la matriz compara los tres estilos fila por fila contra sus escenarios U1–U3 y C1–C3; el ADR 0001 está aceptado con contexto, alternativas con motivo, decisión y consecuencias; y los paquetes hexagonales existen y coinciden con el ADR.

Qué falta (antes del corte 1, semana 5):

1. El esqueleto ejecutable llegó tarde: el commit calificado tiene `main.py` y `test_health.py` vacíos y el README sin comando de arranque. Los empujaron 21 minutos después del cierre. Cuiden los cierres: lo que llega después no se califica.
2. Documenten en el README el comando único de arranque (uvicorn) y cómo se prueba.
3. Enlacen el ADR desde `docs/aspectos.md` (con la tabla de 8 columnas) y desde el escenario U2 que lo motiva.
4. El título del ADR debe enunciar la decisión («Usar arquitectura hexagonal»), no el tema.
5. Borren `docs/adr/.temp` y actualicen `docs/ia.md` (sin commits desde el 9 de agosto), incluyendo qué se rechazó y por qué.
