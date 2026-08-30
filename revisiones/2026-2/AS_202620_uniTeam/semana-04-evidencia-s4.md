# semana-04-evidencia-s4 · uniTeam

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `dc14298` (2026-08-29T11:49:10-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-uniteam.md: estado indica secciones 1-6 redactadas; contenido muestra secciones 1 y 2 sin placeholders | Cumple | Se observan secciones 1 y 2 redactadas; el resto se infiere del estado del documento. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se incluye contenido de la sección 9 en la evidencia | No verificado | Falta ver el texto de la sección 9 para comprobar enlaces a ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se incluye contenido de la sección 10 en la evidencia | No verificado | Falta ver el texto de la sección 10 y su correspondencia con escenarios. |
| Glosario iniciado con términos del dominio | No se incluye contenido de la sección 12 en la evidencia | No verificado | Falta ver el glosario para confirmar términos propios del sistema. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/nivel1-contexto.md y docs/c4/nivel2-contenedores.md existen | No verificado | No se pudo verificar coherencia entre niveles por falta de contenido de los diagramas. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | README.md arquitectura muestra contenedores; árbol incluye web/, app/, compose.yaml | Cumple | Los contenedores Aplicación Web, API y Base de datos corresponden a web/, app/ y MySQL en compose. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | docs/aspectos.md A-01 enlaza page.tsx, rutas_tareas.py, servicio_tareas.py; árbol confirma rutas | Cumple | Interfaz: web/app/proyectos/[id]/page.tsx; lógica: app/application/servicio_tareas.py; persistencia: app/infrastructure/repositorios.py. |
| Arranque documentado con un solo comando | README.md sección Arranque rápido: `docker compose up` | Cumple | Requisitos previos declarados: Docker con Compose. |
| Prueba automatizada del recorrido completo, en verde | test/test_corte_vertical.py existe, pero no hay URL de run en verde | No verificado | Falta evidencia de ejecución en CI; comando declarado: pytest (implícito en workflow). |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 con ID, aspecto, requisito, C4, ADR, código y pruebas; destinos existen en árbol | Cumple | La fila A-01 enlaza correctamente a RF-01, C4 nivel2, ADR 0002, código y test. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_uniTeam, visible true, organización ISCOUTB | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima | Árbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Todas las rutas requeridas presentes. |
| Estado calificado | commit dc14298 fecha 2026-08-29T11:49:10-05:00 anterior al cierre | Cumple | Commit vigente correcto. |
| Convenciones de ADR | ADR 0001-0005 con nombres en kebab-case, uno por decisión | Cumple | ADR 0001 marcado como reemplazado, sin edición posterior visible. |
| Tabla de aspectos | docs/aspectos.md fila A-01 con todas las columnas y enlaces válidos | Cumple | Al menos una fila completa y navegable. |
| Registro de uso de IA | docs/ia.md presente y con historial de commits (ia_log) | Cumple | El archivo crece a lo largo del semestre. |
| README | README.md con arranque rápido y requisitos previos | Cumple | Comando único documentado. |
| Pipeline y análisis estático | .github/workflows/ci.yml existe, pero sin evidencia de runs ni SonarCloud | No verificado | Falta URL de run en verde y configuración de SonarCloud. |

## Recuento y nota sugerida

5 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.0 = 1 + 4 × (5/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 sección 9 enlazada con ADR
- arc42 sección 10 coherente con escenarios
- glosario con términos del dominio
- coherencia C4 nivel 1 y 2
- prueba automatizada en verde (URL de run)
- pipeline con análisis estático SonarCloud

## Hallazgos para la planilla

- Secciones 9, 10 y 12 de arc42 no visibles en la evidencia; no se pudo verificar su contenido.
- No hay evidencia de ejecución de CI en verde para la prueba del corte vertical.
- No se pudo verificar coherencia entre C4 nivel 1 y 2 por falta de contenido de diagramas.
- No se encontró configuración de SonarCloud en el repositorio.
