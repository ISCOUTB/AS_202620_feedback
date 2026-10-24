# Retroalimentación publicable · PideUtb

## Semanas 1 y 2

## Evidencia S1

El repositorio está en la organización y es público (recuerden mantenerlo así: al inicio estuvo privado). La ficha del problema declara usuarios y alcance, y el registro de IA existe. Les faltó: las dos tensiones de calidad en la ficha, la tabla de ocho columnas en `docs/aspectos.md` (hoy es solo texto), la plantilla arc42 en `docs/arc42/` y las carpetas `docs/adr/` y `docs/c4/`. Pasen la ficha a Markdown dentro del repositorio: un PDF no se puede revisar con la misma facilidad.

## Evidencia S2

Excelente semana: las secciones 1, 2 y 3 de arc42 están completas y bien redactadas, los cinco escenarios tienen sus seis partes con medidas numéricas, el árbol de utilidad prioriza por impacto y riesgo con una convención explícita, y el C4 de contexto está como código Mermaid con flechas etiquetadas. Para el corte 1: (1) muevan la documentación a `docs/arc42/` y el C4 a `docs/c4/`; (2) revisen las anclas de los enlaces en `docs/aspectos.md` (varias usan guiones de menos y no llevan al escenario); (3) en `docs/ia.md` registren qué rechazaron de lo que propuso la IA y por qué; (4) repartan la contribución: todo el trabajo de esta semana está firmado por una sola cuenta y un integrante no aparece en el historial.

## Semana 3

Qué está bien: ADR 0001 bien armado (contexto real, alternativas descartadas con motivo, decisión y consecuencias), arranque con un solo comando documentado en el README y esqueleto con paquetes de dominio del monolito modular.

Qué corregir antes del corte 1 (semana 5):
1. Liguen la sección 4 del arc42 a los escenarios priorizados ESC-01/02/03 con tácticas por escenario (hoy la motivación queda a nivel de atributos del árbol).
2. Rehagan la matriz comparativa con filas por escenario del árbol de utilidad: qué escenario mejora y cuál empeora con cada estilo.
3. Enlacen el ADR 0001 desde `docs/aspectos.md` (usando la tabla de 8 columnas del curso) y desde el escenario que lo motiva.
4. Añadan un workflow en `.github/workflows/` que ejecute `pytest` y aporten el run en verde.
5. Registren en `docs/ia.md` qué se rechazó y por qué; muevan `arc42.md` a `docs/arc42/` y el C4 a `docs/c4/`.
6. Contribuyan todos los integrantes: esta semana solo aparecieron dos cuentas en el historial.

## Semana 4 · S4

La entrega documenta bien el arranque, el ADR y el corte vertical en el README, y el historial muestra participación de todo el equipo.
Para el primer corte: suban los diagramas C4 como código en docs/c4/ y verifiquen que los contenedores coincidan con backend/app.
Completen la tabla de aspectos con las columnas ID, C4, ADR, Código y Pruebas, y añadan al ADR la trazabilidad (commit que lo implementa y pruebas).
Registren en docs/ia.md lo que rechazaron de la IA y por qué.
No versionen el entorno virtual (.venv-1).
Ejecuten las pruebas en CI y dejen el enlace al run en verde.
El glosario y las secciones 1-6, 9, 10 y 12 de arc42 deben quedar visibles en docs/arc42/.

## Semana 5 · CORTE1

El proyecto está sólido en arquitectura y trazabilidad, con CI en verde y documentación completa. Para el corte, aseguren que el archivo de correcciones se llame exactamente 'correcciones.md' y esté en la raíz. Completen la restricción asignada en docs/restriccion-s5.md y el ADR 0002, y equilibren la contribución entre integrantes. El pipeline cumple, pero consideren integrar SonarCloud para el segundo corte. Sigan así.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Después del cierre siguieron trabajando el mismo lunes 7 de septiembre (entre las 08:19 y las 13:36), pero nunca crearon la etiqueta `corte-1`, ni antes ni después de esa hora. Como no existe la etiqueta, se calificó el último commit anterior al cierre, que sigue siendo el mismo de la entrega de S4: no hay diagnóstico de la restricción, ADR del reto, medición ni prueba específica en ningún punto del historial. Lo que hicieron después del cierre — mover `arc42.md` a `docs/`, crear una carpeta de C4 y ajustar el texto de los escenarios — no responde al reto y de todas formas no puede contar para esta entrega por llegar tarde. Sigue sin existir un pipeline de CI y el entorno virtual completo continúa versionado. No se encontró ningún documento de correcciones del equipo a la revisión preliminar. Antes de la sustentación: creen la etiqueta sobre el commit correcto para la próxima entrega, documenten la restricción asignada y midan una línea base real.

## Semana 7 · S7

Van muy bien: el contrato OpenAPI 3.1 y AsyncAPI 3.0 está versionado, con esquemas de datos, historial congelado y una política de compatibilidad muy clara. La guía para reproducir un run en rojo es excelente. Para cerrar la evidencia de la semana, adjunten la URL del run en rojo y la del run de CI del hash entregado, además de la URL pública de SonarCloud con el estado del Quality Gate. Añadan también los flujos de interacción de la sección 6 y el C4 nivel 2 con cada flecha etiquetada con protocolo y formato, y verifiquen ruta a ruta que el contrato y los routers coinciden. Con eso la entrega queda redonda.
## Semana 6 · S6

El equipo documenta un mapa de contextos claro y una auditoría de propiedad de datos con violaciones corregidas y planificadas. Para cerrar la evidencia, incorporen el enlace al análisis público de SonarCloud con su Quality Gate y el run de CI del hash revisado. Revisen los títulos de los ADR para que enuncien la decisión, no el tema. Aseguren que arc42 §8 incluya el lenguaje ubicuo y el mapa de contextos. Mantengan la trazabilidad de aspectos y el registro de IA, que están bien encaminados.

## Semana 8 · S8

### Recomendaciones prioritarias

- La sección 2 ya declara presupuesto cero y servicios gratuitos; aclaren la condición de tarjeta solo si afecta las plataformas elegidas. Completen la sección 7 del mismo arc42 con Vercel, backend, Supabase y su ubicación real.
- Corrijan la raíz y el health check que respondieron como recurso inexistente; publiquen URL, respuesta y hora de una nueva comprobación externa.
- Versionen la infraestructura y la inyección segura de secretos; añadan logs estructurados, una métrica, costo con punto de ruptura y ADR de plataforma.

La URL declarada es alcanzable como dominio, pero tanto la raíz como el health check respondieron con recurso inexistente durante la comprobación; por tanto, el sistema aún no es verificable desde fuera. El CI y el análisis estático son una buena base. Las no conformidades restantes son infraestructura reproducible, instrucciones de despliegue, logs estructurados, métrica operativa, costos, vista de despliegue, ADR por plataforma y configuración sensible sin valores inseguros por defecto. Primero recuperen la aplicación y el health check; después documenten el despliegue de punta a punta.

## Semana 8 · S8 (revisión definitiva, 2026-09-28)

La entrega cambió de forma sustancial respecto de la pasada temprana: ahora hay despliegue en Render, infraestructura declarada con Terraform (sitio, base de datos y protección de rama, con la excepción de la API documentada en lugar de disimulada), logs en una línea JSON por petición y una métrica consultable ligada a un escenario de calidad. También están el modelo de costo con supuestos y punto de cruce, la vista de despliegue con una pieza por fila y su ubicación, y una decisión de plataforma con la alternativa descartada. El chequeo de salud que declara lo que no comprueba es un acierto. Quedan pendientes de calificar la URL y el health check, que se entregan por Moodle: cuando la publiquen, adjunten el código de respuesta y la hora de la comprobación (la observación de «404» de la pasada anterior quedó superada por el nuevo despliegue).

Para cerrar, cuatro cosas concretas: (1) la sección 2 de arc42 debe recoger el límite de costo y la restricción de tarjeta; hoy la condición de tarjeta solo vive en el documento de comparación y en el ADR; (2) registren el uso de IA de la semana dentro del periodo —la entrada llegó después del cierre—; (3) no reescriban un ADR aceptado: cuando la decisión cambie, escriban uno nuevo y marquen el anterior como reemplazado; y (4) acrediten el pipeline y SonarCloud sobre el hash entregado, porque el job de análisis está condicionado a un token que sigue marcado como pendiente y falta la URL pública con el estado del Quality Gate.

## Semana 9 · S9 (revisión definitiva)

La auditoría detectó problemas reales y el código ya rechaza firmas cuando falta el secreto de la pasarela. Completen la rotación y configuración segura y acrediten el despliegue de la corrección, sin publicar valores. Enlacen el ADR del panel y la medición desde ESC-03; mantengan separado el tiempo programático local del flujo completo con una persona y red.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

ESC-04 incorpora autenticación, contrato 2.0 y ADR-0007, pero sesiones, tablas y cuentas no están acreditadas en producción. El GET público devuelve el código de canje, que funciona como secreto de retiro, a partir de un identificador entero. Es un hallazgo estático de operación y seguridad; no se consultaron pedidos reales ni se afirma explotación en producción.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación sigue pendiente de calificación docente; no se infiere a partir del repositorio. El [informe del corte](semana-10-corte2.md) y la [planilla](planilla.md) separan ese pendiente del componente técnico.

### Deriva arquitectónica al cierre S10

Canje sin arbitraje atómico; eventos síncronos y README rezagado.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Alta · La transición de entrega valida fuera de la escritura atómica:** ADR0007 atribuye el rechazo de todas las reutilizaciones del canje al estado final. Sin embargo, dos peticiones autorizadas concurrentes pueden leer Listo, validar el mismo código y ejecutar ambas UPDATE por id. También una transición basada en estado atrasado puede sobrescribir otra más reciente. La garantía del estado final necesita protección en persistencia; se trata de un interleaving permitido por el código, no de una duplicación observada en producción. **Acción:** Exponer una operación de repositorio que cambie estado solo si coincide el estado/version leído, y devuelva conflicto si otra petición ganó; mantener validación de tenant/código en la misma transacción o condición. Añadir prueba concurrente de dos entregas y de cancelar frente a preparar, exigiendo un único éxito. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · El canal al panel descrito como asíncrono es un bus síncrono sin consumidor de producción:** ADR0003 afirma que API→panel usa evento asíncrono y desacopla el momento. publicar invoca cada handler inline; confirmar_pago lo llama antes de retornar. Además el panel actual obtiene novedades por polling HTTP, no por ese canal. Capturar excepciones aísla errores, pero no el tiempo de ejecución. Hoy no se halló suscriptor de producción, por lo que no se afirma latencia real por callbacks. **Acción:** Ratificar en un ADR el diseño actual: webhook externo y polling de panel, con bus local síncrono para extensiones; o implementar un transporte/worker realmente desacoplado con consumidor y política de entrega. No basta devolver202 o ignorar el resultado del callback. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).
- **Baja · El README sigue anunciando memoria y contrato1.1 pese a la evolución vigente:** La entrada principal dice que hoy el estado vive en memoria y lista OpenAPI 1.1; el repositorio ya selecciona PostgreSQL y la aplicación anuncia 2.0 con sesiones. Esto oculta requisitos de migración y autenticación para quien instala o integra. **Acción:** Actualizar guía de arranque/estado y tabla de contratos a la versión vigente, distinguendo memoria de pruebas de PostgreSQL cuando está configurado e incorporando requisitos de sesiones y migraciones. Mantener el historial de contratos como histórico. [Contraste y evidencia](semana-10-corte2.md#deriva-d3).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Antes de la defensa, acrediten la corrección y configuración segura del secreto en el despliegue, y resuelvan o delimiten el panel sin autenticación. Confirmen el escenario operativo asignado y midan su línea base y respuesta en el entorno real. La disponibilidad actual no pudo comprobarse por una cancelación de la herramienta; eso no demuestra que el servicio esté caído.

</details>

## Semana 10 · Actualización docente

Se incorporó la calificación de sustentación comunicada por el docente en la planilla y en el [informe S10](semana-10-corte2.md). La evaluación técnica del repositorio mantiene su fundamento y sus observaciones.

## Semana 11 · Integración y resiliencia

La tabla de fallos, las pruebas de conciliación y la decisión razonada de no extraer cubren la evidencia. No confundan el run verde ni la corrección de la migración con recuperación de producción comprobada. Actualicen la bitácora de IA y preserven los ADR aceptados mediante decisiones sucesoras.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

La estrategia de no caché y los límites del bus están documentados. Corrijan la garantía de avance de estado: se valida antes de un UPDATE por identificador, sin la condición de estado prometida en la tabla. Falta un ADR que justifique la decisión de datos más costosa de revertir y su costo; alineen además el intervalo de sondeo y la flecha a la pasarela con el código vigente.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Presentó actualización y ya tiene despliegues, según confirmación docente. El README publica sitio y API bajo iscoutb.dev. El tablero genérico no representa todo el avance.

Issues al corte de consulta: **1 abiertas, 0 cerradas, 1 en total**. Sin cierres registrados. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Institucional**. Sitio y API; actualización y despliegues confirmados por docente. Dirección(es) documentada(s): https://pideutb.iscoutb.dev ; https://api-pideutb.iscoutb.dev/docs.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

La PR #28, fusionada el 20 de octubre, corrige el cálculo del ADR 0009: distingue una estimación de 704 MB, límites de 416 MB y una cuota de 512 MB. La PR #29 de interfaz institucional sigue abierta: su CI verde no convierte esos cambios en contenido integrado de master.

El docente confirmó actualización presentada y despliegues.

**Próximos pasos:**
- Contrastar avance de estado con UPDATE condicionado al estado esperado y prueba de carrera; tabla actual sobrestima atomicidad.
- ADR decisión de datos más costosa de revertir, no confundir con no extraer pagos; alinear sondeo5 s frente8 s y pasarela C4.
- Revisar/integrar PR #29 según equipo; desglosar issue1 genérica en tareas con responsable y criterio.

**Issues:** 1 abiertas y 0 cerradas; 1 abiertas sin responsable. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Institucional. Docente confirmó actualización presentada y despliegues. URL documentada: https://pideutb.iscoutb.dev ; https://pideutb.iscoutb.dev/panel.html ; https://api-pideutb.iscoutb.dev/docs. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#pideutb) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

La PR de identidad visual ya se fusionó el 23 de octubre: integra el sistema de diseño, la hoja de estilos y el índice del README. El CI de master pasó contratos, dependencias y Pytest en Python 3.11/3.12 con comprobación de ejecución PostgreSQL. Atención al alcance: el job SonarCloud termina success, pero sus pasos de análisis, cobertura y espera del Quality Gate quedaron skipped; no acredita un Gate aprobado. La aceptación visual de las pantallas a 375 px, ambos temas y teclado no fue verificada en esta revisión. Se conserva la confirmación docente de presentación y despliegues.

Actualización presentada y despliegues confirmados por el docente.

**Próximos pasos:**
- Verificar y registrar aceptación visual según su guía de diseño; el verde de pruebas backend no la sustituye.
- Restablecer evidencia de análisis y Quality Gate reales o documentar el análisis omitido; no reportarlo aprobado por el nombre del job.
- Para S12, distinguir el UPDATE condicional de marcar_pagado de actualizar_estado, que actualiza por id sin estado esperado; contrastar carreras y ajustar las garantías declaradas. Completar ADR comparativo de reversión y conciliar intervalos/documentación.

**Issues:** 1 abiertas y 0 cerradas; 1 abiertas sin responsable. El estado registrado no acredita por sí solo implementación.

**README:** Institucional. Sitio, panel y API institucionales. Presentación y despliegues confirmados por docente; sin nueva aceptación visual independiente. URL documentada: https://pideutb.iscoutb.dev ; https://pideutb.iscoutb.dev/panel.html ; https://api-pideutb.iscoutb.dev/docs. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#pideutb) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).
