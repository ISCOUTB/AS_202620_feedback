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

El compendio muestra avance real: corte vertical POST /analysis, escenarios, ADR y trazabilidad parcial. Para cerrar el corte: actualicen correcciones.md para reflejar lo ya resuelto, completen arc42 (sección 11 y glosario), terminen docs/c4/03-componentes.md, limpien __pycache__, archivos con sufijos y PDF de la raíz, aseguren commits del tercer integrante, y dejen un run de CI en verde anterior al cierre con SonarCloud. Revisen enlaces rotos en README y aspectos.md.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

No pudimos revisar el corte 1 porque el repositorio del equipo ya no está en la organización del curso: no responde al clonarlo ni a través de la API, y no aparece en el listado completo de repositorios públicos de la organización. No sabemos si esto pasó por un cambio de visibilidad, un traslado a otra cuenta o un borrado — cualquiera de los tres deja el trabajo fuera de nuestro alcance. La última vez que se pudo ver, el 2026-09-02, el repositorio tenía una base de S4 completa (interfaz, lógica y persistencia con su prueba) pero todavía no mostraba una respuesta al reto del corte 1.

Esto es urgente y no depende de esta revisión: hablen con el docente cuanto antes para restablecer el acceso público al repositorio, con el historial completo tal como estaba. Sin eso no hay manera de calificar el corte, y tampoco de que ustedes mismos demuestren el trabajo que hicieron.

## Semana 1 · S1

Sin actividad S1: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 2 · S2

Sin actividad S2: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 6 · S6

La entrega S6 documenta bien el mapa de contextos, la propiedad de datos y la verificación de violaciones. El lenguaje ubicuo en arc42 §8 es correcto. Para cerrar brechas: vincula explícitamente las filas de aspectos.md con los contextos del mapa, añade un ADR si los límites cambiaron, completa la evidencia de la fila A-02 y asegura que todos los integrantes declarados aparezcan en el historial. Incluye enlaces a runs de CI en la documentación.
