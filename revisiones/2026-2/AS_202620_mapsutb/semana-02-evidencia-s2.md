# Evidencia S2 · mapsutb

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `1cf15768d257c8cdf4ac9e600892d805285f2a5a` · `2026-08-16T21:26:05-05:00` (último commit ≤ cierre 2026-08-17T05:00:00Z) |
| Comandos principales | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only <hash>`; `git show <hash>:docs/*.md`; `git grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template'`; `git grep -nI -E '<regex secretos>'`; `git log -- docs/ia.md` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42.md` («Introducción y objetivos», tabla de interesados con rol e interés) | No cumple | La sección 1 lista atributos de calidad con motivación y una buena tabla de stakeholders, pero no declara objetivos de negocio ni los asocia a su interesado |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/restricciones.md` (técnicas, organizacionales, políticas/institucionales; columna Justificación en cada fila) | Cumple | Cada restricción dice de dónde viene. Falta la clase legal de la ficha (términos de APIs, protección de datos de geolocalización) |
| Restricciones separadas de los requisitos | `docs/restricciones.md` frente a `docs/arc42.md` y `docs/ficha-problema.md` | Cumple | No mezcla requisitos funcionales; alguna fila es decisión de alcance (interiores fuera de alcance) más que restricción |
| arc42 sección 3 con actores y sistemas externos | `docs/c4_contexto.md` (3 actores persona + 6 servicios externos de Google, con relación) | Cumple | Contenido de contexto completo; no hay diagrama con el que contrastar coherencia (ver fila C4) |
| Entre 3 y 5 escenarios de calidad redactados | `docs/escenarios_calidad.md` (escenarios 1 a 5) | Cumple | 5 escenarios numerados |
| Cada escenario con sus seis partes y medida numérica | `docs/escenarios_calidad.md` (tabla enunciado + medida) | No cumple | Las 5 filas son enunciado + medida, sin separar fuente/estímulo/artefacto/entorno/respuesta. Las medidas sí tienen cifra y unidad (3 s; 5 s y <10 m; 0 % caídas; <2 min; 90 %), pero la mayoría sin condición de carga. El único escenario en formato de seis partes es el embebido en `docs/aspectos.md` (A-01) |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arbol_utilidad.md` | No cumple | Lista de atributos con sub-bullets, sin valoración de impacto/riesgo ni relación explícita con los escenarios; además `docs/escenarios_calidad.md` enlaza a `./02_arbol_utilidad.md`, archivo que no existe (el real es `arbol_utilidad.md`) |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4_contexto.md` | No cumple | No hay diagrama: el propio archivo declara «no incluye diagramas C4 explícitos… como punto de partida para construir el diagrama». Solo tabla de actores/sistemas; sin leyenda ni flechas |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` (única fila A-01) | No cumple | Solo hay una fila y no enlaza a los 5 escenarios de `docs/escenarios_calidad.md`; el escenario A-01 está embebido en el mismo archivo, sin enlace desde la tabla |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `revisiones/2026-2/_meta/lsremote.txt:22`; clon sin autenticación | Cumple | Sin cambios respecto a S1 |
| Estructura mínima presente | árbol de `1cf15768` | No cumple | Arc42 como archivo único `docs/arc42.md` (no en `docs/arc42/`); sin `docs/adr/` ni `docs/c4/`; el contexto está en `docs/c4_contexto.md`. Desviación registrada, no ausencia |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` | Cumple | `1cf15768d257c8cdf4ac9e600892d805285f2a5a` · `2026-08-16T21:26:05-05:00`. La etiqueta `corte-1` sigue apuntando al commit de S1 (`7e56ad3`) |
| Nombres de ADR según la convención | sin `docs/adr/` → filtro vacío | Cumple | Vacuo: sin ADR (no exigidos en S2) |
| ADR aceptados no reescritos | sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md` → único commit `2026-08-09 f829f2e` | No cumple | Sin entradas nuevas durante S2 (la documentación de esta semana no registra uso de IA). La estructura Aceptado/Rechazado sigue siendo buena |
| Sin credenciales en el repositorio ni en el historial | `git grep -nI -E '<regex>' 1cf15768` (sin salida); sin `.env`; `git log -S'BEGIN PRIVATE KEY'` (vacío) | Cumple | Sin coincidencias |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` → `nerlis-otero` 4, `charlygz21` 3, `CarlosManrique-1397` 1 | No cumple | 3 identidades para 4 integrantes; sin cuenta atribuible a Isabel Sofia Paez Matallana en todo el historial |

## Recuento de criterios

4 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Nada quedó sin verificar por falta de herramientas: todo lo evaluable estaba en texto plano dentro del repositorio.

## Hallazgos para la planilla

- Entregas tardías: ninguna (sin commits después del cierre S2).
- Estructura: arc42 fuera de `docs/arc42/` (un solo `docs/arc42.md`); sin `docs/adr/` ni `docs/c4/`; sin diagrama C4 de ningún tipo.
- Enlace roto: `docs/escenarios_calidad.md` → `./02_arbol_utilidad.md` (no existe).
- Árbol de utilidad sin impacto/riesgo y sin vínculo a los escenarios.
- Escenarios sin el formato de seis partes (solo enunciado + medida); medidas sin condición de carga en su mayoría.
- Contribución: 3 de 4 integrantes con commits; Isabel Sofia Paez Matallana sin aparición.
- Etiqueta `corte-1` mal ubicada (apunta al commit de S1).
- Para el corte 1: los 5 escenarios tienen cifra y unidad, pero ninguno declara cómo se medirá (herramienta, carga y umbral de la medición); solo el escenario A-01 de `docs/aspectos.md` tiene las seis partes completas.
