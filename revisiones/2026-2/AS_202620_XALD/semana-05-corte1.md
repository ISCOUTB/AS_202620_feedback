# semana-05-corte1 · XALD

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `ee9af9c` en `origin/master` (2026-09-06T23:11:50-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master ee9af9c 2026-09-06T23:11:50-05:00 (04:11:50Z), anterior al cierre 2026-09-07T05:00:00Z | Cumple | Rama principal master identificada; sin etiquetas. |
| correcciones.md existe en la raíz del estado calificado | Árbol de ee9af9c contiene correcciones-feedback-XALD.md, no correcciones.md; renombrado en 43b8e35 (post cierre) | No cumple | El nombre exacto exigido no existe en el hash calificado. |
| Correcciones trazables y contrastadas | Sin correcciones.md en ee9af9c no hay índice trazable de hallazgos S1-S4 | No cumple | El archivo con nombre incorrecto no cumple la especificación y no fue contrastable. |
| S1 al día: equipo, problema y repositorio | docs/ficha del problema.md, README.md, shortlog con 4 autores, repo ISCOUTB/AS_202620_XALD público | Cumple | Problema, usuarios y alcance documentados; integrantes en historial. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/arc42-template-EN.md con Architecture Constraints (RT-01..05, RO-01..02, RL-01) y Quality Goals (ESC-01..05) | Cumple | Restricciones y escenarios medibles presentes. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001..0006, docs/matriz-comparativa-estilos.md, ADR-0006 adopta monolito modular | Cumple | Decisiones con contexto, opciones, consecuencias y trazabilidad. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-EN.md, docs/c4/c1.md, c2.md, c4.md, XALDAPP/app/src/test/java/com/proyecto/xald/Cortevertical.kt existen | No verificado | No se pudo comprobar que arc42 contenga las 12 secciones completas en ee9af9c; falta la matriz S4 para contrastar. |
| Corte vertical reproducible y coherente con la arquitectura | README.md con comandos gradlew test; Cortevertical.kt; run Android CI 34077698416 success | Cumple | Los 5 módulos Gradle coinciden con C2; el corte vertical está documentado y probado. |
| Pipeline y pruebas respaldan el estado calificado | runs_ci Android CI success 2026-09-07T02:51:58Z (https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/34077698416) | Cumple | Runs anteriores al cierre en verde; sin embargo ci.yml en ee9af9c no incluía master (corregido en 9bf16cf post cierre). |
| Trazabilidad consolidada navegable | docs/aspectos.md con celdas 'Pendiente' en Código/Pruebas/Evidencia para A-02 a A-05; enlaces a rama experimental | No cumple | Huecos en la cadena aspecto-requisito-C4-ADR-código-pruebas-evidencia. |
| PDF u otro adjunto exigido por el aula | Sin evidencia del PDF en Moodle en los datos del repositorio | No verificado | La ficha indica No verificado si no está disponible. |
| Sustentación del corte | Sesión de sustentación no evaluable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_XALD visible; shortlog con 4 autores | Cumple | Nombre y organización correctos; integrantes en historial. |
| Estructura mínima | Árbol con README.md, docs/arc42/, docs/adr/ (6), docs/c4/, docs/aspectos.md, docs/ia.md | Cumple | README incluye arranque con un comando y requisitos. |
| Convenciones de ADR | docs/adr/0001..0006 con nombres kebab-case y contenido contexto/opciones/decisión/consecuencias/trazabilidad | Cumple | ADR-0005 en revisión, sin aspecto asociado, declarado explícitamente. |
| La tabla de aspectos | docs/aspectos.md: A-02 a A-05 con Código/Pruebas/Evidencia 'Pendiente'; enlaces a blob/experimental | No cumple | Filas con huecos no defendibles según el contrato. |
| Registro de uso de IA | docs/ia.md con tabla de usos, rechazos y justificaciones; log con 6 commits | Cumple | Incluye decisiones de rechazo con motivo técnico. |
| Pipeline y análisis estático | .github/workflows/ci.yml en ee9af9c escucha branches experimental/main, no master; corregido en 9bf16cf post cierre | No cumple | No se ejecutaba CI en cada push a la rama principal al cierre. |
| Secretos | git grep sin coincidencias; sin .env versionados | Cumple | Sin credenciales en el estado calificado. |
| Autoría y colaboración | shortlog: 125, 77, 48, 30 commits distribuidos entre 4 autores | Cumple | Actividad repartida a lo largo del semestre. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `9bf16cf989667977ff8afe95311a595a66517318 2026-09-09T10:07:09-05:00 Change CI branches from 'main' to 'master'`
- **Veredicto**: con pendientes
- Resumen: El primer corte tiene una base sólida (ADRs, C4, corte vertical, CI en verde), pero el archivo de correcciones no cumplía el nombre exacto al cierre y la trazabilidad de aspectos tiene huecos.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 43b8e35 (2026-09-08) renombra correcciones-feedback-XALD.md a correcciones.md, cerrando la fila 2 después del cierre
- 9bf16cf (2026-09-09) ajusta CI a la rama master, cerrando el pipeline transversal después del cierre

Pendientes que siguen abiertos:
- docs/aspectos.md con celdas Pendiente en Código/Pruebas/Evidencia para A-02 a A-05
- Enlaces de aspectos.md a rama experimental en lugar de master
- Completitud de arc42 (12 secciones) sin verificar
- PDF en Moodle y sustentación pendientes de confirmación docente

## Recuento y nota sugerida

6 de 12 criterios Cumple.

## No verificado / pendientes

- S4 al día: completitud de arc42 (12 secciones) no comprobada en ee9af9c
- PDF adjunto en Moodle no disponible en la evidencia
- Sustentación del corte: la resuelve el docente

## Hallazgos para la planilla

- correcciones.md ausente en ee9af9c; solo existía correcciones-feedback-XALD.md
- Renombrado a correcciones.md ocurrió después del cierre (43b8e35)
- Workflow CI en ee9af9c no incluía la rama master; corregido en 9bf16cf post cierre
- docs/aspectos.md con celdas Pendiente en Código, Pruebas y Evidencia para A-02 a A-05
- Enlaces de aspectos.md apuntan a la rama experimental, no a master
- No se pudo verificar que arc42 contenga las 12 secciones completas
- Runs de CI en verde anteriores al cierre respaldan el corte vertical
- Commits posteriores al cierre (no calificados): 9bf16cf 2026-09-09T10:07:09-05:00 Change CI branches from 'main' to 'master'; 43b8e35 2026-09-08T10:25:05-05:00 Rename correcciones-feedback-XALD.md to correcciones.md
