# Retroalimentación publicable · TAIA

## Semana 1

Muy buen inicio: ficha del problema con usuarios y alcance claros, tabla de aspectos con las ocho columnas, registro de IA ejemplar (con lo aceptado, lo rechazado y su verificación) y plantilla arc42 montada.

Les falta crear `docs/adr/` y `docs/c4/`, declarar en la ficha las dos tensiones de calidad que hacen interesante el problema (por ejemplo, rapidez de captura frente a privacidad del contexto que se envía al LLM), y que los demás integrantes empiecen a aparecer en el historial.

## Semana 2

La sección 1 está muy bien lograda (requisitos con horizonte MVP, objetivos de calidad con métricas, interesados con expectativas), las restricciones están muy bien justificadas y los cinco escenarios desglosan las seis partes.

Antes del corte 1: completen la sección 3 (quedó con texto de plantilla), denle medida numérica al escenario de sustitución del LLM, prioricen el árbol de utilidad por impacto y riesgo, muevan los escenarios y el árbol a la sección 10 del arc42 (hoy están en `docs/calidad/` y la sección quedó vacía), reemplacen el PNG del C4 por un diagrama como código (Mermaid) con leyenda y flechas etiquetadas, añadan restricciones legales y enlacen los escenarios desde `docs/aspectos.md`. Crear `docs/adr/` sigue pendiente desde la semana 1.

## Semana 3

Qué está bien: la sección 4 liga la estrategia a los escenarios S1–S5 con mecanismos concretos, la matriz del ADR compara los tres estilos contra su árbol de utilidad con justificación por escenario, `run.bat` documenta el arranque en un solo comando y los paquetes `domain/application/adapters` por módulo coinciden con el ADR.

Qué corregir antes del corte 1 (semana 5):
1. Renombren `docs/adr/0001.md` a la convención `0001-<kebab-case>.md` y corrijan los enlaces rotos que apuntan a `0001-estilo-arquitectonico.md` (en `aspectos.md` y README) y el placeholder `ruta/al/escenario.md`.
2. El ADR no tiene título que enuncie la decisión ni sección de contexto: complétenlos.
3. Completen la entrada 03 de `docs/ia.md` anotando qué se aceptó y qué se rechazó con su motivo.
4. Monten un workflow para que `backend/tests/test_entrega3.py` corra en cada push y quede evidencia del verde.

## Semana 4 · S4

La entrega tiene un corte vertical claro (HTTP → caso de uso → dominio → persistencia en memoria) y la fila A-01 de aspectos está completa y navegable. Para el primer corte: (1) dejen visible el contenido de las secciones 3, 4, 9, 10 y 12 de arc42 y eliminen restos de plantilla (el archivo aún se llama template); (2) agreguen al ADR-0001 la trazabilidad exigida (requisito, C4, commit, pruebas); (3) ejecuten pytest y suban el run en verde o configuren GitHub Actions, porque hoy no hay evidencia de CI; (4) ajusten el C4 nivel 2 para marcar App Móvil y Base de Datos como objetivo, o no dibujarlas como contenedores actuales. El README documenta bien el arranque con run.bat. Sigan así.

## Semana 5 · CORTE1

La entrega no muestra evidencia del reto de línea base en el repositorio.
1) Crear la etiqueta corte-1 en el commit a calificar.
2) Registrar la restricción asignada y su impacto en requisitos, C4 y código.
3) Medir el estado inicial con herramienta y procedimiento.
4) Escribir el ADR del reto con alternativas, fuerzas, decisión y consecuencias.
5) Implementar el cambio y probarlo de extremo a extremo.
6) Ejecutar las pruebas en CI y adjuntar el run.
7) Contrastar el resultado con el umbral del escenario.
8) Completar la fila del aspecto en aspectos.md.
9) Registrar en ia.md la salida de IA de este corte.
10) Entregar el PDF en Moodle.
