# Semana 9 · Generación verificada y trazable · ROUTB

> Revisión definitiva actualizada tras el cierre. Propuesta al docente; la nota final se fija en Moodle.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_ROUTB |
| Rama remota principal | `origin/master` |
| Base S8 | `eae667ef4339d3e8e89461b1e5f865a08eb21d10` |
| Estado revisado | `7c6573e68a5fdab019fab8fddfe1acb2a451cb27` en `origin/master` (2026-10-03T18:20:32-05:00) |
| Cierre S9 | 2026-10-05T05:00:00Z |
| Observación | 2026-10-06T21:18:51Z |

## Alcance y método

Se revisó el delta de S8 a S9: **5 commits**. Se leyeron código, pruebas, documentos y configuración mediante git; no se ejecutó código estudiantil, pruebas ni despliegue. Una consulta de Actions por repositorio identifica las conclusiones de los runs; no se presentan logs no obtenidos como inspeccionados. Los procedimientos documentados se admiten donde lo permite la ficha. No se consultaron etiquetas. **PDF excluido por instrucción docente: no se leyó ni penalizó.**

La entrega final ya incluye reserva grupal entre uno y cuatro cupos, nueva operación atómica de trips, pruebas de concurrencia, auditoría de fronteras y decisión de no usar IA en ejecución. El impedimento del barrido de seguridad es del entorno revisor, no evidencia de una credencial expuesta.

## Matriz de la ficha S9

| Criterio | Evidencia técnica esperada | Estado | Observaciones y evidencia |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | Rutas del código y commits | Cumple | Porción de reserva grupal descrita en [docs/evidencia/SEMANA9.md:5–15](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/SEMANA9.md#L5-L15) e implementada mediante operación atómica con cantidad: [backend/app/modules/trips/application/request_seats.py:35–61](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/backend/app/modules/trips/application/request_seats.py#L35-L61). IA y decisión humana en [docs/ia.md:109–119](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/ia.md#L109-L119). |
| Cadena completa navegable para esa porción | Aspecto → requisito → C4 → ADR → código → prueba → medición | Cumple | Fila 6 enlaza requisito, C4, ADR-0007/0003, operaciones trips, requests, Flutter, pruebas, auditoría y medición: [docs/aspectos.md:12](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/aspectos.md#L12). Destinos inspeccionados; prueba y medición distinguen alcance local y producción. |
| ADR con la decisión argumentada por el equipo | Restricciones, alternativas y consecuencias | Cumple | ADR-0007 define dueño de disponibilidad y solicitud, transacción, compatibilidad por defecto de un cupo y alternativas descartadas; costo y límites explícitos: [docs/adr/0007-reserva-grupal-de-cupos.md:7–65](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0007-reserva-grupal-de-cupos.md#L7-L65). |
| Prueba que falla ante el defecto que cubre | Run rojo, mutación o procedimiento documentado | Cumple | Procedimiento retira `available_seats >= seat_count`, registra fallo de aserción [200,200] frente a [200,409] y restauración: [docs/evidencia/prueba-reserva-grupal-semana9.md:37–51](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/prueba-reserva-grupal-semana9.md#L37-L51). Código conserva condición: [backend/app/modules/trips/application/request_seats.py:35–47](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/backend/app/modules/trips/application/request_seats.py#L35-L47). El [CI del hash final](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/37161463477) está success; no se atribuyen logs del run rojo sin consultarlos. La ficha admite procedimiento documentado. |
| Medición del escenario asociado | Resultado contrastado con el umbral | Cumple | 100 respuestas externas con p95 697,82 ms frente a base 585,10 ms y umbral 3990 ms: [docs/evidencia/medicion-reserva-grupal-semana9.md:3–32](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/medicion-reserva-grupal-semana9.md#L3-L32). Hay medición y contraste; la fuente admite que falta la medición interna oficial. No demuestra causalidad ni que producción ejecute el hash final; [docs/evidencia/prueba-reserva-grupal-semana9.md:53–57](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/prueba-reserva-grupal-semana9.md#L53-L57) registra desalineación de versión observada el 2-oct. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Extracto de criterio técnico de S9 | Cumple | Uso de Codex/Copilot con aceptado, corrección del máximo de personas y rechazo de extensión/dependencia y de generación en runtime, justificados por alcance y propiedad: [docs/ia.md:109–119](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/ia.md#L109-L119). Reforzar la explicación técnica de por qué no se añade dependencia, sin tratar el grep como razón arquitectónica. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Ubicación de hallazgos y correcciones | Cumple | Auditoría E1–E6 ubica y corrige ORM ajeno, helper privado entre routers y acoplamiento auth/users: [docs/evidencia/auditoria-erosion-semana9.md:3–33](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/auditoria-erosion-semana9.md#L3-L33). requests llama operaciones públicas de trips y confirma transacción: [backend/app/modules/requests/application/manage_request.py:1–57](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/backend/app/modules/requests/application/manage_request.py#L1-L57). |
| Dependencias propuestas verificadas en su registro oficial | Inventario del delta y comprobación de legitimidad | Cumple | Alcance documentado sin nuevas dependencias de esta porción: [docs/ia.md:113–118](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/ia.md#L113-L118), [docs/evidencia/SEMANA9.md:77–83](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/SEMANA9.md#L77-L83). Diff S8→S9 de requirements sin cambios; pubspec reordena/documenta paquetes ya existentes y añade fuentes, sin incorporar un paquete. No se exige instalar una biblioteca nueva para cumplir ni se acepta el supuesto «acuerdo» del ADR como excepción docente; el alcance vacío se corroboró en git. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido estático del CONTRATO §9 | No verificado | El barrido independiente fue interrumpido por la herramienta con “automatic approval review was cancelled”, sin resultados completos. [docs/evidencia/SEMANA9.md:77–83](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/evidencia/SEMANA9.md#L77-L83) declara revisión de credenciales, pero eso no reemplaza el barrido pendiente. No se detectó ni se afirma un secreto. Fila bloqueada por entorno revisor; no se convierte en defecto del equipo. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Resultados, costo, latencia, C4 y degradación; o ADR de exclusión | Cumple | ADR-0008 compara chatbot, resúmenes y clasificación generativa; descarta costo y latencia externos con presupuesto cero y p95 <3,99 s: [docs/adr/0008-no-componente-generativo.md:7–35](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/7c6573e68a5fdab019fab8fddfe1acb2a451cb27/docs/adr/0008-no-componente-generativo.md#L7-L35). |

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

## Estado global del proyecto (overall)

Punta actual de la misma rama: `7c6573e68a5fdab019fab8fddfe1acb2a451cb27` · 2026-10-03T18:20:32-05:00. **0 commits posteriores al estado S9**. La punta coincide con S9. Cinco commits nuevos desde S8, con reserva grupal y documentación; CI final success. Health público responde 200. La evidencia del 2-oct señalaba producción 0.2.0 frente a contrato 0.3.0; en esta revisión solo se comprobó salud y no se afirma que esa divergencia esté corregida. La medición interna, Sonar y asignación S10 siguen pendientes. El barrido de seguridad quedó bloqueado por herramienta.

## Recuento y nota sugerida

**9 de 10 criterios Cumple; 0 No cumple; 1 No verificado.**

**Propuesta numérica pendiente por bloqueo del entorno de revisión.** Hay 9 criterios acreditados; el rango posible con la fila bloqueada es 4.6–5.0. No se descuenta el impedimento técnico como defecto del equipo. La fórmula se aplicará sobre las diez filas cuando se resuelva la verificación. La matriz transversal no entra en la fórmula.

## Pendientes y acciones concretas

- Identificar enunciado oficial de S10 y construir baseline/experimento comparable.
- Confirmar versión pública: la evidencia histórica registró API sin seat_count; health 200 no cierra ese problema.
- Obtener medición interna oficial en el mismo despliegue y declarar sus diferencias con la medición externa.
- Integrar scanner Sonar y aportar run/Gate correspondientes al estado revisado.
- Completar barrido de seguridad cuando el entorno de revisión lo permita; no es un defecto demostrado del proyecto.
- Revalidar historial de ADR y confirmar mapeo explícito de identidades.

## Hallazgos previos cerrados o aclarados

- La preliminar sin entrega S9 queda superada por reserva grupal, ADR, pruebas, medición y registro IA.
- Se aporta auditoría de erosión E1–E6 con cambios observables y ADR de no incorporar generación.
- La salud pública anteriormente diferida pudo comprobarse ahora por HTTP; no modifica S8 retroactivamente.
