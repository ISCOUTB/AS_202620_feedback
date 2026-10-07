# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo a lo largo del semestre.

## Identificación

| | |
|---|---|
| Equipo | uniTeam |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Julio Cesar Emiliani Ramos · Ian Novoa Carrillo · Juan Jose Bustamante More · Daniel Isaac Manjarres Herrera. Identidades observadas: `super-gremlin`, `Ian Novoa`, `Julio Cesar Emiliani`, `JuanB`/`JuanBustamante`, `Daniel Manjarres Herrera` y `DaniGamer0907`; ninguna correspondencia individual se da por confirmada. La cuenta listada `iansx` no aparece.; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://uniteam-web.onrender.com · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `6e04b35317a0a68d239ae85c71cd60e21982b195` · 2026-10-04T16:37:55-05:00 | 10/10 | 5.0 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `6e04b35317a0a68d239ae85c71cd60e21982b195` · 2026-10-04T16:37:55-05:00 | 2/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `4b4c5c0` · 2026-08-09T11:22:38-05:00 | 6/9 | 3.7 (propuesta) | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `ca7726a` · 2026-08-16T13:01:06-05:00 | 9/9 | 5.0 (propuesta) | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `ca44917` · 2026-08-23T13:38:40-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `dc14298` (2026-08-29T11:49:10-05:00) | 6/10 | 3.4 | si |
| 5 | CORTE1 | `dc14298` (2026-08-29T11:49:10-05:00) | sin actividad | no aplica | si |
| 6 | S6 | `6cc8e6f` (2026-09-13T20:20:18-05:00) | 2/8 | 2.0 (propuesta) | sí |
| 7 | S7 | `1ea4aba` (2026-09-18T22:21:34Z) | 9/10 | 4.6 | sí (auditoría definitiva corregida) |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `0f3da0f3` (2026-09-27T22:52:09-05:00) | 9/10 | 4.6 (propuesta; 2 filas de despliegue pendientes) | sí (definitiva) |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Recuperar CI del hash actual y comprobación periódica de despliegue; publicar resultado verificable del scanner y Quality Gate. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Medir el costo de consulta adicional en MySQL y carga real: la evidencia S9 es SQLite secuencial en proceso. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Precisar la asignación operativa S10; no equipararla automáticamente con ESC-01/ESC-03. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar arc42 §8 y reconciliar auditoría/mapa/ADRs con el MVP actual. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| No reescribir ADR aceptados; el antecedente de ADR 0011 sigue abierto. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Confirmar correspondencia de firmas del historial con integrantes, sin atribuciones por parecido. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Ya hay incremento S9 y cadena A-12 completa: [docs/aspectos.md:29](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/aspectos.md#L29). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Auditoría de erosión, corrección y prueba negativa ahora documentadas: [docs/calidad/mediciones/mis-tareas-limite-contexto.md:19–23](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/mediciones/mis-tareas-limite-contexto.md#L19-L23) y [docs/calidad/propiedad-datos.md:28–46](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/calidad/propiedad-datos.md#L28-L46). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La no incorporación generativa ya es una decisión aceptada en ADR 0014: [docs/adr/0014-no-incorporar-un-componente-generativo.md:3–32](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/adr/0014-no-incorporar-un-componente-generativo.md#L3-L32). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| El registro de IA sí creció en S9 con aceptado/corregido/rechazado y verificación de dependencias: [docs/ia.md:86–121](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/docs/ia.md#L86-L121). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La planilla antigua dice sin URL, pero el README publica sitio/API y la portada respondió HTTP 200. [README.md:18–22](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/6e04b35317a0a68d239ae85c71cd60e21982b195/README.md#L18-L22). No se da por probado el flujo. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Cuenta `super-gremlin` sin atribuir a persona y 2 integrantes sin commits atribuibles | S1 (y S2) | sí | urgente: la contribución individual se califica sobre el historial en el proyecto final (S3: solo Ian Novoa firmó commits) |
| `docs/aspectos.md` sin la tabla de 8 columnas del curso (S1: sin tabla; S2: tabla propia de 6 columnas sin C4/ADR/Código/Pruebas/Evidencia) | S1 | sí | ajustar a las 8 columnas; en S3 además falta enlazar el ADR-003 desde la tabla |
| Ficha sin tensiones de calidad | S1 | sí | añadir las dos tensiones enfrentadas |
| Nombres de ADR fuera de convención (`ADR-00N-…`, el 003 con « (1)») | S3 (23-ago) | sí | renombrar a `NNNN-titulo-en-kebab-case.md`; marcar ADR-001 como reemplazado por ADR-002 |
| README sin comando de arranque (solo documenta la prueba) y `requirements.txt` con el paquete inexistente `httpx2` | S3 (23-ago) | sí | documentar `uvicorn` y corregir dependencias |
| `docs/ia.md` sin entradas del periodo S3 | S3 (23-ago) | sí | registrar el uso de IA de esta semana con rechazados y motivo |
| Prueba sin CI: verde no verificable (solo lo declara el README) | S3 (23-ago) | sí | montar `.github/workflows/` o aportar evidencia de ejecución |
| Confirmar contenido de secciones 9, 10 y 12 de arc42 | S4 | si | |
| Aportar URL de run de CI en verde | S4 | si | |
| Verificar contenido de docs/ia.md | S4 | si | |
| Etiqueta `corte-1` y respuesta explícita a la restricción asignada | S5 | sí | fijar la etiqueta; el ADR 0005 (OIDC) es una respuesta plausible pero el equipo debe confirmar en sustentación si esa fue la restricción asignada |
| Medición posterior al cambio comparada con la línea base | S5 | sí | falta cuantificar el estado inicial del defecto de autenticación y medir el resultado posterior contra el umbral de ESC-03 (100% denegado, auditoría ≤1s); ESC-01 mide un escenario distinto |
| Registro de IA específico del cambio de autenticación (OIDC) | S5 | sí | `docs/ia.md` menciona el cambio pero sin una entrada de aceptado/corregido/rechazado con motivo técnico propia de esa pieza de trabajo |
| Tabla de propiedad contrastada contra esquema y modelos reales | S6 | sí | el propio documento la declara como primera pasada |
| No conformidades de propiedad con rutas y corrección verificable | S6 | sí | las tres filas conservan marcadores `revisar` |
| Incorporar mapa y lenguaje ubicuo en arc42 §8 | S6 | sí | la sección 8 del arc42 está marcada como pendiente |
| Evidencia pública de SonarCloud y Quality Gate | S6 | sí | `ci.yml` no invoca scanner ni aporta URL de análisis |
| Contrato OpenAPI/AsyncAPI/proto versionado, con rutas, esquemas y versión de API (filas 1-4 de la ficha). | S7 | no | Resuelto en el estado calificado de S7. |
| Prueba de contrato e invocación desde el workflow (filas 5-6). | S7 | no | Resuelto: el workflow valida el contrato y el run exitoso quedó citado. |
| Evidencia de que la prueba falla ante un cambio incompatible (fila 7). | S7 | si | |
| Sección 6 de arc42 con flujos de interacción y formato en cada flecha del C4 nivel 2 (filas 9-10, parcialmente resuelto). | S7 | no | Resuelto en el estado calificado de S7. |
| Evidencia auditable de SonarCloud: línea del scanner, URL del run y URL del análisis con Quality Gate (contrato §8). | S7 | si | |
| Secciones 7 y 8 de arc42, declaradas pendientes por el propio documento. | S7 | si | |
| Publicar el sistema y demostrar que una URL pública y el endpoint de salud responden. | S8 | sí | `/activo` solo está documentado para localhost y el propio repositorio declara que no hay despliegue. |
| Recuperar el pipeline en verde para el estado entregado. | S8 | sí | El run del estado S8 revisado falla. |
| Incorporar logs estructurados, métrica operativa consultable y mecanismo de secretos del proveedor. | S8 | sí | El logging es texto libre y Compose conserva credenciales de desarrollo; no hay métrica ni gestor de secretos verificable. |
| Completar cálculo mensual, arc42 §7 y ADR de plataforma de despliegue. | S8 | sí | Existe la restricción de costo cero, pero faltan cálculo y decisión de plataforma. |
| Sin commits de S9: la punta coincide con el hash calificado de S8. | S9 | sí | Empujar la porción de la evidencia S9 antes del cierre. |
| CI del hash revisado en rojo, incluido el Quality Gate. | S9 | sí | Reparar el workflow `CI` en la rama principal. |
| ADR 0011 editado el 2026-09-27 tras su aceptación, sin declarar reemplazo. | S9 | sí | No editar ADR aceptados; crear uno nuevo y marcar el anterior como reemplazado. |
| Contribución por integrante sin atribuir: seis identidades de correo para cuatro personas. | S9 | No verificado | Confirmar con el docente a qué persona corresponde cada cuenta. |
| Sin evaluación ni ADR sobre el componente generativo. | S9 | sí | Evaluar el componente o decidir su no incorporación con un ADR. |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
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

## Contribución por integrante

Actualización agregada del 2026-10-06: 75 commits repartidos entre siete firmas visibles; existen variantes de firma. Correspondencia individual con la matrícula No verificado; no se publican correos.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Persona sin atribuir | `super-gremlin` | 15 | — | — | El docente debe confirmar a quién corresponde. |
| Integrante sin correspondencia confirmada | `Ian Novoa` | 11 | — | — | La cuenta listada `iansx` no aparece; no se asume equivalencia. |
| Integrante sin correspondencia confirmada | `Julio Cesar Emiliani` | 11 | — | — | Firma observada; correspondencia pendiente de confirmación. |
| Integrante sin correspondencia confirmada | `JuanB`/`JuanBustamante` | 14 | — | — | Alias consolidados por la misma cuenta de GitHub; persona no atribuida. |
| Integrante sin correspondencia confirmada | `Daniel Manjarres Herrera` | 7 | — | — | Firma observada; persona no atribuida. |
| Persona sin atribuir | `DaniGamer0907` | 1 | — | — | Cuenta distinta; no se consolida por parecido de nombre. |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- ¿Qué ocurre si cambia la pertenencia a un proyecto entre las dos consultas y cómo evitan o detectan una respuesta no autorizada?
- ¿Cuál es el costo de la consulta adicional sobre MySQL gestionado, en latencia y capacidad, frente a los 1,2 ms locales?
- ¿Qué cambiarían si la medición en MySQL con concurrencia contradice el resultado de SQLite?
