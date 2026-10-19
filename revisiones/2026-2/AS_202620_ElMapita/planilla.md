# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | ElMapita |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Angel Fabian Gutierrez Gomez (sin cuenta identificada en el historial) · Diego Rosales Garza (sin cuenta identificada) · Rodrigo Vazquez Rico (firma con su nombre). Historial: `RobotDRMX` (sin atribuir) y, en EQUIPOS.md, `YOOUYII` (nunca vista).; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://elmapita-utb-api.onrender.com · ver comprobación y límites en S10 |
| Última revisión | 2026-10-19 · S11 definitiva y S12 preliminar (observación 21:35 UTC); rectificaciones aprobadas sincronizadas |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 12 | [S12 · preliminar](semana-12-evidencia-s12.md) | `main` · `0421885424d13478cf33c717fdd933a4748d9025` | 3/9 | 2.3 (propuesta al docente; preliminar) | sí, 2026-10-19 |
| 11 | [S11 · definitiva](semana-11-evidencia-s11.md) | `main` · `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` | 2/9 | 1.9 (propuesta al docente) | sí, 2026-10-19 |
| 9 | S9 · definitiva | `main` · `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` · 2026-10-04T21:11:20-06:00 | 9/10 | 4.6 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · consolidado al cierre | `main` · `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` · 2026-10-04T21:11:20-06:00 | C1 0,80; C2 0,60; C3 0,60; C4 0,60 (cada uno /1) | Total 3,40/5; técnica 2,60/4 + C5 docente 0,80/1; ver [S10](semana-10-corte2.md) | sí, 2026-10-13 |
| 8 | S8 | `e5c3ac6` (2026-09-27T16:26:27-06:00) | 9/10 (2 filas de despliegue diferidas) | 4.6 (provisional) | si |
| 6 | S6 | `a22f0a4` (2026-09-13T22:21:07-05:00) | 0/8 | 1.0 (prelim.) | si |
| 7 | S7 | `afae3be` (2026-09-20T19:09:25-06:00) | 8/10 | 4.2 | si |
| 5 | CORTE1 | `b28e068` (2026-09-07T14:57:28-06:00) | 7/12 | 3.3 | si |
| 4 | S4 | `07b36f4` (2026-08-30T23:31:03-05:00) | 4/10 | 2.6 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `938d0206` · 2026-08-07T21:36:01-06:00 | 5/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `c5d9964c` · 2026-08-16T14:21:20-05:00 | 8/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `8e30f616` · 2026-08-22T16:12:55-06:00 | 4/9 | no se publica | sí |

## Seguimiento vigente · S11 y avance S12 · 19 de octubre de 2026

S11 se fija antes del límite exclusivo 2026-10-19T05:00:00Z. S12 es preliminar, observada a las 21:35 UTC del 19 de octubre, y cierra el 26 de octubre a las 05:00 UTC. Las matrices transversales actuales están en [S11](semana-11-evidencia-s11.md) y [S12](semana-12-evidencia-s12.md). Sus estados y límites sustituyen las inferencias de arrastre que no hayan sido revalidadas; el historial conserva su fecha.

Dos commits posteriores al cierre: `d77eb7132df6e9dc33001686d47fb50babdc405f` (2026-10-19T08:24:11Z) y `0421885424d13478cf33c717fdd933a4748d9025` (08:33:59Z). El segundo incorpora ADR-0008 con criterios y alternativa no extraer (`docs/adr/0008-decision-extraccion.md:18-41`), tabla de fallos y argumento sobre sagas (`arc42-template-EN.md:664-679`) y enlace en aspectos (`:45-47`); no cambia S11 histórica. Incluso ahora la tabla no incluye explícitamente respuesta duplicada, y el argumento de escrituras futuras debe reconciliarse con registro/cambio de rol existentes (`backend/src/modules/auth/application/use-cases.ts:48-68,145-157`).

Erosión arquitectónica: arc42 describe recuperación offline y caché de metadatos, pero `load_building_use_case.dart:18-23` exige primero la API y `model_cache.dart:69-75` no invalida. `docs/aspectos.md:5-8` reconoce medición HTTP 500, visualización placeholder y 0/20 offline; esos resultados previos no se presentan como nuevas pruebas de esta revisión. Se preservan los límites de módulos del backend, mientras el caso de uso Flutter importa adaptadores concretos (`load_building_use_case.dart:5-16`), divergencia respecto al desacoplo proclamado. CI verde no demuestra todo: pruebas Flutter/E2E y Sonar pueden no bloquear (`.github/workflows/ci.yml:68-74,189-211,253-260,297-309`).

Actividad en principal: 0 commits en la ventana S11 y 2 posteriores al cierre hasta la observación. El número de commits no determina la nota: se contrasta el contenido completo con la ficha.

| Seguimiento | Estado y evidencia |
|---|---|
| Integración, modos de fallo y extracción | [Matriz S11](semana-11-evidencia-s11.md): distingue diseño, código y pendientes explícitos. |
| Consistencia, caché y reversibilidad | [Matriz S12 preliminar](semana-12-evidencia-s12.md): completar los criterios pendientes antes del cierre. |
| CI, seguridad, contribución y decisiones inmutables | Revisar la matriz transversal del informe actual; no se cierran por un CI verde genérico ni por la existencia de archivos. |

## Feedback S10 vigente · 13 de octubre de 2026

Límite exclusivo: **2026-10-13T05:00:00Z**, fin del 12 de octubre en Colombia. Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

**Subtotal técnico: 2,60 / 4,00. Total consolidado C1–C5: 3,40 / 5,00.**

Calificación de sustentación comunicada por el docente: **4,00 / 5,00**, incorporada como **C5 = 0,80 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

La caracterización se apoya en un estado inicial negativo de 0/20, con control online y procedimiento. Ese resultado no se interpreta como cumplimiento del comportamiento offline. La respuesta offline y la coherencia documental siguen incompletas.

Fuentes y alcance completos: [informe S10](semana-10-corte2.md#fundamento-técnico-y-comentarios-vigentes). Las referencias de identidad, contribución y despliegue heredadas conservan sus fechas originales; no constituyen una nueva verificación en esta consolidación.

### Deriva arquitectónica al cierre S10

Escritura sin autorización; ubicación, caché offline y dependencias divergentes.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Alta · La escritura de POIs anunciada como admin no atraviesa autorización:** Si la API está expuesta con la configuración prevista, el código no exige identidad/rol antes de solicitar un upsert. No se afirma explotación ni éxito contra una BD real. **Acción:** Añadir guard JWT validado y guard de rol admin en la entrada, pasar identidad al caso de uso y verificar 401/403 y ausencia de escritura con pruebas. Revisar también las operaciones administrativas de Auth. Swagger addBearerAuth no aplica autorización. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · La ruta real de ubicación omite el caso de uso que filtra precisión y timeout:** GET current puede entregar la ubicación ficticia de precisión 999 m en vez del veredicto de fallback. No se atribuye ese resultado al GPS físico de Flutter. **Acción:** Conectar la entrada HTTP a GetValidatedLocationUseCase o retirar/etiquetar ese endpoint como simulación de servidor. Definir claramente que el GPS real vive en el móvil; añadir prueba de integración router→provider impreciso/timeout. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).
- **Media · La recuperación offline documentada queda detrás de una llamada de red obligatoria:** LoadBuildingUseCase retorna error antes de consultar ModelCache ante fallo de API, por lo que una caché caliente no basta para el modo offline descrito. **Acción:** Persistir metadatos/versiones junto al binario y resolverlos desde caché al fallar la red; emitir estado offline explícito y probar caché válida sin backend. La evidencia S9 ya caracteriza la carencia; no se vende como una regresión nueva. [Contraste y evidencia](semana-10-corte2.md#deriva-d3).
- **Media · LoadBuildingUseCase depende de adaptadores concretos pese a la regla de interfaces:** Cambiar API/cache puede requerir editar el caso de uso y sus pruebas en lugar de sustituir implementaciones detrás de puertos. **Acción:** Definir puertos de consulta de edificios y caché en dominio/aplicación; inyectar implementaciones MapasApi y ModelCache desde DI. Alternativamente aprobar y documentar el acoplamiento pragmático, sin seguir afirmando solo interfaces. [Contraste y evidencia](semana-10-corte2.md#deriva-d4).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Seguimiento anterior a la consolidación S10; estados históricos superados</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Integrar GetValidatedLocationUseCase en el recorrido real y medir el fallback de Flutter; no basta registrarlo como provider. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar enlaces de código/pruebas/medición y actualizar EC-03 hacia los archivos nuevos. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Corregir acceso a modelo/edificio, repetir EC-01 con respuestas exitosas y medir render 3D real; implementar caché de datos y banner offline antes de cerrar EC-04. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Resolver permiso de análisis SonarCloud con quien administra la organización; retirar continue-on-error solo cuando exista run/Gate verificable. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Aportar consigna oficial S10 y conectar hipótesis, línea base, cambio y experimento con esa asignación. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Arrastre de reescritura de ADR-0001/0003 corregido: restaurados textos aceptados y sustitución explícita por 0005/0006, comprobada por diff. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Se corrige la anterior falta de atribución de RobotDRMX mediante .mailmap explícito; no corresponde mantener afirmación de cero contribuciones de esa persona. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Existen porción S9, prueba negativa, auditoría y ADR de no incorporar IA generativa; [docs/ia.md:395–419](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L395-L419). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| El error genérico al faltar un modelo se convierte en NotFoundException y tiene prueba; [backend/src/modules/mapas/infrastructure/storage/supabase-storage.ts:22–30](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/mapas/infrastructure/storage/supabase-storage.ts#L22-L30). No se afirma recuperación operativa sin re-medición. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/ia.md` vacío (0 bytes) en S1 | S1 | no (resuelto: tiene contenido desde 2026-08-30 y crece hasta 2026-09-20) | Ver feedback S1/S2 y S3 |
| Sin ficha del problema | S1 | sí | Ver feedback S1/S2 |
| Sin tensiones de calidad | S1 | sí | Ver feedback S1/S2 |
| Historial con cuentas sin atribuir (2 identidades para 3 integrantes; en S3 solo una cuenta firma) | S1 | sí | Ver feedback S1/S2 y S3 |
| Sección 4 de arc42 vacía (la estrategia está en ADR y matriz, no en arc42) | S3 | sí | Ver feedback S3 |
| ADR no enlazado desde `aspectos.md` ni desde los escenarios | S3 | sí | Ver feedback S3 |
| Sin pipeline (pruebas sin evidencia de verde) | S3 | sí | Ver feedback S3 |
| Run de CI en failure (33357590091) | S4 | si | |
| Pruebas del recorrido completo pendientes y rutas inexistentes en aspectos.md | S4 | si | |
| Sin SonarCloud configurado | S4 | si | |
| Autoría concentrada en una cuenta (9/11 commits) | S4 | si | |
| ADR del reto | S5 | sí | Único ADR sigue siendo el de estilo arquitectónico de la línea base; sin actividad en el repositorio desde el 2026-09-01. |
| Línea base medida y verificable | S5 | sí | Las 4 filas de `docs/aspectos.md` siguen con Evidencia = "Pendiente". |
| Cadena de trazabilidad completa en docs/aspectos.md | S5 | sí | Se rompe sistemáticamente en Pruebas y Evidencia. |
| Prueba en verde en pipeline | S5 | sí (empeoró: confirmado en rojo) | Los 3 runs de CI disponibles, incluido el del commit calificado, están en `failure`. |
| Medición reproducible contra umbral | S5 | sí | Sin ejecutar. |
| Registro de IA con motivo técnico verificable | S5 | no (resuelto: el registro crece hasta 2026-09-20 y documenta rechazos con su motivo) | El informe S7 leyó el registro: descarte de Mermaid/.svg, no elección de Hexagonal y OpenAPI sobre AsyncAPI, cada uno con su motivo. |
| Confirmar etiqueta corte-1 | S5 | sí (se usó un commit con ese mensaje, no una etiqueta) | Se les explicó la diferencia entre `git commit -m "corte-1"` y `git tag corte-1`; deben crear la etiqueta real. |
| Angel Fabian Gutierrez Gomez sin commits identificables | S5 | sí | Confirmado en el commit calificado: `git shortlog` solo muestra RobotDRMX, Rodrigo Vazquez Rico y dgarza2705 (Diego Rosales Garza, ahora identificado por su correo institucional). |
| correcciones.md se añadió en el commit b28e068 (2026-09-07T14:57:28-06:00), posterior al cierre; no se considera en la matriz S5. | S5 | no (resuelto tarde) | — |
| correcciones.md en la raíz del estado calificado. | S5 | si | |
| Evidencia de ejecución del pipeline CI para el hash calificado. | S5 | si | |
| Verificación de reproducibilidad del corte vertical. | S5 | si | |
| Pruebas de EC-01 a EC-04 pendientes | S5 | si | |
| Implementación de LOD y degradación progresiva (ADR-0002) | S5 | si | |
| Verificación de pipeline y CI | S5 | si | |
| Correcciones.md sin contrastar | S5 | si | |
| Contrato OpenAPI/AsyncAPI/proto versionado, con rutas, esquemas y versión | S7 | no (resuelto) | Contrato 3.1 con rutas y components.schemas releído. |
| Prueba de contrato presente y ejecutada desde el workflow | S7 | no (resuelto) | El job `contract` ejecuta `npm run test:contracts`. |
| Evidencia de que la prueba falla ante un cambio incompatible | S7 | sí | Sin run en rojo ni registro del cambio introducido. |
| ADR de estrategia de integración síncrona o asíncrona con alternativa descartada | S7 | no (resuelto) | ADR-0003 descarta AsyncAPI frente a OpenAPI 3.1. |
| arc42 sección 6 con los flujos de interacción | S7 | no (resuelto) | Cuatro escenarios con diagrama y pasos. |
| C4 nivel 2 con protocolo y formato en cada flecha | S7 | no (resuelto) | Relaciones etiquetadas con protocolo y formato. |
| Contenido defendible de docs/aspectos.md y docs/ia.md | S7 | sí (parcial) | `aspectos.md` releído con las ocho columnas; sus celdas Pruebas/Evidencia siguen "Pendiente". `docs/ia.md` se leyó y documenta los rechazos con su motivo. |
| Runs de CI y análisis público de SonarCloud con estado del Quality Gate | S7 | sí | Sin SonarCloud en el repositorio: fila transversal en No cumple. |
| Mapa de contextos con relaciones tipificadas en formato revisable. | S6 | si | |
| Tabla módulo a datos con dueño único y su contraste con las entidades del código. | S6 | si | |
| Lista de no conformidades de propiedad de datos con ubicación y plan de corrección. | S6 | si | |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos. | S6 | si | |
| ADR de reajuste y diff de C4 Nivel 3 si los límites cambiaron desde el primer corte. | S6 | si | |
| Evidencia de SonarCloud: configuración, run de CI y URL pública con Quality Gate. | S6 | si | |
| Sin envíos posteriores al cierre: commits_post_cierre vacío y el commit calificado afae3be es anterior al cierre. | S7 | no (resuelto tarde) | — |
| Brecha de `npm run test:contracts` prometida en ADR-0001 y nunca implementada: se cierra en afae3be con el ADR-0003, dentro del plazo de S7 pero aún sin evidencia de ejecución en CI. | S7 | no (resuelto tarde) | — |
| Deriva de rutas contrato-backend por prefijo duplicado (`/api/api/v1/...`), reconocida en ADR-0003 y no corregida. | S7 | si | |
| Evidencia de que la prueba de contrato se ejecuta en el pipeline y de que falla ante un cambio incompatible. | S7 | sí (parcial) | Ejecución demostrada en `ci.yml`; el fallo controlado sigue sin evidencia. |
| Evidencia de SonarCloud (configuración del scanner, run exitoso y URL pública con Quality Gate), pendiente desde S6. | S7 | sí | Sin SonarCloud en el repositorio. |
| Contenido verificable de la tabla de aspectos, de arc42 §6 y del C4 nivel 2 con protocolo y formato. | S7 | no (resuelto) | Los tres artefactos releídos y conformes; quedan celdas Pruebas/Evidencia pendientes en `aspectos.md`. |
| Implementación pendiente declarada en ADR-0002 (LOD y degradación progresiva). | S7 | si | |
| URL desplegada con hora de comprobación | S8 | si | |
| Health check con código de respuesta | S8 | si | |
| Infraestructura como código versionada | S8 | si | |
| Run de CI en verde con URL | S8 | si | |
| Logs estructurados | S8 | si | |
| Métrica ligada a escenario | S8 | si | |
| Estimación de costo mensual y punto de ruptura | S8 | si | |
| arc42 secciones 7 y 2 | S8 | si | |
| ADR por decisión de plataforma | S8 | si | |
| Sin commits de S9: la punta es la de S8 (`e5c3ac6`, 2026-09-27). | S9 | sí | La pasada S9 no tiene cierre y califica la punta actual; el equipo no ha empujado trabajo nuevo. |
| Recalce S9 por CONTRATO §12: sin artefacto del periodo, las filas de porción con IA, cadena, ADR y extracto de `docs/ia.md` pasan a No cumple, y la de prueba que falla ante el defecto a No verificado. | S9 | sí | Solo el barrido de credenciales queda en Cumple; la evidencia de S3/S7/S8 se cita como contexto pero no se recalifica. |
| `docs/aspectos.md` con Pruebas «(pendiente)» y Evidencia «Pendiente» (EC-01…EC-04). | S4/S9 | sí | La cadena no llega a prueba ni a medición. |
| Sin medición contra umbral de ningún escenario. | S5/S9 | sí | — |
| Sin auditoría de erosión ni verificación de propiedad de datos. | S9 | sí | Fila de la ficha en No cumple. |
| Sin verificación de dependencias del periodo (diff vacío contra S8). | S9 | sí | — |
| Sin ADR sobre el componente generativo (ni componente, ni decisión de no incorporarlo). | S9 | sí | La ausencia de decisión no es la decisión de no hacerlo. |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
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

## Contribución por integrante

Actualización agregada del 2026-10-06: 40 commits y cuatro firmas tras aplicar .mailmap. La atribución de RobotDRMX está declarada explícitamente y corrige el arrastre de autoría ausente; la consolidación completa de las otras variantes queda pendiente. En HEAD: 4 firmas y 40 commits agregados.

La atribución histórica de RobotDRMX como no identificado quedó superada por la .mailmap citada en la revisión actual; la fila de 0 (S3) no describe su contribución vigente. La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Angel Fabian Gutierrez Gomez | sin cuenta identificada | 0 (S3) | — | — | `RobotDRMX` sin atribuir (¿es él o Diego Rosales Garza?) |
| Diego Rosales Garza | `dgarza2705` (correo institucional, confirmado en el corte 1) | 1 (corte 1) | — | — | Único commit del periodo: actualización de C4/arc42/pipeline. |
| Rodrigo Vazquez Rico | firma con su nombre | 0 (S3) | — | — | último commit en S2 |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- ¿Qué recibe hoy el usuario si GPS entrega 999 m y por qué el controlador no llama al validador nuevo?
- ¿Qué costo de almacenamiento/egreso tendría descargar modelos sin caché y qué supuesto cambia al habilitar modo offline real?
- Las pruebas detectaron HTTP500 y 0/20 offline: ¿qué cambiarían primero y cómo evitarían medir un placeholder como si fuera el mapa3D?

</details>
