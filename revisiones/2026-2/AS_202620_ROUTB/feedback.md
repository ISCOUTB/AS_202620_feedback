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

El repositorio conserva la base de semanas anteriores, pero la entrega del corte 1 no presenta avances del reto: no hay etiqueta corte-1, ni diagnóstico, ADR, implementación, pruebas o medición. Se recomienda: 1) crear la etiqueta en un commit anterior al cierre; 2) documentar el diagnóstico con línea base medible; 3) registrar el ADR del reto con alternativas y consecuencias; 4) implementar el cambio y añadir pruebas que cubran el escenario; 5) actualizar docs/aspectos.md y docs/ia.md; 6) configurar SonarCloud. La sustentación se evaluará en sesión.
