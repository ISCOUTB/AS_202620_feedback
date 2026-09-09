# semana-05-corte1 · XALD

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `ee9af9c` (2026-09-06T23:11:50-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | Rama master con hash ee9af9c del 2026-09-06T23:11:50-05:00, anterior al cierre 2026-09-07T05:00:00Z (evidencia: arbol del repo y commits). | Cumple | Hay commits posteriores al cierre pero la matriz se fija en el hash calificado. |
| correcciones.md existe en la raíz del estado calificado | En el hash ee9af9c el árbol contiene 'correcciones-feedback-XALD.md', no 'correcciones.md' (evidencia: arbol del estado calificado). | No cumple | El nombre exacto exigido solo aparece en HEAD tras el commit 43b8e35 posterior al cierre. |
| Correcciones trazables y contrastadas | El archivo de correcciones del estado calificado no tiene la ruta/nombre exigido, por lo que no hay índice contrastable en raíz (evidencia: arbol ee9af9c y diff_desde_cierre). | No cumple | No se puede verificar trazabilidad completa sin el archivo con nombre correcto en el estado calificado. |
| S1 al día: equipo, problema y repositorio | docs/ficha del problema.md plantea problema, usuarios, alcance y tensiones; README.md describe la app; historial con 4 autores (evidencia: documentos y autores). | Cumple | Repositorio público en ISCOUTB y los integrantes aparecen en el historial. |
| S2 al día: escenarios de calidad y restricciones | arc42-template-EN.md incluye Quality Goals (ESC-01..05) y Architecture Constraints (RT-01..05, RO-01/02, RL-01); ADR 0001-0006 referencian escenarios y restricciones (evidencia: documento arc42 y ADR). | Cumple | Escenarios formulados con partes medibles referidas a la sección 10. |
| S3 al día: estrategia de solución y decisiones | docs/matriz-comparativa-estilos.md y docs/adr/0006-seleccion-de-estilo-arquitectonico.md adoptan Monolito Modular; ADR 0001-0005 documentan offline-first, parsing híbrido, Android, seguridad y alcance MVP (evidencia: documentos ADR y matriz). | Cumple | El ADR-0005 queda declarado 'En revisión', lo cual es una decisión de alcance documentada. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-EN.md contiene secciones; docs/c4/c4.md con C1 y C2; XALDAPP/app/src/test/java/com/proyecto/xald/Cortevertical.kt y README documentan el corte (evidencia: documentos y arbol). | Cumple | No hay nivel C3/C4 de código, pero la ficha pide arc42, C4 y corte vertical, no un nivel específico. |
| Corte vertical reproducible y coherente con la arquitectura | README.md da comando único con JAVA_HOME/ANDROID_HOME; prueba Cortevertical.kt existe y CI corre con éxito antes del cierre (evidencia: runs_ci 34077698416 y README). | Cumple | El corte vertical recorre módulos :app, :parser, :corefinanciero, :syncqueue y :aigemini descritos en C2. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml ejecuta ./gradlew testDebugUnitTest; runs success del 2026-09-07T01:48-02:51Z anteriores al cierre (evidencia: runs_ci). | Cumple | En el hash calificado el workflow apunta a experimental/main; en HEAD se corrige a master (9bf16cf), sin afectar esta matriz. |
| Trazabilidad consolidada navegable | docs/aspectos.md deja CÓDIGO, PRUEBAS y EVIDENCIA en '*Pendiente*' para A-02..A-05 y enlaza a blob/experimental, no al hash calificado (evidencia: docs/aspectos.md). | No cumple | Faltan eslabones navegables desde aspecto hasta código, pruebas y evidencia. |
| PDF u otro adjunto exigido por el aula | No hay evidencia del adjunto de Moodle en el repositorio (evidencia: sin dato adjunto). | No verificado | Se requiere el documento entregado en Moodle para poder verificar la fila. |
| Sustentación del corte | No hay acta ni registro de sustentación en el repositorio. | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio (organización, nombre, visibilidad, integrantes) | Repositorio AS_202620_XALD visible en ISCOUTB y shortlog con 4 autores: xaviergarciadiaz20-commits, dilanbejarano011, colmenares2007-crypto, axeljruiz717-hash (evidencia: autores). | Cumple | No se atribuyen cuentas por parecido de nombre; se citan los nombres visibles. |
| Estructura mínima (README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md) | Árbol del estado calificado contiene README.md, docs/arc42/arc42-template-EN.md, docs/adr/0001..0006, docs/c4/c1.md, c2.md y c4.md, docs/aspectos.md y docs/ia.md (evidencia: arbol ee9af9c). | Cumple | Hay archivos adicionales que no obstruyen la estructura mínima. |
| Qué estado se califica (último commit de master/main anterior al cierre) | Hash ee9af9c en rama master, 2026-09-06T23:11:50-05:00, anterior al cierre 2026-09-07T05:00:00Z (evidencia: hash y fecha). | Cumple | La rama master es la principal y contiene el estado calificado. |
| Convenciones de ADR (un archivo por decisión, numeración, título decidido, no reescritura, trazabilidad) | docs/adr contiene 0001-patron-offline-first.md .. 0006-seleccion-de-estilo-arquitectonico.md con nombres kebab-case y trazabilidad; commits 2026-09-06T23:11 agregan trazabilidad (evidencia: arbol y commits ee9af9c, 41c803f, 9e642d3). | Cumple | No se evidencia reescritura de un ADR aceptado; el 0005 está declarado 'En revisión'. |
| docs/ia.md (registro de uso de IA con aceptado/rechazado y motivo) | docs/ia.md incluye tabla con etapa, contribución, decisión y justificación, con rechazos explícitos; historial con 6 commits (evidencia: ia_log y documento). | Cumple | Se documenta el criterio del equipo al rechazar propuestas de la IA. |
| README (qué es, arranque con un solo comando, cómo se prueba) | README.md explica el proyecto y da comandos de arranque y prueba con .\gradlew.bat test y salida esperada (evidencia: README.md). | Cumple | El comando requiere variables de entorno JAVA_HOME/ANDROID_HOME, pero el propio README las declara. |
| Pipeline y análisis estático (CI en cada push; SonarCloud desde segundo corte) | En el estado calificado .github/workflows/ci.yml corre solo para ramas 'experimental' y 'main', no para 'master'; no hay evidencia de SonarCloud (evidencia: ci.yml y runs_ci). | No cumple | El pipeline pasa en runs_ci pero no se dispara en master hasta el commit posterior 9bf16cf; falta SonarCloud. |
| Secretos (ninguna credencial en el repo; .env no versionado) | Búsqueda de patrones de credenciales sin coincidencias y sin archivos .env versionados (evidencia: secretos y envs_versionados). | Cumple | Resultado esperado: no hay secretos en el hash calificado. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `9bf16cf989667977ff8afe95311a595a66517318 2026-09-09T10:07:09-05:00 Change CI branches from 'main' to 'master'`
- **Veredicto**: con pendientes
- Resumen: A HEAD el repositorio contiene los artefactos nucleares (arc42, ADR, C4, corte vertical, CI exitoso y correcciones.md ya renombrado), pero la entrega calificada no cumplía el nombre exacto correcciones.md ni lo resolvió antes del cierre; quedan pendientes de trazabilidad en aspectos.md y de CI sobre master en el estado calificado.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- correcciones-feedback-XALD.md renombrado a correcciones.md en 43b8e35 (2026-09-08T10:25:05-05:00), posterior al cierre.
- Workflow de CI ajustado a la rama master en 9bf16cf (2026-09-09T10:07:09-05:00), posterior al cierre; run success 2026-09-09T15:07:12Z.

Pendientes que siguen abiertos:
- Completar CÓDIGO, PRUEBAS y EVIDENCIA en docs/aspectos.md con enlaces al estado calificado.
- Incorporar análisis estático SonarCloud.
- Verificar entrega del PDF en Moodle y sustentación.

## Recuento y nota sugerida

7 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula: requiere el documento entregado en Moodle, no disponible en el repositorio.
- Sustentación del corte: requiere la sesión de sustentación.
- Correcciones trazables en correcciones.md en estado calificado: no se pudo verificar por ausencia del archivo con el nombre/ruta exigido.

## Hallazgos para la planilla

- En el hash calificado ee9af9c no existe correcciones.md; el archivo se llama correcciones-feedback-XALD.md y solo se renombra tras el cierre (43b8e35).
- docs/aspectos.md deja CÓDIGO, PRUEBAS y EVIDENCIA en pendiente para A-02 a A-05, y enlaza a blob/experimental en vez del hash calificado.
- El workflow del estado calificado escucha experimental/main, no master; en HEAD se corrige con 9bf16cf.
- No se evidencia integración con SonarCloud en el repositorio.
- Correcciones y ajuste de CI subidos después del cierre: rename a correcciones.md (43b8e35) y cambio de ramas del workflow (9bf16cf).
- Commits posteriores al cierre (no calificados): 9bf16cf 2026-09-09T10:07:09-05:00 Change CI branches from 'main' to 'master'; 43b8e35 2026-09-08T10:25:05-05:00 Rename correcciones-feedback-XALD.md to correcciones.md
