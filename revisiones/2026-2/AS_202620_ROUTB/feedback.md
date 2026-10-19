# Retroalimentación publicable · ROUTB

## Semana 1

El repositorio está bien montado: en la organización, público, con la estructura completa y la plantilla arc42 en Markdown. La ficha del problema describe usuarios y alcance con claridad.

Les falta declarar las dos tensiones de calidad que hacen interesante el problema (enfrenten dos atributos, por ejemplo tiempo de respuesta contra costo de infraestructura), armar la tabla de aspectos con las ocho columnas del curso (hoy tiene dos y sin ID) y dejar en `docs/ia.md` una entrada real: si aún no han usado IA, declárenlo, no lo dejen en «pendiente».

## Semana 2

Buen avance: cinco escenarios con cifras concretas, restricciones justificadas y el C4 de contexto está como código Mermaid, revisable en el repositorio.

Antes del corte 1, corrijan: cada escenario debe desglosar las seis partes (fuente, estímulo, artefacto, entorno, respuesta y medida) y la medida necesita cifra, unidad y condición de carga; el árbol de utilidad debe priorizar por impacto y riesgo y casar con los escenarios redactados; el C4 necesita leyenda y flechas etiquetadas (y un solo nodo para el sistema). Reubiquen los escenarios en la sección 10 (quedó vacía), completen las restricciones con categorías organizativas y legales, y enlacen cada escenario desde su fila de `docs/aspectos.md`, que sigue pendiente desde la semana 1, igual que el registro de IA.

## Semana 3

Qué está bien: la sección 4 da tácticas concretas ligadas a las prioridades del árbol de utilidad, el ADR 0001 compara los tres estilos contra el árbol con juicios por atributo y descarta alternativas con motivo, los paquetes del backend respetan el monolito modular del ADR y `docs/ia.md` registra la semana con lo aceptado y rechazado.

Qué corregir antes del corte 1 (semana 5):
1. Falta el enlace del ADR desde el escenario motivador: la tabla de escenarios 10.2 no enlaza la decisión (solo lo hace `aspectos.md`).
2. El README documenta la instalación y el arranque en pasos separados; dejen un único comando documentado.
3. La prueba `backend/tests/test_health.py` existe, pero sin workflow ni evidencia del run: añadan `.github/workflows/` con `pytest` y suban el verde.
4. Revisen el C4 de contexto (`docs/c4/context.md`): quedaron pendientes desde S2 la leyenda y las etiquetas de las flechas.

## Semana 4 · S4

Entrega S4 completa y bien orientada: arc42 1-6, 9, 10 y 12 redactados con contenido propio, C4 niveles 1 y 2 como código, corte vertical de registro con prueba en CI en verde, y fila 2 de aspectos trazable hasta pruebas. Para el primer corte: completen las secciones 7, 8 y 11 de arc42, llenen los huecos de las filas 1 y 3 de aspectos, integren SonarCloud al pipeline, enlacen cada ADR con el commit que lo implementa y registren una medición de línea base. El glosario y los escenarios de calidad están bien alineados con el dominio.

## Semana 5 · CORTE1

El proyecto presenta una línea base arquitectónica sólida con arc42 completo, C4 en tres niveles, ADR bien formados y un corte vertical funcional con pruebas de concurrencia. La trazabilidad en docs/aspectos.md es navegable y el repositorio cumple la estructura del contrato. Para el siguiente corte, aseguren que correcciones.md e ia.md sean verificables desde el repositorio, integren SonarCloud al pipeline y documenten el arranque con un solo comando real. También equilibren la distribución de commits para reflejar la colaboración del equipo.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

El reto quedó resuelto de forma correcta: identificaron un riesgo real (que dos personas reserven el mismo cupo al mismo tiempo), midieron que antes del cambio el sistema ni siquiera tenía ese endpoint, implementaron el control para que solo se acepten tantas reservas como cupos existan, y probaron con 20 intentos simultáneos sobre 4 cupos que efectivamente solo se aceptan 4 y ninguno queda en negativo, dentro del tiempo esperado. La cadena de trazabilidad queda completa. Dos cosas por mejorar: primero, no pudimos confirmar cuál fue la restricción individual que el curso les asignó — verifiquen que lo que resolvieron sea exactamente eso y no una interpretación propia del reto. Segundo, el análisis de SonarCloud lleva varios días en rojo sin resolverse; tener las pruebas en verde no es suficiente si el análisis estático sigue fallando. Para la próxima entrega, repartan mejor el trabajo: casi todo el reto de esta semana lo hizo una sola persona.

## Semana 7 · S7

El contrato en docs/openapi.json, la prueba test_openapi_contract.py, el ADR 0004 y la sección 6 de arc42 están versionados y bien encaminados.
Para cerrar la semana, hagan auditable el contrato: versión visible, dos rutas contrastadas con el código y el fragmento con esquemas.
Confirmen que el workflow invoca la prueba y adjunten el enlace del run.
Aportar la ejecución en rojo, o el cambio incompatible que la produjo, es lo que distingue una prueba real de una que siempre pasa.
Completen el nivel 2 del C4 etiquetando cada flecha con protocolo y formato, y dejen el análisis de SonarCloud con su Quality Gate enlazado.
## Semana 6 · S6

Buen avance: el mapa de contextos y la sección 8 recogen el lenguaje y los límites del dominio, y el C4 nivel 3 y los ADR están al día. Para cerrar el segundo corte: (1) publiquen la evidencia auditable de SonarCloud: archivo de configuración, línea del workflow que invoca el scanner, run exitoso para el hash revisado y URL del Quality Gate; (2) incorporen la tabla módulo a datos y la lista de no conformidades con su plan, dejando explícito qué se esperaba, dónde se buscó y qué se halló sobre el código actual; (3) completen el registro de IA con lo rechazado y su motivo. Revisen además que el arranque quede en un solo comando para facilitar la reproducibilidad.

## Semana 8 · S8

### Recomendaciones prioritarias

- Cierren la evidencia de SonarCloud: falta el paso que invoca el scanner en el workflow y la URL pública del análisis con su Quality Gate. Un enlace genérico al panel no acredita que el análisis corra.
- Dejen de editar ADR ya aceptados: cuando cambie una decisión, escriban un ADR nuevo y marquen el anterior como reemplazado. Hoy varios ADR se editaron después de aceptarse sin ese enlace.
- La URL del sistema y la respuesta del health check quedan pendientes de calificar en esta pasada porque se entregan por Moodle.

El avance de la semana es sólido: la infraestructura está versionada como código, el README explica cómo recrear el entorno, el pipeline de la rama principal volvió a verde, los logs tienen estructura con campos, existe una métrica consultable ligada al escenario de rendimiento, los secretos se toman de la configuración del proveedor, la estimación de costos trae supuestos y punto de ruptura, arc42 representa las plataformas reales en la sección 7 y recoge costo y «sin tarjeta» en la sección 2, y cada decisión de plataforma tiene su propio ADR con la alternativa descartada y la capa gratuita verificada. Mantengan ese nivel y cierren las dos no conformidades transversales.

## Semana 9 · S9 (revisión definitiva)

La reserva grupal ya tiene implementación, decisión, trazabilidad, prueba de mutación y medición. La auditoría concreta corrige accesos entre módulos y conserva la escritura de cupos en su propietario. Completen la medición interna en la versión desplegada y comprueben que producción recibe y devuelve la cantidad solicitada. Falta cerrar Sonar. La comprobación independiente de secretos quedó pendiente por un bloqueo del entorno de revisión, no por una credencial encontrada.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

El nuevo experimento incluye 50 observaciones de base y 50 de fallo, con ajuste de timeout y caché. Las pruebas simulan timeout sin esperar y no demuestran degradación de extremo a extremo real. El CI está verde, pero el paso Sonar es un echo.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

Requests escribe Trips; push síncrono y timeout distinto del ADR.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · Requests modifica directamente los datos de ruta cuyo dueño es Trips:** La operación real accept_request llama refresh_trip_route_and_stop_eta y esta ejecuta UPDATE trips sobre route_geom, route_distance_m, route_duration_s y route_source. El límite de dueño único deja de proteger la actualización de rutas y la lógica de derivación queda repartida. Los cupos sí usan reserve/release públicos y no forman parte de este hallazgo. **Acción:** Mover la actualización de geometría y métricas de viaje a una operación pública de trips.application; Requests entrega las paradas/ids y conserva sus propias ETA. Eliminar también el import de helper privado de create_trip, o promoverlo a contrato público. Añadir regla de dependencias/escrituras entre módulos. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · El envío FCM secundario permanece en el camino síncrono de la respuesta:** ADR0013 exige que push no bloquee el flujo principal. El commit sucede antes y las excepciones se contienen, pero accept_request espera send_push y este llama send_each antes de retornar. Con FCM configurado, latencia/timeout de entrega se suma a la respuesta REST aunque la reserva ya esté confirmada. No se afirma que FCM esté configurado ni que haya lentitud real. **Acción:** Desacoplar envío después del commit mediante tarea/background worker con su propia sesión y timeout, o ratificar que es síncrono best-effort y acotar su presupuesto. Si se necesita entrega garantizada, usar outbox/reintentos; no reutilizar una sesión request cerrada en la tarea. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).
- **Media · La configuración Render sobreescribe el timeout ratificado de 1,4 s con 3,0 s:** La configuración versionada que recrea Render introduce ROUTING_TIMEOUT_SECONDS=3.0, anulando el default 1.4 que sostiene el presupuesto de ADR0014. Una recreación con ese manifiesto no conserva la mitigación documentada; el valor efectivo del panel y la latencia en producción no se verificaron. **Acción:** Cambiar el manifiesto a 1.4 o eliminar el override para usar el default ratificado; revisar la variable efectiva del panel con autorización y añadir prueba estática que compare configuración de despliegue y ADR/config. Medir nuevamente bajo condiciones relevantes, sin prometer el p95 a partir del valor nominal. [Contraste y evidencia](semana-10-corte2.md#deriva-d3).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Identifiquen el escenario operativo asignado antes de presentar la reserva grupal o el rendimiento como respuesta al segundo corte. Salud responde, pero aún deben demostrar el flujo sobre la versión desplegada, línea base y resultado comparables, observabilidad del reto y pipeline bloqueante. La sustentación permanece pendiente.

</details>

## Semana 9 · Aclaración de la revisión

La comprobación de credenciales bloqueada por el entorno del revisor queda excluida del cálculo por decisión docente. Sigue sin verificarse y no implica un hallazgo de filtración. Los demás criterios conservan su valoración sobre la entrega de cierre; véase la [matriz actualizada](semana-09-evidencia-s9.md).

## Semana 11 · Integración y resiliencia

La entrega analiza fallos y alternativas de extracción con criterios; las mitigaciones planificadas para 2027 son válidas como pendientes declarados. Corrijan la afirmación de unicidad atómica al crear solicitudes: el código consulta y luego inserta sin una restricción que impida la carrera concurrente. La aceptación de cupos sí tiene controles transaccionales y no debe confundirse con esa creación; el riesgo previo de privacidad tampoco está demostrado como resuelto.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Se reconoce caché geográfica con duración definida, transacciones de aceptación/rechazo y push como aviso con resincronización REST. Faltan tabla operación→garantía, política de invalidación de la caché, ADR del mayor costo de reversión y consolidación en arc42. No se ha demostrado un fallo de caché sobre cupos: el caché revisado es de geocodificación.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.
