# semana-05-corte1 · Tienda virtual UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `20ab43f` (2026-09-06T07:56:34-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | 20ab43f 2026-09-06T07:56:34-05:00 en rama principal | Cumple | Anterior al cierre 2026-09-07T05:00:00Z |
| correcciones.md existe en la raíz del estado calificado | Árbol de 20ab43f no incluye correcciones.md; aparece en HEAD 3d732d7 y en diff_desde_cierre | No cumple | Añadido después del cierre; no cumple la fila |
| Correcciones trazables y contrastadas | No existe correcciones.md en 20ab43f | No cumple | Sin índice de correcciones no hay trazabilidad contrastable |
| S1 al día: equipo, problema y repositorio | docs/problema.md, docs/aspectos.md, docs/ia.md, docs/disponibilidad.md, README.md en 20ab43f | Cumple | Equipo, problema y repositorio documentados |
| S2 al día: escenarios de calidad y restricciones | docs/arbol-utilidad.md, docs/escenarios-calidad.md, arc42 secciones 1-3, docs/c4/context.md | Cumple | Escenarios y restricciones presentes |
| S3 al día: estrategia de solución y decisiones | docs/matriz-comparativa-arquitectura.md, docs/adr/0001-monolito-modular.md, arc42 sección 4 | Cumple | Estrategia y ADR documentados |
| S4 al día: arc42, C4 y corte vertical | arc42 secciones 1-11, docs/c4/container.md, backend/app/modules/catalog/ con código y tests | Cumple | Incremento arc42, C4 y corte vertical presentes |
| Corte vertical reproducible y coherente con la arquitectura | README documenta docker compose up --build y pytest; backend/tests/test_catalog.py existe | Cumple | Coherente con C4 container.md; pruebas locales documentadas |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/tests.yml; run 34034598673 success 2026-09-06T12:56:43Z | Cumple | Run inmediatamente posterior al hash calificado 20ab43f |
| Trazabilidad consolidada navegable | docs/aspectos.md con 6 columnas; sin columna C4 ni Evidencia | No cumple | No alcanza las 8 columnas del contrato; enlaces parciales |
| PDF u otro adjunto exigido por el aula | Sin acceso a Moodle | No verificado | Requiere adjunto en el aula |
| Sustentación del corte | Sin sesión registrada | No verificado | Lo resuelve el docente |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima | README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md en 20ab43f | Cumple | Estructura completa en el estado calificado |
| Convenciones de ADR | docs/adr/0001-monolito-modular.md con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Nombre y contenido siguen la convención |
| Tabla de aspectos | docs/aspectos.md con columnas: Aspecto, Escenario, Prioridad, Decisión, Ubicación, Pruebas | No cumple | Faltan ID, C4 y Evidencia como columnas separadas; 6 de 8 |
| Registro de uso de IA | docs/ia.md con tabla de usos, descartes y validación; 11 commits en el historial | Cumple | Registro crece a lo largo del semestre |
| README | README.md con qué es, arranque con docker compose up --build y pruebas con pytest | Cumple | Requisitos previos declarados |
| Pipeline y análisis estático | .github/workflows/tests.yml solo ejecuta pytest; sin paso de SonarCloud | No cumple | Falta análisis estático SonarCloud exigido por el contrato |
| Secretos | grep sin coincidencias; sin .env versionados en 20ab43f | Cumple | Sin credenciales en el repositorio |
| Autoría y colaboración | RAZOR7150 (8), pxtroniwnl (5), Jasen/Jasen Yukopila consolidado (7), shalom-A26 (2) | Cumple | Cuatro identidades con commits; actividad repartida en agosto-septiembre |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `3d732d740053c8f10ad4c618d3031024c72630bc 2026-09-07T14:41:37-05:00 corte-1`
- **Veredicto**: con pendientes
- Resumen: El proyecto en HEAD tiene correcciones.md y documentación amplia, pero el estado calificado 20ab43f carecía de correcciones.md y la tabla de aspectos no cumple el formato del contrato.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- correcciones.md añadido en 3d732d7 (2026-09-07T14:41:37-05:00) después del cierre
- docs/aspectos.md y docs/ia.md modificados en 3d732d7 después del cierre

Pendientes que siguen abiertos:
- correcciones.md ausente en el estado calificado
- tabla de aspectos sin las 8 columnas del contrato
- SonarCloud no configurado en el pipeline

## Recuento y nota sugerida

7 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula (requiere acceso a Moodle)
- Sustentación del corte (sesión a cargo del docente)

## Hallazgos para la planilla

- correcciones.md ausente en el estado calificado 20ab43f; añadido en 3d732d7 tras el cierre
- docs/aspectos.md no cumple las 8 columnas del contrato (tiene 6)
- Pipeline sin análisis estático SonarCloud
- Commit 3d732d7 posterior al cierre modifica correcciones.md, docs/aspectos.md y docs/ia.md
- Sin evidencia de PDF en Moodle
- Commits posteriores al cierre (no calificados): 3d732d7 2026-09-07T14:41:37-05:00 corte-1
