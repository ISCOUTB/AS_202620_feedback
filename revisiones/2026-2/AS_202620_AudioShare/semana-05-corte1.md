# semana-05-corte1 · AudioShare

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `cb65d13` en `origin/master` (2026-09-06T22:00:48-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master cb65d13 2026-09-06T22:00:48-05:00 (2026-09-07T03:00:48Z), anterior al cierre 2026-09-07T05:00:00Z | Cumple | Rama principal master, hash y fecha verificados. |
| correcciones.md existe en la raíz del estado calificado | git ls-tree cb65d13 no incluye correcciones.md en la raíz | No cumple | El archivo obligatorio no existe en el estado calificado. |
| Correcciones trazables y contrastadas | No hay correcciones.md ni respuestas a hallazgos S1-S4 | No cumple | Sin índice de verificación no hay trazabilidad de correcciones. |
| S1 al día: equipo, problema y repositorio | docs/ficha-problema.md, README.md, 4 contribuyentes en shortlog | Cumple | Problema, prototipo, usuarios y tensiones documentados; repo público en ISCOUTB. |
| S2 al día: escenarios de calidad y restricciones | docs/escenarios_calidad.md (EC-01..EC-04), docs/arbol_utilidad.md, docs/Restricciones_justificadas.md | Cumple | Escenarios medibles y restricciones justificadas presentes. |
| S3 al día: estrategia de solución y decisiones | docs/Matriz_Comparativa.md, docs/adr/0001-usar-monolito-modular.md, docs/arc42/src/04_solution_strategy.adoc | Cumple | Matriz comparativa y ADR-0001 coherentes con la estrategia. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ presente pero faltan 07_deployment_view.adoc, 08_concepts.adoc y 11_technical_risks.adoc; docs/c4/ y tests/a01.test.ts existen | No cumple | arc42 incompleto respecto a las secciones 1-12 del contrato. |
| Corte vertical reproducible y coherente con la arquitectura | README.md con npm run dev y npm test; tests/a01.test.ts recorre A-01; run CI success 34079348567 | Cumple | El flujo HTTP, persistencia SQLite y sync están implementados y probados. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml ejecuta npm run verify; run 34078177649 success 2026-09-07T03:00:50Z | Cumple | Run de CI exitoso asociado al push del estado calificado y anterior al cierre. |
| Trazabilidad consolidada navegable | docs/aspectos.md con matriz A-01 enlazada a EC, ADR, C4, código y pruebas | Cumple | La cadena aspecto-requisito-C4-ADR-código-pruebas es navegable. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; se entrega en Moodle | No verificado | Requiere revisar el aula para verificar el adjunto. |
| Sustentación del corte | Sesión de sustentación no visible en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima | Árbol cb65d13: faltan docs/arc42/src/07_deployment_view.adoc, 08_concepts.adoc y 11_technical_risks.adoc | No cumple | El contrato exige secciones 1 a 12 de arc42; faltan 3 secciones. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md cumple patrón NNNN-titulo-kebab-case y contiene contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Un ADR aceptado, sin reescrituras posteriores visibles. |
| Tabla de aspectos | docs/aspectos.md con matriz A-01 enlazada a EC, ADR, C4, implementación y pruebas | Cumple | La columna Evidencia está implícita en Pruebas; la cadena es navegable. |
| Registro de uso de IA | docs/ia.md con tabla de usos, herramientas, propuestas rechazadas y motivo; 9 commits en el log | Cumple | Incluye la columna de rechazos con justificación técnica. |
| README | README.md con descripción, requisitos Node.js 22+, arranque npm run dev y pruebas npm test/npm run verify | Cumple | Arranque y verificación con un solo comando documentados. |
| Pipeline y análisis estático | .github/workflows/ci.yml solo ejecuta npm ci y npm run verify; sin configuración ni paso de SonarCloud | No cumple | El contrato exige análisis estático en SonarCloud; no hay evidencia de ello. |
| Secretos | git grep sin coincidencias; sin .env versionados; solo .env.example | Cumple | No se encontraron credenciales en el estado calificado. |
| Autoría y colaboración | shortlog: 45 Elian Daniel Perea Vanegas, 38 Yeiver Andrés Vergel Pérez, 36 cardonavincent26-design, 30 Santiago Adolfo Camacho Hernández | Cumple | 4 cuentas contribuyen con volumen repartido; cardonavincent26-design no tiene nombre visible coincidente con un integrante declarado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `cb65d13134b220c020d0facaa00d0a779d584245 2026-09-06T22:00:48-05:00 Update README.md`
- **Veredicto**: con pendientes
- Resumen: Proyecto con corte vertical A-01 funcional y CI verde, pero con pendientes del contrato: correcciones.md ausente, arc42 incompleto y sin SonarCloud.

Pendientes que siguen abiertos:
- correcciones.md en la raíz
- secciones arc42 07/08/11
- análisis estático SonarCloud

## Recuento y nota sugerida

7 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u adjunto entregado en Moodle (no disponible en el repositorio).
- Sustentación del corte (la resuelve el docente en sesión).

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado cb65d13.
- No hay respuestas trazables a hallazgos S1-S4 por ausencia de correcciones.md.
- Faltan secciones arc42 07 (despliegue), 08 (conceptos) y 11 (riesgos).
- Pipeline sin análisis estático SonarCloud.
- Runs de CI fallidos el 2026-09-04 previos al corte, aunque el estado calificado tiene runs success.
- docs/aspectos.md no incluye columna Evidencia separada.
