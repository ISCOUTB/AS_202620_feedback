# Semana 16 · Proyecto final · ShareU

**Borrador técnico para revisión docente · 23 de noviembre de 2026. Sin calificación final, sin C1/C5 numéricos.**

## Estado y alcance de verificación

- Rama: `master`. Candidato: [869a47c05be71adbc77af4cce9c57e1cc6de4fa4](https://github.com/ISCOUTB/AS_202620_ShareU/commit/869a47c05be71adbc77af4cce9c57e1cc6de4fa4).
- Commit observado: 869a47c05be71adbc77af4cce9c57e1cc6de4fa4 2026-11-22T23:26:29-05:00 fix: API URL resuelta en runtime para que el frontend no se desconfigure.
- Referencia de cierre: 23 de noviembre, 05:00 UTC. La elegibilidad y correspondencia con SAVIO se consolidan por separado; no se certifican solo con la fecha interna del commit.
- Base S10: [39508608eae4c1a56a5e4fc11a055bf6afb2c003](https://github.com/ISCOUTB/AS_202620_ShareU/commit/39508608eae4c1a56a5e4fc11a055bf6afb2c003); [informe S10](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/revisiones/2026-2/AS_202620_ShareU/semana-10-corte2.md).
- Comparación exacta local: 141 files changed, 11801 insertions(+), 1605 deletions(-); 28 commits en el delta. Es tamaño de cambio, no medida de calidad o contribución individual.
- Se inspeccionaron archivos del SHA y evidencia de GitHub; no se ejecutó código estudiantil, no se modificó el repositorio y no se realizaron escrituras en los servicios desplegados. Las mediciones del equipo se distinguen de esta lectura independiente.
- El texto oficialmente asignado del desafío final no quedó verificado. No se sustituye por el escenario S10/S14, por una autoevaluación ni por preguntas propuestas.

## Síntesis

Hay una evolución sustantiva desde S10: persistencia Firestore, contrato ejecutable, caché, idempotencia, outbox y validación documental. La búsqueda desplegada fallida reportada el 21 de noviembre es evidencia histórica, no diagnóstico actual. La entrega necesita reconciliar referencias antiguas de cierre, verificar el flujo desplegado y completar la navegabilidad de C4 en la matriz.

## Alcance S10 → S16

S10 se centró en encontrar un documento en ≤3 interacciones; el informe anterior distinguió una muestra sintética de una línea base operativa y señaló despliegue/contrato sobreestimados. Ahora existen Docker/compose, tests/test_contrato.py y nueva medición. ADR0016 reemplaza la métrica operativa por p95/error/lecturas conservando la prueba funcional: esto no demuestra por sí solo usabilidad con usuarios ni asignación del desafío final.

## Decisiones y evolución

16 ADR. ADR0006 declara reemplazada la persistencia SQLite sin disco por ADR0012 Firestore. ADR0013 documenta caché con invalidación y ADR0015 reconoce outbox en proceso. ADR0016 cambia el indicador a latencia y costo de lecturas con umbrales. Se puede reconstruir decisión, implementación y limitaciones; el documento final mantiene un hash e129842 anterior al candidato y debe ajustarse.

Fuentes: [docs/adr/](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/docs/adr/) · [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/README.md).

## Calidad, resiliencia y seguridad

Medición local ASGI con Firestore falso: 300 solicitudes, calentamiento 20 y concurrencia 10; p95 72,15→67,54 ms, lecturas 1,00→0,07 por búsqueda y 0 % de errores, frente a ≤500 ms, ≤0,1 lecturas y <1 %. Son datos reproducibles documentados, no latencia de red/Firestore reales. Tests cubren publicación idempotente 201/200/409, ausencia de token 503, token erróneo 401 y fallo de persistencia 503. El outbox en memoria pierde pendientes al reiniciar; no equivale a un outbox transaccional durable.

## CI exacto, análisis estático y despliegue

Run exacto con tests/contrato, validación documental, medición y auditoría pip/npm exitosos. El paso Análisis SonarCloud está skipped; no atribuirle ejecución. En paralelo, check externo SonarCloud Code Analysis del SHA es success, con 15 nuevas incidencias y 0 % cobertura nueva. No se verificó requisito obligatorio de ese check para integrar. No se realizó nueva prueba de producción.

[Run exacto](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/45111871423) · [Checks del SHA](https://api.github.com/repos/ISCOUTB/AS_202620_ShareU/commits/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/check-runs) · [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_ShareU&branch=master).

**README y despliegue son evidencias diferentes.** README y guía publican https://shareu.iscoutb.dev y https://api-shareu.iscoutb.dev. La guía registra HTTP 500 de búsqueda el 21 de noviembre, pero el candidato incluye correcciones posteriores, incluida resolución runtime de URL de API. Por ello no se afirma que hoy siga caído ni que el nuevo código esté servido. La comprobación actual y la versión se agregan por separado.

## Coherencia arquitectónica y aspectos

arc42 separado en doce secciones con glosario; C4 tiene contexto, contenedores y componentes. Las 10 filas y 95 enlaces Markdown fueron revisados para existencia de destinos locales, sin faltantes. Sin embargo, la columna C4 de A1–A10 usa nombres entre backticks (web, api, firestore…), no enlaces navegables como exige el contrato. El validador exitoso no elimina este defecto semántico: [scripts/validar_docs.py:133–136](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/scripts/validar_docs.py#L133-L136) acepta un backtick como alternativa a un enlace. Recorridos profundos: A2, A4 y A10. La evidencia S16 y guía de tres páginas refieren e129842; no son la identificación definitiva de este corte.

Fuentes: [docs/arc42/](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/docs/arc42/) · [docs/c4/](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/docs/c4/) · [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/docs/aspectos.md).

### Tres recorridos de trazabilidad contrastados

- **A2 · Rendimiento/costo:** [docs/adr/0016-medicion-de-latencia-y-costo-de-lecturas.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/docs/adr/0016-medicion-de-latencia-y-costo-de-lecturas.md) → [app/documentos/repository.py](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/app/documentos/repository.py) → [tests/test_idempotencia.py](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/tests/test_idempotencia.py) → [docs/evidencia/mediciones/s14-local-asgi.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/docs/evidencia/mediciones/s14-local-asgi.md). Invalidación tras publicar, lectura de caché y artefactos de benchmark; medir con dobles no prueba producción.
- **A4 · Idempotencia:** [docs/adr/0013-cache-de-lectura-con-invalidacion.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/docs/adr/0013-cache-de-lectura-con-invalidacion.md) → [app/documentos/service.py](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/app/documentos/service.py) → [tests/test_idempotencia.py](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/tests/test_idempotencia.py) → [docs/evidencia/s12-datos-cache.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/docs/evidencia/s12-datos-cache.md). Las aserciones 43–62 verifican mismo id al repetir clave/cuerpo y 409 al cambiarlo; líneas 81–90 verifican visibilidad tras publicar.
- **A10 · Entrega asíncrona:** [docs/adr/0015-mensajeria-asincrona-con-outbox.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/docs/adr/0015-mensajeria-asincrona-con-outbox.md) → [app/eventos/outbox.py](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/app/eventos/outbox.py) → [tests/test_eventos.py](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/tests/test_eventos.py) → [docs/eventos/limites.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/docs/eventos/limites.md). El código declara pendientes/procesados/fallidos en memoria; tres intentos y deduplicación no sobreviven un reinicio.

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
| C4 1–3 coincide íntegramente | No verificado en totalidad | Niveles presentes; contraste limitado a recorridos señalados, no certificación exhaustiva |
| Todos los aspectos navegables de extremo a extremo | No cumple | Cobertura y huecos específicos descritos arriba; existencia de enlace no prueba semántica |
| Validación automática documental/arquitectónica | Cumple: documentación y reglas/pruebas de contrato | No se confunde el alcance del validador con corrección completa |
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
| Uso de IA | Registro presente; cobertura temporal completa no verificada | [docs/ia.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/869a47c05be71adbc77af4cce9c57e1cc6de4fa4/docs/ia.md); no inferir autoría o comprensión desde el registro |
| Pipeline/Sonar/gate | Ver lectura diferenciada | Run, check externo, scanner y bloqueo no son sinónimos |
| Ausencia de credenciales en árbol/historia | No verificado exhaustivamente | No se declara ausencia universal por una lectura documental; no se reproduce ningún secreto |
| Contribución de todos | No verificado por persona | Solo agregados, sin consolidación de identidades ni nota C5 |

## Niveles técnicos orientativos C2–C4, sin puntajes

- **C2 · Decisiones y evolución: Competente.** Se sostiene en las alternativas, sucesión y enlaces de implementación/prueba indicados. No se propone sobresaliente por cantidad de ADR.
- **C3 · Calidad, resiliencia y seguridad: Competente en alcance local documentado; sin extrapolación productiva.** Se sostiene en pruebas exactas y mediciones con límites; no equivale a aceptación productiva.
- **C4 · Coherencia y trazabilidad: Básico: mejora clara, pero C4 no navegable en tabla y referencia final desactualizada.** Los huecos descritos impiden afirmar que todos los artefactos coincidan y sean navegables.

No se calcula total, no se propone nota C1 y no se asigna C5.

## Colaboración: evidencia agregada

Actividad por mes de fecha de commit (incluye merges): 2026-08: 2, 2026-09: 49, 2026-10: 1, 2026-11: 26. Hay 8 identidades Git nominales, **no 8 personas verificadas**. No se publican nombres ni correos ni se concluye quién trabajó o faltó. 0 comentarios de revisión en línea en la colección consultada. No equivale a ausencia de toda conversación; queda pendiente evidencia de revisión cruzada sustantiva.

[Comentarios de revisión consultados](https://api.github.com/repos/ISCOUTB/AS_202620_ShareU/pulls/comments?per_page=100).

## Acciones concretas para cierre/defensa

1. Actualizar hash final y resultados de despliegue sin borrar las comprobaciones históricas; no diagnosticar Firestore solo por un HTTP 500.
2. Hacer navegable la columna C4 de las diez filas y ampliar el validador para detectar ese hueco.
3. Distinguir caché/outbox en memoria de garantías durables y medir el flujo con Firestore y red reales.

## Preguntas de sustentación

1. Si Firestore persiste un documento y el proceso cae antes de publicar el evento, ¿qué garantiza que la bandeja lo verá tras reiniciar?
2. Si el frontend abre pero la API da 503, ¿cómo diferencia la interfaz un error de cero resultados y qué versión concreta deben desplegar?
3. Si pasan de una a dos réplicas, ¿qué ocurre con invalidación de caché, deduplicación y métricas de lecturas? ¿Qué medición justificaría el costo del cambio?

## Pendiente de consolidación central

Agregar comprobaciones públicas con hora, códigos y versión servida; procedencia del desafío final; elegibilidad del corte. Conservar explícita la separación entre producción, resultados declarados, CI y demostración docente.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.
[Diferencias frente a la revisión S10](https://github.com/ISCOUTB/AS_202620_ShareU/compare/39508608eae4c1a56a5e4fc11a055bf6afb2c003...869a47c05be71adbc77af4cce9c57e1cc6de4fa4); es evidencia de cambio, no medida de mérito ni certificación de alcance acordado.

**Sondas de solo lectura del 23 de noviembre:**

- web: [https://shareu.iscoutb.dev/](https://shareu.iscoutb.dev/) → HTTP 200 (13:28:13 UTC).
- API salud: [https://api-shareu.iscoutb.dev/health](https://api-shareu.iscoutb.dev/health) → HTTP 200 (13:28:13 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
