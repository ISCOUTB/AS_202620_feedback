# Segundo corte · S10 · LostVault · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_LostVault |
| Rama evaluada | `main` |
| Hash calificado | `99fb413bda00c208ec42104dcfe6a4c189fbad77` |
| Fecha del commit | 2026-10-04T22:30:53-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

Búsqueda con 200 conexiones y p95 ≤2 s

Se valora el escenario documentado disponible; no se afirma asignación docente verificada ni nueva entrega específica S10. Evidencias previas se usan como estado del repositorio, no se traslada ni promedia su nota anterior.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Básico | 0,60 / 1,00 |
| C2 · Decisión e implementación | Básico | 0,60 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Básico | 0,60 / 1,00 |
| C4 · Evolución arquitectónica trazable | Básico | 0,60 / 1,00 |
| C5 · Sustentación del reto | Pendiente docente | Pendiente |

**Subtotal técnico: 2,40 / 4,00. Total sobre 5,00 pendiente de C5.**

C5 sigue pendiente de calificación docente. No se registra como cero ni se estima a partir del repositorio.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

Se comparan cargas en Vercel y un proxy local, sin un antes y después equivalente. Con 200 conexiones se reconocen fallos; el p95 en memoria no se acumula entre invocaciones. El código y la arquitectura documentada divergen.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/adr/000.3-despliegue-busqueda-lostvault.md:65–106](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L65-L106)
2. [docs/arc42/07_vista_despliegue.md:30–65](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/arc42/07_vista_despliegue.md#L30-L65)
3. [docs/ddd/auditoria_backend.md:58–92](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L58-L92)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** El corte Flutter mantiene los contratos públicos y declara sus dobles in-memory. La API Python posterior conserva la brecha de modularidad que el equipo registró como NC6; el README aún la presenta como proveedor futuro.

**Arquitectura declarada:** Monolito modular con hexagonal selectiva, módulos accesibles solo por public/. Flujo de reclamación exige autenticación y verificación; proveedor HTTP síncrono en Vercel con estado volátil explícitamente aceptado.

**Arquitectura implementada:** Flutter main compone servicios en memoria y llama ClaimObjectUseCase a través de interfaces públicas. Separadamente backend/main.py expone FastAPI: JWT→diccionario de objetos→verificación de identidad simplificada→lista de claims y modificación de objeto bajo lock local. No existe una llamada HTTP desde el flujo Flutter examinado al proveedor; ambos son rutas independientes.

**Hallazgos materiales: 2.** Prioridad máxima: **Media**.

<a id="deriva-d1"></a>

### D1 · La reclamación HTTP evita los límites de aplicación y propiedad del monolito modular

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** Alta: ruta ejecutable y escrituras inspeccionadas..

**Motivo de prioridad:** Media: la ruta crítica concentra escrituras de dos contextos en HTTP y viola el límite modular vigente; no se acredita acceso fraudulento ni pérdida de datos.

**Declaración contrastada:**

- [docs/arc42/04_estilo_arquitectonico.md:27–33](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/arc42/04_estilo_arquitectonico.md#L27-L33) — La estrategia exige fronteras públicas e inversión de dependencias.
- [docs/ddd/auditoria_backend.md:86–92](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L86-L92) — El propio equipo mantiene NC6 como corrección pendiente.

**Implementación contrastada:**

- [backend/main.py:213–230](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L213-L230) — El handler HTTP valida negocio y modifica ambos almacenes directamente.
- [backend/main.py:136–151](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L136-L151) — Objects y Claims son estado global del mismo archivo.
- [lib/features/claims/application/claim_object_use_case.dart:1–22](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/lib/features/claims/application/claim_object_use_case.dart#L1-L22) — En Dart sí se consumen interfaces públicas de los otros módulos.

**Efecto y alcance:** El handler create_claim mezcla HTTP, autenticación, regla de disponibilidad, verificación y escritura directa de _claims/_objects. A diferencia del flujo Dart por interfaces, el backend carece de un dueño encapsulado de Objects que reciba la transición; cambios de persistencia y reglas afectan la frontera HTTP. Es una deuda ya reconocida como NC6, todavía presente en el SHA.

**Corrección propuesta:** Extraer caso de uso Python y servicio/repositorio dueño de objetos; el router traduce HTTP, Claims solicita reserva al contrato de Objects y la atomicidad permanece en una unidad de trabajo. Probar la ruta HTTP y los límites de imports, no solo la estructura Dart.

<a id="deriva-d2"></a>

### D2 · README aún describe como futuro un proveedor HTTP que ya tiene implementación

**Naturaleza:** documentación desactualizada. **Prioridad:** Baja. **Confianza:** Alta..

**Motivo de prioridad:** Baja: el desfase puede confundir integración y despliegue, pero no identifica un fallo nuevo del proveedor.

**Declaración contrastada:**

- [README.md:172–185](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/README.md#L172-L185) — El README sigue llamando futuro al proveedor HTTP.

**Implementación contrastada:**

- [backend/main.py:198–230](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L198-L230) — FastAPI ya implementa consulta de objetos y reclamación.
- [docs/adr/0003-plataforma-despliegue-vercel.md:45–60](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L45-L60) — El ADR vigente adopta el proveedor Vercel.
- [lib/main.dart:49–68](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/lib/main.dart#L49-L68) — El cliente continúa compuesto con servicios en memoria.

**Efecto y alcance:** El lector del README recibe una arquitectura anterior: contrato previo a implementar el proveedor, mientras ADR0003 y backend/main.py ya definen API separada. Puede confundirse el demo Flutter en memoria con un flujo móvil conectado a esa API.

**Corrección propuesta:** Actualizar README y vistas con dos rutas actuales: demo Flutter local y proveedor FastAPI; señalar explícitamente que el cliente aún no lo consume. Separar diagrama implementado de integración futura y corregir la referencia obsoleta a vercel.json.

### Cobertura y límites de la auditoría

**Capas, dominio y adaptadores:** Se siguió main.dart→ClaimObjectUseCase→servicios públicos y API create_claim→almacenes globales. NC6 comprobada nuevamente sobre código, no asumida por la auditoría anterior.

**Persistencia:** Diccionarios/listas in-memory en cliente y proveedor. Volatilidad serverless reconocida por ADR0003; no se impone PostgreSQL futuro como deriva.

**API y autorización:** Ruta de claims y respuestas201/401/404/409/422 coinciden en forma con OpenAPI. JWT exige sub; verify_identity es stub no vacío. La limitación documental real se admite explícitamente en arc42§6 y no se vende como verificación institucional.

**Despliegue:** ADR0003 y arc42§7 distinguen API Vercel y Flutter no publicado. No se verificó plataforma remota. La referencia a backend/vercel.json en arc42 está obsoleta frente a Zero-Config y archivo ausente en el árbol; no se trata como fallo de despliegue.

**Asincronía:** Claims HTTP resuelve dentro de la petición y lock local; no hay cola requerida. Cliente Flutter usa Future de servicios locales, no integración remota ya completada.

**Observabilidad:** Middleware JSON, agrupación por plantilla y p95 ventana local presentes en Python. ADR0003 acepta límite de acumulación entre instancias; no se infiere p95 global ni se valida comportamiento de Vercel en vivo.

**Fuentes de la cobertura:**

- [docs/arc42/05_vista_bloques.md:18–34](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/arc42/05_vista_bloques.md#L18-L34)
- [docs/arc42/06_vista_runtime.md:64–66](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/arc42/06_vista_runtime.md#L64-L66)
- [docs/adr/0002-integracion-reclamacion-api.md:21–34](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0002-integracion-reclamacion-api.md#L21-L34)
- [docs/adr/0003-plataforma-despliegue-vercel.md:87–103](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L87-L103)
- [docs/contracts/lostvault-api.yaml:12–48](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/contracts/lostvault-api.yaml#L12-L48)
- [lib/main.dart:49–83](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/lib/main.dart#L49-L83)
- [lib/features/claims/application/claim_object_use_case.dart:24–58](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/lib/features/claims/application/claim_object_use_case.dart#L24-L58)
- [backend/main.py:107–133](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L107-L133)
- [backend/main.py:154–164](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L154-L164)
- [docs/arc42/07_vista_despliegue.md:11–18](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/arc42/07_vista_despliegue.md#L11-L18)

**Límites adicionales:** Auditoría estática nueva del SHA indicado mediante git show, sin checkout ni ejecución de código estudiantil, sin lectura de PDF, sin publicar ni cambiar notas. No se verificaron el runtime desplegado, secretos/configuración de panel, cargas, CI en vivo ni disponibilidad. Los documentos de pruebas aportan intención y alcance, no una ejecución independiente de esta auditoría.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:45:59.573402+00:00 confirmó el hash anterior como último commit de `main` antes del límite exclusivo. La punta observada es [`99fb413bda00c208ec42104dcfe6a4c189fbad77`](https://github.com/ISCOUTB/AS_202620_LostVault/commit/99fb413bda00c208ec42104dcfe6a4c189fbad77) (2026-10-04T22:30:53-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Semana 10 · Segundo corte · LostVault

**Revisión preliminar.** Cierre previsto: 2026-10-12T05:00:00Z (medianoche de Colombia). El estado puede cambiar antes del cierre y debe volver a congelarse entonces.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_LostVault |
| Estado revisado | `99fb413bda00c208ec42104dcfe6a4c189fbad77` en `origin/main` (2026-10-04T22:30:53-05:00) |
| Rama remota principal | `origin/main` |
| Observación | 2026-10-06T21:31:50.350893+00:00 |
| Punta revisada para S10 | `99fb413bda00c208ec42104dcfe6a4c189fbad77` (2026-10-04T22:30:53-05:00) |
| S9 congelado, solo como línea base | `99fb413bda00c208ec42104dcfe6a4c189fbad77` |

## Alcance y escenario operativo asignado

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

**Escenario asignado: No verificado.** Se encontró «condición operativa asignada» para el Escenario 4 en un documento comparativo del taller. ADR-0003 declara expresamente que ese taller es una entrega separada. No prueba cuál es la asignación S10 del equipo. Fuente o búsqueda: [docs/adr/000.3-despliegue-busqueda-lostvault.md:14-22](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L14-L22) y [docs/adr/0003-plataforma-despliegue-vercel.md:23-30](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L23-L30). La evidencia de S6–S9 se usa como base; no se vuelve a calificar por existir. La evolución se contrastó con el hash S5 publicado `c0c17c1e9c3387ac915767cd706e8b785a3deadf`: el delta hasta esta punta modifica 43 archivos; los cambios pertinentes se enlazan en las filas de decisión, implementación y arquitectura. No se recalifica S5 ni se usan sus referencias históricas a etiquetas como requisito vigente.

## Matriz técnica preliminar

La fila «PDF de dos páginas» se omite por exclusión docente; quedan **12 filas**, incluida la sustentación pendiente.

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta main 99fb413bda00c208ec42104dcfe6a4c189fbad77; fecha anterior al cierre futuro, revisión preliminar. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://backend-nu-self-91.vercel.app/health: HTTP 200 en 6.124 s; inicio 2026-10-06T21:23:22Z. URL en [docs/arc42/07_vista_despliegue.md:11-18](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/arc42/07_vista_despliegue.md#L11-L18). No se probó el flujo de reclamación ni se repitió carga. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | Se encontró «condición operativa asignada» para el Escenario 4 en un documento comparativo del taller. ADR-0003 declara expresamente que ese taller es una entrega separada. No prueba cuál es la asignación S10 del equipo. [docs/adr/000.3-despliegue-busqueda-lostvault.md:14-22](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L14-L22) y [docs/adr/0003-plataforma-despliegue-vercel.md:23-30](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L23-L30) |
| Línea base medida y reproducible | No verificado | [docs/adr/000.3-despliegue-busqueda-lostvault.md:91-106](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L91-L106) documenta dos cargas de Vercel, pero no una línea base/intervención del reto S10 confirmado; comparación local/serverless es taller. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0003-plataforma-despliegue-vercel.md:32-76](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L32-L76) justifica plataforma S8; falta decisión de respuesta al reto asignado actual. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [backend/main.py:185-210](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L185-L210) añade señales reales, pero no se presume respuesta a S10 sin asignación confirmada. |
| Resultado contrastado con el umbral | No verificado | [docs/adr/000.3-despliegue-busqueda-lostvault.md:95-100](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L95-L100) revela degradación bajo 200 conexiones; no se debe presentar p95 de peticiones exitosas como cumplimiento íntegro. Falta experimento de respuesta S10. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | Hay JSON y request_id en [backend/main.py:107-133](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L107-L133) y health público; [docs/arc42/07_vista_despliegue.md:30-65](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/arc42/07_vista_despliegue.md#L30-L65) declara que p95 en memoria no acumula entre instancias. Run actual, secretos y observación del reto pendientes; la degradación ya medida exige resolver una métrica agregada. |
| Secretos protegidos | No verificado | El equipo auditó main.py/Dockerfile en [docs/ddd/auditoria_backend.md:29-44](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L29-L44) y el código lee JWT_SECRET del entorno en [backend/main.py:50-55](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L50-L55). El barrido independiente completo fue cancelado por la herramienta, también en el reintento autorizado. No se atribuye exposición ni incumplimiento académico por esa limitación; falta cerrar la comprobación del revisor. El literal de CI en [.github/workflows/build.yml:55-60](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/.github/workflows/build.yml#L55-L60) está rotulado como prueba efímera y no se presenta como secreto de producción. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/ddd/auditoria_backend.md:58-92](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L58-L92) documenta arquitectura Python divergente del ADR modular; [docs/arc42/07_vista_despliegue.md:67-75](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/arc42/07_vista_despliegue.md#L67-L75) cita backend/vercel.json inexistente en el árbol. La documentación debe distinguir IaC real, prototipo y código desplegado. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/000.3-despliegue-busqueda-lostvault.md:100](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L100) contradice expectativa de escalado, pero no hay ADR que confirme/reemplace la decisión a partir de un reto S10 identificado. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Sustentación y pipeline en vivo pendientes de docente. |

Recuento descriptivo: 2 Cumple, 1 No cumple y 9 No verificado, sobre 12 filas. **No se transforma este recuento en nota.**

## Rúbrica del segundo corte (cinco criterios)

Escala del aula: 0,00 / 0,60 / 0,80 / 1,00 por criterio. Niveles exclusivamente propuestos al docente.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Asignación S10 no confirmada; la condición del taller no se da por esa asignación. |
| Decisión e implementación | No verificado | Pendiente | Plataforma S8 documentada, nueva decisión ligada al reto pendiente. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Health y correlación presentes; métricas no agregadas, degradación medida y barrido independiente pendiente. |
| Evolución arquitectónica trazable | No verificado | Pendiente | NC6 y referencias de IaC muestran desalineación; falta decisión a partir del experimento S10. |
| Sustentación del reto | Pendiente de sustentación | Pendiente | La fija el docente en sesión. |

**Total final no determinado.** No se aplica la fórmula semanal. La sustentación corresponde al docente, sobre el entorno desplegado y con el pipeline en vivo; los criterios sin escenario confirmado no reciben un cero por esa falta de verificación.

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_LostVault; [README.md:1-9](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/README.md#L1-L9). |
| Estructura mínima presente | Cumple | Árbol Git contiene las seis rutas mínimas; índice [README.md:207-224](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/README.md#L207-L224). |
| Estado calificado identificable | Cumple | origin/main 99fb413bda00c208ec42104dcfe6a4c189fbad77; último commit anterior al cierre en cabecera. |
| Nombres de ADR según la convención | No cumple | [docs/adr/000.3-despliegue-busqueda-lostvault.md:1-4](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L1-L4) usa 000.3, fuera de convención; [docs/adr/0003-plataforma-despliegue-vercel.md:23-30](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L23-L30) reconoce el typo y que es un taller distinto. |
| ADR aceptados no reescritos | No cumple | Historial verificado de ADR-0001/0002: [edd78d72](https://github.com/ISCOUTB/AS_202620_LostVault/commit/edd78d72afe70c55ca77e37b909f2ab8ab442834) y [b5615768](https://github.com/ISCOUTB/AS_202620_LostVault/commit/b5615768472c8c64dc3abff3dbf701faa40c2420) modifican decisiones aceptadas; no se localizó reemplazo declarado que resuelva el arrastre. |
| docs/ia.md al día para la semana | No cumple | [docs/ia.md:181-223](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ia.md#L181-L223) está al día temporalmente, pero falta rechazo con motivo técnico de S9; la razón de propiedad individual no satisface esa parte. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | [.github/workflows/build.yml:62-76](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/.github/workflows/build.yml#L62-L76) tiene scanner y Quality Gate; configuración versionada sonar-project.properties. Única consulta PR del hash devolvió cero runs, sin demostrar inexistencia de runs push. No se verificó run/Quality Gate público de este hash y no se recicla el verde S8. |
| Sin credenciales en el repositorio ni en el historial | No verificado | El equipo auditó main.py/Dockerfile en [docs/ddd/auditoria_backend.md:29-44](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L29-L44) y el código lee JWT_SECRET del entorno en [backend/main.py:50-55](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L50-L55). El barrido independiente completo fue cancelado por la herramienta, también en el reintento autorizado. No se atribuye exposición ni incumplimiento académico por esa limitación; falta cerrar la comprobación del revisor. El literal de CI en [.github/workflows/build.yml:55-60](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/.github/workflows/build.yml#L55-L60) está rotulado como prueba efímera y no se presenta como secreto de producción. |
| Contribución de todos los integrantes | No verificado | La planilla anterior deja asociaciones de varias cuentas por confirmar. No se asignan personas por semejanza ni se repiten conteos antiguos como estado vigente; pendiente validación docente de autoría. |

## Estado global del proyecto (overall)

Punta observada de `origin/main`: `99fb413bda00c208ec42104dcfe6a4c189fbad77` (2026-10-04T22:30:53-05:00). Hay 0 commits posteriores al estado congelado S9. Punta igual al cierre S9. Health responde. El equipo documentó un resultado importante: con 200 conexiones ~44 % de fallos, aunque el p95 de respuestas exitosas era bajo. No debe ocultarse al defender disponibilidad. NC6 y persistencia/métricas en memoria siguen abiertas.

- Completar cadena navegable de AS-04 con C4, código, prueba y medición.
- Formalizar la decisión de la porción p95; demostrar la prueba ante defecto concreto y registrar rechazo técnico de IA.
- Corregir NC6 o justificar una arquitectura actual que preserve dueño único, con prueba que la proteja.
- Agregación de métricas/persistencia en despliegue serverless y tratamiento del fallo con 200 conexiones.
- Eliminar referencias a IaC inexistente, ordenar ADR y aportar run/Quality Gate actual.
- Asignación S10, autoría y barrido independiente de secretos pendientes.

### Hallazgos anteriores cerrados o delimitados

- Se cierra la ausencia preliminar de porción S9: métrica con objective_ms/met y test nuevos.
- Registro IA S9 y auditoría NC6 existen, aunque no completan todos sus criterios.
- ADR-0004 formaliza no generación.
- Existe medición del despliegue real con umbral y fallos declarados; health accesible hoy.

## Preparación de la sustentación

1. Fallo: ¿cómo evitarán dos reclamaciones inconsistentes o pérdida de datos cuando Vercel atienda solicitudes en instancias distintas?
2. Costo: ¿cuánto cuestan persistencia y métricas compartidas para sostener 200 conexiones, frente al plan gratuito actual?
3. Medición: con ~44 % de fallos bajo la carga prevista, ¿qué decisión de plataforma o control de carga cambiarían y qué resultado demostraría la mejora?

## Próximos pasos

La sonda de salud responde, pero el experimento documenta fallos importantes con 200 conexiones: el p95 de respuestas exitosas no demuestra disponibilidad. Identifiquen el reto asignado, resuelvan persistencia y agregación de métricas entre instancias y documenten qué decisión cambia a la luz de los fallos medidos.

</details>
