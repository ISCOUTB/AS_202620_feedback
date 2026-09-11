# semana-05-corte1 · XALD

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `9bf16cf` en `origin/master` (2026-09-09T10:07:09-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/master, hash 9bf16cf989667977ff8afe95311a595a66517318, fecha 2026-09-09T10:07:09-05:00 (anterior al cierre 2026-09-10T17:00:00Z) | Cumple | El commit calificado existe y es anterior al cierre. |
| correcciones.md existe en la raíz del estado calificado | git show 9bf16cf:correcciones.md presente en el árbol del hash calificado | Cumple | Archivo en la raíz con el nombre exacto. |
| Correcciones trazables y contrastadas | correcciones.md responde a hallazgos S1-S4 pero varias respuestas no se sustentan: 4.1 y 4.3 se declaran 'sin acción' y 4.5 queda pendiente de SonarCloud; no hay run de SonarCloud citado | No cumple | Faltan enlaces a commits/pruebas para verificar cada corrección; la tabla de seguimiento no está completa. |
| S1 al día: equipo, problema y repositorio | docs/ficha del problema.md describe problema, usuarios, alcance y tensiones; README.md describe el proyecto; autores en historial: 126 dilanbejarano011, 77 colmenares2007-crypto, 48 xaviergarciadiaz20-commits, 31 axeljruiz717-hash | Cumple | Equipo visible y problema documentado. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/arc42-template-EN.md secciones Architecture Constraints y Quality Goals con RT-01 a RT-05, RO-01/02, RL-01 y escenarios ESC-01 a ESC-05 | Cumple | Restricciones y escenarios presentes y enlazados desde docs/aspectos.md. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001 a 0006 con contexto, opciones evaluadas, decisión, consecuencias y trazabilidad; docs/matriz-comparativa-estilos.md documenta alternativas | Cumple | Decisiones documentadas y alineadas con la estrategia. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-EN.md con secciones 1-12; docs/c4/c1.md, c2.md y c4.md con diagramas Mermaid; XALDAPP/app/src/test/java/com/proyecto/xald/Cortevertical.kt y Entornotest.kt | Cumple | Documentación y pruebas del corte vertical presentes en el hash calificado. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta comando .\XALDAPP\gradlew.bat -p XALDAPP test; run Android CI 34368132945 success del 2026-09-09T15:07:12Z asociado al hash calificado | Cumple | El comando de arranque y prueba está documentado y el run respalda la ejecución. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml ejecuta ./gradlew testDebugUnitTest; run Android CI 34368132945 success (2026-09-09T15:07:12Z) posterior al hash calificado | Cumple | Pipeline en verde para el estado calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md tiene filas A-02 a A-05 con CÓDIGO, PRUEBAS y EVIDENCIA en 'Pendiente'; A-01 enlaza a rama experimental en lugar del hash calificado | No cumple | La tabla de aspectos no es navegable de extremo a extremo en el estado calificado. |
| PDF u otro adjunto exigido por el aula | No hay PDF en el repositorio (docs/.gitignore excluye *.pdf) y no se dispone del adjunto de Moodle | No verificado | Se requiere el documento entregado en el aula para verificar. |
| Sustentación del corte | No hay evidencia de sesión de sustentación en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repositorio ISCOUTB/AS_202620_XALD visible, nombre coincide con AS_202620_<PROYECTO>; historial con 4 autores | Cumple | Cumple organización, nombre y visibilidad. |
| Estructura mínima | árbol del hash 9bf16cf contiene README.md, docs/arc42/, docs/adr/ con 6 ADR, docs/c4/, docs/aspectos.md y docs/ia.md | Cumple | Estructura mínima presente en la raíz. |
| Estado del repositorio que se califica | rama origin/master, hash 9bf16cf 2026-09-09T10:07:09-05:00, anterior al cierre 2026-09-10T17:00:00Z; sin commits posteriores | Cumple | Estado calificado identificado correctamente. |
| Convenciones de ADR | docs/adr/ contiene 0001-patron-offline-first.md a 0006-seleccion-de-estilo-arquitectonico.md con nombres en kebab-case y contenido con contexto, opciones, decisión, consecuencias y trazabilidad | Cumple | Nombres y contenido cumplen la convención. |
| Tabla de aspectos | docs/aspectos.md filas A-02 a A-05 tienen CÓDIGO, PRUEBAS y EVIDENCIA en 'Pendiente'; A-01 enlaza a rama experimental | No cumple | Filas con huecos no navegables en el estado calificado. |
| Registro de uso de IA | docs/ia.md con tabla de usos, herramienta, decisión del estudiante y justificación; historial con 6 commits entre 2026-08-07 y 2026-09-06 | Cumple | Registro presente y con evolución en el tiempo. |
| README | README.md describe qué es el sistema, comando de arranque .\XALDAPP\gradlew.bat -p XALDAPP test y salida esperada | Cumple | Arranque y prueba documentados con un comando. |
| Pipeline y análisis estático | .github/workflows/ci.yml solo ejecuta testDebugUnitTest; no hay configuración ni run de SonarCloud citado; correcciones.md 4.5 declara la integración pendiente | No cumple | Falta análisis estático en el pipeline. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `9bf16cf989667977ff8afe95311a595a66517318 2026-09-09T10:07:09-05:00 Change CI branches from 'main' to 'master'`
- **Veredicto**: con pendientes
- Resumen: El proyecto entero a HEAD (9bf16cf, sin commits posteriores) mantiene la documentación S1-S4 y el corte vertical en verde, pero arrastra pendientes de semanas anteriores: trazabilidad incompleta en docs/aspectos.md y análisis estático ausente del pipeline.

Pendientes que siguen abiertos:
- Completar columnas CÓDIGO, PRUEBAS y EVIDENCIA en docs/aspectos.md.
- Corregir enlaces de docs/aspectos.md que apuntan a la rama experimental.
- Integrar y evidenciar SonarCloud en el pipeline.
- Contrastar cada corrección de correcciones.md con commit o run específico.

## Recuento y nota sugerida

8 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.7 = 1 + 4 × (8/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula: no disponible en el repositorio; se requiere el adjunto de Moodle.
- Sustentación del corte: sin evidencia; depende de la sesión del docente.

## Hallazgos para la planilla

- correcciones.md no contrasta cada hallazgo con commit o run específico; 4.1 y 4.3 se responden sin acción verificable.
- docs/aspectos.md deja CÓDIGO, PRUEBAS y EVIDENCIA en 'Pendiente' para A-02 a A-05.
- A-01 en docs/aspectos.md enlaza a la rama experimental, no al hash calificado.
- Pipeline sin análisis estático: no hay SonarCloud configurado ni run que lo respalde.
- correcciones.md 4.5 reconoce que la integración de SonarCloud quedó pendiente de ejecutar.
- No hay evidencia del PDF adjunto en Moodle en el repositorio.
- Sustentación del corte sin evidencia en el repositorio.
