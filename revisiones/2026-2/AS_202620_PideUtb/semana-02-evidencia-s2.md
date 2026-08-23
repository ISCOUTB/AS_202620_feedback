# Evidencia S2 · PideUtb

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `9b5f21485776472f75d9b4c571f711dccfb5f992` · `2026-08-16T12:47:26-05:00` (último commit ≤ cierre 2026-08-17T05:00:00Z) |
| Comandos principales | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only <hash>`; `git show <hash>:arc42.md`; `git show <hash>:docs/aspectos.md`; `git grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template'`; `git grep -nI -E '<regex secretos>'`; `git log -- docs/ia.md` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `arc42.md` §1.2 (objetivos de negocio) y §1.3 (tabla de interesados con intereses) | Cumple | Objetivos de negocio (reducir filas, disminuir tiempo, organizar pedidos…), no funcionalidades; el «a quién le importa» está en la tabla 1.3, no mapeado uno a uno |
| arc42 sección 2 con restricciones clasificadas y justificadas | `arc42.md` §2.1 técnicas, §2.2 organizativas, §2.3 legales, cada una con justificación | Cumple | Incluye la clase legal (declara no haber restricción específica y anticipa protección de datos personales) |
| Restricciones separadas de los requisitos | `arc42.md` §2 frente a §1.2/§1.4 | Cumple | La sección 2 solo lista restricciones con su motivo; sin requisitos funcionales mezclados |
| arc42 sección 3 con actores y sistemas externos | `arc42.md` §3.1 (Estudiante, Personal, Administrador, Wompi, Supabase) | Cumple | Coherente con el diagrama Mermaid de §3.2: mismos actores y sistemas externos |
| Entre 3 y 5 escenarios de calidad redactados | `arc42.md` §10.2–10.6 (ESC-01 a ESC-05) | Cumple | 5 escenarios numerados |
| Cada escenario con sus seis partes y medida numérica | `arc42.md` §10.2–10.6 (tablas Fuente/Estímulo/Artefacto/Entorno/Respuesta/Medida) | Cumple | Medidas con cifra y unidad: <3 min; <2 min en ≥90 %; ≤10 s y ≤3 interacciones; <2 s y 100 % rechazo de reutilización; <3 s y 100 % conservación del carrito |
| Árbol de utilidad que prioriza por impacto y riesgo | `arc42.md` §10.1 (árbol con convención A/M = impacto alto/riesgo medio, A/B, M/B) | Cumple | Priorización explícita por impacto y riesgo, por atributo y por escenario, y los escenarios del árbol son los redactados |
| C4 de contexto con leyenda y flechas etiquetadas | `arc42.md` §3.2 (código Mermaid `C4Context`) | Cumple | Como código (no solo imagen). Flechas etiquetadas (`Rel(...)` con texto y protocolo HTTPS/API); la leyenda de formas la genera el render de Mermaid C4Context. Está embebido en `arc42.md` en la raíz, no en `docs/c4/` (desviación) |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` (tablas «Escenario relacionado» por aspecto); seguí Usabilidad→ESC-01 y Confiabilidad→ESC-04 | Cumple | Ambos enlaces resuelven a `arc42.md` con ancla correcta. Ojo: los enlaces de Seguridad, Disponibilidad y Rendimiento usan anclas con guiones de menos (`--` en vez de `-----`) y no resolverán en GitHub |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `revisiones/2026-2/_meta/lsremote.txt:13`; clon sin autenticación | Cumple | Sin cambios respecto a S1 |
| Estructura mínima presente | árbol de `9b5f214` | No cumple | Arc42 como `arc42.md` en la raíz (no `docs/arc42/`); sin `docs/adr/` ni `docs/c4/`; C4 embebido en arc42.md; ficha sigue en PDF |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` | Cumple | `9b5f21485776472f75d9b4c571f711dccfb5f992` · `2026-08-16T12:47:26-05:00` (merge) |
| Nombres de ADR según la convención | sin `docs/adr/` → filtro vacío | Cumple | Vacuo: sin ADR (no exigidos en S2) |
| ADR aceptados no reescritos | sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md` → `2026-08-16 dfd3086` (uso en la segunda entrega) | No cumple | Hay entrada del periodo S2, pero no registra qué se rechazó y por qué (CONTRATO §6) |
| Sin credenciales en el repositorio ni en el historial | `git grep -nI -E '<regex>' 9b5f214` (sin salida); sin `.env`; `git log -S'BEGIN PRIVATE KEY'` (vacío) | Cumple | Sin coincidencias |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` → `daniarriet` 5, `Santiago Cuesta` 3, `Santiago-C0` 1 (misma persona, EQUIPOS.md:95) | No cumple | 2 personas de 3; Ruddy Rodriguez Romero sin cuenta observada en el historial |

## Recuento de criterios

9 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Nada quedó sin verificar: todo lo evaluable estaba en texto (Markdown/Mermaid) dentro del repositorio.

## Hallazgos para la planilla

- Entregas tardías: ninguna (sin commits después del cierre S2).
- Estructura: arc42 en la raíz del repo (`arc42.md`), sin `docs/arc42/`, `docs/adr/` ni `docs/c4/`; ficha del problema solo en PDF.
- Anclas rotas en `docs/aspectos.md`: las filas de Seguridad, Disponibilidad y Rendimiento usan `--` donde el encabezado genera `-----`.
- Contribución: Ruddy Rodriguez Romero sin aparición; Daniela Sofia Arrieta Guardo concentra 5 de 9 commits.
- `docs/ia.md` sin columna de lo rechazado.
- Para el corte 1: los 5 escenarios tienen medida comprobable (cifra + unidad; ESC-02 y ESC-03 con condición de carga). El documento declara que son objetivos iniciales, no resultados; ninguno declara todavía herramienta, carga y umbral de la medición.
