# semana-05-corte1 · XALD

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `9a75929` (2026-08-31T18:20:56-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Hash calificado 9a75929 (2026-08-31T18:20:56-05:00) anterior al cierre; la evidencia no incluye salida de `git tag --list` ni `git log -1 corte-1`. | No verificado | Se necesita confirmar la existencia de la etiqueta; si falta, la fila de versionado transversal sería No cumple. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | docs/.gitignore excluye *.pdf; no hay adjunto en el repositorio. | No verificado | El PDF se entrega en Moodle; no accesible desde la evidencia del repositorio. |
| Impacto de la restricción localizado en requisitos, C4 y código | No se conoce la restricción asignada al equipo; docs/adr/0003-restriccion-os.md aborda una restricción de plataforma sin diagnóstico con línea base. | No verificado | Sin la restricción asignada no se puede juzgar si el diagnóstico localiza lo que debía. |
| Línea base medida y verificable antes del cambio | No se halló en el repositorio una cifra con herramienta y procedimiento; docs/aspectos.md mantiene celdas 'Pendiente'. | No verificado | Podría estar en el PDF de Moodle; no verificable desde el repositorio. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/ contiene 6 ADR; ninguno incluye alternativas, fuerzas y trazabilidad completas (p.ej. 0003 solo contexto/decisión/consecuencias). | No verificado | No se identifica cuál es el ADR del reto sin la restricción asignada. |
| Cambio implementado y ejecutable de extremo a extremo | README.md documenta arranque con `gradlew.bat -p XALDAPP test`; runs_ci en verde; el head es 'Update 0002-parsing-hibrido.md' (documentación). | No verificado | No se distingue un commit que implemente el cambio del reto sobre el corte vertical. |
| Límites declarados conservados tras el cambio | docs/c4/c4.md declara 5 módulos y Backend XALD; el código tiene 5 módulos Gradle sin backend. | No verificado | Sin identificar el cambio del reto no se puede verificar la conservación de límites. |
| Prueba que cubre el cambio, en verde en el pipeline | runs_ci 'Android CI' success (https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/33352959352, 2026-08-31T03:10:13Z); existe XALDAPP/app/src/test/java/com/proyecto/xald/Cortevertical.kt. | No verificado | Hay runs en verde, pero no se sabe si la prueba cubre el cambio del reto. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay en el repositorio una medición con herramienta, carga y procedimiento. | No verificado | Depende del PDF o de arc42 sección 10; no verificable desde el repo. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md fila A-01 tiene Evidencia '*Pendiente*'; filas A-02 a A-05 tienen Código/Pruebas/Evidencia '*Pendiente*'. | No cumple | La cadena se rompe en la celda de evidencia; una fila con huecos no se puede defender. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md registra usos con decisión y justificación técnica; entradas de 2026-08-30 (hash 0d98e74) sobre corte vertical, CI y diagramas. | Cumple | Incluye aceptación, corrección y rechazo con motivos técnicos. |
| Sustentación del reto | La sustentación se resuelve en sesión. | No verificado | Lo fija el docente; no verificable desde el repositorio. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_XALD visible y público; 4 identidades de git en el historial: xaviergarciadiaz20-commits, dilanbejarano011, colmenares2007-crypto, axeljruiz717-hash. | Cumple | Coinciden en número con los integrantes declarados; sin atribución por nombre. Sección 1 del contrato. |
| Estructura mínima | Existen docs/arc42/, docs/adr/ (6 ADR), docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Hay archivos adicionales y docs/c4/c4.md duplica C1/C2; no es ausencia. Sección 2 del contrato. |
| Versionado y estado calificado | Hash calificado 9a75929 anterior al cierre; sin confirmación de la etiqueta corte-1. | No verificado | Si la etiqueta no existe, esta fila sería No cumple. Sección 3 del contrato. |
| Convenciones de ADR | Los nombres de ADR siguen el patrón NNNN-kebab-case, pero ningún ADR incluye la trazabilidad (requisito, C4, commit, pruebas) exigida. | No cumple | Sección 4 del contrato: contexto, opciones, decisión, consecuencias y trazabilidad. |
| Tabla de aspectos | docs/aspectos.md tiene celdas 'Pendiente' en Código/Pruebas/Evidencia (A-02 a A-05) y Evidencia en A-01. | No cumple | Una fila con huecos no se puede defender. Sección 5 del contrato. |
| Registro de uso de IA | docs/ia.md con entradas de 2026-08-30 (hash 0d98e74) y motivos técnicos de aceptación/rechazo. | Cumple | Crece a lo largo del semestre. Sección 6 del contrato. |
| README y reproducibilidad | README.md describe el sistema, el comando de arranque y la prueba; runs_ci 'Android CI' success. | Cumple | Requisitos previos declarados (JDK 17, Android SDK). Sección 7 del contrato. |
| Pipeline, análisis estático y secretos | .github/workflows/ci.yml ejecuta testDebugUnitTest y los runs están en verde; no hay configuración de SonarCloud; sin coincidencias de secretos. | No cumple | El contrato sección 8 pide análisis estático en SonarCloud; no se evidencia en el repo. Secciones 8 y 9 del contrato. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `9a759298810af932171c50a63e2121529a26b2bf 2026-08-31T18:20:56-05:00 Update 0002-parsing-hibrido.md`
- **Veredicto**: con pendientes
- Resumen: Proyecto con estructura, CI y registro de IA en orden, pero la respuesta al reto no es verificable desde el repositorio y persisten huecos de trazabilidad y ADR sin formato completo.

Pendientes que siguen abiertos:
- Confirmar o crear la etiqueta corte-1 sobre el commit evaluado.
- Completar las celdas Pendiente de docs/aspectos.md.
- Añadir trazabilidad (requisito, C4, commit, pruebas) a los ADR.
- Configurar análisis estático SonarCloud en el pipeline.
- Entregar el PDF con diagnóstico, decisión, cambio, medición y trazabilidad.

## Recuento y nota sugerida

1 de 12 criterios Cumple.

## No verificado / pendientes

- Etiqueta corte-1: falta salida de git tag --list y git log -1 corte-1.
- PDF de dos páginas: adjunto en Moodle no disponible en la evidencia.
- Restricción asignada: no proporcionada; impide juzgar diagnóstico, ADR del reto y cambio.
- Línea base y medición: no están en el repositorio; posiblemente en el PDF.
- Prueba del cambio: hay runs verdes pero no se identifica el cambio del reto.

## Hallazgos para la planilla

- No se confirmó la existencia de la etiqueta corte-1 en la evidencia proporcionada.
- docs/aspectos.md mantiene celdas 'Pendiente' en la fila A-01 y en A-02 a A-05.
- Ningún ADR incluye la trazabilidad exigida (requisito, C4, commit, pruebas).
- El workflow de CI no ejecuta análisis estático SonarCloud.
- No hay en el repositorio un diagnóstico del reto con línea base medida ni medición contra umbral.
- El C4 declara un Backend XALD sin código correspondiente en el árbol.
