# Retroalimentación publicable · Clubs UTB

## Semana 1

- Está bien: el repositorio existe con el nombre correcto y es público; el problema de la gestión de clubes está bien descrito; `docs/ia.md` arrancó con contenido real.
- Falta: la ficha del problema (usuarios y alcance), las dos tensiones de calidad y la estructura (`docs/arc42/`, `docs/adr/`, `docs/c4/`, y recuperar el README).
- Corregir antes del corte 1: convertir `docs/aspectos.md` en la tabla de 8 columnas del curso con al menos un aspecto, y asegurar que los cuatro integrantes tengan acceso y firmen commits.

## Semana 2

- Está bien: las secciones 1, 2 y 3 de arc42 están redactadas y sólidas (metas con interesado, restricciones clasificadas y justificadas), el árbol de utilidad usa pares importancia/dificultad, el C4 de contexto está como código Mermaid con flechas etiquetadas, y los 6 escenarios tienen las seis partes con medidas numéricas.
- Falta: `docs/aspectos.md` sigue sin la tabla de aspectos ni enlaces a los escenarios; son 6 escenarios y se pedían entre 3 y 5; `docs/ia.md` no registró usos reales de la semana 2; la ficha del problema aún no declara las dos tensiones de calidad.
- Corregir antes del corte 1: elegir los 3–5 escenarios que se conservan, llenar `docs/aspectos.md` con su fila por aspecto y los enlaces, mover el C4 a `docs/c4/`, y declarar si hay o no restricciones legales.

## Semana 3

Qué está bien: la sección 4 justifica la estrategia hexagonal con tácticas nombradas (timeout, reintento, caché, índices), la matriz comparativa va fila por fila contra sus escenarios U1–U3 y C1–C3, y el ADR 0001 está aceptado con alternativas motivadas.

Qué corregir antes del corte 1 (semana 5):
1. El arranque no quedó documentado en el README y `backend/src/main.py` y `tests/test_health.py` están vacíos en la versión calificada: documenten el comando único de arranque y dejen la prueba con asserts reales.
2. Hagan verificable la prueba en verde: agreguen un pipeline o evidencia de ejecución.
3. Hagan alcanzable el ADR: enlácenlo desde `docs/aspectos.md` (con la tabla de 8 columnas) y desde el escenario U2 que lo motiva.
4. Actualicen `docs/ia.md` (sin cambios desde el 9 de agosto) registrando usos y qué se rechazó y por qué, y borren el residuo `docs/adr/.temp`.

Ojo: parte del trabajo llegó después del cierre y no contó para esta entrega; la próxima vez asegúrense de empujar antes de la medianoche del domingo.

## Semana 4 · S4

El repositorio muestra avances en documentación y un corte vertical mínimo, pero faltan secciones clave de arc42 (6, 9, 12), el C4 nivel 2, la tabla de aspectos con trazabilidad y el arranque documentado. Se recomienda completar la documentación exigida, añadir el pipeline de CI y verificar la prueba en verde. La estructura general es adecuada, con una desviación menor en el nombre del directorio C4.
