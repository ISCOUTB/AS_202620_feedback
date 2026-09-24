# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo a lo largo del semestre.

## Identificación

| | |
|---|---|
| Equipo | uniTeam |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Integrantes y su usuario de GitHub | Julio Cesar Emiliani Ramos · Ian Novoa Carrillo · Juan Jose Bustamante More · Daniel Isaac Manjarres Herrera. Identidades observadas: `super-gremlin`, `Ian Novoa`, `Julio Cesar Emiliani`, `JuanB`/`JuanBustamante`, `Daniel Manjarres Herrera` y `DaniGamer0907`; ninguna correspondencia individual se da por confirmada. La cuenta listada `iansx` no aparece. |
| URL del sistema desplegado | sin URL (sin despliegue todavía) |
| Ultima revision | 2026-09-24 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `4b4c5c0` · 2026-08-09T11:22:38-05:00 | 6/9 | 3.7 (propuesta) | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `ca7726a` · 2026-08-16T13:01:06-05:00 | 9/9 | 5.0 (propuesta) | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `ca44917` · 2026-08-23T13:38:40-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `dc14298` (2026-08-29T11:49:10-05:00) | 6/10 | 3.4 | si |
| 5 | CORTE1 | `dc14298` (2026-08-29T11:49:10-05:00) | sin actividad | no aplica | si |
| 6 | S6 | `6cc8e6f` (2026-09-13T20:20:18-05:00) | 2/8 | 2.0 (propuesta) | sí |
| 7 | S7 | `1ea4aba` (2026-09-18T22:21:34Z) | 9/10 | 4.6 | sí (auditoría definitiva corregida) |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `73d714c` (2026-09-21T11:46:49-05:00) | 3/12 | 2.0 (propuesta preliminar) | sí (preliminar) |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 9 | Evidencia S9 · Generación verificada y trazable | | | no aplica | |
| 10 | Segundo corte · reto aplicado sobre el MVP | `corte-2` | | | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

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
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_uniTeam`, público |
| Estructura mínima | Cumple | seis rutas presentes |
| Convención de nombres de ADR | Cumple | seis ADR con nombres `NNNN-titulo-en-kebab-case.md` |
| ADR aceptados sin reescribir | Cumple | ADR 0001 declara reemplazo por 0002; los demás conservan su decisión |
| `docs/ia.md` al día | No cumple | última actualización verificable 2026-09-18, anterior al periodo S8. |
| Sin credenciales en el repositorio ni en el historial | Cumple | barridos limpios; menciones de token son identificadores de código |
| Contribución de todos los integrantes | No verificado | El historial contiene seis grupos de identidades; solo `JuanB`/`JuanBustamante` se consolidan por compartir cuenta. `EQUIPOS.md` no ofrece correspondencias individuales y `iansx` no aparece. |
| Pipeline en verde | No cumple | El run del estado S8 revisado falla y no se encontró análisis público de SonarCloud con Quality Gate. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Persona sin atribuir | `super-gremlin` | 15 | — | — | El docente debe confirmar a quién corresponde. |
| Integrante sin correspondencia confirmada | `Ian Novoa` | 11 | — | — | La cuenta listada `iansx` no aparece; no se asume equivalencia. |
| Integrante sin correspondencia confirmada | `Julio Cesar Emiliani` | 11 | — | — | Firma observada; correspondencia pendiente de confirmación. |
| Integrante sin correspondencia confirmada | `JuanB`/`JuanBustamante` | 14 | — | — | Alias consolidados por la misma cuenta de GitHub; persona no atribuida. |
| Integrante sin correspondencia confirmada | `Daniel Manjarres Herrera` | 7 | — | — | Firma observada; persona no atribuida. |
| Persona sin atribuir | `DaniGamer0907` | 1 | — | — | Cuenta distinta; no se consolida por parecido de nombre. |

## Preguntas abiertas para la sustentación

- ¿A quién corresponde la cuenta `super-gremlin`? Con eso se cierra el contraste de contribución.
- ¿Qué pasó con el proyecto anterior cuyos artefactos se borraron del repo (historial público)?
- ¿El esqueleto arranca y la prueba pasa en el entorno del equipo? (no ejecutado por regla del kit; el README no documenta el arranque y `requirements.txt` trae el paquete inexistente `httpx2`)
