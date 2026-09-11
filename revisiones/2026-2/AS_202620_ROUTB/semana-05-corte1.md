# semana-05-corte1 · ROUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `343bb9d` en `origin/master` (2026-09-09T21:10:40-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master 343bb9d 2026-09-09T21:10:40-05:00 anterior al cierre 2026-09-10T17:00:00Z | Cumple | Hash y fecha verificados en la rama principal |
| correcciones.md existe en la raíz del estado calificado | correcciones.md presente en el árbol de 343bb9d | Cumple | Ubicación y nombre correctos |
| Correcciones trazables y contrastadas | correcciones.md existe pero su contenido no fue proporcionado | No verificado | Se requiere el contenido del archivo para contrastar hallazgos S1-S4 |
| S1 al día: equipo, problema y repositorio | README.md con descripción, equipo y enlace a docs/problema.md; repo ISCOUTB/AS_202620_ROUTB visible | Cumple | Equipo declarado coincide con integrantes del historial |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/10_requisitos_de_calidad.md con árbol de utilidad y escenarios; docs/arc42/02_restricciones_de_arquitectura.md con restricciones | Cumple | 8 atributos de calidad priorizados con escenarios medibles |
| S3 al día: estrategia de solución y decisiones | docs/arc42/04_estrategia_de_solucion.md y ADR 0001-0003 presentes | Cumple | Decisiones documentadas con alternativas y consecuencias |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ secciones 01-12; docs/c4/context.md con niveles 1-3; backend/tests/test_registro.py y test_cupos.py | Cumple | Documentación completa y código funcional |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta instalación, arranque (uvicorn, flutter run) y pruebas (pytest); tests en backend/tests/ | Cumple | El arranque requiere pasos de instalación previos, no es un solo comando literal |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml presente; README cita run #33992259222 Success, pero no hay runs_ci independiente | No verificado | La URL del run no pudo verificarse directamente |
| Trazabilidad consolidada navegable | docs/aspectos.md con 4 aspectos enlazados a C4, ADR, código, pruebas y evidencia | Cumple | Cada fila tiene enlaces navegables |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; depende de Moodle | No verificado | El aula debe confirmar la entrega |
| Sustentación del corte | Depende de la sesión de sustentación | No verificado | Lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_ROUTB visible; autores en historial: MKeinerrr, diegobrr999-commits, juliandmanjarrez-tech, junior14700 | Cumple | Nombre, organización y visibilidad correctos |
| Estructura mínima | README.md, docs/arc42/01-12, docs/adr/0001-0003, docs/c4/context.md, docs/aspectos.md, docs/ia.md presentes | Cumple | Estructura completa según contrato |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md, 0002-usar-arquitectura-interna-por-capas.md, 0003-control-atomico-de-cupos.md | Cumple | Nombres en kebab-case, numerados, con contexto, alternativas, decisión y trazabilidad |
| Registro de uso de IA | docs/ia.md existe con 6 commits en historial; contenido no disponible | No verificado | Se requiere el contenido para verificar columnas de aceptado/rechazado |
| README | README.md con descripción, equipo, tecnologías, instalación, ejecución y pruebas | Cumple | Documenta arranque y pruebas |
| Pipeline y análisis estático | .github/workflows/ci.yml presente; sin configuración ni evidencia de SonarCloud | No cumple | Falta análisis estático en SonarCloud exigido por el contrato |
| Secretos | Búsqueda de secretos solo arrojó falsos positivos (campos password); sin .env versionados | Cumple | No se encontraron credenciales reales |
| Autoría y colaboración | 4 autores con commits: MKeinerrr (35), diegobrr999-commits (6), juliandmanjarrez-tech (3), junior14700 (2) | Cumple | Distribución desigual pero todos contribuyen |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `343bb9d6565c1a81bdad542efde3fbb56b07e2ca 2026-09-09T21:10:40-05:00 Delete`
- **Veredicto**: al dia
- Resumen: El proyecto cumple la mayoría de criterios de la ficha S5 y del contrato transversal. Quedan aspectos no verificados por falta de evidencia (contenido de correcciones.md e ia.md, run de CI, PDF, sustentación) y una carencia de SonarCloud en el pipeline.

Pendientes que siguen abiertos:
- Verificar contenido de correcciones.md
- Verificar contenido de docs/ia.md
- Verificar run de CI asociado al hash
- Integrar SonarCloud al pipeline
- Entregar PDF en Moodle
- Sustentación del corte

## Recuento y nota sugerida

8 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.7 = 1 + 4 × (8/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correcciones trazables y contrastadas (contenido de correcciones.md)
- Pipeline y pruebas respaldan el estado calificado (run de CI)
- PDF u otro adjunto en Moodle
- Sustentación del corte
- Registro de uso de IA (contenido de docs/ia.md)

## Hallazgos para la planilla

- Contenido de correcciones.md no verificado por falta de evidencia
- Contenido de docs/ia.md no verificado
- Falta análisis estático en SonarCloud
- Run de CI citado en README no verificado directamente
- Distribución de commits desigual entre integrantes
- Arranque requiere pasos manuales de instalación
