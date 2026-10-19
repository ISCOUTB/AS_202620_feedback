# AS_202620_InvenTrack · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_InvenTrack/tree/28506a8eabcde2234e56698d13ae1d8ae8d0ee24) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR S12; no es cierre ni nota final**.

- Rama: `origin/main`; commit evaluado: [`28506a8eabcde2234e56698d13ae1d8ae8d0ee24`](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/28506a8eabcde2234e56698d13ae1d8ae8d0ee24), fecha `2026-10-18T22:29:12-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 15 commits durante S11; 0 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Tabla operación → garantía con operaciones reales | No cumple | [docs/arc42/arc42-template-EN.md:530-568](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/arc42/arc42-template-EN.md#L530-L568). Mapa de propietarios y lock por SKU no sustituyen tabla operación → garantía. |
| Dos operaciones verificadas contra implementación | No cumple | [app/inventario/application/registrar_movimiento.py:37-93](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/app/inventario/application/registrar_movimiento.py#L37-L93). Entradas y salidas usan lock local con timeout, pero no hay tabla S12 para verificar las garantías. El lock no es persistencia ni coordinación entre réplicas. |
| Caché: qué, dónde y cuánto | No cumple | [docs/arc42/arc42-template-EN.md:530-568](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/arc42/arc42-template-EN.md#L530-L568). No se diseña caché ni se argumenta no necesitarla. Repositorios en memoria son almacén primario, no caché de datos durables. |
| Invalidación tras escritura | No cumple | [docs/arc42/arc42-template-EN.md:530-568](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/arc42/arc42-template-EN.md#L530-L568). Falta invalidación tras modificar stock o producto, o justificación de no caché. |
| Garantías de eventos, si existen | Cumple | [docs/adr/0011-idempotencia-y-sagas-en-movimientos.md:15-33](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/adr/0011-idempotencia-y-sagas-en-movimientos.md#L15-L33). Declara monolito síncrono sin coordinación distribuida. No se exige inventar broker o garantías para un flujo por eventos inexistente. |
| ADR de la decisión de datos más costosa de revertir | No cumple | [docs/adr/0011-idempotencia-y-sagas-en-movimientos.md:19-57](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/adr/0011-idempotencia-y-sagas-en-movimientos.md#L19-L57). ADRs 0010/0011 tratan extracción/idempotencia, no seleccionan decisión de datos más costosa de revertir. |
| Razón y costo de reversión | No cumple | [docs/adr/0011-idempotencia-y-sagas-en-movimientos.md:50-57](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/adr/0011-idempotencia-y-sagas-en-movimientos.md#L50-L57). No cuantifica ni compara esfuerzo de reversión de una decisión de datos seleccionada. |
| Almacenes/brokers propios y tecnología en C4 L2 | No cumple | [docs/c4/containers.md:18-35](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/c4/containers.md#L18-L35). El diagrama representa objetos RAM como almacén/contenedor separado, aunque viven dentro del proceso API y no son un contenedor independiente. Las alternativas SQL están declaradas futuras; no hay broker vigente. No basta rotular la tecnología: debe corregirse el límite C4 para representar fielmente el almacenamiento implementado. |
| arc42 §8: consistencia y caché | No cumple | [docs/arc42/arc42-template-EN.md:530-568](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/docs/arc42/arc42-template-EN.md#L530-L568). Describe concurrencia, pero falta estrategia conjunta de consistencia y caché S12. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_InvenTrack](https://github.com/ISCOUTB/AS_202620_InvenTrack); no se usó API de repositorios. |
| Estructura mínima | Cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. Esto no acredita completitud de sus secciones. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Observación preliminar, no estado futuro de cierre. |
| Nombres de ADR | Cumple | Inventario completo docs/adr/ del hash citado: nombres NNNN-titulo-en-kebab-case.md. |
| ADR aceptados no reescritos | No verificado | docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md y arc42:795 declaran ediciones históricas; se requiere contrastar cada aceptación/reemplazo antes de cerrar toda la cadena histórica. No hubo modificación de ADR existentes en el intervalo S11 observado. |
| Bitácora IA vigente | No cumple | docs/ia.md:26, commit 28506a8: registro S10/S11 con rechazo explícito de presentar idempotencia como implementada. La lectura no encontró registro específico S12 con usos, aceptación/rechazo y motivo; incumplimiento documental preliminar, subsanable durante la semana. |
| Pipeline, Sonar y Quality Gate públicos | No verificado | [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/39194936605): success Inspección de workflows; no se ejecutó código localmente. [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_InvenTrack). Consulta pública de estado devolvió HTTP 403; Quality Gate no verificado en vivo, aun cuando exista paso configurado. |
| Sin credenciales actuales ni históricas | No verificado | Búsqueda estática de patrones de credenciales y revisión de configuraciones; el barrido histórico por git log -S no terminó dentro de esta pasada. No se afirma ausencia exhaustiva; falta cerrar el historial sin divulgar valores. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**1/9 criterios de la ficha. Nota sugerida: 1.4/5.0**, resultado de `1 + 4 × (1/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo. S12 es PRELIMINAR y puede cambiar hasta su cierre.

## Overall · punta actual

Punta observada: [`28506a8eabcde2234e56698d13ae1d8ae8d0ee24`](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/28506a8eabcde2234e56698d13ae1d8ae8d0ee24), `2026-10-18T22:29:12-05:00`, misma rama principal. Punta y corte coinciden. Hay integración modular en proceso, almacenamiento RAM y lock por SKU con timeout 2 s; no idempotencia de comandos, persistencia SQL ni coordinación entre instancias. ADR-0011 corrige conceptualmente la deduplicación, pero no reemplaza la afirmación errónea de la tabla S11. S12 todavía carece de tabla de garantías y decisión de datos/reversión.

## Fallos probados frente a descritos

tests/inventario/test_degradacion_lock.py:19-37 fuerza contención y espera agotada; tests/inventario/test_concurrencia.py comprueba concurrencia local. CI Run Tests del hash revisado es exitoso. No demuestra recuperación de inventario tras reinicio ni deduplicación: son límites documentados, no pruebas aprobadas.

## Pendientes prioritarios

Todavía faltan la tabla de garantías por operación, una estrategia razonada de caché e invalidación y la decisión de datos con costo de reversión. Los repositorios RAM son el almacenamiento primario y viven dentro de la API. Mantengan explícita la separación entre arquitectura vigente y SQL futuro.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
