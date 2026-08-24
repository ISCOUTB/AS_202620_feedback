# Feedback S3 · ElMapita

Qué está bien: el ADR 0001 es el más completo de la semana — contexto ligado a los escenarios EC-01…EC-04, alternativas con pros/contras, decisión con estructura BE/FE, consecuencias con mitigaciones y reglas de límites. El esqueleto (backend NestJS + frontend Flutter) respeta el monolito modular del ADR, y el comando único `./scripts/dev.sh` está documentado y soportado por el script.

Qué corregir antes del corte 1 (semana 5):

1. La sección 4 de arc42 está VACÍA (solo el encabezado): trasladen allí la estrategia y sus tácticas, enlazando los escenarios; que no viva solo en el ADR y la matriz.
2. La matriz comparativa (muy buena y ponderada) debe mostrar los escenarios EC-01…EC-04 del árbol de utilidad: qué mejora/empeora cada estilo por escenario.
3. El ADR no es alcanzable: en `docs/aspectos.md` la columna ADR dice «Pendiente» y los escenarios no lo enlazan. Corrijan los dos enlaces.
4. Sin pipeline: las pruebas existen (`app.controller.spec.ts`, `app.e2e-spec.ts`, `widget_test.dart`) pero no hay evidencia de que estén en verde; agreguen un workflow antes del corte.
5. `docs/ia.md` sigue vacío desde S1: regístrense usos reales y rechazos.
6. En S3 solo una cuenta firma commits: los tres integrantes deben aparecer en el historial (arrastrado desde S1).
