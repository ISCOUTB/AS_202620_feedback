# AS_202620_XALD · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_XALD/tree/405a39e0feff40a8414841b6936d5a2dc4488ba4) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR S12 — aún abierta.** Revisión académica del contenido completo disponible en la rama principal; no se toma la falta de commits como ausencia de revisión.

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
| Tabla operación a garantía de consistencia con operaciones reales | No cumple | `docs/arc42/08-Cross-cutting Concepts.md:65-73` | Tabla de casos de recepción/idempotencia, no tabla operación→consistencia para las operaciones reales del sistema. |
| Dos operaciones verificadas contra la implementación | No cumple | `XALDAPP/corefinanciero/src/main/java/com/proyecto/xald/corefinanciero/GestorCoreFinanciero.kt:11-23; backend/app/main.py:58-60,114-148` | Se contrastaron guardar local y registrar remoto: lista en memoria y diccionario de timestamps; no prueban persistencia local ni convergencia completa entre dispositivos. Faltan dos garantías verificadas. |
| Diseño de caché: qué, dónde y cuánto | No cumple | `docs/arc42/08-Cross-cutting Concepts.md:1-92` | No hay diseño de caché ni justificación explícita de no usarla. Una cola/memoria primaria no se convierte por ello en caché. |
| Política de invalidación tras escritura | No cumple | `XALDAPP/corefinanciero/src/main/java/com/proyecto/xald/corefinanciero/GestorCoreFinanciero.kt:13-23; docs/arc42/08-Cross-cutting Concepts.md:55-92` | No se define invalidación tras guardar/reclasificar una transacción; no se afirma que exista caché rota, sino una estrategia todavía no entregada. |
| Garantías del flujo por eventos, si existe | Cumple | `docs/arc42/08-Cross-cutting Concepts.md:59-77,89-92; docs/arc42/11-Risks and Technical Debts.md:55-58` | Diseño de sincronización al menos una vez, con retención hasta 2xx e idempotencia; declara que cliente/envío y persistencia siguen pendientes. Exactamente una vez es una intención condicionada, no garantía implementada duradera. |
| ADR de la decisión de datos más costosa de revertir | No cumple | `docs/adr/0011-resolucion-conflictos-lww.md:7-32; docs/adr/0013-extraer-o-no-integracion-gemini.md:62-79` | ADR de LWW y de no extracción presentes, pero no identifican la decisión de datos más costosa de revertir. |
| Argumento y costo de reversión de esa decisión | No cumple | [docs/adr/0011-resolucion-conflictos-lww.md:27-32](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/docs/adr/0011-resolucion-conflictos-lww.md#L27-L32) | Se explican riesgos, sin comparar ni estimar costo de reversión de la decisión de datos. |
| Almacenes y brokers como contenedores propios en C4 nivel 2 | No cumple | [docs/c4/c2.md:12-27,46-55](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/docs/c4/c2.md#L12-L27) | Nivel 2 dibuja módulos internos y backend; no separa almacenes con tecnología propia. Corregir nivel de abstracción y distinguir memoria actual de Room futuro. |
| arc42 sección 8 con consistencia y caché | No cumple | `docs/arc42/08-Cross-cutting Concepts.md:55-92` | Idempotencia/eventos sí; no completa estrategia de consistencia por operación ni caché. |

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

**1/9 Cumple. Nota sugerida: 1.4/5.0**, calculada como `1 + 4 × (1/9)`, redondeada a un decimal. **Propuesta al docente; la nota final la fija el profesor en Moodle.** La nota S12 es PRELIMINAR y puede cambiar hasta el cierre; no constituye entrega vencida.

## overall · proyecto en la punta actual

S11 está documentada con honestidad sobre lo que falta. El backend aplica LWW y deduplicación de identificador/fecha en memoria; no conserva payload completo ni estado tras reinicio (backend/app/main.py:58-60,117-138). Android usa listas en memoria, no tiene cliente HTTP ni retirada confirmada de cola; Gemini es un mock. Estos límites ya se admiten con plan, por lo que no reducen una fila que admite pendientes. El enunciado de efecto exactamente una vez debe acotarse al proceso vivo; el mismo identificador/fecha no compara contenido.

No hay cambios posteriores al cierre en la rama principal observada. La revisión S12 aplica sus criterios al estado completo actual; no modifica la nota de S11 ni recalifica entregas anteriores.

## Fallos probados, documentados y límites de CI

backend/tests/test_lww.py:48-97,112-132 contiene pruebas de versiones y reenvío duplicado. El bucle de 30 operaciones de :81-87 es secuencial, no una carga concurrente demostrada. CI del hash revisado terminó success: https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/39192603030; .github/workflows/ci.yml:29-37,55-57 configura pruebas Android/backend. MF-01, MF-02 y Gemini siguen sin pruebas de integración ejecutadas, según la propia tabla. No se ejecutó código aquí.

## Pendientes prioritarios

- Tabla operación a garantía de consistencia con operaciones reales: Tabla de casos de recepción/idempotencia, no tabla operación→consistencia para las operaciones reales del sistema.
- Dos operaciones verificadas contra la implementación: Se contrastaron guardar local y registrar remoto: lista en memoria y diccionario de timestamps; no prueban persistencia local ni convergencia completa entre dispositivos. Faltan dos garantías verificadas.
- Diseño de caché: qué, dónde y cuánto: No hay diseño de caché ni justificación explícita de no usarla. Una cola/memoria primaria no se convierte por ello en caché.
- Política de invalidación tras escritura: No se define invalidación tras guardar/reclasificar una transacción; no se afirma que exista caché rota, sino una estrategia todavía no entregada.
- ADR de la decisión de datos más costosa de revertir: ADR de LWW y de no extracción presentes, pero no identifican la decisión de datos más costosa de revertir.
- Argumento y costo de reversión de esa decisión: Se explican riesgos, sin comparar ni estimar costo de reversión de la decisión de datos.
- Almacenes y brokers como contenedores propios en C4 nivel 2: Nivel 2 dibuja módulos internos y backend; no separa almacenes con tecnología propia. Corregir nivel de abstracción y distinguir memoria actual de Room futuro.
- arc42 sección 8 con consistencia y caché: Idempotencia/eventos sí; no completa estrategia de consistencia por operación ni caché.
- El taller de mensajes se evalúa aparte. No se exige introducir caché o broker si su ausencia está razonada; sí precisar las garantías, los límites y las decisiones de datos.
