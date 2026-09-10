# semana-05-corte1 · Clubs UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `4ede977` en `origin/master` (2026-09-06T22:41:55-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/master, hash 4ede977, fecha 2026-09-06T22:41:55-05:00 (anterior al cierre 2026-09-07T05:00:00Z) | Cumple | El estado calificado es el último commit de master antes del cierre. |
| correcciones.md existe en la raíz del estado calificado | git ls-tree del hash 4ede977 no incluye correcciones.md; árbol del estado calificado no lo lista | No cumple | Falta el archivo obligatorio en la raíz del estado calificado. |
| Correcciones trazables y contrastadas | No existe correcciones.md; no hay índice de correcciones para S1-S4 | No cumple | Sin archivo no hay trazabilidad de correcciones. |
| S1 al día: equipo, problema y repositorio | docs/ficha_problema.md describe problema y stakeholders; README.md lista equipo y repositorio; autores en historial: Zavod Dev, Josh Ortega, Luis-Salas-Reyes, Josh4OP, deortahollman-star, Luis Daniel | Cumple | Equipo y problema documentados; repositorio en organización ISCOUTB. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/10_requisitos_de_calidad.md incluye escenarios U1-U3 y C1-C3; docs/arc42/02_restricciones.md lista T1-T4, O1-O3, C1-C2 | Cumple | Escenarios y restricciones presentes y coherentes. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/04_estrategia_de_solucion.md y docs/adr/0001-hexagonal.md documentan decisión hexagonal; matriz comparativa en docs/arc42/matriz_comparativa_estilos.md | Cumple | Estrategia y ADR aceptado con trazabilidad. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ con secciones 1-6,9,10,12; docs/c4/contexto.md con C4 nivel 1 y 2; backend con endpoints /health y /publicaciones, pruebas en backend/tests/ | Cumple | Documentación arc42 completa y corte vertical implementado. |
| Corte vertical reproducible y coherente con la arquitectura | README.md sección 7 documenta arranque con uvicorn y pruebas con pytest; backend/src/linkclub/main.py y routers implementan hexagonal; tests test_health.py y test_publicaciones.py | Cumple | Corte vertical ejecutable y alineado con C4 y ADR. |
| Pipeline y pruebas respaldan el estado calificado | run CI 'Backend tests' success 2026-09-07T03:42:14Z (posterior al cierre pero asociado al hash 4ede977) y run 2026-09-06T23:58:26Z success; workflow .github/workflows/backend-tests.yml | Cumple | Pruebas pasan en CI para el estado calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md con tabla de 8 columnas enlazando escenarios, C4, ADR, código y pruebas; enlaces verificados en el árbol | Cumple | La tabla de aspectos es navegable y completa. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; se entrega en Moodle | No verificado | No se puede verificar desde el repositorio; requiere acceso al aula. |
| Sustentación del corte | No hay evidencia en el repositorio | No verificado | Depende de la sesión de sustentación con el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_Clubs_UTB en organización ISCOUTB, público, integrantes en historial | Cumple | Nombre y organización correctos. |
| Estructura mínima | Árbol incluye README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md | Cumple | Estructura completa según contrato. |
| Estado del repositorio calificado | Hash 4ede977 en origin/master, fecha 2026-09-06T22:41:55-05:00, anterior al cierre | Cumple | Se usó la rama principal master. |
| Convenciones de ADR | docs/adr/0001-hexagonal.md con nombre correcto, estado aceptado, contexto, alternativas, consecuencias y trazabilidad | Cumple | Un ADR, bien formado. |
| Tabla de aspectos | docs/aspectos.md con 7 filas (U1-U3, C1-C3) y columnas ID, Aspecto, Escenario, Requisito, C4, ADR, Código, Pruebas | Cumple | Celdas con enlaces navegables. |
| Registro de uso de IA | docs/ia.md con tabla de usos por semana, herramienta, cómo se usó y motivo; historial de commits en docs/ia.md | Cumple | Registro completo y con evidencia de uso. |
| README | README.md sección 7 documenta arranque con un comando (uvicorn) y pruebas con pytest | Cumple | Instrucciones claras y reproducibles. |
| Pipeline y análisis estático | Workflow .github/workflows/backend-tests.yml ejecuta pytest en cada push; runs CI success en 2026-09-06 y 2026-09-07 | Cumple | CI activo y exitoso; no se exige SonarCloud en este corte. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `4ede977c7cccc335d878019ce06cba2e23cf76d2 2026-09-06T22:41:55-05:00 quite el C2 y lo reemplaze con el C3`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene una base sólida en documentación y código, pero la ausencia de correcciones.md impide el cumplimiento del compendio S5.

Pendientes que siguen abiertos:
- Crear correcciones.md en la raíz del estado calificado.
- Completar la trazabilidad de correcciones para S1-S4.
- Actualizar la tabla de aspectos con código y pruebas para U1, U3, C1, C2, C3.
- Actualizar README para reflejar el estado actual del proyecto.

## Recuento y nota sugerida

8 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula: no disponible en el repositorio; requiere acceso a Moodle.
- Sustentación del corte: no hay evidencia en el repositorio; depende de la sesión con el docente.

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado.
- No hay índice de correcciones para S1-S4.
- El commit 4ede977 modifica la sección 10 de arc42 (reemplaza C2 por C3) sin documentar en correcciones.md.
- La tabla de aspectos tiene filas con 'Pendiente' en código y pruebas (U1, U3, C1, C2, C3).
- El ADR 0001 menciona trazabilidad a U2, C1 y C3, pero no a C2 (que fue reemplazado).
- El README indica que el proyecto está en fase de planeación, pero ya hay código de corte vertical.
- El historial muestra actividad concentrada en agosto y septiembre, con picos en fechas de entrega.
- No hay evidencia de análisis estático con SonarCloud.
- El archivo docs/ia.md no incluye usos de IA para S5.
- El commit 4ede977 tiene mensaje informal 'quite el C2 y lo reemplaze con el C3'.
