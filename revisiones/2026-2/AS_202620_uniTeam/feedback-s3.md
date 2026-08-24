# Feedback S3 · uniTeam (para publicar en el foro)

Buen nivel de documentación: la §4 de arc42 trae tácticas por escenario, la matriz compara los tres estilos contra SUS escenarios ESC-01…ESC-05 (no genérica), y el ADR-003 justifica la decisión con alternativas descartadas con motivo. La estructura de paquetes es coherente con la decisión.

Falta antes del corte 1:
1. Renombrar los ADR a `NNNN-titulo-en-kebab-case.md` (el 003 tiene espacio y «(1)») y marcar ADR-001 como reemplazado por ADR-002.
2. Enlazar el ADR-003 desde `aspectos.md` y desde el escenario que lo motiva.
3. Documentar en el README el comando único de arranque (hoy solo se documenta la prueba) y corregir `httpx2` en `requirements.txt`.
4. `docs/ia.md` sin entradas de esta semana: registrar el uso de IA con lo rechazado y por qué.
5. Contribución: solo una persona firmó los commits de esta semana; dos integrantes siguen sin aparecer en el historial.
6. Si pueden, montar el workflow de CI para que la prueba quede en verde verificable.
