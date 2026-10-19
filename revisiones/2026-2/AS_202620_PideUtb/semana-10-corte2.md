# Segundo corte · S10 · PideUtb · consolidación al cierre

**Actualización del feedback: 19 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_PideUtb |
| Rama evaluada | `master` |
| Hash calificado | `2497bfe7e0c7dc04e4cdf9b550254b9fd73df956` |
| Fecha del commit | 2026-10-12T14:27:07-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

ESC-04: validar el código de recogida en menos de 2 s y rechazar el 100 % de reutilizaciones; nueva autenticación y autorización del panel con sesiones y contrato 2.0.0.

Valoración técnica condicionada al escenario que el equipo declara en dossier S10, no una asignación docente inventada. No se bloquea la valoración por ausencia de asignación independiente.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Básico | 0,60 / 1,00 |
| C2 · Decisión e implementación | Competente | 0,80 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Insuficiente | 0,00 / 1,00 |
| C4 · Evolución arquitectónica trazable | Competente | 0,80 / 1,00 |
| C5 · Sustentación del reto | Calificación docente: 4,00 / 5,00 | 0,80 / 1,00 |

**Subtotal técnico: 2,20 / 4,00. C5 docente: 0,80 / 1,00. Total S10: 3,00 / 5,00.**

C5 incorpora la calificación de sustentación 4,00 / 5,00 indicada por el docente el 18 de octubre de 2026 y sincronizada en esta publicación. Su aporte es 4,00 / 5 = 0,80. Los puntajes C1–C4 y el hash técnico del cierre se conservan; no se infiere la sustentación del repositorio.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

ESC-04 incorpora autenticación, contrato 2.0 y ADR-0007, pero sesiones, tablas y cuentas no están acreditadas en producción. El GET público devuelve el código de canje, que funciona como secreto de retiro, a partir de un identificador entero. Es un hallazgo estático de operación y seguridad; no se consultaron pedidos reales ni se afirma explotación en producción.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/evidencia-s10.md:39–65](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/evidencia-s10.md#L39-L65); [docs/evidencia-s10.md:219–254](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/evidencia-s10.md#L219-L254); [docs/evidencia-s10.md:299–319](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/evidencia-s10.md#L299-L319); [docs/evidencia-s10.md:376–391](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/evidencia-s10.md#L376-L391)
2. [docs/adr/0007-autenticacion-del-panel.md:27–103](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/adr/0007-autenticacion-del-panel.md#L27-L103); [docs/adr/0007-autenticacion-del-panel.md:119–153](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/adr/0007-autenticacion-del-panel.md#L119-L153); [docs/adr/0007-autenticacion-del-panel.md:202–214](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/adr/0007-autenticacion-del-panel.md#L202-L214)
3. [backend/app/pedidos/router.py:45–54](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pedidos/router.py#L45-L54)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** Los módulos y la propiedad de datos están bien separados por servicios/contratos, y la nueva autenticación de panel ya está implementada. Persisten diferencias entre el canal de eventos descrito y el mecanismo real, una frontera transaccional débil para las transiciones del mostrador y un README anterior a PostgreSQL/contrato 2.0.

**Arquitectura declarada:** Monolito modular FastAPI con módulos menu/pedidos/pagos/usuarios, interfaces de service y contracts, repositorios propios. PostgreSQL/Supabase; ADR0003 distingue API síncrona, webhook de pago y evento de panel asíncrono. ADR0007 adopta sesiones opacas propias y tenant derivado de sesión.

**Arquitectura implementada:** main incluye routers y abre pool; crear pedido cruza service de menú/usuarios y escribe mediante repositorio propio. Webhook verifica HMAC, ejecuta procesar_evento en la petición y confirmar_pago usa UPDATE condicional atómico; a continuación publicar recorre callbacks locales. Panel HTML/JS consulta la cola por HTTP cada 8 s. Avanzar estado lee pedido, valida en servicio y guarda con UPDATE por id sin comparar estado anterior.

**Hallazgos materiales: 3.** Prioridad máxima: **Alta**.

<a id="deriva-d1"></a>

### D1 · La transición de entrega valida fuera de la escritura atómica

**Naturaleza:** implementación. **Prioridad:** Alta. **Confianza:** Alta sobre la ausencia de condición/transacción de lectura-escritura; el interleaving no se ejecutó..

**Motivo de prioridad:** Alta: está comprometida la garantía explícita de uso único del código de canje y de estados terminales en una operación central de entrega. Dos solicitudes concurrentes autorizadas pueden superar la misma validación y ser aceptadas. No se afirma entrega física duplicada, perjuicio monetario ni explotación observada.

**Declaración contrastada:**

- [docs/adr/0007-autenticacion-del-panel.md:109–115](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/adr/0007-autenticacion-del-panel.md#L109-L115) — ADR0007 atribuye el rechazo de toda reutilización al estado final.

**Implementación contrastada:**

- [backend/app/pedidos/router.py:125–141](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pedidos/router.py#L125-L141) — La ruta autenticada invoca avanzar_estado antes de responder.
- [backend/app/pedidos/service.py:222–239](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pedidos/service.py#L222-L239) — El servicio lee y valida el estado antes de la escritura.
- [backend/app/pedidos/service.py:251–257](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pedidos/service.py#L251-L257) — El canje se compara antes de llamar guardar.
- [backend/app/pedidos/repository.py:101–121](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pedidos/repository.py#L101-L121) — La escritura SQL solo filtra por id, sin estado previo o versión.
- [backend/app/pedidos/repository.py:158–166](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pedidos/repository.py#L158-L166) — La lectura usa su propio bloque de conexión y retorna después de cerrarlo.
- [backend/app/base_de_datos.py:119–136](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/base_de_datos.py#L119-L136) — Cada bloque with tiene su propia transacción; leer y guardar no comparten una unidad atómica.

**Efecto y alcance:** ADR0007 atribuye el rechazo de todas las reutilizaciones del canje al estado final. Sin embargo, dos peticiones autorizadas concurrentes pueden leer Listo, validar el mismo código y ejecutar ambas UPDATE por id. También una transición basada en estado atrasado puede sobrescribir otra más reciente. La garantía del estado final necesita protección en persistencia; se trata de un interleaving permitido por el código, no de una duplicación observada en producción.

**Corrección propuesta:** Exponer una operación de repositorio que cambie estado solo si coincide el estado/version leído, y devuelva conflicto si otra petición ganó; mantener validación de tenant/código en la misma transacción o condición. Añadir prueba concurrente de dos entregas y de cancelar frente a preparar, exigiendo un único éxito.

<a id="deriva-d2"></a>

### D2 · El canal al panel descrito como asíncrono es un bus síncrono sin consumidor de producción

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** Alta: dispatch y consumidor real revisados; ausencia de suscriptores acotada a backend/app y sitio..

**Motivo de prioridad:** Media: se describe un desacoplamiento temporal que el mecanismo no ofrece y un canal que el panel no consume; con ningún suscriptor productivo observado, no se presume bloqueo actual.

**Declaración contrastada:**

- [docs/adr/0003-estrategia-integracion.md:128–143](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/adr/0003-estrategia-integracion.md#L128-L143) — ADR0003 declara un canal asíncrono desde API al panel.
- [docs/adr/0003-estrategia-integracion.md:190–201](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/adr/0003-estrategia-integracion.md#L190-L201) — La decisión dice que el canal en proceso desacopla el momento.

**Implementación contrastada:**

- [backend/app/eventos.py:48–70](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/eventos.py#L48-L70) — publicar ejecuta los callbacks secuencialmente en la misma llamada.
- [backend/app/pedidos/service.py:150–167](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pedidos/service.py#L150-L167) — confirmar_pago llama publicar antes de retornar.
- [sitio/panel.js:327–337](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/sitio/panel.js#L327-L337) — El panel obtiene su cola mediante petición HTTP.
- [sitio/panel.js:468–470](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/sitio/panel.js#L468-L470) — Un setInterval dispara el refresco periódico.

**Efecto y alcance:** ADR0003 afirma que API→panel usa evento asíncrono y desacopla el momento. publicar invoca cada handler inline; confirmar_pago lo llama antes de retornar. Además el panel actual obtiene novedades por polling HTTP, no por ese canal. Capturar excepciones aísla errores, pero no el tiempo de ejecución. Hoy no se halló suscriptor de producción, por lo que no se afirma latencia real por callbacks.

**Corrección propuesta:** Ratificar en un ADR el diseño actual: webhook externo y polling de panel, con bus local síncrono para extensiones; o implementar un transporte/worker realmente desacoplado con consumidor y política de entrega. No basta devolver202 o ignorar el resultado del callback.

<a id="deriva-d3"></a>

### D3 · El README sigue anunciando memoria y contrato1.1 pese a la evolución vigente

**Naturaleza:** documentación desactualizada. **Prioridad:** Baja. **Confianza:** Alta..

**Motivo de prioridad:** Baja: desalineación de la guía principal frente a una evolución ya documentada e implementada.

**Declaración contrastada:**

- [README.md:25–28](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/README.md#L25-L28) — README afirma que el estado actual vive en memoria.
- [README.md:75–78](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/README.md#L75-L78) — La tabla principal aún anuncia OpenAPI 1.1.0.

**Implementación contrastada:**

- [backend/app/pedidos/repository.py:23–24](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pedidos/repository.py#L23-L24) — Memoria es la alternativa cuando falta DATABASE_URL.
- [backend/app/pedidos/repository.py:84–98](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pedidos/repository.py#L84-L98) — El repositorio implementa creación SQL con PostgreSQL.
- [backend/app/main.py:62–70](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/main.py#L62-L70) — La aplicación anuncia contrato 2.0.0.
- [docs/adr/0007-autenticacion-del-panel.md:121–126](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/adr/0007-autenticacion-del-panel.md#L121-L126) — ADR0007 documenta el cambio incompatible de autenticación.

**Efecto y alcance:** La entrada principal dice que hoy el estado vive en memoria y lista OpenAPI 1.1; el repositorio ya selecciona PostgreSQL y la aplicación anuncia 2.0 con sesiones. Esto oculta requisitos de migración y autenticación para quien instala o integra.

**Corrección propuesta:** Actualizar guía de arranque/estado y tabla de contratos a la versión vigente, distinguendo memoria de pruebas de PostgreSQL cuando está configurado e incorporando requisitos de sesiones y migraciones. Mantener el historial de contratos como histórico.

### Cobertura y límites de la auditoría

**Capas, dominio y adaptadores:** Inspeccionados main, routers, servicios y repository de pedidos, pagos y autenticación transversal. Cruces usan service/contracts; no se penaliza acoplamiento a repositorio propio porque no se eligió hexagonal.

**Persistencia:** PostgreSQL cuando existe PIDEUTB_DATABASE_URL, memoria alternativa declarada. Confirmar pago sí tiene compare-and-set; avance del mostrador no, por lo que no se generaliza idempotencia a todas las transiciones.

**API y autorización:** Panel usa dependencias de sesión y tenant efectivo; cambios de auth están aceptados en ADR0007. HMAC falla cerrado sin secreto; no se republica hallazgo histórico de secreto ya corregido. Integración efectiva con Wompi externo no verificada: iniciar_intento construye URL localmente.

**Despliegue:** Infra Terraform del sitio Render y configuración de pool revisadas; el recurso API manual es limitación declarada en infra/render.tf, no drift por faltar Docker/Terraform completo. Configuración remota no inspeccionada.

**Asincronía:** Webhook es una notificación temporalmente desacoplada del checkout, pero su handler procesa antes del 202. El bus en proceso llama callbacks síncronamente y no se encontraron suscriptores registrados en backend/app ni sitio; panel usa polling. No se afirma retraso actual causado por un suscriptor inexistente.

**Observabilidad:** /health consulta dependencias y /metricas ofrece p95 por proceso; no se extrapola al flujo humano completo. Main documenta limitación de ventana y reinicio.

**Fuentes de la cobertura:**

- [docs/adr/0001-estilo-arquitectonico.md:89–113](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/adr/0001-estilo-arquitectonico.md#L89-L113)
- [backend/app/pedidos/service.py:80–108](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pedidos/service.py#L80-L108)
- [backend/app/pedidos/repository.py:124–155](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pedidos/repository.py#L124-L155)
- [backend/app/pagos/router.py:46–81](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pagos/router.py#L46-L81)
- [backend/app/pagos/service.py:99–118](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/pagos/service.py#L99-L118)
- [backend/app/autenticacion.py:57–87](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/autenticacion.py#L57-L87)
- [docs/adr/0007-autenticacion-del-panel.md:27–35](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/docs/adr/0007-autenticacion-del-panel.md#L27-L35)
- [backend/app/main.py:44–59](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/main.py#L44-L59)
- [backend/app/main.py:165–185](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/backend/app/main.py#L165-L185)
- [infra/render.tf:32–54](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956/infra/render.tf#L32-L54)

**Límites adicionales:** Auditoría estática nueva del SHA indicado mediante git show, sin checkout ni ejecución de código estudiantil, sin lectura de PDF, sin publicar ni cambiar notas. No se verificaron el runtime desplegado, secretos/configuración de panel, cargas, CI en vivo ni disponibilidad. Los documentos de pruebas aportan intención y alcance, no una ejecución independiente de esta auditoría.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:46:05.402055+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`2497bfe7e0c7dc04e4cdf9b550254b9fd73df956`](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/2497bfe7e0c7dc04e4cdf9b550254b9fd73df956) (2026-10-12T14:27:07-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Semana 10 · Segundo corte · PideUtb

**Revisión preliminar.** Cierre previsto: 2026-10-12T05:00:00Z (medianoche de Colombia). El estado puede cambiar antes del cierre y debe volver a congelarse entonces.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_PideUtb |
| Estado revisado | `7e973faf7047e40137762befbc019f4736a813e6` en `origin/master` (2026-10-04T12:47:55-05:00) |
| Rama remota principal | `origin/master` |
| Observación | 2026-10-06T21:31:50.478484+00:00 |
| Punta revisada para S10 | `7e973faf7047e40137762befbc019f4736a813e6` (2026-10-04T12:47:55-05:00) |
| S9 congelado, solo como línea base | `7e973faf7047e40137762befbc019f4736a813e6` |

## Alcance y escenario operativo asignado

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

**Escenario asignado: No verificado.** Se encontró ESC-03 del panel y otros escenarios de calidad, pero no una fuente que identifique el reto operativo asignado al equipo para S10. Se documenta lo verificable sin presumir esa equivalencia. Fuente o búsqueda: [docs/evidencia-s9.md:11-26](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L11-L26) y [docs/adr/0005-maquina-de-estados-del-mostrador.md:21-30](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L21-L30); búsqueda en README, ADR, arc42 y evidencias. La evidencia de S6–S9 se usa como base; no se vuelve a calificar por existir. La evolución se contrastó con el hash S5 publicado `bbefae828185e9baa4df757ea073cbe84539cd3f`: el delta hasta esta punta modifica 109 archivos; los cambios pertinentes se enlazan en las filas de decisión, implementación y arquitectura. No se recalifica S5 ni se usan sus referencias históricas a etiquetas como requisito vigente.

## Matriz técnica preliminar

La fila «PDF de dos páginas» se omite por exclusión docente; quedan **12 filas**, incluida la sustentación pendiente.

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master 7e973faf7047e40137762befbc019f4736a813e6; revisión preliminar anterior al cierre futuro. |
| Despliegue accesible en el momento de la revisión | No verificado | URL declarada: https://pideutb-api.onrender.com/health, [README.md:13-15](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/README.md#L13-L15). Intento iniciado 2026-10-06T21:27:56Z: la herramienta canceló la sesión antes de devolver un resultado HTTP; no es evidencia de caída del servicio. No se probó flujo ni pago. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | Se encontró ESC-03 del panel y otros escenarios de calidad, pero no una fuente que identifique el reto operativo asignado al equipo para S10. Se documenta lo verificable sin presumir esa equivalencia. [docs/evidencia-s9.md:11-26](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L11-L26) y [docs/adr/0005-maquina-de-estados-del-mostrador.md:21-30](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L21-L30); búsqueda en README, ADR, arc42 y evidencias |
| Línea base medida y reproducible | No verificado | [docs/evidencia-s9.md:57-78](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L57-L78) mide porción local programática sin usuario/red; no es línea base del reto S10 confirmado sobre despliegue. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0005-maquina-de-estados-del-mostrador.md:32-72](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L32-L72) acredita alternativas y decisión del panel; falta correspondencia con asignación S10 y su montaje operativo. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [backend/app/pedidos/service.py:200-226](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/pedidos/service.py#L200-L226) prueba implementación estática; el delta desde S5 incluye PostgreSQL, contratos y panel, pero no se presume respuesta a reto no identificado. |
| Resultado contrastado con el umbral | No verificado | [docs/evidencia-s9.md:68-78](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L68-L78) contrasta tres interacciones/tiempo de sistema; falta resultado del reto asignado en entorno desplegado. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | Pipeline y cobertura exigida en [.github/workflows/ci.yml:109-128](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/.github/workflows/ci.yml#L109-L128); health implementado en [backend/app/salud.py:35-55](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/salud.py#L35-L55). La operación actual no se comprobó por cancelación y falta confirmar corrección/configuración de secreto en despliegue. Métrica del reto asignado pendiente. |
| Secretos protegidos | No cumple | Incidente documentado por el equipo en [docs/evidencia-s9.md:196-215](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L196-L215): un valor por defecto publicado se utilizaba para firmas de pago por falta de variable en el despliegue. El valor histórico sigue escrito en documentación/comentario del archivo backend/app/pagos/service.py (sin reproducirlo aquí). [backend/app/pagos/service.py:69-114](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/pagos/service.py#L69-L114) ya falla cerrado al faltar secreto. No se verificó rotación/configuración productiva ni que el despliegue ejecute la corrección. Retirar referencias al valor, rotarlo en los destinos donde se usó y acreditar configuración/despliegue seguro. Esto no afirma que sea explotable actualmente ni se probó pago alguno. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/c4/nivel2-contenedores.md:24-34](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/c4/nivel2-contenedores.md#L24-L34) representa validación de identidad por Supabase, mientras [docs/adr/0005-maquina-de-estados-del-mostrador.md:114-120](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L114-L120) reconoce panel sin autenticar. [docs/aspectos.md:21-30](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/aspectos.md#L21-L30) no enlaza ADR-0005/medición y conserva estado S7. Alinear lo implementado y lo futuro. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | Las notas históricas de títulos [docs/adr/0001-estilo-arquitectonico.md:7-19](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0001-estilo-arquitectonico.md#L7-L19) explican ediciones, pero no confirman/reemplazan una decisión por experimento del reto S10 identificado. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Pendiente de docente sobre despliegue y pipeline en vivo; no se puntúa desde el repositorio. |

Recuento descriptivo: 1 Cumple, 2 No cumple y 9 No verificado, sobre 12 filas. **No se transforma este recuento en nota.**

## Rúbrica del segundo corte (cinco criterios)

Escala del aula: 0,00 / 0,60 / 0,80 / 1,00 por criterio. Niveles exclusivamente propuestos al docente.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Asignación S10 no confirmada; ESC-03 se conserva como antecedente. |
| Decisión e implementación | No verificado | Pendiente | Decisión/código del panel presentes, pertinencia y experimento del reto pendientes. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Incidente de secreto y corrección estática documentados; operación/configuración/rotación actuales no verificadas. No se presume vulnerabilidad activa ni ausencia de riesgo. |
| Evolución arquitectónica trazable | No verificado | Pendiente | Desalineaciones C4/aspectos persisten; falta evolución ligada al reto confirmado. |
| Sustentación del reto | Pendiente de sustentación | Pendiente | La fija el docente en sesión. |

**Total final no determinado.** No se aplica la fórmula semanal. La sustentación corresponde al docente, sobre el entorno desplegado y con el pipeline en vivo; los criterios sin escenario confirmado no reciben un cero por esa falta de verificación.

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_PideUtb; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes; [docs/aspectos.md:8-13](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/aspectos.md#L8-L13) enlaza arc42, ADR, C4 e IA existente en el árbol. |
| Estado calificado identificable | Cumple | origin/master 7e973faf7047e40137762befbc019f4736a813e6; último commit anterior al cierre, fecha en cabecera. |
| Nombres de ADR según la convención | Cumple | Lista docs/adr 0001–0006 conforme a NNNN-titulo-en-kebab-case; [docs/adr/0005-maquina-de-estados-del-mostrador.md:1-5](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L1-L5) y [docs/adr/0006-componente-generativo.md:1-5](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0006-componente-generativo.md#L1-L5). |
| ADR aceptados no reescritos | No cumple | [docs/adr/0001-estilo-arquitectonico.md:5-19](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0001-estilo-arquitectonico.md#L5-L19) y [docs/adr/0002-propiedad-datos-establecimiento.md:5-23](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0002-propiedad-datos-establecimiento.md#L5-L23) ahora explican reescrituras de título; el historial también conserva edición [1b4f0f64](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/1b4f0f64bdb9e51f7e3ded11b7ec336e9a30240d). Reconocimiento histórico útil, pero no reemplazo formal ni ausencia de reescritura. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:259-319](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/ia.md#L259-L319) incorpora S9 con criterio técnico. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/ci.yml:226-277](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/.github/workflows/ci.yml#L226-L277) omite scanner/gate sin token; [docs/evidencia-s9.md:255-290](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L255-L290) declara que cobertura no ingresa al Quality Gate. Cobertura mínima 85 % sí se agregó al job de pruebas, [.github/workflows/ci.yml:109-128](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/.github/workflows/ci.yml#L109-L128). Única consulta PR del hash vacía; no se confunde éxito global con scanner ejecutado. |
| Sin credenciales en el repositorio ni en el historial | No cumple | Incidente documentado por el equipo en [docs/evidencia-s9.md:196-215](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L196-L215): un valor por defecto publicado se utilizaba para firmas de pago por falta de variable en el despliegue. El valor histórico sigue escrito en documentación/comentario del archivo backend/app/pagos/service.py (sin reproducirlo aquí). [backend/app/pagos/service.py:69-114](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/pagos/service.py#L69-L114) ya falla cerrado al faltar secreto. No se verificó rotación/configuración productiva ni que el despliegue ejecute la corrección. Retirar referencias al valor, rotarlo en los destinos donde se usó y acreditar configuración/despliegue seguro. Esto no afirma que sea explotable actualmente ni se probó pago alguno. El incidente histórico se conserva como no conformidad aunque se haya retirado el fallback ejecutable; barrido general pendiente no lo invalida. |
| Contribución de todos los integrantes | No verificado | Historial con firmas múltiples y archivo .mailmap; solo se consolidan identidades cuando la correspondencia está acreditada. La contribución por los tres integrantes debe confirmarse sin inferir personas de nombres/cuentas ni publicar correos. |

## Estado global del proyecto (overall)

Punta observada de `origin/master`: `7e973faf7047e40137762befbc019f4736a813e6` (2026-10-04T12:47:55-05:00). Hay 0 commits posteriores al estado congelado S9. Punta igual al cierre S9. La auditoría encontró un incidente de secreto real y el código ahora falla en cerrado; falta evidencia de rotación y despliegue seguro, sin afirmar explotación vigente. La cobertura tiene umbral en CI, pero sigue fuera de SonarCloud. El panel continúa sin autenticar, declarado y no oculto.

- Rotar/configurar de forma segura el secreto de la pasarela y acreditar que el despliegue usa el fail-closed; retirar el valor histórico de ejemplos/comentarios sin reproducirlo.
- Resolver autenticación/roles del panel y verificación del canje; la máquina de estados no autoriza al establecimiento.
- Completar fila ESC-03 con ADR-0005, código, prueba y medición navegables; reconciliar C4 con autenticación futura.
- Integrar cobertura/Quality Gate en Sonar y aportar run del hash actual.
- Confirmar escenario operativo S10, disponibilidad actual y atribución de contribuciones.

### Hallazgos anteriores cerrados o delimitados

- El fallback ejecutable del secreto se retiró y falta de configuración rechaza firma; solo cierre de código, no de rotación/producción.
- La auditoría de modularidad ya cubre archivos transversales; salud consume servicio, no repositorio ajeno.
- Ya existe ADR del panel y de no incorporación generativa.
- La cobertura se mide con umbral 85 % en el job de pruebas; se retiró la insignia que anunciaba una medida inexistente.
- La migración PostgreSQL y el panel antes tardíos están dentro de este delta; no se altera retrospectivamente S8.

## Preparación de la sustentación

1. Fallo: si falta la variable de la pasarela, ¿cómo se detecta que pagos legítimos se rechazan y cómo prueban el cierre seguro sin usar ni mostrar el valor expuesto?
2. Costo: ¿cómo cambian costo y tiempo de arranque al mantener pool PostgreSQL, agregar roles y sostener el pico de pedidos?
3. Medición: al incluir red y una persona real en ESC-03, ¿qué resultado los haría cambiar la interfaz o las transiciones y cómo aislarían ese efecto?

## Próximos pasos

Antes de la defensa, acrediten la corrección y configuración segura del secreto en el despliegue, y resuelvan o delimiten el panel sin autenticación. Confirmen el escenario operativo asignado y midan su línea base y respuesta en el entorno real. La disponibilidad actual no pudo comprobarse por una cancelación de la herramienta; eso no demuestra que el servicio esté caído.

</details>
