# Retroalimentación publicable · mapsutb

## Semanas 1 y 2

## Evidencia S1

El repositorio está en la organización, es público y la ficha del problema está completa: usuarios, objetivos, alcance y arquitectura propuesta. Su tabla de aspectos es de las mejores de la semana: ocho columnas, una fila con ID, aspecto y requisito, e incluso un escenario en formato de seis partes. El registro de IA incluye qué aceptaron y qué rechazaron. Les faltó montar la estructura de documentación (`docs/arc42/` con la plantilla, `docs/adr/`, `docs/c4/`) y declarar en la ficha las dos tensiones de calidad enfrentadas. Revisen también la etiqueta `corte-1`: apunta a un commit de la semana 1, y el corte aún no ha ocurrido.

## Evidencia S2

Las restricciones están bien: clasificadas por tipo y cada una justificada, y el contexto identifica con claridad actores y sistemas externos. Los cinco escenarios tienen medidas con cifra y unidad. Para corregir antes del corte 1: (1) redacten los escenarios con las seis partes (fuente, estímulo, artefacto, entorno, respuesta, medida) y condición de carga; (2) el árbol de utilidad debe priorizar por impacto y riesgo y apuntar a los escenarios (hay un enlace roto a un archivo que no existe); (3) falta el diagrama C4 de contexto como tal — una tabla no es un diagrama: háganlo como código, con leyenda y flechas etiquetadas, y guárdenlo en `docs/c4/`; (4) la sección 1 necesita objetivos de negocio asociados a su interesado, no solo atributos de calidad; (5) registren el uso de IA de esta semana; (6) organicen los archivos en `docs/arc42/` y actualicen la tabla de aspectos para enlazar cada escenario.

## Semana 3

Qué está bien: estrategia de solución ligada a los objetivos de calidad, ADR 0001 con alternativa descartada y motivo por patrón, y arranque con un solo comando documentado (`scripts/start.sh`).

Qué corregir antes del corte 1 (semana 5):
1. Escriban la matriz comparativa de los tres estilos contra el árbol de utilidad: la ficha la pide y hoy no existe en el repositorio.
2. Materialicen la estructura que declara el ADR en `lib/` (carpetas `adapters/`, `repositories/`, `strategies/`, `services/`, `features/` con `.gitkeep`): hoy solo está `main.dart`.
3. Actualicen `docs/aspectos.md` (todavía dice «Sin ADR aún») y enlacen el ADR desde el escenario que lo motiva; reparen el enlace roto en `docs/escenarios_calidad.md`.
4. Registren el uso de IA de esta semana en `docs/ia.md` y evidencien la prueba en verde (pipeline o run).
5. Contribuyan todos los integrantes (esta semana solo aparecieron tres cuentas) y regularicen `docs/arc42/` y `docs/c4/`.

## Semana 4 · S4

La documentación arc42 (secciones 1-6, 9, 10 y glosario) y los diagramas C4 están bien avanzados, y el corte vertical de zonas (interfaz → repositorio → JSON) está correctamente trazado. Para cerrar las brechas: (1) retiren los bloques de plantilla arc42help de la sección 5; (2) actualicen ficha-problema.md, escenarios_calidad.md y aspectos.md al alcance sin realidad aumentada, con una fila de aspectos defendible hasta Pruebas; (3) implementen o declaren explícitamente los contenedores de contenido panorámico y plano del campus que el C2 dibuja; (4) añadan un workflow de CI que ejecute las pruebas y deje evidencia pública en verde; (5) corrijan las rutas docs/Arc42 y docs/C4 a minúsculas; (6) registren los cambios de decisión en ADR nuevos, no editando ADR aceptados. El equipo va bien encaminado; estos ajustes son de forma y trazabilidad.

## Semana 5 · Primer corte (revisión flexible)

Por indicación docente se aceptaron las correcciones aplicadas durante la semana, aunque sean posteriores al cierre original. El corte sigue siendo el compendio de S1 a S4, sin reto ni restricción nueva. Se verificó que la ficha ya refleja el alcance sin RA, que los cinco escenarios tienen las seis partes, que las rutas de documentación fueron normalizadas y que el ADR 0004 aporta una comparación de tres estilos para justificar el monolito.

La documentación ahora declara con honestidad que el plano y las panorámicas siguen diferidos, y A-01 enlaza requisito, C4, ADR, código y prueba. El flujo de zonas puede seguirse desde la interfaz hasta el JSON local. Aún falta la evidencia verificable de ejecución: el workflow de CI ya ejecuta pruebas, pero no se encontró un run público; tampoco se ejecutó el proyecto durante la revisión. Para la sustentación, demuestren ese recorrido y expliquen cómo preservarán la historia de ADR 0001 cuando una decisión cambie.

## Semana 7 · S7

El contrato de las tres integraciones y el ADR que justifica la estrategia sincrona estan bien construidos y trazados a un escenario de calidad; esa es la base correcta. Para cerrar la semana: (1) hagan que el pipeline invoque explicitamente la prueba de contrato y compartan la URL del run; (2) conserven la corrida en rojo del cambio incompatible con su URL en lugar de revertir el commit sin dejar rastro de la ejecucion; (3) completen la evidencia de analisis estatico: linea del workflow que invoca el scanner, URL del run exitoso y URL publica del analisis con el Quality Gate; (4) suban el contenido de la tabla de aspectos con sus ocho columnas y del registro de IA con lo rechazado y su motivo; (5) unifiquen la documentacion en Markdown, retiren la copia suelta dentro de lib/ y actualicen el estado del README. Con la prueba de contrato fallando de forma reproducible, la entrega sube de nivel.
## Semana 6 · S6

El documento `dominio_y_modularidad.md` aporta un mapa de contextos, dueños de datos y no conformidades con acciones concretas. Para que la arquitectura sea defendible, llévenlo también a arc42 §8, documenten en un ADR el reajuste de límites y vinculen cada contexto con la tabla de aspectos. Añadan SonarCloud con scanner, run y Quality Gate público.

## Semana 8 · S8 (revisión definitiva)

La entrega cambió respecto de la revisión temprana: el sitio está desplegado como aplicación web estática en Firebase Hosting, con health consultable, infraestructura como código, logs en JSON, una métrica de disponibilidad ligada a su escenario, secretos fuera del código, la sección 7 de arc42 con cada pieza y su ubicación, la restricción de costo cero y de no usar tarjeta en la sección 2, y un ADR por decisión de plataforma. El cálculo de costo parte del volumen del escenario y señala en qué punto se agota cada capa gratuita. El pipeline del estado calificado queda en verde y el análisis estático con su Quality Gate va ligado a ese run.

Para cerrar: dejen de reescribir ADR ya aceptados —registren el cambio como un ADR nuevo y marquen el anterior como reemplazado—. Las filas de URL desplegada y de health quedan pendientes de calificar porque la URL se entrega por Moodle.

## Semana 9 · S9 (revisión definitiva)

El ruteo ya tiene decisión, pruebas de defecto y mediciones de cálculo y pantalla; la decisión de no incorporar generación quedó aceptada. Completen los enlaces de A-01 y actualicen el C4 que todavía declara el repositorio de mapas pendiente. Distingan el resultado con GPS simulado de la precisión en campo. La comprobación independiente de credenciales sigue pendiente por una limitación del revisor.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

Dijkstra, sus alternativas y costo están justificados e implementados. Las medidas son posteriores y no identifican una línea base anterior. Logs y sonda aportan observabilidad parcial; C4 aún declara ausente MapaRepository. No se mezcla la línea base de caché con la de ruteo.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

Vistas de mapas y GPS no reflejan OSM, Dijkstra y ubicación simulada.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Baja · Las vistas principales no incorporan por completo los ADR de OSM y ruteo:** Arc42 sigue dibujando un SDK Google embebido y el README dice que routing solo contiene .gitkeep, aunque el mapa solicita teselas OSM y Dijkstra está implementado y llamado. Esto cambia dependencias operativas y alcance disponible, no significa que la elección OSM sea deriva de implementación. **Acción:** Actualizar README/C4/arc42 en conjunto: OSM para mapa base, Dijkstra actual y tour aún pendiente. Dibujar por separado Geocoding/Static Maps opcionales; separar cálculo offline de carga de teselas. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · La vista de ejecución describe GPS actual, pero el arranque compone ubicación simulada:** El flujo documentado recibe posición del sensor; el flujo ejecutable emite coordenadas aleatorias alrededor de un punto fijo cada segundo y usa ese stream para origen de rutas. La interfaz no demuestra ubicación real por tener Observer. La implementación se identifica como simulada en código, por lo que se reporta como desajuste de la vista actual, no como obligación de implementar una función futura. **Acción:** Marcar el sensor/GPS real como objetivo y mostrar el simulador en la vista actual; identificar visiblemente modo demostración en UI. Cuando se integre GPS, sustituir el adaptador y probar permisos, ausencia de señal y precisión sin alterar el contrato Observer. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

El health público identifica el mismo commit revisado. Para el segundo corte, confirmen el escenario asignado y midan su línea base/respuesta sobre el entorno real. Comprueben la caché efectiva de cada recurso y la experiencia tras una reversión, y alineen C4 y aspectos con el código ya entregado.

</details>

## Semana 9 · Aclaración de la revisión

La comprobación de credenciales bloqueada por el entorno del revisor queda excluida del cálculo por decisión docente. Sigue sin verificarse y no implica un hallazgo de filtración. Los demás criterios conservan su valoración sobre la entrega de cierre; véase la [matriz actualizada](semana-09-evidencia-s9.md).

## Semana 11 · Integración y resiliencia

La decisión de no extraer, las mitigaciones y la trazabilidad están justificadas sobre las integraciones reales. Distingan las pruebas con dobles de las mediciones sobre GPS y proveedores reales. El flujo completo en campus sigue sin la medición que permitiría cerrar ese límite.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Ya hay una política HTTP de revalidación y una garantía limitada para analítica. Falta integrar la caché interna del grafo, declarar garantías por operación y justificar la decisión de datos más costosa de revertir. Reúnan consistencia y caché en arc42, manteniendo separado lo vigente de los recorridos panorámicos diferidos.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **2 abiertas, 52 cerradas, 54 en total**. Los 52 cierres figuran como completed. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Externo**. Firebase; pendiente dominio institucional. Dirección(es) documentada(s): https://mapsutb.web.app/.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

No hay commits nuevos desde el 16 de octubre. La sonda programada del 22 de octubre a las 14:32 UTC terminó correctamente; su alcance no equivale a una prueba funcional integral. Las issues Sonar #55 y #56 permanecen abiertas y sin asignar. MapsUTB es un proyecto distinto de ElMapita.

**Próximos pasos:**
- Publicar dirección institucional real iscoutb.dev manteniendo Firebase como alternativa si aplica.
- Asignar/refactorizar complejidad y ternario de indice_busqueda.dart;52 cierres son Sonar, no52 funcionalidades.
- Tabla operación→garantía; incluir caché interna grafo además HTTP y su invalidación; ADR reversión datos; arc42 §8.

**Issues:** 2 abiertas y 52 cerradas; 2 abiertas sin responsable. Cierres: 52 completed. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Externo. Firebase, no subdominio iscoutb.dev. MapsUTB NO es ElMapita. URL documentada: https://mapsutb.web.app/. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#mapsutb) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).
