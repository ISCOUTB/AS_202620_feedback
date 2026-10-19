# AS_202620_LaPlacita · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_LaPlacita/tree/0c9ce082b5850baf1ecda75e82d20757d0101234) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR S12; no es cierre ni nota final**.

- Rama: `origin/master`; commit evaluado: [`0c9ce082b5850baf1ecda75e82d20757d0101234`](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/0c9ce082b5850baf1ecda75e82d20757d0101234), fecha `2026-10-18T21:56:00-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 52 commits durante S11; 0 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Tabla operación → garantía con operaciones reales | No cumple | [docs/arc42/arc42-template-EN.md:401-426](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/arc42/arc42-template-EN.md#L401-L426). Se describe propiedad de datos, pero falta tabla operación → garantía. Explicitar diferencia entre memoria y escritura asíncrona durable. |
| Dos operaciones verificadas contra implementación | No cumple | [backend/src/modules/pedidos/index.js:75-105](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/backend/src/modules/pedidos/index.js#L75-L105). Crear pedido muta RAM y llama escribirPedido sin esperar durabilidad; cambiarEstado:156-173 hace lo mismo. Falta garantía declarada por operación para contrastar ambos caminos. |
| Caché: qué, dónde y cuánto | No cumple | [docs/c4/contenedores.md:24-25](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/c4/contenedores.md#L24-L25). Redis está planeado, sin qué/dónde/cuánto completo. El almacén de claves de S11 no sustituye una estrategia de caché para el sistema. |
| Invalidación tras escritura | No cumple | [docs/arc42/arc42-template-EN.md:401-426](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/arc42/arc42-template-EN.md#L401-L426). No hay política S12 para invalidar lectura de catálogo o pedidos tras escritura. Precisar actualización de precio y cambio de estado. |
| Garantías de eventos, si existen | Cumple | [docs/evidencias/evidencias-s11.md:74-81](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/evidencias/evidencias-s11.md#L74-L81). Flujo actual síncrono en proceso; saga/outbox propuestos solo al extraer. No se exige broker inexistente. |
| ADR de la decisión de datos más costosa de revertir | No cumple | [docs/adr/0019-no-extraccion-a-servicios.md:27-60](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/adr/0019-no-extraccion-a-servicios.md#L27-L60). No identifica una decisión de datos como la más costosa de revertir; ADR de extracción no reemplaza ese entregable. |
| Razón y costo de reversión | No cumple | [docs/adr/0019-no-extraccion-a-servicios.md:52-60](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/adr/0019-no-extraccion-a-servicios.md#L52-L60). No hay comparación del costo de reversión de decisiones de datos; agregar migración, cambio de contrato y recuperación necesarios. |
| Almacenes/brokers propios y tecnología en C4 L2 | Cumple | [docs/c4/contenedores.md:20-38](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/c4/contenedores.md#L20-L38). PostgreSQL y Redis aparecen con tecnología y estado implementado/planeado. Redis no se acredita como operativo. |
| arc42 §8: consistencia y caché | No cumple | [docs/arc42/arc42-template-EN.md:401-426](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/docs/arc42/arc42-template-EN.md#L401-L426). Sección 8 tiene glosario, propietarios y reglas; no la estrategia de consistencia y caché requerida. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita); no se usó API de repositorios. |
| Estructura mínima | Cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. Esto no acredita completitud de sus secciones. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Observación preliminar, no estado futuro de cierre. |
| Nombres de ADR | Cumple | Inventario completo docs/adr/ del hash citado: nombres NNNN-titulo-en-kebab-case.md. |
| ADR aceptados no reescritos | No cumple | docs/aspectos.md:23 registra once ADR editados tras aceptación; el historial conserva modificaciones en 68c8c08 de ADR-0003/0010. ADR-0015 ratifica, pero no elimina la reescritura histórica. Diferenciar cambios de estado/reemplazo legítimos de cambios de contenido. |
| Bitácora IA vigente | No cumple | docs/ia.md registra sesiones hasta 18/10 y rechazo de idempotencia obligatoria incompatible con v1; commit 79a3136 actualiza la bitácora. La lectura no encontró registro específico S12 con usos, aceptación/rechazo y motivo; incumplimiento documental preliminar, subsanable durante la semana. |
| Pipeline, Sonar y Quality Gate públicos | No verificado | [Deploy Dokploy (laboratorio de la U)](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/39192292623): success; [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/39192292599): success Inspección de workflows; no se ejecutó código localmente. [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_LaPlacita). Consulta pública de estado devolvió HTTP 403; Quality Gate no verificado en vivo, aun cuando exista paso configurado. |
| Sin credenciales actuales ni históricas | No verificado | Búsqueda estática de patrones de credenciales y revisión de configuraciones; el barrido histórico por git log -S no terminó dentro de esta pasada. No se afirma ausencia exhaustiva; falta cerrar el historial sin divulgar valores. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**2/9 criterios de la ficha. Nota sugerida: 1.9/5.0**, resultado de `1 + 4 × (2/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo. S12 es PRELIMINAR y puede cambiar hasta su cierre.

## Overall · punta actual

Punta observada: [`0c9ce082b5850baf1ecda75e82d20757d0101234`](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/0c9ce082b5850baf1ecda75e82d20757d0101234), `2026-10-18T21:56:00-05:00`, misma rama principal. Punta y corte coinciden. Backend y PWA han avanzado, con claves idempotentes limitadas a memoria y escritura FIFO por pedido; el 201 todavía no garantiza persistencia PostgreSQL. La cola ordena las escrituras, pero no equivale a outbox durable. Redis, push y pasarela real siguen declarados como futuros/no integrados. Completar S12 desde esta semántica real.

## Fallos probados frente a descritos

backend/tests/idempotencia.test.js:13-45 cubre repetición, conflicto de payload, ausencia de clave y ámbito por tienda. backend/tests/cola-escrituras.test.js contiene la regresión de reordenación; CI del hash es exitoso. El defecto y su restauración están reportados en evidencias-s11.md:151-168, no reejecutados por esta auditoría. Caída/ack perdido y recuperación durable de claves siguen sin acreditarse.

## Pendientes prioritarios

La siguiente entrega necesita tabla operación–consistencia y contraste de dos operaciones, especialmente el desacople entre memoria y escritura PostgreSQL. Faltan política de caché/invalidación y ADR de la decisión de datos más costosa de revertir. Redis y outbox deben conservarse identificados como futuros mientras no estén implementados.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
