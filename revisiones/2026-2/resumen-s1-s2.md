# Resumen de revisión · Semanas 1 y 2 · 2026-2

Barrido ejecutado el 2026-08-23 sobre los 23 repositorios de EQUIPOS.md (incluido
`AS_202620_Verifacts`, conocido después del primer barrido).
Método: `git ls-remote` + clon efímero por equipo (`--filter=blob:none --no-checkout` en
directorio temporal, borrado al terminar) — nada quedó almacenado en disco. API de GitHub no
utilizable (403 por límite de peticiones sin token), así que toda la evidencia sale del protocolo
git. Cierres: S1 `2026-08-10T05:00:00Z`, S2 `2026-08-17T05:00:00Z` (medianoche del domingo,
Colombia UTC-5). Estado calificado: último commit anterior a cada cierre.

**Nota sugerida**: propuesta al docente, regla local no publicada (las fichas S1/S2 no tienen
rúbrica en el aula): `1 + 4 × (cumple ÷ total)` sobre la matriz de la ficha (9 criterios). La
matriz transversal del contrato no entra al número. Redondeo a 1 decimal.

## Tabla consolidada

| Equipo | Repo | S1 hash | S1 n/9 | S1 nota | S2 hash | S2 n/9 | S2 nota |
|---|---|---|---|---|---|---|---|
| DinamikUTB | `AS_202620_DinamikUTB` | `769f970` | 7 | 4.1 | `58734e1c` | 9 | **5.0** |
| InvenTrack | `AS_202620_InvenTrack` | `06920209` | 4 | 2.8 | `db90ff2f` | 9 | **5.0** |
| PideUtb | `AS_202620_PideUtb` | `48cfbe3` | 4 | 2.8 | `9b5f214` | 9 | **5.0** |
| uniTeam | `AS_202620_uniTeam` | `4b4c5c0e` | 6 | 3.7 | `ca7726a3` | 9 | **5.0** |
| ElMapita | `AS_202620_ElMapita` | `938d0206` | 5 | 3.2 | `c5d9964c` | 8 | 4.6 |
| EnAgenda | `AS_202620_EnAgenda` | `13f61b10` | 8 | 4.6 | `5b6f7a8e` | 5 | 3.2 |
| LaPlacita | `AS_202620_LaPlacita` | `37f1deb8` | 8 | 4.6 | `fa7e13bc` | 5 | 3.2 |
| Clubs UTB | `AS_202620_Clubs_UTB` | `c92595ed` | 2 | 1.9 | `69cfe68f` | 7 | 4.1 |
| Calificación automática | `AS_202620_Sistema-de-calificacion-automatica` | `4f6f5687` | 7 | 4.1 | `d4302f4b` | 7 | 4.1 |
| CampusMarket | `AS_202620_PROYECTO_CAMPUSMARKET` | `81ef5f1` | 4 | 2.8 | `4f72799` | 7 | 4.1 |
| LostVault | `AS_202620_LostVault` | `560ba895` | 4 | 2.8 | `af94a300` | 7 | 4.1 |
| Tienda virtual UTB | `AS_202620_TIENDA-VIRTUAL-UTB` | `d414ecff` | 7 | 4.1 | `456365b6` | 6 | 3.7 |
| Drift | `AS_202620_Drift` | `b7ec296c` | 4 | 2.8 | `23fb8c29` | 6 | 3.7 |
| TRACTAR | `AS_202620_TRACTAR` | — | no evaluable (primer commit 12-ago) | — | `0a238559` | 6 | 3.7 |
| mapsutb | `AS_202620_mapsutb` | `7e56ad3` | 5 | 3.2 | `1cf1576` | 4 | 2.8 |
| GimnasioUTB | `AS_202620_GimnasioUTB` | `a45615e9` | 4 | 2.8 | `1b30b7a4` | 5 | 3.2 |
| Recobra | `AS_202620_Recobra` | `da5c15d` | 3 | 2.3 | `d2dac73` | 4 | 2.8 |
| AudioShare | `AS_202620_AudioShare` | `1c9ebb0a` | 2 | 1.9 | `d0760fdf` | 4 | 2.8 |
| TAIA | `AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` | `76d4a916` | 6 | 3.7 | `59590c92` | 3 | 2.3 |
| ROUTB | `AS_202620_ROUTB` | `68b0b05d` | 5 | 3.2 | `14e66888` | 2 | 1.9 |
| ShareU | `AS_202620_ShareU` | `8886d4ef` | 4 | 2.8 | `aa0659c1` | 2 | 1.9 |
| XALD | `AS_202620_XALD` | `bf815451` | 5 | 3.2 | `8c37887a` | 1 | 1.4 |
| Verifacts | `AS_202620_Verifacts` | `8ded7cf`* | 4/9 · 2,8 | `8ded7cf`* | 2/9 · 1,9 |

\* Excepción docente: evaluado sobre HEAD actual (primer commit 18-ago, posterior a ambos cierres).

## Hallazgos transversales (lo que se arrastra)

- **Sin secretos en ningún repositorio** (búsqueda completa del contrato §9). Bien.
- **Contribución desbalanceada o incompleta**: LostVault (3 de 4 integrantes sin aparición),
  CampusMarket (23 commits de una sola cuenta), Calificación automática (1 de 4 contribuye),
  Recobra y ShareU (2 de 4), DinamikUTB (35 de 36 commits de una persona en el periodo S2). En
  S1 el acceso solo es verificable por historial (la API de colaboradores exige token).
- **C4 de contexto como imagen no verificable** en ElMapita, GimnasioUTB, LostVault, TAIA y
  TRACTAR: quedó No verificado y hay que abrirlo a mano o en la sustentación.
- **`docs/aspectos.md` sin tabla de 8 columnas ni enlaces** en Clubs UTB, Drift, GimnasioUTB,
  InvenTrack, ROUTB, Tienda virtual UTB y CampusMarket.
- **Escenarios sin las seis partes o sin medida numérica** en LaPlacita, mapsutb, ROUTB, ShareU,
  Recobra, XALD y TAIA; fuera del rango 3–5 en Clubs UTB (6), Recobra (7) y GimnasioUTB (8).
- **Entregas tardías o actividad posterior al cierre**: DinamikUTB (+9 min), EnAgenda (17-ago),
  AudioShare (C4 reelaborado el 22-ago), Drift (reorganización el 22-ago), XALD (archivos el
  23-ago), TRACTAR (S1 sin commits antes del cierre → no evaluable).
- **Identidad cambiante del proyecto**: ShareU cambió de problema entre S1 y S2; uniTeam
  reutilizó un repo con historial ajeno; AudioShare usó `AS_202620_PROYECTO_AudioShare` hasta el
  18-ago.
- **ADR con nombre fuera de convención** en TRACTAR, uniTeam y XALD (prefijo ADR-, sin kebab).
- **`docs/ia.md` vacío o sin la columna de rechazos** en ElMapita, Recobra (1 byte), ROUTB y
  Tienda virtual UTB.
- **Etiqueta mal puesta**: mapsutb tiene `corte-1` sobre un commit de la semana 1 (verificar
  antes del corte).

## Pendientes del docente

- Abrir los 5 C4 que son imagen y decidir esas filas.
- Confirmar correspondencia cuenta↔estudiante contra matrícula (varias quedaron sin atribuir).
- Decidir qué hacer con las entregas tardías (regla del curso: se califica el último commit
  anterior al cierre; lo posterior queda anotado).
- Verifacts declaró `AS_202620_Verifacts` tarde: primer commit 18-ago, después de los
  dos cierres. **Excepción docente**: evaluado en HEAD (S1 4/9 · 2,8; S2 2/9 · 1,9). Hallazgo
  grave en S2: el PDF de entrega declara 5 escenarios en `docs/escenarios-de-calidad.md`, archivo
  que no existe en el repositorio. Solo 1 de 3 integrantes aparece en el historial.

## Archivos

Un directorio por equipo en `revisiones/2026-2/<repositorio>/` (nombrado igual que el
repositorio, p. ej. `AS_202620_DinamikUTB/`) con `semana-01-evidencia-s1.md`,
`semana-02-evidencia-s2.md`, `planilla.md` (hallazgos que se arrastran) y `feedback.md`
(texto listo para publicar en el foro, sin nombres ni notas). Fechas de cierre en
`revisiones/2026-2/cierres.env`.
