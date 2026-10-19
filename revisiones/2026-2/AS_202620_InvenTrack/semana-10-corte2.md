# Segundo corte · S10 · InvenTrack · consolidación al cierre

**Actualización del feedback: 19 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_InvenTrack |
| Rama evaluada | `main` |
| Hash calificado | `539840be57f8a0b719bb33e19d05031489a25b86` |
| Fecha del commit | 2026-10-11T23:05:35-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

Concurrencia sobre inventario:20 peticiones sobreSKU,stock100→80,p95≤400 ms, reporteS10 autodeclarado

Se evalúa técnicamente el escenario declarado; no se afirma asignación docente verificada.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Básico | 0,60 / 1,00 |
| C2 · Decisión e implementación | Competente | 0,80 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Competente | 0,80 / 1,00 |
| C4 · Evolución arquitectónica trazable | Básico | 0,60 / 1,00 |
| C5 · Sustentación del reto | Calificación docente: 4,00 / 5,00 | 0,80 / 1,00 |

**Subtotal técnico: 2,80 / 4,00. C5 docente: 0,80 / 1,00. Total S10: 3,60 / 5,00.**

C5 incorpora la calificación de sustentación 4,00 / 5,00 indicada por el docente el 18 de octubre de 2026 y sincronizada en esta publicación. Su aporte es 4,00 / 5 = 0,80. Los puntajes C1–C4 y el hash técnico del cierre se conservan; no se infiere la sustentación del repositorio.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

El reporte S10 define el escenario y un cambio coherente. La cifra de 28 ms no tiene una prueba o serie que mida latencia; faltan una línea base y una nueva medición demostrada. La documentación continúa parcial.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/retos/corte-2-experimento.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/docs/retos/corte-2-experimento.md#L7-L33) — C1
2. [docs/adr/0002-control-concurrencia-memoria-inventario.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/docs/adr/0002-control-concurrencia-memoria-inventario.md#L5-L28) — C2
3. [.github/workflows/test.yml](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/.github/workflows/test.yml#L23-L45) — C3

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** La composición y los límites productos–inventario coinciden con los ADR actuales; almacenamiento en memoria, ausencia de auth y destinos Render/Dokploy están declarados. Se detectó una brecha en la traducción de errores de dominio al contrato HTTP.

**Arquitectura declarada:** Monolito modular FastAPI, hexagonal por módulo, integración síncrona por puertos consumidores y adaptadores cruzados hacia application; repositorios en memoria y lock por SKU. Otros módulos y persistencia relacional son objetivos.

**Arquitectura implementada:** app/main.py crea repositorios, casos de uso y adaptadores cruzados y entrega dependencias a crear_router. Inventario valida producto vía ConsultarProducto, serializa movimiento con asyncio.Lock y guarda stock/historial. Productos consulta historial por adaptador de aplicación. Lectura de stock accede al puerto desde router, tal como C4 vigente lo representa.

**Hallazgos materiales: 1.** Prioridad máxima: **Media**.

<a id="deriva-d1"></a>

### D1 · Errores de cantidad del dominio escapan al borde HTTP

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** Alta sobre el camino de excepciones; no ejecutado..

**Motivo de prioridad:** Media: una entrada inválida atraviesa el límite de validación y se convierte en error interno no contractual, sin evidencia de corrupción del stock ni de incidente desplegado.

**Declaración contrastada:**

- [docs/api/inventrack-contrato.md:45–62](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/docs/api/inventrack-contrato.md#L45-L62) — El contrato vigente enumera las respuestas y la traducción de errores de dominio.
- [contracts/openapi/v1.json:288–295](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/contracts/openapi/v1.json#L288-L295)

**Implementación contrastada:**

- [app/inventario/infrastructure/router.py:10–12](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/app/inventario/infrastructure/router.py#L10-L12) — El esquema HTTP acepta cualquier entero, sin mínimo positivo.
- [app/inventario/infrastructure/router.py:25–36](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/app/inventario/infrastructure/router.py#L25-L36) — El handler solo captura producto inválido y timeout, no ValueError.
- [app/inventario/domain/stock.py:9–18](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/app/inventario/domain/stock.py#L9-L18) — El dominio rechaza cantidades cero o negativas mediante ValueError.
- [app/inventario/application/registrar_movimiento.py:38–49](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/app/inventario/application/registrar_movimiento.py#L38-L49) — La ruta de aplicación llama directamente a la regla de stock.

**Efecto y alcance:** El contrato enumera rechazos controlados pero una cantidad 0 o negativa, admitida como int por el esquema HTTP, llega al dominio y lanza ValueError sin traducción. La ruta puede producir un 500 genérico donde debería rechazar una entrada inválida; se debilita la frontera HTTP/dominio. Es deducción estática, no fallo observado en producción.

**Corrección propuesta:** Definir un error de cantidad de dominio y mapearlo a 400/422 en ambos handlers, o validar también cantidad>0 en el esquema conservando la regla de dominio. Actualizar OpenAPI y pruebas negativas HTTP de entrada/salida con 0 y negativos.

### Cobertura y límites de la auditoría

**Capas, dominio y adaptadores:** Inspeccionadas composición, routers, registrar_movimiento y adaptadores cruzados. No se detectó import directo de infraestructura ajena en esos adaptadores; dominio puro en StockProducto.

**Persistencia:** Memoria en el composition root; ADR0006 acepta volatilidad y un solo proceso. No se exige PostgreSQL futuro ni persistencia entre réplicas.

**API y autorización:** Contrato funcional y routers contrastados. Auth está explícitamente fuera del MVP. Hallazgo en cantidad no positiva: ValueError no traducido.

**Despliegue:** Compose fija puerto 10000 y límites; ADR0006 mantiene Render y Dokploy en paralelo y Azure histórico. No se verificaron servicios remotos.

**Asincronía:** Operaciones request-response; lock async es control de concurrencia, no broker. ADR0003 declara límite de concurrencia entre contextos, por lo que no se vuelve a presentar ese límite aceptado como deriva nueva.

**Observabilidad:** Middleware y endpoint /metrics implementan contador, suma y p95 por método/path, en memoria; historia de 1000 por clave. Cardinalidad total y p95 operativo no evaluados dinámicamente.

**Fuentes de la cobertura:**

- [docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md:36–44](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md#L36-L44)
- [docs/adr/0003-integracion-productos-inventario-via-puertos-de-aplicacion.md:54–88](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/docs/adr/0003-integracion-productos-inventario-via-puertos-de-aplicacion.md#L54-L88)
- [docs/adr/0003-integracion-productos-inventario-via-puertos-de-aplicacion.md:104–116](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/docs/adr/0003-integracion-productos-inventario-via-puertos-de-aplicacion.md#L104-L116)
- [docs/c4/components.md:71–83](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/docs/c4/components.md#L71-L83)
- [app/main.py:105–130](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/app/main.py#L105-L130)
- [app/main.py:143–170](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/app/main.py#L143-L170)
- [app/inventario/infrastructure/validador_producto_adapter.py:1–12](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/app/inventario/infrastructure/validador_producto_adapter.py#L1-L12)
- [app/productos/infrastructure/historial_movimientos_adapter.py:1–11](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/app/productos/infrastructure/historial_movimientos_adapter.py#L1-L11)
- [docs/api/inventrack-contrato.md:25–33](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/docs/api/inventrack-contrato.md#L25-L33)
- [docs/adr/0006-desplegar-en-dokploy-institucional.md:45–64](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/docs/adr/0006-desplegar-en-dokploy-institucional.md#L45-L64)
- [deploy/compose.lab.yaml:1–19](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/deploy/compose.lab.yaml#L1-L19)
- [docs/adr/0007-exponer-p95-de-latencia-en-metricas.md:24–38](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/539840be57f8a0b719bb33e19d05031489a25b86/docs/adr/0007-exponer-p95-de-latencia-en-metricas.md#L24-L38)

**Límites adicionales:** Auditoría estática nueva del SHA indicado mediante git show, sin checkout ni ejecución de código estudiantil, sin lectura de PDF, sin publicar ni cambiar notas. No se verificaron el runtime desplegado, secretos/configuración de panel, cargas, CI en vivo ni disponibilidad. Los documentos de pruebas aportan intención y alcance, no una ejecución independiente de esta auditoría.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:45:59.555681+00:00 confirmó el hash anterior como último commit de `main` antes del límite exclusivo. La punta observada es [`539840be57f8a0b719bb33e19d05031489a25b86`](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/539840be57f8a0b719bb33e19d05031489a25b86) (2026-10-11T23:05:35-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Semana 10 · Segundo corte · InvenTrack

**Revisión preliminar.** Cierre previsto: 2026-10-12T05:00:00Z (medianoche de Colombia). El estado puede cambiar antes del cierre y debe volver a congelarse entonces.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_InvenTrack |
| Estado revisado | `35a9c63dd603bab989a18ed17ca56063c5616585` en `origin/main` (2026-10-04T22:14:10-05:00) |
| Rama remota principal | `origin/main` |
| Observación | 2026-10-06T21:31:50.213435+00:00 |
| Punta revisada para S10 | `35a9c63dd603bab989a18ed17ca56063c5616585` (2026-10-04T22:14:10-05:00) |
| S9 congelado, solo como línea base | `35a9c63dd603bab989a18ed17ca56063c5616585` |

## Alcance y escenario operativo asignado

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

**Escenario asignado: No verificado.** No se localizó una asignación oficial del reto S10. ESC-04 es un escenario de calidad previo y el documento del reto disponible es de corte 1; no se asume que equivalga a la asignación del segundo corte. Fuente o búsqueda: [docs/arc42/arc42-template-EN.md:747-756](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/arc42/arc42-template-EN.md#L747-L756); [docs/evidencia-ia-corte-s9.md:7-18](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s9.md#L7-L18); búsqueda en README, ADR y docs/retos. La evidencia de S6–S9 se usa como base; no se vuelve a calificar por existir. La evolución se contrastó con el hash S5 publicado `ac951e3fc2acf849f2cc89ffb622d392b268672a`: el delta hasta esta punta modifica 65 archivos; los cambios pertinentes se enlazan en las filas de decisión, implementación y arquitectura. No se recalifica S5 ni se usan sus referencias históricas a etiquetas como requisito vigente.

## Matriz técnica preliminar

La fila «PDF de dos páginas» se omite por exclusión docente; quedan **12 filas**, incluida la sustentación pendiente.

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | main 35a9c63dd603bab989a18ed17ca56063c5616585 (2026-10-04T22:14:10-05:00); punta anterior al cierre futuro. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://inventrack.iscoutb.dev/health: HTTP 200, 7.043 s; /metrics: HTTP 200, 7.454 s. Consulta iniciada 2026-10-06T21:17:34Z. URL en [README.md:34-39](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/README.md#L34-L39). Son sondas read-only; no se ejecutó el flujo de inventario. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | No se localizó una asignación oficial del reto S10. ESC-04 es un escenario de calidad previo y el documento del reto disponible es de corte 1; no se asume que equivalga a la asignación del segundo corte. [docs/arc42/arc42-template-EN.md:747-756](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/arc42/arc42-template-EN.md#L747-L756); [docs/evidencia-ia-corte-s9.md:7-18](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s9.md#L7-L18); búsqueda en README, ADR y docs/retos |
| Línea base medida y reproducible | No verificado | [docs/evidencia-ia-corte-s9.md:78-94](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s9.md#L78-L94) no es línea base del reto confirmado; /health no modela consultas de stock bajo carga. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0007-exponer-p95-de-latencia-en-metricas.md:15-38](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0007-exponer-p95-de-latencia-en-metricas.md#L15-L38) acredita decisión de p95/costo, pero falta asignación para juzgar adecuación S10. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [app/main.py:99-102](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/app/main.py#L99-L102) y [app/main.py:143-162](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/app/main.py#L143-L162) implementan cálculo y métrica; no se los da por respuesta al reto sin conocerlo. |
| Resultado contrastado con el umbral | No verificado | No hay contraste verificable de línea base/respuesta del reto S10 identificado; la medición S9 de [docs/evidencia-ia-corte-s9.md:78-94](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s9.md#L78-L94) tiene alcance local. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | Health y /metrics accesibles; logs JSON en [app/main.py:36-90](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/app/main.py#L36-L90). Falta run actual confirmado, Quality Gate bloqueante y vínculo de métrica al reto asignado; no se confunde estado visible con resultado de carga. |
| Secretos protegidos | No verificado | La auditoría del equipo declara ausencia de credenciales en [docs/evidencia-ia-corte-s6.md:176-180](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s6.md#L176-L180). Las referencias de secretos de CI son variables en [.github/workflows/test.yml:37-41](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/.github/workflows/test.yml#L37-L41). El barrido independiente ampliado fue cancelado por la herramienta y el único reintento no lo completó; no se convierte esa limitación en evidencia de exposición ni en un árbol limpio verificado. |
| C4, arc42, ADR y contratos correspondientes al MVP | Cumple | [docs/c4/containers.md:68-74](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/c4/containers.md#L68-L74) distingue API real, frontend futuro y memoria; [docs/c4/containers.md:122-128](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/c4/containers.md#L122-L128) declara límites. [docs/aspectos.md:19](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/aspectos.md#L19) enlaza cambio, prueba y medición; ADR-0007 y vista de despliegue están versionados. Coherencia documental de la base acreditada, sin convertirla en logro S10. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md:7-15](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md#L7-L15) consolida decisiones, pero no aporta confirmación/reemplazo basado en el experimento S10. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Pendiente de sesión docente en el despliegue y ejecución de pipeline en vivo. |

Recuento descriptivo: 3 Cumple, 0 No cumple y 9 No verificado, sobre 12 filas. **No se transforma este recuento en nota.**

## Rúbrica del segundo corte (cinco criterios)

Escala del aula: 0,00 / 0,60 / 0,80 / 1,00 por criterio. Niveles exclusivamente propuestos al docente.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Reto asignado no confirmado; no se puntúa ESC-04 como si fuera esa asignación. |
| Decisión e implementación | No verificado | Pendiente | Código, ADR y alternativas presentes para S9; adecuación al reto S10 pendiente. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Sondas y métrica verificadas por lectura; run actual, secreto y gate requieren completar evidencia. |
| Evolución arquitectónica trazable | No verificado | Pendiente | Base documentada y enlazada; confirmación/reemplazo por experimento S10 pendiente. |
| Sustentación del reto | Pendiente de sustentación | Pendiente | La fija el docente en sesión. |

**Total final no determinado.** No se aplica la fórmula semanal. La sustentación corresponde al docente, sobre el entorno desplegado y con el pipeline en vivo; los criterios sin escenario confirmado no reciben un cero por esa falta de verificación.

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_InvenTrack; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Árbol Git contiene seis rutas mínimas; tabla de aspectos [docs/aspectos.md:15-19](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/aspectos.md#L15-L19) y documentos enlazados existentes. |
| Estado calificado identificable | Cumple | main, 35a9c63dd603bab989a18ed17ca56063c5616585, fecha y corte en cabecera. |
| Nombres de ADR según la convención | Cumple | Listado docs/adr: 0001–0009, todos NNNN-titulo-en-kebab-case; [docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md:1-15](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md#L1-L15). |
| ADR aceptados no reescritos | No cumple | [docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md:7-15](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md#L7-L15) reconoce ediciones aceptadas de 0002/0004/0005 y declara consolidación futura; no marca cada decisión anterior reemplazada con enlaces. Historial del periodo incluye restauración [193e2628](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/193e2628757f3e8987ae5a01a90b8e8cce45d7a0). La corrección de política se reconoce, pero no borra las reescrituras. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:23-25](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/ia.md#L23-L25) contiene usos hasta S9, aceptado y rechazos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | [sonar-project.properties:1-7](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/sonar-project.properties#L1-L7) y [.github/workflows/test.yml:23-45](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/.github/workflows/test.yml#L23-L45) acreditan configuración/scanner. Una consulta de runs del commit (limitada a pull_request por el conector) no devolvió registros; no acredita ausencia de push ni éxito. No se verificó el Quality Gate público para este hash; además el YAML no incluye espera/bloqueo explícito de Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | No verificado | La auditoría del equipo declara ausencia de credenciales en [docs/evidencia-ia-corte-s6.md:176-180](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s6.md#L176-L180). Las referencias de secretos de CI son variables en [.github/workflows/test.yml:37-41](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/.github/workflows/test.yml#L37-L41). El barrido independiente ampliado fue cancelado por la herramienta y el único reintento no lo completó; no se convierte esa limitación en evidencia de exposición ni en un árbol limpio verificado. |
| Contribución de todos los integrantes | No verificado | El historial contiene varias firmas; las atribuciones por semejanza no se usan. La planilla previa reconoce correspondencias pendientes. Se debe validar cuenta–integrante y distribución, sin publicar correos. |

## Estado global del proyecto (overall)

Punta observada de `origin/main`: `35a9c63dd603bab989a18ed17ca56063c5616585` (2026-10-04T22:14:10-05:00). Hay 0 commits posteriores al estado congelado S9. La punta coincide con el cierre S9. El backend y las sondas del dominio institucional responden; el proyecto conserva almacenamiento en memoria. El cálculo p95 es verificable estáticamente y la medición debe pasar de /health al flujo de negocio bajo la carga de ESC-04.

- Medir catálogo/stock con la carga y condiciones de ESC-04; la sonda /health no es un sustituto.
- Completar el registro inmutable/reemplazo de ADR anteriores y aportar run/scanner/Quality Gate público del hash revisado.
- Terminar la verificación independiente de secretos e identidad de contribuciones; la limitación de herramienta no demuestra exposición.
- Identificar escenario S10, línea base del despliegue y resultado reproducible.

### Hallazgos anteriores cerrados o delimitados

- Se cierra «sin porción S9»: app/main.py y tests/test_metrics.py cambian dentro del periodo.
- ASP-03 ya enlaza ocho eslabones y existe mutación documentada que falla.
- Hay auditoría de límites con universo de dependencias nuevo vacío explícito; se corrige la lectura anterior que penalizaba no añadir paquetes.
- ADR-0008 formaliza no incorporar generación; ADR-0009 reconoce el problema de inmutabilidad, aunque su resolución es parcial.
- Sondas del despliegue institucional responden; la falta de URL/health no sigue abierta como ausencia de artefacto.

## Preparación de la sustentación

1. Fallo: si se reinicia o replica el proceso, ¿qué ocurre con stock, locks y el historial p95 y cómo detectarán inconsistencias?
2. Costo: ¿qué volumen o necesidad de persistencia obligaría a abandonar el presupuesto cero y qué alternativa compararon?
3. Medición: si las consultas reales de stock incumplen 400 ms aunque /health sea rápido, ¿qué cambio harían y con qué experimento lo validarían?

## Próximos pasos

Las sondas públicas de salud y métricas responden. Confirmen el escenario operativo asignado, midan una línea base del flujo de negocio y comparen la respuesta con el umbral en el despliegue. Aporten evidencia actual del pipeline y Quality Gate y preparen la defensa del almacenamiento en memoria y de su costo de evolución.

</details>
