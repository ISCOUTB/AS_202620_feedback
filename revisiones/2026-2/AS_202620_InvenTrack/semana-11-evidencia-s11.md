# AS_202620_InvenTrack · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_InvenTrack/tree/28506a8eabcde2234e56698d13ae1d8ae8d0ee24) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado: DEFINITIVA S11**.

- Rama: `origin/main`; commit evaluado: [`28506a8eabcde2234e56698d13ae1d8ae8d0ee24`](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/28506a8eabcde2234e56698d13ae1d8ae8d0ee24), fecha `2026-10-18T22:29:12-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 15 commits durante S11; 0 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Integración principal identificada en el código | Cumple | [app/inventario/infrastructure/validador_producto_adapter.py:5-12](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/app/inventario/infrastructure/validador_producto_adapter.py#L5-L12). Inventario llama a ConsultarProducto mediante un adaptador en proceso, no un servicio HTTP actualmente. |
| Tabla de fallos: no responde, tarde y dos veces | Cumple | [docs/retos/fallos-distribuidos-s11.md:20-26](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/retos/fallos-distribuidos-s11.md#L20-L26). Tabla contextualizada con no responde, responde tarde y duplicidad; distingue la extracción hipotética. |
| Mitigación asignada a cada fallo | Cumple | [docs/retos/fallos-distribuidos-s11.md:24-26](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/retos/fallos-distribuidos-s11.md#L24-L26). Asignación de timeout/breaker, espera de lock e Idempotency-Key a los tres modos. |
| Correspondencia o pendiente explícito con plan | No cumple | [docs/retos/fallos-distribuidos-s11.md:25-40](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/retos/fallos-distribuidos-s11.md#L25-L40). La tabla declara duplicidad mitigada por serialización; el código registrar_movimiento.py:37-78 vuelve a aplicar cada comando y no deduplica. ADR-0011:35-48 y arc42:810 sí lo reconocen como pendiente, pero la tabla mantiene la afirmación incompatible. Corregirla; no se penaliza el pendiente razonado. |
| Diseño de idempotencia/saga o justificación | Cumple | [docs/adr/0011-idempotencia-y-sagas-en-movimientos.md:29-57](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/adr/0011-idempotencia-y-sagas-en-movimientos.md#L29-L57). Diseño futuro de clave durable, mismo resultado/payload y rechazo de conflicto; no saga mientras no haya pasos distribuidos. |
| ADR de extracción con criterios | Cumple | [docs/adr/0010-decision-extraccion-microservicios.md:18-66](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/adr/0010-decision-extraccion-microservicios.md#L18-L66). Decisión no extraer sustentada por carga, costo, transacciones y fronteras. |
| Alternativa no extraer evaluada | Cumple | [docs/adr/0010-decision-extraccion-microservicios.md:20-33](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/adr/0010-decision-extraccion-microservicios.md#L20-L33). La opción B es explícitamente mantener el monolito. |
| arc42 §11 con modos de fallo | Cumple | [docs/arc42/arc42-template-EN.md:788-811](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/arc42/arc42-template-EN.md#L788-L811). Tabla vigente registra timeout, reinicio, reintento duplicado y planes de mitigación. |
| Aspectos afectados al día | Cumple | [docs/aspectos.md:15-19](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/aspectos.md#L15-L19). ASP-01 enlaza ADR-0010/0011, módulos, pruebas y evidencia; permite recorrer la integración. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_InvenTrack](https://github.com/ISCOUTB/AS_202620_InvenTrack); no se usó API de repositorios. |
| Estructura mínima | Cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. Esto no acredita completitud de sus secciones. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Corte exclusivo verificado. |
| Nombres de ADR | Cumple | Inventario completo docs/adr/ del hash citado: nombres NNNN-titulo-en-kebab-case.md. |
| ADR aceptados no reescritos | No verificado | docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md y arc42:795 declaran ediciones históricas; se requiere contrastar cada aceptación/reemplazo antes de cerrar toda la cadena histórica. No hubo modificación de ADR existentes en el intervalo S11 observado. |
| Bitácora IA vigente | Cumple | docs/ia.md:26, commit 28506a8: registro S10/S11 con rechazo explícito de presentar idempotencia como implementada. |
| Pipeline, Sonar y Quality Gate públicos | No verificado | [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/39194936605): success Inspección de workflows; no se ejecutó código localmente. [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_InvenTrack). Consulta pública de estado devolvió HTTP 403; Quality Gate no verificado en vivo, aun cuando exista paso configurado. |
| Sin credenciales actuales ni históricas | No verificado | Búsqueda estática de patrones de credenciales y revisión de configuraciones; el barrido histórico por git log -S no terminó dentro de esta pasada. No se afirma ausencia exhaustiva; falta cerrar el historial sin divulgar valores. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**8/9 criterios de la ficha. Nota sugerida: 4.6/5.0**, resultado de `1 + 4 × (8/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo.

## Overall · punta actual

Punta observada: [`28506a8eabcde2234e56698d13ae1d8ae8d0ee24`](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/28506a8eabcde2234e56698d13ae1d8ae8d0ee24), `2026-10-18T22:29:12-05:00`, misma rama principal. Punta y corte coinciden. Hay integración modular en proceso, almacenamiento RAM y lock por SKU con timeout 2 s; no idempotencia de comandos, persistencia SQL ni coordinación entre instancias. ADR-0011 corrige conceptualmente la deduplicación, pero no reemplaza la afirmación errónea de la tabla S11. S12 todavía carece de tabla de garantías y decisión de datos/reversión.

## Fallos probados frente a descritos

tests/inventario/test_degradacion_lock.py:19-37 fuerza contención y espera agotada; tests/inventario/test_concurrencia.py comprueba concurrencia local. CI Run Tests del hash revisado es exitoso. No demuestra recuperación de inventario tras reinicio ni deduplicación: son límites documentados, no pruebas aprobadas.

## Pendientes prioritarios

El análisis y la decisión de no extraer están trazados al inventario real. Corrijan la tabla que equipara serialización con prevención de duplicados: el ADR nuevo reconoce correctamente que la idempotencia sigue pendiente. La contención local tiene prueba, pero no demuestra durabilidad ni coordinación entre réplicas.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
