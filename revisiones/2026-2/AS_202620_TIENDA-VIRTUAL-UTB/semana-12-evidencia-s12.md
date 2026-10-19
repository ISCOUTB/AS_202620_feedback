# AS_202620_TIENDA-VIRTUAL-UTB · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/tree/c58fddfe790932538b37f62017d307ef56bf90d5) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR S12 — aún abierta.** Revisión académica del contenido completo disponible en la rama principal; no se toma la falta de commits como ausencia de revisión.

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
| Tabla operación a garantía de consistencia con operaciones reales | No cumple | `docs/aspectos.md:32-37; docs/idempotencia-saga-s11.md:131-136` | Hay escenarios y una comparación de patrones, no una tabla de operaciones reales con su garantía. |
| Dos operaciones verificadas contra la implementación | No cumple | `backend/app/modules/catalog/repository.py:11-13; backend/app/modules/inventory/repository.py:11-13` | Se contrastaron ambas consultas SQL: son lecturas separadas y no un snapshot conjunto. Falta especificar y verificar las dos garantías; no se infiere consistencia fuerte de compartir PostgreSQL. |
| Diseño de caché: qué, dónde y cuánto | Cumple | `docs/aspectos.md:22-23,36; docs/arc42/arc42-template-EN.md:408-411; frontend/app/page.tsx:25-38` | La estrategia vigente evita caché para consultar datos actuales en cada carga. Se admite la decisión argumentada de no cachear. Redis en F-02 es propuesta futura. |
| Política de invalidación tras escritura | Cumple | `frontend/app/page.tsx:25-38; docs/arc42/arc42-template-EN.md:408-411` | Con no-store se vuelve a consultar al recargar; no hay copia cacheada que invalidar en el camino vigente. Cuando existan escrituras/caché Redis deberá definirse invalidación, no basta el TTL de la saga. |
| Garantías del flujo por eventos, si existe | Cumple | `docs/adr/0002-contrato-integracion-http.md:9-12,27-37; docs/idempotencia-saga-s11.md:3-5` | No aplica al runtime actual: integración HTTP síncrona sin mensajería. La saga es futura y no se presenta como entrega garantizada. |
| ADR de la decisión de datos más costosa de revertir | No cumple | `docs/adr/0010-no-extraer-modulos.md:64-109; inventario git docs/adr/` | La decisión de extracción no identifica la decisión de datos más costosa de revertir. |
| Argumento y costo de reversión de esa decisión | No cumple | [docs/adr/0010-no-extraer-modulos.md:88-109](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/adr/0010-no-extraer-modulos.md#L88-L109) | Se describen costos operativos, pero no comparación ni costo de reversión de la decisión de datos seleccionada. |
| Almacenes y brokers como contenedores propios en C4 nivel 2 | Cumple | [docs/c4/container.md:22-32](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/c4/container.md#L22-L32) | PostgreSQL 17 aparece como ContainerDb propio; no hay broker vigente que falte representar. |
| arc42 sección 8 con consistencia y caché | No cumple | [docs/arc42/arc42-template-EN.md:492-533](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/c58fddfe790932538b37f62017d307ef56bf90d5/docs/arc42/arc42-template-EN.md#L492-L533) | Hay propiedad de datos y diseño de saga; faltan garantías por operación y estrategia de caché/invalidation integradas en sección 8. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia | Observaciones y límites |
|---|---|---|---|
| Repositorio en organización, nombre de convención y público | Cumple | https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB | Clon público por protocolo git sin pedir acceso; API de runs respondió HTTP 200. No se consultó API de metadatos. |
| Estructura mínima presente | Cumple | git ls-tree -r c58fddfe790932538b37f62017d307ef56bf90d5; README.md:1; docs/aspectos.md:1; docs/ia.md:1 | Existen docs/arc42/, docs/adr/, docs/c4/, aspectos, IA y README. Presencia no implica que todas las secciones estén completas. |
| Estado calificado identificable | Cumple | refs/remotes/origin/main c58fddfe790932538b37f62017d307ef56bf90d5 2026-10-18T21:06:47-05:00 | Commit anterior al cierre y punta actual coincidentes; cero commits tardíos observados. |
| Nombres de ADR según convención | Cumple | inventario git docs/adr/ en c58fddfe790932538b37f62017d307ef56bf90d5 | Archivos Markdown numerados con cuatro dígitos y nombres kebab-case; .gitkeep no se evalúa como ADR. |
| ADR aceptados no reescritos | No cumple | docs/adr/0001-monolito-modular.md:18-34; diff e8ae57d | Se añadieron criterios al cuerpo del ADR ya aceptado; registrar ampliaciones/cambios mediante nueva decisión o adenda identificada, preservando la decisión original. |
| Registro de IA al día para la semana | No verificado | docs/ia.md:27; commit c58fddf del 2026-10-18 | Entrada S11 con herramienta, uso, descartes y validación. El estado observado no tiene commits posteriores al cierre; no acredita una entrada de S12 ni permite concluir que hubo uso nuevo de IA sin registrar. Actualización S12 pendiente de verificar. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | .github/workflows/tests.yml:64-80 y sonar-project.properties:1-6: scanner condicional; falta análisis público y Quality Gate verificables del hash. Run de pruebas exitoso citado en overall. | No se completa la triple evidencia requerida: configuración, run de scanner exitoso y análisis/Quality Gate público correspondiente. No se confunde CI general con gate. |
| Sin credenciales en repositorio ni historial | No verificado | git grep -nIE sobre c58fddfe790932538b37f62017d307ef56bf90d5; inventario .env; revisión histórica parcial | Barrido de patrones en la punta sin secreto real confirmado; coincidencias de código, pruebas o documentación no se publican como credenciales. El barrido histórico no pudo completarse por demoras/aborto de conexión al recuperar blobs antiguos; faltaría cerrar la revisión del historial, no solo comprobar la punta. |
| Contribución de todos los integrantes | No verificado | git shortlog -sne c58fddfe790932538b37f62017d307ef56bf90d5; EQUIPOS.md | Se examinó distribución de identidades del historial. No se atribuyen cuentas a personas por parecido ni se equipara número de correos con integrantes. Falta correspondencia consolidada/verificada para certificar aportes de todos; se omiten nombres, correos e identificadores personales. |

## Recuento y nota sugerida

**4/9 Cumple. Nota sugerida: 2.8/5.0**, calculada como `1 + 4 × (4/9)`, redondeada a un decimal. **Propuesta al docente; la nota final la fija el profesor en Moodle.** La nota S12 es PRELIMINAR y puede cambiar hasta el cierre; no constituye entrega vencida.

## overall · proyecto en la punta actual

El corte vigente es un sistema de lectura de catálogo e inventario con frontend Next.js, API FastAPI y PostgreSQL. La entrega S11 agrega análisis y decisión de no extraer; no convierte pedidos, saga, Redis o reintentos en funcionalidades ejecutadas. La documentación todavía llama vacío al inventario ya implementado (docs/modos-fallo-s11.md:18; backend/app/modules/inventory/repository.py:11-13). Para S12, conservar la decisión sin caché si sigue justificada y especificar las garantías de las dos lecturas independientes.

No hay cambios posteriores al cierre en la rama principal observada. La revisión S12 aplica sus criterios al estado completo actual; no modifica la nota de S11 ni recalifica entregas anteriores.

## Fallos probados, documentados y límites de CI

El run de Pruebas del hash revisado es exitoso: https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/39188436440. La suite funcional/contrato está configurada en .github/workflows/tests.yml:29-43; eso no prueba caídas, respuestas tardías ni duplicación de pedidos que todavía no existen. Las mitigaciones S11 son diseño declarado. Sonar se omite si no hay token (.github/workflows/tests.yml:64-80), por lo que un run global exitoso no acredita scanner ni Quality Gate.

## Pendientes prioritarios

- Tabla operación a garantía de consistencia con operaciones reales: Hay escenarios y una comparación de patrones, no una tabla de operaciones reales con su garantía.
- Dos operaciones verificadas contra la implementación: Se contrastaron ambas consultas SQL: son lecturas separadas y no un snapshot conjunto. Falta especificar y verificar las dos garantías; no se infiere consistencia fuerte de compartir PostgreSQL.
- ADR de la decisión de datos más costosa de revertir: La decisión de extracción no identifica la decisión de datos más costosa de revertir.
- Argumento y costo de reversión de esa decisión: Se describen costos operativos, pero no comparación ni costo de reversión de la decisión de datos seleccionada.
- arc42 sección 8 con consistencia y caché: Hay propiedad de datos y diseño de saga; faltan garantías por operación y estrategia de caché/invalidation integradas en sección 8.
- El taller de mensajes se evalúa aparte. No se exige introducir caché o broker si su ausencia está razonada; sí precisar las garantías, los límites y las decisiones de datos.
