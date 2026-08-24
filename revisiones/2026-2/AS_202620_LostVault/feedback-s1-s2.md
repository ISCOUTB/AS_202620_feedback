# Retroalimentación publicable · LostVault

## Semanas 1 y 2

## Evidencia S1

Buen punto de partida: el repositorio está en la organización, es público y tiene la ficha del problema con usuarios, alcance y propuesta clara, además de un registro de IA con contenido real. Les faltó la estructura de documentación que pide la semana (carpetas `docs/arc42/` con la plantilla, `docs/adr/` y `docs/c4/`), y la ficha no declara las dos tensiones de calidad enfrentadas: declaran disponibilidad como atributo prioritario, pero no un segundo atributo en tensión con él. La tabla de `docs/aspectos.md` debe tener las ocho columnas del curso con una fila iniciada, no solo texto narrativo.

## Evidencia S2

Las secciones 1, 2 y 3 de arc42 están redactadas con sustancia: objetivos de negocio, restricciones clasificadas y justificadas, y contexto con actores. Los cuatro escenarios tienen sus seis partes y medidas numéricas con cifra, unidad y condición de carga: muy bien. Para corregir antes del corte 1: (1) el árbol de utilidad ordena los atributos pero no los valora por impacto y riesgo; (2) el C4 de contexto solo existe como imagen — súbanlo como código y a `docs/c4/` para que sea revisable; (3) actualicen `docs/ia.md` con el uso de IA de esta semana e incluyan qué rechazaron y por qué; (4) repartan el historial: todo el trabajo aparece firmado por una sola cuenta.

## Semana 3

Qué está bien: ADR 0001 aceptado con alternativas descartadas con motivo, y README reescrito como guía del esqueleto con comando único y prueba inicial.

Qué corregir antes del corte 1 (semana 5):
1. Reescriban la sección 4 y la matriz comparativa ligándolas a sus escenarios 1-4, fila por escenario del árbol de utilidad (hoy describen los estilos en abstracto).
2. Enlacen el ADR 0001 desde `docs/aspectos.md` y desde los escenarios que lo motivan.
3. Creen los paquetes que declara el ADR (`lib/core` y `lib/features/…` con `.gitkeep`): hoy solo existe `lib/main.dart`, y borren los archivos residuales `front_end` y `ejecutable` de la raíz.
4. Actualicen `docs/ia.md` (última entrada del 08-ago) con los usos de S3 y lo rechazado con motivo; muevan el C4 a `docs/c4/`.
5. Evidencien la prueba en verde (pipeline o run) antes del corte 1.
