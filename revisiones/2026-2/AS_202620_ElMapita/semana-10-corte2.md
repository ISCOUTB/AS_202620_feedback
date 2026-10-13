# Segundo corte · S10 · ElMapita · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_ElMapita |
| Rama evaluada | `main` |
| Hash calificado | `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` |
| Fecha del commit | 2026-10-04T21:11:20-06:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

EC-04: mapa offline con caché

Se valora el escenario documentado disponible; no se afirma asignación docente verificada ni nueva entrega específica S10. Evidencias previas se usan como estado del repositorio, no se traslada ni promedia su nota anterior.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Competente | 0,80 / 1,00 |
| C2 · Decisión e implementación | Básico | 0,60 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Básico | 0,60 / 1,00 |
| C4 · Evolución arquitectónica trazable | Básico | 0,60 / 1,00 |
| C5 · Sustentación del reto | Calificación comunicada por el docente | 0,80 / 1,00 |

**Subtotal técnico: 2,60 / 4,00. Total consolidado C1–C5: 3,40 / 5,00.**

Calificación de sustentación comunicada por el docente: **4,00 / 5,00**, incorporada como **C5 = 0,80 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

La caracterización se apoya en un estado inicial negativo de 0/20, con control online y procedimiento. Ese resultado no se interpreta como cumplimiento del comportamiento offline. La respuesta offline y la coherencia documental siguen incompletas.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/evidencia/s9-ec04-offline-dispositivo.txt:1–31](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/evidencia/s9-ec04-offline-dispositivo.txt#L1-L31)
2. [docs/aspectos.md:3–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L3-L8)
3. [backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts:12–24](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts#L12-L24)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** Cuatro brechas concretas, una alta: autorización de escritura; además ruta de ubicación mal conectada, recuperación offline incompleta y dependencia de adaptadores concretos. Se respetó ADR5/6 vigente y no se trató Supabase Realtime pendiente como mensajería ya obligatoria.

**Arquitectura declarada:** Monolito modular NestJS/Flutter, Supabase aislado por adaptadores, RBAC JWT, caché dos niveles y ubicación con precisión/fallback; ADR5 mantiene DEC01-06.

**Arquitectura implementada:** Módulos Nest inyectan repositorios Supabase y cliente service-role; frontend auth directo permitido; Flutter Mapas usa API/cache concretos. Backend current sigue caso sin filtro; caché binaria solo tras metadatos online.

**Hallazgos materiales: 4.** Prioridad máxima: **Alta**.

<a id="deriva-d1"></a>

### D1 · La escritura de POIs anunciada como admin no atraviesa autorización

**Naturaleza:** implementación. **Prioridad:** Alta. **Confianza:** Alta sobre el código y la documentación al hash; no acredita comportamiento del despliegue..

**Motivo de prioridad:** Se trata de una frontera de seguridad en una operación de escritura con credencial de servicio, no solo de una anotación ausente.

**Declaración contrastada:**

- [docs/c4/C4_L2_Container.md:16–17](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/c4/C4_L2_Container.md#L16-L17) — C4 describe al backend como monolito REST con RBAC JWT y al cliente con caché/fallback de ubicación.
- [docs/c4/C4_L2_Container.md:41–43](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/c4/C4_L2_Container.md#L41-L43) — C4 asigna al backend validación JWT/roles, CRUD geoespacial y operaciones administrativas de almacenamiento.

**Implementación contrastada:**

- [backend/src/modules/pois/interfaces/pois.controller.ts:43–49](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/pois/interfaces/pois.controller.ts#L43-L49) — El POST descrito como Crear nuevo POI (admin) envía directamente el body al caso de uso sin guard visible.
- [backend/src/modules/pois/application/use-cases.ts:64–81](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/pois/application/use-cases.ts#L64-L81) — CreatePoiUseCase construye la entidad y llama poiRepository.save sin recibir ni comprobar identidad del solicitante.
- [backend/src/modules/pois/infrastructure/supabase-poi-repository.ts:68–84](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/pois/infrastructure/supabase-poi-repository.ts#L68-L84) — SupabasePoiRepository.save ejecuta upsert en pois y devuelve el registro obtenido.
- [backend/src/shared/supabase/client.ts:9–24](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/shared/supabase/client.ts#L9-L24) — El cliente compartido se construye con SUPABASE_SERVICE_ROLE_KEY y no persiste sesión.
- [backend/src/main.ts:7–24](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/main.ts#L7-L24) — El bootstrap configura logger, prefijo, CORS y ValidationPipe, sin registrar guard global.
- [backend/src/app.module.ts:11–23](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/app.module.ts#L11-L23) — AppModule importa módulos de features y declara providers vacío, sin guard global en este bloque.
- [backend/src/modules/pois/pois.module.ts:11–24](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/pois/pois.module.ts#L11-L24) — PoisModule inyecta SupabasePoiRepository como PoiRepository y no registra un guard en sus providers.

**Efecto y alcance:** Si la API está expuesta con la configuración prevista, el código no exige identidad/rol antes de solicitar un upsert. No se afirma explotación ni éxito contra una BD real.

**Corrección propuesta:** Añadir guard JWT validado y guard de rol admin en la entrada, pasar identidad al caso de uso y verificar 401/403 y ausencia de escritura con pruebas. Revisar también las operaciones administrativas de Auth. Swagger addBearerAuth no aplica autorización.

<a id="deriva-d2"></a>

### D2 · La ruta real de ubicación omite el caso de uso que filtra precisión y timeout

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** Alta sobre el código y la documentación al hash; no acredita comportamiento del despliegue..

**Motivo de prioridad:** Existe una política/caso validado, pero la ruta pública sigue usando el caso anterior; es un defecto de cableado verificable.

**Declaración contrastada:**

- [docs/arc42/arc42-template-EN.md:535–536](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/arc42/arc42-template-EN.md#L535-L536) — DEC04 exige recuperación offline y DEC05 rechazo de precisión superior a 15 m con fallback tras timeout.
- [docs/c4/C4_L3_Component_Backend.md:29–32](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/c4/C4_L3_Component_Backend.md#L29-L32) — C4 atribuye al servicio de Ubicación control del margen GPS y al adaptador conexión con sensores del teléfono.

**Implementación contrastada:**

- [backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts:13–24](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts#L13-L24) — UbicacionController inyecta GetCurrentLocationUseCase y lo ejecuta en GET current.
- [backend/src/modules/ubicacion/application/use-cases.ts:18–26](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/application/use-cases.ts#L18-L26) — GetCurrentLocationUseCase devuelve el resultado del proveedor sin filtro de precisión ni timeout.
- [backend/src/modules/ubicacion/ubicacion.module.ts:16–27](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/ubicacion.module.ts#L16-L27) — UbicacionModule registra ambos casos de uso, pero selecciona PlatformLocationAdapter fuera de test.
- [backend/src/modules/ubicacion/infrastructure/platform/location-adapter.ts:4–14](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/infrastructure/platform/location-adapter.ts#L4-L14) — PlatformLocationAdapter devuelve coordenadas 0,0, precisión 999 y source gps como datos fijos.
- [backend/src/modules/ubicacion/application/get-validated-location.use-case.ts:25–40](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/application/get-validated-location.use-case.ts#L25-L40) — GetValidatedLocationUseCase aplica carrera contra timeout, evalúa precisión y devuelve rechazo ante errores.

**Efecto y alcance:** GET current puede entregar la ubicación ficticia de precisión 999 m en vez del veredicto de fallback. No se atribuye ese resultado al GPS físico de Flutter.

**Corrección propuesta:** Conectar la entrada HTTP a GetValidatedLocationUseCase o retirar/etiquetar ese endpoint como simulación de servidor. Definir claramente que el GPS real vive en el móvil; añadir prueba de integración router→provider impreciso/timeout.

<a id="deriva-d3"></a>

### D3 · La recuperación offline documentada queda detrás de una llamada de red obligatoria

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** Alta sobre el código y la documentación al hash; no acredita comportamiento del despliegue..

**Motivo de prioridad:** La caché binaria existe, pero el orden de llamadas impide alcanzarla cuando falla la consulta de metadatos.

**Declaración contrastada:**

- [docs/arc42/arc42-template-EN.md:465–472](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/arc42/arc42-template-EN.md#L465-L472) — arc42 describe recuperar escena de caché, emitir MapLoadedOffline y mostrar mapa utilizable sin conexión.
- [docs/c4/C4_L2_Container.md:64–66](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/c4/C4_L2_Container.md#L64-L66) — C4 afirma desacoplo Supabase y recuperación offline mediante Hive/Filesystem versionados.

**Implementación contrastada:**

- [frontend/lib/features/mapas/application/load_building_use_case.dart:18–37](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/frontend/lib/features/mapas/application/load_building_use_case.dart#L18-L37) — LoadBuildingUseCase retorna Left cuando falla la API antes de llamar getOrDownloadModel.
- [frontend/lib/features/mapas/infrastructure/storage/model_cache.dart:21–33](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/frontend/lib/features/mapas/infrastructure/storage/model_cache.dart#L21-L33) — ModelCache reutiliza la ruta almacenada o descarga el modelo si no está en caché.
- [frontend/lib/core/di/injector.dart:46–55](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/frontend/lib/core/di/injector.dart#L46-L55) — DI conecta MapasApi y ModelCache concretos con LoadBuildingUseCase y este con MapasBloc.

**Efecto y alcance:** LoadBuildingUseCase retorna error antes de consultar ModelCache ante fallo de API, por lo que una caché caliente no basta para el modo offline descrito.

**Corrección propuesta:** Persistir metadatos/versiones junto al binario y resolverlos desde caché al fallar la red; emitir estado offline explícito y probar caché válida sin backend. La evidencia S9 ya caracteriza la carencia; no se vende como una regresión nueva.

<a id="deriva-d4"></a>

### D4 · LoadBuildingUseCase depende de adaptadores concretos pese a la regla de interfaces

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** Alta sobre el código y la documentación al hash; no acredita comportamiento del despliegue..

**Motivo de prioridad:** ADR5 mantiene la regla de aplicación dependiente de interfaces; no se exige pureza hexagonal genérica.

**Declaración contrastada:**

- [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:19–28](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L19-L28) — ADR5 mantiene las decisiones DEC01-06 y remite al contenido de ADR1 con referencias actualizadas.
- [docs/adr/0001-estilo-arquitectonico-propuesto.md:133–140](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0001-estilo-arquitectonico-propuesto.md#L133-L140) — La regla de límites exige application dependiente de dominio e interfaces, no implementaciones concretas.

**Implementación contrastada:**

- [frontend/lib/features/mapas/application/load_building_use_case.dart:3–16](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/frontend/lib/features/mapas/application/load_building_use_case.dart#L3-L16) — LoadBuildingUseCase importa MapasApi y ModelCache concretos y los exige como tipos de constructor.
- [frontend/lib/core/di/injector.dart:46–52](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/frontend/lib/core/di/injector.dart#L46-L52) — DI registra MapasApi/ModelCache e inyecta ambas implementaciones directamente en el caso de uso.

**Efecto y alcance:** Cambiar API/cache puede requerir editar el caso de uso y sus pruebas en lugar de sustituir implementaciones detrás de puertos.

**Corrección propuesta:** Definir puertos de consulta de edificios y caché en dominio/aplicación; inyectar implementaciones MapasApi y ModelCache desde DI. Alternativamente aprobar y documentar el acoplamiento pragmático, sin seguir afirmando solo interfaces.

### Cobertura y límites de la auditoría

**Capas y dominio:** Mapas backend usa tokens de repositorio; aplicación Flutter depende de adaptadores concretos. No se calificó uso de Nest en aplicación por sí solo como erosión.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/src/modules/mapas/mapas.module.ts:18–35](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/mapas/mapas.module.ts#L18-L35) — MapasModule vincula los tokens BuildingRepository, FloorRepository y Model3DStorage a adaptadores Supabase.
- [backend/src/modules/mapas/application/use-cases.ts:28–51](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/mapas/application/use-cases.ts#L28-L51) — GetBuildingUseCase recibe repositorios por tokens, consulta edificio/pisos y solicita una URL firmada.
- [frontend/lib/features/mapas/application/load_building_use_case.dart:3–16](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/frontend/lib/features/mapas/application/load_building_use_case.dart#L3-L16) — LoadBuildingUseCase importa MapasApi y ModelCache concretos y los exige como tipos de constructor.

**Persistencia:** Supabase repositorios y storage tras DI; Hive/archivo de modelos en frontend. Upsert de POIs rastreado.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/src/modules/pois/infrastructure/supabase-poi-repository.ts:68–84](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/pois/infrastructure/supabase-poi-repository.ts#L68-L84) — SupabasePoiRepository.save ejecuta upsert en pois y devuelve el registro obtenido.
- [frontend/lib/features/mapas/infrastructure/storage/model_cache.dart:41–61](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/frontend/lib/features/mapas/infrastructure/storage/model_cache.dart#L41-L61) — ModelCache descarga el binario a un archivo versionado y registra su ruta en almacenamiento local.

**API y autorización:** Contrato REST y bootstrap; búsqueda de guards en backend/src y revisión main/AppModule/PoisModule no muestran aplicación de guard a POST POIs. Auth frontend directa está permitida por C4.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/src/main.ts:7–36](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/main.ts#L7-L36) — El bootstrap instala logger, CORS y validación global; addBearerAuth configura Swagger, sin aplicar un guard.
- [backend/src/app.module.ts:11–23](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/app.module.ts#L11-L23) — AppModule importa módulos de features y declara providers vacío, sin guard global en este bloque.
- [docs/c4/C4_L2_Container.md:33–41](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/c4/C4_L2_Container.md#L33-L41) — C4 permite autenticación directa opcional con Supabase y dibuja llamadas REST/Realtime del cliente.
- [frontend/lib/features/auth/infrastructure/supabase_auth_client.dart:15–21](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/frontend/lib/features/auth/infrastructure/supabase_auth_client.dart#L15-L21) — El adaptador Flutter de auth llama signInWithPassword directamente mediante Supabase SDK.

**Despliegue:** Render Docker con health y variables de entorno; no se comprobó estado remoto ni credenciales.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [render.yaml:10–30](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/render.yaml#L10-L30) — render.yaml define un servicio Docker con /health y variables de Supabase inyectadas por el entorno.

**Asincronía:** REST, promesas de I/O y timeout de ubicación; Realtime declarado deuda en decisión de contrato, no se considera incumplimiento de broker.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [docs/arc42/arc42-template-EN.md:538–539](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/arc42/arc42-template-EN.md#L538-L539) — arc42 declara Realtime como deuda, REST como integración actual y Render con logs/métricas como despliegue elegido.
- [backend/src/modules/ubicacion/application/get-validated-location.use-case.ts:25–40](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/application/get-validated-location.use-case.ts#L25-L40) — GetValidatedLocationUseCase aplica carrera contra timeout, evalúa precisión y devuelve rechazo ante errores.

**Observabilidad:** Interceptor de histograma registra éxitos y excepciones; main instala logger. No se midieron p95 ni FPS.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/src/shared/observability/http-metrics.interceptor.ts:31–49](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/shared/observability/http-metrics.interceptor.ts#L31-L49) — El interceptor observa duración/status tanto en respuestas satisfactorias como en excepciones.
- [backend/src/main.ts:7–9](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/main.ts#L7-L9) — NestFactory crea AppModule y conecta el logger de la aplicación.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:45:53.951346+00:00 confirmó el hash anterior como último commit de `main` antes del límite exclusivo. La punta observada es [`f3bcfa83e80f5c8d0e30a01b656d89160c907d64`](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/f3bcfa83e80f5c8d0e30a01b656d89160c907d64) (2026-10-04T21:11:20-06:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Segundo corte S10 · avance preliminar · ElMapita

**Preliminar, no es cierre ni calificación final.** Cierre previsto: **2026-10-12T05:00:00Z**.

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_ElMapita](https://github.com/ISCOUTB/AS_202620_ElMapita) |
| Rama remota principal | `main` |
| Base S5 del segundo corte | `b28e0684d4b38267c0a7d48152b0f5558a789b8c` |
| Base S8 | `e5c3ac6ecb598c8e126aaa091cce9af01fe818c4` |
| Estado revisado | `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` en `origin/main` (2026-10-04T21:11:20-06:00) |
| S9 congelada | `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` · 2026-10-04T21:11:20-06:00 |
| Punta actual / S10 preliminar | `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` · 2026-10-04T21:11:20-06:00 |
| Comprobación | 2026-10-06T21:27:01Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Evolución desde S5 hasta la punta

Base tomada del informe S5 publicado y resuelta por Git, sin etiquetas: `b28e0684d4b38267c0a7d48152b0f5558a789b8c`. En el delta S5→HEAD cambian 87 rutas no PDF (conteo de árboles; no mide mérito). Desde S5 se incorporan contrato API comprobable, despliegue Render y observabilidad, correcciones de inyección/rutas y la porción de ubicación de S9 con sus pruebas, mediciones y ADR sustitutos. Los escenarios fallidos siguen abiertos; la evolución no se confunde con cumplimiento del reto asignado.

## Escenario operativo asignado

No verificado. README, ADR, IA, aspectos y evidencias documentan EC-01..04, pero no contienen la asignación docente del escenario operativo S10. No se toma el plan S9 ni los escenarios genéricos como consigna del segundo corte.

## Matriz de evidencia S10

Se omite la fila de PDF de dos páginas por exclusión docente. Quedan 12 filas observables o pendientes; este recuento no es una fórmula de nota.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta main identificada, anterior al cierre S10; preliminar. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://elmapita-utb-api.onrender.com/health iniciado 2026-10-06T21:27:01Z: HTTP 200 en 19.699114 s, JSON status=ok y checks.supabase=ok. Health disponible; no se ejecutó el flujo de mapa/GPS ni se prueba disponibilidad sostenida. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | EC-01..04 son objetivos generales del producto; no se localizó asignación oficial S10; [docs/aspectos.md:3–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L3-L8). |
| Línea base medida y reproducible | No verificado | Hay mediciones identificadas y reproducibles de EC-01 y offline, pero sin conocer el escenario asignado no se las adopta como línea base del corte; [docs/evidencia/s9-ec01-benchmark.json:1–15](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/evidencia/s9-ec01-benchmark.json#L1-L15), [docs/evidencia/s9-ec04-offline-dispositivo.txt:1–31](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/evidencia/s9-ec04-offline-dispositivo.txt#L1-L31). |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | ADR-0005/0006 y ADR-0007 son decisiones justificadas; falta identificar la respuesta al escenario operativo asignado. [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:19–33](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L19-L33). |
| Respuesta implementada o configurada sobre el MVP | No verificado | Hay validador, corrección de error 500 y arneses, pero el validador no es llamado por el controlador; tampoco se identifica el cambio del reto asignado. [backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts:12–24](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts#L12-L24), [backend/src/modules/ubicacion/ubicacion.module.ts:15–35](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/ubicacion.module.ts#L15-L35). |
| Resultado contrastado con el umbral | No verificado | Resultados francos: EC-01 sin éxito, EC-02 solo placeholder, EC-04 0/20. Son evidencia útil, no cumplimiento del reto S10 aún desconocido; [docs/ia.md:464–469](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L464-L469). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | Health y métricas existen, pero el gate ignora fallo de Sonar y la operación crítica de mapas/offline no satisface escenarios declarados; [.github/workflows/ci.yml:297–313](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/.github/workflows/ci.yml#L297-L313), [docs/aspectos.md:5–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L5-L8). Métrica vinculada al escenario asignado no verificada. |
| Secretos protegidos | Cumple | No se encontraron secretos reales en snapshot. No se equipara un identificador público projectKey con credencial. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | Parte documental avanza con ADR sustitutos, pero aspectos conserva rutas antiguas y el validador no está en el flujo del controlador. El modelo/operación completa aún no representa lo prometido en escenarios; [docs/aspectos.md:5–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L5-L8), [backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts:12–24](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts#L12-L24). |
| Decisión anterior confirmada o reemplazada con evidencia | Cumple | ADR-0005 confirma DEC-01..06 y ADR-0006 reemplaza estado de RSK-04 con evidencias de contrato/DI; [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:19–33](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L19-L33), [docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md:17–26](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md#L17-L26). Se acredita la sustitución trazable concreta, sin atribuirle el reto S10. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Pendiente de sustentación con entorno desplegado y pipeline en vivo. |

## Rúbrica específica de cinco criterios

| Criterio | Nivel sugerido | Puntaje | Fundamento |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | No se localizó evidencia de asignación oficial del escenario; no se sustituye por un escenario genérico. |
| Decisión e implementación | No verificado | Pendiente | No se puede juzgar la respuesta al escenario asignado hasta identificarlo. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Hay evidencia técnica parcial descrita en la matriz; falta vincularla con el escenario asignado y verificar la operación completa. |
| Evolución arquitectónica trazable | No verificado | Pendiente | La coherencia documental se informa en la matriz; falta demostrar la evolución específica exigida por el reto. |
| Sustentación del reto | Pendiente del docente | Pendiente | Sustentación sobre el entorno desplegado y pipeline en vivo; no se puntúa desde el repositorio. |

Escala aplicable: 0,00 / 0,60 / 0,80 / 1,00 por criterio. **No se calcula total mientras haya criterios pendientes.** No se usa la fórmula semanal. Cualquier nivel es propuesta al docente; la sustentación queda a su cargo.

## Matriz transversal · punta actual

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Repositorio público ISCOUTB/AS_202620_ElMapita, rama main; [README.md:1–7](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/README.md#L1-L7). |
| Estructura mínima presente | Cumple | README, arc42 en plantilla única, ADR, C4, aspectos e IA presentes; [docs/aspectos.md:1–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L1-L8). |
| Estado calificado identificable | Cumple | Hash main congelado y fecha en encabezado; coincide con punta actual. |
| Nombres de ADR según la convención | Cumple | ADR-0001 a 0007 usan NNNN-kebab-case; [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:1–11](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L1-L11). |
| ADR aceptados no reescritos | Cumple | Se verificó diff de ADR-0001 contra aa16382 y ADR-0003 contra afae3be: únicamente cambia status a Superseded. Los cambios viven en ADR-0005/0006; [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:13–33](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L13-L33), [docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md:13–26](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md#L13-L26). Arrastre corregido, sin borrar que ocurrió históricamente. |
| docs/ia.md al día para la semana | Cumple | Entradas S9 distinguen aceptado, corregido y rechazos técnicos, incluidas mediciones falsas y pruebas que no representan producto; [docs/ia.md:395–419](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L395-L419), [docs/ia.md:452–469](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L452-L469). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | Workflow CI general success, pero Sonar es no bloqueante y está excluido del fallo del gate; [.github/workflows/ci.yml:254–283](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/.github/workflows/ci.yml#L254-L283), [.github/workflows/ci.yml:297–313](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/.github/workflows/ci.yml#L297-L313). El equipo documenta fallo por permisos, [docs/ia.md:434–439](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L434-L439); no se acredita análisis/Gate ejecutado. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Snapshot sin valores de credencial reales. Gitleaks excluye fingerprints de ejemplos y projectKey públicos; historial completo independiente no certificado. |
| Contribución de todos los integrantes | No verificado | Cuatro firmas visibles tras .mailmap: 40 commits agregados. La correspondencia RobotDRMX con integrante queda explícita en .mailmap, pero no se inventa un mapa completo del resto; [docs/ia.md:397–402](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L397-L402). Punta actual: 4 firmas y 40 commits agregados; no equivalen automáticamente a personas. |

## Actions en la punta actual

- [CI: success](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/37258414405), 2026-10-05T03:11:23Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Se revisó el texto del snapshot, incluidos ejemplos/docs. Las coincidencias corresponden a interfaces password/token, variables de entorno, fixtures y referencias al almacén de Actions. No hay .env versionado. Las exclusiones de gitleaks para projectKey/documentación deben seguir justificadas; no se certifica el historial exhaustivo independiente.

## Estado global del proyecto (overall)

El avance S9 es sustantivo y honesto sobre sus límites: nuevo validador, rojo→verde documentado, corrección 500→404, pruebas en dispositivo y ADR sustitutos. La medición descubre defectos reales, no demuestra éxito del producto: EC-04 falla 20/20 y el rendimiento de un placeholder no representa render 3D. El validador está registrado pero el controlador sigue usando el caso de uso anterior. La punta coincide con S9, y SonarCloud está no bloqueante pese al CI general verde.

El delta S9 contiene 9 commits respecto de S8; hay 0 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Antes del cierre

- Integrar GetValidatedLocationUseCase en el recorrido real y medir el fallback de Flutter; no basta registrarlo como provider.
- Completar enlaces de código/pruebas/medición y actualizar EC-03 hacia los archivos nuevos.
- Corregir acceso a modelo/edificio, repetir EC-01 con respuestas exitosas y medir render 3D real; implementar caché de datos y banner offline antes de cerrar EC-04.
- Resolver permiso de análisis SonarCloud con quien administra la organización; retirar continue-on-error solo cuando exista run/Gate verificable.
- Aportar consigna oficial S10 y conectar hipótesis, línea base, cambio y experimento con esa asignación.

## Tres preguntas de sustentación

1. ¿Qué recibe hoy el usuario si GPS entrega 999 m y por qué el controlador no llama al validador nuevo?
2. ¿Qué costo de almacenamiento/egreso tendría descargar modelos sin caché y qué supuesto cambia al habilitar modo offline real?
3. Las pruebas detectaron HTTP500 y 0/20 offline: ¿qué cambiarían primero y cómo evitarían medir un placeholder como si fuera el mapa3D?

</details>
