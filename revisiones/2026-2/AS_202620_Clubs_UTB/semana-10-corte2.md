# Segundo corte S10 · avance preliminar · Clubs UTB

**Preliminar, no es cierre ni calificación final.** Cierre previsto: **2026-10-12T05:00:00Z**.

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_Clubs_UTB](https://github.com/ISCOUTB/AS_202620_Clubs_UTB) |
| Rama remota principal | `master` |
| Base S5 del segundo corte | `4ede977c7cccc335d878019ce06cba2e23cf76d2` |
| Base S8 | `652f78b76198ca854f7b3e79b910506e65ee4418` |
| Estado revisado | `cd0ad9c64925863ed5067ed53da7f3c6dcf09895` en `origin/master` (2026-10-05T00:46:29-05:00) |
| S9 congelada | `399565f527b633c49a71ac9b8a7f99daa85191d4` · 2026-10-04T23:47:05-05:00 |
| Punta actual / S10 preliminar | `cd0ad9c64925863ed5067ed53da7f3c6dcf09895` · 2026-10-05T00:46:29-05:00 |
| Comprobación | 2026-10-06T21:20:55Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Evolución desde S5 hasta la punta

Base tomada del informe S5 publicado y resuelta por Git, sin etiquetas: `4ede977c7cccc335d878019ce06cba2e23cf76d2`. En el delta S5→HEAD cambian 190 rutas no PDF (conteo de árboles; no mide mérito). Desde S5 cambian la separación de contextos/contrato API, infraestructura Supabase y cliente Flutter; en HEAD se añade JWT/JWKS y pruebas de autenticación. La última parte es posterior al cierre S9 y sí forma parte de la vista preliminar S10.

## Escenario operativo asignado

No verificado. Se revisaron README, ADR, aspectos y arc42 §10 en la punta. U3 de autenticación y U2 de disponibilidad tienen evidencia, pero no hay constancia de que constituyan la asignación operativa docente S10. No se los adopta como consigna por inferencia.

## Matriz de evidencia S10

Se omite la fila de PDF de dos páginas por exclusión docente. Quedan 12 filas observables o pendientes; este recuento no es una fórmula de nota.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master identificada en encabezado, posterior a S9 y anterior al cierre futuro. |
| Despliegue accesible en el momento de la revisión | No verificado | README solo declara URL local de health. No se localizó URL pública del MVP que permita comprobar accesibilidad; [README.md:124–140](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/README.md#L124-L140). |
| Hipótesis, montaje, variables y umbral declarados | No verificado | U1/U2/U3 son escenarios generales; no se localizó asignación oficial S10; [docs/arc42/10_requisitos_de_calidad.md:83–88](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/docs/arc42/10_requisitos_de_calidad.md#L83-L88). |
| Línea base medida y reproducible | No verificado | No hay línea base identificada para el reto asignado. El ADR tardío documenta defecto de autenticación y pruebas, no un experimento operativo completo; [docs/adr/0006-validacion-token-jwt-supabase.md:9–16](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/docs/adr/0006-validacion-token-jwt-supabase.md#L9-L16). |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | ADR-0006 compara JWKS local, consulta remota y HS256 con costos y riesgos, pero está Propuesto y no se ha vinculado a la consigna asignada; [docs/adr/0006-validacion-token-jwt-supabase.md:18–41](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/docs/adr/0006-validacion-token-jwt-supabase.md#L18-L41). |
| Respuesta implementada o configurada sobre el MVP | No verificado | Hay cambio real tardío: puerto AuthPort, adaptador JWKS y require_auth; falta confirmar si responde al reto S10 y probarlo desplegado. [backend/src/linkclub/adapters/inbound/api/auth_dependency.py:1–33](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/backend/src/linkclub/adapters/inbound/api/auth_dependency.py#L1-L33). |
| Resultado contrastado con el umbral | No verificado | El equipo documenta 1/1 rutas de escritura protegidas y 21 pruebas; no equivale al resultado del escenario asignado ni token real, expresamente pendiente; [docs/adr/0006-validacion-token-jwt-supabase.md:61–67](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/docs/adr/0006-validacion-token-jwt-supabase.md#L61-L67). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | Ambos pipelines de HEAD en failure. Health devuelve constante; sin logs estructurados ni métrica observable ligada al reto; [backend/src/linkclub/main.py:1–20](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/backend/src/linkclub/main.py#L1-L20), [backend/src/linkclub/adapters/outbound/persistence/in_memory_status_adapter.py:1–6](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/backend/src/linkclub/adapters/outbound/persistence/in_memory_status_adapter.py#L1-L6). |
| Secretos protegidos | Cumple | Snapshot actual sin secretos reales; el adaptador recibe SUPABASE_URL del entorno y trabaja con JWKS público; [backend/src/linkclub/adapters/inbound/api/auth_dependency.py:18–20](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/backend/src/linkclub/adapters/inbound/api/auth_dependency.py#L18-L20). |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | La trazabilidad conserva enlaces rotos y documentación parcial; U2 apunta a ADR inexistente. ADR-0006 admite autorización por rol pendiente y exposición de autor_id por confirmar; [docs/aspectos.md:28–34](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/docs/aspectos.md#L28-L34), [docs/adr/0006-validacion-token-jwt-supabase.md:50–55](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/docs/adr/0006-validacion-token-jwt-supabase.md#L50-L55). |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | El ADR nuevo complementa seguridad, pero no se identificó decisión anterior confirmada/reemplazada por medición del reto asignado; [docs/adr/0006-validacion-token-jwt-supabase.md:69–75](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/docs/adr/0006-validacion-token-jwt-supabase.md#L69-L75). |
| Sustentación del reto sobre el entorno desplegado | No verificado | Pendiente de sustentación docente con despliegue y pipeline en vivo. |

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
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público de ISCOUTB/AS_202620_Clubs_UTB; master declarado por el remoto; [README.md:1–10](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/README.md#L1-L10). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes, incluyendo arc42 01–12, C4, ADR, aspectos e IA; [docs/aspectos.md:26–34](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/aspectos.md#L26-L34). |
| Estado calificado identificable | Cumple | Punta master cd0ad9c64925863ed5067ed53da7f3c6dcf09895 de 2026-10-05T00:46:29-05:00; preliminar anterior al cierre S10, posterior al cierre S9. |
| Nombres de ADR según la convención | No cumple | [docs/adr/0003- integacion rest openapi.md:1–8](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/adr/0003-%20integacion%20rest%20openapi.md#L1-L8) conserva espacios y no usa kebab-case. La copia duplicada 0003-API.md fue eliminada en S9. |
| ADR aceptados no reescritos | No verificado | Se observan revisiones de ADR previos; sin completar contraste del estado de aceptación en toda la historia no se certifica inmutabilidad. No se presume cerrado el arrastre anterior. |
| docs/ia.md al día para la semana | Cumple | Entrada y sección S9 nuevas con aceptación, corrección y rechazo técnico explícitos; [docs/ia.md:21–31](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/ia.md#L21-L31). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | Los dos workflows de la punta siguen failure; no se acredita SonarCloud ni Quality Gate. [.github/workflows/backend-tests.yml:13–30](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/.github/workflows/backend-tests.yml#L13-L30). |
| Sin credenciales en el repositorio ni en el historial | No verificado | Sin credenciales reales en el snapshot; el historial completo no se certificó. [infra/terraform/provider.tf:11–13](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/infra/terraform/provider.tf#L11-L13) lee el token de archivo externo y [infra/terraform/resource.tf:11–18](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/infra/terraform/resource.tf#L11-L18) usa placeholder. |
| Contribución de todos los integrantes | No verificado | Seis firmas de autor, 134 commits agregados, para cuatro integrantes declarados. Hay variantes de identidad; sin mapeo comprobable completo no se infiere quién falta ni se suman firmas como personas. Punta actual: 6 firmas y 137 commits agregados; no equivalen automáticamente a personas. |

## Actions en la punta actual

- [.github/workflows/backend-tests.yml: failure](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/37269279731), 2026-10-05T05:46:37Z, SHA exacto del estado indicado.
- [.github/workflows/contrato.yml: failure](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/37269279042), 2026-10-05T05:46:36Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Barrido de texto del snapshot: coincidencias de password en formularios y variables; token de Terraform se lee de archivo externo, database_password es placeholder y terraform.tfstate está vacío. No hay .env versionado. No se completó barrido exhaustivo de todos los blobs históricos; transversal No verificado.

## Estado global del proyecto (overall)

La punta incorpora tarde la implementación JWT/JWKS, ADR-0006, pruebas y actualización contractual. Esto corrige el uso aislado de autor_id del snapshot S9, que lo referenciaba sin parámetro definido. La implementación tardía no altera la calificación congelada. El propio ADR advierte que autorización por rol, token de sesión real y latencia siguen pendientes. Los workflows continúan en rojo, y no se encontró URL pública del backend.

El delta S9 contiene 9 commits respecto de S8; hay 3 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Antes del cierre

- Corregir los dos workflows fallidos y publicar evidencia del hash con SonarCloud/Quality Gate.
- Completar enlaces de U2/U3 y medir disponibilidad/rendimiento: un health fijo no comprueba el proveedor.
- Para S10, aportar consigna oficial, URL pública y línea base reproducible; contrastar resultados con el umbral.
- Validar autenticación con token real, comportamiento sin JWKS y control de roles; resolver exposición pública de autor_id antes de declarar seguridad completa.
- Preservar evidencia exacta del defecto, su corrección y las pruebas, sin incorporar el cambio tardío a S9.

## Tres preguntas de sustentación

1. ¿Cómo se recuperan las escrituras si Supabase rota claves o JWKS no responde, y cómo distinguirán 401 de 503?
2. ¿Qué costo y límite de llamadas evita verificar JWKS localmente, y qué costo de seguridad asumen por tokens revocados?
3. Tras medir rutas protegidas, ¿qué cambiarían para impedir que un usuario autenticado publique en un club ajeno?
