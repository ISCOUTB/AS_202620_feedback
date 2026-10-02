> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# Semana 9 · Generación verificada y trazable · GimnasioUTB

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `e6a7f58e10123723a51de38e6368f8c81449804f` en `origin/main` (2026-09-28T01:32:10-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

Esta pasada **no tiene cierre**: se califica la punta actual de `origin/main`. El baseline del periodo
S9 es el hash calificado de S8 (`a71bc7583b67cd4f5eca11dd6d356f7d08d1cdc7`). Entre ese hash y la
punta hay seis commits (todos del 2026-09-28): `201a8cf` (persistencia PostgreSQL y control de
concurrencia), `b5a4fce` (manejo de errores), `ddb27d4` (composición del servidor y observabilidad),
`3fae092` (documentación de arquitectura), `5213f49` (pruebas de integración y health) y `e6a7f58`
(merge). Esos commits son posteriores al cierre de S8 y constituyen el periodo evaluado. Bajo
CONTRATO §12 la evidencia previa es línea base y no se recalifica por existir.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | rutas del código y commits | Cumple | La porción es el adaptador PostgreSQL del contador de aforo: `src/modules/aforo/infrastructure/persistence/aforo-postgres.adapter.js` (nuevo, 97 líneas, commit `201a8cf`), `src/modules/aforo/infrastructure/persistence/schema.sql` y `src/shared/logger.js` (commit `ddb27d4`), más el manejo de errores en `src/server.js` (`b5a4fce`). Es código del sistema, integrado por `AforoRepositoryPort`, no un ejercicio aparte. `docs/ia.md` no registra el uso de IA de esta porción (ver fila 6). |
| Cadena completa navegable para esa porción | fila de `docs/aspectos.md` recorrida hasta la evidencia | Cumple | La fila S1 de `docs/aspectos.md` (reescrita en el periodo) enlaza ADR-0001 y `docs/adr/0004-concurrencia-postgresql.md`, el adaptador PostgreSQL y `tests/postgres/aforo-postgres.integration.test.js`; el escenario y su resultado están en `docs/arc42/arc42_gimnasio_utb.md:246` (§10.2). El eslabón más débil es la evidencia de calidad: se reporta como recuento (12/12, 11/11, 8/8) y no como artefacto enlazado. |
| ADR con la decisión argumentada por el equipo | `docs/adr/NNNN-*.md` con restricciones del proyecto | Cumple | `docs/adr/0004-concurrencia-postgresql.md` (nuevo en `201a8cf`): decisión de usar PostgreSQL con `BEGIN`/`SELECT ... FOR UPDATE`/`UPDATE`/`COMMIT`, alternativas evaluadas (leer-modificar-guardar sin bloqueo, bloqueo optimista, Redis) y consecuencias/límites. Argumenta con las restricciones del proyecto (sin infraestructura extra, dominio aislado). |
| Prueba que falla ante el defecto que cubre | run en rojo, prueba de mutación o procedimiento documentado | No verificado | La prueba existe en el periodo (`tests/postgres/aforo-postgres.integration.test.js`, incluido el subtest «serializa 20 entradas concurrentes sin lost updates»), pero no hay run en rojo, prueba de mutación ni procedimiento documentado que muestre que falla ante el defecto. Queda como pregunta de sustentación (CONTRATO §13). |
| Medición del escenario asociado | resultado contrastado con el umbral | Cumple | `docs/arc42/arc42_gimnasio_utb.md:246` (§10.2, periodo) documenta el escenario S1: veinte entradas concurrentes, resultado «el aforo final es 20 … no se observaron lost updates», con el límite declarado (prueba de integración del adaptador, no de carga HTTP). Resultado contrastado con el criterio del escenario. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | extracto citado del archivo | No cumple | `docs/ia.md` no se modificó en el periodo: último commit `a59410d` (2026-09-13, semana 6). Tiene rechazos motivados previos, pero ninguna entrada de S9. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | hallazgos con su ubicación y su corrección | No cumple | `docs/contextos-delimitados.md` se editó en el periodo, pero solo para acotar el mapa conceptual (relación HTTP/REST) y ajustar la redacción de V1; no es una auditoría de erosión de la generación. No hay artefacto de auditoría del periodo. Contra el código, la única escritura de persistencia nueva es `aforo-postgres.adapter.js:71` (`UPDATE aforo_estado …`) y `schema.sql:6` (`INSERT INTO aforo_estado …`), dentro del módulo aforo, sin contraste documentado de propiedad de datos. |
| Dependencias propuestas verificadas en su registro oficial | lista de dependencias añadidas y su comprobación | Cumple | `package.json` añade una dependencia en el periodo: `pg: ^8.16.3`. Verificado sin autenticar en npm: `pg` («PostgreSQL client», último `8.23.1`) existe y es el paquete legítimo. |
| Sin credenciales en código, ejemplos ni documentación generada | barrido del contrato, incluido `docs/` | Cumple | `git grep` de CONTRATO §9 sobre la punta sin coincidencias; sin `.env` versionado; `git log -S"BEGIN PRIVATE KEY"` vacío. `.env.example` solo declara `DATABASE_URL` con marcadores de posición (`USER`, `PASSWORD`, `HOST`, `DATABASE`). |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | conjunto de evaluación con resultados, o el ADR | No cumple | El sistema no incorpora componente generativo (grep de `openai\|anthropic\|gemini\|llm\|gpt\|generative` sin coincidencias) y no existe el ADR que justifique no incorporarlo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | `ISCOUTB/AS_202620_GimnasioUTB`, clon anónimo con `--filter=blob:none` exitoso; rama `origin/main`. |
| Estructura mínima presente | Cumple | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` presentes en la punta. |
| Estado calificado identificable | Cumple | En esta pasada sin cierre se califica la punta: `e6a7f58` en `origin/main` (2026-09-28T01:32:10-05:00). |
| Nombres de ADR según la convención | No cumple | `docs/adr/ADR0001.md` no sigue `NNNN-titulo-kebab-case.md` y duplica el número 0001 de `docs/adr/0001-arquitectura-hexagonal.md`. |
| ADR aceptados no reescritos | No cumple | ADR-0001, aceptado en `92f4a53`, fue editado después en `c271073`, `b556737`, `59b6d3e`, `47a18d0` (2026-08-30) y de nuevo en `3fae092` (2026-09-28); ADR-0003 también fue editado en `3fae092`, sin ADR de reemplazo declarado. |
| `docs/ia.md` al día para la semana | No cumple | Sin commits sobre `docs/ia.md` en el periodo; la última entrada es del 2026-09-13 (semana 6). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI en verde sobre la punta (`CI`, `e6a7f58`, `success`: https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/36387447299), pero no hay `sonar-project.properties`, ni scanner en `.github/workflows/ci.yml`, ni URL pública del análisis con Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido sin coincidencias reales; sin `.env` versionado; `git log -S` vacío. |
| Contribución de todos los integrantes | Cumple | `shortlog -sne` consolida tres personas para los tres integrantes declarados: una firma con dos identidades (correo institucional y personal) y otra con correo institucional compartido; el resto del historial corresponde a la tercera. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `e6a7f58` en `origin/main` (2026-09-28T01:32:10-05:00).
- **Commits del periodo S9** (posteriores al hash calificado de S8 `a71bc75`): `201a8cf`, `b5a4fce`,
  `ddb27d4`, `3fae092`, `5213f49`, `e6a7f58`.
- **Veredicto**: con entrega parcial de S9. El equipo sí incorporó una porción real (adaptador
  PostgreSQL transaccional, logger y manejo de errores), su ADR (ADR-0004) y la medición del
  escenario en arc42 §10.2. Faltan la prueba que falle ante el defecto, la entrada de `docs/ia.md`,
  la auditoría de erosión y la decisión sobre el componente generativo. No hay commits posteriores
  a la punta a la fecha de esta pasada.
- Resumen: el repositorio conserva las piezas de S8 (backend local, health/ready, CI) que son línea
  base. Transversalmente siguen abiertos el ADR fuera de convención, los ADR aceptados editados
  (incluido uno en este mismo periodo), `docs/ia.md` sin la semana y SonarCloud sin evidencia pública.

## Recuento y nota sugerida

**6 de 10 criterios cumplidos** (filas 1, 2, 3, 5, 8 y 9).

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.4 = 1 + 4 × (6/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Fila 4 (prueba que falla ante el defecto que cubre): No verificado. La prueba existe en el
  periodo, pero no hay run en rojo, prueba de mutación ni procedimiento documentado que demuestre
  que falla ante el defecto. Queda como pregunta de sustentación.

## Hallazgos para la planilla

- S9 incorpora una porción real (adaptador PostgreSQL con bloqueo de fila, `logger` y manejo de
  errores), su ADR-0004 y la medición del escenario S1 en arc42 §10.2: es un avance sustantivo
  respecto de S8.
- `docs/ia.md` no registra el uso de IA de esta porción y se mantiene en la semana 6.
- No hay prueba que demuestre fallar ante el defecto (run en rojo, mutación o procedimiento) ni
  auditoría de erosión del periodo.
- No hay ADR de decisión sobre el componente generativo.
- Transversal: `ADR0001.md` fuera de convención y duplicando el número; ADR-0001 y ADR-0003
  editados tras su aceptación, uno de ellos en este periodo; SonarCloud sin configuración, scanner
  ni URL pública. El barrido de credenciales y la contribución de los tres integrantes siguen bien.
