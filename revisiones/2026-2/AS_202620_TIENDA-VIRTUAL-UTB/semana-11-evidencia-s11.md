# AS_202620_TIENDA-VIRTUAL-UTB · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/tree/c58fddfe790932538b37f62017d307ef56bf90d5) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado: DEFINITIVA S11.** Revisión académica del contenido completo disponible en la rama principal; no se toma la falta de commits como ausencia de revisión.

- Repositorio público: https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB
- Rama: `origin/main`.
- Hash S11: `c58fddfe790932538b37f62017d307ef56bf90d5`; fecha del commit: `2026-10-18T21:06:47-05:00`.
- Hash observado S12 / overall: `c58fddfe790932538b37f62017d307ef56bf90d5` (misma punta).
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (domingo 18, medianoche Colombia). Se eligió el último commit con fecha anterior al cierre, consultando solo la rama principal, sin etiquetas.
- Observación del avance S12: `2026-10-19T21:35:00Z`; S12 no se cierra ni se sustituye con esta pasada.
- Commits S11 desde `2026-10-12T05:00:00Z`: 1; posteriores al cierre y hasta observación S12: 0.

## Alcance y evidencia

Se leyeron las fichas S11/S12 y el contrato, el árbol completo del hash y los documentos/código pertinentes. Se contrastaron las evidencias aunque no hubiera avance S12. No se ejecutó código, pruebas, instalaciones, despliegues ni scripts del equipo; no se procesaron PDFs. Las referencias `ruta:línea` pertenecen al hash anterior. Las ausencias se decidieron sobre inventario y búsqueda documental/código, no sobre un nombre de archivo supuesto. La matriz transversal no entra en la nota. Las pruebas presentes, resultados declarados y runs públicos se distinguen expresamente.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica | Observaciones y límites |
|---|---|---|---|
| Integración principal identificada en el código | Cumple | [frontend/app/page.tsx:25-55](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/frontend/app/page.tsx#L25-L55) | Next.js consulta catálogo e inventario por HTTP y compone ambas respuestas; esta es la integración que existe. |
| Tabla de modos de fallo: no responde, responde tarde y responde dos veces | No cumple | `docs/modos-fallo-s11.md:16-34; frontend/app/page.tsx:25-38` | F-02 cubre caída/latencia de BD, pero el duplicado F-04 pertenece a pedidos aún inexistentes. Falta completar los tres casos sobre la integración real de consulta; no se exige implementar pedidos. |
| Mitigación asignada a cada modo de fallo | Cumple | [docs/modos-fallo-s11.md:26-34](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/modos-fallo-s11.md#L26-L34) | Cada modo enumerado tiene una mitigación concreta: caché/retry, idempotencia, TTL, bloqueo, DLQ y límites. Es diseño, con el límite de alcance señalado en la fila anterior. |
| Correspondencia entre mitigaciones declaradas e implementadas, o pendiente declarado | Cumple | `docs/modos-fallo-s11.md:3-5,16-24; docs/idempotencia-saga-s11.md:21-32,74-90` | Se declara que las tácticas son pendientes y se describe cómo aplicarlas. Se acepta el plan de diseño; no se exige implementar todo en S11. Corregir la frase que llama reservado a inventory, que ya tiene repositorio real. |
| Diseño de idempotencia o saga, o argumento de no aplicabilidad | Cumple | [docs/idempotencia-saga-s11.md:14-66,68-127](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/idempotencia-saga-s11.md#L14-L66) | Clave por usuario, respuesta guardada, vigencia de 24 h y compensación de inventario. Diseño explícito para la escritura futura, no garantía ya implementada. |
| ADR con decisión de extraer o no extraer y sus criterios | Cumple | [docs/adr/0010-no-extraer-modulos.md:30-86](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/adr/0010-no-extraer-modulos.md#L30-L86) | Decisión razonada de conservar el monolito, con criterios y disparadores; estado propuesto declarado. |
| Alternativa no extraer evaluada explícitamente | Cumple | [docs/adr/0010-no-extraer-modulos.md:54-62](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/adr/0010-no-extraer-modulos.md#L54-L62) | No extraer se compara con extraer Inventario y Pedidos, con ventajas y límites. |
| arc42 sección 11 con los modos de fallo | Cumple | [docs/arc42/arc42-template-EN.md:577-588](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/arc42/arc42-template-EN.md#L577-L588) | Riesgo de mitigaciones F-01 a F-07 pendientes y enlaces al diseño incorporados en sección 11. |
| Filas de aspectos afectadas por la integración al día | No cumple | [docs/aspectos.md:32-37](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/aspectos.md#L32-L37) | Las filas siguen remitiendo a ADR 0001/0008; no incorporan ADR 0010, catálogo de fallos ni plan de resiliencia S11. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia | Observaciones y límites |
|---|---|---|---|
| Repositorio en organización, nombre de convención y público | Cumple | https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB | Clon público por protocolo git sin pedir acceso; API de runs respondió HTTP 200. No se consultó API de metadatos. |
| Estructura mínima presente | Cumple | git ls-tree -r c58fddfe790932538b37f62017d307ef56bf90d5; README.md:1; docs/aspectos.md:1; docs/ia.md:1 | Existen docs/arc42/, docs/adr/, docs/c4/, aspectos, IA y README. Presencia no implica que todas las secciones estén completas. |
| Estado calificado identificable | Cumple | refs/remotes/origin/main c58fddfe790932538b37f62017d307ef56bf90d5 2026-10-18T21:06:47-05:00 | Commit anterior al cierre y punta actual coincidentes; cero commits tardíos observados. |
| Nombres de ADR según convención | Cumple | inventario git docs/adr/ en c58fddfe790932538b37f62017d307ef56bf90d5 | Archivos Markdown numerados con cuatro dígitos y nombres kebab-case; .gitkeep no se evalúa como ADR. |
| ADR aceptados no reescritos | No cumple | docs/adr/0001-monolito-modular.md:18-34; diff e8ae57d | Se añadieron criterios al cuerpo del ADR ya aceptado; registrar ampliaciones/cambios mediante nueva decisión o adenda identificada, preservando la decisión original. |
| Registro de IA al día para la semana | Cumple | docs/ia.md:27; commit c58fddf del 2026-10-18 | Entrada S11 con herramienta, uso, descartes y validación; S12 conserva esta línea base, sin nueva actividad. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | .github/workflows/tests.yml:64-80 y sonar-project.properties:1-6: scanner condicional; falta análisis público y Quality Gate verificables del hash. Run de pruebas exitoso citado en overall. | No se completa la triple evidencia requerida: configuración, run de scanner exitoso y análisis/Quality Gate público correspondiente. No se confunde CI general con gate. |
| Sin credenciales en repositorio ni historial | No verificado | git grep -nIE sobre c58fddfe790932538b37f62017d307ef56bf90d5; inventario .env; revisión histórica parcial | Barrido de patrones en la punta sin secreto real confirmado; coincidencias de código, pruebas o documentación no se publican como credenciales. El barrido histórico no pudo completarse por demoras/aborto de conexión al recuperar blobs antiguos; faltaría cerrar la revisión del historial, no solo comprobar la punta. |
| Contribución de todos los integrantes | No verificado | git shortlog -sne c58fddfe790932538b37f62017d307ef56bf90d5; EQUIPOS.md | Se examinó distribución de identidades del historial. No se atribuyen cuentas a personas por parecido ni se equipara número de correos con integrantes. Falta correspondencia consolidada/verificada para certificar aportes de todos; se omiten nombres, correos e identificadores personales. |

## Recuento y nota sugerida

**7/9 Cumple. Nota sugerida: 4.1/5.0**, calculada como `1 + 4 × (7/9)`, redondeada a un decimal. **Propuesta al docente; la nota final la fija el profesor en Moodle.** Esta revisión S11 es definitiva respecto del cierre indicado.

## overall · proyecto en la punta actual

El corte vigente es un sistema de lectura de catálogo e inventario con frontend Next.js, API FastAPI y PostgreSQL. La entrega S11 agrega análisis y decisión de no extraer; no convierte pedidos, saga, Redis o reintentos en funcionalidades ejecutadas. La documentación todavía llama vacío al inventario ya implementado (docs/modos-fallo-s11.md:18; backend/app/modules/inventory/repository.py:11-13). Para S12, conservar la decisión sin caché si sigue justificada y especificar las garantías de las dos lecturas independientes.

No hay cambios posteriores al cierre en la rama principal observada. La revisión S12 aplica sus criterios al estado completo actual; no modifica la nota de S11 ni recalifica entregas anteriores.

## Fallos probados, documentados y límites de CI

El run de Pruebas del hash revisado es exitoso: https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/39188436440. La suite funcional/contrato está configurada en .github/workflows/tests.yml:29-43; eso no prueba caídas, respuestas tardías ni duplicación de pedidos que todavía no existen. Las mitigaciones S11 son diseño declarado. Sonar se omite si no hay token (.github/workflows/tests.yml:64-80), por lo que un run global exitoso no acredita scanner ni Quality Gate.

## Pendientes prioritarios

- Tabla de modos de fallo: no responde, responde tarde y responde dos veces: F-02 cubre caída/latencia de BD, pero el duplicado F-04 pertenece a pedidos aún inexistentes. Falta completar los tres casos sobre la integración real de consulta; no se exige implementar pedidos.
- Filas de aspectos afectadas por la integración al día: Las filas siguen remitiendo a ADR 0001/0008; no incorporan ADR 0010, catálogo de fallos ni plan de resiliencia S11.
- Para el proyecto final, incorporar pruebas de no respuesta, respuesta tardía y duplicación sobre la integración real, y conservar evidencia ejecutada citable. S11 acepta planes pendientes bien declarados; no obliga a extraer servicios ni a implementar mensajería.
