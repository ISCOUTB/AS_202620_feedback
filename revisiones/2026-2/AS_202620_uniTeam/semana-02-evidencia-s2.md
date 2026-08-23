# Evidencia S2 · uniTeam

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `ca7726a38c756eb6b376e7adb744473c8a757a42` · `2026-08-16T13:01:06-05:00` («Update README.md») |
| Cierre de la actividad | `2026-08-17T05:00:00Z` (domingo 16 de agosto, medianoche Colombia) |
| Visibilidad | pública, comprobada con clone y `git ls-remote` sin autenticación (revisiones/2026-2/_meta/lsremote.txt) |

Comandos principales ejecutados: `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only ca7726a`; `git show ca7726a:docs/…`; `git grep -niE '<[a-z /]+>|\bTODO\b|lorem ipsum' ca7726a -- docs/arc42/`; `git shortlog -sne HEAD`; `git log --format='%cI %h' -- docs/ia.md`; `git log --after='2026-08-17T05:00:00Z'`.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/arc42-uniteam.md:22-95`: requisitos funcionales separados (§1.1), 3 metas priorizadas con motivación de negocio (§1.2) e interesados I-01…I-06 con expectativa principal y atributo derivado (§1.3) | Cumple | La ligadura objetivo→interesado se hace vía el atributo derivado (p. ej. I-05→Seguridad, I-02→Rendimiento), no literalmente; los RF están separados de las metas. |
| arc42 sección 2 con restricciones clasificadas y justificadas | `arc42-uniteam.md:96-103`: técnicas T1-T4, organizativas O1-O4 y legales L1-L3, cada una con justificación y consecuencia | Cumple | Clasificación completa (incluye legales, Ley 1581) y origen declarado. |
| Restricciones separadas de los requisitos | §2 con solo restricciones impuestas; los RF están en §1.1 y el documento distingue explícitamente ambos | Cumple | Ninguna restricción es un requisito funcional disfrazado. |
| arc42 sección 3 con actores y sistemas externos | `arc42-uniteam.md:107-141`: tabla de comunicaciones y contexto técnico coherentes con el C4 (mismos actores: estudiante, líder, profesor; mismos externos: IdP y correo) | Cumple | — |
| Entre 3 y 5 escenarios de calidad redactados | `docs/arc42/arc42-uniteam.md:203-215` resume los 5 escenarios ESC-01…ESC-05; detalle completo en `docs/calidad/escenarios-calidad.md` | Cumple | §10 redactada con tabla resumen y enlaces al detalle. |
| Cada escenario con sus seis partes y medida numérica | `docs/calidad/escenarios-calidad.md`: Fuente/Estímulo/Artefacto/Entorno/Respuesta/Medida en los 5; medidas con cifra, unidad y condición de carga (p95≤2s con 200 tareas y 30 concurrentes; ≤5 min y 8/10 participantes; 100% denegado con 403; ≤2 min de restablecimiento; ≤2 componentes y ≤1 día-persona) | Cumple | Además cada escenario declara «Cómo se verifica» (herramienta, carga y umbral): exactamente lo que el corte 1 valora como sobresaliente. |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/calidad/arbol-utilidad.md`: árbol (mermaid) con etiquetas (impacto, riesgo) y tabla de priorización ordenada con justificación por escenario | Cumple | No es lista plana: prioriza y justifica el orden ESC-03, ESC-01, ESC-02, ESC-05, ESC-04. |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/nivel1-contexto.md`: mermaid con flechas etiquetadas y tabla «Leyenda» (color→significado: persona, sistema, externo) | Cumple | Como código (mermaid), con leyenda explícita y flechas con texto. |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md`: filas A-01 y A-06 seguidas al azar → enlaces `calidad/escenarios-calidad.md#esc-02` y `#esc-01`, con anclas `<a id>` presentes en el destino | Cumple | Las 6 filas de la tabla enlazan a su escenario; el destino existe y el ancla resuelve. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clone y ls-remote sin autenticación | Cumple | — |
| Estructura mínima presente | `git ls-tree -r ca7726a`: `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` | Cumple | Las seis rutas presentes. |
| Estado calificado identificable | sin etiquetas; hash `ca7726a3…` + `%cI 2026-08-16T13:01:06-05:00` | Cumple | — |
| Nombres de ADR según la convención | `docs/adr/ADR-001-seleccion-de-stack.md` | No cumple | El nombre no sigue `NNNN-titulo-en-kebab-case.md`: lleva el prefijo «ADR-» y 3 dígitos. El filtro del CONTRATO §4 lo detectaría. |
| ADR aceptados no reescritos | ADR-001 en estado «Propuesta — pendiente de decisión del equipo» | Cumple | No hay ADR aceptado que reescribir. |
| `docs/ia.md` al día para la semana | commits el 2026-08-16 (`da6055f`) y el registro documenta decisiones del equipo que descartan opciones con motivo (D-001 stack acotado, D-002 sin app móvil) más bitácora por uso | Cumple | El formato no tiene la columna literal «rechazado», pero D-001/D-002 registran lo descartado y su motivo, y la política exige revisión explícita de cada uso. |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'` sin salida | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: 3 identidades — `super-gremlin` (noreply, 15 commits), `Ian Novoa` (2), `Julio Cesar Emiliani` (2) | No cumple | `super-gremlin` no se atribuye a nadie; con 3 identidades para 4 integrantes, al menos un integrante (Juan Jose Bustamante More o Daniel Isaac Manjarres Herrera) no tiene commits atribuibles al cierre. |

## Recuento de criterios

9 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Atribución de `super-gremlin` (noreply): el docente deberá confirmar a quién corresponde; de ello depende saber cuál de Juan Jose Bustamante More / Daniel Isaac Manjarres Herrera no aparece en el historial.
- La cuenta `iansx` del listado de `EQUIPOS.md` no firma commits; los commits de Ian Novoa usan `correo omitido` (por confirmar si es la misma persona).

## Hallazgos para la planilla

- Sin entregas tardías posteriores al cierre S2 (`git log --after='2026-08-17T05:00:00Z'` vacío).
- `docs/adr/ADR-001-seleccion-de-stack.md` fuera de la convención de nombres (`NNNN-…`), aunque el ADR en sí está bien formado.
- Repositorio reutilizado: el historial conserva los commits que borraron un proyecto anterior («InnovaActivos» / «Active Asset Management», 09/08). Greps de secretos limpios.
- `CLAUDE.md` en la raíz (configuración de Claude Code): no viola nada, queda anotado por transparencia.
- Positivo para el corte 1: los 5 escenarios declaran «Cómo se verifica» con herramienta, carga y umbral.
- Contribución al cierre S2: super-gremlin 15, Ian Novoa 2, Julio Cesar Emiliani 2.
