# Feedback S3 · TRACTAR (para publicar en el foro)

Muy buena entrega: la sección 4 liga tácticas a los escenarios priorizados, la matriz compara los tres estilos contra sus propios escenarios y restricciones, y el ADR 0001 tiene alternativas descartadas con motivo y consecuencias. El esqueleto Django arranca con `./run.sh` y los paquetes (`usuarios`, `vehiculos`, `viajes`, `facturacion`) coinciden con el monolito modular decidido.

Antes del corte 1:
1. Aportar evidencia del test en verde (pipeline en `.github/workflows/` o captura del run), hoy la prueba existe pero no se puede certificar.
2. Corregir los enlaces rotos (ADR → `10_requisitos_calidad.md` que no existe; `aspectos.md` → ruta `arc42.md#qs-…`).
3. Purgar `__pycache__/` y `db.sqlite3` del repositorio y ampliar `.gitignore`.
4. Registrar en `docs/ia.md` el uso de IA de esta semana con lo rechazado y por qué.
5. Urgente: que los cuatro integrantes contribuyan; el historial sigue siendo de una sola persona.
