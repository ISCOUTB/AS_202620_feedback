# AS_202620_XALD · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_XALD/tree/405a39e0feff40a8414841b6936d5a2dc4488ba4) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado: DEFINITIVA S11.** Revisión académica del contenido completo disponible en la rama principal; no se toma la falta de commits como ausencia de revisión.

- Repositorio público: https://github.com/ISCOUTB/AS_202620_XALD
- Rama: `origin/master`.
- Hash S11: `405a39e0feff40a8414841b6936d5a2dc4488ba4`; fecha del commit: `2026-10-18T22:00:24-05:00`.
- Hash observado S12 / overall: `405a39e0feff40a8414841b6936d5a2dc4488ba4` (misma punta).
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (domingo 18, medianoche Colombia). Se eligió el último commit con fecha anterior al cierre, consultando solo la rama principal, sin etiquetas.
- Observación del avance S12: `2026-10-19T21:35:00Z`; S12 no se cierra ni se sustituye con esta pasada.
- Commits S11 desde `2026-10-12T05:00:00Z`: 35; posteriores al cierre y hasta observación S12: 0.

## Alcance y evidencia

Se leyeron las fichas S11/S12 y el contrato, el árbol completo del hash y los documentos/código pertinentes. Se contrastaron las evidencias aunque no hubiera avance S12. No se ejecutó código, pruebas, instalaciones, despliegues ni scripts del equipo; no se procesaron PDFs. Las referencias `ruta:línea` pertenecen al hash anterior. Las ausencias se decidieron sobre inventario y búsqueda documental/código, no sobre un nombre de archivo supuesto. La matriz transversal no entra en la nota. Las pruebas presentes, resultados declarados y runs públicos se distinguen expresamente.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica | Observaciones y límites |
|---|---|---|---|
| Integración principal identificada en el código | Cumple | `XALDAPP/app/src/main/java/ProcesarNotificacionUseCase.kt:18-35; backend/app/main.py:107-148` | Caso de uso Android coordina categorización, core y cola; endpoint de sincronización existe. Se distingue integración HTTP pendiente de llamadas internas implementadas. |
| Tabla de modos de fallo: no responde, responde tarde y responde dos veces | Cumple | `docs/arc42/11-Risks and Technical Debts.md:22-33` | MF-01 a MF-06 cubren explícitamente los tres modos para backend y Gemini, identificando mock y cliente HTTP pendiente. |
| Mitigación asignada a cada modo de fallo | Cumple | `docs/arc42/11-Risks and Technical Debts.md:28-33` | Cada modo tiene táctica concreta y estado: cola, timeout, reintento, idempotencia o descarte/fallback. |
| Correspondencia entre mitigaciones declaradas e implementadas, o pendiente declarado | Cumple | `docs/arc42/11-Risks and Technical Debts.md:35-59; XALDAPP/syncqueue/src/main/java/ColaSincronizacion.kt:9-23; XALDAPP/aigemini/src/main/java/CategorizadorGemini.kt:9-16` | La tabla distingue implementación/parcial/pendiente y P-01 a P-05 fijan pasos, semana y prueba de cierre. Se aceptan pendientes; no se exige implementar toda resiliencia en S11. |
| Diseño de idempotencia o saga, o argumento de no aplicabilidad | Cumple | `docs/arc42/08-Cross-cutting Concepts.md:55-92; backend/app/main.py:117-138` | Diseño por identificador/fecha, deduplicación y justificación de no saga; declara pérdida del estado en reinicio y límites de reloj. |
| ADR con decisión de extraer o no extraer y sus criterios | Cumple | [docs/adr/0013-extraer-o-no-integracion-gemini.md:16-26,62-79](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/docs/adr/0013-extraer-o-no-integracion-gemini.md#L16-L26) | No extraer con criterios de disponibilidad, latencia, operación, seguridad y disparadores. |
| Alternativa no extraer evaluada explícitamente | Cumple | [docs/adr/0013-extraer-o-no-integracion-gemini.md:28-60](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/docs/adr/0013-extraer-o-no-integracion-gemini.md#L28-L60) | Alternativa no extraer evaluada frente a endpoint intermediario; no es una omisión ni solo falta de tiempo. |
| arc42 sección 11 con los modos de fallo | Cumple | `docs/arc42/11-Risks and Technical Debts.md:22-59` | Catálogo de fallos, correspondencia y plan integrados en sección 11. |
| Filas de aspectos afectadas por la integración al día | Cumple | [docs/aspectos.md:7-11,34-35](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/docs/aspectos.md#L7-L11) | A-01/A-03/A-05 incorporan fallos, ADR y límites reales. Los enlaces apuntan a experimental: se contrastaron las rutas equivalentes del hash de master, sin usar aquella rama para calificar. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia | Observaciones y límites |
|---|---|---|---|
| Repositorio en organización, nombre de convención y público | Cumple | https://github.com/ISCOUTB/AS_202620_XALD | Clon público por protocolo git sin pedir acceso; API de runs respondió HTTP 200. No se consultó API de metadatos. |
| Estructura mínima presente | Cumple | git ls-tree -r 405a39e0feff40a8414841b6936d5a2dc4488ba4; README.md:1; docs/aspectos.md:1; docs/ia.md:1 | Existen docs/arc42/, docs/adr/, docs/c4/, aspectos, IA y README. Presencia no implica que todas las secciones estén completas. |
| Estado calificado identificable | Cumple | refs/remotes/origin/master 405a39e0feff40a8414841b6936d5a2dc4488ba4 2026-10-18T22:00:24-05:00 | Commit anterior al cierre y punta actual coincidentes; cero commits tardíos observados. |
| Nombres de ADR según convención | Cumple | inventario git docs/adr/ en 405a39e0feff40a8414841b6936d5a2dc4488ba4 | Archivos Markdown numerados con cuatro dígitos y nombres kebab-case; .gitkeep no se evalúa como ADR. |
| ADR aceptados no reescritos | No verificado | docs/adr/0013-extraer-o-no-integracion-gemini.md:3; diff 3f23a54 | El cambio examinado perfecciona una propuesta al pasar a Decidido; no prueba reescritura posterior a aceptación. Otros ADR tienen cambios históricos que requieren cotejo completo antes de certificar inmutabilidad. |
| Registro de IA al día para la semana | No cumple | docs/ia.md:37-41; último cambio f3f018a del 2026-10-04 | El registro llega a S9; faltan actualización y criterio de IA de los cambios S11. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | .github/workflows/ci.yml:1-95: CI exitoso del hash, pero no invoca scanner Sonar ni contiene configuración de SonarCloud; falta análisis y Quality Gate público. | No se completa la triple evidencia requerida: configuración, run de scanner exitoso y análisis/Quality Gate público correspondiente. No se confunde CI general con gate. |
| Sin credenciales en repositorio ni historial | No verificado | git grep -nIE sobre 405a39e0feff40a8414841b6936d5a2dc4488ba4; inventario .env; revisión histórica parcial | Barrido de patrones en la punta sin secreto real confirmado; coincidencias de código, pruebas o documentación no se publican como credenciales. El barrido histórico no pudo completarse por demoras/aborto de conexión al recuperar blobs antiguos; faltaría cerrar la revisión del historial, no solo comprobar la punta. |
| Contribución de todos los integrantes | No verificado | git shortlog -sne 405a39e0feff40a8414841b6936d5a2dc4488ba4; EQUIPOS.md | Se examinó distribución de identidades del historial. No se atribuyen cuentas a personas por parecido ni se equipara número de correos con integrantes. Falta correspondencia consolidada/verificada para certificar aportes de todos; se omiten nombres, correos e identificadores personales. |

## Recuento y nota sugerida

**9/9 Cumple. Nota sugerida: 5.0/5.0**, calculada como `1 + 4 × (9/9)`, redondeada a un decimal. **Propuesta al docente; la nota final la fija el profesor en Moodle.** Esta revisión S11 es definitiva respecto del cierre indicado.

## overall · proyecto en la punta actual

S11 está documentada con honestidad sobre lo que falta. El backend aplica LWW y deduplicación de identificador/fecha en memoria; no conserva payload completo ni estado tras reinicio (backend/app/main.py:58-60,117-138). Android usa listas en memoria, no tiene cliente HTTP ni retirada confirmada de cola; Gemini es un mock. Estos límites ya se admiten con plan, por lo que no reducen una fila que admite pendientes. El enunciado de efecto exactamente una vez debe acotarse al proceso vivo; el mismo identificador/fecha no compara contenido.

No hay cambios posteriores al cierre en la rama principal observada. La revisión S12 aplica sus criterios al estado completo actual; no modifica la nota de S11 ni recalifica entregas anteriores.

## Fallos probados, documentados y límites de CI

backend/tests/test_lww.py:48-97,112-132 contiene pruebas de versiones y reenvío duplicado. El bucle de 30 operaciones de :81-87 es secuencial, no una carga concurrente demostrada. CI del hash revisado terminó success: https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/39192603030; .github/workflows/ci.yml:29-37,55-57 configura pruebas Android/backend. MF-01, MF-02 y Gemini siguen sin pruebas de integración ejecutadas, según la propia tabla. No se ejecutó código aquí.

## Pendientes prioritarios

- Para el proyecto final, incorporar pruebas de no respuesta, respuesta tardía y duplicación sobre la integración real, y conservar evidencia ejecutada citable. S11 acepta planes pendientes bien declarados; no obliga a extraer servicios ni a implementar mensajería.
