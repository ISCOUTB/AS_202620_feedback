# semana-05-corte1 · mapsutb

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `e8bad4c` en `origin/master` (2026-09-09T18:34:48-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master e8bad4c 2026-09-09T18:34:48-05:00 | Cumple | Anterior al cierre 2026-09-10T17:00:00Z |
| correcciones.md existe en la raíz del estado calificado | correcciones.md en ls-tree de e8bad4c | Cumple | Presente en la raíz del hash calificado |
| Correcciones trazables y contrastadas | Sin contenido de correcciones.md en la evidencia | No verificado | No se pudo contrastar cada hallazgo S1-S4; falta el contenido del archivo |
| S1 al día: equipo, problema y repositorio | docs/ficha-problema.md en e8bad4c; commits 8e9c06d y 7af89e6 lo modifican tras el cierre | No verificado | Repositorio e integrantes verificados; contenido del problema no contrastable |
| S2 al día: escenarios de calidad y restricciones | docs/Arc42/02_architecture_constraints.adoc y 10_quality_requirements.adoc completos | Cumple | Escenarios RE/PR/DI/US/FI/MA/PO y restricciones documentados |
| S3 al día: estrategia de solución y decisiones | ADR 0001 editado y sin marcar reemplazo; ADR 0002 con nombre 0002.md | No cumple | Estrategia en 04_solution_strategy.adoc actualizada, pero gestión de ADR viola convención |
| S4 al día: arc42, C4 y corte vertical | docs/Arc42/07_deployment_view.adoc y 08_concepts.adoc son plantillas | No cumple | arc42 incompleto; C4 presente; corte vertical sin evidencia de ejecución |
| Corte vertical reproducible y coherente con la arquitectura | README documenta ./scripts/start.sh; test/app_smoke_test.dart existe | No verificado | Sin runs_ci; comando anotado: ./scripts/start.sh |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/sonar-sync-issues.yml presente; sin runs_ci | No verificado | No hay run asociado al hash e8bad4c |
| Trazabilidad consolidada navegable | docs/aspectos.md existe en e8bad4c | No verificado | Contenido no disponible para verificar las 8 columnas |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio | No verificado | Se entrega en Moodle; no verificable desde el repo |
| Sustentación del corte | Sesión de sustentación | No verificado | Lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_mapsutb público; 4 identidades en historial | Cumple | Nombre y organización correctos |
| Estructura mínima | docs/Arc42/ y docs/C4/ con mayúsculas | No cumple | Desviación de rutas; artefactos presentes pero en ubicación distinta |
| Convenciones de ADR | 0002.md no sigue patrón; 0001 editado sin marcar reemplazo | No cumple | Violación de la sección 4 del contrato |
| Tabla de aspectos | docs/aspectos.md existe | No verificado | Contenido no disponible para verificar columnas y navegabilidad |
| Registro de uso de IA | docs/ia.md con 4 commits de log | No verificado | Contenido no disponible para verificar rechazos y motivos |
| Pipeline y análisis estático | Solo workflow sonar-sync-issues.yml; sin runs_ci | No verificado | No hay evidencia de pruebas en CI |
| Secretos | git grep sin coincidencias; sin .env versionados | Cumple | Sin credenciales en el repositorio |
| Autoría y colaboración | shortlog: 4 identidades con 53/42/22/21 commits | Cumple | Contribución repartida entre los integrantes |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `7af89e6b3f0c608950c7ebe2fd7899459c1c9b4e 2026-09-11T07:15:32-05:00 Rename ficha-problema.md to ficha_problema.md`
- **Veredicto**: con pendientes
- Resumen: Proyecto con documentación arc42/C4/ADR avanzada y contribución de todo el equipo, pero con secciones arc42 vacías, gestión de ADR deficiente y sin evidencia de CI.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 4b464f1, 8e9c06d y 7af89e6 (2026-09-11) corrigen ficha-problema y trazabilidad de aspectos tras el cierre

Pendientes que siguen abiertos:
- Secciones 7 y 8 de arc42 sin completar
- ADR 0001 sin marcar reemplazo
- ADR 0002 con nombre incorrecto
- Sin runs_ci de pruebas
- correcciones.md sin contenido contrastable

## Recuento y nota sugerida

3 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.0 = 1 + 4 × (3/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correcciones trazables (criterio 3): falta contenido de correcciones.md
- S1: contenido de docs/ficha-problema.md no contrastable
- Corte vertical reproducible: falta run de CI
- Pipeline y pruebas: falta run asociado al hash
- Trazabilidad: contenido de docs/aspectos.md no disponible
- PDF: no disponible en repositorio
- Sustentación: la resuelve el docente
- Tabla de aspectos (transversal): contenido no disponible
- Registro de IA (transversal): contenido no disponible
- Pipeline (transversal): sin runs_ci

## Hallazgos para la planilla

- ADR 0001 editado tras aceptarse y sin marcar reemplazo por ADR 0002
- ADR 0002 no sigue la convención de nombre NNNN-titulo-kebab-case.md
- Secciones 7 y 8 de arc42 quedaron como plantilla sin contenido
- Rutas docs/Arc42/ y docs/C4/ con mayúsculas, desvían la estructura mínima
- Commits 4b464f1, 8e9c06d y 7af89e6 corrigen ficha-problema y aspectos tras el cierre
- Sin runs_ci que respalden pruebas del hash calificado
- correcciones.md presente pero sin contenido contrastable en la evidencia
- Commits posteriores al cierre (no calificados): 7af89e6 2026-09-11T07:15:32-05:00 Rename ficha-problema.md to ficha_problema.md; 8e9c06d 2026-09-11T07:13:39-05:00 Revise project details and objectives in ficha-problema; 4b464f1 2026-09-11T07:08:02-05:00 Revise aspect tracing for user guidance system
