# semana-04-evidencia-s4 · EnAgenda

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `b8582c6` (2026-08-29T23:06:57-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/02 y 03 redactadas; 01,04,05,06 no incluidas en la evidencia | No verificado | Falta contenido de 01,04,05,06 para comprobar redacción y ausencia de plantilla. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09-decisiones-de-arquitectura.md: 'Esta sección se completará...' | No cumple | Texto de plantilla, sin enlaces a ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10-requisitos-de-calidad.md incluye EC-01 a EC-05 coherentes con ADR | Cumple | Escenarios detallados y alineados con el dominio. |
| Glosario iniciado con términos del dominio | docs/arc42/12-glosario.md: 'Esta sección se completará...' | No cumple | Sin términos del dominio. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/nivel-1-contexto.md y nivel-2-contenedores.md con actores y sistema coincidentes | Cumple | Actores Organizador e Invitado reaparecen; contenedores dentro del sistema. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No hay directorios de código; solo docs/ | No cumple | Contenedores webApp, portalInvitado, api, database sin código correspondiente. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Sin archivos de código fuente | No cumple | No se identifican rutas de interfaz, lógica ni persistencia. |
| Arranque documentado con un solo comando | README.md sin sección de arranque ni requisitos | No cumple | No declara comando único. |
| Prueba automatizada del recorrido completo, en verde | Sin pruebas ni pipeline | No cumple | No hay código ni CI. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 con celdas 'Pendiente' en C4, ADR, Código, Pruebas, Evidencia | No cumple | Fila incompleta, huecos. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_EnAgenda visible; autores: 3 cuentas con commits | Cumple | Tres autores corresponden a integrantes declarados. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Estructura conforme. |
| Estado calificado/versionado | Commit b8582c6 antes del cierre, sin etiqueta corte-1 | No cumple | Etiqueta ausente; se revisó último commit. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md sin trazabilidad con commit/PR ni pruebas | No cumple | Falta trazabilidad completa. |
| Tabla de aspectos | docs/aspectos.md fila A-01 con celdas 'Pendiente' | No cumple | Fila con huecos, no defendible. |
| Registro de uso de IA | docs/ia.md con entradas que incluyen qué se rechazó y por qué | Cumple | Registro adecuado. |
| README | README.md sin comando de arranque ni requisitos previos | No cumple | No cumple reproducibilidad. |
| Pipeline y análisis estático | No existe .github/workflows/ | No cumple | Sin CI ni SonarCloud. |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de docs/arc42/01,04,05,06 no incluido en la evidencia; no se pudo verificar redacción.
- Ejecución de arranque y pruebas no verificada por ausencia de código y pipeline.

## Hallazgos para la planilla

- No hay código fuente en el repositorio.
- Sección 9 de arc42 sin redactar.
- Glosario vacío.
- Fila de aspectos incompleta.
- ADR sin trazabilidad de commit/PR/pruebas.
- README sin instrucciones de arranque.
- Sin pipeline de CI.
- Sin etiqueta de corte.
