# Segundo corte · S10 · UTB Tracker · consolidación al cierre

**Actualización del feedback: 13 de octubre de 2026.** La tabla siguiente sustituye la valoración preliminar conservada al final.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_UTB_TRACKER |
| Rama evaluada | `main` |
| Hash calificado | `d17c9eb241e56755d48b022dc00ddb865e40c391` |
| Fecha del commit | 2026-10-06T01:08:05-05:00 |
| Límite exclusivo S10 | `2026-10-13T05:00:00Z` |
| Último instante incluido | 12 de octubre de 2026, 23:59:59, Colombia (UTC-5) |

## Alcance vigente

Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

Los PDF están excluidos sin penalización. No se ejecutó código estudiantil en la revisión. Las cifras y experimentos documentados por los equipos se distinguen de las comprobaciones del revisor; esta publicación consolida la evaluación ya realizada y no representa una nueva prueba de flujo principal, despliegue, carga o seguridad. La lista de comprobación y la matriz transversal de las pasadas anteriores se conservan abajo con su alcance histórico; no se recalculan ni se convierten en una nota mediante la fórmula semanal. S9 permanece congelada.

## Escenario documentado

QS-06: confiabilidad de recursos y préstamos

Se valora el escenario documentado disponible; no se afirma asignación docente verificada ni nueva entrega específica S10. Evidencias previas se usan como estado del repositorio, no se traslada ni promedia su nota anterior.

## Rúbrica consolidada

| Criterio | Nivel técnico / origen | Puntaje |
|---|---|---:|
| C1 · Caracterización del escenario operativo | Básico | 0,60 / 1,00 |
| C2 · Decisión e implementación | Básico | 0,60 / 1,00 |
| C3 · Operación, seguridad y observabilidad | Insuficiente | 0,00 / 1,00 |
| C4 · Evolución arquitectónica trazable | Básico | 0,60 / 1,00 |
| C5 · Sustentación del reto | Calificación comunicada por el docente | 0,80 / 1,00 |

**Subtotal técnico: 1,80 / 4,00. Total consolidado C1–C5: 2,60 / 5,00.**

Calificación de sustentación comunicada por el docente: **4,00 / 5,00**, incorporada como **C5 = 0,80 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

Los componentes técnicos se publican como propuesta al docente. Publicar esta consolidación no acredita un registro de la calificación en Moodle.

## Fundamento técnico y comentarios vigentes

El escenario está formulado, sin línea base ni resultado numérico reproducible. La integración y autenticación son parciales y no hay ADR del nuevo cambio. No se instrumentan la métrica del escenario ni logs estructurados; el despliegue sigue como plantilla.

Los puntajes C1–C4 se conservan de la evaluación consolidada; el comentario y las fuentes siguientes sustentan la valoración conjunta, sin inferir puntajes nuevos de los recuentos preliminares.

### Fuentes del estado calificado

1. [docs/aspectos.md:65–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L65-L82)
2. [.github/workflows/ci.yml:19–23](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/.github/workflows/ci.yml#L19-L23)
3. [docs/arc42/arc42.md:249–278](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/arc42/arc42.md#L249-L278)

## Deriva arquitectónica al cierre S10

Auditoría estática de la arquitectura declarada frente a las rutas implementadas en el mismo hash del cierre S10. Se revisaron capas y dominio, persistencia, API y autorización, despliegue, asincronía y observabilidad. Se excluyeron PDF y commits posteriores al cierre; no se ejecutó código estudiantil ni se probó el servicio remoto. Una funcionalidad futura explícitamente delimitada o una deuda aceptada por un ADR vigente no se cuenta por sí sola como deriva. La gravedad indica prioridad técnica del hallazgo; no equivale a un descuento automático en la rúbrica. Los hallazgos se incorporan como feedback y propuestas de corrección; los puntajes C1–C4 conservan la matriz técnica vigente, sin recalificación por esta auditoría.

**Resultado:** El backend sí conserva el flujo síncrono REST/SQL del corte vertical, pero la autorización declarada no está conectada a las rutas de recursos, préstamos y gestión de usuarios. La promesa de exclusión de préstamos concurrentes tampoco tiene arbitraje atómico visible. El arranque de BD ya no coincide con la documentación SQLite sin configuración.

**Arquitectura declarada:** Monolito modular FastAPI y cliente Flutter previsto; SQLAlchemy, PostgreSQL en despliegue/SQLite automático en desarrollo; integración síncrona. Arc42 declara Depends de autorización y bcrypt; regla un recurso, un préstamo activo. Alembic pendiente aceptado.

**Arquitectura implementada:** main monta routers sin dependencias de seguridad globales. Recursos/Préstamos operan directamente sobre modelos SQL y comparten recurso_models; esa dependencia está expresamente documentada. Auth crea JWT pero no hay guardia en las rutas inspeccionadas; login sombrea su servicio. DATABASE_URL es obligatoria. Préstamo hace SELECT, verifica estado en Python y luego INSERT/UPDATE/commit.

**Hallazgos materiales: 3.** Prioridad máxima: **Alta**.

<a id="deriva-d1"></a>

### D1 · La seguridad declarada no está conectada al camino de escritura y gestión de usuarios

**Naturaleza:** implementación. **Prioridad:** Alta. **Confianza:** alta.

**Declaración contrastada:**

- [docs/arc42/arc42.md:139–142](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/arc42/arc42.md#L139-L142) — Afirma políticas de autorización por Depends y bcrypt.
- [docs/arc42/arc42.md:374–383](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/arc42/arc42.md#L374-L383) — Define rechazo de modificaciones fuera de rol como escenario de seguridad.

**Implementación contrastada:**

- [app/main.py:9–14](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/main.py#L9-L14) — No se configura guardia global ni al montar routers.
- [app/routers/resources.py:17–26](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/routers/resources.py#L17-L26) — Escritura solo depende de la sesión de BD.
- [app/routers/loans.py:20–35](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/routers/loans.py#L20-L35) — Préstamo acepta usuario_id del payload, sin identidad autenticada.
- [app/routers/auth.py:1–24](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/routers/auth.py#L1-L24) — Login redefine el nombre importado y se llama a sí mismo; consultar/borrar usuario no usan guardia.
- [app/services/auth.py:21–27](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/services/auth.py#L21-L27) — La cadena escrita compara password directamente; no verifica hash bcrypt.

**Efecto y alcance:** Quien alcance estas rutas de la aplicación puede invocar creación de recursos/préstamos y gestión de usuarios sin verificación de identidad/rol en el código. Es de alta prioridad por integridad y datos; no se verificó publicación ni explotación remota. Además, el camino de login no llega al servicio por sombreado del nombre.

**Corrección propuesta:** Conectar una dependencia de identidad y otra de roles en rutas protegidas; derivar usuario desde el token cuando corresponda. Renombrar handler/servicio de login para evitar sombreado, verificar hashes con bcrypt y añadir pruebas 401/403. No se afirma cómo están almacenadas contraseñas reales: únicamente ausencia de hash/verificación en esta cadena.

<a id="deriva-d2"></a>

### D2 · La exclusión de dos préstamos activos está validada antes de escribir, sin arbitraje atómico

**Naturaleza:** implementación. **Prioridad:** Media. **Confianza:** alta en ausencia de mecanismo; media sobre concurrencia efectiva.

**Declaración contrastada:**

- [docs/arc42/arc42.md:240–247](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/arc42/arc42.md#L240-L247) — Afirma que nunca permite dos préstamos activos por recurso.

**Implementación contrastada:**

- [app/routers/loans.py:20–36](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/routers/loans.py#L20-L36) — SELECT seguido de validación Python y escritura separada.
- [app/models/recurso_models.py:30–40](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/models/recurso_models.py#L30-L40) — Modelo de préstamos no declara unicidad activa por recurso.
- [tests/test_loans.py:32–49](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/tests/test_loans.py#L32-L49) — Prueba dos solicitudes sucesivas, no simultáneas.

**Efecto y alcance:** En una ejecución concurrente dos transacciones pueden leer disponible antes de que alguna actualice; no se ve bloqueo de fila, actualización condicional ni restricción única de préstamo activo. El test secuencial no demuestra la garantía nunca dos préstamos. No se observó un duplicado real.

**Corrección propuesta:** Proteger la decisión con UPDATE condicional y chequeo de filas afectadas o bloqueo transaccional apropiado a PostgreSQL; sumar restricción de unicidad activa donde aplique y prueba concurrente. Mantener 409 como rechazo de la operación perdedora.

<a id="deriva-d3"></a>

### D3 · El arranque de persistencia ya requiere configuración aunque README promete SQLite automático

**Naturaleza:** documentación desactualizada. **Prioridad:** Media. **Confianza:** alta.

**Declaración contrastada:**

- [README.md:65–67](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/README.md#L65-L67) — Promete SQLite sin configuración en desarrollo/CI y DATABASE_URL solo en despliegue.

**Implementación contrastada:**

- [app/core/database.py:1–12](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/database.py#L1-L12) — Carga dotenv y exige os.environ[DATABASE_URL], sin fallback SQLite.
- [app/main.py:3–7](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/main.py#L3-L7) — El punto de entrada importa engine y crea tablas al cargar.

**Efecto y alcance:** Un clon sin DATABASE_URL no sigue el recorrido local prometido: la lectura obligatoria de la variable ocurre al importar la configuración. Esto afecta reproducibilidad del despliegue de desarrollo; no es prueba de indisponibilidad remota.

**Corrección propuesta:** Actualizar el contrato operativo a DATABASE_URL obligatoria y dar plantilla sin secretos, o recuperar fallback explícito y seguro solo en desarrollo. Mantener Alembic como deuda aceptada, sin presentarlo ya implementado.

### Cobertura y límites de la auditoría

**Capas, dominio y adaptadores:** Routers concentran regla y acceso ORM; préstamos lee/modifica recursos directamente.

Límite: Arc42 declara expresamente esa dependencia; no se etiqueta la disposición por carpetas como deriva ni se exige hexagonal.

- [docs/arc42/arc42.md:167–184](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/arc42/arc42.md#L167-L184) — Dependencia préstamos→recursos y fronteras declaradas.
- [app/routers/loans.py:13–35](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/routers/loans.py#L13-L35) — Ruta real directa router→ORM.

**Persistencia:** Se examinó configuración, modelos, creación esquema y atomicidad de préstamo.

Límite: Alembic pendiente aceptado por ADR-0002; motor/aislamiento desplegados desconocidos.

- [docs/adr/0002-cambio-stack-fastapi-flutter.md:53–57](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/adr/0002-cambio-stack-fastapi-flutter.md#L53-L57) — Migraciones como deuda aceptada.

**API y autorización:** Se revisaron routers, seguridad JWT, servicio y modelos de auth y contratos de préstamos/recursos.

Límite: No se ejecutó código ni se probaron usuarios/credenciales reales.

- [app/core/security.py:8–20](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/security.py#L8-L20) — Funciones de emisión/verificación existen, pero no se inyectan en rutas protegidas.

**Despliegue:** C4 distingue Flutter/API/SQL; árbol no contiene proyecto Flutter ni manifiesto de despliegue reproducible en este repositorio.

Límite: Flutter puede estar en otro repositorio como declara C4; no se infiere inexistencia externa ni caída.

- [docs/c4/C2.md:3–16](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/c4/C2.md#L3-L16) — Vista describe cliente en repo/carpeta propia y flujo síncrono.

**Asincronía:** Handlers REST y SQL síncronos. ADR-0003 descarta cola para resultado inmediato de préstamo.

Límite: La concurrencia del framework no equivale a exclusión transaccional.

- [docs/adr/0003-integracion-sincrona.md:21–32](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/adr/0003-integracion-sincrona.md#L21-L32) — Decisión de integración síncrona y motivo.

**Observabilidad:** Router health montado; no se identificó middleware propio de métricas/logs estructurados en árbol del snapshot.

Límite: No se convierte ausencia de plataforma de observabilidad no prometida en deriva; no se observaron servicios externos.

- [app/main.py:1–14](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/main.py#L1-L14) — Composición completa de aplicación.

**Límites adicionales:** Auditoría estática por git show al hash fijo, sin checkout, ejecución de código estudiantil, lectura de PDF, escritura en GitHub, pruebas en producción ni cambios de notas. No certifica ausencia de defectos fuera de las rutas revisadas.

## Estado global del proyecto (overall)

La verificación de metadatos del 2026-10-13T16:46:15.728011+00:00 confirmó el hash anterior como último commit de `main` antes del límite exclusivo. La punta observada es [`d17c9eb241e56755d48b022dc00ddb865e40c391`](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/d17c9eb241e56755d48b022dc00ddb865e40c391) (2026-10-06T01:08:05-05:00). Coincide con el estado calificado; no hay commits posteriores al cierre en esa rama al momento de la comprobación.

<details>
<summary>Historial S10 anterior, superado; conservar fechas y alcance originales</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

# Segundo corte S10 · revisión preliminar · UTB Tracker

**Preliminar; no es la calificación del corte.** Se revisa la punta actual, con cierre futuro **2026-10-12T05:00:00Z**. S9 queda congelada de forma independiente.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_UTB_TRACKER |
| Rama principal remota | `main` |
| Base S5 publicada | `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849` |
| Base S8 | `ae526db29b4f2d1f5981536e18438f9a62b1516d` |
| Estado revisado | `d17c9eb241e56755d48b022dc00ddb865e40c391` en `origin/main` (2026-10-06T01:08:05-05:00) |
| Punta actual / S10 preliminar | `d17c9eb241e56755d48b022dc00ddb865e40c391` · 2026-10-06T01:08:05-05:00 |
| Observado | 2026-10-06T21:28:33.555768Z |

## Alcance y método

Revisión de archivos y del historial mediante Git, sin ejecutar código, pruebas, scripts ni despliegues de estudiantes. Se consultó una vez el listado de runs de GitHub Actions; un run verde se limita a los pasos que declara su workflow y no acredita la sustentación, el flujo desplegado ni un Quality Gate omitido. No se consultaron etiquetas. No se leyó ningún PDF; el criterio PDF se excluye por decisión docente, sin penalización. Las mediciones documentadas se atribuyen al equipo y no se presentan como ejecuciones del revisor.

## Escenario operativo asignado

**No verificado.** README, ADR 0001–0003 y arc42 describen QS-01…QS-06 y el corte vertical, pero no registran la asignación oficial del reto S10. Fuente inspeccionada: [docs/aspectos.md:65–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L65-L82). No se equipara un escenario de calidad genérico ni el ejercicio S9 con la asignación oficial. Las filas que dependen de esa correspondencia permanecen abiertas hasta obtener la consigna y contrastarla.

## Matriz de preparación S10

El renglón «PDF de dos páginas» se omite expresamente por exclusión docente: quedan **12 filas**, sin fórmula semanal de calificación.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Estado preliminar de main registrado en el encabezado y anterior al cierre futuro. |
| Despliegue accesible en el momento de la revisión | No verificado | [README.md:5–11](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/README.md#L5-L11) solo declara localhost; falta URL pública verificable. [app/routers/health.py:6–12](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/routers/health.py#L6-L12) implementa /salud, sin comprobación externa. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | [docs/aspectos.md:65–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L65-L82) contiene escenarios de calidad anteriores; no asignación S10 con hipótesis/montaje/variables. |
| Línea base medida y reproducible | No cumple | [docs/aspectos.md:72–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L72-L82) solo narra la regla de préstamos; no hay medición reproducible de línea base en la punta. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0003-integracion-sincrona.md:21–60](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/adr/0003-integracion-sincrona.md#L21-L60) conserva decisión previa; la nueva autenticación/reorganización no tiene ADR del reto ni costo documentado. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [app/main.py:3–14](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/main.py#L3-L14) integra autenticación y nuevos módulos después de S9; no hay vínculo a la consigna S10. |
| Resultado contrastado con el umbral | No cumple | [docs/aspectos.md:72–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L72-L82) no aporta resultado numérico frente a línea base y umbral; el árbol carece de experimento S10 reproducible. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | [CI actual en failure](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/37422096531); [.github/workflows/ci.yml:19–23](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/.github/workflows/ci.yml#L19-L23) cubre solo app/tests/. Salud en código sin logs estructurados ni métrica del escenario identificable. |
| Secretos protegidos | Cumple | [app/core/config.py:7–11](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/config.py#L7-L11) usa entorno y el barrido actual no detecta credenciales reales. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/arc42/arc42.md:249–278](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/arc42/arc42.md#L249-L278) conserva plantilla de despliegue; [README.md:42–67](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/README.md#L42-L67) y [docs/c4/C2.md:3–6](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/c4/C2.md#L3-L6) citan estructura/base de datos anterior a la reorganización. |
| Decisión anterior confirmada o reemplazada con evidencia | No cumple | [docs/adr/0003-integracion-sincrona.md:51–60](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/adr/0003-integracion-sincrona.md#L51-L60) registra consecuencias previas sin confirmación/reemplazo a partir de mediciones del reto actual; no hay ADR nuevo. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Sustentación sobre despliegue y pipeline en vivo pendiente del docente. |

## Rúbrica específica de cinco criterios

| Criterio | Nivel sugerido | Puntaje | Evidencia y límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | README, ADR 0001–0003 y arc42 describen QS-01…QS-06 y el corte vertical, pero no registran la asignación oficial del reto S10. |
| Decisión e implementación | No verificado | Pendiente | Existe cambio tardío de autenticación, pero falta escenario oficial y decisión del reto. |
| Operación, seguridad y observabilidad | Insuficiente | 0.00 | Pipeline de la punta en failure; no se instrumenta métrica del escenario ni logs estructurados, por lo que no se demuestra observabilidad de la respuesta. |
| Evolución arquitectónica trazable | Básico | 0.60 | Hay C4/arc42/ADR previos, pero despliegue conserva plantilla y las rutas no reflejan la reorganización. |
| Sustentación del reto | Lo fija el docente | Pendiente | Sesión pendiente. |

**No se publica total final.** La escala de cada criterio es 0,00 / 0,60 / 0,80 / 1,00; la sustentación queda a cargo del docente, con entorno desplegado y pipeline en vivo. Las celdas pendientes no equivalen a cero. S6–S9 no se recalifican por existir.

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público del repositorio vigente; [README.md:1–3](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/README.md#L1-L3). |
| Estructura mínima presente | Cumple | Las seis rutas mínimas siguen presentes en la punta. La vigencia de enlaces/diagramas se evalúa por separado. [docs/aspectos.md:63–72](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/aspectos.md#L63-L72). |
| Estado calificado identificable | Cumple | main d17c9eb241e56755d48b022dc00ddb865e40c391 del 2026-10-06; punta preliminar distinta del estado S9 congelado. |
| Nombres de ADR según la convención | Cumple | Tres nombres conformes: 0001-estilo-arquitectonico.md, 0002-cambio-stack-fastapi-flutter.md y 0003-integracion-sincrona.md; [docs/adr/0003-integracion-sincrona.md:7–25](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/adr/0003-integracion-sincrona.md#L7-L25). |
| ADR aceptados no reescritos | Cumple | Historial de los tres ADR: solo sus commits de creación (5f923cd, e88a3d6, 9cf1ac9); sin ediciones posteriores. [docs/adr/0003-integracion-sincrona.md:3–5](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/adr/0003-integracion-sincrona.md#L3-L5). |
| docs/ia.md al día para la semana | No cumple | [docs/ia.md:11–14](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/docs/ia.md#L11-L14): no documenta tampoco la nueva autenticación y reorganización de octubre. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [Run de la punta](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/37422096531) en failure. [.github/workflows/ci.yml:19–23](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/.github/workflows/ci.yml#L19-L23) solo invoca app/tests/, omitiendo tests/ de contratos/préstamos/recursos; no incluye scanner SonarCloud. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido de la punta sin credenciales reales; [app/core/config.py:7–11](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/config.py#L7-L11) toma las claves del entorno. No se verificó rotación ni configuración del servidor externo. |
| Contribución de todos los integrantes | No verificado | Firmas del historial agregadas, con variantes de identidad; correspondencia con toda la matrícula no verificada. No se mantienen inferencias individuales de informes anteriores. |

## Estado global del proyecto (overall)

Punta de la misma rama: `d17c9eb241e56755d48b022dc00ddb865e40c391` (2026-10-06T01:08:05-05:00). Hay **0 commits en el delta S8→S9** y **7 commits posteriores al cierre S9**. S9 está congelada sin cambios respecto de S8. Después del cierre hay siete commits, incluida reorganización del backend y autenticación JWT. El CI sigue fallando y la documentación no refleja todavía la nueva estructura.



### Hallazgos abiertos

- S9 no incorpora commits nuevos frente a S8; la autenticación de octubre es tardía y solo se valora en overall/S10.
- Recuperar el CI y ejecutar también tests/ de contratos, préstamos y recursos; actualmente solo se invoca app/tests/.
- Actualizar README, enlaces de aspectos y C4 para la nueva estructura; completar arc42 de despliegue.
- Publicar URL de despliegue, procedimiento reproducible, logs estructurados, métricas y costo.
- Registrar la asignación S10, la línea base, ADR y experimento con resultados.
- Actualizar docs/ia.md, auditar propiedad de datos y decidir sobre componente generativo.
- Corregir configuración de expiración JWT: [app/core/config.py:10](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/config.py#L10) devuelve texto y [app/core/security.py:10](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/security.py#L10) lo pasa a timedelta(minutes=...). Hallazgo estático; no se ejecutó.
- Verificar correspondencia de las identidades del historial con los integrantes.

### Hallazgos cerrados o sustituidos con evidencia actual

- El workflow actual coloca preparación de Python y pruebas antes del despliegue mediante needs: test: [.github/workflows/ci.yml:7–26](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/.github/workflows/ci.yml#L7-L26). Es una mejora tardía; el run aún falla y no cierra CI.
- Aparecen firmas adicionales en el historial actual; se retira la afirmación categórica antigua de que solo una persona ha contribuido. No se atribuye por nombre una firma a una persona.

## Para completar antes del cierre

Primero recuperen el pipeline y hagan que incluya también las pruebas de contratos, préstamos y recursos. Revisen la conversión de la duración del token a número, actualicen documentación y configuración de arranque y publiquen la URL del entorno. Para el reto, falta identificar la asignación, medir línea base y resultado y añadir observabilidad y costo. La defensa queda pendiente del docente.

## Tres preguntas para la sustentación

1. ¿Cómo evitarían dos préstamos simultáneos del mismo recurso y qué prueba o métrica evidencia que el control funciona?
2. ¿Qué servidor y base de datos sostienen el despliegue y cuál es su costo mensual y límite de capacidad?
3. ¿Qué decisión cambiarían después de comparar la línea base con el experimento del escenario asignado?

## Delta S5→S10 (sin recalificar entregas previas)

Se verificó por Git la base S5 publicada `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849` contra la punta `d17c9eb241e56755d48b022dc00ddb865e40c391`: 11 commits. [Comparación inmutable](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/compare/7cfb8729db79435bf9de7d3975a9a3bd7ac5b849...d17c9eb241e56755d48b022dc00ddb865e40c391). Las filas de decisión, implementación y evolución usan este delta como contexto, sin volver a calificar S5–S9.

Cambios documentales contrastados:

- docs/adr/0003-integracion-sincrona.md | 60 +++++++++++++++++++++++++++++++++++
- docs/c4/C2.md                         | 21 ++++++++----
- 2 files changed, 75 insertions(+), 6 deletions(-)

</details>
