# semana-04-evidencia-s4 · ShareU

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `27e1190` (2026-08-30T15:22:02-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42.md (árbol HEAD 27e1190) | No verificado | No se dispone del contenido del archivo; no se pueden comprobar encabezados ni ausencia de texto de plantilla. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/arc42.md; docs/adr/0001-estilo-arquitectonico.md | No verificado | Existen ambos archivos, pero sin contenido no se verifica la cita al ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/arc42.md | No verificado | Sin contenido no se puede contrastar con los escenarios previos. |
| Glosario iniciado con términos del dominio | docs/arc42/arc42.md | No verificado | No se pudo localizar la sección 12 ni sus términos propios. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/nivel1.mmd, docs/c4/nivel2.mmd, docs/c4/nivel-2.md, docs/c4/NIVEL2.png | No verificado | Archivos presentes; coherencia entre niveles no verificable sin leer los diagramas. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/nivel2.mmd; app/{administracion,busqueda,calificaciones,documentos,usuarios}/ | No verificado | El código tiene módulos por dominio, pero no se pudo contrastar con el diagrama. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | app/main.py, app/busqueda/router.py, app/busqueda/service.py, app/documentos/repository.py | No verificado | Rutas candidatas presentes; sin leer el flujo no se confirma el recorrido completo. |
| Arranque documentado con un solo comando | README.md | No verificado | README presente; no se pudo verificar el comando declarado ni los requisitos previos. |
| Prueba automatizada del recorrido completo, en verde | tests/test_busqueda.py, tests/test_esqueleto.py, .github/workflows/tests.yml; runs_ci vacío | No verificado | Hay pruebas y workflow, pero no hay URL de run en verde; comando de verificación: curl API actions/runs. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos/aspectos.md | No verificado | Archivo presente en ruta desviada; sin contenido no se verifican celdas ni destinos. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible=true, repo=AS_202620_ShareU, org=ISCOUTB; shortlog: 1 steven | No cumple | Repositorio correcto, pero solo un autor en el historial frente a cuatro integrantes declarados. |
| Estructura mínima | Árbol HEAD: docs/arc42/, docs/adr/, docs/c4/, docs/ia.md, README.md, .github/workflows/tests.yml | Cumple | docs/aspectos.md está en docs/aspectos/aspectos.md; desviación registrada, no ausencia. |
| Estado calificado / versionado | hash 27e1190, fecha 2026-08-30T15:22:02-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Commit vigente al cierre correcto; HEAD coincide sin commits posteriores. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md | No verificado | Nombre cumple el patrón; contenido (contexto, opciones, trazabilidad) no disponible. |
| Tabla de aspectos | docs/aspectos/aspectos.md | No verificado | Ruta desviada; no se pudo verificar columnas ni enlaces. |
| Registro de uso de IA | docs/ia.md; ia_log sin commits propios | No verificado | Archivo presente, pero sin historial ni contenido no se verifica el registro de usos y rechazos. |
| README y reproducibilidad | README.md | No verificado | No se pudo leer el comando de arranque ni los requisitos previos. |
| Pipeline y análisis estático | .github/workflows/tests.yml; runs_ci vacío | No verificado | Workflow presente, pero sin runs no hay evidencia de ejecución; no se ve configuración de SonarCloud. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `27e1190a0a2a5b759f002f7e37a979c78a18d0ce 2026-08-30T15:22:02-05:00 Completar estructura y documentacion del proyecto`
- **Veredicto**: con pendientes
- Resumen: HEAD coincide con el commit calificado 27e1190 (2026-08-30T15:22:02-05:00), anterior al cierre; no hay commits posteriores ni correcciones tardías. La estructura base está presente, pero la mayoría de los criterios no pudieron verificarse por falta de contenido y de runs de CI; además, el historial muestra un solo autor. Ficha: 0/10; transversal: 2/8.

Pendientes que siguen abiertos:
- Verificar contenido de docs/arc42/arc42.md (secciones 1-6, 9, 10, 12)
- Verificar coherencia C4 nivel 1/2 y correspondencia con código
- Verificar recorrido del corte vertical en app/
- Verificar comando de arranque en README.md
- Obtener run de CI en verde para tests/test_busqueda.py
- Verificar fila de docs/aspectos/aspectos.md
- Verificar contenido de docs/adr/0001-estilo-arquitectonico.md
- Verificar docs/ia.md
- Incorporar a los integrantes faltantes al historial

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de docs/arc42/arc42.md (secciones 1-6, 9, 10, 12)
- Coherencia C4 nivel 1/2 y correspondencia con código
- Recorrido del corte vertical en app/
- Comando de arranque en README.md
- Prueba en verde: runs_ci vacío
- Fila de docs/aspectos/aspectos.md
- Contenido de docs/adr/0001-estilo-arquitectonico.md
- Contenido de docs/ia.md

## Hallazgos para la planilla

- Un solo autor en el historial (steven) frente a cuatro integrantes declarados.
- docs/aspectos.md está en docs/aspectos/aspectos.md, desviación de la ruta mínima.
- runs_ci vacío: no hay evidencia de ejecución del pipeline en verde.
- docs/ia.md presente pero sin commits propios; no se pudo verificar contenido.
- arc42 en un único archivo docs/arc42/arc42.md; no se pudo verificar secciones redactadas.
- C4 nivel 1 y 2 presentes como .mmd y PNG; coherencia no verificada sin contenido.
- No hay commits posteriores al cierre; HEAD coincide con el estado calificado.
