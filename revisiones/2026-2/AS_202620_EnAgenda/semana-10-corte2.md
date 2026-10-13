# Segundo corte · S10 · EnAgenda · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_EnAgenda |
| Rama evaluada | `master` |
| Hash calificado | `4bec22f3821493014e8352ece8274bb2950e97db` |
| Fecha del commit | 2026-10-11T23:47:24-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

Solo documento operativo EC-XX de consulta pública/health y latencia; no se identificó reto S10 nuevo explícito.

Se evalúa técnicamente el escenario declarado; no se afirma asignación docente verificada.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Básico | 0,60 / 1,00 |
| C2 · Decisión e implementación | Básico | 0,60 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Básico | 0,60 / 1,00 |
| C4 · Evolución arquitectónica trazable | Básico | 0,60 / 1,00 |
| C5 · Sustentación del reto | Calificación comunicada por el docente | 0,84 / 1,00 |

**Subtotal técnico: 2,40 / 4,00. Total consolidado C1–C5: 3,24 / 5,00.**

Calificación de sustentación comunicada por el docente: **4,20 / 5,00**, incorporada como **C5 = 0,84 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

Se corrigieron la protección y normalización de métricas y se añadió la prueba de no filtración; el CI pasa. Faltan una línea base y un umbral medidos en el despliegue, así como una decisión coherente con toda la arquitectura.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/despliegue/medicion-dokploy.md:5–25](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/despliegue/medicion-dokploy.md#L5-L25); [docs/despliegue/medicion-dokploy.md:27–39](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/despliegue/medicion-dokploy.md#L27-L39); [docs/despliegue/medicion-dokploy.md:51–58](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/despliegue/medicion-dokploy.md#L51-L58) — URL, umbral y medición todavía pendientes
2. [docs/adr/0003-desplegar-api-flask-en-dokploy.md:24–74](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L24-L74); [docs/adr/0003-desplegar-api-flask-en-dokploy.md:95–99](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L95-L99) — decisión de plataforma y pendientes
3. [app/web.py:46–61](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L46-L61); [app/web.py:79–114](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L79-L114) — normalización, health y métricas protegidas

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** Dos desalineaciones documentales. El corte de invitaciones sigue la separación ligera declarada y la memoria temporal está expresamente reconocida; no se exige BD durable ni interfaces hexagonales no adoptadas.

**Arquitectura declarada:** Monolito modular, entrada web Flask/Jinja y API de invitaciones; dominio de tokens/vigencia; repositorio memoria; Dokploy. ADR1 conserva una elección tecnológica anterior no reconciliada.

**Arquitectura implementada:** Gunicorn→app.web:app; rutas web/REST→GestionarInvitacion→Invitacion→RepositorioInvitacionesMemoria. Métricas en memoria con Bearer y rutas normalizadas.

**Hallazgos materiales: 2.** Prioridad máxima: **Media**.

<a id="deriva-d1"></a>

### D1 · ADR1 conserva Next.js/Server Actions y prohibición de API mientras el sistema vigente es Flask con REST

**Naturaleza:** documentación desactualizada. **Prioridad:** Media. **Confianza:** Alta sobre el código y la documentación al hash; no acredita comportamiento del despliegue..

**Motivo de prioridad:** ADR2/3 y arc42 ya describen la implementación reciente; falta marcar explícitamente el alcance sustituido del ADR1 aceptado.

**Declaración contrastada:**

- [docs/adr/0001-usar-monolito-modular.md:106–122](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0001-usar-monolito-modular.md#L106-L122) — ADR1 aceptado prescribe Next.js/Server Actions y afirma que EnAgenda no expondrá API pública.

**Implementación contrastada:**

- [app/web.py:22–35](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L22-L35) — Flask crea una instancia del repositorio en memoria y la inyecta a GestionarInvitacion.
- [app/web.py:427–439](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L427-L439) — La aplicación registra una ruta REST GET de consulta de invitaciones y delega al servicio.
- [docs/arc42/05-vista-de-bloques-de-construcción.md:19–21](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/05-vista-de-bloques-de-construcci%C3%B3n.md#L19-L21) — arc42 identifica Flask/Jinja2 como entrada web actual e Invitaciones como corte funcional.
- [docs/adr/0003-desplegar-api-flask-en-dokploy.md:64–71](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L64-L71) — ADR3 adopta Dokploy y explicita API Flask construida con Dockerfile y ejecutada mediante Compose.

**Efecto y alcance:** Las decisiones vigentes parecen contradictorias sobre cliente, entrada HTTP y contrato, dificultando futuras modificaciones.

**Corrección propuesta:** Registrar aclaración/supersesión parcial de ADR1: mantener monolito modular, sustituir Next.js/Server Actions y actualizar exposición REST. No cambiar la implementación solo para seguir una decisión histórica.

<a id="deriva-d2"></a>

### D2 · El procedimiento operativo aún espera /metrics 200 sin explicar el token

**Naturaleza:** documentación desactualizada. **Prioridad:** Baja. **Confianza:** Alta sobre el código y la documentación al hash; no acredita comportamiento del despliegue..

**Motivo de prioridad:** La protección se implementó correctamente; lo rezagado es la instrucción de comprobación.

**Declaración contrastada:**

- [docs/arc42/07-vista-de-despliegue.md:86–93](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/07-vista-de-despliegue.md#L86-L93) — El procedimiento de arc42 espera HTTP 200 en GET /health y GET /metrics sin detallar autorización.
- [README.md:289–295](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/README.md#L289-L295) — El smoke check de README propone curl a /metrics sin cabecera Bearer.

**Implementación contrastada:**

- [app/web.py:90–114](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L90-L114) — /metrics exige token de observabilidad y después expone contadores generales/de invitaciones.

**Efecto y alcance:** Un operador siguiendo README/arc42 interpreta 401/503 esperado como fallo del servicio o no configura el secreto requerido.

**Corrección propuesta:** Actualizar smoke check para configurar ENAGENDA_METRICS_TOKEN, enviar Bearer de forma segura y distinguir 401/503 de liveness /health. No desproteger métricas para satisfacer el ejemplo antiguo.

### Cobertura y límites de la auditoría

**Capas y dominio:** Aplicación delega reglas al dominio; usa repositorio concreto dentro de módulo como capas ligeras. La dependencia concreta sola no viola ADR1 que descarta hexagonal completa.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [src/invitaciones/aplicacion/gestionar_invitacion.py:1–26](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/src/invitaciones/aplicacion/gestionar_invitacion.py#L1-L26) — GestionarInvitacion importa la entidad y el repositorio concreto e invoca Invitacion.crear antes de guardar.
- [src/invitaciones/aplicacion/gestionar_invitacion.py:30–60](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/src/invitaciones/aplicacion/gestionar_invitacion.py#L30-L60) — El servicio busca por token, valida vigencia y delega cambio de estado a la entidad antes de guardar.
- [docs/adr/0001-usar-monolito-modular.md:77–80](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0001-usar-monolito-modular.md#L77-L80) — ADR1 descarta hexagonal completa porque su coste no compensa todavía la complejidad del proyecto.

**Persistencia:** Repositorio diccionario por proceso explícitamente temporal; no se infiere durabilidad ni incoherencia por ausencia de BD.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [src/invitaciones/infraestructura/repositorio_memoria.py:1–12](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/src/invitaciones/infraestructura/repositorio_memoria.py#L1-L12) — El repositorio guarda invitaciones en un diccionario del proceso y las busca por token.
- [docs/arc42/05-vista-de-bloques-de-construcción.md:125–131](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/05-vista-de-bloques-de-construcci%C3%B3n.md#L125-L131) — arc42 declara almacenamiento temporal en memoria que no sobrevive al reinicio.

**API y autorización:** GET/POST de invitación por token delega vigencia; métricas Bearer; no se verificó acceso real ni envío de correos.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [app/web.py:427–459](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L427-L459) — GET /api/v1/invitaciones/{token} consulta el servicio, responde JSON y aumenta el contador de consultas.
- [app/web.py:494–506](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L494-L506) — El POST llama gestionar_invitacion.responder y convierte ValueError a respuesta 404.
- [app/web.py:90–101](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L90-L101) — /metrics devuelve 503 sin secreto configurado y 401 si falta o no coincide el Bearer.

**Despliegue:** Docker/Gunicorn único servicio Compose y dominio aún pendiente declarado. No se afirma caída ni disponibilidad pública.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [Dockerfile:11–15](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/Dockerfile#L11-L15) — Dockerfile inicia Gunicorn apuntando a app.web:app en el puerto configurado.
- [docker-compose.yml:1–11](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docker-compose.yml#L1-L11) — Compose define un único servicio construido desde Dockerfile, publica 5000 y carga .env.
- [docs/adr/0003-desplegar-api-flask-en-dokploy.md:91–99](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L91-L99) — ADR3 deja URL pública, HTTPS, cuotas y rollback pendientes de confirmar.

**Asincronía:** Llamadas en proceso y HTTP síncrono; no broker, worker ni envío de invitaciones automatizado en la ruta auditada.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [app/web.py:323–345](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L323-L345) — El formulario crea invitaciones por el servicio y construye enlaces para renderizar la pantalla de resultados.
- [src/invitaciones/aplicacion/gestionar_invitacion.py:16–28](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/src/invitaciones/aplicacion/gestionar_invitacion.py#L16-L28) — crear_invitacion delega construcción a Invitacion.crear y persiste mediante el repositorio.

**Observabilidad:** Contadores por plantilla de ruta evitan tokens; /metrics requiere secreto y autorización.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [app/web.py:46–61](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L46-L61) — El contador HTTP usa la plantilla de ruta de Flask para no guardar tokens de invitaciones.
- [app/web.py:90–114](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L90-L114) — /metrics exige token de observabilidad y después expone contadores generales/de invitaciones.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:45:53.877459+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`4bec22f3821493014e8352ece8274bb2950e97db`](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/4bec22f3821493014e8352ece8274bb2950e97db) (2026-10-11T23:47:24-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Segundo corte S10 · avance preliminar · EnAgenda

**Preliminar, no es cierre ni calificación final.** Cierre previsto: **2026-10-12T05:00:00Z**.

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_EnAgenda](https://github.com/ISCOUTB/AS_202620_EnAgenda) |
| Rama remota principal | `master` |
| Base S5 del segundo corte | `696882ecb889c01bdc93170556c90044acf4fcff` |
| Base S8 | `2c7d77a421ab95b89dd68d696d49277e9f36a45c` |
| Estado revisado | `c2077ac55a29562adc728734ca4c283ccb40f310` en `origin/master` (2026-10-05T10:40:19-05:00) |
| S9 congelada | `5aa889370dcf342ba06666893b97f8065b513de9` · 2026-10-04T23:46:49-05:00 |
| Punta actual / S10 preliminar | `c2077ac55a29562adc728734ca4c283ccb40f310` · 2026-10-05T10:40:19-05:00 |
| Comprobación | 2026-10-06T21:29:42Z |
| Corrección documental | 2026-10-07 · seguridad y C3; se conservan el hash y la observación original |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Evolución desde S5 hasta la punta

Base tomada del informe S5 publicado y resuelta por Git, sin etiquetas: `696882ecb889c01bdc93170556c90044acf4fcff`. En el delta S5→HEAD cambian 42 rutas no PDF (conteo de árboles; no mide mérito). Desde S5 se incorporan contrato API, Docker/Dokploy, health y métricas, nueva UI y creación múltiple. HEAD completa la plantilla faltante y documentación. El cambio se reconoce sin trasladarlo a la nota S9 ni dar por demostrado el experimento S10.

## Escenario operativo asignado

No verificado. Se buscaron la asignación en README, ADR, aspectos, arc42 y mediciones. El documento de medición mantiene EC-XX y un umbral por aprobar, lo que tampoco identifica un reto operativo asignado. Hace falta la consigna oficial S10; [docs/despliegue/medicion-dokploy.md:9–25](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/despliegue/medicion-dokploy.md#L9-L25).

## Matriz de evidencia S10

Se omite la fila de PDF de dos páginas por exclusión docente. Quedan 12 filas observables o pendientes; este recuento no es una fórmula de nota.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | HEAD master identificable y anterior al cierre futuro; preliminar. |
| Despliegue accesible en el momento de la revisión | No verificado | No hay URL pública verificable: el README mantiene host y HTTPS pendientes; [README.md:305–319](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/README.md#L305-L319). El estado Done de Dokploy no sustituye una comprobación externa. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | No se localiza consigna oficial S10; el documento operativo todavía usa EC-XX y umbral sin definir; [docs/despliegue/medicion-dokploy.md:9–25](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/despliegue/medicion-dokploy.md#L9-L25). |
| Línea base medida y reproducible | No cumple | El procedimiento de veinte solicitudes es un plan sin datos; no hay línea base medida reproducible; [docs/despliegue/medicion-dokploy.md:27–39](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/despliegue/medicion-dokploy.md#L27-L39). |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | Dokploy tiene ADR y alternativa institucional, pero no hay respuesta coherente trazada al escenario S10 asignado; [docs/adr/0003-desplegar-api-flask-en-dokploy.md:24–74](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L24-L74). |
| Respuesta implementada o configurada sobre el MVP | No verificado | Cambios reales de UI/observabilidad y plantilla tardía, pero falta conocer escenario asignado para juzgar respuesta; [docs/ia.md:45–47](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/ia.md#L45-L47). |
| Resultado contrastado con el umbral | No cumple | Medición externa y umbral siguen pendientes en la punta; [docs/despliegue/medicion-dokploy.md:51–58](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/despliegue/medicion-dokploy.md#L51-L58). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | CI success, health y contadores presentes; no logs estructurados ni métrica ligada al escenario definido. Riesgo: request.path se almacena sin normalizar y /metrics lo devuelve públicamente, exponiendo tokens usados en rutas; [app/web.py:45–58](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/app/web.py#L45-L58), [app/web.py:87–101](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/app/web.py#L87-L101). No se consultaron tokens ni datos reales. |
| Secretos protegidos | No cumple | El código conserva `request.path` sin normalizar en `http_requests_by_path` ([app/web.py:45–58](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/app/web.py#L45-L58)) y lo devuelve desde `/metrics`, definido sin autenticación en la aplicación ([app/web.py:87–101](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/app/web.py#L87-L101)). Las rutas de invitación llevan un token cuya posesión permite consultar y responder ([app/web.py:360–411](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/app/web.py#L360-L411)); por tanto, la ausencia de credenciales hardcodeadas no acredita la protección de estos secretos dinámicos. Conclusión por lectura estática del hash revisado: no se consultaron métricas ni tokens reales y no se verificó exposición o incidente en producción. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | La documentación actual mejora Flask/plantillas, pero ADR-0001 sigue describiendo Next.js sin API y el contrato no representa todas las rutas de UI nuevas; [docs/adr/0001-usar-monolito-modular.md:116–125](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/adr/0001-usar-monolito-modular.md#L116-L125), [docs/aspectos.md:5–12](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/aspectos.md#L5-L12). |
| Decisión anterior confirmada o reemplazada con evidencia | No cumple | La transición Render→Dokploy reescribe/elimina ADR-0003 aceptado, en vez de preservarlo y sustituirlo con evidencia; [docs/adr/0003-desplegar-api-flask-en-dokploy.md:1–18](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L1-L18). |
| Sustentación del reto sobre el entorno desplegado | No verificado | Pendiente del docente en sustentación con entorno desplegado y pipeline en vivo. |

Recuento corregido el **2026-10-07**: **1/12 Cumple, 6/12 No cumple y 5/12 No verificado**. Este recuento de comprobación no calcula una nota final de S10.

## Rúbrica específica de cinco criterios

| Criterio | Nivel sugerido | Puntaje | Fundamento |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | No se localizó evidencia de asignación oficial del escenario; no se sustituye por un escenario genérico. |
| Decisión e implementación | No verificado | Pendiente | No se puede juzgar la respuesta al escenario asignado hasta identificarlo. |
| Operación, seguridad y observabilidad | Insuficiente | 0,00 | La ruta de exposición de tokens está acreditada en el código citado en «Secretos protegidos». La [instrucción 7 de la ficha S10](https://github.com/ISCOUTB/AS_202620_feedback/blob/94d9261bb265315dd31eec984ce9abd34fe33bb2/fichas/semana-10-corte2.md#L61-L62) sitúa este criterio en insuficiente si se exponen secretos. Este nivel sugerido se funda en la evidencia estática; no afirma un incidente en producción ni resuelve la asignación del escenario o la sustentación. |
| Evolución arquitectónica trazable | No verificado | Pendiente | La coherencia documental se informa en la matriz; falta demostrar la evolución específica exigida por el reto. |
| Sustentación del reto | Pendiente del docente | Pendiente | Sustentación sobre el entorno desplegado y pipeline en vivo; no se puntúa desde el repositorio. |

Escala aplicable: 0,00 / 0,60 / 0,80 / 1,00 por criterio. **No se calcula total mientras haya criterios pendientes.** No se usa la fórmula semanal. Cualquier nivel es propuesta al docente; la sustentación queda a su cargo.

## Matriz transversal · punta actual

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público en organización ISCOUTB y nombre conforme; master declarado remoto, [README.md:1–8](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/README.md#L1-L8). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes y tablas ampliadas; [docs/aspectos.md:1–12](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/aspectos.md#L1-L12). |
| Estado calificado identificable | Cumple | Punta master c2077ac55a29562adc728734ca4c283ccb40f310 de 2026-10-05T10:40:19-05:00, preliminar anterior a cierre S10. |
| Nombres de ADR según la convención | Cumple | ADR 0001–0003 usan convención de nombres; [docs/adr/0003-desplegar-api-flask-en-dokploy.md:1–4](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L1-L4). |
| ADR aceptados no reescritos | No cumple | El ADR-0003 aceptado de Render en S8 fue eliminado y sustituido por otro 0003 de Dokploy sin preservar la decisión ni declarar nuevo ADR supersedes. [docs/adr/0003-desplegar-api-flask-en-dokploy.md:1–18](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L1-L18). Se verificó el original aceptado en el hash S8. |
| docs/ia.md al día para la semana | Cumple | Registro condensado en tabla y nueva entrada de diagnóstico de plantilla faltante; [docs/ia.md:43–47](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/ia.md#L43-L47). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI exacto success, pero no hay scanner/configuración/Quality Gate SonarCloud en el árbol; [.github/workflows/ci.yml:13–45](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/.github/workflows/ci.yml#L13-L45) solo prueba y build. |
| Sin credenciales en el repositorio ni en el historial | No verificado | No hay credenciales reales hardcodeadas ni .env versionado en el snapshot; no se certifica todo el historial. Existe riesgo operativo distinto: métricas exponen request.path, que puede contener tokens de invitación. |
| Contribución de todos los integrantes | No verificado | Cuatro firmas, 173 commits agregados en S9, para tres integrantes. Variantes deben consolidarse por evidencia de identidad; no se adivina la equivalencia. Punta actual: 4 firmas y 177 commits agregados; no equivalen automáticamente a personas. |

## Actions en la punta actual

- [CI: success](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/37334800510), 2026-10-05T15:41:02Z, SHA exacto del estado indicado.
- [pages build and deployment: success](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/37334799574), 2026-10-05T15:41:02Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Barrido estático sin credenciales reales hardcodeadas; tokens de invitación se generan con secrets.token_urlsafe y el workflow usa claves efímeras de prueba. No hay .env versionado. No se certifica historia completa. Hallazgo de privacidad por lectura de código: los paths con tokens se agregan a http_requests_by_path y se publican en /metrics. Se recomienda usar plantillas de ruta/redactar tokens y restringir acceso a métricas; no se accedió a invitaciones reales.

## Estado global del proyecto (overall)

Se resolvieron los conflictos de merge de infraestructura y el CI del hash S9 está en verde en ejecución posterior al cierre. El flujo S9 requería invitados.html, ausente en ese árbol: la plantilla y CSS llegaron después, junto a documentación y tabla de aspectos ampliadas. Se reconoce la corrección tardía sin modificar S9. La URL pública/HTTPS, medición y umbral siguen pendientes. La nueva observabilidad puede divulgar tokens por rutas crudas y debe normalizarse antes de exponer usuarios reales.

El delta S9 contiene 11 commits respecto de S8; hay 4 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Antes del cierre

- Normalizar/redactar tokens en métricas y restringir /metrics: no publicar rutas crudas de invitaciones.
- Crear prueba del flujo completo POST / → plantilla de invitados → creación → respuesta; un test directo a /crear-invitaciones omite la pantalla intermedia.
- Configurar host/HTTPS, medir salud y flujo principal con umbral y línea base identificables.
- Aportar ADR coherente de evolución del flujo y preservar decisiones aceptadas con un ADR sustituto para Dokploy.
- Añadir auditoría de erosión del cambio, inventario verificado de propuestas/dependencias y decisión sobre componente generativo.
- Integrar SonarCloud y publicar scanner, run y Quality Gate; aclarar asignación operativa S10.

## Tres preguntas de sustentación

1. ¿Qué pasa con invitaciones, tokens y contadores si el contenedor reinicia, y cómo evitarían exponer tokens mediante /metrics?
2. ¿Qué cuotas de CPU/RAM/tráfico ofrece Dokploy y cuándo deja de ser válida la estimación de costo cero?
3. El test directo no detectó TemplateNotFound: ¿qué cambiarían en la prueba para cubrir el recorrido real del organizador?

</details>
