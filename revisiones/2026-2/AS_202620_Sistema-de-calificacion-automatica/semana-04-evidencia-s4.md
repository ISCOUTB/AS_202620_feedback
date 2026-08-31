# semana-04-evidencia-s4 · Calificación automática

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `cede35e` (2026-08-30T23:51:34-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-ES.md declara secciones 1-6 escritas; commits e40ce90 y cede35e actualizan 5 y 6; sección 1 visible redactada (RF-01..RF-11, QG-1..QG-4, stakeholders) | Cumple | Secciones 2-4 no inspeccionadas en detalle; sin marcadores de plantilla en el texto visible |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/arc42-template-ES.md declara sección 9 escrita; docs/adr/ contiene 0001-0005; tabla de convenciones del arc42 enlaza a ../adr/ | Cumple | Texto de la sección 9 no inspeccionado; respaldado por declaración del documento y existencia de ADRs |
| arc42 sección 10 coherente con los escenarios de la semana 2 | ADR-0002 y ADR-0004 referencian EC-03/EC-04/EC-05; aspectos.md enlaza EC-01..EC-07; sección 10 declarada escrita | Cumple | Coherencia respaldada por referencias cruzadas; texto de sección 10 no inspeccionado |
| Glosario iniciado con términos del dominio | ADR-0004 menciona el glosario del arc42 con términos del dominio (OMR, casilla); sección 12 declarada escrita | Cumple | Términos específicos no visibles; respaldado por declaración del documento |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/doc-c4.md tabla 'Niveles completos \| Nivel 1 (Contexto)'; sección Nivel 2 lista contenedores 'previstos' sin diagrama completo visible | No cumple | El nivel 2 está declarado pero no completo; no se puede confirmar coherencia plena |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Depende del nivel 2, incompleto; estructura de código (backend/api, backend/worker, backend/infraestructura, frontend) sugiere correspondencia | No verificado | Se requiere completar el diagrama de nivel 2 para contrastar contenedores con directorios |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md sección 'Corte vertical' describe navegador→API→ingesta→infraestructura→worker; rutas: frontend/lib/pantalla_carga.dart, backend/ingesta/recepcion.py, backend/infraestructura/almacen.py, backend/worker/main.py | Cumple | Recorrido completo visible y documentado |
| Arranque documentado con un solo comando | README.md 'Cómo se arranca' declara Docker como requisito y 'docker compose up' como comando único | Cumple | Alternativas de desarrollo documentadas sin reemplazar el comando oficial |
| Prueba automatizada del recorrido completo, en verde | .github/workflows/ci.yml existe; README declara 34 pruebas backend y 6 frontend; sin runs_ci en la evidencia | No verificado | Comando para verificar: curl -s https://api.github.com/repos/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs?per_page=20 |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01: columna C4 dice 'C1: Sistema de Calificación OMR · C2 pendiente (S4)'; rutas de código y pruebas existen | No cumple | El hueco en C4 impide la trazabilidad completa hasta Pruebas |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Sistema-de-calificacion-automatica en ISCOUTB, visible; 4 autores en shortlog (scp1109, josueacademico17-source, SusanaRosales, Mariadelmar-restrepo) | Cumple | Nombres visibles sin correos; identidades consolidadas por autor |
| Estructura mínima | docs/arc42/, docs/adr/ (5 archivos), docs/c4/, docs/aspectos.md, docs/ia.md, README.md presentes en el árbol | Cumple | Rutas estándar respetadas |
| Estado que se califica / versionado | cede35e 2026-08-30T23:51:34-05:00 (04:51Z) anterior al cierre 2026-08-31T05:00:00Z; sin commits post cierre | Cumple | Commit vigente correcto para evidencia semanal |
| Convenciones de ADR | 5 ADRs con nombres NNNN-titulo-kebab-case.md; 0001 reemplazado por 0002 sin editar; cada uno con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Convención de no edición respetada |
| Tabla de aspectos | docs/aspectos.md fila A-01 con columna C4 'C2 pendiente (S4)'; hueco en la trazabilidad | No cumple | Las filas declaradas con Pendiente son aceptables; A-01 es la construida y debería tener C4 completo |
| Registro de uso de IA | docs/ia.md con 6 commits (2026-08-07 a 2026-08-30); contenido no visible para verificar columnas de aceptado/rechazado | No verificado | Se requiere inspeccionar docs/ia.md |
| README y pipeline | README cumple (docker compose up, cómo probar); .github/workflows/ci.yml existe pero sin runs_ci | No verificado | Fila agrupada: README Cumple, pipeline No verificado por falta de runs |
| Secretos y autoría | grep de secretos sin coincidencias; sin .env versionado; 4 autores con 34+16+7+3 commits | Cumple | Sin incidentes de secretos; contribución distribuida |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `cede35e4229f8dae2aad95e6ffe92b453b4715a8 2026-08-30T23:51:34-05:00 Las secciones 5 y 6 describen el estado real del código`
- **Veredicto**: con pendientes
- Resumen: Proyecto con avance sustancial: corte vertical A-01 construido, ADRs sólidos, README reproducible. Faltan C4 nivel 2 completo y verificación de CI en verde.

Pendientes que siguen abiertos:
- C4 nivel 2 incompleto en docs/c4/doc-c4.md
- Fila A-01 de aspectos.md con C2 pendiente
- Verificación de CI sin runs
- Secciones 7 y 8 del arc42 pendientes (declarado)

## Recuento y nota sugerida

6 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.4 = 1 + 4 × (6/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- C4 nivel 2: diagrama no visible; se requiere completar doc-c4.md
- Prueba en CI: sin runs_ci; comando: curl -s https://api.github.com/repos/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs?per_page=20
- docs/ia.md: contenido no visible para verificar columnas de aceptado/rechazado

## Hallazgos para la planilla

- C4 nivel 2 declarado pendiente en doc-c4.md; solo Nivel 1 completo
- Fila A-01 de aspectos.md con hueco en C4 ('C2 pendiente (S4)')
- Sin runs de CI visibles; no se confirma pipeline en verde
- docs/ia.md con historial pero sin contenido verificado
- ADR-0001 reemplazado por 0002 sin editar; convención respetada
- Cuatro autores con contribuciones distribuidas en el historial
