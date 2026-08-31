# Retroalimentación publicable · PideUtb

## Semanas 1 y 2

## Evidencia S1

El repositorio está en la organización y es público (recuerden mantenerlo así: al inicio estuvo privado). La ficha del problema declara usuarios y alcance, y el registro de IA existe. Les faltó: las dos tensiones de calidad en la ficha, la tabla de ocho columnas en `docs/aspectos.md` (hoy es solo texto), la plantilla arc42 en `docs/arc42/` y las carpetas `docs/adr/` y `docs/c4/`. Pasen la ficha a Markdown dentro del repositorio: un PDF no se puede revisar con la misma facilidad.

## Evidencia S2

Excelente semana: las secciones 1, 2 y 3 de arc42 están completas y bien redactadas, los cinco escenarios tienen sus seis partes con medidas numéricas, el árbol de utilidad prioriza por impacto y riesgo con una convención explícita, y el C4 de contexto está como código Mermaid con flechas etiquetadas. Para el corte 1: (1) muevan la documentación a `docs/arc42/` y el C4 a `docs/c4/`; (2) revisen las anclas de los enlaces en `docs/aspectos.md` (varias usan guiones de menos y no llevan al escenario); (3) en `docs/ia.md` registren qué rechazaron de lo que propuso la IA y por qué; (4) repartan la contribución: todo el trabajo de esta semana está firmado por una sola cuenta y un integrante no aparece en el historial.

## Semana 3

Qué está bien: ADR 0001 bien armado (contexto real, alternativas descartadas con motivo, decisión y consecuencias), arranque con un solo comando documentado en el README y esqueleto con paquetes de dominio del monolito modular.

Qué corregir antes del corte 1 (semana 5):
1. Liguen la sección 4 del arc42 a los escenarios priorizados ESC-01/02/03 con tácticas por escenario (hoy la motivación queda a nivel de atributos del árbol).
2. Rehagan la matriz comparativa con filas por escenario del árbol de utilidad: qué escenario mejora y cuál empeora con cada estilo.
3. Enlacen el ADR 0001 desde `docs/aspectos.md` (usando la tabla de 8 columnas del curso) y desde el escenario que lo motiva.
4. Añadan un workflow en `.github/workflows/` que ejecute `pytest` y aporten el run en verde.
5. Registren en `docs/ia.md` qué se rechazó y por qué; muevan `arc42.md` a `docs/arc42/` y el C4 a `docs/c4/`.
6. Contribuyan todos los integrantes: esta semana solo aparecieron dos cuentas en el historial.

## Semana 4 · S4

El repositorio no permite verificar la mayoría de criterios porque el árbol de archivos está truncado y no incluye docs/ ni código fuente. Se recomienda no versionar .venv-1 y subir evidencia completa de docs/arc42, docs/c4, docs/adr, docs/aspectos.md, docs/ia.md y README.md. El commit calificado es correcto en fecha. Falta confirmar organización y CI.
