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

El contrato OpenAPI/AsyncAPI, la prueba de contrato y el ADR de integración ya están versionados, y la justificación de la estrategia híbrida frente a EC-01, EC-03 y EC-04 es sólida. Para que la prueba de contrato demuestre algo, falta la evidencia de que falla con un cambio incompatible: un run en rojo en el pipeline o el registro del cambio que la hizo fallar. También falta mostrar que el pipeline invoca esa prueba y aportar la evidencia pública de SonarCloud (línea del workflow, URL del run y URL del análisis con Quality Gate). En el commit calificado quedaron marcadores de conflicto de fusión en el README y en el ADR-0001, y enlaces a un ADR que no existe con ese nombre: conviene limpiarlos y validar que todos los enlaces resuelven. La tabla de aspectos necesita la columna de evidencia y los diagramas C4 y arc42 deberían usar los mismos nombres de módulo que el código. Revisen además que todas las flechas del nivel 2 indiquen protocolo y formato.
## Semana 6 · S6

Buen avance: el mapa de contextos, la tabla módulo a datos y el plan de corrección ya están en el repositorio, y la trazabilidad de A-01 enlaza ADR, C4, código y pruebas. Para cerrar el corte: tipifiquen cada relación del mapa con el vocabulario de la semana (núcleo compartido, cliente-proveedor, capa anticorrupción), no solo flechas. Registren el recorrido de la auditoría de propiedad (comandos, hash y rutas) y declaren como no conformidad la escritura de startAt y del estado de reproducción desde la persistencia de Session. Falta incorporar la sección 8 de arc42: el lenguaje ubicuo y el mapa existen, pero en documentos sueltos y con un include roto. Si los límites cambiaron desde el primer corte, suban el C4 nivel 3 y el ADR del reajuste. Completen la evidencia pública de SonarCloud (workflow, run y URL con Quality Gate) y las pruebas de EC-02 y EC-03.

## Semana 8 · S8

El repositorio ya tiene una base sólida: estructura de documentos, ADR iniciales, contratos y pruebas del backend y del cliente.; Lo que falta es la entrega de despliegue: sin URL pública, health check y hora de comprobación no se puede sustentar el entorno.; Versionen la infraestructura del entorno desplegado (compose, terraform o configuración del proveedor), no solo el devcontainer.; Añadan la sección 7 de arc42 con una caja por pieza y dónde se ejecuta, y recojan el límite de costo en la sección 2.; Escriban un ADR por decisión de plataforma, con la alternativa descartada y la capa gratuita verificada.; Documenten los logs estructurados con un ejemplo de línea y expongan una métrica ligada a un escenario de calidad.; Incluyan la estimación de costo mensual desde el volumen del escenario y el punto donde se rompe la capa gratuita.; Aporten el run de CI sobre la rama principal y la URL pública del análisis con su Quality Gate.; Corrijan el enlace de `docs/aspectos.md` al ADR de cliente Flutter y ajusten las columnas a las ocho del curso.; Agreguen al README la URL desplegada y el procedimiento de recreación del entorno desplegado.
