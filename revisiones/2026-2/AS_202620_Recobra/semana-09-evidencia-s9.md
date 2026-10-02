> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · Recobra

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `f8c0287451caf40487d5e54d8ec8ffda02680518` en `origin/master` (2026-10-01T13:13:00-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

Esta pasada **no tiene corte**: se califica la punta actual del 2026-10-01, no un commit anterior a un
cierre. El periodo S9 (`5c7f77b..origin/master`, con `5c7f77b` el hash de S8) contiene seis commits
(`34ab8f2`, `32a5a27`, `e580b47`, `1db41df`, `d0dc075`, `f8c0287`): la evidencia S9 formal, el ADR-0007,
la auditoría de erosión, la prueba de mutación, la medición del escenario S3 y la unificación del
esquema de error del contrato. La porción de código que la cadena presenta (Emparejamiento +
persistencia PostgreSQL) fue creada en `e952f5b` (2026-09-27T13:27), que es ancestro del hash calificado
de S8 (`5c7f77b`): es línea base y no se recalifica, pero el periodo sí aporta su cadena verificada y
las piezas de evidencia. La fila de credenciales y la matriz transversal se deciden sobre el estado en
la punta.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | `src/emparejamiento/` (`emparejamiento.controller.ts`, `publicacion-creada.listener.ts`, `emparejamiento.module.ts`), `src/application/use-cases/buscar-coincidencias.ts`, `src/domain/entities/coincidencia.ts` y `postgres-publicacion.repository.ts`. `docs/ia.md` atribuye su construcción asistida a IA (entrada 2026-09-27/28). | No cumple | La porción citada se creó en `e952f5b` (2026-09-27T13:27), ancestro del hash de S8 (`5c7f77b`): bajo CONTRATO §12 es línea base y no satisface la fila, que exige una porción del periodo S9. El periodo sí contiene cambios reales de sistema (unificación del esquema de error en `src/publicaciones/publicacion-invalida.filter.ts` y `docs/contracts/openapi.yaml`, `test/contract.e2e-spec.ts`, `public/index.html`, `mobile/lib/api/recobra_api.dart`), pero no son la porción que la cadena presenta. |
| Cadena completa navegable para esa porción | `docs/aspectos.md` fila `A5` (actualizada en `32a5a27`) recorre S3 → ADR-0004/ADR-0007 → `src/domain/entities/coincidencia.ts`, `src/application/use-cases/buscar-coincidencias.ts`, `src/emparejamiento/` → `coincidencia.spec.ts`, `buscar-coincidencias.spec.ts`, `test/emparejamiento.e2e-spec.ts` → evidencia de mutación (`docs/ia-auditoria-mutacion-emparejamiento.txt`) y medición (`docs/medicion-emparejamiento.md`). Todas las rutas existen en la punta. | Cumple | La fila enlaza aspecto, requisito, ADR, código, pruebas y evidencia, y la celda de Evidencia llega a la medición; la cadena no se rompe. |
| ADR con la decisión argumentada por el equipo | `docs/adr/0007-no-incorporar-componente-generativo.md` (creado en `32a5a27`, `## Estado` «Aceptada — 2026-10-01») compara incorporar un LLM frente a la heurística determinista contra las restricciones reales del proyecto: costo $0/mes, latencia de S5, disponibilidad de S4a, confiabilidad y costo de reversión. | Cumple | ADR del periodo, del equipo y argumentado con las restricciones del proyecto; no se limita a lo que propuso la herramienta. |
| Prueba que falla ante el defecto que cubre | `docs/ia-auditoria-mutacion-emparejamiento.txt` captura la salida real de `pytest`/`jest` con la mutación `!==` → `===` en `buscar-coincidencias.ts`: 3 pruebas fallan y 1 pasa, con el mensaje y el stack del defecto introducido; se revierte después. `docs/auditoria-generacion-ia.md` §4 lo describe. | Cumple | Prueba de mutación real, no solo afirmada, con la salida roja adjunta. |
| Medición del escenario asociado | `docs/medicion-emparejamiento.md`: escenario S3, umbral 60.000 ms; tres corridas el 2026-10-01 con latencias de 2.89 ms, 1.73 ms y 1.63 ms (~20.000× de margen). Procedimiento reproducible con `scripts/measure-emparejamiento.js` (nuevo en el periodo) y `npm run measure:emparejamiento`. | Cumple | Resultado contrastado con el umbral y con margen explícito; declara el alcance real (detección, sin componente de Notificaciones aún). |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | `docs/ia.md` suma dos entradas en el periodo: 2026-09-27/28 (aceptado Emparejamiento y persistencia; corregido el bug de CSS de la vitrina y una cifra de arranque en frío; rechazado inventar una identidad visual «UTB») y 2026-10-01 (aceptado auditoría, medición, script y ADR-0007; corregida una afirmación falsa de `no-conformidades.md`; rechazado usar un LLM, con motivo). | Cumple | Extracto del periodo con aceptado, corregido y rechazo motivado; el rechazo del LLM remite al ADR-0007. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | `docs/auditoria-generacion-ia.md` §1: barrido `(INSERT INTO\|UPDATE \|\.save\(\|\.create\(\|repository\.)` sobre `HEAD`; un único `INSERT INTO publicaciones` en el adaptador dueño `postgres-publicacion.repository.ts`, y revisión manual de `buscar-coincidencias.ts` (solo lectura por el puerto). Conclusión: sin erosión. | Cumple | El barrido replicado en la punta devuelve el mismo resultado: la escritura de `publicaciones` vive en el adaptador del contexto dueño. |
| Dependencias propuestas verificadas en su registro oficial | El diff del periodo contra el hash de S8 (`5c7f77b`) sobre `package.json` solo agrega el script `measure:emparejamiento`; no añade dependencias. La auditoría del equipo verifica `pg`, `@types/pg`, `@nestjs/event-emitter` y `jest-openapi` en el registro de npm, pero esas dependencias entraron en S6/S7 (línea base). | No cumple | No hay dependencias añadidas en el periodo S9 que verificar; la tabla de comprobación cubre dependencias de semanas anteriores y bajo CONTRATO §12 no satisface la fila. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido del contrato sobre la punta sin coincidencias en código ni en `docs/`; sin `.env` versionado; `.env.example` solo declara `PORT` y `DATABASE_URL=` sin valor (`32a5a27`); `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. El único secreto histórico (`node_modules/debug/.coveralls.yml`) está documentado como ajeno al equipo en `docs/no-conformidades.md`. | Cumple | Sin credenciales reales del equipo en la punta ni en el historial. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | `docs/adr/0007-no-incorporar-componente-generativo.md` decide no incorporar un LLM en tiempo de ejecución y argumenta costo por operación, latencia p95 y confiabilidad; por eso no aparece como contenedor externo en el C4 nivel 2. | Cumple | Existe el ADR de no incorporarlo, exigido por la ficha; la decisión está argumentada y es del periodo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_Recobra`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre `AS_202620_Recobra` conforme y visibilidad pública. |
| Estructura mínima presente | En `f8c0287`: `docs/arc42/arc42.md`, `docs/adr/` (0001–0007), `docs/c4/` (C4-C1/C2/C3), `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2; los C4 viven en `docs/c4/` con nombres propios. |
| Estado calificado identificable | `f8c0287451caf40487d5e54d8ec8ffda02680518` en `origin/master`, commit del 2026-10-01T13:13:00-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual. |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico.md` … `docs/adr/0007-no-incorporar-componente-generativo.md`. | Cumple | Los siete cumplen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | `git log --follow`: además de las ediciones de línea base de ADR-0002 y ADR-0003 (`f7c1a6c`, 2026-09-07), ADR-0004 (creado `d51910b`/`e1dfeaf`, S7) se editó en `34ab8f2` (2026-09-28) para agregar una «Actualización» y cambiar el relato del contrato a la versión 2.0.0, sin declarar un ADR de reemplazo. | No cumple | CONTRATO §4 prohíbe editar un ADR aceptado sin declarar reemplazo; ADR-0004 se modificó después de aceptarse en el periodo S9. |
| `docs/ia.md` al día para la semana | `docs/ia.md` suma las entradas 2026-09-27/28 y 2026-10-01 en el periodo, con lo aceptado, lo corregido y lo rechazado con motivo. | Cumple | El registro crece dentro del periodo revisado y documenta rechazos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Único run del hash revisado: [ci 36905180747](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/36905180747), conclusión `success`. Existe `sonar-project.properties` y el workflow invoca `SonarSource/sonarqube-scan-action`, pero el paso está marcado `continue-on-error: true` y no hay URL pública del análisis con su Quality Gate. | No cumple | Faltan la garantía de ejecución real del scanner y la URL pública del Quality Gate exigidas por el contrato §8; el propio equipo lo reconoce en `docs/ia.md`. |
| Sin credenciales en el repositorio ni en el historial | Barrido del contrato y `git log -S` sin coincidencias; sin `.env` versionado; `.env.example` con claves vacías. | Cumple | Sin credenciales del equipo; el token histórico de Coveralls está documentado como ajeno. |
| Contribución de todos los integrantes | `git shortlog -sne f8c0287`: `Cconde31` 49 más 1 con la variante `cconde31` del mismo correo (consolidado) y la identidad `Steamlinker`; `vylrir` 25; `Fernando Isacc Conde Herrera` 24; `MiguelJacome` 10. | Cumple | Cuatro personas para cuatro integrantes; aporte repartido, con Fernando ya con contribución sustantiva. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `f8c0287451caf40487d5e54d8ec8ffda02680518 2026-10-01T13:13:00-05:00 Dejar de registrar campos de la respuesta HTTP en measure-emparejamiento.js` (`origin/master`)
- **Veredicto**: evidencia S9 completa en su matriz, con dos no conformidades (porción de línea base y SonarCloud)
- Resumen: el equipo produjo en el periodo una evidencia S9 sólida: ADR-0007 de no incorporar un LLM
  argumentado con costo y latencia, auditoría de erosión que confirma un único dueño de escritura,
  prueba de mutación real con la salida roja adjunta, medición del escenario S3 con tres corridas
  (~2 ms frente a 60.000 ms) y dos entradas nuevas en `docs/ia.md` con rechazos motivados. La cadena
  de `docs/aspectos.md` (A5) es navegable de extremo a extremo. La deuda principal es de frontera: la
  porción de código que la cadena presenta (Emparejamiento y persistencia PostgreSQL) es línea base
  (creada en `e952f5b`, antes del hash de S8), así que la fila 1 no se satisface con el periodo. La
  otra es transversal y viene de atrás: SonarCloud no es auditable (scanner con `continue-on-error` y
  sin URL pública del Quality Gate), y ADR-0004 se editó en el periodo sin declarar reemplazo. El CI
  del hash revisado está en verde (run 36905180747).

Pendientes que siguen abiertos:
- La porción construida con IA de la cadena es de S8; para S9 falta una porción del periodo.
- Sin dependencias añadidas en el periodo que verificar en los registros.
- SonarCloud sin URL pública del Quality Gate; el paso del scanner no garantiza ejecución real.
- ADR-0004 editado el 2026-09-28 (`34ab8f2`) sin ADR de reemplazo declarado (y ADR-0002/0003 de línea base).
- El análisis de documentos previos (`docs/no-conformidades.md`) requirió corrección de afirmaciones no verificadas; el equipo lo documentó.

## Recuento y nota sugerida

**8 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 4.2 = 1 + 4 × (8/10).** La nota final la fija el profesor en Moodle.

La fila 1 no se satisface porque la porción de código presentada es línea base (CONTRATO §12); la fila
8 no se satisface porque el periodo S9 no añadió dependencias que verificar.

## No verificado / pendientes

- Nada quedó en **No verificado** en la ficha: todas las comprobaciones se resolvieron sobre archivos
  legibles del repositorio.
- SonarCloud: sin URL pública del Quality Gate y con el paso del scanner en `continue-on-error`; fila
  transversal en No cumple.
- La porción de código de la fila 1 es de S8; queda como hallazgo, no como pregunta de sustentación.

## Hallazgos para la planilla

- El periodo S9 (`5c7f77b..f8c0287`) tiene seis commits con evidencia real: ADR-0007, auditoría de erosión, prueba de mutación, medición S3 y unificación del esquema de error del contrato.
- La porción de código que la cadena presenta (Emparejamiento + PostgreSQL) se creó en `e952f5b`, ancestro del hash de S8: es línea base (CONTRATO §12).
- `docs/aspectos.md` fila A5 es navegable hasta la evidencia de mutación y la medición; la cadena no se rompe.
- Medición del escenario S3: 2.89/1.73/1.63 ms frente a un umbral de 60.000 ms, con procedimiento reproducible.
- Verificación de `pg`, `@types/pg`, `@nestjs/event-emitter` y `jest-openapi` en npm correcta, pero corresponden a S6/S7 (línea base).
- Sin credenciales en la punta ni en el historial.
- CI del hash revisado en verde (run 36905180747); SonarCloud sigue sin Quality Gate público y el scanner está en `continue-on-error`.
- ADR-0004 editado en el periodo (`34ab8f2`, 2026-09-28) sin reemplazo declarado: no conformidad transversal.
- Los cuatro integrantes contribuyen; Fernando ya supera la contribución mínima.
