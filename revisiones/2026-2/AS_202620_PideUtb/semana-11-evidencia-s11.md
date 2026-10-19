# AS_202620_PideUtb · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_PideUtb/tree/2395d7812aa86ae98c177d58cbea0e927d9593d5) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado: DEFINITIVA S11**.

- Rama: `origin/master`; commit evaluado: [`2395d7812aa86ae98c177d58cbea0e927d9593d5`](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/2395d7812aa86ae98c177d58cbea0e927d9593d5), fecha `2026-10-18T18:40:46-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 44 commits durante S11; 0 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Integración principal identificada en el código | Cumple | [backend/app/pagos/service.py:125-202](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/backend/app/pagos/service.py#L125-L202). iniciar_intento construye URL, no HTTP saliente; procesar_evento recibe webhook e invoca Pedidos y Pagos. PostgreSQL por TCP sigue siendo red aunque sea contenedor vecino. |
| Tabla de fallos: no responde, tarde y dos veces | Cumple | [docs/arc42/arc42.md:669-745](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/arc42/arc42.md#L669-L745). §6.5 y §6.7 cubren evento ausente/tardío/repetido, BD que no responde, respuesta perdida y corte entre escrituras. |
| Mitigación asignada a cada fallo | Cumple | [docs/arc42/arc42.md:732-819](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/arc42/arc42.md#L732-L819). Estado pendiente consultable, idempotencia, health y conciliación asignados; sin exigir breaker hacia una llamada a pasarela inexistente. |
| Correspondencia o pendiente explícito con plan | Cumple | [backend/app/pagos/service.py:187-247](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/backend/app/pagos/service.py#L187-L247). Dos commits separados y conciliación concuerdan con S11; no se oculta la ventana. Pool tiene timeout en base_de_datos.py:85-90,124-129. Recuperación del despliegue no se infiere de pruebas unitarias. |
| Diseño de idempotencia/saga o justificación | Cumple | [docs/arc42/arc42.md:1236-1307](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/arc42/arc42.md#L1236-L1307). Tres mecanismos identificados y no saga razonada; repository.marcar_pagado:145-150 usa UPDATE condicional real. No se extrapola al avance de estado. |
| ADR de extracción con criterios | Cumple | [docs/adr/0009-no-extraer-un-servicio.md:19-138](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/adr/0009-no-extraer-un-servicio.md#L19-L138). Evalúa pagos y decide no extraer con restricciones de recursos, equipo, datos y disparadores. |
| Alternativa no extraer evaluada | Cumple | [docs/adr/0009-no-extraer-un-servicio.md:65-103](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/adr/0009-no-extraer-un-servicio.md#L65-L103). Compara monolito actual y extracción, eligiendo explícitamente no extraer. |
| arc42 §11 con modos de fallo | Cumple | [docs/arc42/arc42.md:2114-2221](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/arc42/arc42.md#L2114-L2221). Riesgos de bus por proceso, instancia única, proxy y deuda de configuración incorporados, con enlace a fallos §6.7. Las mejoras etiquetadas S12–S14 ya estaban integradas antes del cierre. |
| Aspectos afectados al día | Cumple | [docs/aspectos.md:19-24](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/aspectos.md#L19-L24). ESC-04/05 enlazan pagos, idempotencia, repetición y conservación de pedido. Completar enlace directo a ADR-0009 y conciliación para facilitar la revisión. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_PideUtb](https://github.com/ISCOUTB/AS_202620_PideUtb); no se usó API de repositorios. |
| Estructura mínima | Cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. Esto no acredita completitud de sus secciones. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Corte exclusivo verificado. |
| Nombres de ADR | Cumple | Inventario completo docs/adr/ del hash citado: nombres NNNN-titulo-en-kebab-case.md. |
| ADR aceptados no reescritos | No cumple | Historial 32abc9d modifica ADR-0007 aceptado; 59ec90c cambia el título de ADR-0008 y documenta la reversión de la decisión de origen único. La sustitución declarada ADR-0004→0008 es distinta y válida; no justifica reescrituras de otros ADR. |
| Bitácora IA vigente | No cumple | docs/ia.md termina en S9 (últimas secciones:259-353); commit 07dc813 del periodo corrige información previa, pero no registra usos/aceptados/rechazados correspondientes a S11/S12. |
| Pipeline, Sonar y Quality Gate públicos | No verificado | [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39177528726): success Inspección de workflows; no se ejecutó código localmente. [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_PideUtb). Consulta pública de estado devolvió HTTP 403; Quality Gate no verificado en vivo, aun cuando exista paso configurado. |
| Sin credenciales actuales ni históricas | No cumple | backend/pagos/service.py:27-43 documenta exposición histórica y retirada/rotación de credencial. La rotación declarada reduce el riesgo actual, pero no demuestra ausencia histórica; no se publica ningún valor. No se verificó su vigencia contra el servicio. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**9/9 criterios de la ficha. Nota sugerida: 5.0/5.0**, resultado de `1 + 4 × (9/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo.

## Overall · punta actual

Punta observada: [`2395d7812aa86ae98c177d58cbea0e927d9593d5`](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/2395d7812aa86ae98c177d58cbea0e927d9593d5), `2026-10-18T18:40:46-05:00`, misma rama principal. Punta y corte coinciden. PR 24, PR 25 (datos y eventos), PR 26 (rama de fallos parciales) y PR 27 (corrección migración) constan integrados antes del corte; se evalúa su código, no solo la etiqueta semanal. El bus carece de suscriptores; el panel usa sondeo, ahora 5 s, mientras S12/ADR-0010 conservan 8 s. La tabla sobrestima atomicidad del avance de estado y el C4 mantiene una llamada a pasarela inexistente. El equipo documenta caída 404 de unos 30 minutos por checksum de migración; el fix está versionado, pero la recuperación pública no fue verificada en esta auditoría. CI exitoso no acredita servicio recuperado.

## Fallos probados frente a descritos

backend/tests/test_fallos_parciales.py:71-174 inyecta fallo entre escrituras, detecta conciliación y verifica reintento sin segundo código; :176-226 cubre publicación tras persistir, suscriptor fallido y ausencia de suscriptores. CI exitoso del hash es citable. No se ejecutó código ni se prueba desde aquí disponibilidad, restauración de backup o carrera entre avances de estado.

## Pendientes prioritarios

La tabla de fallos, las pruebas de conciliación y la decisión razonada de no extraer cubren la evidencia. No confundan el run verde ni la corrección de la migración con recuperación de producción comprobada. Actualicen la bitácora de IA y preserven los ADR aceptados mediante decisiones sucesoras.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
