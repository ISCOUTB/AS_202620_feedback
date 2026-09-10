# semana-05-corte1 · DinamikUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `f89564f` en `origin/master` (2026-09-06T23:35:03-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master f89564f 2026-09-06T23:35:03-05:00 (2026-09-07T04:35:03Z), anterior al cierre 2026-09-07T05:00:00Z | Cumple | Hash y fecha verificados en la rama principal. |
| correcciones.md existe en la raíz del estado calificado | correcciones.md presente en el árbol de f89564f | Cumple | Archivo en la raíz del hash calificado. |
| Correcciones trazables y contrastadas | No se proporcionó el contenido de correcciones.md en f89564f | No verificado | Se requiere el contenido para contrastar cada hallazgo S1-S4. |
| S1 al día: equipo, problema y repositorio | README.md y docs/fichadelproblema.md presentes; falta la matriz vigente de semana-01-evidencia-s1.md | No verificado | Sin la matriz S1 no se puede confirmar el estado. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/10-quality-requirements.md y 02-architecture-constraints.md presentes; falta la matriz vigente de semana-02-evidencia-s2.md | No verificado | Sin la matriz S2 no se puede confirmar el estado. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/04-solution-strategy.md y docs/adr/0001-0003 presentes; falta la matriz vigente de semana-03-evidencia-s3.md | No verificado | Sin la matriz S3 no se puede confirmar el estado. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/07-deployment-view.md y 08-cross-cutting-concepts.md están vacíos en f89564f | No cumple | arc42 incompleto: secciones 07 y 08 sin contenido. |
| Corte vertical reproducible y coherente con la arquitectura | backend/app/requisitos/, frontend/lib/requisitos/, backend/tests/test_requisitos.py, frontend/test/widget_test.dart presentes; sin runs de CI | No verificado | Código y pruebas existen, pero no hay evidencia de ejecución. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml presente; sin runs_ci asociados | No verificado | Se requiere URL de run o evidencia de ejecución. |
| Trazabilidad consolidada navegable | docs/aspectos.md presente; contenido no proporcionado | No verificado | Sin el contenido no se puede verificar la navegabilidad de las 8 columnas. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio | No verificado | Depende de la entrega en Moodle. |
| Sustentación del corte | Sesión de sustentación no evaluable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima | README.md, docs/arc42/01-12, docs/adr/0001-0003, docs/c4/, docs/aspectos.md, docs/ia.md en el árbol de f89564f | Cumple | Estructura completa; contenido de 07/08 vacío afecta a arc42, no a la estructura. |
| Convenciones de ADR | docs/adr/0001-seleccion-monolito-modular.md, 0002-seleccion-tecnologia-backend-frontend.md, 0003-seleccion-motor-de-base-de-datos.md | Cumple | Nombres y estructura de ADR correctos. |
| Tabla de aspectos | docs/aspectos.md presente; contenido no proporcionado | No verificado | Se requiere el contenido para verificar las 8 columnas. |
| Registro de uso de IA | docs/ia.md presente con historial de 14 commits; contenido no proporcionado | No verificado | Se requiere el contenido para verificar las columnas de aceptado/rechazado. |
| README | README.md con descripción, arranque (start.bat), pruebas y estructura | Cumple | Incluye comando único de inicio y cómo probar. |
| Pipeline y análisis estático | .github/workflows/ci.yml presente; sin runs_ci | No verificado | Se requiere evidencia de ejecución en GitHub Actions. |
| Secretos | git grep sin coincidencias; sin .env versionados | Cumple | No se encontraron credenciales en el hash. |
| Autoría y colaboración | shortlog: 4 identidades consolidadas: JuanchisV/404Vargas/Juan José Vargas Pérez (104), Daniel-dev02/LUIS DANIEL (37), gillianisperez-prog (23), Eramirezr (7) | Cumple | Los 4 integrantes tienen contribuciones; distribución desigual pero presente. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `72bfc7e206eac4147dd244c03fa09b4b32b9a7e7 2026-09-07T22:28:37-05:00 Update correcciones.md`
- **Veredicto**: con pendientes
- Resumen: El compendio S5 no está completo: arc42 tiene secciones vacías, no hay evidencia de CI y correcciones.md no se pudo contrastar. La base del proyecto es sólida pero persisten carencias de S4.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 72bfc7e, 86870bf, 30efaa7, af1d7e3 (2026-09-07) actualizan correcciones.md e ia.md después del cierre; no se puede confirmar que resuelvan hallazgos previos sin su contenido.

Pendientes que siguen abiertos:
- Completar docs/arc42/07-deployment-view.md y 08-cross-cutting-concepts.md
- Verificar contenido de correcciones.md en el hash calificado
- Aportar runs de CI del estado calificado
- Completar trazabilidad navegable en docs/aspectos.md

## Recuento y nota sugerida

2 de 12 criterios Cumple.

## No verificado / pendientes

- Contenido de correcciones.md en f89564f
- Matrices vigentes de S1, S2 y S3
- Contenido de docs/aspectos.md
- Contenido de docs/ia.md
- Runs de CI asociados al hash
- PDF en Moodle
- Sustentación

## Hallazgos para la planilla

- docs/arc42/07-deployment-view.md y 08-cross-cutting-concepts.md vacíos en el hash calificado.
- correcciones.md existe pero su contenido no fue contrastable en f89564f.
- Sin runs de CI que respalden el estado calificado.
- Matrices S1-S3 no disponibles para verificar el compendio.
- 4 commits posteriores al cierre modifican correcciones.md e ia.md.
- Commits posteriores al cierre (no calificados): 72bfc7e 2026-09-07T22:28:37-05:00 Update correcciones.md; 86870bf 2026-09-07T22:25:30-05:00 Update ia.md; 30efaa7 2026-09-07T22:12:21-05:00 Update correcciones.md; af1d7e3 2026-09-07T21:53:03-05:00 Update correcciones.md
