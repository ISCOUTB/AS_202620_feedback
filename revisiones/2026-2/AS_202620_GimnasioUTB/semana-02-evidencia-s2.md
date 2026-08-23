# Evidencia S2 · GimnasioUTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `1b30b7a4d81e28352260587765e8ec0a9ef44386` · 2026-08-16T21:04:17-05:00 (commit vigente al cierre S2; es también HEAD) |
| Cierre S2 | 2026-08-17T05:00:00Z |
| Comandos principales | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only 1b30b7a4`; `git show 1b30b7a4:"docs/Evidencia S2 gimnasio_utb.md"`; `git grep -nIE '<plantilla>' 1b30b7a4`; `git grep -nIE '<secretos>' HEAD`; `git log -S'<patrón>'` |

Nota de método: todo el contenido arc42 de la semana está en un único archivo, `docs/Evidencia S2 gimnasio_utb.md`, y el C4 es una imagen (`docs/C4.jpg`). Desviación de estructura (no ausencia): el artefacto se evalúa donde está, y la desviación se registra en la fila de estructura de la matriz transversal.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/Evidencia S2 gimnasio_utb.md:16-60` — visión de requisitos (1.1), objetivos de calidad con motivación (1.2), trade-off (1.3), stakeholders con rol, preocupaciones y expectativas (1.4) | Cumple | Los objetivos (1.2) son de calidad y van con motivación; los interesados están en 1.4. El objetivo de negocio queda implícito en 1.1 y el mapeo objetivo→interesado no es explícito — se puede afinar |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/Evidencia S2 gimnasio_utb.md:62-85` — 2.1 organizacionales (OC1–OC6) y 2.2 técnicas (TC1–TC5), cada una con «Justificación / impacto en la arquitectura» | No cumple | Clasificación organizacional/técnica presente y justificación de impacto en todas; falta la categoría legal y el origen explícito de varias restricciones |
| Restricciones separadas de los requisitos | Requisitos en 1.1 (líneas 18-26) y 3.1 (89-97); restricciones con IDs OC/TC en la sección 2 | Cumple | Separación estructural clara. Observación: TC5 («registro por cámara/QR») está redactada como requisito funcional más que como restricción |
| arc42 sección 3 con actores y sistemas externos | `docs/Evidencia S2 gimnasio_utb.md:87-114` — actores (estudiante, encargado, Bienestar), canales técnicos con FCM como sistema externo | Cumple | Coherente con la descripción textual del C4 (mismos actores y FCM). La imagen en sí no se pudo inspeccionar (ver fila del C4) |
| Entre 3 y 5 escenarios de calidad redactados | `docs/Evidencia S2 gimnasio_utb.md:174-266` — ES1 a ES8 | No cumple | Son 8 escenarios: exceden el máximo de 5 pedido por la ficha. El trabajo extra se valora, pero conviene seleccionar los 3–5 priorizados para la entrega |
| Cada escenario con sus seis partes y medida numérica | `docs/Evidencia S2 gimnasio_utb.md:176-185` (ES1 completo) y 187-266 (ES2–ES8) | Cumple | Las seis partes (fuente, estímulo, artefacto, ambiente, respuesta, medida) en los 8, con cifra y unidad. ES4 (línea 218) declara método completo: P95 ≤ 2 s, ventana de 30 min, carga de 50 usuarios concurrentes e instrumentación en ambos extremos |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/Evidencia S2 gimnasio_utb.md:136-172` — 7 atributos, cada hoja con «ES# · Prioridad: Alta/Media · Dificultad: Alta/Media/Baja» | Cumple | No es lista plana; priorización visible y la dificultad aproxima el riesgo. Las hojas corresponden a los escenarios redactados |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/C4.jpg` (imagen, no código) referenciado en `docs/Evidencia S2 gimnasio_utb.md:118-120` | No verificado | Solo imagen: la herramienta de revisión no pudo inspeccionarla, así que no se pudo comprobar leyenda ni flechas etiquetadas. La descripción textual (líneas 122-132) lista actores y relaciones coherentes, pero no sustituye la verificación visual. Haría falta abrir la imagen o versionar el diagrama como código (mermaid/PlantUML) |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` — prosa sobre «Consistencia de datos», sin tabla ni enlaces | No cumple | No hay tabla de aspectos ni enlaces de ningún escenario; el aspecto declarado ni siquiera referencia ES1 |

## Matriz transversal (CONTRATO)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:9` + clon sin autenticación | Cumple | |
| Estructura mínima presente | `ls-tree 1b30b7a4`: README.md, `docs/aspectos.md`, `docs/ia.md`, `docs/problema.md`, `docs/C4.jpg`, `docs/Evidencia S2 gimnasio_utb.md` | No cumple | Siguen sin `docs/arc42/`, `docs/adr/` y `docs/c4/`. El arc42 está completo en un solo archivo (`docs/Evidencia S2 gimnasio_utb.md`) y el C4 en `docs/C4.jpg` — desviación de estructura anotada, artefactos evaluados donde están |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` → `1b30b7a4` 2026-08-16T21:04:17-05:00 | Cumple | Sin etiqueta; commit vigente al cierre |
| Nombres de ADR según la convención | No existe `docs/adr/` | Cumple | Vacuo: sin ADR |
| ADR aceptados no reescritos | Sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md`: único commit `a45615e` (2026-08-08); ninguno en el periodo S2 | No cumple | El registro no creció en la semana 2 y su contenido sigue sin entradas con herramienta, aceptado y rechazado con motivo |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env`; `git log -S` limpio para 10 patrones (incluye blobs subidos y borrados) | Cumple | Limpio |
| Contribución de todos los integrantes | `shortlog -sne 1b30b7a4`: `PedroPambi` (8), `RodrigoFacioLince` (3) | No cumple | 2 cuentas de 3 integrantes. No aparece ninguna cuenta atribuible a Sebastián Caicedo Acosta en todo el historial |

## Recuento de criterios

5 de 9 criterios cumplidos (1 fila No verificado).

## No verificado / pendientes

- Leyenda y flechas etiquetadas del C4: no verificables sobre la imagen (`docs/C4.jpg`); haría falta abrirla con un visor o versionar el diagrama como código.

## Hallazgos para la planilla

- Sin entregas tardías: HEAD (2026-08-16T21:04) está dentro del cierre S2.
- El arc42 completo vive en un solo archivo (`docs/Evidencia S2 gimnasio_utb.md`) y no existe `docs/arc42/` — se arrastra desde S1.
- 8 escenarios: fuera del rango de 3 a 5.
- `docs/aspectos.md` sin tabla y sin enlaces a escenarios.
- C4 solo como imagen, en `docs/C4.jpg` (antes un `.jpg` con nombre UUID y un PDF con nombre desbordado, ambos gestionados el mismo día; el PDF se borró antes del cierre).
- Para el corte 1: los 8 escenarios tienen medida numérica; ES4 declara cómo se medirá (P95 ≤ 2 s, 50 usuarios concurrentes, ventana de 30 min, instrumentación en ambos extremos).
