# Evidencia S9 definitiva · Clubs UTB

Revisión actualizada tras el cierre del **2026-10-05T05:00:00Z** (domingo a medianoche COT).

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_Clubs_UTB](https://github.com/ISCOUTB/AS_202620_Clubs_UTB) |
| Rama remota principal | `master` |
| Base S5 del segundo corte | `4ede977c7cccc335d878019ce06cba2e23cf76d2` |
| Base S8 | `652f78b76198ca854f7b3e79b910506e65ee4418` |
| Estado revisado | `399565f527b633c49a71ac9b8a7f99daa85191d4` en `origin/master` (2026-10-04T23:47:05-05:00) |
| S9 congelada | `399565f527b633c49a71ac9b8a7f99daa85191d4` · 2026-10-04T23:47:05-05:00 |
| Punta actual / S10 preliminar | `cd0ad9c64925863ed5067ed53da7f3c6dcf09895` · 2026-10-05T00:46:29-05:00 |
| Comprobación | 2026-10-06T21:20:55Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Matriz S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | No cumple | Se audita health de la línea base sin cambio de su implementación o prueba en S9; [docs/ia.md:23–31](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/ia.md#L23-L31). El único delta backend añade autor_id sin definirlo, [backend/src/linkclub/application/use_cases/crear_publicacion.py:10–34](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/backend/src/linkclub/application/use_cases/crear_publicacion.py#L10-L34); la implementación JWT completa llegó después del cierre. |
| Cadena completa navegable para esa porción | No cumple | U2 enlaza ADR inexistente adr/0004-supabase.md y nombres de archivos sin enlaces de código; U3 deja Código/Pruebas Pendiente. No hay cadena completa hasta medición; [docs/aspectos.md:28–34](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/aspectos.md#L28-L34). |
| ADR con la decisión argumentada por el equipo | No cumple | No hay nuevo ADR de la porción health auditada. ADR-0005 sí argumenta no incorporar LLM, que se acredita en su criterio específico; [docs/adr/0005-no-incorporacion-llm.md:9–31](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/adr/0005-no-incorporacion-llm.md#L9-L31). |
| Prueba que falla ante el defecto que cubre | Cumple | La ficha admite procedimiento documentado: el equipo describe mutar status a caido_por_error y obtener AssertionError, [docs/ia.md:30–31](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/ia.md#L30-L31). La prueba real exige exactamente status=ok, [backend/tests/test_health.py:12–15](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/backend/tests/test_health.py#L12-L15). Se acredita ese procedimiento limitado, no un run externo ni una ejecución del revisor. |
| Medición del escenario asociado | No cumple | La evidencia U2 es una mutación funcional, no medición de disponibilidad o latencia contra umbral; [docs/aspectos.md:30–32](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/aspectos.md#L30-L32). El adaptador health devuelve ok fijo, sin consultar Supabase; [backend/src/linkclub/adapters/outbound/persistence/in_memory_status_adapter.py:1–6](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/backend/src/linkclub/adapters/outbound/persistence/in_memory_status_adapter.py#L1-L6). |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | La sección S9 distingue estructura aceptada, import directo corregido y dependencia/credenciales rechazadas con motivo; [docs/ia.md:21–31](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/ia.md#L21-L31). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | Auditoría nueva identifica propuesta que cruzaba router→Supabase y la separación mediante puertos/adaptador; [docs/ia.md:27–28](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/ia.md#L27-L28). El código final respeta esa separación, [backend/src/linkclub/adapters/inbound/api/health_router.py:1–12](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/backend/src/linkclub/adapters/inbound/api/health_router.py#L1-L12). Alcance: estructura estática; el adaptador en memoria no prueba disponibilidad de BD. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | El periodo S9 no añade dependencias backend; documenta rechazo de supabase-fastapi-health-checker tras PyPI, [docs/ia.md:28–28](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/ia.md#L28-L28). La consulta de lectura https://pypi.org/pypi/supabase-fastapi-health-checker/json devolvió 404. Se acredita el descarte auditado, sin convertir ausencia de paquetes nuevos en falla. |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | No se detectan credenciales reales en código/documentación/ejemplos del hash. Terraform usa token externo y password de ejemplo; [infra/terraform/provider.tf:11–13](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/infra/terraform/provider.tf#L11-L13), [infra/terraform/resource.tf:11–18](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/infra/terraform/resource.tf#L11-L18). Sin .env versionado. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | ADR-0005 decide no incorporar componente generativo y analiza alternativas, costo, latencia y consecuencias; [docs/adr/0005-no-incorporacion-llm.md:13–38](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/adr/0005-no-incorporacion-llm.md#L13-L38). |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público de ISCOUTB/AS_202620_Clubs_UTB; master declarado por el remoto; [README.md:1–10](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/README.md#L1-L10). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes, incluyendo arc42 01–12, C4, ADR, aspectos e IA; [docs/aspectos.md:26–34](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/aspectos.md#L26-L34). |
| Estado calificado identificable | Cumple | Hash S9 congelado por fecha en master, indicado en encabezado; el commit posterior no se usa para calificar S9. |
| Nombres de ADR según la convención | No cumple | [docs/adr/0003- integacion rest openapi.md:1–8](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/adr/0003-%20integacion%20rest%20openapi.md#L1-L8) conserva espacios y no usa kebab-case. La copia duplicada 0003-API.md fue eliminada en S9. |
| ADR aceptados no reescritos | No verificado | Se observan revisiones de ADR previos; sin completar contraste del estado de aceptación en toda la historia no se certifica inmutabilidad. No se presume cerrado el arrastre anterior. |
| docs/ia.md al día para la semana | Cumple | Entrada y sección S9 nuevas con aceptación, corrección y rechazo técnico explícitos; [docs/ia.md:21–31](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/ia.md#L21-L31). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | Los dos workflows del hash S9 concluyen failure. [.github/workflows/backend-tests.yml:13–30](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/.github/workflows/backend-tests.yml#L13-L30) no invoca SonarCloud; no se encontró configuración ni análisis público con Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Sin credenciales reales en el snapshot; el historial completo no se certificó. [infra/terraform/provider.tf:11–13](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/infra/terraform/provider.tf#L11-L13) lee el token de archivo externo y [infra/terraform/resource.tf:11–18](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/infra/terraform/resource.tf#L11-L18) usa placeholder. |
| Contribución de todos los integrantes | No verificado | Seis firmas de autor, 134 commits agregados, para cuatro integrantes declarados. Hay variantes de identidad; sin mapeo comprobable completo no se infiere quién falta ni se suman firmas como personas. |

## Actions en el estado congelado

- [.github/workflows/backend-tests.yml: failure](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/37265056373), 2026-10-05T04:47:49Z, SHA exacto del estado indicado.
- [.github/workflows/contrato.yml: failure](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/37265055623), 2026-10-05T04:47:48Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Barrido de texto del snapshot: coincidencias de password en formularios y variables; token de Terraform se lee de archivo externo, database_password es placeholder y terraform.tfstate está vacío. No hay .env versionado. No se completó barrido exhaustivo de todos los blobs históricos; transversal No verificado.

## Estado global del proyecto (overall · punta actual)

La punta incorpora tarde la implementación JWT/JWKS, ADR-0006, pruebas y actualización contractual. Esto corrige el uso aislado de autor_id del snapshot S9, que lo referenciaba sin parámetro definido. La implementación tardía no altera la calificación congelada. El propio ADR advierte que autorización por rol, token de sesión real y latencia siguen pendientes. Los workflows continúan en rojo, y no se encontró URL pública del backend.

El delta S9 contiene 9 commits respecto de S8; hay 3 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Recuento y nota sugerida

**6 de 10 criterios Cumple. Nota sugerida: 3.4 = 1 + 4 × (6/10).** Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no integra este cálculo.

## Acciones prioritarias

- Corregir los dos workflows fallidos y publicar evidencia del hash con SonarCloud/Quality Gate.
- Completar enlaces de U2/U3 y medir disponibilidad/rendimiento: un health fijo no comprueba el proveedor.
- Para S10, aportar consigna oficial, URL pública y línea base reproducible; contrastar resultados con el umbral.
- Validar autenticación con token real, comportamiento sin JWKS y control de roles; resolver exposición pública de autor_id antes de declarar seguridad completa.
- Preservar evidencia exacta del defecto, su corrección y las pruebas, sin incorporar el cambio tardío a S9.

## Hallazgos cerrados con evidencia nueva

- Se incorporó decisión explícita de no incorporar LLM; [docs/adr/0005-no-incorporacion-llm.md:25–38](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/adr/0005-no-incorporacion-llm.md#L25-L38).
- Se documentaron auditoría y procedimiento de mutación para health; [docs/ia.md:21–31](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/399565f527b633c49a71ac9b8a7f99daa85191d4/docs/ia.md#L21-L31).
- En la punta, el caso de uso ya recibe autor_id explícito y el router lo toma de autenticación; [backend/src/linkclub/application/use_cases/crear_publicacion.py:10–35](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/cd0ad9c64925863ed5067ed53da7f3c6dcf09895/backend/src/linkclub/application/use_cases/crear_publicacion.py#L10-L35). Corrección posterior al cierre S9.
