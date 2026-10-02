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

El proyecto avanza bien en contenido: la documentación arc42, los ADR, el C4 y el corte vertical están sólidos y el pipeline pasa. El punto crítico es la ausencia de correcciones.md, que es obligatorio para esta entrega. Deben crearlo en la raíz, documentando cómo responden a los hallazgos de S1-S4. También asegúrense de subir el PDF a Moodle y preparen la sustentación. Revisen la consistencia de nombres de autor en git para facilitar la evaluación de contribución.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

No encontramos una respuesta identificable al reto de este corte. El repositorio no tiene la etiqueta `corte-1` y no tuvo ningún cambio entre la revisión de antes del cierre y el cierre mismo: quedó igual. Sigue faltando, en este orden: (1) decir cuál fue la restricción asignada y medir cómo estaba el sistema antes de tocarlo; (2) un ADR nuevo que compare alternativas para resolver esa restricción; (3) el cambio en sí, implementado sobre el corte vertical; (4) una medición posterior contrastada contra un umbral, con el procedimiento para repetirla; y (5) una fila en `docs/aspectos.md` y una entrada en `docs/ia.md` que hablen de este trabajo, no del de semanas anteriores.

Lo que sí se sostiene de antes: la documentación base (arc42, C4, dos ADR de estilo y stack) sigue ahí y el pipeline de integración continua corre en verde sobre el estado actual. Eso es la base sobre la que debía construirse el reto, no el reto en sí.

Se mantiene, sin resolver desde el inicio del semestre, que solo una persona del equipo aparece en el historial de commits (con distintas identidades de git). Esto va a pesar cada vez más de cara al proyecto final: la nota es de equipo, pero la evidencia de trabajo debe verse repartida.

## Semana 1 · S1

Sin actividad S1: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 6 · S6

Sin actividad S6: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 7 · S7

El repositorio está ordenado y la documentación base (README, ADR, aspectos, C4 nivel 2 y registro de IA) está en las rutas esperadas; el C4 de contenedores ya etiqueta sus flechas con protocolo y formato. Lo que falta es el corazón de esta entrega: un contrato OpenAPI, AsyncAPI o proto versionado en el repositorio, con rutas y esquemas, más una prueba de contrato que el workflow ejecute y que se demuestre capaz de fallar ante un cambio incompatible (run en rojo o cambio aportado como evidencia). Como FastAPI ya genera el esquema, exportarlo a un archivo versionado y validarlo con schemathesis o similar cierra varios criterios a la vez. Conviene además: hacer que el pipeline ejecute toda la carpeta de pruebas y no solo una parte, añadir el análisis estático con su URL pública y su Quality Gate, completar la sección 6 de arc42 con los flujos de interacción, registrar al menos un uso de IA rechazado con su motivo y equilibrar la contribución en el historial, hoy concentrada en una sola cuenta.

## Semana 8 · S8

La evidencia de despliegue no llegó a este corte. En el estado calificado no hay URL pública ni sistema desplegado: el README solo describe la ejecución local en el puerto 8000. Tampoco hay infraestructura como código (ningún Dockerfile, compose, Terraform, manifiestos ni Procfile), ni un procedimiento para recrear el entorno desplegado.

Además, el pipeline quedó en rojo: los últimos commits añadieron al workflow un paso de despliegue por SSH y el run de la rama principal falla. Recuperen el verde antes de seguir, corrigiendo ese paso o retirándolo del job de pruebas.

Quedan pendientes la verificación de salud, los logs estructurados, una métrica ligada a un escenario de calidad, la estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita, la sección 7 de arc42 con una caja por pieza y dónde se ejecuta, la sección 2 con el límite de costo y la condición de tarjeta, y un ADR por decisión de plataforma con su alternativa descartada y la capa gratuita verificada.

Mantengan el registro de uso de IA al día (hoy no crece desde agosto y no documenta rechazos con motivo) y repartan el trabajo: dos integrantes siguen sin aparecer en el historial de commits. La higiene de secretos sí está bien resuelta: las credenciales se toman del entorno y del almacén del proveedor, sin nada versionado.

## Semana 9 · S9 (pasada temprana, previa al cierre)

En esta pasada temprana la rama principal no se movió desde la entrega anterior: el periodo de la
evidencia está vacío. Bajo la regla del contrato, la evidencia previa no se recalifica por existir.

Qué falta para cerrarla antes del cierre:

- Empujar la porción del sistema construida con apoyo de IA, con sus rutas de código y sus commits.
- Llevar su cadena completa en la tabla de aspectos: escenario, elementos C4, ADR, código, prueba y
  medición, navegable hasta la evidencia.
- La prueba que falla ante el defecto que cubre (run en rojo, prueba de mutación o procedimiento
  documentado).
- La medición del escenario asociado, contrastada con su umbral.
- El registro de uso de IA de la semana, con lo aceptado y al menos un rechazo con su motivo.
- La auditoría de erosión sobre límites de contexto y propiedad de datos.
- La verificación de las dependencias propuestas en su registro oficial.

Además: el pipeline sigue en rojo y conviene recuperar el verde antes de seguir; falta decidir en un
ADR la no incorporación de un componente generativo (hoy no hay ni componente ni decisión); el registro
de IA no crece desde agosto; y dos integrantes declarados siguen sin commits visibles en el historial.
La higiene de secretos sigue correcta.
