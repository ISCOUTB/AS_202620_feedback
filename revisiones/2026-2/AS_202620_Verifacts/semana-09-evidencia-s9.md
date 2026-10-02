> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · Verifacts

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `dae98e8d322b33898dd24622b0f5fbbeca6fa5a2` en `origin/master` (2026-09-28T22:24:54-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

Esta pasada **no tiene corte**: se califica la punta actual del 2026-10-01. El periodo S9
(`d2d7b5c..dae98e8`) tiene **22 commits** del 2026-09-28 con artefactos específicos de la evidencia:
ADR-0006, pruebas de frontera, mutaciones inducidas, medición de Q-01/Q-05 y auditoría de erosión.
Bajo CONTRATO §12 las filas que describen la entrega S9 se deciden con la evidencia del periodo; la
fila de credenciales y la matriz transversal se deciden sobre el estado en la punta. La excepción
docente de S1/S2 no aplica a S9.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | En el periodo: `app/modules/scoring/service.py` (constantes `MAX_SCORE`, `UMBRAL_RIESGO_MEDIO`, `UMBRAL_RIESGO_ALTO` y `classify_score`), pesos en `app/modules/analysis/analyzer.py`; commits `1893548`, `a73c226` y `8538bd5`. | Cumple | Porción real del sistema (módulo `Scoring`) modificada en el periodo; el ADR-0006 declara que se construyó con apoyo de IA. |
| Cadena completa navegable para esa porción | Fila `A-06` de `docs/aspectos.md` (nueva en el periodo) con enlaces a escenarios, C4, ADR, pruebas y evidencia. La celda ADR enlaza `adr/0006-semantica-del-resultado.md`, que **no existe** (el archivo real es `docs/adr/ADR-0006.md`); el enlace a la auditoría apunta a `auditoria-s9.md` bajo `docs/`, pero el archivo está en la raíz. | No cumple | La cadena se rompe en el eslabón ADR y en el enlace a la auditoría; los enlaces a pruebas y medición sí resuelven. |
| ADR con la decisión argumentada por el equipo | `docs/adr/ADR-0006.md`: «Decisor: Equipo VeriFacts (no la herramienta)»; contexto con tres hallazgos de la auditoría, decisión (significado, valores, regla de cambio), alternativas descartadas con motivo (bajar el umbral, subir pesos, delegar a un modelo generativo, renombrar etiquetas) y consecuencias. | Cumple | La decisión está argumentada por el equipo con las restricciones del proyecto; no es un «se eligió lo que propuso la herramienta». |
| Prueba que falla ante el defecto que cubre | `docs/evidencia/mutaciones-s9.md` + `scripts/mutaciones_s9.py`: cinco defectos inducidos (M1–M5); la suite previa no detectaba 3 y `tests/test_scoring_boundaries.py` detecta los 5. | Cumple | Evidencia de mutación del periodo que demuestra el fallo ante el defecto. |
| Medición del escenario asociado | `docs/evidencia/medicion-q01-q05.md` + `scripts/medir_q01_q05.py`: Q-01 P95 = 46.9 ms contra umbral ≤ 3000 ms (CUMPLE); Q-05 100 % de coincidencia (CUMPLE). | Cumple | Resultado contrastado con el umbral del escenario. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | El último commit sobre `docs/ia.md` es `50568f1` (2026-09-23), anterior al periodo; no hay extracto de la semana S9. | No cumple | El registro histórico documenta aceptados y rechazos, pero no creció en el periodo S9; la evidencia previa no satisface la fila (CONTRATO §12). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | `auditoria-s9.md` §1 (E-1…E-5) documenta la detección y corrección de la erosión sobre límites de contexto y propiedad de datos (`scoring` importaba `analyzer.py` — corregido; pruebas escribían en `data/verifacts.db` — corregido; `sqlite3` solo en `repository.py`); contrastado con el código (`git grep sqlite3 -- app` solo `repository.py`) y vigilado por `tests/test_boundaries.py`. | Cumple | Hallazgos con su ubicación y corrección; se contrastó sobre el código generado. |
| Dependencias propuestas verificadas en su registro oficial | El periodo cambia `requirements.txt`: `pytest>=9.0.3,<10`. Verificado contra PyPI: `https://pypi.org/pypi/pytest/9.0.3/json` responde HTTP 200 y la versión figura entre las publicadas. | Cumple | Dependencia del periodo existente y con nombre legítimo. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido de patrones de credenciales sobre `dae98e8` sin coincidencias; `.env.example` y `frontend/.env.example` versionados sin valores; `.gitignore` cubre `.env`, `.pem` y `.key`; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | El único secreto referenciado es `${{ secrets.SONAR_TOKEN }}`, no un valor. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | El sistema no incorpora un componente generativo en ejecución; `ADR-0006` descarta delegar la calibración a un modelo generativo y cita el rechazo del LLM como clasificador en el registro de `docs/ia.md`. | No cumple | No hay ADR dedicado a la decisión de no incorporar un componente generativo; el rechazo de ADR-0006 es sobre la calibración, no sobre el componente. La ausencia de decisión no es la decisión de no hacerlo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_Verifacts`, clonado sin autenticación; rama principal `origin/master`. | Cumple | Nombre conforme y visibilidad pública. |
| Estructura mínima presente | En `dae98e8`: `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Las seis rutas están presentes. |
| Estado calificado identificable | `origin/master`, `dae98e8d322b33898dd24622b0f5fbbeca6fa5a2`, 2026-09-28T22:24:54-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual. |
| Nombres de ADR según la convención | El filtro de §4 devuelve `ADR-0006.md`: no sigue `NNNN-titulo-en-kebab-case.md` (mayúsculas y sin número inicial). | No cumple | El ADR del periodo rompe la convención de nombres. |
| ADR aceptados no reescritos | `git log --follow`: `9430845` (2026-09-23) editó ADR-0001, 0002, 0003 y 0004 después de su aceptación, sin ADR de reemplazo declarado. | No cumple | Viene registrado desde S8; el historial de la punta conserva esas ediciones. |
| `docs/ia.md` al día para la semana | Último commit sobre el archivo: `50568f1` (2026-09-23); sin entrada del periodo S9. | No cumple | El registro no creció en la ventana de esta evidencia. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Runs del hash revisado: `Tests` `36517048309` y `SonarCloud` `36517048351`, ambos `success`; `sonar-project.properties` existe; URL pública `https://sonarcloud.io/project/overview?id=ISCOUTB_AS_202620_Verifacts`, pero `docs/despliegue.md:37` declara el **Quality Gate general en rojo**. | No cumple | El run ejecutó el scanner y la URL es pública, pero un Quality Gate en rojo es no conformidad (CONTRATO §8). |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de credenciales en `dae98e8` sin coincidencias; sin `.env`, `.pem` ni `.key` versionados; `git log -S'BEGIN PRIVATE KEY'` sin resultados. | Cumple | Barrido limpio. |
| Contribución de todos los integrantes | `git shortlog -sne dae98e8` consolidado por correo idéntico: `PedroC1213` (262, dos correos y dos firmas) y `Cristian Cardeño` (33, dos correos). | No cumple | Solo 2 de los 3 integrantes declarados aparecen; el tercer integrante no tiene commits. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `dae98e8d322b33898dd24622b0f5fbbeca6fa5a2` 2026-09-28T22:24:54-05:00 `S9: pruebas de frontera y erosion, medicion Q-01/Q-05` (`origin/master`)
- **Veredicto**: al día en el trabajo de S9; con no conformidades transversales
- Resumen: la punta de `master` contiene la evidencia S9 completa: ADR-0006 con la decisión del
  equipo sobre pesos y umbrales, pruebas de frontera (`tests/test_scoring_boundaries.py`), pruebas de
  límites de módulo (`tests/test_boundaries.py`), evidencia de mutaciones, medición de Q-01/Q-05 y la
  auditoría de erosión. El avance satisface las filas 1, 3, 4, 5, 7, 8 y 9 de la ficha. Quedan
  abiertos: la cadena de aspectos se rompe en el enlace al ADR-0006 (nombre de archivo distinto) y al
  informe de auditoría; `docs/ia.md` no se actualizó en el periodo; no hay ADR de no incorporar un
  componente generativo. En lo transversal persisten el ADR-0006 fuera de convención, ediciones de ADR
  aceptados sin reemplazo, Quality Gate de SonarCloud en rojo y un integrante sin contribución.

Pendientes que siguen abiertos:
- Corregir los enlaces de la fila `A-06` de `docs/aspectos.md`: el ADR apunta a `adr/0006-semantica-del-resultado.md` y la auditoría a `docs/auditoria-s9.md`; ambos no existen.
- Renombrar `docs/adr/ADR-0006.md` a la convención `0006-<kebab-case>.md` (el código y el ADR referencian `0006-semantica-del-resultado.md`).
- Registrar el uso de IA del periodo S9 en `docs/ia.md`.
- Decidir en un ADR propio la no incorporación del componente generativo (hoy solo parcial en ADR-0006).
- Corregir el Quality Gate de SonarCloud, documentado en rojo.
- Dejar de editar ADR aceptados sin declarar reemplazo.
- Confirmar la contribución del tercer integrante sin inferir identidades.

## Recuento y nota sugerida

**7 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

Bajo CONTRATO §12, las filas 1, 3, 4, 5, 7, 8 y 9 se resuelven con evidencia del periodo S9 y el
barrido de credenciales sobre la punta; la fila 2 se rompe por enlaces no resolubles, la fila 6 carece
de entrada de `docs/ia.md` del periodo y la fila 10 no tiene el ADR que exige.

## No verificado / pendientes

- No quedó ninguna fila en No verificado: las comprobaciones se resolvieron con archivos legibles del
  repositorio o con el registro público.
- La afirmación de `auditoria-s9.md` de que `docs/ia.md` y ADR-0002 se «corrigieron» en S9 no se
  corresponde con el estado del repositorio: `docs/ia.md` no cambió en el periodo y sigue listando
  `MLAnalyzer` como «Aceptado» aunque el código no lo contiene. Queda como hallazgo para la sustentación.

## Hallazgos para la planilla

- S9 con evidencia completa: ADR-0006, pruebas de frontera y de módulos, mutaciones inducidas, medición de Q-01/Q-05 y auditoría de erosión (E-1…E-5).
- La fila `A-06` de `docs/aspectos.md` enlaza un ADR con nombre inexistente (`0006-semantica-del-resultado.md`) y la auditoría desde `docs/`; la cadena no es navegable en esos dos eslabones.
- `docs/adr/ADR-0006.md` rompe la convención de nombres; el código y los documentos esperan `0006-semantica-del-resultado.md`.
- `docs/ia.md` no creció en el periodo; la corrección de la afirmación sobre `MLAnalyzer` que declara la auditoría no está en el repositorio.
- `pytest` sube a `9.0.3` y la versión existe en PyPI; verificación correcta.
- Quality Gate de SonarCloud en rojo pese a los runs verdes.
- ADR 0001-0004 editados en `9430845` sin reemplazo declarado; el tercer integrante sigue sin commits.
