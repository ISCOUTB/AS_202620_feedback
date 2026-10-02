# Retroalimentación publicable · ROUTB

## Semana 1

El repositorio está bien montado: en la organización, público, con la estructura completa y la plantilla arc42 en Markdown. La ficha del problema describe usuarios y alcance con claridad.

Les falta declarar las dos tensiones de calidad que hacen interesante el problema (enfrenten dos atributos, por ejemplo tiempo de respuesta contra costo de infraestructura), armar la tabla de aspectos con las ocho columnas del curso (hoy tiene dos y sin ID) y dejar en `docs/ia.md` una entrada real: si aún no han usado IA, declárenlo, no lo dejen en «pendiente».

## Semana 2

Buen avance: cinco escenarios con cifras concretas, restricciones justificadas y el C4 de contexto está como código Mermaid, revisable en el repositorio.

Antes del corte 1, corrijan: cada escenario debe desglosar las seis partes (fuente, estímulo, artefacto, entorno, respuesta y medida) y la medida necesita cifra, unidad y condición de carga; el árbol de utilidad debe priorizar por impacto y riesgo y casar con los escenarios redactados; el C4 necesita leyenda y flechas etiquetadas (y un solo nodo para el sistema). Reubiquen los escenarios en la sección 10 (quedó vacía), completen las restricciones con categorías organizativas y legales, y enlacen cada escenario desde su fila de `docs/aspectos.md`, que sigue pendiente desde la semana 1, igual que el registro de IA.

## Semana 3

Qué está bien: la sección 4 da tácticas concretas ligadas a las prioridades del árbol de utilidad, el ADR 0001 compara los tres estilos contra el árbol con juicios por atributo y descarta alternativas con motivo, los paquetes del backend respetan el monolito modular del ADR y `docs/ia.md` registra la semana con lo aceptado y rechazado.

Qué corregir antes del corte 1 (semana 5):
1. Falta el enlace del ADR desde el escenario motivador: la tabla de escenarios 10.2 no enlaza la decisión (solo lo hace `aspectos.md`).
2. El README documenta la instalación y el arranque en pasos separados; dejen un único comando documentado.
3. La prueba `backend/tests/test_health.py` existe, pero sin workflow ni evidencia del run: añadan `.github/workflows/` con `pytest` y suban el verde.
4. Revisen el C4 de contexto (`docs/c4/context.md`): quedaron pendientes desde S2 la leyenda y las etiquetas de las flechas.

## Semana 4 · S4

Entrega S4 completa y bien orientada: arc42 1-6, 9, 10 y 12 redactados con contenido propio, C4 niveles 1 y 2 como código, corte vertical de registro con prueba en CI en verde, y fila 2 de aspectos trazable hasta pruebas. Para el primer corte: completen las secciones 7, 8 y 11 de arc42, llenen los huecos de las filas 1 y 3 de aspectos, integren SonarCloud al pipeline, enlacen cada ADR con el commit que lo implementa y registren una medición de línea base. El glosario y los escenarios de calidad están bien alineados con el dominio.

## Semana 5 · CORTE1

El proyecto presenta una línea base arquitectónica sólida con arc42 completo, C4 en tres niveles, ADR bien formados y un corte vertical funcional con pruebas de concurrencia. La trazabilidad en docs/aspectos.md es navegable y el repositorio cumple la estructura del contrato. Para el siguiente corte, aseguren que correcciones.md e ia.md sean verificables desde el repositorio, integren SonarCloud al pipeline y documenten el arranque con un solo comando real. También equilibren la distribución de commits para reflejar la colaboración del equipo.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

El reto quedó resuelto de forma correcta: identificaron un riesgo real (que dos personas reserven el mismo cupo al mismo tiempo), midieron que antes del cambio el sistema ni siquiera tenía ese endpoint, implementaron el control para que solo se acepten tantas reservas como cupos existan, y probaron con 20 intentos simultáneos sobre 4 cupos que efectivamente solo se aceptan 4 y ninguno queda en negativo, dentro del tiempo esperado. La cadena de trazabilidad queda completa. Dos cosas por mejorar: primero, no pudimos confirmar cuál fue la restricción individual que el curso les asignó — verifiquen que lo que resolvieron sea exactamente eso y no una interpretación propia del reto. Segundo, el análisis de SonarCloud lleva varios días en rojo sin resolverse; tener las pruebas en verde no es suficiente si el análisis estático sigue fallando. Para la próxima entrega, repartan mejor el trabajo: casi todo el reto de esta semana lo hizo una sola persona.

## Semana 7 · S7

El contrato en docs/openapi.json, la prueba test_openapi_contract.py, el ADR 0004 y la sección 6 de arc42 están versionados y bien encaminados.
Para cerrar la semana, hagan auditable el contrato: versión visible, dos rutas contrastadas con el código y el fragmento con esquemas.
Confirmen que el workflow invoca la prueba y adjunten el enlace del run.
Aportar la ejecución en rojo, o el cambio incompatible que la produjo, es lo que distingue una prueba real de una que siempre pasa.
Completen el nivel 2 del C4 etiquetando cada flecha con protocolo y formato, y dejen el análisis de SonarCloud con su Quality Gate enlazado.
## Semana 6 · S6

Buen avance: el mapa de contextos y la sección 8 recogen el lenguaje y los límites del dominio, y el C4 nivel 3 y los ADR están al día. Para cerrar el segundo corte: (1) publiquen la evidencia auditable de SonarCloud: archivo de configuración, línea del workflow que invoca el scanner, run exitoso para el hash revisado y URL del Quality Gate; (2) incorporen la tabla módulo a datos y la lista de no conformidades con su plan, dejando explícito qué se esperaba, dónde se buscó y qué se halló sobre el código actual; (3) completen el registro de IA con lo rechazado y su motivo. Revisen además que el arranque quede en un solo comando para facilitar la reproducibilidad.

## Semana 8 · S8

### Recomendaciones prioritarias

- Cierren la evidencia de SonarCloud: falta el paso que invoca el scanner en el workflow y la URL pública del análisis con su Quality Gate. Un enlace genérico al panel no acredita que el análisis corra.
- Dejen de editar ADR ya aceptados: cuando cambie una decisión, escriban un ADR nuevo y marquen el anterior como reemplazado. Hoy varios ADR se editaron después de aceptarse sin ese enlace.
- La URL del sistema y la respuesta del health check quedan pendientes de calificar en esta pasada porque se entregan por Moodle.

El avance de la semana es sólido: la infraestructura está versionada como código, el README explica cómo recrear el entorno, el pipeline de la rama principal volvió a verde, los logs tienen estructura con campos, existe una métrica consultable ligada al escenario de rendimiento, los secretos se toman de la configuración del proveedor, la estimación de costos trae supuestos y punto de ruptura, arc42 representa las plataformas reales en la sección 7 y recoge costo y «sin tarjeta» en la sección 2, y cada decisión de plataforma tiene su propio ADR con la alternativa descartada y la capa gratuita verificada. Mantengan ese nivel y cierren las dos no conformidades transversales.

## Semana 9 · S9 (revisión preliminar)

Esta revisión es preliminar y no tiene corte todavía: se califica la punta actual de la rama principal y la nota puede cambiar si empujan antes del cierre del 2026-10-05.

Al momento de revisar, la rama principal no tenía ningún commit nuevo desde la entrega anterior. Por la regla del contrato, el trabajo de semanas previas es línea base y no se vuelve a calificar por existir: las filas que describen la entrega S9 —la porción construida con apoyo de IA y su cadena, el ADR de esa porción, la prueba que falla ante el defecto, la medición del escenario y la entrada de `docs/ia.md` del periodo— quedan sin cumplir hasta que empujen la evidencia de esta semana. La única comprobación que sí se resuelve sobre el estado actual es el barrido de credenciales, que sigue limpio.

Para cerrar S9 antes del cierre necesitan: (1) una porción real del sistema construida con IA en el periodo, no un ejercicio aparte, con sus rutas de código y commits; (2) la fila de la tabla de aspectos que la recorre hasta el código, la prueba y la medición; (3) el ADR donde la decisión la argumenta el equipo con las restricciones del proyecto, no lo que propuso la herramienta; (4) una prueba que falle ante el defecto que cubre (run en rojo, prueba de mutación o procedimiento documentado); (5) la medición del escenario contrastada con su umbral; (6) el extracto de `docs/ia.md` con lo aceptado, lo corregido y al menos un rechazo con motivo técnico; (7) la auditoría de erosión sobre límites de contexto y propiedad de datos, con ubicación y corrección; (8) la verificación de las dependencias añadidas en el periodo contra su registro oficial; y (9) la decisión sobre el componente generativo: si no lo incorporan, el ADR que lo justifica, porque la ausencia de decisión no es la decisión de no hacerlo.

Siguen abiertas, además, las dos no conformidades transversales de semanas anteriores: el análisis estático no es auditable desde el pipeline —falta el paso que invoca el scanner y la URL pública con su Quality Gate— y varios ADR aceptados se editaron después sin declarar un ADR de reemplazo.
