# Retroalimentación publicable · AudioShare

## Semana 1

- Está bien: el repositorio existe, es público y el problema de AudioShare (audio en tiempo real por Wi-Fi) está descrito con un prototipo claro; `docs/ia.md` arrancó con contenido real.
- Falta: la ficha del problema no dice quiénes son los usuarios ni cuáles son las dos tensiones de calidad.
- Corregir antes del corte 1: montar la estructura completa (`docs/arc42/` con plantilla, `docs/adr/`, `docs/c4/`), poner `docs/aspectos.md` como la tabla de 8 columnas del curso y asegurar que las cuatro personas tengan acceso y firmen commits.

## Semana 2

- Está bien: 4 escenarios de calidad con medidas numéricas con unidad, un árbol de utilidad con prioridades y escenarios enlazados desde el aspecto, C4 de contexto como código Mermaid, restricciones separadas de los requisitos y `docs/ia.md` actualizado.
- Falta: cada escenario debe declarar fuente, artefacto y entorno (hoy solo tienen estímulo, respuesta y medida); las restricciones deben clasificarse (técnica, organizativa, legal) y una de ellas es en realidad un requisito funcional; los objetivos de la sección 1 deben decir a quién le importan.
- Corregir antes del corte 1: alinear el C4 con la sección 3 (misma red Wi-Fi, mismo moderador), añadir leyenda al diagrama, y empezar a registrar en `docs/ia.md` qué se rechazó de la IA y por qué.

## Semana 3

Qué está bien: el ADR 0001 está completo (contexto, alternativas con motivo, decisión y consecuencias), el README documenta el arranque con un solo comando y el esqueleto monolito modular con paquetes por frontera coincide con lo decidido.

Qué corregir antes del corte 1 (semana 5):
1. La sección 4 quedó desincronizada: aún declara «pendiente» la selección del estilo que el ADR ya decidió; actualícenla y nombren tácticas concretas contra EC-01…EC-04.
2. Rehagan la matriz comparativa contra el árbol de utilidad: una fila por escenario (EC-01…EC-04) que diga qué mejora y qué empeora con cada estilo.
3. Hagan alcanzable el ADR: enlácenlo desde `docs/aspectos.md` (además, con la tabla de 8 columnas) y desde el escenario que lo motiva; reemplacen el «EC-nn» del ADR por el escenario real.
4. Registren en `docs/ia.md` qué se rechazó y por qué en cada uso (arrastrado desde S2).

## Semana 4 · S4

La documentación arc42 y los diagramas C4 están avanzados, pero el corte vertical no atraviesa persistencia y el C4 nivel 2 dibuja contenedores que aún no existen en el código. La sección 9 debe enlazar los ADR reales en docs/adr/ en lugar de repetirlos o crear ADR sin archivo. Completen la fila de aspectos con las columnas Requisito y C4, y citen la prueba del recorrido (tests/a01.test.ts) en la celda de Pruebas. El README debería declarar un único comando de arranque. Configuren integración continua y dejen evidencia del run en verde. Revisen que el ADR-0001 refleje el estado actual o creen uno nuevo si la decisión cambió.

## Semana 5 · CORTE1

El proyecto presenta una base arquitectónica sólida: el monolito modular está documentado en ADR y la implementación del corte A-01 es coherente con arc42, C4 y las pruebas automatizadas. El CI corre en verde y respalda el estado evaluado. La carencia principal del corte es la ausencia de correcciones.md en la raíz del repositorio, exigido como índice de verificación de correcciones de S1 a S4. Se recomienda crear ese archivo, enlazando cada hallazgo previo con la ruta, sección, prueba o run que lo resuelve, y declarar el estado de cada corrección. También conviene aportar la evidencia del análisis estático si la rúbrica lo pide. En general, el entregable está al día y listo para sustentación.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Ya existe la etiqueta `corte-1` y apunta a un commit anterior al cierre: eso quedó resuelto. Pero, revisando el repositorio completo hasta esa etiqueta, no encontramos ninguna señal de que el equipo haya recibido o trabajado la restricción nueva que pedía este corte: no hay un ADR nuevo, no hay una cifra de línea base medida, no hay una prueba nueva, y el pipeline de integración continua corre en verde pero sobre el mismo contenido de siempre, no sobre un cambio del reto. Lo que sí se hizo en esta semana fue terminar de integrar el corte vertical (que en rigor pertenece a la semana anterior), ajustar diagramas C4 y hacer limpieza de README y de la versión de Node en el CI.

Qué falta para la sustentación: quién puede explicar cuál fue la restricción asignada, qué se midió antes del cambio, qué decisión se tomó y con qué alternativas se comparó, y qué prueba demuestra que el cambio funciona — porque ninguna de esas cuatro cosas aparece hoy en el repositorio. Además, sigue pendiente conciliar el C4 de contenedores (describe cuatro contenedores) con la implementación real (un monolito de un solo proceso), y agregar en `docs/ia.md` una entrada propia de esta semana.
