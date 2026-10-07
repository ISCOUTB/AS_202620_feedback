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

El proyecto está sólido: repositorio correcto, documentación arc42/C4/ADR presente, corte vertical A-01 implementado y CI en verde. El pendiente principal es crear correcciones.md en la raíz del estado calificado, con una fila por hallazgo de S1-S4, indicando acción, evidencia y estado. Revisen también la consistencia del nombre de un integrante entre la declaración y el historial de git. Completen las secciones arc42 faltantes si la ficha S4 las exige. El PDF y la sustentación se verifican en el aula.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Ya existe la etiqueta `corte-1` y apunta a un commit anterior al cierre: eso quedó resuelto. Pero, revisando el repositorio completo hasta esa etiqueta, no encontramos ninguna señal de que el equipo haya recibido o trabajado la restricción nueva que pedía este corte: no hay un ADR nuevo, no hay una cifra de línea base medida, no hay una prueba nueva, y el pipeline de integración continua corre en verde pero sobre el mismo contenido de siempre, no sobre un cambio del reto. Lo que sí se hizo en esta semana fue terminar de integrar el corte vertical (que en rigor pertenece a la semana anterior), ajustar diagramas C4 y hacer limpieza de README y de la versión de Node en el CI.

Qué falta para la sustentación: quién puede explicar cuál fue la restricción asignada, qué se midió antes del cambio, qué decisión se tomó y con qué alternativas se comparó, y qué prueba demuestra que el cambio funciona — porque ninguna de esas cuatro cosas aparece hoy en el repositorio. Además, sigue pendiente conciliar el C4 de contenedores (describe cuatro contenedores) con la implementación real (un monolito de un solo proceso), y agregar en `docs/ia.md` una entrada propia de esta semana.

## Semana 7 · S7

El contrato OpenAPI/AsyncAPI con rutas y esquemas, la prueba de contrato, su ejecución en el pipeline y el ADR de integración están versionados, y la justificación de la estrategia híbrida frente a EC-01, EC-03 y EC-04 es sólida. Para que la prueba de contrato demuestre algo, falta la evidencia de que falla con un cambio incompatible: un run en rojo en el pipeline o el registro del cambio que la hizo fallar. Sigue pendiente la URL pública del análisis de SonarCloud con su Quality Gate, junto con la columna de evidencia en la tabla de aspectos y la limpieza de los marcadores de conflicto de fusión y de los enlaces a un ADR que no existe. Conviene que los diagramas C4 y arc42 usen los mismos nombres de módulo que el código y que todas las flechas del nivel 2 indiquen protocolo y formato.
## Semana 6 · S6

Buen avance: el mapa de contextos, la tabla módulo a datos y el plan de corrección ya están en el repositorio, y la trazabilidad de A-01 enlaza ADR, C4, código y pruebas. Para cerrar el corte: tipifiquen cada relación del mapa con el vocabulario de la semana (núcleo compartido, cliente-proveedor, capa anticorrupción), no solo flechas. Registren el recorrido de la auditoría de propiedad (comandos, hash y rutas) y declaren como no conformidad la escritura de startAt y del estado de reproducción desde la persistencia de Session. Falta incorporar la sección 8 de arc42: el lenguaje ubicuo y el mapa existen, pero en documentos sueltos y con un include roto. Si los límites cambiaron desde el primer corte, suban el C4 nivel 3 y el ADR del reajuste. Completen la evidencia pública de SonarCloud (workflow, run y URL con Quality Gate) y las pruebas de EC-02 y EC-03.

## Semana 8 · S8 (revisión definitiva)

La entrega de despliegue llegó y es la más completa del corte: infraestructura versionada (Dockerfile, compose y el workflow que publica la imagen), procedimiento de recreación enlazado desde el README, logs JSON con campos, una métrica ligada a los escenarios de sincronización, secretos tomados del almacén, estimación de costo con supuestos propios y punto de ruptura, la vista de despliegue con una caja por pieza y las restricciones de costo y tarjeta, y un ADR de plataforma con la alternativa descartada y la capa gratuita verificada.

Para cerrar del todo:
1. Pongan en verde el workflow de Flutter sobre la rama principal: es el único pipeline que falla en el último push.
2. Publiquen la URL pública del análisis estático con el estado del Quality Gate y alineen la organización del proyecto con la del curso.
3. Actualicen `docs/ia.md` con el uso de IA de esta semana.
4. Un ADR aceptado no se edita: cuando la decisión cambie, escriban un ADR nuevo que lo reemplace y marquen el anterior como reemplazado.

La URL del despliegue se entrega por Moodle y no se califica en esta pasada.

## Semana 9 · S9 (revisión definitiva)

Hay dos decisiones nuevas y una URL accesible. La prueba de sincronización calcula números fijos sin llamar al sistema, así que todavía no demuestra el comportamiento del producto. Conecten la cadena del aspecto con el ADR nuevo, código real, prueba que falle ante el defecto y medición. Precisen la auditoría y las propuestas de IA rechazadas.

## Semana 10 · Segundo corte (avance preliminar)

Antes del corte, identifiquen el escenario operativo asignado y midan una línea base reproducible. El health check responde, pero falta demostrar el flujo principal, corregir el pipeline Flutter y alinear la documentación con Dokploy. La sustentación y los niveles dependientes del reto quedan pendientes.
