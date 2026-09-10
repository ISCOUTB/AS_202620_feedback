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

## Semana 4 · S4

Entrega sólida de la semana 4: arc42 1-6, 9, 10 y glosario redactados con contenido propio, corte vertical AS-03 que atraviesa UI, lógica y persistencia, y fila de aspectos completa con pruebas en verde en CI. Para el primer corte, conviertan el C4 nivel 2 a código (puml, mmd o Structurizr) para que sea trazable y revisable, y añadan la integración con SonarCloud al pipeline según el contrato. Ejecuten y verifiquen el arranque con flutter run -d chrome para dejar evidencia de que el comando funciona. Los demás aspectos (AS-01, AS-02, AS-04) quedan pendientes de cortes ejecutables, como indica la propia tabla.

## Semana 5 · CORTE1

El repositorio muestra una línea base sólida: problema, escenarios, ADR, arc42, C4 y corte vertical AS-03 están documentados y el código del corte es coherente con la arquitectura declarada. El pendiente principal es crear correcciones.md en la raíz del commit calificado, con trazabilidad a los hallazgos S1-S4 y evidencia contrastada. También conviene dejar un run de CI asociado al hash de la entrega, porque los runs actuales son posteriores al cierre. Revisar el nombre del archivo C4 nivel 2.jpg para evitar espacios. Completar los cortes y mediciones pendientes de AS-01, AS-02 y AS-04 en las próximas semanas.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Se revisó de nuevo después del cierre y no hay cambios: el repositorio quedó exactamente igual a como estaba el 3 de septiembre, cuando se hizo la revisión preliminar. No hubo ningún commit nuevo entre esa fecha y el cierre del corte.

Esto significa que sigue faltando todo lo que se pidió para el reto: identificar la restricción, medir cómo estaba el sistema antes, escribir un ADR con la decisión, hacer el cambio de código y medir el resultado. La línea base (corte vertical de seguridad, AS-03) sigue firme y probada, pero eso ya se evaluó en semanas anteriores.

De paso, noten que un documento propio del equipo (`REVISION_CORREGIDA.md`, escrito en agosto) dice que ya habían eliminado unas carpetas residuales (`front_end`, `ejecutable`), pero esas carpetas todavía están en el repositorio.

Antes de la sustentación, sería importante que el equipo pueda mostrar avance real sobre el reto, aunque sea parcial, y explicar qué pasó durante estos días adicionales.
