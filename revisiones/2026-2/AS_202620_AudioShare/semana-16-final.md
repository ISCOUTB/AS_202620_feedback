# AudioShare · Semana 16 · proyecto final

> Revisión técnica documental. Los niveles son propuestas parciales, no calificación final. La demostración y el criterio 5 corresponden al docente.

**Hallazgo principal:** El flujo integrado pasó de archivos MP3 a audio en vivo por WebSocket; hay implementación y CI, no medición física ni vinculación del despliegue al hash exacto. El README excluye Android nativo pese al motor Android de esta revisión.

- Rama principal: `master`. [Candidato de cierre `47a380ec3c4e8597a9aa6f02b19daab7a9d77faa`](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa) observado tras el corte de referencia del 23-11-2026 a las 05:00 UTC (cierre del domingo 22 en Colombia). SAVIO, envío y transición en segundos inmediatos no comprobados.
- [Línea base S10 `1da287c662986033871ef0e044ed29894b978593`](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/1da287c662986033871ef0e044ed29894b978593); [comparación S10→S16](https://github.com/ISCOUTB/AS_202620_AudioShare/compare/1da287c662986033871ef0e044ed29894b978593...47a380ec3c4e8597a9aa6f02b19daab7a9d77faa): 74 commits por delante según GitHub. No se usaron tags ni ramas de trabajo.
- [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) y [contrato del curso](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

## Matriz técnica de la ficha

### C1 · Sistema funcional, desafío y alcance (1,25)

La línea base S10 trataba sincronía de pista y no integraba plenamente reloj/ACK de Flutter. En S16, [README](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/README.md#L149-L178), [ADR-0015](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/docs/adr/0015-transmision-de-audio-en-vivo.md#L6-L34) y [relay](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/src/modules/live/index.ts) muestran salas, emisor/receptor y transporte PCM temporizado. El [motor Android](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/lib/features/live/data/live_engine_android.dart#L16-L76) ofrece captura y reproducción; su existencia y un APK de CI no demuestran funcionamiento físico. El [relay test](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/tests/live-relay.test.ts#L150-L260) cubre errores de sala/autorización y controles. No se constató guía final separada ni desafío asignado. La URL declarada es [audioshare.iscoutb.dev](https://audioshare.iscoutb.dev); README documenta health histórico sin SHA y distingue imagen Docker Hub de Dokploy. Salud, flujo y error en ejecución actual: no verificados.

### C2 · Decisiones y evolución (1,00)

La evolución reconstruye monolito, Flutter, sincronización por reloj/ACK, MP3 HTTP y paso a vivo; ADR-0015 explica temporización, plataformas y desventajas de PCM. [EC-01](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/docs/evidencia-a01-ec01.md#L20-L75) compara con/sin corrección (≈2–7 ms frente a ≈2958–2998 ms de desfase real en las corridas citadas), y presenta por qué medir sobre el mismo reloj. Confirma el mecanismo en el banco sintético, no el audio perceptible del sistema nuevo.

### C3 · Calidad, resiliencia y seguridad (1,00)

[Escenarios EC-01–04](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/docs/escenarios_calidad.md) y la [tabla de aspectos](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/docs/aspectos.md#L150-L191) distinguen objetivos y validaciones físicas pendientes. [Backend/Sonar](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/45107710472), [Flutter Web](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/45107710349), [APK](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/45107710313) e [imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/45107710299) pasaron en el SHA; no sustituyen medición de latencia y desfase físico, revocación en el entorno desplegado o funcionamiento con red variable. [Privacidad](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/docs/privacidad.md#L59-L81) documenta retención y controles, separando código de despliegue.

### C4 · Coherencia y trazabilidad (0,75)

Existen **12 secciones arc42** y C4 1–3. La [única familia A-01: cuatro escenarios](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/docs/aspectos.md#L36-L50) relaciona requisitos, C4, ADR, código y pruebas, pero no completa la medición física de ninguno y sigue describiendo el corte MP3. [C4 nivel 3](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/docs/c4/Componentes%20-%20Nivel%203.mmd) describe HTTP Range, no el relay ni los motores en vivo actuales. OpenAPI existe, revisar contrato del socket y consistencia con alcance Android. No confirmado un validador global documental.

### C5 · Aportes verificables y sustentación (1,00)

Cuatro cuentas de autor observadas en los 74 commits S10→S16. [PR #10](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/10), [#11](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/11) y [#12](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/12) ofrecen trazas de trabajos distintos; en sus hilos inspeccionados aparecieron checks automatizados, no revisión humana técnica sustantiva. No certificar correspondencia de personas ni contribución de toda la cohorte solo por recuento. Demostración y defensa: **no verificadas; las resuelve el docente**.

| Criterio | Propuesta técnica |
|---|---|
| C1 | Pendiente demo/desafío |
| C2 | Sobresaliente documental (1,00), por comparación controlada de reloj; no atribuirla al vivo físico |
| C3 | Básico (0,60) |
| C4 | Básico (0,45) |
| C5 | **Reservado al docente** |
| Total | **Pendiente** |

## Matriz transversal del contrato

| Comprobación | Resultado |
|---|---|
| Repositorio público, nombre, estructura y estado | Repositorio accesible y rama/hash verificables; las salvedades de estructura/trazabilidad están en C4. |
| ADR, convenciones y vigencia | Véanse ADR y desalineaciones en C2/C4; integridad de todo el historial de ADR aceptados no certificada. |
| Registro IA | [Presente](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/docs/ia.md); no se certifica exhaustividad de la declaración. |
| README arranque y pruebas | Documentado en [README](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/47a380ec3c4e8597a9aa6f02b19daab7a9d77faa/README.md); sin recrear entorno. |
| Pipeline y análisis estático | Resultados exactos y pasos omitidos diferenciados en C3. |
| Credenciales e historial | No verificado exhaustivamente; no se usaron credenciales ni se reportan identificadores personales. |
| Contribución y revisión cruzada | Evidencia parcial en C5; autoría no confirmada sólo mediante conteos. |

## Preguntas para sustentación

1. ¿Qué ocurre al duplicar el número de receptores en Wi-Fi? midan diferencia audible y ancho de banda, no solo timestamps.
2. Si se pierde el WebSocket o llega un paquete tarde, ¿qué ve y oye cada rol y cómo vuelve el receptor a sincronía?
3. ¿Cómo prueban cuál revisión sirve Dokploy y qué plataforma puede emitir/recibir, incluido Android, sin extrapolar un APK de CI?

**Límites:** lectura de repositorio y metadatos/pasos de CI. No ejecutamos código estudiantil, no escribimos en aplicaciones, no verificamos despliegue ni usamos credenciales. La asignación oficial del desafío, documento entregado en SAVIO y defensa quedan pendientes.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- web: [https://audioshare.iscoutb.dev/](https://audioshare.iscoutb.dev/) → HTTP 200 (13:28:09 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
