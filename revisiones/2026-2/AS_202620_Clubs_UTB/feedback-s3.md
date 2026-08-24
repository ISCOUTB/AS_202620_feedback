# Retroalimentación publicable · Clubs UTB (S3)

Qué está bien: la sección 4 justifica la estrategia hexagonal con tácticas nombradas (timeout, reintento, caché, índices), la matriz comparativa va fila por fila contra sus escenarios U1–U3 y C1–C3, y el ADR 0001 está aceptado con alternativas motivadas.

Qué corregir antes del corte 1 (semana 5):
1. El arranque no quedó documentado en el README y `backend/src/main.py` y `tests/test_health.py` están vacíos en la versión calificada: documenten el comando único de arranque y dejen la prueba con asserts reales.
2. Hagan verificable la prueba en verde: agreguen un pipeline o evidencia de ejecución.
3. Hagan alcanzable el ADR: enlácenlo desde `docs/aspectos.md` (con la tabla de 8 columnas) y desde el escenario U2 que lo motiva.
4. Actualicen `docs/ia.md` (sin cambios desde el 9 de agosto) registrando usos y qué se rechazó y por qué, y borren el residuo `docs/adr/.temp`.

Ojo: parte del trabajo llegó después del cierre y no contó para esta entrega; la próxima vez asegúrense de empujar antes de la medianoche del domingo.
