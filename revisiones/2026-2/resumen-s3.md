# Resumen de revisión · Semana 3 · 2026-2 (registro local del docente)

Cierre S3: 2026-08-24T05:00:00Z (medianoche del domingo 23, Colombia). Dos pasadas: una antes
del cierre y esta actualización definitiva tras el cierre, sobre el último commit ≤ cierre de
cada repositorio. Regla de nota sugerida: `1 + 4 × (n/9)`, propuesta al docente, NO publicada.

## Notas sugeridas S3 (NO publicadas)

| Equipo | Repo | Hash | n/9 | Nota |
|---|---|---|---|---|
| CampusMarket | `AS_202620_PROYECTO_CAMPUSMARKET` | `4dd857a` | 9 | **5,0** |
| InvenTrack | `AS_202620_InvenTrack` | `dd4ea1c` | 9 | **5,0** |
| LaPlacita | `AS_202620_LaPlacita` | `014751d` | 9 | **5,0** |
| GimnasioUTB | `AS_202620_GimnasioUTB` | `73c1f24` | 8 | 4,6 |
| TRACTAR | `AS_202620_TRACTAR` | `5f923cd` | 7 | 4,1 |
| Clubs UTB | `AS_202620_Clubs_UTB` | `5bf86ea` | 6 | 3,7 |
| ROUTB | `AS_202620_ROUTB` | `1ed002b` | 6 | 3,7 |
| ShareU | `AS_202620_ShareU` | `0833272` | 6 | 3,7 |
| Calificación automática | `AS_202620_Sistema-de-calificacion-automatica` | `dd422fb` | 6 | 3,7 |
| Tienda virtual UTB | `AS_202620_TIENDA-VIRTUAL-UTB` | `f4602a3` | 6 | 3,7 |
| AudioShare | `AS_202620_AudioShare` | `024ae34` | 5 | 3,2 |
| DinamikUTB | `AS_202620_DinamikUTB` | `fe52ab5` | 5 | 3,2 |
| Drift | `AS_202620_Drift` | `0d006bb` | 5 | 3,2 |
| PideUtb | `AS_202620_PideUtb` | `b5f0310` | 5 | 3,2 |
| TAIA | `AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` | `46257a0` | 5 | 3,2 |
| uniTeam | `AS_202620_uniTeam` | `ca44917` | 5 | 3,2 |
| XALD | `AS_202620_XALD` | `dc38992` | 5 | 3,2 |
| mapsutb | `AS_202620_mapsutb` | `ed55eda` | 5 | 3,2 |
| ElMapita | `AS_202620_ElMapita` | `8e30f61` | 4 | 2,8 |
| LostVault | `AS_202620_LostVault` | `1ddb826` | 4 | 2,8 |
| Recobra | `AS_202620_Recobra` | `cb5c579` | 4 | 2,8 |
| Verifacts | `AS_202620_Verifacts` | `8259b75` | 4 | 2,8 |
| EnAgenda | `AS_202620_EnAgenda` | `c38adfb` | 3 | 2,3 |

## Hallazgos transversales S3

- **Entregas tardías (posteriores al cierre, no calificadas)**: Calificación automática (esqueleto
  llegó 2 h tarde, `88294cc` 01:00 y `e976c92` 01:58), Verifacts (15 commits entre 00:06 y 00:58),
  Clubs UTB (`8d69f62` 00:21 con el esqueleto real).
- **CI en verde verificado**: CampusMarket (run 32691690794), InvenTrack (run 32691253620),
  GimnasioUTB (run 32677307908) y Tienda virtual UTB (run 32514183233).
- **ADR 0001 fuera de convención o ausente** quedó resuelto en casi todos tras la primera pasada;
  siguen fuera de convención: XALD (`ADR-006`), TAIA (`0001.md`), uniTeam, EnAgenda (nombre con
  espacio).
- **Enlaces del ADR desde `aspectos.md` y el escenario**: la asignatura pendiente más repetida;
  InvenTrack, CampusMarket y LaPlacita los tienen.
- **Basura versionada**: XALD (`.gradle/`, `build/`, `.idea/`, `local.properties`), TRACTAR
  (`__pycache__/`, `db.sqlite3`), Recobra (`node_modules/`). Señalar en clase antes del corte 1.
- **Contribución**: uniTeam, Verifacts, TRACTAR, LostVault con integrantes sin commits en S3;
  mapsutb con toda la S3 de una sola cuenta.
- **Sin ejecutar código de estudiantes** (regla del kit): los arranques quedaron No verificado
  donde no hay run de CI que lo respalde.
