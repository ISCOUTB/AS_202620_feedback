# Primer corte · reto de línea base arquitectónica · XALD

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión manual preliminar
> hecha antes del cierre (2026-09-03). Se repite sobre el estado admisible tras
> `2026-09-07T05:00:00Z`. A diferencia de la preliminar, esta vez **sí existe la etiqueta
> `corte-1`**: el equipo tuvo una actividad muy intensa el 2026-09-06, la noche previa al cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Etiqueta `corte-1` | **Presente** — `2861d8b66b56ba5287e77dd9176be1a9fe4f80f5`, 2026-09-06T22:50:12-05:00 (= 2026-09-07T03:50:12Z), anterior al cierre |
| HEAD (informativo) | `ee9af9c564682653ed26c4d7ecba36c567a279d7`, 2026-09-06T23:11:50-05:00 (= 2026-09-07T04:11:50Z) — 21 minutos después de la etiqueta, también antes del cierre; son 7 commits más de ajustes de trazabilidad en ADR, no evaluados como parte del corte |
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`, `git tag --list`, `git checkout corte-1`, `ls docs/adr`, lectura completa de los 6 ADR, `docs/aspectos.md`, `docs/ia.md`, `README.md`, workflow de CI, `find` de pruebas Kotlin, `git shortlog -sne corte-1`, `git grep` de credenciales, `git log --follow` de ADR 0001/0002, `curl` a la API de Actions (paginada), `git branch --contains` para confirmar la rama de disparo del CI |
| `correcciones-feedback-XALD.md` | Existe en la raíz (nombre distinto de `correcciones.md`, pero misma función); presente tanto en HEAD como en el estado etiquetado |

## Sobre `correcciones-feedback-XALD.md`

El equipo entregó un documento de corrección con ese nombre (no `correcciones.md`), fechado
2026-09-06. Se trata como lo que es: testimonio del equipo, verificado contra el repositorio, no
como hecho. Ver la sección "Correcciones del equipo" al final.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `2861d8b`, 2026-09-06T22:50:12-05:00, anterior al cierre | Cumple | Corrige la revisión preliminar: la etiqueta ya existe. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay PDF versionado en el estado etiquetado; Moodle fuera del alcance de este kit | No verificado | Debe comprobarse en Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | Los 6 ADR (`docs/adr/`) declaran restricciones (RT-01 Android, RT-03/RL-01 seguridad, RT-04 parsing, RO-01 organizacional), pero todas corresponden a restricciones de línea base ya documentadas en S2/S3, no a una restricción nueva asignada para S5; no se identifica un reto distinto | No cumple | No se pudo ubicar cuál fue la restricción **nueva** asignada al equipo para este corte, ni en el kit ni en el repositorio; lo que se hizo fue completar y endurecer las decisiones ya existentes. |
| Línea base medida y verificable antes del cambio | Ningún ADR ni `docs/aspectos.md` contiene una cifra medida (tiempo, tasa, conteo) con procedimiento; los commits "Enhance ADR with traceability and baseline details" añadieron enlaces de trazabilidad, no mediciones numéricas | No cumple | La palabra "baseline" en los mensajes de commit se refiere a enlaces, no a una medición. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Los ADR 0001-0006 sí tienen ahora "Opciones Evaluadas", fuerzas y consecuencias — nivel competente como documentación general — pero ninguno se presenta como la respuesta a una restricción nueva de este corte | No cumple | Buena documentación de las decisiones **existentes**, no evidencia de un ADR de reto S5. |
| Cambio implementado y ejecutable de extremo a extremo | Se agregó `backend_xald/` (Node.js, `index.js`/`package.json`) para alinear el código con el backend que el C4 ya declaraba; hubo endurecimiento de seguridad (`cleartextTraffic`, `dependencyLocking`, `isMinifyEnabled`); el "corte vertical" ejecutable (`Entornotest.kt`) es una prueba trivial (`assertTrue(true)`), no una demostración de los 5 módulos interactuando | No cumple | Hay cambios reales de calidad/estructura, pero no un cambio identificable como respuesta a un reto, y la prueba que se presenta como "corte vertical" no ejercita el flujo de datos entre módulos. |
| Límites declarados conservados tras el cambio | `backend_xald/` ahora existe en la raíz del repositorio, coherente con el Backend XALD declarado en el C4; corrige la divergencia que señaló la revisión preliminar | Cumple | Divergencia C4/código resuelta antes del cierre. |
| Prueba que cubre el cambio, en verde en el pipeline | El workflow de CI (`\.github/workflows/ci.yml`) solo dispara con push a las ramas `experimental` y `main`; el repositorio usa `master` como rama por defecto. La API de Actions no muestra ningún run para los commits del 2026-09-06 después de las 02:52 UTC, que incluyen la etiqueta `corte-1` (`2861d8b`) y todo lo posterior — ninguno disparó el pipeline | No cumple | El código fusionado sí se probó en verde en la rama `experimental` antes de fusionarse (runs previos exitosos), pero el estado etiquetado en sí no tiene un run de CI propio: el workflow no escucha la rama en la que realmente vive el proyecto. |
| Resultado contrastado con el umbral del escenario y reproducible | No se encontró ninguna medición con herramienta, carga y procedimiento contra un umbral de escenario | No cumple | Sin medición. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md` en el estado etiquetado: 4 de 5 filas (A-02 a A-05) tienen "*Pendiente*" en CÓDIGO, PRUEBAS y EVIDENCIA; la fila A-01 enlaza a código y pruebas, pero en la rama `experimental` (no en el estado etiquetado) y su celda EVIDENCIA también dice "*Pendiente*" | No cumple | Ninguna fila llega completa hasta evidencia dentro del propio estado calificado. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md`, última fila ("Resolución de Hallazgos y Calidad (SonarCloud)"): diagnóstico de vulnerabilidades, acciones tomadas (hardening del manifiesto, lockfiles, R8, refactor de pruebas) y justificación técnica ("Quality Gate Passed"); fila anterior también describe auditoría de entregables contra el feedback docente | Cumple | Entrada específica, técnica y fechada en la ventana final previa a la etiqueta; sí satisface el criterio para este corte. |
| Sustentación del reto | No verificable desde el repositorio | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `ISCOUTB/AS_202620_XALD` exitoso | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | `git ls-tree` en el estado etiquetado muestra `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md` | Cumple | Las seis rutas están presentes. |
| Estado calificado identificable | Etiqueta `corte-1` en `2861d8b`, anterior al cierre | Cumple | Corrige la revisión preliminar. |
| Nombres de ADR según la convención | `0001-patron-offline-first.md` … `0006-seleccion-de-estilo-arquitectonico.md` | Cumple | Los seis siguen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | `0002-parsing-hibrido.md` fue editado el 2026-08-30 (`4ca7f92`) después de su renombre/aceptación previa, sin declarar reemplazo; ADR 0001 también reescrito en su historial de agosto | No cumple | Persiste desde la revisión preliminar: las ediciones posteriores a la aceptación no se registran como reemplazo. |
| `docs/ia.md` al día para la semana | Última entrada fechada en la ventana de commits del 2026-09-06 (SonarCloud, auditoría de entregables) | Cumple | Corrige la revisión preliminar: sí hay registro de la semana del corte. |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE …` sobre el estado etiquetado: sin coincidencias; `.env` no versionado | Cumple | Sin hallazgos. |
| Contribución de todos los integrantes | `git shortlog -sne corte-1`: dilanbejarano011 (118), colmenares2007-crypto (77), xaviergarciadiaz20-commits (48), axeljruiz717-hash (30) — las cuatro cuentas de `EQUIPOS.md` | Cumple | Los cuatro integrantes con contribución sustancial y visible. |

## Estado global del proyecto en HEAD

- HEAD (`ee9af9c`) está 21 minutos después de la etiqueta, con 7 commits más que solo ajustan formato y enlaces de trazabilidad en los ADR — no cambian la evaluación del corte.
- El equipo tuvo una actividad de desarrollo muy concentrada el 2026-09-06 (decenas de commits desde media mañana hasta minutos antes del cierre): completó las secciones "Opciones evaluadas" de los seis ADR, alineó el código con el backend declarado en el C4, aplicó correcciones de seguridad reportadas por SonarCloud y actualizó el registro de IA.
- Pese a esa actividad, **no se identifica una restricción nueva asignada ni una respuesta de reto propiamente dicha**: el trabajo consistió en madurar y corregir la arquitectura ya declarada en semanas anteriores, no en diagnosticar-decidir-implementar frente a algo nuevo.
- El pipeline de CI solo se dispara en la rama `experimental`; los commits de la noche del cierre (incluida la etiqueta) se hicieron directamente y no dispararon ningún run.

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Insuficiente | 0,00 | No se identifica una restricción nueva ni su línea base medida. |
| Alternativas y decisión | Insuficiente | 0,00 | Los ADR mejorados son de restricciones preexistentes, no de un reto nuevo. |
| Aplicación sobre el corte vertical | Básico | 0,60 | Hay cambios reales (backend alineado con C4, hardening de seguridad) que funcionan de forma parcial, pero no como respuesta a un reto identificado, y la prueba de "corte vertical" es trivial. |
| Pruebas, medición y trazabilidad | Insuficiente | 0,00 | `docs/aspectos.md` sigue con celdas "Pendiente"; sin medición contra umbral; CI no cubre el estado etiquetado. |
| Sustentación del reto | Pendiente del docente | — | No verificable desde el repositorio. |
| **Subtotal técnico** |  | **0,60 / 4,00** | Propuesta al docente; no es la nota final. |

## Recuento

3 de 12 criterios de la ficha cumplen (etiqueta, límites C4 conservados, registro de IA). En la matriz transversal: 7 de 8 cumplen.

## No verificado

- PDF de dos páginas en Moodle.
- Sustentación del reto.
- Estado real del panel de SonarCloud (solo se pudo contrastar contra los mensajes de commit y `docs/ia.md`, no contra el dashboard).

## Hallazgos

- La etiqueta `corte-1` ya existe y apunta a un commit anterior al cierre — corrige el hallazgo principal de la revisión preliminar.
- No se identifica una restricción nueva asignada ni una respuesta de reto: el trabajo del 2026-09-06 consistió en madurar la documentación y el código ya existentes (ADR con alternativas, backend alineado con C4, hardening de seguridad), no en diagnosticar y resolver algo nuevo.
- El pipeline de CI no se dispara en la rama por defecto (`master`), solo en `experimental`; el estado etiquetado no tiene un run de CI propio, aunque el código que lo compone sí se probó en verde antes de fusionarse.
- `docs/aspectos.md` sigue con la mayoría de sus celdas de código, pruebas y evidencia en "*Pendiente*" en el estado etiquetado.
- El "corte vertical ejecutable" que cita el README se apoya en una prueba trivial (`assertTrue(true)`), no en una demostración real de los cinco módulos interactuando.
- Persisten ediciones de ADR después de su aceptación sin declarar reemplazo (hallazgo repetido desde S3/S4).
- Contribución de los cuatro integrantes claramente visible y sustancial.

## Correcciones del equipo

El repositorio incluye `correcciones-feedback-XALD.md` (nombre distinto de `correcciones.md`,
misma función), fechado 2026-09-06. Se adjudica cada punto verificable contra el estado
etiquetado (no contra las afirmaciones del documento):

| Corrección | Adjudicación | Justificación |
|---|---|---|
| "Semanas 1 a 3: todos los hallazgos están resueltos" (ADR renombrados, arc42 completo, C4 con leyenda, aspectos.md navegable) | Aceptada parcialmente | Los ADR sí siguen la convención de nombres y arc42 tiene contenido sustancial (objetivos, restricciones, escenarios); pero `docs/aspectos.md` en el estado etiquetado **todavía** tiene la mayoría de sus celdas de código/pruebas/evidencia en "Pendiente", contra lo que afirma el documento. |
| "4.1 — Requisitos de S4 sí estaban entregados a tiempo; el calificador automático falló, no la entrega" | No verificable en esta revisión | No se tuvo acceso al estado exacto evaluado por la revisión de S4 en este ejercicio (fuera del alcance de esta revisión de corte 1); se anota para que el docente lo contraste con la revisión de S4 archivada. |
| "4.2 — El Backend es un despliegue independiente de la app Android; la ausencia de carpeta de backend era coherente con esa separación, y se creará la estructura antes del cierre" | Aceptada | Verificado: `backend_xald/` existe en el estado etiquetado (`corte-1`), con `index.js` y `package.json`; la corrección prometida sí se aplicó antes del cierre. La divergencia original que señaló la revisión preliminar (código sin backend pese al C4) queda resuelta. |
| "4.3 — El corte vertical sí ejecuta los cinco módulos con dobles de prueba, contra lo que reportó el calificador" | Rechazada | La única prueba nueva relevante (`XALDAPP/app/src/test/java/com/proyecto/xald/Entornotest.kt`) es `assertTrue(sistemaConfigurado)` con `sistemaConfigurado = true`: no ejercita ningún flujo de datos entre módulos ni usa dobles de prueba. No se encontró otra prueba que demuestre la interacción de los cinco módulos. |
| "4.4 — Los ADR se completarán con opciones evaluadas antes del cierre del corte 1" | Aceptada | Verificado en el estado etiquetado: los seis ADR (`0001`-`0006`) tienen sección "Opciones Evaluadas" con alternativas descartadas y su motivo. |
| "4.5 — El pipeline no tenía análisis estático porque la organización no había habilitado SonarCloud hasta el 2026-09-05; se integrará con el commit final" | Aceptada con reserva | Hay evidencia circunstancial fuerte: varios commits del 2026-09-06 corrigen hallazgos típicos de SonarCloud (`cleartextTraffic`, `dependencyLocking`, minificación, nombres de prueba) y `docs/ia.md` describe el resultado como "Quality Gate Passed". No se pudo confirmar directamente en el dashboard de SonarCloud (fuera del alcance de este kit). |

## Preguntas para la sustentación

- ¿Cuál fue la restricción nueva asignada para este corte? Todo lo documentado en los ADR corresponde a restricciones ya declaradas en semanas anteriores.
- ¿Dónde está la línea base medida (cifra + procedimiento) de esa restricción, antes de cualquier cambio?
- La prueba `Entornotest.kt` solo verifica `true == true`: ¿dónde está la prueba que demuestra que los cinco módulos (`app`, `parser`, `corefinanciero`, `syncqueue`, `aigemini`) intercambian datos de extremo a extremo?
- ¿Por qué el workflow de CI dispara solo en `experimental`/`main` y no en `master`, que es la rama donde vive el estado etiquetado?
- ¿Pueden mostrar el panel de SonarCloud con el resultado "Quality Gate Passed" que menciona `docs/ia.md`?
