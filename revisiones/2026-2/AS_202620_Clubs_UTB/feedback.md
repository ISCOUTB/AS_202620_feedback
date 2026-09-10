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

El proyecto avanza bien en documentación y corte vertical, pero falta el archivo correcciones.md en la raíz, que es obligatorio para esta entrega. Deben crear ese archivo con el seguimiento de hallazgos de S1-S4 y de la pasada preliminar de S5, citando evidencia real. También conviene completar las celdas 'Pendiente' en la tabla de aspectos y actualizar el README para reflejar el estado actual del código. El pipeline y las pruebas están funcionando; sigan así. Revisen la coherencia entre el ADR y los escenarios de calidad tras el cambio de C2 a C3.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Revisando el repositorio completo hasta el último commit antes del cierre, seguimos sin encontrar una respuesta a la restricción nueva que pedía este corte: no hay etiqueta `corte-1`, no hay un ADR nuevo, no hay una cifra de línea base medida ni un resultado contrastado contra un umbral. Lo único que se agregó en esta semana fue un endpoint de publicaciones (con su prueba y con el pipeline en verde) y un ajuste de una línea en la sección de requisitos de calidad, ninguno de los dos vinculado a una restricción diagnosticada en la documentación.

Un hallazgo nuevo de esta revisión: el ADR-0001, que ya estaba aceptado, se editó otra vez el 30 de agosto para agregarle una sección de trazabilidad. El contrato pide que un ADR aceptado no se toque — si hace falta completar o cambiar algo, se escribe un ADR nuevo que lo reemplace y se enlaza. No hace falta deshacer ese cambio, pero de aquí en adelante cualquier ajuste a esa decisión debe ir en un ADR nuevo, no en el mismo archivo.

Para la sustentación: preparen quién puede explicar qué restricción les asignaron, qué se midió antes del cambio, y por qué el endpoint agregado no aparece documentado como respuesta a ella.

## Semana 3 · S3

El ADR y la matriz comparativa están bien orientados y la estructura de paquetes refleja la decisión hexagonal. Para las próximas entregas: automaticen la prueba en un pipeline visible, documenten el arranque en el README desde el primer commit, y hagan navegable la trazabilidad en docs/aspectos.md y en los escenarios de calidad. Cuiden también las convenciones de nombres de ADR y el orden del repositorio. Varios de estos puntos se corrigieron después del cierre; procuren que los arreglos lleguen antes del cierre en las siguientes semanas.
