# semana-05-corte1 · mapsutb

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `f40775d` en `origin/master` (2026-09-06T22:35:28-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master f40775d 2026-09-06T22:35:28-05:00 (cierre 2026-09-07T05:00:00Z) | Cumple | Hash anterior al cierre y rama principal identificada. |
| correcciones.md existe en la raíz del estado calificado | Árbol de f40775d no incluye correcciones.md en la raíz | No cumple | No existe el archivo exigido en el estado calificado. |
| Correcciones trazables y contrastadas | No hay correcciones.md que enlace hallazgos S1-S4 con evidencia | No cumple | Sin índice de correcciones no se puede contrastar trazabilidad. |
| S1 al día: equipo, problema y repositorio | docs/ficha-problema.md presente; autores: CarlosManrique-1397, i-matallana, charlygz21, nerlis-otero | Cumple | Equipo y problema documentados en el estado calificado. |
| S2 al día: escenarios de calidad y restricciones | docs/escenarios_calidad.md y docs/Arc42/02_architecture_constraints.adoc presentes | Cumple | Escenarios y restricciones documentados. |
| S3 al día: estrategia de solución y decisiones | docs/Arc42/04_solution_strategy.adoc y docs/adr/0001-patrones-de-diseno.md, docs/adr/0002.md presentes | Cumple | Estrategia y ADR documentados. |
| S4 al día: arc42, C4 y corte vertical | docs/Arc42/ secciones 01-12, docs/C4/C1.md, C2.md, C3.md, Contexto.md; lib/ y test/app_smoke_test.dart | Cumple | Documentación arc42 y C4 presentes; esqueleto Flutter con prueba de arranque. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta ./scripts/start.sh y flutter test; no hay run de CI citado | No verificado | No se ejecutó código; falta evidencia de ejecución del script y pruebas. |
| Pipeline y pruebas respaldan el estado calificado | No hay runs_ci en la evidencia; solo test/app_smoke_test.dart en el árbol | No verificado | Falta URL o run de CI asociado al hash calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md presente pero sin contenido citado; docs/arbol_utilidad.md y docs/escenarios_calidad.md separados | No cumple | No se evidencia la tabla de trazabilidad aspecto-requisito-C4-ADR-código-pruebas navegable. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; depende de Moodle | No verificado | El PDF se entrega en el aula; no verificable desde el repositorio. |
| Sustentación del corte | Sesión de sustentación no disponible en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_mapsutb visible; autores: CarlosManrique-1397, i-matallana, charlygz21, nerlis-otero | Cumple | Nombre, organización y visibilidad correctos; integrantes en historial. |
| Estructura mínima | README.md, docs/Arc42/, docs/adr/, docs/C4/, docs/aspectos.md, docs/ia.md presentes | Cumple | Estructura mínima presente; docs/Arc42 en mayúscula es desviación menor de ruta. |
| Estado del repositorio que se califica | origin/master f40775d 2026-09-06T22:35:28-05:00 anterior al cierre | Cumple | Se usó la rama principal declarada y el hash anterior al cierre. |
| Convenciones de ADR | docs/adr/0002.md no sigue convención NNNN-titulo-en-kebab-case.md | No cumple | El ADR 0002 no tiene título en kebab-case; además 0001 y 0002 duplican el mismo título. |
| La tabla de aspectos | docs/aspectos.md presente pero sin contenido citado en la evidencia | No cumple | No se puede verificar que tenga las 8 columnas ni enlaces navegables. |
| Registro de uso de IA | docs/ia.md con 4 commits: f829f2e, a6e51bc, 098ac4e, 3d4b0c9 | Cumple | El registro crece a lo largo del semestre. |
| README | README.md documenta qué es, requisitos, ./scripts/start.sh y flutter test | Cumple | Arranque con un solo comando documentado. |
| Pipeline y análisis estático | No hay runs_ci ni .github/workflows en la evidencia | No verificado | Falta evidencia de ejecución de CI y SonarCloud. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `e8bad4c286e5b985b324234b644e3b1fe961b626 2026-09-09T18:34:48-05:00 added: Manual identidad Visual`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene documentación arquitectónica completa (arc42, C4, ADR) y un esqueleto Flutter con prueba de arranque, pero la entrega de corte carece de correcciones.md y de evidencia de CI; hay pendientes de trazabilidad y convención de ADR.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Commits posteriores al cierre: 3f5221b, 09f7aad, af22316, fd046a8, e8bad4c (2026-09-08/09) ajustan plugins y manual de identidad visual; no se evidencia que corrijan hallazgos S1-S4.

Pendientes que siguen abiertos:
- correcciones.md en la raíz del estado calificado
- Trazabilidad navegable en docs/aspectos.md
- Convención de nombre del ADR 0002
- Evidencia de CI y pruebas asociadas al hash calificado

## Recuento y nota sugerida

5 de 12 criterios Cumple.

## No verificado / pendientes

- Corte vertical reproducible y coherente con la arquitectura
- Pipeline y pruebas respaldan el estado calificado
- PDF u otro adjunto exigido por el aula
- Sustentación del corte
- Pipeline y análisis estático (transversal)

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado.
- No hay trazabilidad de correcciones S1-S4.
- docs/aspectos.md no muestra la tabla navegable de 8 columnas.
- docs/adr/0002.md no cumple la convención de nombre.
- No hay evidencia de CI ni run asociado al hash calificado.
- No se verificó la reproducibilidad del corte vertical por falta de run.
- Hay 10 commits posteriores al cierre en la rama principal.
- Commits posteriores al cierre (no calificados): e8bad4c 2026-09-09T18:34:48-05:00 added: Manual identidad Visual; fd046a8 2026-09-09T18:32:53-05:00 added: Manual identidad Visual; af22316 2026-09-09T18:31:12-05:00 added: Manual identidad Visual; 09f7aad 2026-09-08T18:41:24-05:00 Add exclusions for generated plugin files in SonarQube; 3f5221b 2026-09-08T17:59:58-05:00 Remove comment about unregistered plugins
