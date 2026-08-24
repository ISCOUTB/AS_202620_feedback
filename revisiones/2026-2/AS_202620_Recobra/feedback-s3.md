# Feedback S3 · Recobra

- Gran reacción de última hora: ya hay esqueleto Node/Express con comando único (`npm install && npm start`), prueba automatizada, ADR renombrado a la convención y reescrito (hexagonal puro), sección 4 nueva, C4 como código en `docs/c4/` y `ia.md` con entrada de la semana.
- Pendiente antes del corte 1: crear los paquetes `domain/ports`, `application/use-cases` y el adaptador de persistencia que declaran el ADR y el README (hoy solo existe el adaptador HTTP), y subir el run en verde de la prueba.
- La matriz de §4.2 mejoró mucho, pero aún no es contra el árbol: hagan filas por escenario S1–S7 (qué mejora/empeora con cada estilo). Borren o alineen `matriz_arquitectura.md`, que sigue diciendo «hexagonal como monolito modular» y contradice el ADR.
- No borren ADR aceptados: si la decisión cambia, el anterior se marca «reemplazado» (CONTRATO §4).
- Enlacen el ADR desde `aspectos.md` (con la tabla de 8 columnas) y desde el escenario que lo motiva.
- Higiene urgente: `node_modules/` está versionado completo — añadan `.gitignore` y sáquenlo del historial.
