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
