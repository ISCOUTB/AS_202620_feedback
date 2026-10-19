# AS_202620_GimnasioUTB · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/tree/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado: DEFINITIVA S11**.

- Rama: `origin/main`; commit evaluado: [`2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf), fecha `2026-10-18T22:02:01-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 9 commits durante S11; 1 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Integración principal identificada en el código | Cumple | [src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js:39-107](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js#L39-L107). API → PostgreSQL mediante pg; lectura y transición del contador identificadas, además del borde HTTP. |
| Tabla de fallos: no responde, tarde y dos veces | Cumple | [docs/s11-fallos-parciales.md:24-36](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/docs/s11-fallos-parciales.md#L24-L36). F1/F3/F4/F5 cubren ausencia, demora y repetición de respuesta sobre el aforo real. |
| Mitigación asignada a cada fallo | Cumple | [docs/s11-fallos-parciales.md:26-36](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/docs/s11-fallos-parciales.md#L26-L36). Cada fallo tiene táctica: idempotencia, timeout, backoff, atomicidad o cierre ordenado; FCM e identidad son futuros. |
| Correspondencia o pendiente explícito con plan | Cumple | [docs/s11-fallos-parciales.md:136-159](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/docs/s11-fallos-parciales.md#L136-L159). Separa IMPLEMENTADO, DISEÑO y FUTURO; detalla archivos y pruebas pendientes. Pool sin timeouts en aforo-postgres.adapter.js:73-76 y transacción:39-59 concuerdan. No se exige implementar todo en S11. |
| Diseño de idempotencia/saga o justificación | Cumple | [docs/s11-fallos-parciales.md:42-159](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/docs/s11-fallos-parciales.md#L42-L159). Clave por intención, payload conflictivo, retención 24 h y registro dentro de la misma transacción. Saga solo hipotética, justificada en 202-218. |
| ADR de extracción con criterios | Cumple | [docs/adr/0005-no-extraer-notificaciones.md:24-88](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/docs/adr/0005-no-extraer-notificaciones.md#L24-L88). No extraer Notificaciones; criterios de escala, aislamiento, datos, operación y disparadores medibles. |
| Alternativa no extraer evaluada | Cumple | [docs/adr/0005-no-extraer-notificaciones.md:26-59](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/docs/adr/0005-no-extraer-notificaciones.md#L26-L59). Alternativa A no extraer comparada con servicio+broker y servicio+HTTP. |
| arc42 §11 con modos de fallo | Cumple | [docs/arc42/arc42_gimnasio_utb.md:288-321](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/docs/arc42/arc42_gimnasio_utb.md#L288-L321). F1–F11 incorporados con mitigaciones y estado de implementación. |
| Aspectos afectados al día | No cumple | [docs/aspectos.md:29-35](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2f97dbc42cc957f35f9aab280dfb8122bdbeb6bf/docs/aspectos.md#L29-L35). La tabla sigue limitada a consistencia del contador y ADR-0001/0004; no incorpora ADR-0005, idempotencia, timeouts ni enlaces a las pruebas pendientes S11. Actualizar la fila afectada. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_GimnasioUTB](https://github.com/ISCOUTB/AS_202620_GimnasioUTB); no se usó API de repositorios. |
| Estructura mínima | Cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. Esto no acredita completitud de sus secciones. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Corte exclusivo verificado. |
| Nombres de ADR | No cumple | Fuera de convención: docs/adr/ADR0001.md |
| ADR aceptados no reescritos | No cumple | docs/adr/0005-no-extraer-notificaciones.md:5: aceptado el 18/10; commit 1d63ed2 modifica el contenido aceptado creado en 8909a1b, sin ADR sustituto. |
| Bitácora IA vigente | Cumple | docs/ia.md:128-142; commit 4f61931 registra S11, verificación y rechazo razonado de implementación prematura. |
| Pipeline, Sonar y Quality Gate públicos | No cumple | [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/39192779430): success Inspección de workflows; no se ejecutó código localmente. No se encontró configuración SonarCloud/Quality Gate en el árbol revisado. |
| Sin credenciales actuales ni históricas | No verificado | Búsqueda estática de patrones de credenciales y revisión de configuraciones; el barrido histórico por git log -S no terminó dentro de esta pasada. No se afirma ausencia exhaustiva; falta cerrar el historial sin divulgar valores. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**8/9 criterios de la ficha. Nota sugerida: 4.6/5.0**, resultado de `1 + 4 × (8/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo.

## Overall · punta actual

Punta observada: [`2227faf9919983e5835d484a848301d67a0e5866`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/2227faf9919983e5835d484a848301d67a0e5866), `2026-10-19T16:20:32-05:00`, misma rama principal. El único commit posterior al cierre incorpora AforoApi en Flutter con GET/POST reales y timeout de 8 s (docs/Flutter/lib/core/api/aforo_api.dart:24-89), pantallas y pruebas. No cambia retroactivamente S11. No incorpora Idempotency-Key ni idempotencia durable; timeout del cliente no equivale a deduplicación. arc42 y C4 todavía describen Flutter como no integrado y deben reconciliarse con esta punta. Backend conserva transacción PostgreSQL; QR, identidad y FCM siguen fuera del alcance implementado.

## Fallos probados frente a descritos

Pruebas PostgreSQL de rollback y 20 entradas concurrentes existen en tests/postgres/aforo-postgres.integration.test.js:58-97, pero CI (.github/workflows/ci.yml:15-23) no ejecuta test:postgres. El run verde acredita base/contrato/arquitectura, no crash real, COMMIT incierto, idempotencia o FCM; estos son diseños o pruebas pendientes.

## Pendientes prioritarios

El análisis de fallos distingue implementación, diseño y trabajo futuro; el plan de idempotencia es válido para esta evidencia. Actualicen aspectos con la decisión de extracción y las mitigaciones, y conserven los ADR aceptados sin reescribirlos. Las pruebas de PostgreSQL existen, pero el workflow citado no las ejecuta.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
