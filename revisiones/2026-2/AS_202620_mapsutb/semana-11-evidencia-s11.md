# AS_202620_mapsutb · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_mapsutb/tree/4b8fa088faec96772e76c8c4f2782919ec87a9b9) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado: DEFINITIVA S11**.

- Rama: `origin/master`; commit evaluado: [`4b8fa088faec96772e76c8c4f2782919ec87a9b9`](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/4b8fa088faec96772e76c8c4f2782919ec87a9b9), fecha `2026-10-16T12:38:48-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 9 commits durante S11; 0 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Integración principal identificada en el código | Cumple | [lib/adapters/mapa_widget.dart:120-128](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/lib/adapters/mapa_widget.dart#L120-L128). TileLayer llama a OSM; grafo local mantiene ruta independiente de teselas. |
| Tabla de fallos: no responde, tarde y dos veces | Cumple | [docs/arc42/11_technical_risks.adoc:70-109](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/arc42/11_technical_risks.adoc#L70-L109). MF-01/02/03 cubren los tres casos de la integración principal; hasta MF-15 amplía otras fronteras. |
| Mitigación asignada a cada fallo | Cumple | [docs/arc42/11_technical_risks.adoc:81-206](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/arc42/11_technical_risks.adoc#L81-L206). Cada fila asigna táctica y señala si está probada o solo descrita. |
| Correspondencia o pendiente explícito con plan | Cumple | [docs/evidencia-s11.md:26-43](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/evidencia-s11.md#L26-L43). Timeout y errores propios en adaptadores; callback de teselas y filtrado GPS en código. Reintentos/abortos propios de flutter_map no se presentan como prueba propia. |
| Diseño de idempotencia/saga o justificación | Cumple | [docs/adr/0016-no-extraer-modulos-por-ahora.md:117-128](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/adr/0016-no-extraer-modulos-por-ahora.md#L117-L128). Lecturas GET idempotentes, analítica sin reintento (como máximo una vez) y no saga por no escribir en varios sistemas. |
| ADR de extracción con criterios | Cumple | [docs/adr/0016-no-extraer-modulos-por-ahora.md:34-145](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/adr/0016-no-extraer-modulos-por-ahora.md#L34-L145). Cuatro alternativas y criterios de costo, latencia, seguridad y operación; disparadores explícitos. |
| Alternativa no extraer evaluada | Cumple | [docs/adr/0016-no-extraer-modulos-por-ahora.md:47-59](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/adr/0016-no-extraer-modulos-por-ahora.md#L47-L59). No extraer con tabla propia, incluida debilidad de credencial de analítica en binario. |
| arc42 §11 con modos de fallo | Cumple | [docs/arc42/11_technical_risks.adoc:70-216](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/arc42/11_technical_risks.adoc#L70-L216). Modos, estados, pruebas y deuda de medición GPS en campus incorporados. |
| Aspectos afectados al día | Cumple | [docs/aspectos.md:1-28](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/docs/aspectos.md#L1-L28). A-01/A-02 incorporan ADR-0016, pruebas de fallos y enlaces a arc42; no se exige crear infraestructura distribuida. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_mapsutb](https://github.com/ISCOUTB/AS_202620_mapsutb); no se usó API de repositorios. |
| Estructura mínima | Cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. Esto no acredita completitud de sus secciones. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Corte exclusivo verificado. |
| Nombres de ADR | Cumple | Inventario completo docs/adr/ del hash citado: nombres NNNN-titulo-en-kebab-case.md. |
| ADR aceptados no reescritos | No verificado | No se modifican ADR existentes en el intervalo S11 según git log --diff-filter=M; falta comprobar el historial completo de aceptación de cada ADR para afirmar inmutabilidad histórica. |
| Bitácora IA vigente | Cumple | docs/ia.md:26-27, commit e8f2995: S11 con rechazo de reintentos automáticos y Cloud Functions por costo/tarjeta, y GPS real. |
| Pipeline, Sonar y Quality Gate públicos | No verificado | [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/39327726983): success; [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/39320013447): success; [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/39310919986): success; [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/39304022694): success Las sondas programadas y sincronización Sonar no equivalen a ejecución de pruebas; docs/evidencia-s11.md:70-73 cita un run anterior, sin consulta independiente adicional. Inspección de workflows; no se ejecutó código localmente. [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_mapsutb). Consulta pública de estado devolvió HTTP 403; Quality Gate no verificado en vivo, aun cuando exista paso configurado. |
| Sin credenciales actuales ni históricas | No verificado | Búsqueda estática de patrones de credenciales y revisión de configuraciones; el barrido histórico por git log -S no terminó dentro de esta pasada. No se afirma ausencia exhaustiva; falta cerrar el historial sin divulgar valores. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**9/9 criterios de la ficha. Nota sugerida: 5.0/5.0**, resultado de `1 + 4 × (9/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo.

## Overall · punta actual

Punta observada: [`4b8fa088faec96772e76c8c4f2782919ec87a9b9`](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/4b8fa088faec96772e76c8c4f2782919ec87a9b9), `2026-10-16T12:38:48-05:00`, misma rama principal. Punta y corte coinciden. La ruta se calcula localmente; teselas OSM, GPS y adaptadores HTTP tienen tratamientos diferenciados. Google Geocoding/Static Maps no deben confundirse con integración activa sin credenciales. S12 tiene base aprovechable en caché HTTP y entrega analítica, pero faltan garantías por operación, ADR de datos/costo de reversión y actualización de arc42 §8.

## Fallos probados frente a descritos

test/modos_de_fallo_test.dart:64-185 contiene errores, timeout, doble toque y no reenvío; test/mapa_test.dart cubre callback MF-01 sin petición real OSM. arc42:214-216 distingue MF-02/03/12 solo descritos. La consulta limitada de Actions devuelve sondas/sincronización, no el run CI del hash; docs/evidencia-s11.md:70-73 enlaza run 38439161941 del commit anterior e8f2995. No convertir una sonda verde en suite verificada para esta punta.

## Pendientes prioritarios

La decisión de no extraer, las mitigaciones y la trazabilidad están justificadas sobre las integraciones reales. Distingan las pruebas con dobles de las mediciones sobre GPS y proveedores reales. El flujo completo en campus sigue sin la medición que permitiría cerrar ese límite.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
