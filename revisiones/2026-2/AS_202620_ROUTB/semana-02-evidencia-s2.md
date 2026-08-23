# Evidencia S2 · ROUTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `14e66888c12156bc7ffd6c8d9529345958f1bd56` · `2026-08-16T12:44:08-05:00` («ROUTB - Semana 2») |
| Cierre S2 | `2026-08-17T05:00:00Z` (domingo 16 de agosto medianoche, Colombia) |
| Comandos principales ejecutados | `git log -1 --until`; `git ls-tree -r --name-only $HASH`; `git show $HASH:docs/arc42/arc42-template-EN.md`; `grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template'`; `git show $HASH:docs/c4/context.md`; `git grep` (secretos); `git log --after` (tardías) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/arc42-template-EN.md:18-103` en `14e6688` | No cumple | Hay «Objetivos de calidad» (líneas 44-53) y tabla de Stakeholders (95-103), pero ningún objetivo dice a quién le importa, y los «Objetivos específicos» (28-35) son funcionalidades |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/arc42-template-EN.md:106-147` | No cumple | Cada restricción está justificada («dado que…»), pero la clasificación es propia (técnicas / integración / comerciales y de alcance): no hay categorías organizativas ni legales |
| Restricciones separadas de los requisitos | sección 2 (106-147) vs «Descripción general de los requisitos» (36-42) | Cumple | Las restricciones están en su sección; ninguna es un requisito funcional disfrazado |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42/arc42-template-EN.md:148-256` | No cumple | Identifica actores y sistemas, pero no corresponde con el C4 de contexto: incluye «Universidad» (ausente del C4) y el contexto técnico añade App Flutter y PostgreSQL, que no están en el C4 |
| Entre 3 y 5 escenarios de calidad redactados | `docs/arc42/arc42-template-EN.md:85-93` (5 filas) | Cumple | 5 escenarios (rendimiento, usabilidad, seguridad, disponibilidad, escalabilidad). Desviación de estructura: están en la sección 1; la sección 10 (líneas 404-408) quedó vacía |
| Cada escenario con sus seis partes y medida numérica | `docs/arc42/arc42-template-EN.md:87-93` | No cumple | Tabla de dos columnas sin desglosar fuente/estímulo/artefacto/entorno/respuesta/medida; falta el entorno en varios escenarios y la condición de carga en 4 de 5 medidas («3 pasos», «100 % endpoints», «99 % mensual» no declaran carga) |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arc42/arc42-template-EN.md:57-84` | No cumple | El árbol es una jerarquía plana de atributos sin valores de impacto/riesgo. La priorización 1-8 está en otra tabla (44-53) y no coincide con los escenarios redactados (Usabilidad, prioridad 8, sí está; Portabilidad 5, Mantenibilidad 6 y Privacidad 7 no) |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/context.md` (mermaid, código) | No cumple | Está como código ✓ (ruta `docs/c4/context.md`), pero las flechas no llevan etiqueta y no hay caja de leyenda (solo `classDef` con colores). Además el sistema aparece dos veces: `R` y `ROUTB` como nodos distintos |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` en `14e6688` | No cumple | Una sola fila, sin enlaces a escenarios ni columnas C4/ADR/código/pruebas/evidencia |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:14` | Cumple | — |
| Estructura mínima presente | `git ls-tree -r 14e6688`: las seis rutas | Cumple | — |
| Estado calificado identificable | `14e66888c12156bc7ffd6c8d9529345958f1bd56` · `2026-08-16T12:44:08-05:00` | Cumple | Commit anterior al cierre, sin etiqueta |
| Nombres de ADR según la convención | `docs/adr/` solo `.gitkeep` | Cumple | Sin ADR todavía |
| ADR aceptados no reescritos | Sin ADR | Cumple | No aplica por ausencia |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia.md`: último commit `b9b4ee8` (08-08), fuera del periodo S2; contenido idéntico al de S1, «Pendiente por documentar» | No cumple | Sin actualización en la semana ni registro de rechazos |
| Sin credenciales en el repositorio ni en el historial | `git grep` regex §9 sobre `14e6688`: sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'`: vacío | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: MKeinerrr (19+2, identidades consolidadas), diegobrr999-commits (6), juliandmanjarrez-tech (3), junior14700 (2) | Cumple | Los 4 integrantes constan en el historial |

## Recuento de criterios

- **2 de 9** criterios cumplidos en la matriz de la ficha.

## No verificado / pendientes

- Nada adicional: todo lo calificable se pudo leer desde el repositorio.

## Hallazgos para la planilla

- Sin entregas tardías: `14e6688` dentro del plazo. Después del cierre solo `df174b9` (22-ago, «Changes - Semana 3 (#3)»).
- Sección 10 vacía; escenarios viven en la sección 1 (desviación de estructura, no ausencia).
- Escenarios sin las seis partes; medidas sin condición de carga en 4 de 5.
- Árbol de utilidad sin impacto/riesgo; prioridades de la tabla de objetivos no casan con los escenarios redactados.
- C4: sin etiquetas en las flechas, sin leyenda visible, nodo del sistema duplicado (`R` y `ROUTB`).
- `docs/aspectos.md` sigue con una sola fila y sin enlaces (se arrastra de S1, igual que `ia.md` en blanco).
- Queda pendiente declarar tensiones de calidad de la S1.
- Restricciones sin categorías organizativas ni legales.
