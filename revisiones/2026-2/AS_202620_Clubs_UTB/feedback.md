# Retroalimentación publicable · Clubs UTB

## Semana 1

- Está bien: el repositorio existe con el nombre correcto y es público; el problema de la gestión de clubes está bien descrito; `docs/ia.md` arrancó con contenido real.
- Falta: la ficha del problema (usuarios y alcance), las dos tensiones de calidad y la estructura (`docs/arc42/`, `docs/adr/`, `docs/c4/`, y recuperar el README).
- Corregir antes del corte 1: convertir `docs/aspectos.md` en la tabla de 8 columnas del curso con al menos un aspecto, y asegurar que los cuatro integrantes tengan acceso y firmen commits.

## Semana 2

- Está bien: las secciones 1, 2 y 3 de arc42 están redactadas y sólidas (metas con interesado, restricciones clasificadas y justificadas), el árbol de utilidad usa pares importancia/dificultad, el C4 de contexto está como código Mermaid con flechas etiquetadas, y los 6 escenarios tienen las seis partes con medidas numéricas.
- Falta: `docs/aspectos.md` sigue sin la tabla de aspectos ni enlaces a los escenarios; son 6 escenarios y se pedían entre 3 y 5; `docs/ia.md` no registró usos reales de la semana 2; la ficha del problema aún no declara las dos tensiones de calidad.
- Corregir antes del corte 1: elegir los 3–5 escenarios que se conservan, llenar `docs/aspectos.md` con su fila por aspecto y los enlaces, mover el C4 a `docs/c4/`, y declarar si hay o no restricciones legales.

## Semana 3

Qué está bien: la sección 4 justifica la estrategia hexagonal con tácticas nombradas (timeout, reintento, caché, índices), la matriz comparativa va fila por fila contra sus escenarios U1–U3 y C1–C3, y el ADR 0001 está aceptado con alternativas motivadas.

Qué corregir antes del corte 1 (semana 5):
1. El arranque no quedó documentado en el README y `backend/src/main.py` y `tests/test_health.py` están vacíos en la versión calificada: documenten el comando único de arranque y dejen la prueba con asserts reales.
2. Hagan verificable la prueba en verde: agreguen un pipeline o evidencia de ejecución.
3. Hagan alcanzable el ADR: enlácenlo desde `docs/aspectos.md` (con la tabla de 8 columnas) y desde el escenario U2 que lo motiva.
4. Actualicen `docs/ia.md` (sin cambios desde el 9 de agosto) registrando usos y qué se rechazó y por qué, y borren el residuo `docs/adr/.temp`.

Ojo: parte del trabajo llegó después del cierre y no contó para esta entrega; la próxima vez asegúrense de empujar antes de la medianoche del domingo.

## Semana 4 · S4

Entrega S4 completa en lo esencial: arc42 1-6, 9, 10 y glosario redactados; C4 niveles 1-2 coherentes; corte vertical que atraviesa interfaz, lógica y persistencia con prueba en verde; fila U2 de aspectos.md trazable hasta Pruebas. Para cerrar los pendientes: (1) unificar el arranque en un solo comando en el README; (2) configurar SonarCloud para el análisis estático del contrato; (3) declarar explícitamente que el contenedor Flutter aún no tiene código. El registro de IA y los ADR están bien llevados; continúen así.

## Semana 5 · CORTE1

El proyecto está sólido en documentación y corte vertical, con CI pasando. Sin embargo, falta el archivo correcciones.md en la raíz, que es obligatorio para esta entrega. Deben crearlo antes del cierre, listando cada hallazgo de S1-S4 y cómo lo resolvieron, con evidencia. También asegúrense de subir el PDF al aula. El resto de la matriz está bien.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Revisando el repositorio completo hasta el último commit antes del cierre, seguimos sin encontrar una respuesta a la restricción nueva que pedía este corte: no hay etiqueta `corte-1`, no hay un ADR nuevo, no hay una cifra de línea base medida ni un resultado contrastado contra un umbral. Lo único que se agregó en esta semana fue un endpoint de publicaciones (con su prueba y con el pipeline en verde) y un ajuste de una línea en la sección de requisitos de calidad, ninguno de los dos vinculado a una restricción diagnosticada en la documentación.

Un hallazgo nuevo de esta revisión: el ADR-0001, que ya estaba aceptado, se editó otra vez el 30 de agosto para agregarle una sección de trazabilidad. El contrato pide que un ADR aceptado no se toque — si hace falta completar o cambiar algo, se escribe un ADR nuevo que lo reemplace y se enlaza. No hace falta deshacer ese cambio, pero de aquí en adelante cualquier ajuste a esa decisión debe ir en un ADR nuevo, no en el mismo archivo.

Para la sustentación: preparen quién puede explicar qué restricción les asignaron, qué se midió antes del cambio, y por qué el endpoint agregado no aparece documentado como respuesta a ella.

## Semana 3 · S3

El ADR y la matriz comparativa están bien orientados y la estructura de paquetes refleja la decisión hexagonal. Para las próximas entregas: automaticen la prueba en un pipeline visible, documenten el arranque en el README desde el primer commit, y hagan navegable la trazabilidad en docs/aspectos.md y en los escenarios de calidad. Cuiden también las convenciones de nombres de ADR y el orden del repositorio. Varios de estos puntos se corrigieron después del cierre; procuren que los arreglos lleguen antes del cierre en las siguientes semanas.

## Semana 6 · S6

El mapa de contextos con relaciones tipificadas, la tabla de dueño único, el ADR del reajuste y la lista de no conformidades muestran un avance sólido en la entrega. Para cerrar del todo:
1) Agreguen el scanner de SonarCloud al workflow y publiquen la URL del análisis con su Quality Gate; hoy solo hay pruebas.
2) Completen docs/aspectos.md con la columna de evidencia y eliminen las celdas 'Pendiente' que dejan filas sin defender.
3) Escriban explícitamente qué fila de aspectos corresponde a cada contexto del mapa (hoy la relación queda implícita).
4) Corrijan el enlace roto a la tabla de módulos y las menciones que aún declaran pendiente una alineación ya aplicada.
5) Cierren NC-01 y NC-02 o actualicen su plan con fecha y responsable.
6) Dejen registrado el recorrido de auditoría (comando y alcance) para que la lista de no conformidades sea repetible.
## Semana 7 · S7

Buen avance del corte: el contrato OpenAPI está versionado con CHANGELOG y esquemas, el ADR de integración compara alternativas síncronas y asíncronas, y la vista de ejecución ya describe un flujo con diagrama de secuencia. Para cerrar la evidencia: (1) adjunten la ejecución del workflow de contrato y, sobre todo, un run en rojo provocado por un cambio incompatible, que es lo que demuestra que la prueba protege de verdad; (2) publiquen la URL del análisis estático con su Quality Gate y la línea del workflow que invoca el scanner, hoy no hay configuración en el repositorio; (3) unifiquen el ADR de integración en un solo archivo con nombre NNNN-en-kebab-case y corrijan el enlace roto que apunta a él; (4) etiqueten cada flecha del diagrama de contenedores con protocolo y formato; (5) actualicen la tabla de módulos y cierren las no conformidades registradas. ¿Pueden documentar también el flujo de publicaciones en la vista de ejecución y subir la evidencia del cambio que hizo fallar la prueba?
