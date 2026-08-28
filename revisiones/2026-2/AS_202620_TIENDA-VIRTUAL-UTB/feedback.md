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

El repositorio cumple identidad, estructura y README. Para la siguiente entrega, completen el C4 nivel 2, implementen el corte vertical con su prueba automatizada, y actualicen docs/aspectos.md a las 8 columnas. Revisen el ADR para incluir trazabilidad y el registro de IA para documentar rechazos. Añadan etiqueta corte-1 y configuren SonarCloud. La evidencia de arc42 está incompleta; asegúrense de que el archivo completo esté disponible.
