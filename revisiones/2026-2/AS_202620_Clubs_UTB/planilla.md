# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Clubs UTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Hollman Jose De Orta Gonzalez (`deortahollman-star`) · Josh Robinson Ortega Castellon (`Josh4OP`) · Diego Andres Ramos De Avila (`Zavod Dev`, atribución sin confirmar) · Luis Daniel Salas Reyes (`Luis-Salas-Reyes`); ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | URL pública vigente no localizada; despliegue No verificado. Ver [S10](semana-10-corte2.md). |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `399565f527b633c49a71ac9b8a7f99daa85191d4` · 2026-10-04T23:47:05-05:00 | 6/10 | 3.4 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `cd0ad9c64925863ed5067ed53da7f3c6dcf09895` · 2026-10-05T00:46:29-05:00 | 2/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 8 | S8 | `652f78b7` (2026-09-27T23:39:11-05:00) | 5/10 | 3.0 (provisional; 2 filas de despliegue diferidas por decisión docente) | si |
| 7 | S7 | `dc211b8` (2026-09-20T23:56:51-05:00) | 8/10 | 4.2 | si |
| 6 | S6 | `743cc1f` (2026-09-13T23:55:10-05:00) | 6/8 | 4.0 (prelim.) | si |
| 5 | CORTE1 | `4ede977` (2026-09-06T22:41:55-05:00) | 8/12 | 3.7 | si |
| 4 | S4 | `91323d6` (2026-08-30T23:21:56-05:00) | 9/10 | 4.6 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `c92595ed` · 2026-08-09T13:25:24-05:00 | 2/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `69cfe68f` · 2026-08-16T18:33:10-05:00 | 7/9 | no se publica | sí |
| 3 | S3 | `5bf86ea` (2026-08-23T23:05:10-05:00) | 6/9 | 3.7 | si |

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Corregir los dos workflows fallidos y publicar evidencia del hash con SonarCloud/Quality Gate. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar enlaces de U2/U3 y medir disponibilidad/rendimiento: un health fijo no comprueba el proveedor. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Para S10, aportar consigna oficial, URL pública y línea base reproducible; contrastar resultados con el umbral. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Validar autenticación con token real, comportamiento sin JWKS y control de roles; resolver exposición pública de autor_id antes de declarar seguridad completa. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Preservar evidencia exacta del defecto, su corrección y las pruebas, sin incorporar el cambio tardío a S9. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Se incorporó decisión explícita de no incorporar LLM; [docs/adr/0005-no-incorporacion-llm.md:25–38](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/adr/0005-no-incorporacion-llm.md#L25-L38). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Se documentaron auditoría y procedimiento de mutación para health; [docs/ia.md:21–31](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/ia.md#L21-L31). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| En la punta, el caso de uso ya recibe autor_id explícito y el router lo toma de autenticación; [backend/src/linkclub/application/use_cases/crear_publicacion.py:10–35](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/backend/src/linkclub/application/use_cases/crear_publicacion.py#L10-L35). Corrección posterior al cierre S9. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/aspectos.md` sin la tabla de 8 columnas del curso | S1 | sí (en S3 rompe el enlace hacia el ADR) | Ver feedback S1/S2 y S3 |
| Ficha del problema sin tensiones de calidad | S1 | sí | Ver feedback S1/S2 |
| Estructura con desviaciones: `docs/C4/` en mayúscula; en S3 aparece `docs/adr/.temp` residual | S1 (C4), S3 (.temp) | sí | Ver feedback S1/S2 y S3 |
| `docs/ia.md` sin usos reales ni rechazos, sin commits en S2 ni S3 | S2 | sí | Ver feedback S1/S2 y S3 |
| Sin esqueleto ejecutable al cierre: `main.py` y `test_health.py` vacíos en `5bf86ead1`, README sin comando de arranque; el esqueleto real llegó TARDÍO (`8d69f62`, 00:21, 21 min después del cierre) | S3 | sí (llegó fuera del cierre) | Ver feedback S3 |
| ADR no alcanzable desde `aspectos.md` ni desde el escenario U2 | S3 | sí | Ver feedback S3 |
| Josh sin commits en S3 (primera revisión) | S3 | cerrado: `5bf86ea` (23:05) firmado por Josh Ortega, mismo correo que Josh4OP | Contribución 4/4 en S3 |
| Arranque con un solo comando en README | S4 | si | |
| Análisis estático en SonarCloud | S4 | si | |
| Código del contenedor Flutter pendiente (esperado para fases siguientes) | S4 | si | |
| Etiqueta corte-1 ausente | S5 | sí (al cierre de S5 sigue sin existir) | Se calificó el último commit ≤ cierre (`4ede977c`); se les dijo que deben crear la etiqueta antes del próximo corte. |
| ADR del reto no creado | S5 | sí | Solo existe el ADR-0001 de arquitectura hexagonal; no hay ADR de una restricción nueva. |
| Diagnóstico y línea base no documentados | S5 | sí | Sin restricción diagnosticada ni cifra de línea base en ningún artefacto. |
| Cambio no implementado | S5 | sí (parcial) | Se agregó un endpoint de publicaciones con prueba y CI en verde, pero no está vinculado a ninguna restricción diagnosticada. |
| Medición no aportada | S5 | sí | — |
| Tabla de aspectos incompleta | S5 | sí | Sin columna Evidencia; la mayoría de filas siguen en "Pendiente". |
| Registro IA sin entrada de S5 | S5 | sí | `docs/ia.md` no tiene commits desde S3-S4. |
| Análisis estático SonarCloud ausente | S5 | sí | No se verificó badge ni run de SonarCloud en el estado revisado. |
| ADR-0001 editado después de aceptado (`c6c46e3`, 30/08) sin ADR de reemplazo | S5 | sí | Corrige el hallazgo de S4 ("sin reescrituras"): sí hay una edición posterior a la aceptación; se les pidió escribir un ADR nuevo si la decisión cambia. |
| README con arranque y pruebas documentado después del cierre (commits 7017270, 91323d6). | S3 | no (resuelto tarde) | — |
| Workflow .github/workflows/backend-tests.yml añadido tras el cierre. | S3 | no (resuelto tarde) | — |
| docs/C4 renombrado a docs/c4 y docs/aspectos.md actualizado después del cierre. | S3 | no (resuelto tarde) | — |
| Corrección de nombres de archivos y enlaces en docs (commits 46c7fa3, 993f51d). | S3 | no (resuelto tarde) | — |
| docs/aspectos.md aún sin las 8 columnas del contrato ni enlace al ADR. | S3 | si | |
| docs/ia.md sin registros concretos de uso de IA. | S3 | si | |
| ADR con nombre fuera de la convención kebab-case. | S3 | si | |
| Sin evidencia de que la prueba automatizada esté en verde en CI. | S3 | si | |
| Archivo basura docs/adr/.temp aún presente. | S3 | si | |
| Crear correcciones.md en la raíz del estado calificado. | S5 | si | |
| Completar la trazabilidad de correcciones para S1-S4. | S5 | si | |
| Actualizar la tabla de aspectos con código y pruebas para U1, U3, C1, C2, C3. | S5 | si | |
| Actualizar README para reflejar el estado actual del proyecto. | S5 | si | |
| Mapa de contextos con relaciones tipificadas | S6 | si | |
| Tabla módulo a datos con dueño único | S6 | si | |
| Lista de violaciones con plan de corrección | S6 | si | |
| arc42 sección 8 | S6 | si | |
| C4 nivel 3 y ADR de reajuste | S6 | si | |
| Completar secciones 07 y 11 de arc42 | S6 | si | |
| SonarCloud en pipeline | S6 | si | |
| NC-01: datos de clubes hardcodeados en frontend/linkclub/lib/clubs_page.dart (docs/arc42/lista_errores.md). | S7 | si | |
| NC-02: sin manejo de errores de conexión en backend (docs/arc42/lista_errores.md). | S7 | si | |
| docs/arc42/tabla_modulo.md desalineada con los tres contextos vigentes, según ADR 0002 y arc42 §8.3. | S7 | si | |
| Secciones 07 y 11 de arc42 ausentes. | S7 | si | |
| Contrato de API, prueba de contrato en el pipeline y ADR de estrategia de integración: entregados en S7 y releídos; faltan el run en rojo del hash calificado y el etiquetado del C4 nivel 2. | S7 | si | |
| d2d1450 'Update IA usage log for week 6' (2026-09-15T10:14:52-05:00), único cambio en diff_desde_cierre: docs/ia.md, con run 'Backend tests' success del 2026-09-15T15:14:55Z (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/34987143230). | S6 | no (resuelto tarde) | — |
| NC-02: ausencia de manejo de errores de conexión en el backend. | S6 | si | |
| Enlace roto a docs/adr/0002-ajuste-contextos-publicaciones.md y documentos que declaran pendiente una alineación ya aplicada. | S6 | si | |
| Análisis estático SonarCloud ausente del pipeline y sin URL pública con Quality Gate. | S6 | si | |
| docs/aspectos.md con celdas 'Pendiente' y sin columna de evidencia; sin mapeo a los contextos del mapa. | S6 | si | |
| Secciones arc42 07 y 11 no presentes en el repositorio. | S6 | si | |
| Actualizar docs/arc42/tabla_modulo.md a los tres contextos vigentes (abierto en ADR 0002 y arc42 §8.3). | S7 | si | |
| Cerrar NC-01 y NC-02 de docs/arc42/lista_errores.md. | S7 | si | |
| Eliminar el ADR duplicado y renombrar 0003 según NNNN-kebab-case, corrigiendo el enlace roto. | S7 | si | |
| Aportar análisis SonarCloud público con Quality Gate y configuración en el repositorio. | S7 | si | |
| Aportar el run del workflow de contrato y la evidencia de fallo por cambio incompatible. | S7 | si | |
| Completar las secciones 07 y 11 de arc42 y etiquetar con protocolo y formato el C4 nivel 2 (la correspondencia contrato↔código quedó verificada). | S7 | si | |
| Ninguno: commits_tardios_post_cierre está vacío y no hay commits nuevos desde el cierre anterior. | S8 | no (resuelto tarde) | — |
| URL pública del sistema y comprobación externa de /health | S8 | si | |
| Infraestructura como código versionada | S8 | si | |
| arc42 §7 (vista de despliegue) y §11 | S8 | si | |
| ADR por decisión de plataforma con alternativa descartada | S8 | si | |
| Estimación de costo mensual y restricciones de costo y tarjeta en §2 | S8 | si | |
| Métrica consultable ligada a un escenario de calidad | S8 | si | |
| Logs estructurados con campos | S8 | si | |
| Runs de CI y análisis público de SonarCloud | S8 | si | |
| Corregir nombres y duplicados de ADR y el enlace roto de la sección 9 | S8 | si | |
| Resolver NC-01 y NC-02 de docs/arc42/lista_errores.md | S8 | si | |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público de ISCOUTB/AS_202620_Clubs_UTB; master declarado por el remoto; [README.md:1–10](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/README.md#L1-L10). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes, incluyendo arc42 01–12, C4, ADR, aspectos e IA; [docs/aspectos.md:26–34](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/aspectos.md#L26-L34). |
| Estado calificado identificable | Cumple | Punta master cd0ad9c64925863ed5067ed53da7f3c6dcf09895 de 2026-10-05T00:46:29-05:00; preliminar anterior al cierre S10, posterior al cierre S9. |
| Nombres de ADR según la convención | No cumple | [docs/adr/0003- integacion rest openapi.md:1–8](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/adr/0003-%20integacion%20rest%20openapi.md#L1-L8) conserva espacios y no usa kebab-case. La copia duplicada 0003-API.md fue eliminada en S9. |
| ADR aceptados no reescritos | No verificado | Se observan revisiones de ADR previos; sin completar contraste del estado de aceptación en toda la historia no se certifica inmutabilidad. No se presume cerrado el arrastre anterior. |
| docs/ia.md al día para la semana | Cumple | Entrada y sección S9 nuevas con aceptación, corrección y rechazo técnico explícitos; [docs/ia.md:21–31](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/ia.md#L21-L31). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | Los dos workflows de la punta siguen failure; no se acredita SonarCloud ni Quality Gate. [.github/workflows/backend-tests.yml:13–30](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/.github/workflows/backend-tests.yml#L13-L30). |
| Sin credenciales en el repositorio ni en el historial | No verificado | Sin credenciales reales en el snapshot; el historial completo no se certificó. [infra/terraform/provider.tf:11–13](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/infra/terraform/provider.tf#L11-L13) lee el token de archivo externo y [infra/terraform/resource.tf:11–18](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/infra/terraform/resource.tf#L11-L18) usa placeholder. |
| Contribución de todos los integrantes | No verificado | Seis firmas de autor, 134 commits agregados, para cuatro integrantes declarados. Hay variantes de identidad; sin mapeo comprobable completo no se infiere quién falta ni se suman firmas como personas. Punta actual: 6 firmas y 137 commits agregados; no equivalen automáticamente a personas. |

## Contribución por integrante

Actualización agregada del 2026-10-06: Seis firmas observadas, 134 commits agregados en S9. Correspondencia de variantes con cuatro integrantes pendiente de validación; sin correos publicados. En HEAD: 6 firmas y 137 commits agregados.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Diego Andres Ramos De Avila | `Zavod Dev` (atribución sin confirmar) | 2 (S3) | — | — | Matriz comparativa y corrección de enlaces |
| Luis Daniel Salas Reyes | `Luis-Salas-Reyes` | 2 (S3) | — | — | Autor del ADR y su revisión |
| Hollman Jose De Orta Gonzalez | `deortahollman-star` | 1 (S3) | — | — | Matriz comparativa |
| Josh Robinson Ortega Castellon | `Josh4OP` (firma también como «Josh Ortega», mismo correo) | 1 (S3) | — | — | Carpetas hexagonales (`5bf86ea`) y esqueleto ejecutable (`8d69f62`, tardío) |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- ¿Cómo se recuperan las escrituras si Supabase rota claves o JWKS no responde, y cómo distinguirán 401 de 503?
- ¿Qué costo y límite de llamadas evita verificar JWKS localmente, y qué costo de seguridad asumen por tokens revocados?
- Tras medir rutas protegidas, ¿qué cambiarían para impedir que un usuario autenticado publique en un club ajeno?
