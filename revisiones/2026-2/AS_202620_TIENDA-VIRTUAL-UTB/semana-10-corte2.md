# Segundo corte S10 · revisión preliminar · Tienda virtual UTB

**Preliminar; no es la calificación del corte.** Se revisa la punta actual, con cierre futuro **2026-10-12T05:00:00Z**. S9 queda congelada de forma independiente.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB |
| Rama principal remota | `main` |
| Base S5 publicada | `3d732d740053c8f10ad4c618d3031024c72630bc` |
| Base S8 | `858e78f9e34ee4e205bdc84982ed8b04bd0dbb0d` |
| Estado revisado | `76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33` en `origin/main` (2026-10-04T18:07:32-05:00) |
| Punta actual / S10 preliminar | `76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33` · 2026-10-04T18:07:32-05:00 |
| Observado | 2026-10-06T21:28:33.520983Z |

## Alcance y método

Revisión de archivos y del historial mediante Git, sin ejecutar código, pruebas, scripts ni despliegues de estudiantes. Se consultó una vez el listado de runs de GitHub Actions; un run verde se limita a los pasos que declara su workflow y no acredita la sustentación, el flujo desplegado ni un Quality Gate omitido. No se consultaron etiquetas. No se leyó ningún PDF; el criterio PDF se excluye por decisión docente, sin penalización. Las mediciones documentadas se atribuyen al equipo y no se presentan como ejecuciones del revisor.

## Escenario operativo asignado

**No verificado.** No hay constancia de la asignación operativa oficial S10 en README, ADR o documentación de experimentos. AC-04 es un escenario de calidad medido en S9. Fuente inspeccionada: [README.md:100–140](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/README.md#L100-L140). No se equipara un escenario de calidad genérico ni el ejercicio S9 con la asignación oficial. Las filas que dependen de esa correspondencia permanecen abiertas hasta obtener la consigna y contrastarla.

## Matriz de preparación S10

El renglón «PDF de dos páginas» se omite expresamente por exclusión docente: quedan **12 filas**, sin fórmula semanal de calificación.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta main y fecha del encabezado anteriores al cierre futuro; estado preliminar. |
| Despliegue accesible en el momento de la revisión | No verificado | [README.md:116–121](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/README.md#L116-L121) indica que el dominio Dokploy aún no está registrado. No hay URL vigente verificable; no se probó flujo ni salud externa. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | [docs/entrega-cadena-ia.md:54–85](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/entrega-cadena-ia.md#L54-L85) caracteriza AC-04 local, pero no identifica la consigna S10; falta correspondencia oficial. |
| Línea base medida y reproducible | No verificado | El resultado local de AC-04 no es una línea base antes/después del reto asignado: [docs/entrega-cadena-ia.md:61–85](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/entrega-cadena-ia.md#L61-L85). |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0008-separar-catalogo-inventario.md:3–6](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0008-separar-catalogo-inventario.md#L3-L6) está pendiente de decisión del equipo; [docs/adr/0007-despliegue-dokploy.md:7–34](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0007-despliegue-dokploy.md#L7-L34) documenta infraestructura, sin vínculo verificable al reto S10. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [backend/app/modules/inventory/repository.py:1–13](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/backend/app/modules/inventory/repository.py#L1-L13) y [docs/c4/container.md:22–32](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/c4/container.md#L22-L32) muestran incremento real; no se puede afirmar que responde al escenario asignado aún desconocido. |
| Resultado contrastado con el umbral | No verificado | La medición local S9 tiene umbral; falta experimento de respuesta al reto asignado y contraste con su línea base. [docs/entrega-cadena-ia.md:79–85](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/entrega-cadena-ia.md#L79-L85). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | CI de pruebas verde: [run](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/37242837748). [README.md:135–140](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/README.md#L135-L140) declara salud, logs JSON y métricas; no hay dominio vigente ni métrica validada contra la asignación S10. |
| Secretos protegidos | Cumple | Barrido estático del árbol de este hash, incluidos ejemplos y Markdown, sin credenciales reales detectadas. La coincidencia de [compose.yaml:4–8](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/compose.yaml#L4-L8) es interpolación obligatoria de entorno; los valores de prueba de [docs/entrega-cadena-ia.md:125–125](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/entrega-cadena-ia.md#L125-L125) están identificados como efímeros. No prueba revocación de credenciales compartidas fuera de Git. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/c4/container.md:22–32](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/c4/container.md#L22-L32) refleja inventario; [README.md:88–89](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/README.md#L88-L89) y [README.md:197–198](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/README.md#L197-L198) aún lo describen vacío; ADR 0008 pendiente. Representación del MVP parcialmente desactualizada. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0007-despliegue-dokploy.md:3–12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0007-despliegue-dokploy.md#L3-L12) reemplaza decisiones de plataforma, pero no aporta evidencia medida del reto S10 que motive el cambio. |
| Sustentación del reto sobre el entorno desplegado | No verificado | La sesión, defensa en despliegue y ejecución del pipeline en vivo corresponden al docente. |

## Rúbrica específica de cinco criterios

| Criterio | Nivel sugerido | Puntaje | Evidencia y límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | No hay constancia de la asignación operativa oficial S10 en README, ADR o documentación de experimentos. AC-04 es un escenario de calidad medido en S9. |
| Decisión e implementación | No verificado | Pendiente | Hay implementación y alternativas en ADR 0008, pero ratificación y correspondencia con la consigna pendientes. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Pruebas verdes y observabilidad en código; sin URL actual para comprobar operación ni escenario oficialmente identificado. |
| Evolución arquitectónica trazable | Básico | 0.60 | C4/contratos/arc42 avanzan, pero README conserva inventario como vacío y el ADR de separación no está aceptado. |
| Sustentación del reto | Lo fija el docente | Pendiente | Sustentación pendiente. |

**No se publica total final.** La escala de cada criterio es 0,00 / 0,60 / 0,80 / 1,00; la sustentación queda a cargo del docente, con entorno desplegado y pipeline en vivo. Las celdas pendientes no equivalen a cero. S6–S9 no se recalifican por existir.

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público correcto del repositorio vigente ISCOUTB; [README.md:1–3](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/README.md#L1-L3). |
| Estructura mínima presente | Cumple | Árbol Git con README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md; [README.md:224–228](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/README.md#L224-L228). |
| Estado calificado identificable | Cumple | Rama main; hash y fecha exactos del encabezado, último commit ≤ cierre, sin etiquetas. |
| Nombres de ADR según la convención | Cumple | ADR 0001–0009 siguen NNNN-titulo-en-kebab-case.md; [docs/adr/0008-separar-catalogo-inventario.md:3–6](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0008-separar-catalogo-inventario.md#L3-L6). |
| ADR aceptados no reescritos | No cumple | [docs/adr/0001-monolito-modular.md:19–35](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0001-monolito-modular.md#L19-L35): el historial confirma edición posterior a aceptación en e8ae57df776b3d171957f4d0c8a1e19cfb968ba5. El reemplazo 0003–0006 por 0007 sí está declarado en [docs/adr/0007-despliegue-dokploy.md:3–5](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0007-despliegue-dokploy.md#L3-L5), pero no cierra la reescritura histórica de 0001. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:26](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/ia.md#L26) añadida en el delta S9, con correcciones y descartes técnicos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [Pruebas del hash en success](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/37242837748); [.github/workflows/tests.yml:64–80](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/.github/workflows/tests.yml#L64-L80) omite el scanner si falta SONAR_TOKEN y [docs/pendientes.md:20–23](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/pendientes.md#L20-L23) aún solicita configurarlo. No se acredita run del scanner más Quality Gate público de la revisión; verde global no basta. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido del árbol sin credenciales reales y búsqueda histórica de patrones de alta especificidad sin incidentes confirmados. [compose.yaml:4–8](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/compose.yaml#L4-L8). Alcance estático; la rotación externa pendiente en [docs/pendientes.md:17–18](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/pendientes.md#L17-L18) debe verificarse por separado. |
| Contribución de todos los integrantes | No verificado | El historial presenta varias firmas y variantes; no hay correspondencia individual verificada suficiente para afirmar contribución de todos. No se atribuyen cuentas por semejanza de nombre. |

## Estado global del proyecto (overall)

Punta de la misma rama: `76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33` (2026-10-04T18:07:32-05:00). Hay **8 commits en el delta S8→S9** y **0 commits posteriores al cierre S9**. El nuevo incremento de inventario ya está presente en S9; no hay commits tardíos en la punta revisada. La migración documental a Dokploy reemplaza Vercel/Render/Neon, pero el dominio continúa pendiente. Las pruebas y mediciones documentadas son locales.



### Hallazgos abiertos

- Ratificar ADR 0008 y 0009 con decisión y razones propias del equipo; ambos se declaran propuestas.
- Registrar dominio público vigente y evidencias fechadas de salud/flujo Dokploy; el costo del servidor y backups está por confirmar.
- Completar SonarCloud: scanner realmente ejecutado y Quality Gate público de la revisión.
- Corregir contradicciones del README y pendientes que todavía presentan Inventario vacío.
- Precisar asignación S10 y registrar línea base, experimento, resultado y límites de validez.
- Confirmar correspondencia de autoría sin inferencias y verificar rotación de credenciales compartidas fuera del repositorio.

### Hallazgos cerrados o sustituidos con evidencia actual

- Cadena, prueba negativa, medición y auditoría S9 ya están documentadas y enlazadas: [docs/entrega-cadena-ia.md:7–23](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/entrega-cadena-ia.md#L7-L23).
- La migración a Terraform pendiente deja de ser el plan vigente: ADR 0007 reemplaza 0003–0006; no se declara ejecutado Terraform. [docs/adr/0007-despliegue-dokploy.md:3–12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0007-despliegue-dokploy.md#L3-L12).
- CI del hash actual pasa [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/37242837748); el cron keep-alive fue retirado. Esto no cierra SonarCloud ni demuestra despliegue.

## Para completar antes del cierre

Antes del corte, documenten cuál fue el escenario operativo asignado y midan una línea base reproducible en el entorno desplegado. Publiquen el dominio vigente de Dokploy, sus comprobaciones de salud y flujo, el resultado del experimento frente al umbral y el costo real de servidor y backups. La medición local de cinco usuarios es un insumo, pero todavía no acredita el reto asignado.

## Tres preguntas para la sustentación

1. ¿Qué ocurre si Catálogo responde y la lectura de Inventario falla o devuelve referencias distintas, y cómo se observa?
2. ¿Cuánto cuesta el host Dokploy con backups y cuál es el umbral de capacidad que obliga a ampliarlo?
3. Con 5/5 respuestas locales, ¿qué cambiarían en el experimento al pasar a PostgreSQL y al despliegue real antes de decidir?

## Delta S5→S10 (sin recalificar entregas previas)

Se verificó por Git la base S5 publicada `3d732d740053c8f10ad4c618d3031024c72630bc` contra la punta `76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33`: 20 commits. [Comparación inmutable](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/compare/3d732d740053c8f10ad4c618d3031024c72630bc...76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33). Las filas de decisión, implementación y evolución usan este delta como contexto, sin volver a calificar S5–S9.

Cambios documentales contrastados:

- docs/adr/0002-contrato-integracion-http.md   | 104 ++++++++++++++++
- docs/adr/0003-frontend-vercel.md             |  40 ++++++
- docs/adr/0004-api-contenedor-render.md       |  44 +++++++
- docs/adr/0005-postgres-neon.md               |  43 +++++++
- docs/adr/0006-infra-como-codigo-terraform.md | 175 +++++++++++++++++++++++++++
- docs/adr/0007-despliegue-dokploy.md          |  34 ++++++
- docs/adr/0008-separar-catalogo-inventario.md |  52 ++++++++
- docs/adr/0009-sin-componente-generativo.md   |  42 +++++++
- docs/arc42/arc42-template-EN.md              |  94 ++++++++++----
- docs/c4/container.md                         |  20 +--
- docs/c4/context.md                           |  10 +-
- 11 files changed, 626 insertions(+), 32 deletions(-)
