# Feedback S3 · TAIA (para publicar en el foro)

Buen trabajo de base: la sección 4 de arc42 sí liga estrategias concretas a sus escenarios S1-S5 y la matriz compara los tres estilos contra SU árbol de utilidad, no contra ventajas genéricas. El esqueleto es coherente con la decisión (módulos con domain/application/adapters) y el README documenta el arranque.

Falta antes del corte 1:
1. Renombrar `docs/adr/0001.md` a `0001-<titulo-en-kebab-case>.md` y darle título H1 y sección de contexto.
2. Corregir los enlaces rotos: `aspectos.md`, README y el escenario S1 apuntan a `0001-estilo-arquitectonico.md`, que no existe; el enlace del escenario es un placeholder.
3. Completar la Entrada 03 de `docs/ia.md` (falta aceptado/rechazado).
4. Montar el workflow de CI para que la prueba corra en cada push; hoy no hay `.github/workflows/` y el verde no es verificable.
