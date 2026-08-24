# Retroalimentación publicable · ElMapita (S3)

Qué está bien: el ADR 0001 está completo (contexto ligado a EC-01…EC-04, alternativas con pros/contras, consecuencias con mitigaciones), el esqueleto BE/FE respeta el monolito modular y `./scripts/dev.sh` está documentado como arranque único.

Qué corregir antes del corte 1 (semana 5):
1. La sección 4 de arc42 está vacía (solo el encabezado): trasladen allí la estrategia con tácticas ligadas a los escenarios; que no viva solo en el ADR y la matriz.
2. La matriz comparativa (bien ponderada) debe comparar contra los escenarios EC-01…EC-04 del árbol de utilidad, no contra criterios propios.
3. Hagan alcanzable el ADR: la columna ADR de `docs/aspectos.md` sigue «Pendiente» y los escenarios no lo enlazan.
4. `docs/ia.md` sigue vacío: registren usos reales y rechazos con motivo.
5. Repartan la contribución: en S3 solo una cuenta firma commits; procuren que todos aparezcan en el historial.
6. Evidencien el verde de las pruebas existentes con un pipeline o capturas de ejecución.
