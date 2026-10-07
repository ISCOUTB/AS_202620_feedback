# Semana 10 · Segundo corte · ROUTB

> **Revisión preliminar**, realizada el 6 de octubre de 2026. El cierre de S10 todavía no ha ocurrido. No constituye nota aplicada ni evaluación de sustentación.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_ROUTB |
| Estado revisado | `7c6573e68a5fdab019fab8fddfe1acb2a451cb27` en `origin/master` (2026-10-03T18:20:32-05:00) |
| Rama remota principal | `origin/master` |
| Base S8 | `eae667ef4339d3e8e89461b1e5f865a08eb21d10` |
| Estado preliminar S10 / HEAD | `7c6573e68a5fdab019fab8fddfe1acb2a451cb27` · 2026-10-03T18:20:32-05:00 |
| Cierre previsto S10 | 2026-10-12T05:00:00Z |
| Observación | 2026-10-06T21:18:51Z |

## Escenario operativo asignado y alcance

**No verificado.** La reserva grupal de S9 es una decisión del equipo; el rendimiento GET /trips/ es un escenario de calidad propio. No se localizó en las fuentes inspeccionadas un enunciado oficial que los asigne como reto S10. [docs/evidencia/SEMANA9.md:9–22](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/SEMANA9.md#L9-L22), [docs/adr/0007-reserva-grupal-de-cupos.md:37–43](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0007-reserva-grupal-de-cupos.md#L37-L43) y [docs/evidencia/medicion-reserva-grupal-semana9.md:3–9](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/medicion-reserva-grupal-semana9.md#L3-L9).

Se revisaron README, ADR, arc42 y evidencias/experimentos. Un escenario de calidad elegido por el equipo no demuestra cuál le asignó el docente. Antes de valorar la respuesta del reto hay que disponer del enunciado o una referencia oficial equipo–escenario. Las evidencias S6–S9 se describen como línea base, sin recalificarlas por existir.

**PDF excluido por instrucción docente:** se omite su fila; no se leyó ningún PDF ni se cuenta como incumplimiento. La matriz conserva 12 comprobaciones. Se realizaron únicamente consultas HTTP de lectura indicadas abajo. No se ejecutó código del equipo ni se probó el flujo principal.

## Matriz de comprobación S10

| Criterio | Evidencia técnica esperada | Estado preliminar | Observaciones y evidencia |
|---|---|---|---|
| Estado de S10 identificable y anterior al cierre | Rama principal, hash y fecha; estado preliminar | Cumple | HEAD 7c6573e68a5fdab019fab8fddfe1acb2a451cb27, 2026-10-03T18:20:32-05:00, anterior al cierre futuro; preliminar. |
| Despliegue accesible en el momento de la revisión | Respuesta HTTP, tiempo y hora | Cumple | GET de lectura a https://as-202620-routb.onrender.com/health, iniciado 2026-10-06T21:18:51Z: HTTP 200 en 26,971224 s. URL en [README.md:105–106](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/README.md#L105-L106). No se probó reserva/login ni se confirmó versión desplegada; un health 200 no demuestra flujo principal. |
| Hipótesis, montaje, variables y umbral declarados | Caracterización del escenario operativo asignado | No verificado | Falta asignación S10. Umbral propio GET /trips/ en [docs/evidencia/medicion-reserva-grupal-semana9.md:3–9](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/medicion-reserva-grupal-semana9.md#L3-L9) no la acredita. |
| Línea base medida y reproducible | Herramienta, carga y procedimiento del escenario asignado | No verificado | Base externa 585,10 ms y procedimiento documentados; falta identificar que correspondan al reto asignado y a un despliegue comparable. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | ADR y respuesta al escenario asignado | No verificado | ADR-0007 fundamenta reserva grupal, pero no identifica asignación S10: [docs/adr/0007-reserva-grupal-de-cupos.md:7–65](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0007-reserva-grupal-de-cupos.md#L7-L65). |
| Respuesta implementada o configurada sobre el MVP | Cambio trazable correspondiente al reto | No verificado | Código y transacción de reserva existen; despliegue con esa versión y respuesta al reto no comprobados. La divergencia histórica está reconocida en [docs/evidencia/prueba-reserva-grupal-semana9.md:53–57](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/prueba-reserva-grupal-semana9.md#L53-L57). |
| Resultado contrastado con el umbral | Medición final comparable con línea base | No verificado | Resultado externo S9 contrastado; medición interna pendiente, sin escenario S10 confirmado: [docs/evidencia/medicion-reserva-grupal-semana9.md:27–32](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/medicion-reserva-grupal-semana9.md#L27-L32). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | Run y observabilidad del escenario asignado | No verificado | CI success y health 200; pendiente métrica y observabilidad de la asignación, pipeline bloqueante y scanner Sonar: [.github/workflows/ci.yml:29–67](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/.github/workflows/ci.yml#L29-L67). |
| Secretos protegidos | Barrido del contrato | No verificado | Barrido independiente bloqueado por herramienta; no se asume exposición ni limpieza por declaración documental. |
| C4, arc42, ADR y contratos correspondientes al MVP | Consistencia documental y trazabilidad | No verificado | Aspectos/ADR/contrato se actualizan para reserva grupal: [docs/aspectos.md:12](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/aspectos.md#L12). Falta contrastar documentación completa del MVP y estado desplegado con el escenario S10; no se recalifica la porción S9. |
| Decisión anterior confirmada o reemplazada con evidencia | Relación explícita entre medición y decisión | No verificado | ADR-0007 conserva decisión atómica de ADR-0003, pero la confirmación mediante experimento específico de S10 queda pendiente: [docs/adr/0007-reserva-grupal-de-cupos.md:37–42](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0007-reserva-grupal-de-cupos.md#L37-L42). |
| Sustentación del reto sobre el entorno desplegado | Sesión y pipeline en vivo; lo resuelve el docente | No verificado | Sustentación sobre despliegue y pipeline en vivo pendiente del docente. |

## Rúbrica del segundo corte · cinco criterios

Escala de la ficha: **0,00 · 0,60 · 0,80 · 1,00 por criterio**. No se aplica la fórmula semanal. Una comprobación pendiente conserva puntaje pendiente; no se convierte automáticamente en cero.

| Criterio | Nivel sugerido | Puntaje | Fundamento |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Escenario asignado no identificado; escenario de rendimiento propio no sustituye la consigna. |
| Decisión e implementación | No verificado | Pendiente | Reserva grupal implementada y justificada en S9; no se acredita respuesta al reto y versión pública. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Faltan correspondencia de métrica con reto y verificación de seguridad bloqueada; no se penaliza al equipo por el entorno revisor. |
| Evolución arquitectónica trazable | No verificado | Pendiente | Se dispone de trazabilidad S9, pendiente evolución específica S10 y correspondencia con el despliegue. |
| Sustentación del reto | Pendiente del docente | Pendiente | Pendiente de sustentación sobre el despliegue y ejecución del pipeline en vivo; no se infiere desde el repositorio. |

**Total: pendiente, no calculado.** La correspondencia con la asignación y la sustentación impiden proponer un total responsable.

## Matriz transversal · CONTRATO §11

| Criterio transversal | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Repositorio ISCOUTB/AS_202620_ROUTB visible por clon git público, rama master. |
| Estructura mínima presente | Cumple | Árbol con README, docs/arc42, adr, c4, aspectos e ia. Cadena [docs/aspectos.md:5–12](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/aspectos.md#L5-L12). |
| Estado calificado identificable | Cumple | 7c6573e68a5fdab019fab8fddfe1acb2a451cb27, 2026-10-03T18:20:32-05:00, último master ≤ cierre; HEAD coincide. |
| Nombres de ADR según la convención | Cumple | Ocho ADR con nombre NNNN-kebab-case.md; nuevos [docs/adr/0007-reserva-grupal-de-cupos.md:1–5](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0007-reserva-grupal-de-cupos.md#L1-L5) y [docs/adr/0008-no-componente-generativo.md:1–5](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0008-no-componente-generativo.md#L1-L5). |
| ADR aceptados no reescritos | No verificado | Las revisiones previas señalaban edición de ADR 0001/0002/0003/0005/0006. Se mantiene como antecedente pendiente de comprobación histórica completa en esta pasada; no se eleva texto previo no revalidado a evidencia nueva. Los nuevos ADR no sustituyen explícitamente esos registros. |
| docs/ia.md al día para la semana | Cumple | Entrada S9 del 2-oct con decisiones y rechazo: [docs/ia.md:109–119](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/ia.md#L109-L119). No se acredita todavía un registro del reto S10. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [CI final success](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/37161463477), pero [.github/workflows/ci.yml:29–67](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/.github/workflows/ci.yml#L29-L67) ejecuta pytest/build sin scanner Sonar. [README.md:91–95](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/README.md#L91-L95) contiene enlace genérico; falta cadena scanner→run→Gate de la revisión. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Barrido snapshot/histórico interrumpido por herramienta; no se presume limpio el historial ni se afirma un incidente. Debe completarse sin publicar valores sensibles. |
| Contribución de todos los integrantes | No verificado | 71 commits distribuidos en cuatro nombres de autor; aporte concentrado (60 de 71 bajo una firma). [README.md:36–41](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/README.md#L36-L41) lista miembros sin correspondencia completa con cuentas. Confirmar mapeo; no se deduce por parecido. |

## Estado global (overall)

HEAD: `7c6573e68a5fdab019fab8fddfe1acb2a451cb27` · 2026-10-03T18:20:32-05:00. La punta coincide con S9. Cinco commits nuevos desde S8, con reserva grupal y documentación; CI final success. Health público responde 200. La evidencia del 2-oct señalaba producción 0.2.0 frente a contrato 0.3.0; en esta revisión solo se comprobó salud y no se afirma que esa divergencia esté corregida. La medición interna, Sonar y asignación S10 siguen pendientes. El barrido de seguridad quedó bloqueado por herramienta.

Recuento descriptivo: **2 Cumple, 0 No cumple, 10 No verificado, sobre 12.** No es una nota ni sustituye la rúbrica.

## Próximos pasos

Identifiquen el escenario operativo asignado antes de presentar la reserva grupal o el rendimiento como respuesta al segundo corte. Salud responde, pero aún deben demostrar el flujo sobre la versión desplegada, línea base y resultado comparables, observabilidad del reto y pipeline bloqueante. La sustentación permanece pendiente.

## Tres preguntas para la sustentación

1. Fallo: ¿cómo evitan aceptar dos grupos simultáneos sin capacidad suficiente y liberar dos veces los cupos al repetir una cancelación?
2. Costo: ¿qué límite de Render o Supabase agotaría primero el presupuesto cero y cómo afectaría la latencia caliente y fría?
3. Medición: ante el aumento del p95 externo frente a la base, ¿qué repetirían para separar efecto de red, versión desplegada y cambio funcional?

## Delta arquitectónico desde el primer corte

Base publicada de S5: `343bb9d6565c1a81bdad542efde3fbb56b07e2ca`; comparación git contra HEAD `7c6573e68a5fdab019fab8fddfe1acb2a451cb27`: 237 rutas cambiadas, de ellas 14 en ADR/arc42/C4 (sin leer PDF). Se inspeccionaron las decisiones, contratos, código y evidencia citados en las filas. El delta sirve para examinar evolución y consistencia del MVP, no para recalificar las entregas S6–S9. La correspondencia con el escenario asignado S10 sigue pendiente.
