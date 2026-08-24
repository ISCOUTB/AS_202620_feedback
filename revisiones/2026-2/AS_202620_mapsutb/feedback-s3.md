# Feedback S3 · mapsutb (para publicar en el foro)

Buena entrega de esqueleto: Flutter arranca con `./scripts/start.sh`, hay prueba de humo en `test/app_smoke_test.dart`, y el ADR 0001 documenta cada patrón (Adapter, Repository, Strategy, Observer) con alternativas descartadas, motivo y consecuencias. La estrategia de solución liga cada escenario a un patrón concreto.

Falta antes del corte 1:
1. La matriz comparativa de los tres estilos (capas, hexagonal, monolito modular) contra el árbol de utilidad: la ficha S3 la pide y no existe en el repositorio.
2. Materializar la estructura que declara el ADR: `lib/` solo tiene `main.dart`; creen las carpetas `adapters/`, `repositories/`, `strategies/`, `services/` y `features/` (con `.gitkeep`).
3. Actualizar `aspectos.md` (todavía dice «Sin ADR aún») y enlazar el ADR desde el escenario que lo motiva.
4. Evidenciar la prueba en verde (pipeline o run) y registrar el uso de IA de esta semana en `docs/ia.md`.
5. Mover la etiqueta `corte-1` al commit real del corte y contribuir todos los integrantes: el historial sigue sin una integrante.
