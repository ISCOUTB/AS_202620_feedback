# Evidencia S2 · Calificación automática

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `d4302f4b6fef2d1eec2c3d39f491726494fddfd9` · `2026-08-16T23:17:26-05:00` («ia.md actualizado») |
| Cierre S2 | `2026-08-17T05:00:00Z` (domingo 16 de agosto medianoche, Colombia) |
| Comandos principales ejecutados | `git log -1 --until`; `git ls-tree -r --name-only $HASH`; `git show $HASH:docs/arc42/arc42-template-ES.md`; `grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template'` (solo falsos positivos de «todo» en frases); `git show $HASH:docs/c4/doc-c4.md`; `git grep` (secretos); `git log --after` (tardías) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/arc42-template-ES.md:16-53` en `d4302f4` | Cumple | «Quality Goals» (35-43) y tabla de Stakeholders rellena (45-53) con expectativas por rol; el vínculo objetivo↔interesado se lee en las expectativas |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/arc42-template-ES.md:54-75` | No cumple | 6 restricciones, todas justificadas y con su origen citado, pero la clasificación es propia (tecnológica / de entrada / de diseño / de dominio / de usuarios / de salida): no hay categorías organizativas ni legales como pide la ficha |
| Restricciones separadas de los requisitos | sección 2 (54-75) vs «Requirements Overview» (17-33) | Cumple | Restricciones en su sección, separadas de los requisitos funcionales; ninguna es un requisito disfrazado |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42/arc42-template-ES.md:76-114` | Cumple | Identifica al actor Profesor/TA y no declara sistemas externos, coherente con el C4 de contexto (que documenta por qué la BD es interna) |
| Entre 3 y 5 escenarios de calidad redactados | `docs/arc42/arc42-template-ES.md:262-330` (sección 10) | Cumple | 5 escenarios numerados en la sección 10 |
| Cada escenario con sus seis partes y medida numérica | `docs/arc42/arc42-template-ES.md:272-330` | Cumple | Los 5 desglosan fuente, estímulo, artefacto, entorno, respuesta y medida con cifra, unidad y condición de carga (p. ej. escenario 4: 100 % en ≤10 min con CPU/memoria <85 %) |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arc42/arc42-template-ES.md:226-260` | Cumple | Árbol con anotación «(Impacto: X | Riesgo técnico: Y)» en cada hoja, y los escenarios redactados son los priorizados |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/doc-c4.md` (mermaid, código) | Cumple | Como código ✓, ruta `docs/c4/doc-c4.md`. Flecha etiquetada («Carga exámenes… [HTTPS / Web UI]»); leyenda vía estereotipos «person»/«system» en los nodos más tabla «Elementos del contexto». Solo 1 actor y sin sistemas externos (justificado en la nota del archivo) |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` en `d4302f4` | No cumple | La tabla de trazabilidad de A-01 sigue con C4/ADR/Código/Pruebas/Evidencia en «Pendiente» y no hay enlaces a los 5 escenarios del arc42 |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:17` | Cumple | — |
| Estructura mínima presente | `git ls-tree -r d4302f4`: `README.md`, `docs/arc42/`, `docs/adr` (blob vacío), `docs/c4/doc-c4.md`, `docs/aspectos.md`, `docs/ia.md` | Cumple | `docs/adr` sigue siendo un blob vacío, no un directorio (observación de montaje que se arrastra de S1) |
| Estado calificado identificable | `d4302f4b6fef2d1eec2c3d39f491726494fddfd9` · `2026-08-16T23:17:26-05:00` | Cumple | Commit anterior al cierre, sin etiqueta |
| Nombres de ADR según la convención | `docs/adr` sin contenido al cierre | Cumple | Sin ADR todavía (el primero llega el 22-ago, ya en semana 3) |
| ADR aceptados no reescritos | Sin ADR al cierre | Cumple | No aplica por ausencia |
| `docs/ia.md` al día para la semana | commit `d4302f4` (16-ago) dentro del periodo; Entrada 2 con lo aceptado, lo rechazado y su motivo | Cumple | — |
| Sin credenciales en el repositorio ni en el historial | `git grep` regex §9 sobre `d4302f4`: sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'`: vacío | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne d4302f4`: 1 persona de 4 | No cumple | Solo `scp1109` hasta el cierre de S2; `josueacademico17-source` empieza el 22-ago; sin cuentas de los otros dos integrantes |

## Recuento de criterios

- **7 de 9** criterios cumplidos en la matriz de la ficha.

## No verificado / pendientes

- Nada adicional: todo lo calificable se pudo leer desde el repositorio.

## Hallazgos para la planilla

- Entrega a tiempo: `d4302f4` (16-ago 23:17, 43 minutos antes del cierre). Los commits del 18 y 22-ago (plantilla ADR, `0001`, actualización de arquitectura) son trabajo de semana 3, posterior al cierre.
- Restricciones sin categorías organizativas ni legales (todas técnicas/de alcance), aunque muy bien justificadas.
- `docs/aspectos.md` no enlaza los 5 escenarios del arc42 (tabla de trazabilidad en «Pendiente»).
- Se arrastra de S1: `docs/adr` como blob vacío; ficha del problema fuera del repositorio; solo 1 cuenta contribuyendo.
- Para la S3: el ADR creado el 22-ago queda en `docs/adr/0001.md`, nombre que no sigue la convención `NNNN-titulo-en-kebab-case.md`.
