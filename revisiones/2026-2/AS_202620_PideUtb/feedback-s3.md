# Retroalimentación publicable · PideUtb (S3)

Qué está bien: ADR 0001 bien armado (contexto real, alternativas descartadas con motivo, decisión y consecuencias), arranque con un solo comando documentado en el README y esqueleto con paquetes de dominio del monolito modular.

Qué corregir antes del corte 1 (semana 5):
1. Liguen la sección 4 del arc42 a los escenarios priorizados ESC-01/02/03 con tácticas por escenario (hoy la motivación queda a nivel de atributos del árbol).
2. Rehagan la matriz comparativa con filas por escenario del árbol de utilidad: qué escenario mejora y cuál empeora con cada estilo.
3. Enlacen el ADR 0001 desde `docs/aspectos.md` (usando la tabla de 8 columnas del curso) y desde el escenario que lo motiva.
4. Añadan un workflow en `.github/workflows/` que ejecute `pytest` y aporten el run en verde.
5. Registren en `docs/ia.md` qué se rechazó y por qué; muevan `arc42.md` a `docs/arc42/` y el C4 a `docs/c4/`.
6. Contribuyan todos los integrantes: esta semana solo aparecieron dos cuentas en el historial.
