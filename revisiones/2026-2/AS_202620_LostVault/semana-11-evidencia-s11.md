# AS_202620_LostVault · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_LostVault/tree/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado: DEFINITIVA S11**.

- Rama: `origin/main`; commit evaluado: [`34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f`](https://github.com/ISCOUTB/AS_202620_LostVault/commit/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f), fecha `2026-10-18T20:43:15-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 4 commits durante S11; 0 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Integración principal identificada en el código | Cumple | [backend/main.py:234-290](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/backend/main.py#L234-L290). API de reclamación y cambio de estado implementados; cliente Flutter aún no llama HTTP, según evidencia S11:20-27. |
| Tabla de fallos: no responde, tarde y dos veces | Cumple | [docs/fallos-parciales/s11-fallos-parciales.md:29-39](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/fallos-parciales/s11-fallos-parciales.md#L29-L39). F1/F2/F3 cubren no responde, tardía y repetida; agrega multinstancia y reutilización de clave. |
| Mitigación asignada a cada fallo | Cumple | [docs/fallos-parciales/s11-fallos-parciales.md:33-39](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/fallos-parciales/s11-fallos-parciales.md#L33-L39). Timeout, clave/deduplicación natural, backoff, breaker y persistencia compartida con restricciones. |
| Correspondencia o pendiente explícito con plan | Cumple | [backend/main.py:234-290](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/backend/main.py#L234-L290). Clave y bloqueo locales concuerdan con diseño; cliente/backoff/breaker y PostgreSQL quedan pendientes declarados con plan en S11:33-38. No se confunde RAM con garantía entre instancias. |
| Diseño de idempotencia/saga o justificación | Cumple | [docs/fallos-parciales/s11-fallos-parciales.md:41-126](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/fallos-parciales/s11-fallos-parciales.md#L41-L126). Clave por usuario, conflicto, TTL 24 h y deduplicación natural; saga hipotética con compensaciones y outbox futuro. |
| ADR de extracción con criterios | Cumple | [docs/adr/0005-no-extraer-verificacion-identidad.md:37-119](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/adr/0005-no-extraer-verificacion-identidad.md#L37-L119). No extraer verificación de identidad, comparando seguridad, escala, equipo, latencia y persistencia. |
| Alternativa no extraer evaluada | Cumple | [docs/adr/0005-no-extraer-verificacion-identidad.md:39-45](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/adr/0005-no-extraer-verificacion-identidad.md#L39-L45). Opción A no extraer evaluada contra HTTP y saga; no es ausencia de decisión. |
| arc42 §11 con modos de fallo | Cumple | [docs/arc42/11_riesgos.md:10-34](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/arc42/11_riesgos.md#L10-L34). R1–R7 trazan los modos y aclaran límites de instancia y cliente sin adaptador HTTP. |
| Aspectos afectados al día | No cumple | [docs/aspectos.md:9-14](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/aspectos.md#L9-L14). AS-03 mantiene trazabilidad Flutter/ADR-0001 y pruebas anteriores; no enlaza ADR-0005, idempotencia backend, riesgos nuevos ni pruebas S11. Actualizar esta fila y la disponibilidad afectada. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_LostVault](https://github.com/ISCOUTB/AS_202620_LostVault); no se usó API de repositorios. |
| Estructura mínima | No cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. El contrato §2 exige arc42 secciones 1–12: la sección 08 no aparece en el inventario ni se localizó su contenido equivalente. Los demás artefactos están localizados; se registra la incompletitud estructural sin añadir descuentos al recuento de la ficha. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Corte exclusivo verificado. |
| Nombres de ADR | No cumple | Fuera de convención: docs/adr/000.3-despliegue-busqueda-lostvault.md |
| ADR aceptados no reescritos | No cumple | docs/adr/0002-integracion-reclamacion-api.md:3-4 ya estaba aceptado; 43794ae añade en :83-85 un enlace y una aclaración de idempotencia. Es una edición documental del ADR aceptado, no un cambio probado de la decisión original; el contrato prohíbe editarlo y permite marcar reemplazo con sucesor. |
| Bitácora IA vigente | Cumple | docs/ia.md:225-273, commit d1d20c2: S11, aceptado/rechazado y límites de RAM/cliente documentados. |
| Pipeline, Sonar y Quality Gate públicos | No verificado | [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39186637229): success; [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39186637112): success; [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39186637073): success Inspección de workflows; no se ejecutó código localmente. [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_LostVault). Consulta pública de estado devolvió HTTP 403; Quality Gate no verificado en vivo, aun cuando exista paso configurado. |
| Sin credenciales actuales ni históricas | No verificado | Búsqueda estática de patrones de credenciales y revisión de configuraciones; el barrido histórico por git log -S no terminó dentro de esta pasada. No se afirma ausencia exhaustiva; falta cerrar el historial sin divulgar valores. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**8/9 criterios de la ficha. Nota sugerida: 4.6/5.0**, resultado de `1 + 4 × (8/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo.

## Overall · punta actual

Punta observada: [`34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f`](https://github.com/ISCOUTB/AS_202620_LostVault/commit/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f), `2026-10-18T20:43:15-05:00`, misma rama principal. Punta y corte coinciden. La idempotencia está implementada y probada en memoria de un proceso; reinicios y múltiples funciones Vercel no comparten claves ni objetos. PostgreSQL es plan, no persistencia existente. Flutter sigue con adaptadores en memoria; timeout/backoff/breaker del cliente están especificados, no implementados. Persiste la divergencia entre modularidad Flutter y backend concentrado en main.py.

## Fallos probados frente a descritos

backend/test_api.py:125-217 cubre reintento, clave conflictiva, expiración y concurrencia dentro del proceso; Backend checks del hash es exitoso. No acredita múltiples instancias, reinicio con recuperación ni red Flutter→API. Estos modos deben conservarse como pendientes, no como resiliencia desplegada.

## Pendientes prioritarios

El backend tiene deduplicación y exclusión mutua locales, y el diseño reconoce sus límites frente a reinicio o varias instancias. Actualicen aspectos para enlazar los fallos, la decisión de extracción y sus pruebas. La propagación de la clave desde Flutter sigue pendiente y no debe presentarse como completada.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
