# Segundo corte S10 · revisión preliminar · uniTeam

**Preliminar; no es la calificación del corte.** Se revisa la punta actual, con cierre futuro **2026-10-12T05:00:00Z**. S9 queda congelada de forma independiente.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_uniTeam |
| Rama principal remota | `master` |
| Base S5 publicada | `dc14298c32a4fde0956266b0300063c24d7a9486` |
| Base S8 | `0f3da0f36f8cd7b829106667de88a56a1bc81f54` |
| Estado revisado | `6e04b35317a0a68d239ae85c71cd60e21982b195` en `origin/master` (2026-10-04T16:37:55-05:00) |
| Punta actual / S10 preliminar | `6e04b35317a0a68d239ae85c71cd60e21982b195` · 2026-10-04T16:37:55-05:00 |
| Observado | 2026-10-06T21:29:11.332360Z |

## Alcance y método

Revisión de archivos y del historial mediante Git, sin ejecutar código, pruebas, scripts ni despliegues de estudiantes. Se consultó una vez el listado de runs de GitHub Actions; un run verde se limita a los pasos que declara su workflow y no acredita la sustentación, el flujo desplegado ni un Quality Gate omitido. No se consultaron etiquetas. No se leyó ningún PDF; el criterio PDF se excluye por decisión docente, sin penalización. Las mediciones documentadas se atribuyen al equipo y no se presentan como ejecuciones del revisor.

## Escenario operativo asignado

**No verificado.** Los documentos identifican ESC-01/ESC-03 y la auditoría A-12, pero no contienen la consigna operativa oficialmente asignada al equipo para S10. Fuente inspeccionada: [docs/calidad/mediciones/mis-tareas-limite-contexto.md:3–5](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/mediciones/mis-tareas-limite-contexto.md#L3-L5). No se equipara un escenario de calidad genérico ni el ejercicio S9 con la asignación oficial. Las filas que dependen de esa correspondencia permanecen abiertas hasta obtener la consigna y contrastarla.

## Matriz de preparación S10

El renglón «PDF de dos páginas» se omite expresamente por exclusión docente: quedan **12 filas**, sin fórmula semanal de calificación.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master del encabezado anterior al cierre futuro; evaluación preliminar. |
| Despliegue accesible en el momento de la revisión | No verificado | [README.md:18–22](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/README.md#L18-L22). La aplicación pública devolvió HTTP 200 en 6,029311 s en la consulta iniciada 2026-10-06T21:21:59Z. La consulta de /health iniciada 2026-10-06T21:22:05Z agotó 25,001788 s sin bytes recibidos (curl 28, HTTP 000); es timeout de esta comprobación, no prueba concluyente de caída del servidor. Un segundo intento de /health iniciado 2026-10-06T21:27:21Z también agotó 90,000219 s sin bytes (HTTP 000). No se probó el flujo autenticado. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | [docs/calidad/mediciones/mis-tareas-limite-contexto.md:7–17](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/mediciones/mis-tareas-limite-contexto.md#L7-L17) caracteriza la medición S9, pero su correspondencia con la asignación S10 no está verificada. |
| Línea base medida y reproducible | No verificado | [docs/calidad/mediciones/mis-tareas-limite-contexto.md:9–29](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/mediciones/mis-tareas-limite-contexto.md#L9-L29) aporta antes/después local; no sustituye línea base del MVP desplegado bajo el escenario operativo asignado. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md:19–49](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md#L19-L49) compara alternativas y costo de la consulta adicional; falta demostrar correspondencia con el reto operativo asignado y costo en MySQL. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [app/application/servicio_tareas.py:219–232](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/app/application/servicio_tareas.py#L219-L232) implementa separación real, sin vínculo verificable con una consigna S10. |
| Resultado contrastado con el umbral | No verificado | [docs/calidad/mediciones/mis-tareas-limite-contexto.md:25–32](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/mediciones/mis-tareas-limite-contexto.md#L25-L32) declara límites de la medición: SQLite, sin red, sin 30 concurrentes. No acredita resultado del reto en el despliegue. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | [CI del estado](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/37236877375) y [chequeo de despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/37512258356) en failure. [README.md:138–147](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/README.md#L138-L147) declara salud/logs/métricas, pero falta funcionamiento conjunto y métrica ligada a la asignación verificada. |
| Secretos protegidos | Cumple | Barrido estático del árbol y revisión de coincidencias: sin credenciales productivas reales detectadas. [.env.example:1–21](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/.env.example#L1-L21) contiene marcadores; [compose.yaml:9–27](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/compose.yaml#L9-L27) acota valores de desarrollo a contenedor local; [.github/workflows/ci.yml:23–40](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/.github/workflows/ci.yml#L23-L40) genera contraseña efímera. No se reproducen valores en este informe. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/arc42/arc42-uniteam.md:557–575](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/arc42/arc42-uniteam.md#L557-L575) deja conceptos transversales pendientes; [docs/calidad/propiedad-datos.md:23–24](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/propiedad-datos.md#L23-L24) aún pide contrastar el mapa con el esquema. La nueva cadena A-12 existe, pero el conjunto sigue parcial. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md:11–17](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md#L11-L17) y [docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md:35–49](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md#L35-L49) corrigen erosión y confirman la intención de ADR 003 con evidencia S9; no hay confirmación/reemplazo sustentado en el experimento operativo asignado S10. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Lo resuelve el docente en la sustentación sobre entorno desplegado y pipeline en vivo. |

## Rúbrica específica de cinco criterios

| Criterio | Nivel sugerido | Puntaje | Evidencia y límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Los documentos identifican ESC-01/ESC-03 y la auditoría A-12, pero no contienen la consigna operativa oficialmente asignada al equipo para S10. |
| Decisión e implementación | No verificado | Pendiente | ADR 0013 tiene alternativas y una implementación real, pero la relación con la asignación operativa y el efecto en MySQL quedan abiertos. |
| Operación, seguridad y observabilidad | Básico | 0.60 | Health, logs JSON y métricas existen en código; CI y chequeos públicos fallan, sin evidencia operativa completa del reto. |
| Evolución arquitectónica trazable | Básico | 0.60 | Cadena A-12 y ADR nuevos navegables; arc42 §8 y contraste de propiedad con esquema real siguen pendientes. |
| Sustentación del reto | Lo fija el docente | Pendiente | Sustentación pendiente. |

**No se publica total final.** La escala de cada criterio es 0,00 / 0,60 / 0,80 / 1,00; la sustentación queda a cargo del docente, con entorno desplegado y pipeline en vivo. Las celdas pendientes no equivalen a cero. S6–S9 no se recalifican por existir.

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público ISCOUTB/AS_202620_uniTeam correcto; [README.md:14–23](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/README.md#L14-L23). |
| Estructura mínima presente | Cumple | README y docs/arc42, adr, c4, aspectos.md, ia.md presentes; [docs/aspectos.md:44–51](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/aspectos.md#L44-L51). |
| Estado calificado identificable | Cumple | master y hash/fecha del encabezado; último commit ≤ cierre, sin etiquetas. |
| Nombres de ADR según la convención | Cumple | ADR 0001–0014 con nombres NNNN-titulo-en-kebab-case.md; [docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md:1–6](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md#L1-L6). |
| ADR aceptados no reescritos | No cumple | Historial leído: ADR 0011 creado en 369b0d9 y editado en 0f3da0f tras figurar Aceptada; [docs/adr/0011-mantener-la-api-despierta-con-un-sondeo-externo.md:3–7](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0011-mantener-la-api-despierta-con-un-sondeo-externo.md#L3-L7). El reemplazo parcial de 0008 por 0011 está declarado, pero no reemplaza la edición posterior de 0011. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:86–121](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/ia.md#L86-L121) aporta entrada y auditoría del periodo S9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [CI del hash actual](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/37236877375) concluye failure. [.github/workflows/ci.yml:161–179](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/.github/workflows/ci.yml#L161-L179) exige scanner y espera Quality Gate, pero configuración no equivale a resultado; falta gate público satisfactorio de este estado. [Comprobación de despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/37512258356) también falla. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido de árbol e historial con patrones de alta especificidad sin credenciales reales confirmadas; valores locales/marcadores revisados en [compose.yaml:9–27](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/compose.yaml#L9-L27). Alcance de patrones declarado; no prueba sobre secretos externos. |
| Contribución de todos los integrantes | No verificado | 75 commits con siete firmas de autor y variantes; no se atribuyen las firmas a las cuatro personas de matrícula sin correspondencia confirmada. |

## Estado global del proyecto (overall)

Punta de la misma rama: `6e04b35317a0a68d239ae85c71cd60e21982b195` (2026-10-04T16:37:55-05:00). Hay **6 commits en el delta S8→S9** y **0 commits posteriores al cierre S9**. La punta incorpora seis commits S9 que corrigen la lectura cruzada de tablas y añaden ADR aceptados, pruebas, medición y auditoría. No hay tardíos. Persisten CI y chequeos de despliegue en failure; se distinguen esos runs de los resultados locales documentados.

La aplicación pública devolvió HTTP 200 en 6,029311 s en la consulta iniciada 2026-10-06T21:21:59Z. La consulta de /health iniciada 2026-10-06T21:22:05Z agotó 25,001788 s sin bytes recibidos (curl 28, HTTP 000); es timeout de esta comprobación, no prueba concluyente de caída del servidor. Un segundo intento de /health iniciado 2026-10-06T21:27:21Z también agotó 90,000219 s sin bytes (HTTP 000). No se probó el flujo autenticado.

### Hallazgos abiertos

- Recuperar CI del hash actual y comprobación periódica de despliegue; publicar resultado verificable del scanner y Quality Gate.
- Medir el costo de consulta adicional en MySQL y carga real: la evidencia S9 es SQLite secuencial en proceso.
- Precisar la asignación operativa S10; no equipararla automáticamente con ESC-01/ESC-03.
- Completar arc42 §8 y reconciliar auditoría/mapa/ADRs con el MVP actual.
- No reescribir ADR aceptados; el antecedente de ADR 0011 sigue abierto.
- Confirmar correspondencia de firmas del historial con integrantes, sin atribuciones por parecido.

### Hallazgos cerrados o sustituidos con evidencia actual

- Ya hay incremento S9 y cadena A-12 completa: [docs/aspectos.md:29](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/aspectos.md#L29).
- Auditoría de erosión, corrección y prueba negativa ahora documentadas: [docs/calidad/mediciones/mis-tareas-limite-contexto.md:19–23](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/mediciones/mis-tareas-limite-contexto.md#L19-L23) y [docs/calidad/propiedad-datos.md:28–46](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/propiedad-datos.md#L28-L46).
- La no incorporación generativa ya es una decisión aceptada en ADR 0014: [docs/adr/0014-no-incorporar-un-componente-generativo.md:3–32](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0014-no-incorporar-un-componente-generativo.md#L3-L32).
- El registro de IA sí creció en S9 con aceptado/corregido/rechazado y verificación de dependencias: [docs/ia.md:86–121](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/ia.md#L86-L121).
- La planilla antigua dice sin URL, pero el README publica sitio/API y la portada respondió HTTP 200. [README.md:18–22](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/README.md#L18-L22). No se da por probado el flujo.

## Para completar antes del cierre

Identifiquen la consigna operativa asignada y diseñen su experimento con línea base en el MVP desplegado. Recuperen CI y los chequeos de despliegue, repitan la medición relevante con MySQL y carga de red, y completen arc42 y propiedad de datos. La comparación local es un buen punto de partida, pero no sustituye el resultado operativo ni la sustentación.

## Tres preguntas para la sustentación

1. ¿Qué ocurre si cambia la pertenencia a un proyecto entre las dos consultas y cómo evitan o detectan una respuesta no autorizada?
2. ¿Cuál es el costo de la consulta adicional sobre MySQL gestionado, en latencia y capacidad, frente a los 1,2 ms locales?
3. ¿Qué cambiarían si la medición en MySQL con concurrencia contradice el resultado de SQLite?

## Delta S5→S10 (sin recalificar entregas previas)

Se verificó por Git la base S5 publicada `dc14298c32a4fde0956266b0300063c24d7a9486` contra la punta `6e04b35317a0a68d239ae85c71cd60e21982b195`: 25 commits. [Comparación inmutable](https://github.com/ISCOUTB/AS_202620_uniTeam/compare/dc14298c32a4fde0956266b0300063c24d7a9486...6e04b35317a0a68d239ae85c71cd60e21982b195). Las filas de decisión, implementación y evolución usan este delta como contexto, sin volver a calificar S5–S9.

Cambios documentales contrastados:

- .../0006-estilo-sincrono-con-eventos-en-proceso.md | 119 ++++++++++
- ...servir-la-aplicacion-web-como-sitio-estatico.md |  76 +++++++
- ...8-desplegar-la-api-como-contenedor-en-render.md |  91 ++++++++
- ...iven-for-mysql-como-base-de-datos-gestionada.md |  83 +++++++
- .../0010-usar-auth0-como-proveedor-de-identidad.md |  85 +++++++
- ...tener-la-api-despierta-con-un-sondeo-externo.md |  80 +++++++
- ...ublicar-el-flujo-de-estados-desde-el-dominio.md |  72 ++++++
- .../0013-tareas-no-lee-las-tablas-de-proyectos.md  |  62 ++++++
- .../0014-no-incorporar-un-componente-generativo.md |  40 ++++
- docs/arc42/arc42-uniteam.md                        | 243 ++++++++++++++++++++-
- docs/c4/nivel2-contenedores.md                     |  28 +--
- 11 files changed, 962 insertions(+), 17 deletions(-)
