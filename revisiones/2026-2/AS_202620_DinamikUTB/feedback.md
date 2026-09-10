# Retroalimentación publicable · DinamikUTB

## Semana 1

- Está bien: estructura completa desde la semana 1 (arc42 con plantilla, adr, c4, aspectos, ia), `docs/aspectos.md` con la tabla de 8 columnas y 6 aspectos, `docs/ia.md` con una entrada real, y la ficha del problema con usuarios y alcance.
- Falta: una segunda tensión de calidad (solo declararon consistencia vs. disponibilidad), y que los cuatro integrantes firmen commits.
- Corregir antes del corte 1: declarar las dos tensiones y preferir la ficha en Markdown dentro del repositorio (hoy es un PDF).

## Semana 2

- Está bien: secciones 1, 2 y 3 redactadas y sin texto de plantilla; restricciones clasificadas (técnicas, organizativas, legales) y justificadas; 3 escenarios con sus seis partes y medidas numéricas (100 %, 100 %, 80 %); árbol de utilidad con impacto y riesgo técnico; C4 de contexto como PlantUML con leyenda y flechas etiquetadas; aspectos enlazando escenarios.
- Falta: enlazar los escenarios con hipervínculos reales desde `docs/aspectos.md` (hoy son ID de texto), registrar en `docs/ia.md` qué se rechazó de la IA y por qué, y equilibrar la participación (casi todo el trabajo de la semana lo subió una sola persona).
- Corregir antes del corte 1: definir cómo se medirán los escenarios (herramienta y carga) y repartir los commits de la próxima entrega entre los cuatro.

## Semana 3

Qué está bien: el ADR 0001 enuncia la decisión con contexto, alternativas motivadas y consecuencias, el README documenta el arranque único con `start.bat` y la estructura de paquetes coincide con el monolito modular decidido.

Qué corregir antes del corte 1 (semana 5):
1. La sección 4 no nombra tácticas concretas: liguen cada táctica a Q-01, Q-02 y Q-03 en `docs/arc42/04-solution-strategy.md`.
2. La matriz comparativa usa criterios genéricos con puntaje 1–5: háganla contra el árbol de utilidad, fila por fila con los escenarios Q-01…Q-03 (qué mejora y qué empeora con cada estilo).
3. Completen el enlace del ADR: la columna ADR de `docs/aspectos.md` sigue en «Pendiente» y el escenario Q-01 no lo enlaza (el ADR 0001 ya existe).
4. Evidencien el verde de las pruebas: hoy no hay pipeline ni evidencia de ejecución; agreguen un workflow antes del corte.

## Semana 4 · S4

La documentación arc42 y el C4 están bien avanzados y el corte vertical es trazable en el código. Para el primer corte: enlacen el ADR-0002 desde la sección 9 y añadan trazabilidad con commits y pruebas en los ADR. Ejecuten el pipeline y dejen visible el run en verde como evidencia de las pruebas. Completen la fila de aspectos con enlaces verificables. Eviten commits después del cierre; el arranque con start.bat debe quedar cerrado antes. El glosario y la coherencia C4-código son un buen punto de partida.

## Semana 5 · CORTE1

El proyecto tiene una base sólida: README completo, ADR bien formados, estructura modular y código de corte vertical. Para el compendio S5 falta: completar las secciones 07 y 08 de arc42, que están vacías; asegurar que correcciones.md en el hash calificado sea verificable con enlaces a commits/pruebas; y adjuntar evidencia de CI (URL de runs) que respalde el estado. También conviene revisar docs/aspectos.md e ia.md para que sus columnas sean navegables. Los commits posteriores al cierre deben evitarse; si corrigen hallazgos, se registran como tardíos.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Buenas noticias primero: el pipeline sigue en verde antes del cierre y `docs/ia.md` sí tiene una entrada fechada de esta semana con su justificación, así que ese punto queda resuelto. Lo que preocupa es que el trabajo que hicieron en esta semana (el ADR-0003 sobre el motor de base de datos) formaliza una decisión que ya venía pendiente desde varias semanas atrás, no responde a la restricción nueva que debía asignárseles para este corte. No encontramos en el repositorio ningún diagnóstico de esa restricción, ninguna cifra de línea base medida, ni un resultado comparado contra un umbral. Tampoco existe todavía la etiqueta `corte-1`.

Sobre `correcciones.md`: lo leímos completo. Es una autoevaluación de las semanas 1 a 4 donde ustedes mismos marcan todo como "Cumple", pero esas semanas ya fueron calificadas y no se vuelven a calificar por existir el documento — necesitábamos que el archivo respondiera a la revisión preliminar de este corte (semana-05-corte1), y no encontramos ningún punto que lo hiciera. Para la próxima entrega, si quieren disputar una fila concreta de una revisión ya publicada, cítenla y aporten la evidencia puntual que la contradice, en vez de una lista general de "cumple" sin evidencia verificable.

Preparen para la sustentación: cuál era la restricción asignada, qué midieron antes de cualquier cambio y con qué procedimiento, y por qué el ADR-0003 no aparece conectado a esa restricción.
