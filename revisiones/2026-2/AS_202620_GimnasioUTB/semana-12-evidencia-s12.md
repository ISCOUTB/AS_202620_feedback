# AS_202620_GimnasioUTB · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/tree/2227faf9919983e5835d484a848301d67a0e5866) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR S12; no es cierre ni nota final**.

- Rama: `origin/main`; commit evaluado: [`2227faf9919983e5835d484a848301d67a0e5866`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/2227faf9919983e5835d484a848301d67a0e5866), fecha `2026-10-19T16:20:32-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 9 commits durante S11; 1 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Tabla operación → garantía con operaciones reales | No cumple | [docs/arc42/arc42_gimnasio_utb.md:227-245](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2227faf9919983e5835d484a848301d67a0e5866/docs/arc42/arc42_gimnasio_utb.md#L227-L245). Describe transacción y métricas, pero no tabla operación → garantía para consulta, entrada y salida. |
| Dos operaciones verificadas contra implementación | No cumple | [src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js:39-107](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2227faf9919983e5835d484a848301d67a0e5866/src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js#L39-L107). Lectura y actualización son inspeccionables, pero falta la declaración por operación que permita contrastar dos garantías S12; no se sustituye por inferencia del evaluador. |
| Caché: qué, dónde y cuánto | No cumple | [docs/arc42/arc42_gimnasio_utb.md:221-245](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2227faf9919983e5835d484a848301d67a0e5866/docs/arc42/arc42_gimnasio_utb.md#L221-L245). No hay estrategia de caché con qué/dónde/cuánto, ni decisión argumentada de no utilizarla. |
| Invalidación tras escritura | No cumple | [docs/arc42/arc42_gimnasio_utb.md:221-245](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2227faf9919983e5835d484a848301d67a0e5866/docs/arc42/arc42_gimnasio_utb.md#L221-L245). No se declara invalidación tras registrar una entrada/salida; describir el refresco del contador o justificar no cachearlo. |
| Garantías de eventos, si existen | Cumple | [docs/s11-fallos-parciales.md:161-200](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2227faf9919983e5835d484a848301d67a0e5866/docs/s11-fallos-parciales.md#L161-L200). Outbox futuro declara al menos una vez, duplicados y límites FCM; no se presenta como broker o consumidor existente. |
| ADR de la decisión de datos más costosa de revertir | No cumple | [docs/adr/0005-no-extraer-notificaciones.md:38-77](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2227faf9919983e5835d484a848301d67a0e5866/docs/adr/0005-no-extraer-notificaciones.md#L38-L77). ADR de extracción analiza reversibilidad, pero no selecciona la decisión de datos más costosa de revertir. Inventario docs/adr:0001,0003,0004,0005,ADR0001. |
| Razón y costo de reversión | No cumple | [docs/adr/0005-no-extraer-notificaciones.md:46-50](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2227faf9919983e5835d484a848301d67a0e5866/docs/adr/0005-no-extraer-notificaciones.md#L46-L50). Hay costo de extracción hipotética, no comparación del costo de revertir la decisión de datos seleccionada. |
| Almacenes/brokers propios y tecnología en C4 L2 | Cumple | [docs/c4/c4_level2.md:7-25](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2227faf9919983e5835d484a848301d67a0e5866/docs/c4/c4_level2.md#L7-L25). PostgreSQL como ContainerDb con tecnología; no hay broker implementado y se distingue el futuro. |
| arc42 §8: consistencia y caché | No cumple | [docs/arc42/arc42_gimnasio_utb.md:221-245](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/2227faf9919983e5835d484a848301d67a0e5866/docs/arc42/arc42_gimnasio_utb.md#L221-L245). Consistencia presente, caché ausente: sección 8 incompleta para S12. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_GimnasioUTB](https://github.com/ISCOUTB/AS_202620_GimnasioUTB); no se usó API de repositorios. |
| Estructura mínima | Cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. Esto no acredita completitud de sus secciones. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Observación preliminar, no estado futuro de cierre. |
| Nombres de ADR | No cumple | Fuera de convención: docs/adr/ADR0001.md |
| ADR aceptados no reescritos | No cumple | docs/adr/0005-no-extraer-notificaciones.md:5: aceptado el 18/10; commit 1d63ed2 modifica el contenido aceptado creado en 8909a1b, sin ADR sustituto. |
| Bitácora IA vigente | No cumple | docs/ia.md:128-142; commit 4f61931 registra S11, verificación y rechazo razonado de implementación prematura. La lectura no encontró registro específico S12 con usos, aceptación/rechazo y motivo; incumplimiento documental preliminar, subsanable durante la semana. |
| Pipeline, Sonar y Quality Gate públicos | No cumple | [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/39327011165): success Inspección de workflows; no se ejecutó código localmente. No se encontró configuración SonarCloud/Quality Gate en el árbol revisado. |
| Sin credenciales actuales ni históricas | No verificado | Búsqueda estática de patrones de credenciales y revisión de configuraciones; el barrido histórico por git log -S no terminó dentro de esta pasada. No se afirma ausencia exhaustiva; falta cerrar el historial sin divulgar valores. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**2/9 criterios de la ficha. Nota sugerida: 1.9/5.0**, resultado de `1 + 4 × (2/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo. S12 es PRELIMINAR y puede cambiar hasta su cierre.

## Overall · punta actual

Punta observada: [`2227faf9919983e5835d484a848301d67a0e5866`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/2227faf9919983e5835d484a848301d67a0e5866), `2026-10-19T16:20:32-05:00`, misma rama principal. El único commit posterior al cierre incorpora AforoApi en Flutter con GET/POST reales y timeout de 8 s (docs/Flutter/lib/core/api/aforo_api.dart:24-89), pantallas y pruebas. No cambia retroactivamente S11. No incorpora Idempotency-Key ni idempotencia durable; timeout del cliente no equivale a deduplicación. arc42 y C4 todavía describen Flutter como no integrado y deben reconciliarse con esta punta. Backend conserva transacción PostgreSQL; QR, identidad y FCM siguen fuera del alcance implementado.

## Fallos probados frente a descritos

Pruebas PostgreSQL de rollback y 20 entradas concurrentes existen en tests/postgres/aforo-postgres.integration.test.js:58-97, pero CI (.github/workflows/ci.yml:15-23) no ejecuta test:postgres. El run verde acredita base/contrato/arquitectura, no crash real, COMMIT incierto, idempotencia o FCM; estos son diseños o pruebas pendientes.

## Pendientes prioritarios

El cliente Flutter ya llama a la API y aplica timeout; falta reconciliar ese avance con arc42 y C4. Para completar datos, declaren garantías por operación, justifiquen caché e invalidación y seleccionen la decisión de datos más difícil de revertir. El timeout del cliente no proporciona idempotencia.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
