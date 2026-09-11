# Retroalimentación publicable · CampusMarket

## Semanas 1 y 2

## Evidencia S1

El repositorio está en la organización, es público y el README funciona como ficha del problema: declara beneficiarios, problema y objetivo general. El registro de IA ya tiene su primera entrada. Les faltó: las dos tensiones de calidad, la tabla de ocho columnas en `docs/aspectos.md` (hoy es texto), la plantilla arc42 y las carpetas `docs/adr/` y `docs/c4/` (las crearon como archivos sueltos el 11 de agosto, después del cierre). Ojo con el README: al cierre listaba dos integrantes y el equipo es de tres.

## Evidencia S2

Las restricciones están clasificadas y justificadas con origen de cada una, los cuatro escenarios tienen sus seis partes y medidas numéricas con condición de carga, el árbol de utilidad prioriza por impacto y riesgo, y el C4 de contexto está como código PlantUML con leyenda y flechas etiquetadas: muy buen trabajo. Para corregir antes del corte 1: (1) la sección 1 de arc42 lista funcionalidades, no objetivos de negocio con su interesado; (2) `docs/aspectos.md` sigue igual que en S1: pónganle la tabla de ocho columnas y enlacen cada escenario; (3) organicen la documentación en `docs/arc42/` y `docs/c4/`; (4) unifiquen el tamaño del equipo en los documentos (dicen «dos» y «tres» integrantes); (5) registren en `docs/ia.md` qué rechazaron de lo que propuso la IA; (6) repartan el historial: todo está firmado por una sola cuenta.

## Semana 3

Qué está bien: el ADR 0001 está completo y enlazado desde `aspectos.md` y EC-03, la sección 4 trae tácticas ligadas a los escenarios, la matriz comparativa evalúa los tres estilos contra su árbol de utilidad y el esqueleto backend arranca con un comando único con su prueba en CI en verde.

Qué corregir antes del corte 1 (semana 5):
1. `docs/ia.md`: quedó sin entradas de la semana 3 (17–23 ago) y sin la columna de qué se rechazó y por qué; pónganlo al día.
2. El frontend sigue siendo la plantilla Flutter por defecto: lleven en S4 los mismos módulos del backend para que la estructura del ADR quede materializada en todo el sistema.

## Semana 4 · S4

La evidencia S4 está sólida: arc42 1-6, 9, 10 y 12 redactados con contenido propio; C4 niveles 1 y 2 coherentes y versionados como código; corte vertical de publicaciones trazado desde la interfaz hasta SQLite con prueba en verde; y la fila ASP-05 de aspectos queda completa hasta Pruebas. Para el primer corte, integren SonarCloud al pipeline, enlacen cada ADR con el commit que lo implementa y añadan una medición de línea base. El arranque con un solo comando está bien documentado; conviene dejarlo verificado en un run o captura. Sigan manteniendo el registro de IA con lo rechazado y su motivo, que está bien logrado.

## Semana 5 · CORTE1

El proyecto presenta una línea base arquitectónica sólida y bien documentada. Se valora la trazabilidad completa desde aspectos hasta evidencia, la implementación del corte vertical y la respuesta al reto de bloqueo SQLite con ADR-0002. Se recomienda asegurar la entrega del PDF en Moodle y preparar la sustentación. Mantener el ritmo de actualización de evidencias y CI.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Muy buen trabajo en el reto de corte 1. Diagnosticaron el problema con una cifra de línea base real (un bloqueo de la base de datos que tardaba más de 7 segundos y devolvía un error interno), compararon tres alternativas con sus ventajas y desventajas, y documentaron la decisión en un ADR completo que incluye hasta el dato concreto que los haría reconsiderarla más adelante. Implementaron el cambio, lo cubrieron con una prueba automatizada que reproduce exactamente el problema original, y volvieron a medir después del cambio para comprobar que ahora responde dentro del tiempo esperado sin perder información. La cadena que conecta el aspecto con el requisito, el diagrama, la decisión, el código, la prueba y la evidencia queda completa y se puede seguir de punta a punta. Lo único que falta por revisar es el estado real de SonarCloud (la configuración está, pero no se confirmó en vivo) y que dos de los escenarios definidos desde la semana 2 todavía no están implementados — lo cual dejaron dicho con claridad en vez de simularlo. Buen manejo también del registro de uso de IA, con rechazos justificados técnicamente. En la sustentación, prepárense para explicar en vivo el estado de SonarCloud y el plan para los escenarios pendientes.

## Semana 6 · S6

La base documental de S1-S5 está sólida, pero la evidencia S6 no se subió al commit vigente: faltan el mapa de contextos con relaciones tipificadas, la tabla módulo-datos con dueño único, la lista de violaciones con plan de corrección, la sección 8 de arc42 y, si aplica, el C4 nivel 3 con su ADR. Revisen el estado de master al cierre y completen los artefactos de la semana sobre el código actual.
