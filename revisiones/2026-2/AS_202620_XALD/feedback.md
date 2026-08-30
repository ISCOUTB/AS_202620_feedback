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

El repositorio muestra avances en estructura y documentación inicial. Para cumplir la evidencia S4, es prioritario completar el diagrama C4 nivel 2 y llenar las columnas Código, Pruebas y Evidencia de aspectos.md. Revisen que todos los ADR incluyan opciones evaluadas y trazabilidad. Agreguen análisis estático SonarCloud al pipeline. Asegúrense de que las secciones 3-6, 9, 10 y 12 de arc42 estén redactadas y verificables. El corte vertical y su prueba necesitan evidencia de ejecución en verde.
