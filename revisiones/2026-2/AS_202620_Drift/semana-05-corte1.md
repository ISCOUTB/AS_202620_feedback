# semana-05-corte1 · Drift

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `74337a3` en `origin/master` (2026-09-08T02:53:31Z) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/master, hash 74337a3, fecha 2026-09-08T02:53:31Z (anterior al cierre 2026-09-10T17:00:00Z) | Cumple | El estado calificado es identificable y cumple la condición temporal. |
| correcciones.md existe en la raíz del estado calificado | En el árbol del hash 74337a3 no aparece correcciones.md; solo docs/correciones.md (mal escrito y en subcarpeta) | No cumple | El archivo requerido en la raíz no existe en el estado calificado. |
| Correcciones trazables y contrastadas | docs/correciones.md (hash 74337a3) lista hallazgos pero con errores de ruta (p.ej. 'arc42_10_requisitos_de_calidad.md' no existe) y sin commits de verificación; los commits de corrección son posteriores al cierre (1cab45e, df8f512, etc.) | No cumple | El archivo no está en la raíz y las correcciones no se pueden contrastar con el estado calificado. |
| S1 al día: equipo, problema y repositorio | README.md (hash 74337a3) declara equipo de 4 integrantes y enlace a docs/ficha_problema.md; ficha_problema.md existe en el árbol | Cumple | El repositorio es público y la identidad del equipo es correcta. |
| S2 al día: escenarios de calidad y restricciones | docs/escenarios.md y docs/arc42/arc42_2_restricciones.md (hash 74337a3) definen E1-E5 y restricciones con medidas verificables | Cumple | Los escenarios y restricciones están documentados y trazables. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/arc42_4_soluciones_arquitectonica.md y docs/adr/0001-0002 (hash 74337a3) documentan la estrategia hexagonal y decisiones | Cumple | La estrategia y los ADR están presentes y coherentes. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ (secciones 1-6, 9, 10, 12), docs/c4/contexto.md y contenedores.md, y backend/tests/test_search_games.py (hash 74337a3) implementan el corte vertical | Cumple | La documentación arc42 y C4 están completas y el corte vertical está implementado. |
| Corte vertical reproducible y coherente con la arquitectura | README.md (hash 74337a3) documenta arranque con uvicorn y next; backend/tests/test_search_games.py prueba el flujo endpoint->caso de uso->adaptador Steam | Cumple | El corte vertical es reproducible y coherente con la arquitectura hexagonal. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml (hash 74337a3) y run 34060984657 (conclusión success) citado en docs/correciones.md | Cumple | El pipeline ejecuta pruebas y el run asociado está en verde. |
| Trazabilidad consolidada navegable | docs/aspectos.md (hash 74337a3) tiene tabla de trazabilidad pero con enlaces rotos (p.ej. 'arc42_10_requisitos_de_calidad.md' no existe) y celdas 'Pendiente' en E3-E5 | No cumple | La trazabilidad no es completamente navegable por enlaces incorrectos y huecos. |
| PDF u otro adjunto exigido por el aula | No hay evidencia del PDF en el repositorio; depende de Moodle | No verificado | No se puede verificar desde el repositorio; requiere acceso al aula. |
| Sustentación del corte | No hay evidencia de sesión de sustentación en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_Drift público; integrantes declarados en README y autores en historial (JerryDBM, maufern4ndez, lmpdiaz12, JoshuaR01) | Cumple | El nombre y la organización cumplen el contrato. |
| Estructura mínima | Falta docs/adr/ con nombres correctos (hay 0001 y 0002 pero ambos 'arquitectura-base', no kebab-case descriptivo); docs/c4/ y docs/arc42/ presentes; docs/aspectos.md y docs/ia.md existen | No cumple | La estructura general existe pero los ADR no siguen la convención de nomenclatura. |
| Estado del repositorio calificado | Rama origin/master, hash 74337a3, fecha 2026-09-08T02:53:31Z (anterior al cierre) | Cumple | El estado calificado es el correcto. |
| Convenciones de ADR | docs/adr/0001-arquitectura-base.md y 0002-arquitectura-base.md (hash 74337a3) tienen nombres que no siguen el patrón 'NNNN-titulo-en-kebab-case' (título genérico); ADR-0001 no está marcado como reemplazado formalmente (solo dice 'Superada parcialmente') | No cumple | Los nombres de archivo no son descriptivos y el estado de reemplazo no es explícito. |
| Tabla de aspectos | docs/aspectos.md (hash 74337a3) tiene tabla de 8 columnas pero con enlaces rotos (p.ej. 'arc42_10_requisitos_de_calidad.md' no existe) y celdas 'Pendiente' en E3-E5 | No cumple | La tabla existe pero no es completamente navegable por enlaces incorrectos y huecos. |
| Registro de uso de IA | docs/ia.md (hash 74337a3) con historial de commits desde 2026-08-09 hasta 2026-09-07 (23 commits) | Cumple | El registro existe y crece a lo largo del semestre. |
| README | README.md (hash 74337a3) describe el sistema, comandos de arranque (uvicorn, next) y requisitos previos | Cumple | El README es completo y reproducible. |
| Pipeline y análisis estático | .github/workflows/ci.yml (hash 74337a3) existe y run 34060984657 exitoso, pero no hay configuración de SonarCloud en el repositorio | No cumple | El pipeline existe pero falta el análisis estático con SonarCloud. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `6d0a1b88b48ae1da248f77a09bcd5c52d4e95ff1 2026-09-10T22:21:13-05:00 Fix links in correciones.md to GitHub URLs`
- **Veredicto**: con pendientes
- Resumen: El proyecto está avanzado pero con pendientes de semanas anteriores sin resolver en la rama principal a HEAD.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Correcciones a correcciones.md y enlaces subidas después del cierre (commits 1cab45e, df8f512, 11577b9, 6e275a6, 6d0a1b8, 2026-09-10T22:15:10Z a 22:21:13Z) no estaban en el estado calificado.

Pendientes que siguen abiertos:
- correcciones.md en la raíz (a HEAD sigue en docs/correciones.md).
- Enlaces rotos en docs/aspectos.md y docs/correciones.md.
- Celdas pendientes en la tabla de trazabilidad (E3-E5).
- Nomenclatura de ADR no conforme.
- Falta SonarCloud en el pipeline.

## Recuento y nota sugerida

7 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.3 = 1 + 4 × (7/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula (depende de Moodle).
- Sustentación del corte (depende de la sesión).

## Hallazgos para la planilla

- correcciones.md no existe en la raíz del estado calificado; solo docs/correciones.md (mal escrito y en subcarpeta).
- docs/correciones.md tiene enlaces rotos y referencias a archivos inexistentes (p.ej. arc42_10_requisitos_de_calidad.md).
- Los ADR no siguen la convención de nomenclatura del contrato (títulos genéricos).
- La tabla de aspectos tiene celdas 'Pendiente' y enlaces rotos, afectando la trazabilidad.
- No hay configuración de SonarCloud en el repositorio.
- El equipo subió correcciones después del cierre (commits 1cab45e, df8f512, etc.) que no afectan el estado calificado.
- Commits posteriores al cierre (no calificados): 6d0a1b8 2026-09-10T22:21:13-05:00 Fix links in correciones.md to GitHub URLs; 6e275a6 2026-09-10T22:17:18-05:00 Update correciones.md; 11577b9 2026-09-10T22:16:57-05:00 Fix file references in correciones.md; df8f512 2026-09-10T22:15:26-05:00 Fix link to aspectos.md in correciones.md; 1cab45e 2026-09-10T22:15:10-05:00 Fix file paths in correciones.md
