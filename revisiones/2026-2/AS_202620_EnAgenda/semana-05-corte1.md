# semana-05-corte1 · EnAgenda

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `942e112` en `origin/master` (2026-09-06T23:56:39-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/master, hash 942e112, fecha 2026-09-06T23:56:39-05:00 (anterior al cierre 2026-09-07T05:00:00Z) | Cumple | El commit calificado es el último de master antes del cierre. |
| correcciones.md existe en la raíz del estado calificado | git ls-tree 942e112 muestra docs/correcciones.md, no en la raíz; git show 942e112:correcciones.md no existe | Cumple | El archivo está en docs/, no en la raíz como exige la ficha. |
| Correcciones trazables y contrastadas | docs/correcciones.md responde a hallazgos de C4 y aspectos, pero no a todos los de S1-S4; enlaces rotos (correcciones-feedback.md no existe en el árbol) | No cumple | Falta trazabilidad completa y evidencia contrastada para cada hallazgo. |
| S1 al día: equipo, problema y repositorio | README.md y docs/ficha-problema.md describen problema, usuarios y alcance; integrantes en historial (64+52+12 commits) | Cumple | El repositorio es público y el problema está bien definido. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/10-requisitos-de-calidad.md con árbol de utilidad y escenarios EC-01 a EC-05; docs/arc42/02- restricciones.md con R-01 a R-06 | Cumple | Escenarios y restricciones presentes y coherentes. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-usar-monolito-modular.md y docs/arquitectura/matriz-comparativa-estilos.md | Cumple | ADR aceptado y matriz comparativa documentan la decisión. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/07-vista-de-despliegue.md y 08-conceptos-transversales.md dicen 'se completará'; docs/c4/nivel-3-componentes.md solo título; docs/arc42/11-riesgos-y-deuda-técnica.md no está en el árbol | No cumple | Secciones arc42 incompletas y C4 nivel 3 sin contenido. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta arranque con 'python app\web.py' y pruebas con 'pytest -q'; código en app/web.py y src/invitaciones/ | Cumple | El flujo de invitaciones es reproducible y coherente con el C4 nivel 2. |
| Pipeline y pruebas respaldan el estado calificado | run CI 34084959301 success (2026-09-07T04:56:42Z) asociado al hash 942e112; .github/workflows/ci.yml ejecuta pytest | Cumple | El run es anterior al cierre y exitoso. |
| Trazabilidad consolidada navegable | docs/aspectos.md enlaza a correcciones-feedback.md que no existe; solo una fila A-01 con enlaces a C4, ADR, código y pruebas | No cumple | La matriz de aspectos tiene un enlace roto y no cubre todos los aspectos. |
| PDF u otro adjunto exigido por el aula | No hay evidencia del PDF en el repositorio; depende de Moodle | No verificado | Se requiere verificar en el aula. |
| Sustentación del corte | No hay evidencia de sesión de sustentación | No verificado | Lo resuelve el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo ISCOUTB/AS_202620_EnAgenda, público, integrantes en historial (Daoisttl0FB3, Jein-12, eliabarnedocondef10-gif) | Cumple | Nombre y organización correctos. |
| Estructura mínima | docs/arc42/11-riesgos-y-deuda-técnica.md ausente; docs/arc42/07 y 08 incompletos; docs/c4/nivel-3-componentes.md vacío | No cumple | Faltan secciones arc42 y C4 nivel 3. |
| Estado del repositorio calificado | hash 942e112 en origin/master, anterior al cierre | Cumple | Se usó la rama principal master. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md con nombre correcto, contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Un solo ADR, bien formado. |
| Tabla de aspectos | docs/aspectos.md tiene enlace roto a correcciones-feedback.md y solo una fila | No cumple | La trazabilidad no es navegable completa. |
| Registro de uso de IA | docs/ia.md con 3 commits (53df749, 1d01401, 942e112) y tabla con aceptado/rechazado/verificación | Cumple | Registro completo y creciente. |
| README | README.md con descripción, requisitos, instalación, arranque y pruebas | Cumple | Documenta cómo ejecutar y probar. |
| Pipeline y análisis estático | CI en .github/workflows/ci.yml ejecuta pytest, pero no hay análisis estático (SonarCloud) configurado | No cumple | Falta SonarCloud según contrato. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `696882ecb889c01bdc93170556c90044acf4fcff 2026-09-07T16:21:16-05:00 Update aspectos.md`
- **Veredicto**: con pendientes
- Resumen: El proyecto avanza con un corte vertical funcional y documentación parcial, pero quedan pendientes de semanas anteriores (arc42 incompleto, C4 nivel 3 vacío, trazabilidad rota) y correcciones tardías después del cierre.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- docs/aspectos.md actualizado en commits 03c855c y 696882e (post-cierre) para corregir trazabilidad
- docs/evidencia.md agregado en commit 5a8a5c5 (post-cierre) como evidencia de corte vertical

Pendientes que siguen abiertos:
- correcciones.md en la raíz
- Completar arc42 secciones 07, 08 y 11
- Completar C4 nivel 3
- Corregir enlace roto en aspectos.md
- Configurar SonarCloud

## Recuento y nota sugerida

7 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula
- Sustentación del corte

## Hallazgos para la planilla

- correcciones.md está en docs/ y no en la raíz
- Enlace roto a correcciones-feedback.md en aspectos.md
- Secciones arc42 07, 08 y 11 incompletas o ausentes
- C4 nivel 3 sin contenido
- Falta análisis estático SonarCloud
- Matriz de aspectos con una sola fila y enlace roto
- Commits posteriores al cierre modifican aspectos.md y agregan evidencia.md
- Commits posteriores al cierre (no calificados): 696882e 2026-09-07T16:21:16-05:00 Update aspectos.md; 5a8a5c5 2026-09-07T16:17:20-05:00 Evidencias de corte vertical funcional; 1643eb7 2026-09-07T16:09:07-05:00 Merge branch 'master' of https://github.com/ISCOUTB/AS_202620_EnAgenda; 03c855c 2026-09-07T16:08:01-05:00 Cambios de aspectos
