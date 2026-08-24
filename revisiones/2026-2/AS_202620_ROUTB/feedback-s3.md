# Retroalimentación publicable · ROUTB (S3)

Qué está bien: la sección 4 da tácticas concretas ligadas a las prioridades del árbol de utilidad, el ADR 0001 compara los tres estilos contra el árbol con juicios por atributo y descarta alternativas con motivo, los paquetes del backend respetan el monolito modular del ADR y `docs/ia.md` registra la semana con lo aceptado y rechazado.

Qué corregir antes del corte 1 (semana 5):
1. Falta el enlace del ADR desde el escenario motivador: la tabla de escenarios 10.2 no enlaza la decisión (solo lo hace `aspectos.md`).
2. El README documenta la instalación y el arranque en pasos separados; dejen un único comando documentado.
3. La prueba `backend/tests/test_health.py` existe, pero sin workflow ni evidencia del run: añadan `.github/workflows/` con `pytest` y suban el verde.
4. Revisen el C4 de contexto (`docs/c4/context.md`): quedaron pendientes desde S2 la leyenda y las etiquetas de las flechas.
