# semana-05-corte1 · Calificación automática

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `201acac` (2026-09-06T23:34:17-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama master, hash 201acac, fecha 2026-09-06T23:34:17-05:00 < cierre 2026-09-07T05:00:00Z | Cumple | El commit calificado es identificable y anterior al cierre. |
| correcciones.md existe en la raíz del estado calificado | árbol de 201acac contiene correcciones_feedback.md y no correcciones.md; git show 201acac:correcciones.md no disponible | No cumple | El archivo con el nombre exigido solo aparece en el commit 8b0d00b posterior al cierre. |
| Correcciones trazables y contrastadas | no existe correcciones.md en 201acac; no se puede contrastar respuesta a hallazgos S1-S4 | No cumple | Sin el archivo exigido en el estado calificado no hay trazabilidad de correcciones. |
| S1 al día: equipo, problema y repositorio | README.md, docs/ficha-problema.md, autores del historial (scp1109, josueacademico17-source, SusanaRosales, Mariadelmar-restrepo) | Cumple | Problema, repositorio y equipo identificados. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/arc42-template-ES.md secciones 1.2, 2 y 10; docs/aspectos.md con EC-07 | Cumple | Escenarios EC-01 a EC-07 y restricciones RNF documentados. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001 a 0006 con estado, contexto, alternativas, decisión y consecuencias | Cumple | Seis ADR, incluido el 0006 que implementa la bitácora previa al encolado. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-ES.md, docs/c4/doc-c4.md, backend/tests/test_durabilidad_recepcion.py | Cumple | arc42 1-6 y 9-12, C4 niveles 1-2 y corte vertical A-01 construido con pruebas. |
| Corte vertical reproducible y coherente con la arquitectura | backend/tests/test_recepcion.py, test_durabilidad_recepcion.py, test_carga_hojas.py; docker-compose.yml; README sección 'Cómo se arranca' y 'Cómo recorrerlo' | Cumple | Corte vertical de carga con frontend web, API, almacenamiento, cola y worker; coincide con C4 y ADR-0002/0006. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml existe en el árbol; no se citan runs_ci con URL ni conclusión | No verificado | Falta evidencia de un run asociado al hash 201acac o anterior al corte; comando anotado: curl a actions/runs del repositorio. |
| Trazabilidad consolidada navegable | docs/aspectos.md con columnas Aspecto-Requisito-EC-C4-ADR-Código-Pruebas-Evidencia enlazadas; docs/evidencia/medicion-ec07.md | Cumple | La fila A-01 enlaza a código, pruebas y evidencia de EC-07. |
| PDF u otro adjunto exigido por el aula | sin acceso a Moodle | No verificado | El PDF se entrega en el aula; no está disponible en el repositorio. |
| Sustentación del corte | no hay sesión de sustentación en la evidencia | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura | árbol de 201acac: existen README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md no aparece | No cumple | Falta docs/ia.md en el estado calificado; el resto de la estructura mínima está. |
| ADR | docs/adr/0001 a 0006 con nombres NNNN-titulo-en-kebab-case; cada ADR incluye contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | La convención de nombres y el contenido exigido se cumplen. |
| Qué estado del repositorio se califica | hash 201acac en master, 2026-09-06T23:34:17-05:00, anterior al cierre 2026-09-07T05:00:00Z | Cumple | Estado calificado correctamente identificado; commits posteriores se registran en overall. |
| Convenciones de ADR | ls docs/adr: 0001-0006 siguen el patrón; sin commits de reescritura visibles sobre ADR aceptados; 0001 reemplazado por 0002 sin editarse | Cumple | Los ADR aceptados no se reescriben; los cambios de decisión se registran en ADR nuevos. |
| La tabla de aspectos | docs/aspectos.md con 8 columnas y filas enlazadas a requisito, escenario, C4, ADR, código, pruebas y evidencia | Cumple | La fila A-01 está completa; las demás quedan declaradas, lo que es coherente con la semana. |
| docs/ia.md | git ls-tree 201acac no incluye docs/ia.md | No cumple | No hay registro de uso de IA en el estado calificado. |
| README | README.md con 'docker compose up' como arranque de un solo comando y sección 'Cómo se prueba' | Cumple | El README explica arranque, recorrido del corte vertical y ejecución de pruebas. |
| Pipeline y análisis estático | .github/workflows/ci.yml en el árbol; sin runs_ci citados | No verificado | Faltan evidencia de ejecución (URL de run o conclusión) y de análisis en SonarCloud. Comando anotado: curl a actions/runs del repositorio. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `8b0d00b62d2a03dfe509edae578261748a842294 2026-09-07T14:29:28-05:00 Rename correcciones_feedback.md to correcciones.md`
- **Veredicto**: al dia
- Resumen: En HEAD el proyecto mantiene el corte vertical A-01 construido y probado, con seis ADR y documentación arc42/C4 completa. Persisten dos pendientes: docs/ia.md no existe y la corrección del nombre correcciones.md se hizo después del cierre. Aunque el hash calificado 201acac no incluye correcciones.md, el commit 8b0d00b de HEAD sí lo añade, por lo que esa fila queda resuelta de forma tardía.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 8b0d00b (2026-09-07T14:29:28-05:00) renombra correcciones_feedback.md a correcciones.md: corrige la fila 2 de la ficha S5 después del cierre.

Pendientes que siguen abiertos:
- docs/ia.md sigue ausente en HEAD.
- Correcciones trazables en correcciones.md no se pudieron contrastar: no se verificó su contenido ni respuesta a hallazgos S1-S4.
- No hay runs_ci citados para respaldar el pipeline en HEAD.

## Recuento y nota sugerida

7 de 12 criterios Cumple.

## No verificado / pendientes

- Pipeline y pruebas respaldan el estado calificado
- PDF u otro adjunto exigido por el aula
- Sustentación del corte
- Pipeline y análisis estático (contrato)

## Hallazgos para la planilla

- Hash calificado 201acac está en master y es anterior al cierre.
- En 201acac no existe correcciones.md sino correcciones_feedback.md: la fila 2 de la ficha incumple.
- docs/ia.md no está en el árbol de 201acac ni en HEAD: falta el registro de uso de IA.
- El commit 8b0d00b posterior al cierre renombra correcciones_feedback.md a correcciones.md.
- No hay runs_ci citados: la fila de pipeline queda sin verificar.
- El corte vertical A-01 tiene código, pruebas y evidencia de medición EC-07 (0 % pérdida, 1,744 s).
- Los seis ADR documentan decisiones y trazabilidad; los cambios de alcance se registran en ADR nuevos sin reescribir los anteriores.
- Commits posteriores al cierre (no calificados): 8b0d00b 2026-09-07T14:29:28-05:00 Rename correcciones_feedback.md to correcciones.md
