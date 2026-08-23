# Evidencia S2 · AudioShare

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` (en el cierre S2 el nombre era `AS_202620_PROYECTO_AudioShare`; renombrado el 2026-08-18) |
| Estado revisado | `d0760fdf51d5c26f3c797a0a29fa417740749f23` · 2026-08-16T23:31:32-05:00 · «Update arbol_utilidad.md» |
| Cierre | 2026-08-17T05:00:00Z (domingo 16 de agosto medianoche, UTC-5) |
| Comandos principales ejecutados | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only d0760fdf`; `git show d0760fdf:docs/...`; `git grep -nIE '<[a-z ]+>|TODO|lorem ipsum' d0760fdf -- docs/arc42/src/`; `git grep` de secretos; `git shortlog -sne d0760fdf` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/src/01_introduction_and_goals.adoc` | No cumple | Declara objetivos de calidad (rendimiento, disponibilidad, tolerancia a fallos, escalabilidad), pero no dice a quién le importa cada uno: no hay interesado ni sección de stakeholders. |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/src/02_architecture_constraints.adoc` y `docs/Restricciones_justificadas.md` (R-01 a R-05) | No cumple | Justificadas sí (cada R-n trae justificación y consecuencia arquitectónica); clasificadas no: ninguna etiqueta técnica/organizativa/legal, y no hay restricciones legales. |
| Restricciones separadas de los requisitos | requisitos en 01, restricciones en 02 + archivo propio | Cumple | Separación física correcta. Ojo: R-05 («una sala maneje varios receptores») es en realidad un requisito funcional presentado como restricción, y R-03 («transmitir audio en tiempo real») roza serlo. Anotado. |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42/src/03_context_and_scope.adoc` frente a `docs/c4/context.mmd` | No cumple | La sección 3 identifica emisor, receptor y moderador, y lista la red Wi-Fi como elemento externo; el C4 de contexto solo tiene emisor y receptor y no modela la red Wi-Fi. Actores y sistemas no coinciden. |
| Entre 3 y 5 escenarios de calidad redactados | `docs/escenarios_calidad.md` (EC-01 a EC-04) | Cumple | 4 escenarios numerados. Están fuera de `docs/arc42/` (no existe `10*`): desviación de estructura, el artefacto se evalúa donde está. |
| Cada escenario con sus seis partes y medida numérica | `docs/escenarios_calidad.md:10-31` (EC-01 como cita) | No cumple | Los 4 tienen estímulo, respuesta y medida numérica con unidad (100 ms, 200 ms, 100 ms, 3 s). Ninguno declara fuente, artefacto ni entorno explícitos; la condición de carga es débil («uno o varios receptores», sin cifra de dispositivos salvo EC-04). |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arbol_utilidad.md` | Cumple | Prioriza por niveles (rendimiento y disponibilidad: alta; usabilidad y seguridad: media) justificando por impacto en el usuario; el riesgo está implícito, no explícito. Los 4 escenarios redactados están referenciados (coinciden). |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/context.mmd` (código Mermaid) + `docs/c4/context.png` (PNG 5655×3280 válido) | No cumple | Está como código y como imagen. Flechas etiquetadas sí («Inicia una sesión y comparte audio», «Se une a una sesión…»). Sin leyenda, sin sistemas externos (red Wi-Fi ausente) y sin moderador. El PNG se verificó como archivo válido; su contenido visual se evaluó por la fuente Mermaid. |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` → enlaces a EC-01…EC-04 | Cumple | La fila A-01 enlaza los 4 escenarios con anclas (`escenarios_calidad.md#ec-01-…`). Seguidos dos al azar (EC-01 y EC-04): ambos llegan. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt` OK; clon sin autenticación OK | No cumple | Público sí. Nombre en el cierre S2 seguía siendo `AS_202620_PROYECTO_AudioShare`; el renombrado a `AS_202620_AudioShare` (`31bcc18`) es del 2026-08-18, posterior al cierre. |
| Estructura mínima presente | `git ls-tree -r --name-only d0760fdf` | No cumple | 5 de 6: `README.md` ✓, `docs/arc42/` ✓ (plantilla `.adoc` + `src/01-03`), `docs/c4/` ✓, `docs/aspectos.md` ✓, `docs/ia.md` ✓. Falta `docs/adr/` (sin `.gitkeep`, no versionado). |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` | Cumple | Hash `d0760fdf…` con `%cI` 2026-08-16T23:31:32-05:00; último commit anterior al cierre. |
| Nombres de ADR según la convención | sin `docs/adr/` | Cumple (vacuo) | Sin ADR todavía: nada que incumpla la convención. |
| ADR aceptados no reescritos | sin ADR | Cumple (vacuo) | Ídem. |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia.md` | Cumple | Actualizado dentro del periodo (`40dd80b`, 2026-08-16) con tabla de usos de S1 y S2. Sigue sin la columna de «qué se rechazó y por qué» (CONTRATO §6); anotar para las próximas semanas. |
| Sin credenciales en el repositorio ni en el historial | `git grep` (regex §9), `.env`, `git log -S'BEGIN PRIVATE KEY'` | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | `git shortlog -sne d0760fdf` | Cumple | 4 identidades: `cardonavincent26-design` (15), Yeiver Andrés Vergel Pérez (14), Elian Daniel Perea Vanegas (13), Santiago Adolfo Camacho Hernández (12). `cardonavincent26-design` se atribuye a Vincent Cardona Castro por el handle (cardona/vincent), sin confirmación oficial contra matrícula. |

## Recuento de criterios

- Ficha: **4 de 9** criterios Cumple.

## No verificado / pendientes

- Contenido visual del PNG del C4 (herramienta de revisión sin soporte de imágenes; se evaluó por el `.mmd`).
- Correspondencia oficial de `cardonavincent26-design` con Vincent Cardona Castro (confirmar con matrícula).

## Hallazgos para la planilla

- Entregas tardías (posteriores al cierre S2): `31bcc18` 2026-08-18 (renombrado del repo); `56c6108`, `33a6ee8`, `3575e85`, `8ca9e55` 2026-08-22 (reelaboración del C4 de contexto).
- Sección 10 y árbol de utilidad fuera de `docs/arc42/` (`docs/escenarios_calidad.md`, `docs/arbol_utilidad.md`); arc42 en AsciiDoc, no en Markdown.
- Escenarios sin fuente, artefacto ni entorno; condición de carga sin definir.
- Restricciones sin clasificación por tipo; R-05 (y en parte R-03) son requisitos funcionales, no restricciones.
- C4 de contexto sin leyenda y sin la red Wi-Fi ni el moderador (incoherente con la sección 3).
- `docs/ia.md` sin entradas de lo rechazado y su motivo.
- De los 4 escenarios, los 4 tienen medida numérica; ninguno declara todavía cómo se medirá (herramienta, carga, umbral): pendiente para el primer corte.
