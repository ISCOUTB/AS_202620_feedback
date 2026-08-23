# Evidencia S2 · ShareU

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `aa0659c1666479ec1d163ab00c5f4544b86e3f5a` · `2026-08-16T22:47:16-05:00` («Fix formatting issues in arc42 template document») |
| Cierre S2 | `2026-08-17T05:00:00Z` (domingo 16 de agosto medianoche, Colombia) |
| Comandos principales ejecutados | `git log -1 --until`; `git ls-tree -r --name-only $HASH`; `git show $HASH:docs/arc42-template-EN.md`; `grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template'`; `git grep -niE 'escenario|mermaid|C4|diagrama' $HASH`; `git grep` (secretos); `git log --after` (tardías) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42-template-EN.md:18-80` en `aa0659c` | No cumple | Hay objetivos de calidad con prioridades (46-65), pero la tabla de Stakeholders (70-80) sigue con texto de plantilla (`\<Role-1\>`, `\<Contact-1\>`) y ningún objetivo dice a quién le importa |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42-template-EN.md:82` | No cumple | «Architecture Constraints» vacía: solo el encabezado, sin restricciones ni clasificación |
| Restricciones separadas de los requisitos | sección 2 vacía vs «Requirements Overview» (25-45) | No cumple | No hay restricciones que separar de los requisitos |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42-template-EN.md:84-98` | No cumple | «Context and Scope» conserva los placeholders de plantilla (`\<Diagram or Table\>`); no identifica actores ni sistemas externos |
| Entre 3 y 5 escenarios de calidad redactados | `git grep -niE 'escenario' aa0659c`: solo `docs/aspectos.md:11` | No cumple | Solo 1 escenario (Usabilidad, en `docs/aspectos.md`); la sección 10 del arc42 (líneas 253-259) está vacía |
| Cada escenario con sus seis partes y medida numérica | `docs/aspectos.md:13-25` | Cumple | El único escenario existente desglosa fuente, estímulo, artefacto, entorno, respuesta y medida numérica («menos de 3 interacciones»). Faltan los otros 2-4 escenarios exigidos |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arc42-template-EN.md:61-65` | No cumple | Solo hay un párrafo de «Priorización» con prioridades cualitativas (Muy alta/Alta/Media); no hay árbol ni priorización por impacto y riesgo |
| C4 de contexto con leyenda y flechas etiquetadas | `git grep -niE 'mermaid|C4|diagrama' aa0659c`: sin resultados en `docs/c4/` (el directorio no existe) | No cumple | No hay diagrama C4 de contexto en ninguna ruta ni formato |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md:5-25` | Cumple | El escenario está contenido en la sección del aspecto Usabilidad y es alcanzable desde ella. Observación: no hay tabla de 8 columnas con enlaces, el archivo es prosa |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:16` | Cumple | — |
| Estructura mínima presente | `git ls-tree -r aa0659c`: `README.md`, `docs/arc42-template-EN.md`, `docs/aspectos.md`, `docs/ia.md`; faltan `docs/arc42/`, `docs/adr/`, `docs/c4/` | No cumple | La plantilla arc42 está en `docs/` (desviación de estructura), y `docs/adr/` y `docs/c4/` siguen sin crearse |
| Estado calificado identificable | `aa0659c1666479ec1d163ab00c5f4544b86e3f5a` · `2026-08-16T22:47:16-05:00` | Cumple | Commit anterior al cierre, sin etiqueta |
| Nombres de ADR según la convención | No existe `docs/adr/` | Cumple | Sin ADR; filtro vacío |
| ADR aceptados no reescritos | Sin ADR | Cumple | No aplica por ausencia |
| `docs/ia.md` al día para la semana | commit `b980836` (16-ago) dentro del periodo; contenido: herramientas y lineamientos, sin registro de usos ni de lo rechazado | No cumple | Actualizado en la semana, pero sin entradas reales ni motivos de rechazo |
| Sin credenciales en el repositorio ni en el historial | `git grep` regex §9 sobre `aa0659c`: sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'`: vacío | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne aa0659c`: Dayana (12), Nicolas-HH (8), steven (1); falta Luis Carlos Corredor | No cumple | 3 de 4 integrantes; no aparece ninguna cuenta atribuible a Luis Carlos Corredor Altamiranda |

## Recuento de criterios

- **2 de 9** criterios cumplidos en la matriz de la ficha.

## No verificado / pendientes

- Nada adicional: todo lo calificable se pudo leer desde el repositorio.

## Hallazgos para la planilla

- Sin entregas tardías en S2: último commit antes del cierre `aa0659c`; no hay commits posteriores al 17-ago.
- Cambio de problema entre S1 y S2: la ficha «EncuentraUTB» (objetos perdidos) se borra (`cf57f6e`, 16-ago) y el proyecto pasa a «ShareU» (material académico). El README se reescribe (`eb31957`). Repositorio y contenido quedan alineados con el nombre ShareU, pero el giro debe reflejarse en toda la documentación para el corte 1.
- Secciones 2, 3 y 10 del arc42 vacías o con placeholders de plantilla; stakeholders sin rellenar.
- Un solo escenario de calidad (bien formado, con seis partes y medida), cuando se piden de 3 a 5.
- Sin árbol de utilidad y sin C4 de contexto; `docs/adr/` y `docs/c4/` siguen sin existir.
- `docs/ia.md` anuncia una «tabla de registro» que no tiene entradas.
- Luis Carlos Corredor Altamiranda sigue sin aparecer en el historial.
