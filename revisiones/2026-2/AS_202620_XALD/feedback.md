# Retroalimentación publicable · XALD

## Semanas 1 y 2

## Evidencia S1

Bien: repositorio con el nombre de la convención, los cuatro integrantes aparecen en el historial desde la primera semana, plantilla arc42 descomprimida y un registro de IA con entradas reales y rechazos justificados.

Corregir: la ficha del problema debe declarar usuarios, alcance y las dos tensiones de calidad enfrentadas (hoy son dos limitaciones sueltas, no un tradeoff); `docs/aspectos.md` debe ser la tabla de ocho columnas (hoy tiene dos); `docs/adr/` y `docs/c4/` deben existir en el repositorio (git no guarda carpetas vacías: usen un archivo de marcador); y limpien los restos de edición de herramientas de IA en los documentos.

## Evidencia S2

Bien: restricciones separadas de los requisitos, C4 de contexto como código con flechas etiquetadas, cinco ADR con contexto y consecuencias, tabla de aspectos con las ocho columnas, y los cuatro integrantes contribuyendo con un PR en el historial.

Corregir antes del corte 1 (es lo más urgente del curso): la entrega pedía los escenarios de calidad — entre 3 y 5, cada uno con sus seis partes (fuente, estímulo, artefacto, entorno, respuesta y medida numérica) — y el árbol de utilidad priorizado por impacto y riesgo; hoy la sección 10 del arc42 está vacía y solo hay una tabla de resúmenes en la sección 1. También: la sección 2 debe clasificar las restricciones técnicas, organizativas y legales con su origen (la Ley 1581 está citada fuera de la sección), la sección 3 debe coincidir con el C4 (el backend aparece en una y no en el otro), el C4 necesita leyenda, los ADR deben llamarse `NNNN-titulo-en-kebab-case.md`, y cada aspecto debe enlazar a su escenario.

## Semana 3

Qué está bien: la sección 4 de arc42 liga tácticas concretas a las metas de calidad, el ADR-006 tiene contexto, opciones, decisión y consecuencias, el README documenta el comando de verificación y el esqueleto Android/Kotlin coincide con los paquetes del ADR.

Qué corregir antes del corte 1 (semana 5):
1. Subir los escenarios de calidad y el árbol de utilidad (pendientes desde S2) y anclar a ellos la matriz comparativa; corregir en la matriz la referencia al «ADR 0001» (la decisión es el ADR-006).
2. Renombrar los seis ADR a `NNNN-titulo-en-kebab-case.md`.
3. En `docs/aspectos.md`, enlazar de verdad la columna ADR (incluido el ADR-006) y limpiar el resto `[cite: 1]`.
4. Registrar en `docs/ia.md` el trabajo de esta semana con lo aceptado y lo rechazado con motivo.

## Semana 4 · S4

El C4 en Mermaid es claro y coherente entre niveles, y los cinco módulos Gradle corresponden a la estructura dibujada. El CI ejecuta las pruebas en verde y la fila A-01 de aspectos está completa hasta Pruebas. Para el próximo corte: completar y verificar las secciones 3-6, 9, 10 y el glosario del arc42; asegurar que la prueba de corte vertical invoque explícitamente la persistencia; implementar o justificar el contenedor Backend XALD; añadir análisis estático con SonarCloud; y enriquecer los ADR con opciones evaluadas y trazabilidad a commits y pruebas.

## Semana 5 · CORTE1

Revisión preliminar antes del cierre: la base tiene módulos Android, C4, ADR, participación del equipo y CI en verde. Aún no se distingue la respuesta al reto del corte: faltan la etiqueta, el diagnóstico de la restricción asignada, una línea base realmente ejecutada, el cambio y la medición final contra el umbral. Completen las celdas pendientes de la tabla de aspectos y corrijan la diferencia entre el backend dibujado y el árbol implementado. El registro de IA debe indicar qué se aceptó, corrigió o rechazó específicamente en este corte.

## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Buena noticia primero: ya existe la etiqueta `corte-1`, sobre un commit de la noche antes del cierre. Y en esa noche el equipo hizo un trabajo real: completaron las secciones de alternativas de los seis ADR, alinearon el código con el backend que el diagrama C4 ya mostraba, corrigieron varias advertencias de seguridad que señalaba el análisis estático, y dejaron un registro de IA con el detalle de qué se aceptó y por qué.

Lo que falta, y es lo central del corte: todo ese trabajo mejora la arquitectura que ya tenían, pero no encontramos una restricción **nueva** diagnosticada, con su estado inicial medido, comparada contra alternativas en un ADR propio del reto, y con un resultado posterior medido contra un umbral. Eso es distinto de mejorar lo que ya existía, y es lo que pide este corte.

Dos detalles técnicos que vale la pena que revisen: la prueba que presentan como "corte vertical ejecutable" solo comprueba que `true` es igual a `true` — no demuestra que los cinco módulos se pasen datos entre sí. Y el pipeline de integración continua está configurado para dispararse en las ramas `experimental` y `main`, pero el proyecto vive en `master`: eso significa que los commits de la noche del cierre, incluida la propia etiqueta `corte-1`, no tienen un run de CI que los respalde directamente, aunque el código que traían ya se había probado en verde antes de fusionarse.

También revisamos el documento de correcciones que dejaron en el repositorio. La mayoría de lo que prometieron para antes del cierre (opciones evaluadas en los ADR, la carpeta del backend) sí se hizo y quedó verificado. Lo que no pudimos confirmar es que el corte vertical ejercite los cinco módulos con dobles de prueba, como afirma el documento — la prueba que encontramos no lo demuestra.
