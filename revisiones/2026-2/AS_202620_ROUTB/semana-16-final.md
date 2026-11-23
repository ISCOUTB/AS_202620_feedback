# Semana 16 · Proyecto final · ROUTB

**Borrador técnico para revisión docente · 23 de noviembre de 2026. Sin calificación final, sin C1/C5 numéricos.**

## Estado y alcance de verificación

- Rama: `master`. Candidato: [eb38d11f34fdf647c840072d47fea49df7a845d1](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/eb38d11f34fdf647c840072d47fea49df7a845d1).
- Commit observado: eb38d11f34fdf647c840072d47fea49df7a845d1 2026-11-22T23:40:10-05:00 ROUTB - Final (#86).
- Referencia de cierre: 23 de noviembre, 05:00 UTC. La elegibilidad y correspondencia con SAVIO se consolidan por separado; no se certifican solo con la fecha interna del commit.
- Base S10: [adde017b72d73f210eef6cb48d97cdf1687f5141](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/adde017b72d73f210eef6cb48d97cdf1687f5141); [informe S10](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/revisiones/2026-2/AS_202620_ROUTB/semana-10-corte2.md).
- Comparación exacta local: 376 files changed, 44130 insertions(+), 6306 deletions(-); 16 commits en el delta. Es tamaño de cambio, no medida de calidad o contribución individual.
- Se inspeccionaron archivos del SHA y evidencia de GitHub; no se ejecutó código estudiantil, no se modificó el repositorio y no se realizaron escrituras en los servicios desplegados. Las mediciones del equipo se distinguen de esta lectura independiente.
- El texto oficialmente asignado del desafío final no quedó verificado. No se sustituye por el escenario S10/S14, por una autoevaluación ni por preguntas propuestas.

## Síntesis

La integración incorpora reservas grupales y concurrencia, rutas degradadas y despacho push fuera de la respuesta HTTP. Hay pruebas específicas y CI del candidato. No confundir la tarea BackgroundTasks con entrega durable: el reinicio puede perder avisos. La documentación final tiene desfases de C4 y del despliegue web.

## Alcance S10 → S16

En S10 se evaluó resiliencia de routing/geocodificación, con cero HTTP 500 y p95 inferior a 3,99 s, bajo supuesto de pertinencia, no asignación oficial acreditada. La entrega conserva reservas de uno a cuatro cupos y añade modalidad, cuenta y vehículo. El router de solicitudes ya programa avisos con BackgroundTasks después del caso de uso, corrigiendo el envío síncrono advertido en S10. No se heredan las notas anteriores ni se convierte ese escenario en el desafío final.

## Decisiones y evolución

29 ADR numerados. ADR0005 se vincula con ADR0015 para Render → Dokploy. ADR0025 explica por qué no se incorporó el bus en memoria de ADR0022, compara alternativas y define sesión propia para el envío de FCM. El código de requests/infrastructure/router.py, líneas 108–123 y 156–168, programa send_push_async_safe; test_push.py:253 y :291 verifica orden tras commit y sesión independiente. La evolución es defendible, sin llamar garantizada a una entrega best-effort.

Fuentes: [docs/adr/](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/adr/) · [README.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/README.md).

## Calidad, resiliencia y seguridad

La medición S14 declara tres rondas de 100 peticiones secuenciales: peor p95 631,76 ms desplegado con lista vacía y 2.564,52 ms local con cinco viajes, frente a 3.990 ms. No son cargas equivalentes ni prueba de capacidad concurrente. Para el fallo OSRM, el registro histórico declara N=50 por escenario y p95 1,6368→2,7047 s, con cero 500; no se reejecutó ni acredita hoy producción. La consistencia cuenta con tests explícitos de aceptación concurrente, duplicados y devolución de cupos.

## CI exacto, análisis estático y despliegue

Cuatro jobs exitosos: Flutter (formato/análisis/tests), pip-audit, backend (migraciones, suite y OpenAPI) y construcción Docker. El workflow no ejecuta scanner Sonar en este run. El endpoint de check-runs del SHA sí entrega SonarCloud Code Analysis externo exitoso: se reconoce esa evidencia y no se informa ausencia de análisis. Su resumen indica 36 nuevas incidencias y 0 % de cobertura de código nuevo; éxito no significa ausencia de deuda. No quedó acreditado en esta revisión que el check externo sea requisito obligatorio para integrar.

[Run exacto](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/45113237913) · [Checks del SHA](https://api.github.com/repos/ISCOUTB/AS_202620_ROUTB/commits/eb38d11f34fdf647c840072d47fea49df7a845d1/check-runs) · [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_ROUTB&branch=master).

**README y despliegue son evidencias diferentes.** README publica la API https://routb.iscoutb.dev y /health. El índice S16 publica https://approutb.iscoutb.dev y comprobaciones del 22 de noviembre, sobre una referencia anterior 9287f8a. Son resultados declarados en el repositorio, no nuevas verificaciones del revisor. El README incluso prescribe desplegar la rama Changes: no se debe asumir que producción coincide con master.

## Coherencia arquitectónica y aspectos

arc42 contiene secciones 1–12 y glosario; C4 niveles 1–3 están reunidos en docs/c4/context.md, ubicación válida. La vista de despliegue sigue describiendo el cliente celular sin representar Nginx/Flutter Web; el nivel de contenedores incluye reputación y el índice S16 reconoce componentes no correspondientes a módulos dedicados. Actualizar vistas, no eliminar evidencia porque esté en un único archivo. La tabla tiene 10 filas; 123 enlaces Markdown revisados, sin destinos locales inexistentes. Esto verifica existencia, no todos los fragmentos ni semántica. Se contrastaron a profundidad tres filas: 6, 7 y 9; las referencias genéricas a directorios y mediciones históricas no equivalen a nueva medición.

Fuentes: [docs/arc42/](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/arc42/) · [docs/c4/](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/c4/) · [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/aspectos.md).

### Tres recorridos de trazabilidad contrastados

- **6 · Reserva grupal:** [docs/adr/0007-reserva-grupal-de-cupos.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/adr/0007-reserva-grupal-de-cupos.md) → [backend/app/modules/trips/application/request_seats.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/backend/app/modules/trips/application/request_seats.py) → [backend/tests/test_requests_flow.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/backend/tests/test_requests_flow.py) → [docs/evidencia/prueba-reserva-grupal-semana9.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/evidencia/prueba-reserva-grupal-semana9.md). test_reserva_grupal_de_cuatro_y_cancelacion_libera_todos_los_cupos, línea 369, y rechazo de aceptación parcial, línea 445.
- **7 · Concurrencia:** [docs/adr/0021-integridad-solicitudes-y-concurrencia.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/adr/0021-integridad-solicitudes-y-concurrencia.md) → [backend/app/modules/requests/application/manage_request.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/backend/app/modules/requests/application/manage_request.py) → [backend/tests/test_requests_concurrency.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/backend/tests/test_requests_concurrency.py) → [docs/evidencia/concurrencia-solicitudes-cupos.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/evidencia/concurrencia-solicitudes-cupos.md). Los tests incluyen creaciones simultáneas, aceptación/retiro y aceptación/rechazo; el descuento se delega a reserve_request_seats.
- **9 · Resiliencia routing:** [docs/adr/0014-fallback-geocode-cache.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/adr/0014-fallback-geocode-cache.md) → [backend/app/shared/routing/service.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/backend/app/shared/routing/service.py) → [backend/tests/test_routing.py](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/backend/tests/test_routing.py) → [docs/evidencia/corte2-fallo-medicion.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/evidencia/corte2-fallo-medicion.md). Fallback y caché tienen prueba y medición histórica; no se eleva el timeout nominal a garantía de p95 productivo.

## Matriz S16

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Identificación de estado | Cumple en identificación; elegibilidad pendiente de consolidación | SHA y fecha arriba; no se usa HEAD posterior ni tags |
| Sistema desplegado estable | No verificado en esta pasada | README y registros históricos no sustituyen comprobación viva y revisión servida |
| Flujos principales con datos realistas | No verificado en producción | Suite exacta y recorridos citados prueban el entorno de CI, no la demostración |
| Caminos de error | Cumple en la suite inspeccionada | Pruebas y run exacto; se reserva comportamiento vivo |
| Respuesta al desafío asignado | No verificado | Falta procedencia verificable de la consigna específica; no es ausencia de código |
| Alcance frente a S10 | Cumple como contraste documental | Comparación de hashes, README y pendientes declarados; no implica alcance íntegro completado |
| Evolución de ADR | Cumple | Secuencia y decisiones citadas en el apartado correspondiente |
| Decisión confirmada/reemplazada con evidencia | Cumple en evidencia documental | Sustitución/ajuste descrito y recorrido de código/prueba, no reproducción del experimento |
| Atributos medidos frente a umbral | Cumple con alcance de las mediciones descritas | No extrapolar entorno, volumen, datos ni revisión |
| Modos de fallo y mitigaciones | Cumple en muestra técnica | Pruebas específicas y CI; quedan riesgos residuales declarados |
| arc42 1–12 y glosario | Cumple en estructura y contenido revisado | No basta contar archivos; ver desfases de coherencia señalados |
| C4 1–3 coincide íntegramente | No cumple | Niveles presentes; contraste limitado a recorridos señalados, no certificación exhaustiva |
| Todos los aspectos navegables de extremo a extremo | No verificado en totalidad | Cobertura y huecos específicos descritos arriba; existencia de enlace no prueba semántica |
| Validación automática documental/arquitectónica | Cumple: límites modulares y contrato | No se confunde el alcance del validador con corrección completa |
| Contribución de todos los integrantes | No verificado por persona | Se registra actividad agregada; no se equiparan identidades Git con personas |
| Revisión cruzada de fondo | No verificado con evidencia suficiente | Colección de comentarios revisada; límites abajo |
| Demostración y sustentación | No verificado | Corresponde al docente y jurado; no se puntúa desde el repositorio |

## Matriz transversal

| Criterio | Estado | Evidencia |
|---|---|---|
| Organización/nombre | Cumple en URL observada | Repositorio ISCOUTB/AS_202620; acceso anónimo no comprobado por separado |
| Estructura mínima | Cumple | README, arc42, ADR, C4, aspectos e IA presentes; ubicación combinada válida |
| Hash evaluable | Pendiente de consolidación del corte | Candidato fijado, no sustituido por revisiones posteriores |
| Convención de nombres ADR | Cumple | Catálogo numerado en docs/adr |
| Inmutabilidad histórica de ADR | No verificado exhaustivamente | Sucesión declarada no equivale a barrido de todos los cambios históricos |
| Uso de IA | Registro presente; cobertura temporal completa no verificada | [docs/ia.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/ia.md); no inferir autoría o comprensión desde el registro |
| Pipeline/Sonar/gate | Ver lectura diferenciada | Run, check externo, scanner y bloqueo no son sinónimos |
| Ausencia de credenciales en árbol/historia | No verificado exhaustivamente | No se declara ausencia universal por una lectura documental; no se reproduce ningún secreto |
| Contribución de todos | No verificado por persona | Solo agregados, sin consolidación de identidades ni nota C5 |

## Niveles técnicos orientativos C2–C4, sin puntajes

- **C2 · Decisiones y evolución: Competente.** Se sostiene en las alternativas, sucesión y enlaces de implementación/prueba indicados. No se propone sobresaliente por cantidad de ADR.
- **C3 · Calidad, resiliencia y seguridad: Competente, limitado a las pruebas y mediciones documentadas.** Se sostiene en pruebas exactas y mediciones con límites; no equivale a aceptación productiva.
- **C4 · Coherencia y trazabilidad: Básico: artefactos presentes, pero coherencia completa todavía no satisfecha.** Los huecos descritos impiden afirmar que todos los artefactos coincidan y sean navegables.

No se calcula total, no se propone nota C1 y no se asigna C5.

## Colaboración: evidencia agregada

Actividad por mes de fecha de commit (incluye merges): 2026-08: 40, 2026-09: 26, 2026-10: 12, 2026-11: 12. Hay 5 identidades Git nominales, **no 5 personas verificadas**. No se publican nombres ni correos ni se concluye quién trabajó o faltó. 12 comentarios de revisión en línea, todos de bot, en la colección consultada. No se infiere ausencia de toda conversación de PR; la revisión técnica cruzada humana queda pendiente de acreditar.

[Comentarios de revisión consultados](https://api.github.com/repos/ISCOUTB/AS_202620_ROUTB/pulls/comments?per_page=100).

## Acciones concretas para cierre/defensa

1. Sincronizar README, vista de despliegue y C4 con la web y el SHA/árbol servido.
2. Actualizar el índice S16, que aún refiere 9287f8a y su run, para señalar el candidato final sin borrar el registro histórico.
3. Mantener explícita la pérdida posible de push al reiniciar y mostrar reconciliación por REST.

## Preguntas de sustentación

1. Si el contenedor cae entre el commit de la reserva y el envío FCM, ¿qué estado conserva el pasajero y cómo recupera el aviso? ¿Qué cambia al exigir entrega durable?
2. Si veinte pasajeros solicitan el último cupo y el conductor cancela simultáneamente, ¿qué transacción y prueba sostienen el invariante sin sobreventa?
3. Si aumentan diez veces los viajes y OSRM responde tarde, ¿por qué la medición con lista vacía no basta y cómo compararían local y producción con el mismo conjunto?

## Pendiente de consolidación central

Agregar comprobaciones públicas con hora, códigos y versión servida; procedencia del desafío final; elegibilidad del corte. Conservar explícita la separación entre producción, resultados declarados, CI y demostración docente.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.
[Diferencias frente a la revisión S10](https://github.com/ISCOUTB/AS_202620_ROUTB/compare/adde017b72d73f210eef6cb48d97cdf1687f5141...eb38d11f34fdf647c840072d47fea49df7a845d1); es evidencia de cambio, no medida de mérito ni certificación de alcance acordado.

**Sondas de solo lectura del 23 de noviembre:**

- salud: [https://routb.iscoutb.dev/health](https://routb.iscoutb.dev/health) → HTTP 200, estado declarado `ok` (13:28:11 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
