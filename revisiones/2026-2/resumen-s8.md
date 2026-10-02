# Resumen de revisión · Semana 8 · S8 (definitiva)

Pasada definitiva de los 23 equipos sobre el último commit ≤ cierre (`2026-09-28T05:00:00Z`).
Sustituye la consolidación preliminar, que había calificado sobre revisiones del 20 al 23 de
septiembre y que en varios equipos no llegó a leer el contenido de los archivos.

**Filas de despliegue diferidas.** Por decisión del docente, la URL del sistema desplegado no se
califica en esta pasada: se entrega por Moodle y no está disponible. Las filas «URL del sistema
accesible desde fuera de la red de la universidad» y «Health check consultable» quedan pendientes
en los 23 equipos, con el motivo escrito, y la nota se calcula sobre los **10 criterios
graduables**. Es una **propuesta provisional**: cuando llegue la lista de URL se completan las dos
filas y se recalcula. En las observaciones de esas filas quedó registrado lo que el repositorio
prueba (URL declarada y ruta de health check), para que esa segunda pasada sea corta.

| Equipo | Repo | Hash | n/10 | Nota provisional |
|---|---|---|---|---|
| AudioShare | `AS_202620_AudioShare` | `e4789d8` | 9/10 | 4.6 |
| Clubs UTB | `AS_202620_Clubs_UTB` | `652f78b` | 5/10 | 3.0 |
| DinamikUTB | `AS_202620_DinamikUTB` | `287c65d` | 10/10 | 5.0 |
| Drift | `AS_202620_Drift` | `74709aa` | 10/10 | 5.0 |
| ElMapita | `AS_202620_ElMapita` | `e5c3ac6` | 9/10 | 4.6 |
| EnAgenda | `AS_202620_EnAgenda` | `2c7d77a` | 5/10 | 3.0 |
| GimnasioUTB | `AS_202620_GimnasioUTB` | `a71bc75` | 3/10 | 2.2 |
| InvenTrack | `AS_202620_InvenTrack` | `48aeecf` | 10/10 | 5.0 |
| LaPlacita | `AS_202620_LaPlacita` | `b03a797` | 10/10 | 5.0 |
| LostVault | `AS_202620_LostVault` | `4a9ecc9` | 10/10 | 5.0 |
| CampusMarket | `AS_202620_PROYECTO_CAMPUSMARKET` | `784d788` | 10/10 | 5.0 |
| PideUtb | `AS_202620_PideUtb` | `a94bf4e` | 9/10 | 4.6 |
| ROUTB | `AS_202620_ROUTB` | `eae667e` | 10/10 | 5.0 |
| Recobra | `AS_202620_Recobra` | `5c7f77b` | 10/10 | 5.0 |
| ShareU | `AS_202620_ShareU` | `332f67f` | 7/10 | 3.8 |
| Calificación automática | `AS_202620_Sistema-de-calificacion-automatica` | `1f8f76d` | 10/10 | 5.0 |
| TAIA | `AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` | `4b07242` | 10/10 | 5.0 |
| Tienda virtual UTB | `AS_202620_TIENDA-VIRTUAL-UTB` | `858e78f` | 10/10 | 5.0 |
| TRACTAR | `AS_202620_UTB_TRACKER` | `ae526db` | 1/10 | 1.4 |
| Verifacts | `AS_202620_Verifacts` | `d2d7b5c` | 10/10 | 5.0 |
| XALD | `AS_202620_XALD` | `f90f28d` | 10/10 | 5.0 |
| mapsutb | `AS_202620_mapsutb` | `8cfe458` | 10/10 | 5.0 |
| uniTeam | `AS_202620_uniTeam` | `0f3da0f` | 9/10 | 4.6 |

Promedio del curso: **4.4** (197 de 230 criterios graduables). La consolidación preliminar daba
**1.8** de promedio: calificaba revisiones anteriores al cierre y, en varios equipos, no leía el
contenido de los archivos.

## Hallazgos transversales (no entran en la nota)

| Fila de §11 | Equipos que no cumplen |
|---|---|
| ADR aceptados no reescritos | 20 de 23 |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | 21 de 23 (1 queda en No verificado) |
| `docs/ia.md` al día para la semana | 5 |
| Contribución de todos los integrantes | 4 (1 queda en No verificado) |
| Nombres de ADR según la convención | 4 |
| Estructura mínima presente | 1 |

Dos patrones explican casi todo el resto: los ADR aceptados se siguen editando después de
aceptarse sin declarar reemplazo, y SonarCloud no queda ligado al pipeline con una URL pública de
Quality Gate. Ninguno de los dos entra en la fórmula de la nota, que corre sobre la matriz de la
ficha.

## Pendiente

- Completar las dos filas de despliegue con la lista de URL de Moodle y recalcular las notas.
- El taller de despliegue (`arqsw:taller-docker`) no se evaluó: es otra entrega y no lleva nota en
  el calendario.
