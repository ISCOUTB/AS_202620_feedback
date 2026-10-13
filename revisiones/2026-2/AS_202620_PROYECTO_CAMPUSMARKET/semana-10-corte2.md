# Segundo corte · S10 · CampusMarket · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET |
| Rama evaluada | `master` |
| Hash calificado | `1582c1ff609202fa2cc4a06fa14d18b9b61bed74` |
| Fecha del commit | 2026-10-11T23:50:44-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

S10-CT-01: incompatibilidad del consumidor sale frente a enum venta/alquiler; conservar API v2 y adaptar consumidor

Se evalúa técnicamente el escenario declarado; no se afirma asignación docente verificada.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Sobresaliente | 1,00 / 1,00 |
| C2 · Decisión e implementación | Sobresaliente | 1,00 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Sobresaliente | 1,00 / 1,00 |
| C4 · Evolución arquitectónica trazable | Sobresaliente | 1,00 / 1,00 |
| C5 · Sustentación del reto | Calificación comunicada por el docente | 0,80 / 1,00 |

**Subtotal técnico: 4,00 / 4,00. Total consolidado C1–C5: 4,80 / 5,00.**

Calificación de sustentación comunicada por el docente: **4,00 / 5,00**, incorporada como **C5 = 0,80 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

El experimento del consumidor incompatible tiene línea base y 58 observaciones contrastadas en la evaluación, correlación en las 58 y secuencia de rechazo y recuperación 200→422→200. El ADR-0020 confirma decisiones previas mediante evidencia. Se recupera el consumidor experimental; no se demuestra recuperación de infraestructura.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/evidencias/evidencia-s10-corte2-2026-10-11.md:7](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/evidencias/evidencia-s10-corte2-2026-10-11.md#L7); [docs/evidencias/evidencia-s10-corte2-2026-10-11.md:26–43](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/evidencias/evidencia-s10-corte2-2026-10-11.md#L26-L43); [docs/evidencias/evidencia-s10-corte2-2026-10-11.md:45–85](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/evidencias/evidencia-s10-corte2-2026-10-11.md#L45-L85); [docs/evidencias/evidencia-s10-corte2-2026-10-11.md:87–108](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/evidencias/evidencia-s10-corte2-2026-10-11.md#L87-L108); [docs/evidencias/evidencia-s10-corte2-2026-10-11.md:129–145](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/evidencias/evidencia-s10-corte2-2026-10-11.md#L129-L145) — asignación pendiente, escenario, resultados, observabilidad, trazabilidad y límites
2. [docs/adr/0020-preservar-contrato-v2-y-adaptar-consumidor-incompatible.md:3–42](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/adr/0020-preservar-contrato-v2-y-adaptar-consumidor-incompatible.md#L3-L42) — alternativas, no-cambio justificado, confirmación previa
3. [scripts/experimento_s10_contrato.py:33–35](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/scripts/experimento_s10_contrato.py#L33-L35); [scripts/experimento_s10_contrato.py:47–104](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/scripts/experimento_s10_contrato.py#L47-L104); [scripts/experimento_s10_contrato.py:124–149](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/scripts/experimento_s10_contrato.py#L124-L149) — adaptación, observación, cálculo y plan previo

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** No se observó deriva material en los recorridos muestreados. La adaptación S10 vive en el consumidor experimental; no se atribuyó al proveedor un cambio inexistente. MySQL, fronteras de servicios y volúmenes concuerdan con las decisiones recientes.

**Arquitectura declarada:** Monolito modular FastAPI con Usuarios, Publicaciones, Catálogo y Administración; único escritor por tabla; Flutter, MySQL y Dokploy.

**Arquitectura implementada:** Routers→servicios→repositorios propietarios; Catálogo pide publicaciones/imágenes al servicio Publicaciones; Administración solicita ocultamiento por servicio; identidad mediante sesión opaca.

**Hallazgos materiales: 0.** No se observó deriva material en los recorridos inspeccionados; esto no acredita conformidad exhaustiva ni ejecución correcta en producción.

### Cobertura y límites de la auditoría

**Capas y dominio:** Rastreo de GET /catalogo hasta lectura por Publicaciones; moderación pasa por servicio propietario, no repository ajeno.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [docs/arc42/05-bloques-de-construccion.md:9–27](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/arc42/05-bloques-de-construccion.md#L9-L27) — arc42 asigna tablas a sus contextos y exige que Catálogo/Administración consuman el servicio de Publicaciones.
- [backend/app/catalogo/router.py:41–65](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/backend/app/catalogo/router.py#L41-L65) — El router de catálogo valida filtros y llama buscar_publicaciones con los parámetros aceptados.
- [backend/app/catalogo/service.py:1–5](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/backend/app/catalogo/service.py#L1-L5) — Catálogo importa capacidades de publicaciones.service, no su repositorio SQL.
- [backend/app/catalogo/service.py:55–62](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/backend/app/catalogo/service.py#L55-L62) — El catálogo consulta imágenes agrupadas por IDs y compone las respuestas sin consultas por fila.
- [backend/app/administracion/service.py:24–30](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/backend/app/administracion/service.py#L24-L30) — La resolución de reportes solicita ocultamiento al servicio Publicaciones dentro de la revisión del reporte.

**Persistencia:** MySQL y volumen de uploads; bloqueo de reporte con transacción. Fallo parcial entre contextos/SQL-filesystem reconocido, no atomicidad global prometida.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [deploy/compose.lab.yaml:42–54](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/deploy/compose.lab.yaml#L42-L54) — Compose configura MySQL 8.4 y monta mysql_data en el directorio de datos.
- [backend/app/administracion/repository.py:59–69](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/backend/app/administracion/repository.py#L59-L69) — open_review bloquea el reporte con SELECT FOR UPDATE y rechaza reportes ya resueltos.
- [docs/arc42/08-conceptos-transversales.md:69–76](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/arc42/08-conceptos-transversales.md#L69-L76) — arc42 reconoce transacciones separadas para ocultamiento/resolución y compensación entre SQL y filesystem.

**API y autorización:** v2 admite venta/alquiler; Dependencias de sesión y moderación; adaptación experimental no cambia servidor.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/app/catalogo/router.py:41–46](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/backend/app/catalogo/router.py#L41-L46) — El esquema de query restringe modalidad a venta/alquiler y valida rangos de precio.
- [backend/app/usuarios/dependencies.py:12–34](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/backend/app/usuarios/dependencies.py#L12-L34) — Las dependencias exigen Bearer, resuelven usuario y devuelven 403 si no tiene capacidad de moderación.
- [docs/adr/0020-preservar-contrato-v2-y-adaptar-consumidor-incompatible.md:20–30](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/adr/0020-preservar-contrato-v2-y-adaptar-consumidor-incompatible.md#L20-L30) — ADR20 mantiene proveedor v2 y transforma sale a venta solo en el consumidor experimental.

**Despliegue:** API y MySQL con volúmenes/256 MiB por servicio; Pages fuera de Compose. Arc42 distingue revisión realmente observada del commit documental.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [deploy/compose.lab.yaml:19–24](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/deploy/compose.lab.yaml#L19-L24) — La API monta publication_images y depende de que MySQL reporte salud.
- [deploy/compose.lab.yaml:36–54](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/deploy/compose.lab.yaml#L36-L54) — Compose limita API a 256 MiB y define MySQL con su volumen de datos separado.
- [docs/arc42/s10-adenda-operativa.md:15–19](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/arc42/s10-adenda-operativa.md#L15-L19) — La adenda mantiene Pages/Dokploy y distingue revisión del proveedor observado de la documentación posterior.

**Asincronía:** HTTP/JSON y llamadas internas síncronas; no se prometen broker ni servicios por contexto.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [docs/arc42/08-conceptos-transversales.md:25–33](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/arc42/08-conceptos-transversales.md#L25-L33) — El mapa de contextos define relaciones internas por servicios y descarta servicios desplegables por contexto.
- [docs/arc42/08-conceptos-transversales.md:62–67](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/arc42/08-conceptos-transversales.md#L62-L67) — El contrato vigente es HTTP/JSON síncrono con Bearer/OpenAPI v2; v1 queda histórico.
- [backend/app/catalogo/service.py:17–24](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/backend/app/catalogo/service.py#L17-L24) — buscar_publicaciones obtiene primero la colección del servicio de Publicaciones para aplicar filtros.

**Observabilidad:** Middleware de logs/correlación, health dependiente de persistencia y métrica EC01; S10 usa observador externo, explícitamente no logs privados.

Límite: Inspección estática; no se ejecutaron pruebas ni se comprobó el servicio remoto.

- [backend/app/main.py:52–65](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/backend/app/main.py#L52-L65) — main instala límite de cuerpo, observabilidad y manejadores que devuelven errores de persistencia/validación seguros.
- [backend/app/main.py:101–120](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/backend/app/main.py#L101-L120) — main expone la métrica EC01 y /health, que consulta disponibilidad de la persistencia.
- [docs/adr/0020-preservar-contrato-v2-y-adaptar-consumidor-incompatible.md:32–37](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/1582c1ff609202fa2cc4a06fa14d18b9b61bed74/docs/adr/0020-preservar-contrato-v2-y-adaptar-consumidor-incompatible.md#L32-L37) — ADR20 limita las observaciones productivas a HTTP/correlación y distingue los logs verificados localmente.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:45:48.479240+00:00 confirmó el hash anterior como último commit de `master` antes del límite exclusivo. La punta observada es [`1582c1ff609202fa2cc4a06fa14d18b9b61bed74`](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/1582c1ff609202fa2cc4a06fa14d18b9b61bed74) (2026-10-11T23:50:44-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Semana 10 · Segundo corte · CampusMarket

> **Revisión preliminar**, realizada el 6 de octubre de 2026. El cierre de S10 todavía no ha ocurrido. No constituye nota aplicada ni evaluación de sustentación.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET |
| Estado revisado | `de6ed67c05ccdb7eabd9b1951f146ab8958b1d00` en `origin/master` (2026-10-04T02:14:34-05:00) |
| Rama remota principal | `origin/master` |
| Base S8 | `784d788c19418099decde77a2cfb5ba831ab993b` |
| Estado preliminar S10 / HEAD | `de6ed67c05ccdb7eabd9b1951f146ab8958b1d00` · 2026-10-04T02:14:34-05:00 |
| Cierre previsto S10 | 2026-10-12T05:00:00Z |
| Observación | 2026-10-06T21:17:09Z |

## Escenario operativo asignado y alcance

**No verificado.** EC-01 está documentado como escenario propio de consulta de productos y utilizado en S9. No se encontró evidencia que lo identifique como el escenario operativo oficialmente asignado para el segundo corte. Fuentes consultadas: [README.md:17–28](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L17-L28), [docs/evidencias/evidencia-s9-2026-10-01.md:350–371](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/evidencias/evidencia-s9-2026-10-01.md#L350-L371) y [docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md:8–51](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md#L8-L51).

Se revisaron README, ADR, arc42 y evidencias/experimentos. Un escenario de calidad elegido por el equipo no demuestra cuál le asignó el docente. Antes de valorar la respuesta del reto hay que disponer del enunciado o una referencia oficial equipo–escenario. Las evidencias S6–S9 se describen como línea base, sin recalificarlas por existir.

**PDF excluido por instrucción docente:** se omite su fila; no se leyó ningún PDF ni se cuenta como incumplimiento. La matriz conserva 12 comprobaciones. Se realizaron únicamente consultas HTTP de lectura indicadas abajo. No se ejecutó código del equipo ni se probó el flujo principal.

## Matriz de comprobación S10

| Criterio | Evidencia técnica esperada | Estado preliminar | Observaciones y evidencia |
|---|---|---|---|
| Estado de S10 identificable y anterior al cierre | Rama principal, hash y fecha; estado preliminar | Cumple | HEAD de6ed67c05ccdb7eabd9b1951f146ab8958b1d00, 2026-10-04T02:14:34-05:00, anterior al cierre previsto; es una foto preliminar, no el futuro estado final. |
| Despliegue accesible en el momento de la revisión | Respuesta HTTP, tiempo y hora | Cumple | Comprobación de lectura iniciada 2026-10-06T21:17:09Z: frontend https://nnigarp.github.io/AS_202620_PROYECTO_CAMPUSMARKET/ HTTP 200 en 3,046350 s; /health https://campusmarket.iscoutb.dev/health HTTP 200 en 6,379432 s. URLs declaradas en [README.md:50–69](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L50-L69). No se probó flujo principal ni se atribuye el despliegue al hash documental. |
| Hipótesis, montaje, variables y umbral declarados | Caracterización del escenario operativo asignado | No verificado | EC-01 tiene carga y umbral propios, pero falta fuente de asignación S10: [docs/evidencias/evidencia-s9-2026-10-01.md:350–371](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/evidencias/evidencia-s9-2026-10-01.md#L350-L371). |
| Línea base medida y reproducible | Herramienta, carga y procedimiento del escenario asignado | No verificado | Hay baseline del defecto N+1 y resultados bajo cuota de S9: [docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md:8–15](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md#L8-L15). No demuestra línea base del reto oficialmente asignado. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | ADR y respuesta al escenario asignado | No verificado | ADR-0019 fundamenta respuesta N+1; coherencia observada como base. Pendiente contrastarla con la consigna de S10, sin otorgar otra nota por S9. |
| Respuesta implementada o configurada sobre el MVP | Cambio trazable correspondiente al reto | No verificado | Implementación real de lote en [backend/app/catalogo/service.py:57–62](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/backend/app/catalogo/service.py#L57-L62); no puede afirmarse que sea la respuesta al escenario S10 desconocido. |
| Resultado contrastado con el umbral | Medición final comparable con línea base | No verificado | Medición S9 de loopback documentada y CI success; medición pública completa y correspondencia con el reto pendientes: [docs/evidencias/evidencia-s9-2026-10-01.md:350–371](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/evidencias/evidencia-s9-2026-10-01.md#L350-L371). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | Run y observabilidad del escenario asignado | No verificado | Cuatro runs finales success y /health 200; métrica EC-01 documentada en [README.md:60–69](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L60-L69). Falta demostrar observación de la respuesta a la asignación S10 y el bloqueo de integración; scanner Sonar continúa abierto. |
| Secretos protegidos | Barrido del contrato | Cumple | Sin credenciales productivas detectadas en código/documentos actuales; CI Gitleaks de checkout success: [.github/workflows/backend-tests.yml:70–78](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/.github/workflows/backend-tests.yml#L70-L78). No se presenta el historial completo como comprobado. |
| C4, arc42, ADR y contratos correspondientes al MVP | Consistencia documental y trazabilidad | Cumple | C4 describe cuatro contextos, MySQL/archivos, HTTPS y OpenAPI v2: [docs/c4/02-contenedores.md:4–48](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/c4/02-contenedores.md#L4-L48). arc42 registra topología vigente separada de historia Azure: [docs/arc42/07-vista-despliegue.md:3–46](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/arc42/07-vista-despliegue.md#L3-L46). Correspondencia de base verificable; evolución específica del reto aún pendiente. |
| Decisión anterior confirmada o reemplazada con evidencia | Relación explícita entre medición y decisión | No verificado | ADR-0019 extiende 0009/0016 con evidencia N+1: [docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md:3–51](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md#L3-L51). Es respuesta medida de S9, sin identificación como cambio requerido por S10. |
| Sustentación del reto sobre el entorno desplegado | Sesión y pipeline en vivo; lo resuelve el docente | No verificado | El docente debe evaluar explicación del reto en el entorno desplegado y pipeline en vivo; no se puntúa desde el repositorio. |

## Rúbrica del segundo corte · cinco criterios

Escala de la ficha: **0,00 · 0,60 · 0,80 · 1,00 por criterio**. No se aplica la fórmula semanal. Una comprobación pendiente conserva puntaje pendiente; no se convierte automáticamente en cero.

| Criterio | Nivel sugerido | Puntaje | Fundamento |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Sin asignación oficial, EC-01 propio no permite fijar nivel de caracterización del reto. |
| Decisión e implementación | No verificado | Pendiente | Hay decisión e implementación fundamentadas de S9; pendiente su correspondencia con el reto S10. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | CI y health actuales verificados; observabilidad específica del reto, scanner y bloqueo de integración pendientes. |
| Evolución arquitectónica trazable | No verificado | Pendiente | C4/arc42/contrato actualizados como línea base; no se atribuye nivel de evolución S10 a la entrega S9 por existir. |
| Sustentación del reto | Pendiente del docente | Pendiente | Pendiente de sustentación sobre el despliegue y ejecución del pipeline en vivo; no se infiere desde el repositorio. |

**Total: pendiente, no calculado.** La correspondencia con la asignación y la sustentación impiden proponer un total responsable.

## Matriz transversal · CONTRATO §11

| Criterio transversal | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon git público de ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET y rama master; URL oficial y nombre conforme. |
| Estructura mínima presente | Cumple | Árbol con README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md; entrada navegable [README.md:13–28](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L13-L28). |
| Estado calificado identificable | Cumple | Último commit de origin/master anterior o igual al cierre: de6ed67c05ccdb7eabd9b1951f146ab8958b1d00, 2026-10-04T02:14:34-05:00; coincide con HEAD observado. |
| Nombres de ADR según la convención | Cumple | Inventario git de docs/adr: 0001–0019 siguen NNNN-titulo-en-kebab-case.md. Ejemplo [docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md:1–6](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/adr/0019-consultar-imagenes-en-lote-a-traves-de-publicaciones.md#L1-L6). |
| ADR aceptados no reescritos | No cumple | Historial revalidado de ADR-0002 (77e1323 → d72d6ac/3bb84a9/04fe631), 0003 (485249a → df72b1c), 0005 (39f0952 → 0e2b85b): ediciones después de aceptación sin reemplazo. El cierre reconoce que el hallazgo persiste: [docs/evidencias/evidencia-s9-2026-10-01.md:414–425](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/evidencias/evidencia-s9-2026-10-01.md#L414-L425). No se penaliza por añadir ADR sucesores nuevos. |
| docs/ia.md al día para la semana | Cumple | Registro S9 actualizado y rechazo razonado: [docs/ia.md:482–506](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/ia.md#L482-L506). Para S10 aún no se acredita un registro específico del reto asignado. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI backend y otros tres workflows del hash están success, pero backend-tests solo ejecuta Ruff/Gitleaks/pruebas: [.github/workflows/backend-tests.yml:61–78](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/.github/workflows/backend-tests.yml#L61-L78), [.github/workflows/backend-tests.yml:105–130](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/.github/workflows/backend-tests.yml#L105-L130). Falta scanner Sonar en CI; la documentación lo reconoce: [README.md:67–69](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L67-L69). Gate automático o badge no satisface los tres eslabones del contrato. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Checkout y CI sin hallazgos productivos observados. El barrido independiente amplio del historial no concluyó por interrupción de la herramienta; CI solo cubre el intervalo fijado en [.github/workflows/backend-tests.yml:70–78](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/.github/workflows/backend-tests.yml#L70-L78). El barrido histórico documentado distingue cinco falsos positivos: [docs/evidencias/evidencia-s9-2026-10-01.md:529–555](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/docs/evidencias/evidencia-s9-2026-10-01.md#L529-L555). Falta completar comprobación independiente del historial completo. |
| Contribución de todos los integrantes | No verificado | Historial agregado: 365 commits y cinco nombres de autor; dos firmas comparten dirección y se consolidan, sin publicar correos. [README.md:5–9](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/de6ed67c05ccdb7eabd9b1951f146ab8958b1d00/README.md#L5-L9) enumera integrantes sin mapear todas las cuentas. La correspondencia previa no se da por probada por parecido de nombres; confirmar mapa explícito persona–cuenta. |

## Estado global (overall)

HEAD: `de6ed67c05ccdb7eabd9b1951f146ab8958b1d00` · 2026-10-04T02:14:34-05:00. La punta coincide con S9; no hay cambios tardíos que alteren la calificación. Cuatro runs del hash están success. El frontend público y /health respondieron 200 en esta revisión. S9 presenta evidencia completa dentro de su alcance; siguen abiertos Sonar en pipeline, medición pública extremo a extremo y las ediciones históricas de ADR. La asignación específica S10 no se localizó.

Recuento descriptivo: **4 Cumple, 0 No cumple, 8 No verificado, sobre 12.** No es una nota ni sustituye la rúbrica.

## Próximos pasos

Para el segundo corte falta identificar el escenario operativo asignado por el docente. El despliegue y el health check responden; preparen la línea base, la intervención y el resultado comparable del reto, con métrica y límites de validez. No presenten el experimento de S9 como respuesta a una asignación todavía no confirmada. La sustentación y el pipeline en vivo quedan pendientes.

## Tres preguntas para la sustentación

1. Fallo: ¿qué ocurre con catálogo, health y datos si MySQL falla, y qué evidencia distingue recuperación de API de recreación de ambos contenedores?
2. Costo: ¿qué límite de memoria, CPU o volumen haría inviable la solución actual y por qué la lectura en lote fue preferible a aumentar recursos?
3. Medición: si el navegador público sigue sobre dos segundos mientras loopback cumple, ¿qué medirían y cambiarían primero?

## Delta arquitectónico desde el primer corte

Base publicada de S5: `8044215811e53b111888f75b30fc175fb889dc56`; comparación git contra HEAD `de6ed67c05ccdb7eabd9b1951f146ab8958b1d00`: 157 rutas cambiadas, de ellas 34 en ADR/arc42/C4 (sin leer PDF). Se inspeccionaron las decisiones, contratos, código y evidencia citados en las filas. El delta sirve para examinar evolución y consistencia del MVP, no para recalificar las entregas S6–S9. La correspondencia con el escenario asignado S10 sigue pendiente.

</details>
