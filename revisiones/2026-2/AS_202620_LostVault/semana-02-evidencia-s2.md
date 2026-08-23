# Evidencia S2 · LostVault

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `af94a3007c68c5ebedd60efc0eec2a376900c7da` · `2026-08-16T22:09:43-05:00` (último commit ≤ cierre 2026-08-17T05:00:00Z) |
| Comandos principales | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only <hash>`; `git show <hash>:docs/arc42/*.md`; `git grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template'`; `git grep -nI -E '<regex secretos>'`; extracción de `docs/arc42/c4_contexto.png` (PNG 875×630) |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/01_objetivos.md` §1.5 (10 objetivos) y §1.7 (tabla stakeholders/intereses) | Cumple | Objetivos de negocio derivados del problema; el «a quién le importa» está en la tabla 1.7, no mapeado objetivo a objetivo |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/02_restricciones.md` (técnicas, organizativas, legales, cada una con su motivo) | Cumple | Clasificación explícita y justificación por restricción (p. ej. «porque el equipo no tiene definido… el proceso de integración») |
| Restricciones separadas de los requisitos | `docs/arc42/02_restricciones.md` frente a `docs/arc42/01_objetivos.md` §1.3 | Cumple | La sección 2 no lista funcionalidades; el alcance funcional vive en §1.3 y en la ficha del problema |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42/03_contexto.md:23-30` (tabla de 3 actores; declara «no tiene sistemas externos en este nivel») | Cumple | Coherencia visual con el diagrama no verificable en este entorno (PNG, ver fila C4) |
| Entre 3 y 5 escenarios de calidad redactados | `docs/arc42/10_requisitos_calidad.md` — Escenarios 1 a 4 | Cumple | 4 escenarios: Disponibilidad, Usabilidad, Seguridad, Rendimiento |
| Cada escenario con sus seis partes y medida numérica | `docs/arc42/10_requisitos_calidad.md` (fuente/estímulo/artefacto/entorno/respuesta/medida en los 4) | Cumple | Medidas: 99 % mensual con <7 h/mes; 90 % en <3 min; 100 % bloqueados; 95 % ≤2 s (p95) con 200 usuarios concurrentes |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arc42/10_requisitos_calidad.md` «Árbol de utilidad» | No cumple | Es jerárquico y ordenado (no plano) y coincide con los 4 escenarios redactados, pero no valora impacto/riesgo (p. ej. H/M/L); la prioridad con motivos está en `01_objetivos.md` §1.6 |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/arc42/c4_contexto.png` (solo imagen, 875×630; sin versión como código) | No verificado | PNG extraído del commit calificado pero no inspeccionable visualmente en este entorno de revisión: no se pudo confirmar leyenda ni flechas etiquetadas. Además está guardado en `docs/arc42/`, no en `docs/c4/` (desviación de estructura) |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md:5-8` (tabla con enlaces `[Escenario N](arc42/10_requisitos_calidad.md#escenario-…)`); seguí Disponibilidad→Esc 1 y Usabilidad→Esc 2 | Cumple | Los enlaces relativos resuelven al archivo y los anclajes coinciden con los encabezados `## Escenario 1 — Disponibilidad` y `## Escenario 2 — Usabilidad`. La tabla usa solo 3 de las 8 columnas del contrato |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `revisiones/2026-2/_meta/lsremote.txt:11`; clon sin autenticación | Cumple | Sin cambios respecto a S1 |
| Estructura mínima presente | árbol de `af94a300` | No cumple | Faltan `docs/adr/` y `docs/c4/`; el C4 vive en `docs/arc42/c4_contexto.png` (desviación registrada); arc42 con solo las 4 secciones pedidas |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` | Cumple | `af94a3007c68c5ebedd60efc0eec2a376900c7da` · `2026-08-16T22:09:43-05:00` |
| Nombres de ADR según la convención | sin `docs/adr/` → filtro vacío | Cumple | Sin ADR (no exigidos en S2) |
| ADR aceptados no reescritos | sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md` → único commit `2026-08-09 560ba89` | No cumple | Sin entradas nuevas en el periodo S2 (toda la documentación arc42 se escribió sin registrar uso de IA) y sigue sin registrar lo rechazado |
| Sin credenciales en el repositorio ni en el historial | `git grep -nI -E '<regex>' af94a300` (sin salida); sin `.env`; `git log -S'BEGIN PRIVATE KEY'` (vacío) | Cumple | Sin coincidencias |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` → 13 commits, una sola identidad («Roy Gonzalez») | No cumple | 3 de 4 integrantes sin aparición en el historial |

## Recuento de criterios

7 de 9 criterios de la ficha cumplidos (1 No cumple, 1 No verificado).

## No verificado / pendientes

- C4 de contexto: solo imagen; sin leyenda ni flechas confirmables desde este entorno. Haría falta abrir el PNG o versionarlo como código (PlantUML/Mermaid) en `docs/c4/`.
- Coherencia visual sección 3 ↔ diagrama: pendiente por el mismo motivo.

## Hallazgos para la planilla

- Entregas tardías: nada con contenido S2 después del cierre; el commit `0c3f69f` (2026-08-23T11:54:40-05:00, «Add comparative matrix of architectural styles») es posterior al cierre y corresponde a contenido de S3, no a una entrega tardía de S2.
- Contribución: sigue una sola identidad en todo el historial (13 commits); sin commits atribuibles a Jose Faustino Espana Noriega, Shamara Llorente Tapias ni Kiefer Monterroza Manjarres.
- Estructura: `docs/adr/` y `docs/c4/` siguen sin existir; C4 en `docs/arc42/` (desviación, no ausencia).
- `docs/ia.md` sin entradas nuevas durante S2 y sin columna de lo rechazado.
- Árbol de utilidad sin valoración de impacto/riesgo.
- Para el corte 1: los 4 escenarios tienen medida comprobable (cifra + unidad + condición de carga); ninguno declara todavía cómo se medirá (herramienta, carga y umbral de la medición).
