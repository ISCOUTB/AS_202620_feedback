# Resumen definitivo · Semana 5 · Primer corte

> Evaluación definitiva de los 23 equipos, realizada el 2026-09-07 después del cierre
> (`2026-09-07T05:00:00Z`), sobre la etiqueta `corte-1` o, cuando faltaba, sobre el último commit
> admisible antes del cierre. Reemplaza la revisión preliminar del 2026-09-03: aquella se hizo antes
> del cierre y casi ningún equipo tenía todavía la etiqueta.

Se evaluó la respuesta al reto de S5 (restricción nueva, diagnóstico, ADR, cambio, medición,
trazabilidad). Las evidencias S1-S4 se usaron como línea base y no se recalificaron. La sección
`overall` de cada informe revisa el estado global en `HEAD`. Donde el equipo dejó `correcciones.md`
(o un nombre equivalente) en su repositorio contradiciendo la revisión preliminar, se adjudicó cada
punto contra la evidencia real — ver columna «Correcciones».

| Equipo | Repositorio | Estado calificado | Matriz | Subtotal técnico | Hallazgo principal | Correcciones |
|---|---|---|---:|---:|---|---|
| AudioShare | `AS_202620_AudioShare` | `corte-1` → `cb65d131` | 1/12 | 0,00/4,00 | Única etiqueta correcta del lote, pero cero evidencia de respuesta a una restricción asignada. | sin correcciones.md |
| Clubs UTB | `AS_202620_Clubs_UTB` | sin etiqueta → `4ede977c` | 0/12 | 0,00/4,00 | Sin reto identificable; el ADR-0001 ya aceptado se editó de nuevo sin reemplazo. | sin correcciones.md |
| DinamikUTB | `AS_202620_DinamikUTB` | sin etiqueta → `f89564fd` | 1/12 | 0,00/4,00 | Formalizó una decisión de backlog previa (ADR-0003, motor de BD) en vez de responder al reto. | 0 aceptadas / 5 rechazadas |
| Drift | `AS_202620_Drift` | sin etiqueta → `d110d6d0` | 2/12 | 0,00/4,00 | La consolidación de línea base más completa del lote; el propio equipo admite en su documento que etiqueta, ADR del reto y medición siguen pendientes. | 10 aceptadas / 3 rechazadas |
| ElMapita | `AS_202620_ElMapita` | sin etiqueta → `4806374a` | 0/12 | 0,00/4,00 | Cero actividad en la semana; confundieron un mensaje de commit "corte-1" con una etiqueta git; CI en rojo. | sin correcciones.md |
| EnAgenda | `AS_202620_EnAgenda` | `corte-1` → `31773ad` | 1/12 | 0,60/4,00 | El equipo admite que no formuló reto ni restricción nueva; solo ajustó C4/aspectos de S4. | sin disputa (0/0) |
| GimnasioUTB | `AS_202620_GimnasioUTB` | sin etiqueta → `9b9f7c8` | 2/12 | 0,60/4,00 | Sin respuesta al reto; ADR-0001 ya aceptado fue editado en contenido en 4 commits posteriores. | sin disputa (0/0) |
| InvenTrack | `AS_202620_InvenTrack` | `corte-1` → `2988b03` | 3/12 | 2,00/4,00 | **Hallazgo crítico:** el ADR y el reporte de medición describen un lock de concurrencia y cifras de latencia que no existen en el código (`app/` sin cambios desde S4). | sin correcciones.md |
| LaPlacita | `AS_202620_LaPlacita` | `corte-1` → `50b92f8` | 10/12 | 3,80/4,00 | Única respuesta genuina y verificable de punta a punta al reto (aislamiento por tienda): línea base medida, ADR sobresaliente, código real, medición reproducible. | 7 aceptadas / 0 rechazadas |
| LostVault | `AS_202620_LostVault` | `corte-1` → `952af8f` (sin cambios) | 1/12 | 0,00/4,00 | Cero commits nuevos desde el 30-ago; la etiqueta no se movió. | sin correcciones.md |
| mapsutb | `AS_202620_mapsutb` | `corte-1` → `7e56ad3` (apunta a S1) | 0/12 | 0,00/4,00 | La etiqueta sigue apuntando al estado de evidencia S1; HEAD avanzó pero no lo refleja `docs/aspectos.md`. | sin correcciones.md |
| PideUtb | `AS_202620_PideUtb` | sin etiqueta → `1636f20` | 0/12 | 0,00/4,00 | Nunca crearon `corte-1`; el trabajo del lunes 7/09 es posterior al cierre y no responde al reto. | sin correcciones.md |
| CampusMarket | `AS_202620_PROYECTO_CAMPUSMARKET` | `corte-1` → `8044215` | 9/12 | 4,00/4,00 | Reto completo y verificado de punta a punta, con CI en verde en el propio commit etiquetado. | 3 aceptadas / 0 rechazadas |
| Recobra | `AS_202620_Recobra` | `corte-1` → `f7c1a6c` (posterior al cierre, ~10h) | 10/12 | 4,00/4,00 | Trabajo técnico sobresaliente, pero la etiqueta se movió después del cierre; un token de Coveralls sigue sin rotar en el historial público. | sin correcciones.md |
| ROUTB | `AS_202620_ROUTB` | `corte-1` → `493efdb` | 10/12 | 3,20/4,00 | Reto de concurrencia de cupos bien resuelto y medido; SonarCloud consistentemente en rojo. | sin correcciones.md |
| ShareU | `AS_202620_ShareU` | `corte-1` → `a5d08c1` (posterior al cierre, +7h) | 0/12 | 0,00/4,00 | Etiqueta tardía sobre un árbol triplicado por cargas ZIP; sin ADR, diagnóstico, medición ni un solo run de CI en la vida del repo. | sin correcciones.md |
| Calificación automática | `AS_202620_Sistema-de-calificacion-automatica` | `corte-1` → `201acac` | 10/12 | 3,80/4,00 | Reto resuelto por completo en un commit voluminoso: diagnóstico medido, ADR con 4 alternativas, pruebas y CI verde antes del cierre. | 8 aceptadas / 0 rechazadas |
| TAIA | `AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` | sin etiqueta → `a3f4d82` | 0/12 | 0,00/4,00 | La última noche se dedicó a arc42/CI y a justificar notas de S1-S4, no al reto; el ADR-0001 aceptado se editó en vez de reemplazarse. | `correcciones.md` versa solo sobre S1-S4 (fuera de alcance del corte 1) |
| Tienda virtual UTB | `AS_202620_TIENDA-VIRTUAL-UTB` | sin etiqueta → `20ab43f` | 0/12 | 0,00/4,00 | El único commit rotulado "Corte 1" solo agrega dos líneas al README. | sin correcciones.md |
| TRACTAR | `AS_202620_TRACTAR` | sin etiqueta → `7cfb872` | 0/12 | 0,00/4,00 | Sin respuesta identificable; autoría concentrada en un solo integrante. Repo renombrado a `AS_202620_UTB_TRACKER` (redirección activa). | sin correcciones.md |
| uniTeam | `AS_202620_uniTeam` | sin etiqueta → `dc14298` | 6/12 | 2,80/4,00 | ADR de autenticación OIDC sólido, que se infiere como respuesta al reto, pero sin línea base cuantificada ni medición posterior. | sin correcciones.md |
| Verifacts | `AS_202620_Verifacts` | **repositorio no accesible (404)** | — | — | **Hallazgo crítico:** el repositorio desapareció de la organización `ISCOUTB` entre la revisión preliminar (2026-09-02) y el cierre. No se pudo evaluar nada. | sin correcciones.md |
| XALD | `AS_202620_XALD` | `corte-1` → `2861d8b` (2026-09-06, antes del cierre) | 3/12 | 0,60/4,00 | Actividad intensa la noche previa al cierre; sin restricción diagnosticada ni medición. | 3 aceptadas / 1 rechazada / 1 parcial / 1 no verificable |

## Lectura consolidada

- **21 de 23 repositorios** se revisaron manualmente en modo de solo lectura sobre el estado
  correcto (etiqueta o fallback de cierre); `AS_202620_Verifacts` no fue evaluable porque su
  repositorio ya no existe en la organización.
- **Solo 4 equipos** (CampusMarket, Recobra, ROUTB, Calificación automática) entregaron una respuesta
  técnica completa y verificable al reto, con subtotal ≥ 3,20/4,00. LaPlacita se suma con 3,80/4,00.
- **Dos etiquetas se movieron después del cierre** (Recobra, ShareU) y **dos apuntan a un estado
  equivocado** (mapsutb sigue en S1; LostVault no se movió desde S4). El resto de equipos sin
  respuesta completa tampoco creó la etiqueta.
- **Dos hallazgos críticos** requieren atención antes de aplicar cualquier nota: InvenTrack describe
  en su documentación una implementación que no está en el código, y el repositorio de Verifacts
  desapareció de la organización.
- **Un secreto sin rotar** en el historial público de Recobra (token de Coveralls) — se avisa al
  equipo aparte de la nota, porque quitarlo del último commit no lo quita del historial.
- Se adjudicaron correcciones de siete equipos: la mayoría de las contradicciones sobre criterios de
  S1-S4 o sobre lo ya documentado se aceptaron tras verificar evidencia; las que pedían dar por
  cumplido lo que el propio equipo reconocía pendiente (etiqueta, ADR del reto, medición) se
  rechazaron.
- No se calcula una nota total sobre 5,00 antes de la sustentación: el corte tiene rúbrica propia y
  el quinto criterio (sustentación) lo fija el docente en la sesión.
