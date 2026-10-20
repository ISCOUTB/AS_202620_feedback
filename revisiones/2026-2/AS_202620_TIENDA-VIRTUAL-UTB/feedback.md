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

Por indicación docente, la matriz de S6 se completó sobre el estado actual del repositorio, sin que ello altere el registro de la ventana original.

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

## Semana 8 · S8 (revisión definitiva)

Entrega muy completa: el sistema quedó desplegado por piezas (cliente web, API y base de datos en tres proveedores con capa gratuita sin tarjeta), con infraestructura como código versionada, un procedimiento de arranque reproducible, logs en JSON por petición, una métrica consultable ligada al escenario de disponibilidad, secretos fuera del repositorio y una estimación de costo mensual con supuestos y punto de ruptura. Cada decisión de plataforma tiene su ADR con la alternativa descartada y la capa gratuita verificada, y el registro de uso de IA creció documentando lo que se descartó y por qué.

Dos filas de despliegue quedaron pendientes de calificar porque la URL se entrega por Moodle y no se probó ninguna; el repositorio sí declara las URLs y las rutas de salud y métricas.

Para cerrar: (1) el cron de keep-alive inunda el listado de ejecuciones y deja el run de la revisión fuera del alcance de la comprobación, así que citen el run de la rama principal que confirme el resultado; (2) el análisis estático no deja evidencia auditable mientras el token no esté configurado, de modo que el pipeline ejecute el scanner y publique el Quality Gate; y (3) no reescriban un ADR ya aceptado: si la decisión cambia, escriban uno nuevo y marquen el anterior como reemplazado.

## Semana 9 · S9 (revisión definitiva)

La separación Catálogo–Inventario ya tiene una cadena sólida: prueba negativa, medición local y auditoría de propiedad de datos. Falta que el equipo ratifique las decisiones de separación y de no incorporar generación; ambas siguen como propuestas. Corrijan además el README que aún presenta Inventario vacío y aporten la evidencia pública del scanner y Quality Gate.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

Hay una medición local posterior con cinco usuarios, sin línea base del despliegue. La implementación existe, pero el ADR-0008 sigue propuesto y README declara el inventario vacío. CI, health, readiness y logs están en el código; no se declara una URL pública vigente.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

README llama vacío a Inventario ya implementado.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Baja · README conserva Inventario como paquete vacío aunque ya sirve un contrato separado:** Confunde el mapa de responsabilidades y el número de llamadas del corte vertical, pero las vistas C4 y el código sí preservan la separación. **Acción:** Actualizar README: distinguir identity/orders pendientes de inventory operativo; describir los dos recorridos y enlazar el ADR-0008 sin cambiar su estado de ratificación pendiente. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Antes del corte, documenten cuál fue el escenario operativo asignado y midan una línea base reproducible en el entorno desplegado. Publiquen el dominio vigente de Dokploy, sus comprobaciones de salud y flujo, el resultado del experimento frente al umbral y el costo real de servidor y backups. La medición local de cinco usuarios es un insumo, pero todavía no acredita el reto asignado.

</details>

## Semana 11 · Integración y resiliencia

La decisión de no extraer está razonada y el diseño de idempotencia y saga distingue lo pendiente. Completen los tres modos de fallo sobre las consultas reales de catálogo e inventario, y actualicen aspectos y referencias que todavía llaman vacío al inventario. Para el final, las mitigaciones diseñadas necesitan pruebas de fallo sobre la integración real.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Avance preliminar: la lectura sin caché está justificada y PostgreSQL aparece en el C4. Falta la tabla operación a garantía, contrastar dos operaciones y elegir la decisión de datos de mayor costo de reversión. La estrategia de consistencia y caché debe quedar reunida en la sección 8.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **0 abiertas, 0 cerradas, 0 en total**. Sin cierres registrados. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Sin URL vigente**. Declara URL definitiva pendiente en Dokploy.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.
