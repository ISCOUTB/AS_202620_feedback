# Retroalimentación publicable · Verifacts

## Semanas 1 y 2

Hola equipo: por decisión del profesor, sus evidencias S1 y S2 se revisaron sobre el estado actual
del repositorio (excepción única: su primer commit llegó después de los cierres).

Lo que está bien: repositorio público con la convención, ficha del problema con usuarios y alcance,
restricciones justificadas y separadas de los requisitos, contexto coherente con el C4 (mermaid
con flechas etiquetadas), un ADR bien formado con opciones evaluadas y el README con instrucciones
de ejecución.

Lo que falta y es urgente para el corte 1:

- **Los 5 escenarios de calidad que declara su PDF de entrega no están en el repositorio.** El
  repositorio es la entrega: suban `docs/escenarios-de-calidad.md` con cada escenario en sus seis
  partes (fuente, estímulo, artefacto, entorno, respuesta, medida numérica).
- Priorizar el árbol de utilidad por impacto y riesgo (hoy es una lista plana de atributos).
- La tabla de aspectos con las 8 columnas y enlaces hasta la evidencia (hoy es narrativa).
- Leyenda en el C4 y dos tensiones de calidad enfrentadas en la ficha del problema.
- El registro de IA como uso real (qué se usó, qué se rechazó y por qué), en `docs/ia.md`.
- Los tres integrantes con commits en el repositorio.

Alinéense también a la estructura mínima del curso: `docs/arc42/` como directorio, `docs/c4/` para
los diagramas y `docs/ia.md` en minúsculas.

## Semana 3

Qué está bien: el ADR 0001 tiene contexto, alternativas descartadas con motivo, decisión y consecuencias, la estructura de paquetes coincide con el monolito modular y la documentación arc42 quedó organizada en carpetas.

Qué corregir antes del corte 1 (semana 5):
1. Completar la sección 4 de arc42 con tácticas concretas ligadas a cada escenario Q-01…Q-05 (hoy son principios genéricos).
2. Rehacer `docs/matriz-estilos.md` contra las ramas de su árbol de utilidad, escenario por escenario.
3. Enlazar el ADR desde `docs/aspectos.md` y desde el escenario que lo motiva, y convertir `docs/IA.md` en el registro de uso de IA (aceptado/rechazado con motivo).
4. Documentar el comando único de arranque en el README (existe `run.py`, no se menciona) y acomodar la estructura mínima (`docs/c4/`).
5. Contribución: los tres integrantes deben aparecer en el historial antes del corte 1.

Ojo: parte del trabajo llegó después del cierre y no contó para esta entrega; la próxima vez asegúrense de empujar antes de la medianoche del domingo.

## Semana 4 · S4

Qué está bien: la documentación arc42 (1–6, 9, 10) está redactada con contenido propio, la sección 9 enlaza el ADR, el glosario tiene términos del dominio y los C4 de contexto y contenedores están como código Mermaid y son coherentes entre sí. El README documenta el arranque con un solo comando.

Qué corregir antes del corte 1 (semana 5):
1. El corte vertical al cierre solo cubría `GET /health` (sin lógica ni persistencia); el recorrido completo y su prueba llegaron después del cierre y no contaron para esta evidencia. Para el corte 1 ya está avanzado: asegúrense de empujar a tiempo.
2. La tabla de `docs/aspectos.md` no usa las 8 columnas del curso (falta la cadena requisito-C4-ADR-código): rehacerla y hacer navegable la fila completa hasta Pruebas.
3. Aportar evidencia de CI: la URL del run citada en `aspectos.md` da 404 y no hay runs visibles. Un enlace al run en verde (o ejecutar las pruebas en la sustentación) cierra la fila.
4. Limpiar la basura versionada: `__pycache__/`, `*.pyc`, archivos duplicados `« (1).py»` y PDFs en la raíz (el `.gitignore` ya se corrigió, pero lo versionado sigue en el historial).
5. Sigue pendiente desde S1: que el tercer integrante aparezca en el historial de commits.

## Semana 5 · CORTE1

Revisión preliminar antes del cierre: el repositorio mejoró la línea base con un recorrido completo y su prueba, pero todavía no presenta la respuesta al reto del primer corte. Falta crear la etiqueta, identificar la restricción asignada, medir el estado inicial, registrar la decisión en un ADR nuevo, implementar el cambio y comparar el resultado con el umbral. El PDF versionado tiene una sola página y describe la evidencia anterior, no el reto actual. También faltan un run público de CI, el registro de IA de esta etapa y contribución verificable del tercer integrante.
