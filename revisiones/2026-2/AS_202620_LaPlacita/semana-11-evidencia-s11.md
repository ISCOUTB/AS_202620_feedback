# AS_202620_LaPlacita · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_LaPlacita/tree/0c9ce082b5850baf1ecda75e82d20757d0101234) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado: DEFINITIVA S11**.

- Rama: `origin/master`; commit evaluado: [`0c9ce082b5850baf1ecda75e82d20757d0101234`](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/0c9ce082b5850baf1ecda75e82d20757d0101234), fecha `2026-10-18T21:56:00-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 52 commits durante S11; 0 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Integración principal identificada en el código | Cumple | [backend/src/modules/pedidos/index.js:14-28](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/backend/src/modules/pedidos/index.js#L14-L28). Rutas HTTP → Pedidos → persistencia PostgreSQL; el módulo usa escribirPedido y memoria compartida. |
| Tabla de fallos: no responde, tarde y dos veces | Cumple | [docs/evidencias/evidencias-s11.md:26-35](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/evidencias/evidencias-s11.md#L26-L35). No responde/tarde y duplicado, además de ack perdido, caída BD y scanner. |
| Mitigación asignada a cada fallo | Cumple | [docs/evidencias/evidencias-s11.md:28-35](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/evidencias/evidencias-s11.md#L28-L35). Timeout/backoff, clave, outbox y breaker asignados; estados actualizados en §§8–9. |
| Correspondencia o pendiente explícito con plan | Cumple | [docs/evidencias/evidencias-s11.md:115-173](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/evidencias/evidencias-s11.md#L115-L173). FIFO e idempotencia parcial implementadas; durabilidad de claves, outbox y backoff quedan pendientes explícitos. Código pedidos/index.js:115-134 conserva una clave por tienda en RAM; no garantiza reinicio. |
| Diseño de idempotencia/saga o justificación | Cumple | [docs/evidencias/evidencias-s11.md:60-81](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/evidencias/evidencias-s11.md#L60-L81). Define ámbito, payload, conflicto, retención y límite de la clave; saga hipotética justificada si se extrae. |
| ADR de extracción con criterios | Cumple | [docs/adr/0019-no-extraccion-a-servicios.md:18-60](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/adr/0019-no-extraccion-a-servicios.md#L18-L60). Decide no extraer con escala, equipo, acoplamiento y disparadores. arc42:844-848 aclara aceptación sin alterar el texto propuesto original. |
| Alternativa no extraer evaluada | Cumple | [docs/adr/0019-no-extraccion-a-servicios.md:27-50](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/adr/0019-no-extraccion-a-servicios.md#L27-L50). Compara pagos, notificaciones y no extraer, eligiendo explícitamente la última. |
| arc42 §11 con modos de fallo | Cumple | [docs/arc42/arc42-template-EN.md:712-729](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/arc42/arc42-template-EN.md#L712-L729). Modos F-01 a F-06 y estado real de mitigación actualizados. |
| Aspectos afectados al día | Cumple | [docs/aspectos.md:11-17](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/aspectos.md#L11-L17). A-01 enlaza integración, prueba FIFO y evidencia S11. Falta completar enlace directo a ADR-0019 y pruebas de idempotencia; la cadena vigente sí conduce al detalle de la semana. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita); no se usó API de repositorios. |
| Estructura mínima | Cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. Esto no acredita completitud de sus secciones. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Corte exclusivo verificado. |
| Nombres de ADR | Cumple | Inventario completo docs/adr/ del hash citado: nombres NNNN-titulo-en-kebab-case.md. |
| ADR aceptados no reescritos | No cumple | docs/aspectos.md:23 registra once ADR editados tras aceptación; el historial conserva modificaciones en 68c8c08 de ADR-0003/0010. ADR-0015 ratifica, pero no elimina la reescritura histórica. Diferenciar cambios de estado/reemplazo legítimos de cambios de contenido. |
| Bitácora IA vigente | Cumple | docs/ia.md registra sesiones hasta 18/10 y rechazo de idempotencia obligatoria incompatible con v1; commit 79a3136 actualiza la bitácora. |
| Pipeline, Sonar y Quality Gate públicos | No verificado | [Deploy Dokploy (laboratorio de la U)](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/39192292623): success; [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/39192292599): success Inspección de workflows; no se ejecutó código localmente. [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_LaPlacita). Consulta pública de estado devolvió HTTP 403; Quality Gate no verificado en vivo, aun cuando exista paso configurado. |
| Sin credenciales actuales ni históricas | No verificado | Búsqueda estática de patrones de credenciales y revisión de configuraciones; el barrido histórico por git log -S no terminó dentro de esta pasada. No se afirma ausencia exhaustiva; falta cerrar el historial sin divulgar valores. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**9/9 criterios de la ficha. Nota sugerida: 5.0/5.0**, resultado de `1 + 4 × (9/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo.

## Overall · punta actual

Punta observada: [`0c9ce082b5850baf1ecda75e82d20757d0101234`](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/0c9ce082b5850baf1ecda75e82d20757d0101234), `2026-10-18T21:56:00-05:00`, misma rama principal. Punta y corte coinciden. Backend y PWA han avanzado, con claves idempotentes limitadas a memoria y escritura FIFO por pedido; el 201 todavía no garantiza persistencia PostgreSQL. La cola ordena las escrituras, pero no equivale a outbox durable. Redis, push y pasarela real siguen declarados como futuros/no integrados. Completar S12 desde esta semántica real.

## Fallos probados frente a descritos

backend/tests/idempotencia.test.js:13-45 cubre repetición, conflicto de payload, ausencia de clave y ámbito por tienda. backend/tests/cola-escrituras.test.js contiene la regresión de reordenación; CI del hash es exitoso. El defecto y su restauración están reportados en evidencias-s11.md:151-168, no reejecutados por esta auditoría. Caída/ack perdido y recuperación durable de claves siguen sin acreditarse.

## Pendientes prioritarios

La evidencia distingue los mecanismos presentes de las mitigaciones planificadas y evalúa explícitamente no extraer. La deduplicación actual está limitada a memoria del proceso y no ofrece durabilidad tras reinicio. Mantengan trazabilidad e inmutabilidad de decisiones históricas, sin presentar una ratificación como eliminación de las ediciones anteriores.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
