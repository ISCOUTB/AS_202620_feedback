# Evidencia S2 · DinamikUTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `58734e1c9e37f386a0d9069805aa29e0d90cda00` · 2026-08-16T23:33:53-05:00 · «Rename Contexto.png to contexto.png» |
| Cierre | 2026-08-17T05:00:00Z (domingo 16 de agosto medianoche, UTC-5) |
| Comandos principales ejecutados | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only 58734e1c`; `git show 58734e1c:docs/...`; `git grep -nIE '<[a-z ]+>|TODO|lorem ipsum'`; `git grep` de secretos; `git shortlog -sne 58734e1c`; `git log --after='2026-08-17T05:00:00Z'` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/01-introduction-and-goals.md` | Cumple | §1.2 metas de calidad priorizadas con motivación; §1.3 tabla de stakeholders (estudiante, coordinador, administrador, equipo) con interés y necesidad. |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/02-architecture-constraints.md` | Cumple | Clasificadas en técnicas (§2.1), organizativas (§2.2) y legales (§2.3), cada una con justificación, más tabla resumen con impacto arquitectónico (§2.4). |
| Restricciones separadas de los requisitos | 02 frente a requisitos funcionales en 01/03 | Cumple | Separación correcta; no se detectan requisitos funcionales presentados como restricciones. |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42/03-context-and-scope.md` frente a `docs/c4/contexto.puml` | Cumple | Actores: estudiante, coordinador, administrador — los mismos tres del C4. §3 declara que no hay sistemas externos en el alcance y el diagrama tampoco los modela: coherente. |
| Entre 3 y 5 escenarios de calidad redactados | `docs/arc42/10-quality-requirements.md` | Cumple | 3 escenarios numerados: Q-01, Q-02, Q-03. |
| Cada escenario con sus seis partes y medida numérica | Q-01 (cita completa) en `10-quality-requirements.md` §10.3 | Cumple | Los 3 tienen Fuente, Estímulo, Artefacto, Entorno, Respuesta y Medida. Medidas numéricas: Q-01 «100 % de los datos mostrados debe corresponder», Q-02 «100 % de los intentos no autorizados rechazado», Q-03 «al menos 80 % de los usuarios evaluados». La condición de carga es declarada pero suave (sin cifra de usuarios/volumen). |
| Árbol de utilidad que prioriza por impacto y riesgo | §10.1 (tabla de priorización) y §10.2 (árbol) | Cumple | Tabla con columnas Impacto y Riesgo técnico por atributo (exactitud #1, seguridad #2, usabilidad #3…). Los 3 escenarios redactados corresponden a los 3 atributos priorizados. |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/contexto.puml` (PlantUML) + `docs/c4/contexto.png` (PNG 738×578 válido) | Cumple | Como código y como imagen. `SHOW_LEGEND()` incluye leyenda; las 3 relaciones están etiquetadas con propósito y protocolo («Consulta su progreso y envía solicitudes», HTTPS/JSON). El PNG se verificó como archivo válido; su contenido se evaluó por la fuente PlantUML. |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` (columna «Escenario de calidad») | Cumple | Tabla con filas por aspecto; A-01 → Q-01, Q-03 y A-05 → Q-02 (dos filas seguidas hasta el escenario: llegan). Observación: referencias por ID de texto, no hipervínculos (CONTRATO §5 pide eslabones navegables). |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt` OK; clon sin autenticación OK | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | `git ls-tree -r --name-only 58734e1c` | Cumple | Las seis rutas presentes (arc42 con las 12 secciones; `docs/adr/` con `.gitkeep`; `docs/c4/` con `.puml` y `.png`). |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` | Cumple | Hash `58734e1c…` con `%cI` 2026-08-16T23:33:53-05:00. |
| Nombres de ADR según la convención | `docs/adr/` solo con `.gitkeep` en el cierre | Cumple (vacuo) | Sin ADR todavía (el primer ADR se creó el 2026-08-23, fuera del cierre S2). |
| ADR aceptados no reescritos | sin ADR | Cumple (vacuo) | Ídem. |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia.md` | Cumple | `a3bbdcb` (2026-08-10, Eramirezr) dentro del periodo S2. Sin entradas de «qué se rechazó y por qué» (CONTRATO §6): pendiente. |
| Sin credenciales en el repositorio ni en el historial | `git grep` (regex §9), `.env`, `git log -S'BEGIN PRIVATE KEY'` | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | `git shortlog -sne 58734e1c` | Cumple | 4 identidades: `JuanchisV` (36), `Daniel-dev02` (8), `gillianisperez-prog` (3), `Eramirezr` (1). Desbalance fuerte: 35 de los commits del periodo S2 son de una persona (JuanchisV). |

## Recuento de criterios

- Ficha: **9 de 9** criterios Cumple.

## No verificado / pendientes

- Contenido visual del PNG del C4 (la herramienta de revisión no inspecciona imágenes; se evaluó por la fuente PlantUML).
- Correspondencia oficial cuenta↔persona contra la matrícula (los correos hacen evidentes las cuatro).

## Hallazgos para la planilla

- Entrega tardía: `51f7ce7` 2026-08-17T00:09:35-05:00 «Update ia.md» (9 minutos después del cierre S2, no incluido en el estado calificado).
- Trabajo del periodo S2 concentrado en una persona (JuanchisV, 35 commits del 10 al 16 de agosto); los demás suman 1 commit en el periodo.
- Trabajo posterior al cierre con pinta de semana 3: `3d5aad8` «Create 0001-seleccion-monolito-modular.md» y actualizaciones de `04-solution-strategy.md` (2026-08-23) — no cuentan para S2.
- `docs/aspectos.md` referencia escenarios por ID de texto, no por enlace (navegabilidad §5).
- La sección 10 declara 3 escenarios con medida comprobable y dice cómo se verificará (pruebas de acceso, prueba de uso sin asistencia): buen punto de partida para el corte 1; falta definir herramienta y carga.
