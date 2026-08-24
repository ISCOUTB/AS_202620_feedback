# Retroalimentación publicable · DinamikUTB (S3)

Qué está bien: el ADR 0001 enuncia la decisión con contexto, alternativas motivadas y consecuencias, el README documenta el arranque único con `start.bat` y la estructura de paquetes coincide con el monolito modular decidido.

Qué corregir antes del corte 1 (semana 5):
1. La sección 4 no nombra tácticas concretas: liguen cada táctica a Q-01, Q-02 y Q-03 en `docs/arc42/04-solution-strategy.md`.
2. La matriz comparativa usa criterios genéricos con puntaje 1–5: háganla contra el árbol de utilidad, fila por fila con los escenarios Q-01…Q-03 (qué mejora y qué empeora con cada estilo).
3. Completen el enlace del ADR: la columna ADR de `docs/aspectos.md` sigue en «Pendiente» y el escenario Q-01 no lo enlaza (el ADR 0001 ya existe).
4. Evidencien el verde de las pruebas: hoy no hay pipeline ni evidencia de ejecución; agreguen un workflow antes del corte.
