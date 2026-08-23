# Evidencia S2 · TAIA

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `59590c9243aad55222769426c45f6f7d4084572e` · `2026-08-16T19:15:15-05:00` («Feat: updating ia.md») |
| Cierre S2 | `2026-08-17T05:00:00Z` (domingo 16 de agosto medianoche, Colombia) |
| Comandos principales ejecutados | `git log -1 --until`; `git ls-tree -r --name-only $HASH`; `git show $HASH:docs/arc42/arc42-template-EN.md`; `grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template'`; `git show $HASH:docs/calidad/*`; `git show $HASH:docs/c4/C4-ContextoTAIA.png` (imagen no inspeccionable por el agente); `git grep` (secretos); `git log --after` (tardías) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/arc42-template-EN.md:18-98` en `59590c9` | Cumple | Objetivos de calidad con motivación y métrica (76-88) y tabla de Stakeholders rellena con expectativas (91-96) |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/arc42-template-EN.md:99-134` | No cumple | Clasificadas en técnicas, organizacionales y convenciones, cada una con su implicación arquitectónica (excelente justificación), pero no hay categoría legal |
| Restricciones separadas de los requisitos | sección 2 (99-134) vs «Requirements Overview» (42-74) | Cumple | Separación clara, incluida la distinción MVP / deseable / fuera de alcance |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42/arc42-template-EN.md:135-149` | No cumple | «Context and Scope» conserva los placeholders de plantilla (`\<Diagram or Table\>`); sin actores ni sistemas externos identificados |
| Entre 3 y 5 escenarios de calidad redactados | `docs/calidad/escenarios_calidad.md` en `59590c9` | Cumple | 5 escenarios redactados. Desviación de estructura: viven en `docs/calidad/`, no en la sección 10 del arc42, que quedó vacía (líneas 297-303) |
| Cada escenario con sus seis partes y medida numérica | `docs/calidad/escenarios_calidad.md` | No cumple | Los 5 desglosan las seis partes, pero el escenario 5 («Sustitución del modelo de IA») no tiene medida numérica («el cambio queda solo en la capa de adaptador» = enunciado). Los otros 4 sí tienen cifra, unidad y condición |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/calidad/arbol_utilidad.md` | No cumple | Es una jerarquía plana de atributos, sin valores de impacto ni riesgo |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/C4-ContextoTAIA.png` (solo imagen, no código) | No verificado | El archivo existe (378 KB), pero este agente no puede inspeccionar imágenes: haría falta abrir el PNG para comprobar leyenda y flechas etiquetadas. Anotado que es imagen, no código como prefiere el curso |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` en `59590c9` | No cumple | La fila de A-01 sigue con C4/ADR/Código/Pruebas/Evidencia en «Pendiente» y no hay enlaces a los escenarios |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:18` | Cumple | — |
| Estructura mínima presente | `git ls-tree -r 59590c9`: `README.md`, `docs/arc42/`, `docs/c4/C4-ContextoTAIA.png`, `docs/aspectos.md`, `docs/ia.md`; falta `docs/adr/` | No cumple | `docs/adr/` sigue sin existir (se crea el 22-ago, ya en semana 3) |
| Estado calificado identificable | `59590c9243aad55222769426c45f6f7d4084572e` · `2026-08-16T19:15:15-05:00` | Cumple | Commit anterior al cierre, sin etiqueta |
| Nombres de ADR según la convención | No existe `docs/adr/` | Cumple | Sin ADR al cierre |
| ADR aceptados no reescritos | Sin ADR al cierre | Cumple | No aplica por ausencia |
| `docs/ia.md` al día para la semana | commit `59590c9` (16-08) dentro del periodo; Entradas 001 y 002 | Cumple | La Entrada 001 documenta lo rechazado con motivo; la 002 solo registra lo aceptado |
| Sin credenciales en el repositorio ni en el historial | `git grep` regex §9 sobre `59590c9`: sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'`: vacío | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne 59590c9`: val (2 identidades consolidadas), dei0811, luis20072002, mark | Cumple | Los 4 integrantes constan en el historial |

## Recuento de criterios

- **3 de 9** criterios cumplidos en la matriz de la ficha (1 fila No verificado).

## No verificado / pendientes

- C4 de contexto: `docs/c4/C4-ContextoTAIA.png` es una imagen que el agente de revisión no pudo inspeccionar. Haría falta abrirla manualmente para comprobar leyenda y flechas etiquetadas.

## Hallazgos para la planilla

- Entrega a tiempo: `59590c9` (16-ago 19:15). Después del cierre siguieron trabajando (20-ago: actualización de escenarios y árbol; 22-ago: ADR 0001 y esqueleto de backend) — trabajo de semana 3.
- Sección 3 del arc42 con texto de plantilla; sección 10 vacía (los escenarios están en `docs/calidad/` — desviación de estructura, evaluados donde están).
- Escenario 5 sin medida numérica (enunciado).
- Árbol de utilidad sin impacto/riesgo.
- C4 solo como imagen PNG (el curso prefiere diagramas como código).
- `docs/adr/` inexistente hasta el 22-ago (post-cierre).
- Restricciones sin categoría legal; `docs/aspectos.md` sin enlaces a los escenarios.
- El propio equipo anota en la sección 2 que `README.md` está codificado en UTF-16 LE, a diferencia del resto del repositorio (UTF-8).
- Cuenta observada «mark» no coincide con «EtienneGW» del listado de EQUIPOS.md; correspondencia no evidente, a confirmar con el equipo.
