> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# Semana 9 · Evidencia S9 · Generación verificada y trazable · CampusMarket


| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `784d788` en `origin/master` (2026-09-27T23:50:19-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

La punta actual de `origin/master` coincide con el hash calificado de S8 (`784d788`). El
periodo S9 es **vacío**: `git rev-list --count 784d788..origin/master` = **0**. No hay ninguna
porción, cadena, ADR, prueba, medición ni extracto de IA producido entre el hash de S8 y la
punta. Por la regla del periodo, ninguna fila de la entrega S9 puede apoyarse en el artefacto de
una semana anterior: la evidencia S8 es línea base y no satisface la fila.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | rutas del código y commits | No cumple | Periodo vacío: no hay commits entre `784d788` y la punta. No existe porción construida en el periodo S9. |
| Cadena completa navegable para esa porción | fila de `docs/aspectos.md` recorrida hasta la evidencia | No cumple | Sin fila de `docs/aspectos.md` añadida o modificada en el periodo. |
| ADR con la decisión argumentada por el equipo | `docs/adr/NNNN-*.md` con restricciones del proyecto | No cumple | `docs/adr/` sin cambios en el periodo (siguen los ADR 0001-0008 del estado de S8). |
| Prueba que falla ante el defecto que cubre | run en rojo, prueba de mutación o procedimiento documentado | No verificado | No hay run en rojo, mutación ni procedimiento de S9. La evidencia más reciente es de S7 (`docs/evidencias/fallo-contrato-s7-2026-09-15.md`), línea base. Queda como pregunta de sustentación. |
| Medición del escenario asociado | resultado contrastado con el umbral | No cumple | Sin medición nueva en el periodo. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | extracto citado del archivo | No cumple | El último cambio de `docs/ia.md` es `083bcc3` (2026-09-27, registro de S8), anterior al periodo S9. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | hallazgos con su ubicación y su corrección | No cumple | Sin auditoría de erosión en el periodo. |
| Dependencias propuestas verificadas en su registro oficial | lista de dependencias añadidas y su comprobación | No cumple | `git diff 784d788..origin/master -- backend/requirements.txt requirements.txt package.json …` vacío: no se añadió ninguna dependencia en el periodo. |
| Sin credenciales en código, ejemplos ni documentación generada | barrido del contrato, incluido `docs/` | Cumple | `git grep` del contrato sobre la punta: solo `password=os.environ["CAMPUSMARKET_DB_PASSWORD"]` en `.github/workflows/backend-tests.yml:78` y `scripts/run_s4.ps1:31` (referencias, no valores). Sin `.env` versionado. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | conjunto de evaluación con resultados, o el ADR | No cumple | Sin conjunto de evaluación, costo/latencia ni ADR de no incorporarlo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET`; clon anónimo `--filter=blob:none` exitoso; rama `origin/master`. | Cumple | Responde sin autenticación; el nombre sigue `AS_202620_<PROYECTO>`. |
| Estructura mínima presente | El árbol contiene `docs/arc42/`, `docs/adr/` (0001-0008), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2. |
| Estado calificado identificable | `784d788` en `origin/master`, `2026-09-27T23:50:19-05:00`: `Merge pull request #44 from ISCOUTB/S8-cierre-evidencia`. | Cumple | La punta actual coincide con el hash de S8; no hay commits posteriores. |
| Nombres de ADR según la convención | `0001-usar-monolito-modular.md` … `0008-desplegar-mysql-en-azure-flexible-server.md`. | Cumple | Los ocho pasan el filtro `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | ADR-0002 aceptado `77e1323` (2026-09-05) y editado en `d72d6ac`, `3bb84a9`, `04fe631`; ADR-0003 aceptado `485249a` (2026-09-15) y editado en `df72b1c`; ADR-0005 aceptado `39f0952` (2026-09-27) y reescrito en `0e2b85b`. Sin cambios en el periodo S9, pero el hallazgo sigue abierto. | No cumple | El contrato §4 prohíbe editar un ADR aceptado sin declarar reemplazo; ninguna edición lo declara. |
| `docs/ia.md` al día para la semana | Sin commit sobre `docs/ia.md` en el periodo S9; el último es `083bcc3` (2026-09-27, S8). | No cumple | No hay registro de uso de IA de la semana 9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Run del hash revisado: `Pruebas del backend` — `success` (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/36379371983). Análisis público en SonarCloud para la revisión `784d788`: Quality Gate **OK**. Pero `.github/workflows/backend-tests.yml` no invoca el scanner (solo `pytest` y `ruff`) y ningún run de CI ejecutó el scanner. | No cumple | El contrato §8 exige la línea del workflow que invoca el scanner y el run que lo ejecutó; esa parte falta. El análisis público existe, pero llega por análisis automático, no por la cadena auditable exigida. |
| Sin credenciales en el repositorio ni en el historial | `git grep` del contrato sobre la punta sin valores reales; ningún `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | El password de CI (`campusmarket_ci`) es un valor efímero de prueba del propio workflow, no una credencial de producción. |
| Contribución de todos los integrantes | `shortlog -sne` consolidado por correo idéntico: `nilver-garcia` + `Nnigarp` (193), `camilixo92` (26), `Carulla-sd` (19). | Cumple | Los tres integrantes declarados tienen commits. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `784d788` — `2026-09-27T23:50:19-05:00 Merge pull request #44 from ISCOUTB/S8-cierre-evidencia`.
- **Veredicto**: sin entrega S9; la punta no avanzó desde S8.
- **Commits posteriores al cierre de S8**: ninguno; la punta coincide con el hash calificado de S8.
- Resumen: entre el hash calificado de S8 y la punta no hay ningún commit. No existe una porción S9, ni cadena, ni ADR, ni prueba, ni medición, ni registro de IA de la semana. La única evidencia del periodo es la del estado de S8, que es línea base y no se recalifica. Siguen abiertos los pendientes transversales arrastrados de S8: la evidencia auditable de SonarCloud (el workflow no invoca el scanner) y la edición de ADR aceptados (ADR-0002, ADR-0003 y ADR-0005).

Pendientes que siguen abiertos:
- Sin entrega S9: cuando el equipo empuje, la nota sube sola al aparecer el periodo.
- SonarCloud: añadir el paso del scanner al workflow y aportar el run que lo ejecute.
- No editar ADR aceptados sin declarar reemplazo (ADR-0002, ADR-0003, ADR-0005).

## Recuento y nota sugerida

**1 de 10 criterios Cumple** (el criterio 9, barrido de credenciales sobre la punta).

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Criterio 4 (prueba que falla): No verificado por ausencia de run en rojo, mutación o procedimiento de S9; queda como pregunta de sustentación.
- SonarCloud: el análisis público existe con Quality Gate OK, pero el workflow no invoca el scanner y ningún run de CI lo ejecutó: fila transversal No cumple.
- `docs/ia.md` y los ADR aceptados siguen como en S8: sin entrada de S9 y con ediciones sin reemplazo declarado.

## Hallazgos para la planilla

- La punta de `origin/master` no avanzó desde S8: `git rev-list --count 784d788..origin/master` = 0.
- Sin evidencia S9 en el periodo: ninguna fila de la entrega puede cumplirse con un artefacto de S8 (línea base).
- El barrido de credenciales sobre la punta está limpio (solo referencias a variables de entorno).
- SonarCloud sigue sin la cadena auditable del §8 pese a existir análisis público con Quality Gate OK.
- ADR-0002, ADR-0003 y ADR-0005 fueron editados después de su aceptación sin declarar un ADR de reemplazo.
