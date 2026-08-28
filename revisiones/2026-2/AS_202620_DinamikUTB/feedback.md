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

El repositorio cumple con la estructura mínima y la identidad. Se recomienda completar el diagrama C4 nivel 2 y asegurar que las secciones arc42 pendientes estén redactadas. Es necesario proporcionar evidencia de la ejecución del pipeline y del corte vertical para poder verificar esos criterios.
