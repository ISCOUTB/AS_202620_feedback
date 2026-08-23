# Evidencia S2 · ElMapita

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `c5d9964c4415be16ccc3cb2641d26fd1da5b01d2` · 2026-08-16T14:21:20-05:00 · «docs: Secciones 1-3 de arc42, escenarios de calidad y C4» |
| Cierre | 2026-08-17T05:00:00Z (domingo 16 de agosto medianoche, UTC-5) |
| Comandos principales ejecutados | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only c5d9964c`; `git show c5d9964c:docs/...`; `git show --stat c5d9964c`; `git cat-file -s` (ia.md); `git grep` de secretos; `git shortlog -sne c5d9964c`; `git log --after='2026-08-17T05:00:00Z'` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/arc42-template-EN.md` §1 (redactada dentro de la plantilla) | Cumple | §1.2 objetivos de calidad con prioridad y criterio de éxito; §1.3 tabla de interesados con preocupaciones. Nota: las secciones viven dentro de la plantilla, no en archivos separados (desviación de estructura, el artefacto se evalúa donde está). |
| arc42 sección 2 con restricciones clasificadas y justificadas | §2 del mismo archivo | Cumple | RES-01 académica, RES-02 física/tecnológica, RES-03 operacional: tipo y origen declarados, con justificación y consecuencia. Sin categoría legal explícita (la privacidad se menciona como restricción legal en §10.1, de pasada). |
| Restricciones separadas de los requisitos | §2 frente a §1.1 | Cumple | Separación explícita y cuidada: declaran que Flutter/NestJS/Supabase no son restricciones porque fueron elegidos libremente (serán decisiones vía ADR). |
| arc42 sección 3 con actores y sistemas externos | §3.1 del mismo archivo | Cumple | Identifica actores (estudiante/visitante/personal) y sistemas externos (plataforma de ubicación, Supabase) con entradas/salidas. Observación: la coherencia visual con el PNG del C4 no pudo verificarse (herramienta sin soporte de imágenes), y el enlace normativo a `c4/contexto.md` está roto (ese archivo no existe en el cierre). |
| Entre 3 y 5 escenarios de calidad redactados | §10.2 (EC-01…EC-04) | Cumple | 4 escenarios numerados y enlazables por ancla. |
| Cada escenario con sus seis partes y medida numérica | EC-01 (cita completa) en §10.2 | Cumple | Los 4 tienen Fuente, Estímulo, Artefacto, Entorno, Respuesta y Medida. Medidas numéricas con unidad y carga: EC-01 «<5 s p95 en una prueba de 30 cargas», EC-02 «95 % de fotogramas ≤33,3 ms», EC-03 «≤15 m; opción manual en ≤2 s tras 10 s», EC-04 «<5 s en el 100 % de 20 pruebas». Además cada escenario declara «Evidencia prevista» (cómo se medirá). |
| Árbol de utilidad que prioriza por impacto y riesgo | §10.1 | Cumple | Hojas con pares Impacto/Riesgo (A/A, A/M) y priorización explícita (EC-01 a EC-03 primero por combinar impacto y riesgo altos). Los escenarios priorizados son los redactados. |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/C4_Contexto.png` (PNG 1942×346 válido) | No verificado | Solo imagen, sin fuente (no hay `contexto.md` ni código de diagrama en el cierre, y el enlace `../c4/contexto.md` desde §3 y `docs/aspectos.md` está roto). Leyenda y flechas no verificables con la herramienta de revisión; haría falta el diagrama como código o abrir el PNG. |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` (columna «Escenarios de calidad») | Cumple | A-01 enlaza EC-01…EC-04 con anclas válidas a `arc42/arc42-template-EN.md#ec-0X`; seguidas dos filas al azar (EC-01 y EC-04): llegan. Ojo: el enlace de la columna C4 (`c4/contexto.md`) sí está roto. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt` OK; clon sin autenticación OK | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | `git ls-tree -r --name-only c5d9964c` | Cumple | Las seis rutas literales presentes (`docs/arc42/` con la plantilla redactada; `docs/adr/` y `docs/c4/` con `.gitkeep`). Los artefactos arc42 viven dentro de la plantilla y el C4 solo como PNG: anotado. |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` | Cumple | Hash `c5d9964c…` con `%cI` 2026-08-16T14:21:20-05:00. |
| Nombres de ADR según la convención | `docs/adr/` solo con `.gitkeep` en el cierre | Cumple (vacuo) | Sin ADR (el `0001-estilo-arquitectonico-propuesto.md` llega el 2026-08-22, fuera del cierre S2). |
| ADR aceptados no reescritos | sin ADR | Cumple (vacuo) | Ídem. |
| `docs/ia.md` al día para la semana | `git cat-file -s c5d9964c:docs/ia.md` → 0 bytes | No cumple | Sigue vacío; único commit `df1e2f7` (2026-08-07). No registra usos ni rechazos de IA. |
| Sin credenciales en el repositorio ni en el historial | `git grep` (regex §9), `.env`, `git log -S'BEGIN PRIVATE KEY'` | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | `git shortlog -sne c5d9964c` | No cumple | 2 identidades para 3 integrantes: `RobotDRMX` (7 commits, todos de la semana 1, cuenta sin atribuir) y Rodrigo Vazquez Rico (1 commit, `c5d9964c`). En el periodo S2 solo commitó Rodrigo. Angel Fabian Gutierrez Gomez y Diego Rosales Garza no aparecen con identidad atribuible; `YOOUYII` nunca vista. |

## Recuento de criterios

- Ficha: **8 de 9** criterios Cumple (el noveno, No verificado).

## No verificado / pendientes

- Contenido del PNG del C4 (leyenda, flechas): requiere inspección humana o publicar el diagrama como código (`contexto.md` referenciado pero inexistente).
- Atribución de `RobotDRMX` a un integrante (¿Angel Fabian Gutierrez Gomez o Diego Rosales Garza?) y estado de `YOOUYII`.

## Hallazgos para la planilla

- Entregas tardías (posteriores al cierre S2): `aa16382` 2026-08-22 «Documentos de arquitectura completa: arc42 S4, matriz comparativa, ADR-0001 \| Esqueleto en codigo Base» (añade código backend/frontend y ADR-0001) y `8e30f61` 2026-08-22.
- `docs/ia.md` vacío en ambos cierres (arrastre desde S1).
- Sin ficha del problema y sin tensiones de calidad (arrastre desde S1).
- Secciones arc42 redactadas dentro de la plantilla; las secciones 4–9, 11 y 12 conservan texto de plantilla (no exigidas en S2).
- Enlace roto a `docs/c4/contexto.md` desde §3 y desde `docs/aspectos.md` (también en HEAD): el C4 solo existe como PNG.
- Contribución mínima en S2: 1 commit de una sola persona en todo el periodo.
- Los 4 escenarios declaran medida y, además, evidencia prevista de medición (pruebas instrumentadas, dispositivo de referencia): es el punto más fuerte para el criterio de diagnóstico del corte 1.
