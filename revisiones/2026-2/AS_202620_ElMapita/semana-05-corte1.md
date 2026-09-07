# semana-05-corte1 · ElMapita

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión preliminar del 2026-09-03. No existe la etiqueta `corte-1`; se calificó el último commit anterior al cierre. El repositorio no tuvo ningún commit nuevo entre la revisión preliminar y el cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado calificado | sin etiqueta `corte-1` real; último commit ≤ cierre: `4806374a4d643707611720836e59dd436e7a441f` (`2026-09-01T08:39:54-06:00`, mensaje de commit literalmente **"corte-1"**) |
| Cierre | `2026-09-07T05:00:00Z` |
| Comandos ejecutados | `git tag --list` (vacío); `git branch -a`; `git log --until=... HEAD`; `git ls-tree -r --name-only`; `git log --diff-filter=A -- docs/adr/`; lectura de `docs/adr/0001-*.md`, `docs/aspectos.md`, `docs/ia.md`, README; `git grep` de secretos; `git ls-files \| grep .env`; `git shortlog -sne`; `curl .../actions/runs?per_page=10` (1 llamada) |
| Restricción asignada | No disponible en el kit ni citada explícitamente como tal en el repositorio. |

**Hallazgo de versionado importante:** el equipo **no creó una etiqueta Git** `corte-1`; en su lugar hicieron un **commit cuyo mensaje es literalmente `corte-1`** (`git commit -m "corte-1"`). Un mensaje de commit no es una etiqueta (`git tag`) y no cumple el requisito de la ficha ni del contrato.

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| 1. Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` sin salida; `git log` muestra un commit con mensaje `corte-1` en `4806374`, `2026-09-01T08:39:54-06:00`, anterior al cierre | **No cumple** | Confusión entre mensaje de commit y etiqueta Git; no existe ninguna etiqueta en el repositorio. |
| 2. PDF de dos páginas | No hay PDF versionado en el repositorio en la ruta esperada (no se encontró `docs/cortes/`) | **No verificado** | Debe comprobarse en Moodle. |
| 3. Impacto de la restricción en requisitos, C4 y código | `docs/aspectos.md` documenta el aspecto A-01 (mapa 3D + geolocalización) de la línea base; ningún artefacto declara una restricción nueva asignada | **No cumple** | No hay diagnóstico de una restricción nueva. |
| 4. Línea base medida y verificable | Las 4 filas de `docs/aspectos.md` (EC-01…EC-04) tienen columna Evidencia = "Pendiente"; ninguna prueba se ejecutó todavía | **No cumple** | Sin cifra medida con herramienta/procedimiento. |
| 5. ADR del reto | Único ADR: `docs/adr/0001-estilo-arquitectonico-propuesto.md` (creado 2026-08-22), decisión de estilo arquitectónico de la línea base | **No cumple** | No hay ADR de una restricción nueva; tiene alternativas, fuerzas, decisión y consecuencias muy completas, pero para el estilo base, no para un reto de S5. |
| 6. Cambio implementado extremo a extremo | El único commit funcional del periodo (`f6956ad`, "Primer prueba codigo") solo agrega recursos gráficos de splash screen de Android/Flutter (imágenes), sin lógica de negocio nueva | **No cumple** | No hay cambio de código que implemente una restricción nueva; todas las pruebas de `docs/aspectos.md` siguen "(pendiente)". |
| 7. Límites C4 conservados | `docs/c4/C4_L1_Context.md` y `C4_L2_Container.md` no cambiaron en el periodo | **No verificado** | No hay cambio que contrastar. |
| 8. Prueba que cubre el cambio, en verde en pipeline | `curl .../actions/runs`: los 3 runs disponibles (`07b36f40`, `d3be5145`, `4806374a`, incluido el commit calificado) están en **`failure`** | **No cumple** | El pipeline del estado calificado está en rojo, no en verde. |
| 9. Resultado contrastado con umbral | Sin medición ejecutada | **No cumple** | — |
| 10. Cadena de trazabilidad navegable | `docs/aspectos.md` tiene 8 columnas (`ID…Evidencia`) muy completas hasta Código, pero Pruebas y Evidencia = "(pendiente)"/"Pendiente" en las 4 filas | **No cumple** | La cadena se rompe sistemáticamente en Pruebas y Evidencia. |
| 11. Salida de IA con motivo técnico, de este corte | `docs/ia.md`: última sección fechada 2026-08-30 ("Sesión de trabajo con Claude Code"), sin ninguna entrada posterior; los commits de S5 (01/09) no tocan `docs/ia.md` | **No cumple** | Sin entrada referida a este corte. |
| 12. Sustentación del reto | — | **No verificado** | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| a. Repositorio en la organización, convención y público | Clon anónimo exitoso de `github.com/ISCOUTB/AS_202620_ElMapita` | **Cumple** | — |
| b. Estructura mínima | `git ls-tree` en `4806374`: `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` presentes | **Cumple** | — |
| c. Estado calificado identificable | Sin etiqueta; commit `4806374a`, `2026-09-01T08:39:54-06:00` | **No cumple** | Falta la etiqueta `corte-1`; existe solo un commit con ese texto como mensaje. |
| d. Nombres de ADR según convención | `docs/adr/0001-estilo-arquitectonico-propuesto.md` | **Cumple** | — |
| e. ADR aceptados no reescritos | Único ADR, estado "Accepted" desde su creación (2026-08-22), sin ediciones posteriores detectadas en el periodo de S5 | **Cumple** | — |
| f. `docs/ia.md` al día para la semana | Ver criterio 11 | **No cumple** | Sin entrada de S5. |
| g. Sin credenciales | `git grep` con la regex del contrato: coincidencias solo en nombres de campo (`password: string` en tipos TypeScript/Dart) y un token de ejemplo de badge (`abc123def456` en un README heredado de plantilla NestJS); ninguna es una credencial real | **Cumple** | Falsos positivos de la regex, revisados manualmente uno por uno. |
| h. Contribución de todos los integrantes | `git shortlog -sne 4806374`: RobotDRMX 12, Rodrigo Vazquez Rico 1, dgarza2705 (Diego Rosales Garza) 1 | **No cumple** | El equipo declara 3 integrantes (Angel Fabian Gutierrez Gomez, Diego Rosales Garza, Rodrigo Vazquez Rico); solo aparecen 2 identidades claramente atribuibles (Rodrigo, Diego) y una tercera (`RobotDRMX`, 12 de 14 commits = 86%) que EQUIPOS.md lista como handle del equipo pero sin nombre civil confirmado; Angel Fabian Gutierrez Gomez no tiene ningún commit identificable. |

## Estado global del proyecto (overall · HEAD)

HEAD no cambió desde el 2026-09-01 (`4806374a`): el equipo no volvió a tocar el repositorio en toda la ventana de S5 hasta el cierre. La documentación de línea base (ADR-0001, C4, aspectos.md, arc42) es notablemente detallada y bien escrita, pero **todo el código (pruebas, medición, servicios) sigue marcado como "(pendiente)"**, el pipeline de CI está en rojo en el commit calificado, y no hay ningún indicio de que se haya diagnosticado o respondido una restricción nueva.

## Nivel de rúbrica sugerido (propuesta al docente)

| Criterio | Nivel | Puntaje | Evidencia |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia | 0,00 | No se identifica una restricción nueva ni una línea base medida. |
| Alternativas y decisión | Sin evidencia del reto | 0,00 | El único ADR es el de estilo arquitectónico de la línea base. |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | El único commit del periodo agrega solo recursos gráficos de splash screen. |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | Pipeline en rojo; todas las pruebas y evidencias marcadas "(pendiente)". |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico verificable** | | **0,00 / 4,00** | La nota final la fija Moodle. |

## Recuento

**0 de 12 criterios Cumple.**

## No verificado

- PDF adjunto en Moodle.
- Coincidencia del diagnóstico con la restricción asignada (no disponible).
- Conservación de límites C4 (sin cambio que contrastar).
- Sustentación del reto.

## Hallazgos

- El equipo confundió un mensaje de commit (`corte-1`) con una etiqueta Git (`git tag`); no existe ninguna etiqueta en el repositorio.
- No hubo actividad en el repositorio entre el 2026-09-01 y el cierre (2026-09-07): la ventana completa de S5 quedó sin uso.
- El pipeline de CI está en **rojo** (`failure`) en los tres runs disponibles, incluido el commit calificado.
- La documentación (ADR, C4, aspectos) es de alta calidad narrativa, pero el código y las pruebas siguen "(pendiente)" en su totalidad.
- Contribución muy desbalanceada: un colaborador (`RobotDRMX`) concentra el 86% de los commits; un integrante declarado (Angel Fabian Gutierrez Gomez) no tiene commits identificables en el historial.
- Se sigue versionando un archivo temporal de Word (`docs/~$rteVertical_ElMapitaUTB.docx`), arrastrado de la revisión preliminar.

## Preguntas para la sustentación

1. ¿Por qué se usó un commit con el mensaje "corte-1" en vez de crear la etiqueta Git que exige la ficha, y a qué se debió que no hubiera ninguna actividad en el repositorio durante toda la semana 5?
2. ¿Cuál fue la restricción asignada, y qué evidencia (diagnóstico, ADR, medición) pueden mostrar que no esté en el repositorio?
3. ¿Por qué el pipeline de CI está en rojo en el commit que se presenta como entrega, y puede Angel Fabian Gutierrez Gomez mostrar su contribución al proyecto?
