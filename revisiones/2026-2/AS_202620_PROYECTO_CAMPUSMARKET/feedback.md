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

La entrega S6 está sólida: el mapa de contextos, la propiedad de datos y la sección 8 de arc42 están bien documentados y alineados con el código actual. Para futuras revisiones, aseguren que los archivos de evidencia (auditoría, aspectos.md, ia.md) sean directamente revisables en el repositorio y aporten enlaces a los runs de CI. La distinción entre producto y publicación y la declaración explícita de que no hay shared kernel son buenas prácticas. Mantengan la trazabilidad entre aspectos y contextos para que la sustentación sea defendible.

## Semana 7 · S7

El contrato OpenAPI versionado, la prueba que lo compara con FastAPI y el ADR de integración están bien encadenados y se sostienen entre sí. Para que la entrega sea demostrable y no solo declarada, conviene: 1) aportar la URL del run de CI sobre el hash revisado y la línea del workflow que ejecuta la prueba de contrato; 2) publicar la URL del análisis en SonarCloud con el estado del Quality Gate y la línea del scanner; 3) mover a la organización el run en rojo del cambio incompatible, que hoy vive en un fork, o adjuntar la evidencia con su contenido; 4) dejar revisables en el repositorio la tabla de aspectos, el registro de uso de IA y el C4 nivel 2, etiquetando protocolo y formato en cada flecha. Con esos cuatro puntos la entrega pasa de correcta a verificable de punta a punta.

## Semana 8 · S8

### Recomendaciones prioritarias

- El arc42 combina un consolidado y módulos: completen la sección 2 con el límite económico y sustituyan en la sección 7 el esquema local por nodos y proveedores realmente elegidos.
- Publiquen URL, respuesta de salud y hora; versionen la infraestructura, el origen de secretos y los pasos para recrear el entorno.
- Añadan logs estructurados y una métrica ligada a un escenario; calculen costo mensual y punto de ruptura, y documenten la elección en un ADR.
- Conserven la evidencia del CI en verde junto a la evidencia operativa.

El pipeline principal continúa en verde, pero todavía no se observa una entrega operativa de despliegue. Las no conformidades prioritarias son la ausencia de URL pública y health check externo, infraestructura como código, pasos reproducibles de despliegue, logs estructurados, una métrica ligada a un escenario, estimación de costos, vista de despliegue real y ADR de plataforma. La mejor siguiente iteración es publicar primero una URL declarada y su health check, y luego documentar exactamente cómo se recrea ese entorno.

## Semana 8 · S8 (revisión definitiva, 2026-09-28)

La entrega S8 llegó y está bien armada: el despliegue público quedó documentado (frontend en GitHub Pages, API en Azure App Service y base de datos en Azure MySQL Flexible Server), la infraestructura está versionada en Bicep, el pipeline corre en verde sobre la rama principal, los logs son JSON con campos y hay una métrica operativa ligada a un escenario de calidad. También están la estimación de costo con supuestos y punto de ruptura, la vista de despliegue con una caja por pieza, el límite económico y la restricción de tarjeta en las restricciones, y una decisión de plataforma por pieza con su alternativa descartada. Quedan pendientes de calificar la URL y el health check, que se entregan por Moodle: cuando la publiquen, adjunten el código de respuesta y la hora de la comprobación.

Para cerrar el flanco transversal, dos cosas: (1) la evidencia de SonarCloud sigue sin ser auditable —hay configuración, pero falta el paso del analizador en el workflow y la URL pública del análisis con el estado del Quality Gate; una afirmación o una insignia no sustituyen el run; (2) no editen un ADR ya aceptado: cuando la decisión cambie, escriban uno nuevo y marquen el anterior como reemplazado. Sigan así con el nivel de detalle y de declaración honesta de límites que mostraron en esta entrega.

## Semana 9 · S9 (revisión definitiva)

La entrega final incorpora una porción real de Catálogo y una cadena navegable hasta mutaciones y medición HTTP/MySQL bajo cuota. La auditoría amplía correctamente el alcance de dependencias y distingue pruebas locales de experiencia pública. Mantengan esa separación: aún falta medir EC-01 desde el navegador público con el conjunto completo, integrar el scanner Sonar y preservar los ADR aceptados. Revisen además los avisos vigentes de la versión de python-multipart.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

El experimento del consumidor incompatible tiene línea base y 58 observaciones contrastadas en la evaluación, correlación en las 58 y secuencia de rechazo y recuperación 200→422→200. El ADR-0020 confirma decisiones previas mediante evidencia. Se recupera el consumidor experimental; no se demuestra recuperación de infraestructura.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

Sin deriva material observada en los recorridos inspeccionados.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

No se observó deriva material en los recorridos revisados; se conservan los límites y deudas explícitos del diseño.

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Para el segundo corte falta identificar el escenario operativo asignado por el docente. El despliegue y el health check responden; preparen la línea base, la intervención y el resultado comparable del reto, con métrica y límites de validez. No presenten el experimento de S9 como respuesta a una asignación todavía no confirmada. La sustentación y el pipeline en vivo quedan pendientes.

</details>

## Semana 11 · Integración y resiliencia

La evidencia S11 identifica la integración real, distingue los tres fallos y propone mitigaciones y una decisión argumentada de no extraer Catálogo. La idempotencia sigue diseñada y pendiente, lo cual está declarado correctamente; no debe presentarse como implementada ni confundir CI general con pruebas de fallos. Actualicen las referencias de CI, porque el flujo real fue exitoso en una revisión anterior y falló en la revisión final evaluada.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

El avance S12 permite contrastar crear publicaciones y cambiar su estado con transacciones locales y reconoce la ausencia de broker. Faltan tabla operación→garantía, decisión de caché e invalidación, ADR de la decisión de datos más costosa de revertir y su incorporación en arc42. El diagnóstico es preliminar y no corresponde a un cierre de S12.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **1 abiertas, 0 cerradas, 1 en total**. Sin cierres registrados. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Institucional**. Cumple la API; frontend en GitHub Pages, cumplimiento parcial del sitio. Dirección(es) documentada(s): https://campusmarket.iscoutb.dev ; https://nnigarp.github.io/AS_202620_PROYECTO_CAMPUSMARKET/.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Sin commits nuevos; PR #60 abierta documental. CI backend y otros success, run de flujo real falla Android pero web-desktop/web-mobile success.

**Próximos pasos:**
- Tabla crear/cambiar estado/ocultar publicación → garantía, distinguiendo transacciones MySQL de compensación SQL/archivos.
- Decidir caché o no caché de catálogo y actualización tras crear/cambiar visibilidad; incorporarlo a arc42 §8.
- ADR de costo comparativo de reversión de datos; reproducir/corregir flujo Android y resolver PR #60 sin llamar todo CI verde.

**Issues:** 1 abiertas y 0 cerradas; 1 abiertas sin responsable. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Institucional. API institucional; frontend en GitHub Pages. Cumplimiento parcial del sitio. URL documentada: https://campusmarket.iscoutb.dev ; https://nnigarp.github.io/AS_202620_PROYECTO_CAMPUSMARKET/. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#proyecto_campusmarket) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

No hay cambios en la rama principal respecto al 22 de octubre. La PR #60 permanece abierta, sin incorporación a master. Se mantienen los workflows exitosos de Compose/persistencia y contrato del cliente, y el fallo del workflow de flujo real observado previamente en Android. La documentación del despliegue distingue correctamente API institucional y frontend Pages; no anunciar toda la validación como verde.

**Próximos pasos:**
- Tabla crear/cambiar estado/ocultar publicación → garantía, distinguiendo transacciones MySQL de compensación SQL/archivos.
- Decidir caché o no caché de catálogo y actualización tras crear/cambiar visibilidad; incorporarlo a arc42 §8.
- ADR de costo comparativo de reversión de datos; reproducir/corregir flujo Android y resolver PR #60 sin llamar todo CI verde.

**Issues:** 1 abiertas y 0 cerradas; 1 abiertas sin responsable. El estado registrado no acredita por sí solo implementación.

**README:** Institucional. API institucional, interfaz Flutter en GitHub Pages: cumplimiento parcial del sitio. Azure aparece solo como histórico. URL documentada: https://campusmarket.iscoutb.dev ; https://nnigarp.github.io/AS_202620_PROYECTO_CAMPUSMARKET/. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#proyecto_campusmarket) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).



## Seguimiento actual · 25 de octubre de 2026 · S12 abierta

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Sin cambios en master desde el corte previo. #60 sigue abierta y no integrada. En la punta actual pasan Compose/persistencia, contrato cliente, backend y Flutter; Flujo real Web y Android conserva failure. API institucional y frontend GitHub Pages permanecen separados; no afirmar todo CI verde.

**Próximos pasos:**
- Corregir/reproducir el flujo Android y resolver #60.
- Publicar frontend bajo iscoutb.dev; API institucional no completa ese requisito.
- Completar garantías de publicación, política de caché y ADR de costo de reversión.

**Issues GitHub:** 1 abiertas y 0 cerradas; 1 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Institucional. Cumplimiento parcial: API institucional, frontend externo GitHub Pages. Azure es histórico.

[Fuentes y alcance](../seguimiento-s12-2026-10-25.md#proyecto_campusmarket) · [Issues](../seguimiento-issues-2026-10-25.md) · [URL y dominio](../seguimiento-despliegues-2026-10-25.md).


## Seguimiento actual · 26 de octubre de 2026 · sin cierre automático de S12

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

PR #61–65 fusionadas: estrategia de datos S12, correcciones de evidencia/C4 y estabilización del flujo Android, más taller aislado de mensajería. La punta actual pasa backend, Flutter, Compose/persistencia, contrato público y flujo real Web/Android; el job Android ejecutó el emulador y no fue omitido. Esto supera fallos de revisiones anteriores, sin transferirles el resultado. El taller usa SQLite, deduplicación, reintentos/DLQ y backoff real con sleeper inyectable; no integra broker ni outbox productivo. README distingue API iscoutb.dev y frontend GitHub Pages: el requisito de dominio de toda la solución sigue parcial.

**Próximos pasos:**
- Conservar evidencia exacta del flujo Web/Android reparado y separar CI controlado de aceptación manual del despliegue.
- Mover/documentar el frontend bajo iscoutb.dev y mantener explícito el carácter aislado del taller frente a MySQL productivo.

**Issues GitHub:** 1 abiertas y 0 cerradas; 1 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Institucional. Cumplimiento parcial: API institucional, frontend externo GitHub Pages. Azure es histórico.

[Fuentes y alcance](../seguimiento-s12-2026-10-26.md#proyecto_campusmarket) · [Issues](../seguimiento-issues-2026-10-26.md) · [URL y dominio](../seguimiento-despliegues-2026-10-26.md).
