# Retroalimentación publicable · Tienda virtual UTB

## Semanas 1 y 2

## Evidencia S1

Bien: repositorio público con el nombre de la convención, ficha del problema con usuarios, alcance y dos tensiones de calidad bien enfrentadas, plantilla arc42 descomprimida con sus doce secciones, `docs/adr/` y `docs/c4/` creados, y un registro de uso de IA con contenido real.

Corregir antes del corte 1: la tabla de `docs/aspectos.md` debe tener las ocho columnas del curso (ID, aspecto, requisito, C4, ADR, código, pruebas, evidencia) con al menos una fila con ID y aspecto; y en `docs/ia.md` falta registrar qué propuestas de la herramienta se rechazaron y por qué. Confirmen también que los cuatro integrantes tienen acceso al repositorio.

## Evidencia S2

Bien: secciones 1, 2 y 3 del arc42 redactadas sin texto de plantilla, restricciones clasificadas y justificadas y separadas de los requisitos, cuatro escenarios completos con sus seis partes y medida numérica, árbol de utilidad que prioriza por impacto y riesgo, y C4 de contexto como código con flechas etiquetadas.

Corregir antes del corte 1: la sección 10 del arc42 está vacía (los escenarios deben quedar allí, o al menos enlazados desde ella); la sección 1 debe declarar objetivos de negocio y decir a quién le importa cada uno; el C4 necesita leyenda de tipos de elementos; y cada escenario debe ser alcanzable desde la fila de su aspecto en `docs/aspectos.md`. Aseguren además que todos los integrantes aparezcan en el historial.

## Semana 3

Qué está bien: la sección 4 de arc42 liga la estrategia a los objetivos de calidad, el ADR 0001 está completo (contexto, alternativas, decisión y consecuencias), el README documenta el arranque con un solo comando, la CI está en verde y la estructura de paquetes coincide con el monolito modular.

Qué corregir antes del corte 1 (semana 5):
1. Rehacer `docs/matriz-comparativa-arquitectura.md` contra los escenarios de su árbol de utilidad: digan qué escenario mejora o empeora con cada estilo; hoy compara criterios genéricos.
2. Enlazar el ADR 0001 desde `docs/aspectos.md` y desde el escenario de calidad que lo motiva.
3. Registrar en `docs/ia.md` los usos de IA de esta semana, con lo aceptado y lo rechazado con motivo.

## Semana 4 · S4

La S4 deja un corte vertical de catálogo funcional, con C4 niveles 1 y 2 coherentes con el código y pruebas en verde.
Para el primer corte: verificar que las secciones 5, 6, 9, 10 y 12 del arc42 estén completas y sin texto de plantilla.
Añadir al ADR 0001 la trazabilidad con el commit que lo implementa y las pruebas que lo cubren.
Ajustar docs/aspectos.md a las 8 columnas del curso.
Incorporar en docs/ia.md lo rechazado con su motivo técnico.
Configurar SonarCloud en el pipeline.
El arranque con un solo comando y la fila de disponibilidad hasta Pruebas ya están resueltos.

## Semana 5 · CORTE1

El proyecto consolida bien S1-S4: problema, escenarios, ADR, arc42, C4 y corte vertical están documentados y el CI pasa. Para el compendio, conviertan correcciones.md en un índice de verificación real: cada hallazgo de S1-S4 con acción, ruta/prueba/commit y estado. Incorporen SonarCloud al pipeline como exige el contrato. Conviertan las rutas de código y pruebas de docs/aspectos.md en enlaces navegables. El PDF y la sustentación se gestionan por Moodle y la sesión.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Se revisó de nuevo después del cierre. No existe ninguna etiqueta en el repositorio, así que se tomó el último commit subido antes del cierre.

Qué está bien: el equipo sí trabajó activamente en esos días — corrigió pendientes reales de semanas anteriores (objetivos de negocio, trazabilidad entre escenarios y ADR, registro de IA) y hasta adelantó evidencia de la semana 6.

Qué falta: nada de ese trabajo fue sobre el reto de este corte. El único commit que se llama literalmente "Corte 1" agrega dos líneas al README y no toca ni ADR, ni código, ni pruebas, ni documentación de aspectos. No hay ninguna restricción diagnosticada, ni medición, ni cambio implementado.

Qué corregir: dedicar el esfuerzo que sí se ve en el historial (que es real y de buena calidad para otras semanas) al reto específico de este corte: identificar la restricción, medir el estado inicial, decidir en un ADR nuevo, implementar el cambio y volver a medir contra el umbral del escenario. Después, crear la etiqueta `corte-1` sobre ese commit.

## Semana 6 · S6

Sin actividad S6: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 7 · S7

La entrega sí contiene el contrato OpenAPI ejecutable, con rutas, esquemas y versión alineados con la API. La prueba compara el contrato con FastAPI, valida respuestas reales y ejerce dos mutaciones incompatibles; además, el workflow la ejecuta y publica su reporte. La sección 6 de arc42 también documenta los flujos de arranque y navegación del catálogo.

Quedan dos no conformidades de la ficha. El ADR compara alternativas y consecuencias, pero no justifica la integración contra un escenario de calidad concreto y medible. En el C4 nivel 2, las relaciones entre actores y cliente web declaran HTTPS, pero omiten el formato. Adicionalmente, el pipeline del estado revisado está en rojo y sigue sin evidencia pública de SonarCloud con Quality Gate. Corrijan esas piezas y retiren del repositorio el entorno de terceros versionado, que añade ruido innecesario a los barridos.

## Semana 8 · S8

### Recomendaciones prioritarias

- Aclaración: la sección 7 del arc42 único ya representa el despliegue; no hace falta rehacerla ni dividir el documento. Precisen en la sección 2 el límite económico y la condición de tarjeta.
- Publiquen URL, respuesta de salud y hora; versionen infraestructura y procedimiento de despliegue.
- Añadan logs estructurados, una métrica de calidad, origen seguro de secretos y cálculo de costo con punto de ruptura; registren las decisiones de plataforma en ADR.
- Resuelvan la ejecución fallida del pipeline y enlacen el run de la rama principal que confirme el resultado.

La sección 7 del arc42 ya representa el despliegue, pero las demás evidencias operativas del segundo corte no quedaron suficientemente verificables. Primero publiquen la URL del sistema y confirmen que responde desde fuera de la red, con su health check. Después versionen la infraestructura y documenten en el README cómo recrear el despliegue. Añadan logs estructurados con una línea de ejemplo, una métrica ligada a un escenario de calidad y la estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita. Precisen el límite económico en la sección 2 y registren cada decisión de plataforma en un ADR con su alternativa descartada. Eviten versionar entornos de terceros: inflan el repositorio y dificultan el barrido de secretos. Resuelvan el pipeline fallido y enlacen el run de la rama principal que confirme el resultado. Con eso, la próxima revisión podrá verificar criterio por criterio.
