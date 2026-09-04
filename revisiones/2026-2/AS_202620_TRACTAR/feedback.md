# Retroalimentación publicable · TRACTAR

## Semanas 1 y 2

## Evidencia S1

El repositorio no tenía commits antes del cierre de la semana 1, así que no hubo estado S1 que revisar: todo el montaje (ficha del problema, aspectos, registro de IA, plantilla arc42) se subió entre el 12 y el 16 de agosto, dentro de la ventana de la semana 2. Queda como semana no evaluable; si quieren que el docente lo considere recuperación, aclárenlo en el foro con el enlace al repositorio.

## Evidencia S2

Bien: secciones 1, 2 y 3 del arc42 redactadas sin texto de plantilla, restricciones clasificadas (técnicas, organizacionales y legales) y justificadas, cinco escenarios completos con sus seis partes y medida numérica, árbol de utilidad que prioriza por importancia y dificultad, y C4 de contexto.

Corregir antes del corte 1: la sección 1 debe declarar objetivos de negocio y decir a quién le importa cada uno (y revisar la tabla de interesados, que menciona nombres que no son del equipo); el ADR de `docs/adr/` debe llamarse `NNNN-titulo-en-kebab-case.md`; los enlaces de `docs/aspectos.md` apuntan a un archivo que no existe (`arc42/10_requisitos_calidad.md`) — hagan que cada escenario sea alcanzable desde su fila; entreguen el C4 también como código (el `workspace.dsl` citado no está en el repo); y en `docs/ia.md` registren qué propuestas rechazaron y por qué. Sobre todo: es urgente que todos los integrantes aparezcan en el historial de commits.

## Semana 3

Qué está bien: la sección 4 de arc42 liga tácticas a los escenarios, la matriz compara los tres estilos contra sus propios escenarios y restricciones, el ADR 0001 tiene alternativas descartadas con motivo y el esqueleto Django con sus módulos coincide con el monolito modular decidido.

Qué corregir antes del corte 1 (semana 5):
1. Completar la estructura mínima: crear `docs/c4/` para los diagramas C4 y mover `ficha_problema.md` a su carpeta.
2. Contribución: tres de cuatro integrantes siguen sin commits; todos deben aparecer en el historial antes del corte 1.
3. Registrar en `docs/ia.md` el trabajo de esta semana (ADR, matriz y esqueleto), incluyendo lo rechazado con motivo.

## Semana 4 · S4

La entrega S4 quedó incompleta al cierre: arc42 solo cubre secciones 1-4, falta el C4 nivel 2, el corte vertical no llega a persistencia y no hay glosario. El commit posterior añade C4 nivel 2, ADR 0002, persistencia y pruebas, pero el pipeline de HEAD está en rojo. Revisen que la documentación se suba antes del cierre y que el CI quede en verde. Completen docs/ia.md con lo que se rechazó y por qué. Distribuyan el trabajo: el historial muestra un solo autor. La fila A-01 de aspectos es un buen inicio; extiendan la trazabilidad al resto.

## Semana 5 · CORTE1

Revisión preliminar antes del cierre: la base incluye corte vertical, C4, ADR y pruebas, pero todavía no aparece una respuesta identificable al reto del corte. Falta fijar la etiqueta, documentar la restricción asignada, medir el estado inicial, registrar alternativas y decisión, implementar el cambio y contrastar el resultado con el umbral. La fila de aspectos existente corresponde a la evidencia anterior y el registro de IA no se actualiza desde agosto. El historial sigue concentrado en una persona. Antes del cierre, conviertan esos elementos en una cadena navegable y preparen cómo justificarán la medición y las alternativas descartadas.
