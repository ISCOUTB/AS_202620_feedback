# Resumen de revisión · Semana 7 · S7 (definitiva)

Consolidación local de los 23 informes definitivos auditados. Sin publicación remota.

**Corrección posterior.** Ocho equipos fueron re-leídos en el repositorio, en el hash calificado,
porque la pasada automática había dejado en «No verificado» 37 filas cuyo artefacto sí estaba
presente y era legible con `git show`, lo que `CONTRATO.md` §13 prohíbe. De esas 37 filas, 31
pasaron a Cumple y 6 a No cumple. Simultáneamente se auditó el defecto espejo: nueve filas
publicadas como «Cumple» cuya observación admitía no haber leído el artefacto. Se leyeron y sus
observaciones y evidencias quedaron respaldadas con `ruta:línea`; ninguna cambió de estado.

Ninguna revisión calificada cambió: los 23 hashes son la última revisión ≤ cierre
(`2026-09-21T05:00:00Z`), verificado con `git rev-list -1 --before` y con la API pública.

Nota sugerida = 1 + 4 × (n/m) sobre la matriz de la ficha, **propuesta al docente**; la nota final se fija en Moodle.

| Equipo | Repo | Hash | n/m | Nota sugerida |
|---|---|---|---|---|
| AudioShare | `AS_202620_AudioShare` | `0ada095` | 9/10 | 4.6 |
| Clubs UTB | `AS_202620_Clubs_UTB` | `dc211b8` | 8/10 | 4.2 |
| DinamikUTB | `AS_202620_DinamikUTB` | `5e6fa73` | 10/10 | 5.0 |
| Drift | `AS_202620_Drift` | `9334a03` | 10/10 | 5.0 |
| ElMapita | `AS_202620_ElMapita` | `afae3be` | 8/10 | 4.2 |
| EnAgenda | `AS_202620_EnAgenda` | `849ee8c` | 4/10 | 2.6 |
| GimnasioUTB | `AS_202620_GimnasioUTB` | `0e3aeb5` | 8/10 | 4.2 |
| InvenTrack | `AS_202620_InvenTrack` | `f10fd01` | 9/10 | 4.6 |
| LaPlacita | `AS_202620_LaPlacita` | `8c2e1bc` | 10/10 | 5.0 |
| LostVault | `AS_202620_LostVault` | `7bf515f` | 7/10 | 3.8 |
| CampusMarket | `AS_202620_PROYECTO_CAMPUSMARKET` | `c53ee32` | 10/10 | 5.0 |
| PideUtb | `AS_202620_PideUtb` | `3d78106` | 10/10 | 5.0 |
| ROUTB | `AS_202620_ROUTB` | `fe266aa` | 9/10 | 4.6 |
| Recobra | `AS_202620_Recobra` | `8f25313` | 10/10 | 5.0 |
| ShareU | `AS_202620_ShareU` | `29184bc` | 6/10 | 3.4 |
| Calificación automática | `AS_202620_Sistema-de-calificacion-automatica` | `2269ca5` | 10/10 | 5.0 |
| TAIA | `AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` | `0a12f0c` | 10/10 | 5.0 |
| Tienda virtual UTB | `AS_202620_TIENDA-VIRTUAL-UTB` | `69aa82d` | 8/10 | 4.2 |
| TRACTAR | `AS_202620_UTB_TRACKER` | `7cfb872` | 2/10 | 1.8 |
| Verifacts | `AS_202620_Verifacts` | `635f9b7` | 10/10 | 5.0 |
| XALD | `AS_202620_XALD` | `62a0d15` | 9/10 | 4.6 |
| mapsutb | `AS_202620_mapsutb` | `5e2fdd5` | 10/10 | 5.0 |
| uniTeam | `AS_202620_uniTeam` | `1ea4aba` | 9/10 | 4.6 |

## Cambios de la corrección

| Equipo | Antes | Ahora | Pasaron a Cumple | Quedaron en No cumple |
|---|---|---|---|---|
| AudioShare | 5/10 · 3.0 | 9/10 · 4.6 | rutas y esquemas, correspondencia, versión e historial, pipeline, registro de IA, análisis estático | — |
| Clubs UTB | 6/10 · 3.4 | 8/10 · 4.2 | correspondencia, pipeline, registro de IA | C4 nivel 2, tabla de aspectos |
| DinamikUTB | 7/10 · 3.8 | 10/10 · 5.0 | versión e historial, arc42 §6, C4 nivel 2 | tabla de aspectos |
| Drift | 5/10 · 3.0 | 10/10 · 5.0 | correspondencia, pipeline, fallo controlado, arc42 §6, C4 nivel 2, tabla de aspectos | — |
| ElMapita | 4/10 · 2.6 | 8/10 · 4.2 | rutas y esquemas, pipeline, arc42 §6, C4 nivel 2, tabla de aspectos | análisis estático |
| TAIA | 6/10 · 3.4 | 10/10 · 5.0 | versión e historial, pipeline, fallo controlado, C4 nivel 2, tabla de aspectos | análisis estático |
| Verifacts | 8/10 · 4.2 | 10/10 · 5.0 | versión e historial, pipeline, análisis estático | — |
| LostVault | 7/10 · 3.8 | 7/10 · 3.8 | — | C4 nivel 2 |

Promedio del curso: 4.0 → 4.4.

Las filas «No cumple» que ya estaban publicadas no se tocaron: se sostienen con evidencia (TRACTAR
sin contrato alguno; ElMapita con deriva de rutas `/api/api/v1`; EnAgenda con el ADR de integración
posterior al cierre; AudioShare con marcadores de conflicto de fusión en el commit calificado).

## Interpretación de criterio fijada

«C4 nivel 2 con protocolo y formato en cada flecha»: las flechas **persona→contenedor** se toleran
(describen interacción humana). Se exige protocolo y formato en toda flecha que cruce un límite
tecnológico. Aplicado de forma uniforme; es lo que separa el Cumple de DinamikUTB (`HTTP/JSON`,
`SQL`) del No cumple de Clubs_UTB (`Valida tokens de sesión`, sin protocolo ni formato) y de
LostVault (diagrama en imagen, flechas de cruce sin formato).

## Correcciones de cierre (aplicadas)

- **Guarda de semana cerrada reparada.** `informes_definitivos()` dejó de depender del texto de la
  cabecera: cuenta los informes publicados y el modo definitivo lo decide `estado-s7.json`. Un pase
  definitivo ya no puede reprocesar S7 y pisar estas correcciones.
- **Matriz transversal de 9 filas.** El prompt del pipeline pedía «exactamente 8» y `CONTRATO.md`
  §11 tiene 9, por eso los informes omitían filas. Se corrigieron el prompt y el conteo, y se
  completaron las filas faltantes en Verifacts, TAIA, ElMapita, DinamikUTB y TRACTAR.
- **Tres ADR aceptados editados sin reemplazo declarado** (fila §11 «ADR aceptados no reescritos» →
  No cumple): Verifacts ADR-0001 (`73beb28`, 2026-09-07), TAIA ADR-0001 (`42c5b03`, 2026-09-06) y
  ElMapita ADR-0001 (`07b36f4`, 2026-08-30). En DinamikUTB el mismo hallazgo afecta a cuatro ADR.
- **Contribución incompleta** (fila §11 → No cumple): Verifacts (2 de 3 integrantes), ElMapita (2 de
  3 identificables) y TRACTAR (1 de 4).
- **Volcado del pipeline con presupuesto explícito.** Los documentos que deciden filas entran
  primero y con cupo propio; lo que queda afuera se publica en `documentos_omitidos` y el prompt
  prohíbe escribir «no se aportó» por un recorte del volcado.
- **TRACTAR**: el repositorio fue renombrado a `ISCOUTB/AS_202620_UTB_TRACKER`
  (`AS_202620_TRACTAR` redirige con 301); el cargo de identidad anterior era autocontradictorio y
  quedó corregido. Se registra además el commit `9cf1ac9`, catorce minutos posterior al cierre.
- **Higiene**: se quitaron nombres propios y correos de informes y feedback donde aparecían.

Ninguna de estas correcciones cambia una nota: la matriz transversal no entra en la fórmula.

## Pendiente

- Repetir el barrido de filas «Cumple» sin respaldo y de volcado recortado en S8 y en las semanas
  siguientes: el mismo prompt las genera.
- Actualizar el nombre de TRACTAR en el mapeo del kit si se quiere evitar la redirección.
