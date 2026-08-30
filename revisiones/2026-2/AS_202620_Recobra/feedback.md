# Retroalimentación publicable · Recobra

## Semanas 1 y 2

## Evidencia S1

El repositorio está en la organización, es público y el README funciona como ficha del problema con objetivos claros (centralizar, emparejar, notificar, trazabilidad). Les faltó casi todo el montaje: las dos tensiones de calidad, la tabla de ocho columnas en `docs/aspectos.md` (hoy es texto), la plantilla arc42 y las carpetas `docs/adr/` y `docs/c4/`. El archivo `docs/ia` está vacío: regístrenlo con usos reales (o declaren que aún no han usado IA) y pónganle la extensión `.md`.

## Evidencia S2

Las restricciones están bien trabajadas: clasificadas (técnicas, organizativas, legales), justificadas y vinculadas al escenario que las comprueba. El árbol de utilidad prioriza por impacto y riesgo con tabla de priorización, y la mayoría de escenarios tiene sus seis partes con medidas numéricas. Para corregir antes del corte 1: (1) la ficha pide entre 3 y 5 escenarios y tienen 7 (más sub-escenarios): prioricen y quédense con los más importantes; (2) el escenario S2 de seguridad no tiene medida numérica — exprésenla con cifra, unidad y condición; (3) el C4 no es un diagrama: `docs/C4.md` es solo texto, háganlo como código con leyenda y flechas etiquetadas; (4) actualicen `docs/aspectos.md` con la tabla de ocho columnas y enlaces a los escenarios; (5) llenen `docs/ia.md`; (6) organicen la documentación en `docs/arc42/`, `docs/adr/` y `docs/c4/`; (7) dos integrantes no aparecen en el historial.

## Semana 3

Qué está bien: el ADR 0001 sigue la convención y trae contexto, alternativas descartadas con motivo y consecuencias; el README documenta el arranque con un solo comando y `docs/ia.md` ya registra la semana 3 con lo aceptado y lo rechazado.

Qué corregir antes del corte 1 (semana 5):
1. Sección 4: faltan tácticas concretas ligadas a los escenarios S1–S7 (timeouts, reintentos, colas…); §4.4 son principios de paquetes, no tácticas.
2. La matriz comparativa de §4.2 no evalúa contra el árbol de utilidad (no hay filas por escenario); además `docs/matriz_arquitectura.md` quedó obsoleto y contradice el ADR: bórrenlo o alinéenlo.
3. Enlacen el ADR desde `docs/aspectos.md` y desde el escenario que lo motiva; hoy solo se alcanza desde §4.3.
4. Materialicen los paquetes `domain/ports` y `application/use-cases` que declaran el ADR y el README (solo existe el adaptador HTTP) y aporten evidencia del verde (workflow o run).
5. Higiene del repo: saquen `node_modules/` con un `.gitignore` y registren el ADR anterior como «reemplazado» en lugar de borrarlo (contrato del curso).

## Semana 4 · S4

El repositorio muestra avances sólidos en ADR, README y coherencia de escenarios. Para cumplir la evidencia S4, completen las secciones 5 y 6 de arc42 con bloques de construcción y vista de ejecución, agreguen el diagrama C4 nivel 2, y completen la tabla de aspectos con las ocho columnas. Configuren un pipeline de CI y etiqueten el commit de corte. Retiren node_modules del control de versiones y revisen el secreto en dependencias. La documentación base está bien encaminada; falta cerrar los requisitos específicos de la semana.
