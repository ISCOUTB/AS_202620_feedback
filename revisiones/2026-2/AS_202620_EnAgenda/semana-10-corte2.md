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
