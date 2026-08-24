# Feedback S3 · ROUTB

Lo que está bien: el ADR 0001 es completo (contexto, alternativas con motivo de descarte, decisión, consecuencias con riesgos y trazabilidad), la matriz de decisión compara los tres estilos contra su propio árbol de utilidad, la sección 4 de arc42 da tácticas concretas por objetivo priorizado, y los paquetes del backend reflejan el monolito modular con módulos por dominio. `docs/ia.md` es referencia de cómo registrar uso de IA.

Qué corregir antes del corte 1 (semana 5):

- Enlazar el ADR desde el escenario de calidad que lo motiva (tabla 10.2); hoy solo se llega desde aspectos, §4 y §9.
- Documentar en el README el arranque con **un solo comando** (hoy son 6 pasos de instalación y pasos de ejecución separados).
- Añadir un workflow `.github/workflows/` que ejecute `pytest` y aportar el run en verde.
- Revisar el C4 de contexto (leyenda y flechas etiquetadas, pendiente desde S2).
- Detalle: hay una fila duplicada en la tabla de trazabilidad del ADR.
