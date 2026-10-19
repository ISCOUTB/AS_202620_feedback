# AS_202620_UTB_TRACKER · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/tree/277098684766fdf35f12b9d6713ee78c423a08b4) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR S12 — aún abierta.** Revisión académica del contenido completo disponible en la rama principal; no se toma la falta de commits como ausencia de revisión.

- Repositorio público: https://github.com/ISCOUTB/AS_202620_UTB_TRACKER
- Rama: `origin/main`.
- Hash S11: `277098684766fdf35f12b9d6713ee78c423a08b4`; fecha del commit: `2026-10-18T23:20:54-05:00`.
- Hash observado S12 / overall: `277098684766fdf35f12b9d6713ee78c423a08b4` (misma punta).
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (domingo 18, medianoche Colombia). Se eligió el último commit con fecha anterior al cierre, consultando solo la rama principal, sin etiquetas.
- Observación del avance S12: `2026-10-19T21:35:00Z`; S12 no se cierra ni se sustituye con esta pasada.
- Commits S11 desde `2026-10-12T05:00:00Z`: 2; posteriores al cierre y hasta observación S12: 0.

## Alcance y evidencia

Se leyeron las fichas S11/S12 y el contrato, el árbol completo del hash y los documentos/código pertinentes. Se contrastaron las evidencias aunque no hubiera avance S12. No se ejecutó código, pruebas, instalaciones, despliegues ni scripts del equipo; no se procesaron PDFs. Las referencias `ruta:línea` pertenecen al hash anterior. Las ausencias se decidieron sobre inventario y búsqueda documental/código, no sobre un nombre de archivo supuesto. La matriz transversal no entra en la nota. Las pruebas presentes, resultados declarados y runs públicos se distinguen expresamente.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica | Observaciones y límites |
|---|---|---|---|
| Tabla operación a garantía de consistencia con operaciones reales | No cumple | [docs/arc42/arc42.md:327-360](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/277098684766fdf35f12b9d6713ee78c423a08b4/docs/arc42/arc42.md#L327-L360) | ACID se describe globalmente; falta tabla operación→garantía. |
| Dos operaciones verificadas contra la implementación | No cumple | `app/services/loans.py:29-74; app/services/resources.py:16-28` | Se contrastaron crear préstamo y crear recurso: ambas hacen commit local; préstamos añade bloqueo condicional PostgreSQL. Sin garantías por operación ni prueba concurrente no se acreditan dos verificaciones completas. |
| Diseño de caché: qué, dónde y cuánto | No cumple | [docs/arc42/arc42.md:327-360](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/277098684766fdf35f12b9d6713ee78c423a08b4/docs/arc42/arc42.md#L327-L360) | No hay diseño de caché ni justificación explícita para prescindir de ella. |
| Política de invalidación tras escritura | No cumple | `app/services/resources.py:24-28; docs/arc42/arc42.md:327-360` | Falta declarar qué hacer al crear un recurso o prestar uno si se cachea el catálogo; hoy no se demuestra un defecto por caché inexistente. |
| Garantías del flujo por eventos, si existe | Cumple | `docs/arc42/arc42.md:357-359; docs/c4/C2.md:15-16` | No aplica a runtime: transacción local e integración síncrona; las integraciones externas son futuras. |
| ADR de la decisión de datos más costosa de revertir | No cumple | [docs/adr/0005-monolito-vs-microservicios.md:20-62](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/277098684766fdf35f12b9d6713ee78c423a08b4/docs/adr/0005-monolito-vs-microservicios.md#L20-L62) | ADR de no extracción, no selección comparada de la decisión de datos más costosa. |
| Argumento y costo de reversión de esa decisión | No cumple | [docs/adr/0005-monolito-vs-microservicios.md:46-62](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/277098684766fdf35f12b9d6713ee78c423a08b4/docs/adr/0005-monolito-vs-microservicios.md#L46-L62) | No se estima costo de migrar/revertir la decisión de datos ni se explica por qué sería el mayor. |
| Almacenes y brokers como contenedores propios en C4 nivel 2 | Cumple | [docs/c4/C2.md:30-43](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/277098684766fdf35f12b9d6713ee78c423a08b4/docs/c4/C2.md#L30-L43) | PostgreSQL es contenedor propio con tecnología y conexión SQL; no existe broker actual. |
| arc42 sección 8 con consistencia y caché | No cumple | [docs/arc42/arc42.md:327-360](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/277098684766fdf35f12b9d6713ee78c423a08b4/docs/arc42/arc42.md#L327-L360) | Sección 8 describe ACID/idempotencia pero omite estrategia de caché y garantías completas por operación. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia | Observaciones y límites |
|---|---|---|---|
| Repositorio en organización, nombre de convención y público | Cumple | https://github.com/ISCOUTB/AS_202620_UTB_TRACKER | Clon público por protocolo git sin pedir acceso; API de runs respondió HTTP 200. No se consultó API de metadatos. |
| Estructura mínima presente | Cumple | git ls-tree -r 277098684766fdf35f12b9d6713ee78c423a08b4; README.md:1; docs/aspectos.md:1; docs/ia.md:1 | Existen docs/arc42/, docs/adr/, docs/c4/, aspectos, IA y README. Presencia no implica que todas las secciones estén completas. |
| Estado calificado identificable | Cumple | refs/remotes/origin/main 277098684766fdf35f12b9d6713ee78c423a08b4 2026-10-18T23:20:54-05:00 | Commit anterior al cierre y punta actual coincidentes; cero commits tardíos observados. |
| Nombres de ADR según convención | Cumple | inventario git docs/adr/ en 277098684766fdf35f12b9d6713ee78c423a08b4 | Archivos Markdown numerados con cuatro dígitos y nombres kebab-case; .gitkeep no se evalúa como ADR. |
| ADR aceptados no reescritos | No cumple | docs/adr/0001-estilo-arquitectonico.md:3-61; diff ae17616 | El ADR aceptado se reescribió de Django/viajes a FastAPI/préstamos, incluyendo contexto, decisión y alternativas. Debió preservarse y reemplazarse mediante otro ADR. |
| Registro de IA al día para la semana | No cumple | docs/ia.md:15-28; commit ae17616 del 2026-10-18 | Registro actualizado, pero adopta propuestas sin descartes técnicos razonados; falta el criterio requerido por contrato. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | .github/workflows/ci.yml:43-50; sonar-project.properties:1-2: run failure y organización declarada iscoutb, distinta de isco-utb; falta Quality Gate público verificable. | No se completa la triple evidencia requerida: configuración, run de scanner exitoso y análisis/Quality Gate público correspondiente. No se confunde CI general con gate. |
| Sin credenciales en repositorio ni historial | No verificado | git grep -nIE sobre 277098684766fdf35f12b9d6713ee78c423a08b4; inventario .env; revisión histórica parcial | Barrido de patrones en la punta sin secreto real confirmado; coincidencias de código, pruebas o documentación no se publican como credenciales. El barrido histórico no pudo completarse por demoras/aborto de conexión al recuperar blobs antiguos; faltaría cerrar la revisión del historial, no solo comprobar la punta. |
| Contribución de todos los integrantes | No verificado | git shortlog -sne 277098684766fdf35f12b9d6713ee78c423a08b4; EQUIPOS.md | El historial agrupa alias con el mismo correo y la doble identidad documentada en EQUIPOS.md: aparecen aportes atribuibles a tres integrantes, sin correspondencia verificada para el cuarto. Esta incertidumbre de atribución no demuestra ausencia de contribución. No se publican identidades ni se presenta cada correo como persona distinta; cualquier correspondencia adicional debe ser confirmada por el equipo. |

## Recuento y nota sugerida

**2/9 Cumple. Nota sugerida: 1.9/5.0**, calculada como `1 + 4 × (2/9)`, redondeada a un decimal. **Propuesta al docente; la nota final la fija el profesor en Moodle.** La nota S12 es PRELIMINAR y puede cambiar hasta el cierre; no constituye entrega vencida.

## overall · proyecto en la punta actual

Se incorporaron capas de servicio, JWT, pooling, idempotencia y utilidades de resiliencia. El diseño de no extracción es válido. El timeout de pool no es límite de duración de una consulta; las utilidades retry/breaker no están aplicadas a la operación de préstamos. La búsqueda de idempotencia antecede al bloqueo (app/services/loans.py:29-49): no se demuestra aquí la carrera de dos solicitudes con la misma clave ni se garantiza aislamiento por usuario/payload. No se ejecutó código para confirmar esos riesgos.

No hay cambios posteriores al cierre en la rama principal observada. La revisión S12 aplica sus criterios al estado completo actual; no modifica la nota de S11 ni recalifica entregas anteriores.

## Fallos probados, documentados y límites de CI

tests/test_resilience.py:32-67 verifica reenvío secuencial; :70-135 prueba utilidades aisladas, no caída/latencia de PostgreSQL ni carrera real. El run del hash evaluado terminó en failure: https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/39199034464. No se atribuye una causa sin logs ni se declara la suite en verde por lo escrito en docs/ia.md. .github/workflows/ci.yml:43-50 configura suite y scanner, pero no acredita su éxito.

## Pendientes prioritarios

- Tabla operación a garantía de consistencia con operaciones reales: ACID se describe globalmente; falta tabla operación→garantía.
- Dos operaciones verificadas contra la implementación: Se contrastaron crear préstamo y crear recurso: ambas hacen commit local; préstamos añade bloqueo condicional PostgreSQL. Sin garantías por operación ni prueba concurrente no se acreditan dos verificaciones completas.
- Diseño de caché: qué, dónde y cuánto: No hay diseño de caché ni justificación explícita para prescindir de ella.
- Política de invalidación tras escritura: Falta declarar qué hacer al crear un recurso o prestar uno si se cachea el catálogo; hoy no se demuestra un defecto por caché inexistente.
- ADR de la decisión de datos más costosa de revertir: ADR de no extracción, no selección comparada de la decisión de datos más costosa.
- Argumento y costo de reversión de esa decisión: No se estima costo de migrar/revertir la decisión de datos ni se explica por qué sería el mayor.
- arc42 sección 8 con consistencia y caché: Sección 8 describe ACID/idempotencia pero omite estrategia de caché y garantías completas por operación.
- El taller de mensajes se evalúa aparte. No se exige introducir caché o broker si su ausencia está razonada; sí precisar las garantías, los límites y las decisiones de datos.
