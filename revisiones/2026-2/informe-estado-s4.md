# Informe de estado de los proyectos · Semana 4 (S4)

Generado el 2026-08-31 tras la pasada definitiva de S4 (cierre 2026-08-31T05:00:00Z). Fuente: los
23 informes `semana-04-evidencia-s4.md` (matriz de ficha + transversal + overall en HEAD),
`planilla.md` y `resumen-s4.md`. Las notas son **sugeridas** (propuesta al docente, `1 + 4 × n/10`);
la nota final se fija en Moodle.

## Resumen ejecutivo

- **23 de 23 proyectos revisados** en su commit ≤ cierre. **4 equipos "al día"** en el overall
  (ROUTB, LostVault, LaPlacita, uniTeam); el resto avanza con pendientes de semanas anteriores o de S4.
- **Nota sugerida media: 3.05** (máx. ROUTB 5.0; mín. ShareU 1.0). Distribución: 8 equipos ≥ 3.8,
  5 entre 3.0 y 3.4, 10 por debajo de 3.0.
- **CI en verde con run citable**: 10 equipos. **Sin CI configurado**: 6 (AudioShare, PideUtb,
  Recobra, TAIA, mapsutb, Verifacts).
- **Entregas tardías** (commits post-cierre, no calificados): 5 equipos — DinamikUTB, EnAgenda,
  InvenTrack, TRACTAR, Verifacts. En Verifacts y TRACTAR lo tardío es sustancial (corte vertical /
  avances S4 completos fuera de plazo).
- **Contribución incompleta**: ShareU (un solo autor), TRACTAR (3 integrantes sin commits),
  ElMapita (9/11 commits de una cuenta), Verifacts (tercer integrante sin aparición).
- **Incidente de seguridad**: Recobra tiene un `repo_token` de Coveralls expuesto
  (`node_modules/debug/.coveralls.yml`) — **avisar al equipo para rotarlo** (CONTRATO §9).
- **SonarCloud**: ningún equipo lo tiene configurado; es exigencia del contrato §8 desde el inicio
  y sigue abierta para el corte 1.

## Tabla general

| Equipo | S4 (n/10) | Nota sugerida | Overall (HEAD) | CI | Tardíos |
|---|---|---|---|---|---|
| ROUTB | 10/10 | 5.0 | al día | verde (run citable) | — |
| Clubs UTB | 9/10 | 4.6 | con pendientes | verde | — |
| CampusMarket | 9/10 | 4.6 | con pendientes | verde | — |
| EnAgenda | 8/10 | 4.2 | con pendientes | verde | sí (docs, 00:28) |
| Verifacts | 7/10 | 3.8 | con pendientes | sin runs verificables | sí (corte vertical completo, 10:00–11:24) |
| Drift | 7/10 | 3.8 | con pendientes | workflow sin run citado | — |
| DinamikUTB | 7/10 | 3.8 | con pendientes | workflow sin run citado | sí (start.bat, 00:07–00:13) |
| LostVault | 7/10 | 3.8 | al día | verde | — |
| Calificación automática | 6/10 | 3.4 | con pendientes | workflow sin runs | — |
| Tienda virtual UTB | 6/10 | 3.4 | con pendientes | verde | — |
| uniTeam | 6/10 | 3.4 | al día | workflow, run sin citar | — |
| TAIA | 5/10 | 3.0 | con pendientes | sin CI | — |
| mapsutb | 5/10 | 3.0 | con pendientes | sin CI | — |
| AudioShare | 4/10 | 2.6 | con pendientes | sin CI | — |
| ElMapita | 4/10 | 2.6 | con pendientes | run en rojo | — |
| InvenTrack | 4/10 | 2.6 | con pendientes | verde | sí (docs, 00:59–01:23) |
| LaPlacita | 4/10 | 2.6 | al día | verde | — |
| XALD | 4/10 | 2.6 | con pendientes | verde | — |
| GimnasioUTB | 2/10 | 1.8 | con pendientes | verde (solo health) | — |
| Recobra | 2/10 | 1.8 | con pendientes | sin CI | — |
| PideUtb | 1/10 | 1.4 | con pendientes | sin CI | — |
| TRACTAR | 1/10 | 1.4 | con pendientes | verde en cierre, rojo en HEAD | sí (avances S4, 03:35) |
| ShareU | 0/10 | 1.0 | con pendientes | workflow sin runs | — |

## Estado por proyecto

### Destacados (≥ 7/10)

- **ROUTB (10/10, 5.0)** — Referencia del curso: arc42 1–6, 9, 10 y glosario redactados; C4 1–2 en
  Mermaid coherentes con el código; corte vertical completo con prueba en CI verde. Pendiente solo
  SonarCloud y secciones arc42 7, 8, 11 (no exigidas).
- **Clubs UTB (9/10, 4.6)** — Documentación y corte vertical completos con CI verde. Pendiente:
  arranque con un solo comando y SonarCloud.
- **CampusMarket (9/10, 4.6)** — Todo verificado salvo arranque ejecutado (regla del kit).
  Pendiente: SonarCloud, enlazar ADR con commit y definir línea base.
- **EnAgenda (8/10, 4.2)** — Corte vertical y pruebas en verde. Pendiente: C4 nivel 2 coherente con
  el código real (monolito Flask) y SonarCloud. Un commit tardío de documentación (00:28).
- **Verifacts (7/10, 3.8)** — arc42 y C4 excelentes, README completo. El corte vertical al cierre
  solo era `GET /health`; el recorrido completo con persistencia llegó **después del cierre** (no
  calificado). Pendientes: run de CI verificable (URL citada da 404), tabla de aspectos fuera de las
  8 columnas, basura versionada, tercer integrante sin commits.
- **Drift (7/10, 3.8)** — C4 coherentes y corte vertical con las tres capas. Pendiente: prueba del
  recorrido completo, run de CI citable, trazabilidad del ADR y tabla de aspectos.
- **DinamikUTB (7/10, 3.8)** — arc42/C4/corte vertical implementados. Pendiente: ADR-0002 enlazado,
  trazabilidad y run de CI en verde. Commits tardíos menores (start.bat, 00:07–00:13).
- **LostVault (7/10, 3.8)** — Al día: corte vertical, prueba, arranque y CI en verde. Pendiente:
  C4 nivel 2 solo como imagen (no verificable), SonarCloud y cortes de los otros aspectos.

### En camino (5–6/10)

- **Calificación automática (6/10)** — Corte vertical A-01 y ADR sólidos. Pendiente: C4 nivel 2
  completo, verificación de CI (sin runs) y secciones 7–8 del arc42.
- **Tienda virtual UTB (6/10)** — C4, corte vertical, arranque y prueba en verde. Pendiente:
  trazabilidad del ADR, columnas de aspectos, rechazos en ia.md y SonarCloud.
- **uniTeam (6/10)** — Al día en el overall. Pendiente: contenido verificable de arc42 9/10/12,
  URL de run en verde y docs/ia.md.
- **TAIA (5/10)** — Corte vertical con prueba existente pero **sin CI** y sin run en verde.
  Pendiente: trazabilidad del ADR y contenido de varias secciones arc42.
- **mapsutb (5/10)** — Avance sólido en arc42/C4/corte vertical, pero arrastra deudas: alcance de
  RA en documentos viejos, plantilla sin sustituir, ADR editado tras aceptarse, sin CI, carpetas
  `docs/Arc42` y `docs/C4` con mayúsculas, sin etiqueta `corte-1`.

### En riesgo (< 5/10)

- **AudioShare (4/10)** — arc42 y C4 presentes, pero la sección 9 no enlaza ADR reales, el C4 nivel
  2 no corresponde al código, el corte vertical no tiene persistencia y **no hay CI**.
- **ElMapita (4/10)** — Entrega a tiempo, pero el **run de CI está en rojo**, las pruebas del
  recorrido están pendientes y la autoría está concentrada (9/11 commits de una cuenta).
- **InvenTrack (4/10)** — Al cierre faltaban arc42 4–6, 9 y 12 (los completó después del cierre).
  CI verde. Pendiente: SonarCloud y celda de Pruebas de aspectos.
- **LaPlacita (4/10)** — Al día y con CI verde, pero la ficha puntúa bajo: contenedores C4 sin
  código, ia.md sin rechazos y trazabilidad de ADR pendientes.
- **XALD (4/10)** — C4 completo y CI Android en verde. Pendiente: verificar contenido arc42,
  confirmar que el corte vertical atraviesa persistencia, contenedor Backend sin código y ADR sin
  trazabilidad.
- **GimnasioUTB (2/10)** — CI en verde pero **sin corte vertical implementado** (solo health);
  trazabilidades apuntan a artefactos inexistentes; README y arc42 con huecos.
- **Recobra (2/10)** — Documentación presente pero **no existe el código del corte vertical** (sin
  src/ ni tests/); C4 dibuja contenedores sin implementación; `node_modules` versionado y **token
  de Coveralls expuesto (rotar)**.
- **PideUtb (1/10)** — Sin C4, sin glosario verificable, sin CI; tabla de aspectos fuera de esquema;
  `.venv-1` versionado.
- **TRACTAR (1/10)** — Al cierre S4 incompleta; los avances llegaron **después del cierre**
  (03:35). El CI de HEAD está **en rojo**, 3 integrantes sin commits y sin SonarCloud.
- **ShareU (0/10)** — Estructura presente pero casi todo sin contenido verificable; **un solo
  autor** en el historial; runs_ci vacío.

## Hallazgos transversales

1. **SonarCloud ausente en los 23 equipos** — exigencia del contrato §8; bloquea la fila de
   pipeline/análisis estático para todos en el corte 1.
2. **Patrón de entrega tardía** — 5 equipos con commits post-cierre; en TRACTAR y Verifacts lo
   tardío era la parte central de la entrega. Recordar en clase la regla: el repositorio se califica
   en el commit ≤ cierre.
3. **Contribución** — 4 equipos con integrantes sin commits (ShareU, TRACTAR, Verifacts, ElMapita
   concentrado). Es criterio calificado en el corte 1 y el final.
4. **CI** — 10 equipos con run en verde citable; 6 sin CI configurado; 4 con workflow pero sin run
   citable. Un run en verde cierra dos filas de la ficha y una del contrato.
5. **Basura versionada** — `node_modules` (Recobra), `.venv-1` (PideUtb), `__pycache__`/`.pyc` y
   PDFs (Verifacts), carpetas con mayúsculas (mapsutb). Limpiar antes de etiquetar `corte-1`.
6. **Seguridad** — Recobra: `repo_token` de Coveralls expuesto en `node_modules/debug/.coveralls.yml`.
   Rotar la credencial y purgarla del historial (es público).

## Próximos hitos

- **Semana 5 (corte 1)**: cierre domingo 2026-09-06 a medianoche COT. Se califica el commit
  **etiquetado `corte-1`** (ficha `semana-05-corte1.md`): etiquetar a tiempo es condición de la fila
  de versionado. Se mirará: trazabilidad completa (aspectos→requisito→C4→ADR→commit→prueba→evidencia),
  medición de línea base y los arrastres de S1–S4.
- **Semana 6 (S6)**: contextos delimitados y propiedad de datos (cierre 2026-09-13).
- **Pasadas automáticas**: miércoles y viernes 06:00 COT (flash, delta) y lunes 06:00 COT
  (pro, completa) con notas preliminares en las tempranas.

## Nota de proceso

La matriz transversal de algunos informes S4 nombró los criterios del contrato con etiquetas
propias en vez de los 8 nombres canónicos; el prompt del pipeline ya se ajustó para exigir los 8
criterios exactos en las próximas semanas. No afecta al recuento de la ficha (que es el que
determina la nota sugerida).
