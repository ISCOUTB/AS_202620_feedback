# Retroalimentación publicable · Recobra (S3)

Qué está bien: el ADR 0001 sigue la convención y trae contexto, alternativas descartadas con motivo y consecuencias; el README documenta el arranque con un solo comando y `docs/ia.md` ya registra la semana 3 con lo aceptado y lo rechazado.

Qué corregir antes del corte 1 (semana 5):
1. Sección 4: faltan tácticas concretas ligadas a los escenarios S1–S7 (timeouts, reintentos, colas…); §4.4 son principios de paquetes, no tácticas.
2. La matriz comparativa de §4.2 no evalúa contra el árbol de utilidad (no hay filas por escenario); además `docs/matriz_arquitectura.md` quedó obsoleto y contradice el ADR: bórrenlo o alinéenlo.
3. Enlacen el ADR desde `docs/aspectos.md` y desde el escenario que lo motiva; hoy solo se alcanza desde §4.3.
4. Materialicen los paquetes `domain/ports` y `application/use-cases` que declaran el ADR y el README (solo existe el adaptador HTTP) y aporten evidencia del verde (workflow o run).
5. Higiene del repo: saquen `node_modules/` con un `.gitignore` y registren el ADR anterior como «reemplazado» en lugar de borrarlo (contrato del curso).
