# AS_202620_mapsutb · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_mapsutb/tree/4b8fa088faec96772e76c8c4f2782919ec87a9b9) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR S12; no es cierre ni nota final**.

- Rama: `origin/master`; commit evaluado: [`4b8fa088faec96772e76c8c4f2782919ec87a9b9`](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/4b8fa088faec96772e76c8c4f2782919ec87a9b9), fecha `2026-10-16T12:38:48-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 9 commits durante S11; 0 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Tabla operación → garantía con operaciones reales | No cumple | [docs/arc42/08_concepts.adoc:76-105](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/arc42/08_concepts.adoc#L76-L105). Tabla módulo→dato→dueño no es operación→garantía de consistencia; falta declarar consultas de zonas/grafo y evento analítico. |
| Dos operaciones verificadas contra implementación | No cumple | [lib/routing/mapa_repository.dart:14-29](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/lib/routing/mapa_repository.dart#L14-L29). Lectura del grafo cacheada en instancia; no hay dos garantías declaradas S12 para contrastar. La segunda operación (zonas) también requiere especificación. |
| Caché: qué, dónde y cuánto | Cumple | [docs/adr/0015-cache-del-sitio-revalidar.md:26-35](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/adr/0015-cache-del-sitio-revalidar.md#L26-L35). Caché HTTP de HTML/JS/JSON se revalida cada carga; health no-store y recursos versionados mantienen política. Falta ampliar la explicación a caché RAM del grafo. |
| Invalidación tras escritura | Cumple | [docs/adr/0015-cache-del-sitio-revalidar.md:28-35](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/adr/0015-cache-del-sitio-revalidar.md#L28-L35). Tras despliegue/escritura de activos se revalida por ETag en siguiente carga; firebase.json:8-16 implementa no-cache/no-store. Límite de pestaña abierta y copias anteriores:59-63. |
| Garantías de eventos, si existen | Cumple | [lib/adapters/analytics_adapter.dart:62-112](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/lib/adapters/analytics_adapter.dart#L62-L112). Evento analítico de mejor esfuerzo, una llamada sin reenvío y pérdida aceptada; ADR-0016:110-125 lo declara como máximo una vez. |
| ADR de la decisión de datos más costosa de revertir | No cumple | [docs/adr/0015-cache-del-sitio-revalidar.md:37-63](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/adr/0015-cache-del-sitio-revalidar.md#L37-L63). ADR de caché existente no identifica decisión de datos más costosa de revertir; no basta tener un ADR sobre datos. |
| Razón y costo de reversión | No cumple | [docs/adr/0016-no-extraer-modulos-por-ahora.md:89-101](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/adr/0016-no-extraer-modulos-por-ahora.md#L89-L101). Discute externalizar datos del campus, pero no selecciona ni compara costo de reversión de la decisión de datos más costosa. |
| Almacenes/brokers propios y tecnología en C4 L2 | Cumple | [docs/c4/C2.md:11-32](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/c4/C2.md#L11-L32). Almacenes JSON/grafo como cajas propias y tecnología; distingue panorámicas diferidas. Sin broker implementado; analítica es sistema externo. |
| arc42 §8: consistencia y caché | No cumple | [docs/arc42/08_concepts.adoc:1-122](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/arc42/08_concepts.adoc#L1-L122). La sección 8 describe contextos, propietarios y observabilidad; no integra garantías de consistencia ni política de caché del ADR-0015. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_mapsutb](https://github.com/ISCOUTB/AS_202620_mapsutb); no se usó API de repositorios. |
| Estructura mínima | Cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. Esto no acredita completitud de sus secciones. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Observación preliminar, no estado futuro de cierre. |
| Nombres de ADR | Cumple | Inventario completo docs/adr/ del hash citado: nombres NNNN-titulo-en-kebab-case.md. |
| ADR aceptados no reescritos | No verificado | No se modifican ADR existentes en el intervalo S11 según git log --diff-filter=M; falta comprobar el historial completo de aceptación de cada ADR para afirmar inmutabilidad histórica. |
| Bitácora IA vigente | No cumple | docs/ia.md:26-27, commit e8f2995: S11 con rechazo de reintentos automáticos y Cloud Functions por costo/tarjeta, y GPS real. La lectura no encontró registro específico S12 con usos, aceptación/rechazo y motivo; incumplimiento documental preliminar, subsanable durante la semana. |
| Pipeline, Sonar y Quality Gate públicos | No verificado | [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/39327726983): success; [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/39320013447): success; [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/39310919986): success; [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/39304022694): success Las sondas programadas y sincronización Sonar no equivalen a ejecución de pruebas; docs/evidencia-s11.md:70-73 cita un run anterior, sin consulta independiente adicional. Inspección de workflows; no se ejecutó código localmente. [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_mapsutb). Consulta pública de estado devolvió HTTP 403; Quality Gate no verificado en vivo, aun cuando exista paso configurado. |
| Sin credenciales actuales ni históricas | No verificado | Búsqueda estática de patrones de credenciales y revisión de configuraciones; el barrido histórico por git log -S no terminó dentro de esta pasada. No se afirma ausencia exhaustiva; falta cerrar el historial sin divulgar valores. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**4/9 criterios de la ficha. Nota sugerida: 2.8/5.0**, resultado de `1 + 4 × (4/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo. S12 es PRELIMINAR y puede cambiar hasta su cierre.

## Overall · punta actual

Punta observada: [`4b8fa088faec96772e76c8c4f2782919ec87a9b9`](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/4b8fa088faec96772e76c8c4f2782919ec87a9b9), `2026-10-16T12:38:48-05:00`, misma rama principal. Punta y corte coinciden. La ruta se calcula localmente; teselas OSM, GPS y adaptadores HTTP tienen tratamientos diferenciados. Google Geocoding/Static Maps no deben confundirse con integración activa sin credenciales. S12 tiene base aprovechable en caché HTTP y entrega analítica, pero faltan garantías por operación, ADR de datos/costo de reversión y actualización de arc42 §8.

## Fallos probados frente a descritos

test/modos_de_fallo_test.dart:64-185 contiene errores, timeout, doble toque y no reenvío; test/mapa_test.dart cubre callback MF-01 sin petición real OSM. arc42:214-216 distingue MF-02/03/12 solo descritos. La consulta limitada de Actions devuelve sondas/sincronización, no el run CI del hash; docs/evidencia-s11.md:70-73 enlaza run 38439161941 del commit anterior e8f2995. No convertir una sonda verde en suite verificada para esta punta.

## Pendientes prioritarios

Ya hay una política HTTP de revalidación y una garantía limitada para analítica. Falta integrar la caché interna del grafo, declarar garantías por operación y justificar la decisión de datos más costosa de revertir. Reúnan consistencia y caché en arc42, manteniendo separado lo vigente de los recorridos panorámicos diferidos.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
