# semana-06-evidencia-s6 · CampusMarket

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `8044215` en `origin/master` (2026-09-06T16:05:15-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | Árbol de HEAD 8044215 sin archivo de mapa de contextos; docs/arc42/05 describe módulos técnicos, no contextos del dominio | No cumple | No hay diagrama ni tabla con contextos y relaciones (núcleo compartido, cliente-proveedor, capa anticorrupción) |
| Tabla módulo a datos con dueño único por entidad | No existe tabla módulo-datos en el árbol de HEAD 8044215 | No cumple | Falta el artefacto completo |
| La tabla cubre las entidades que existen en el código | No hay tabla que contrastar; el único acceso a datos es backend/app/publicaciones/repository.py | No cumple | Sin tabla no se puede verificar cobertura de entidades |
| Violaciones de propiedad de datos detectadas sobre el código actual | No hay lista de violaciones en el árbol de HEAD 8044215 | No cumple | La auditoría sobre código actual no está documentada |
| Plan de corrección por violación | No hay plan de corrección asociado a violaciones | No cumple | Falta el plan |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | No existe docs/arc42/08* en el árbol de HEAD 8044215 | No cumple | La sección 8 de arc42 no está presente |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | commits_nuevos_desde_cierre_anterior: (sin commits nuevos); no hay ADR que reemplace 0001 | Cumple | No hay cambios de límites desde S5, por lo que el requisito condicional no se activa |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md existe pero no hay mapa de contextos con el cual relacionar las filas | No cumple | Sin mapa, los aspectos no tienen contexto asignado |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible: true; repo AS_202620_PROYECTO_CAMPUSMARKET en ISCOUTB; autores: Nnigarp, camilixo92, Carulla-sd | Cumple | Los tres integrantes aparecen en el historial |
| Estructura mínima | docs/arc42/ARC42.md, docs/adr/0001 y 0002, docs/c4/01 y 02, docs/aspectos.md, docs/ia.md, README.md en HEAD 8044215 | Cumple | Directorio docs/arc42 presente con índice ARC42.md |
| Estado del repositorio que se califica | origin/master, hash 8044215, fecha 2026-09-06T16:05:15-05:00, anterior al cierre 2026-09-14T05:00:00Z | Cumple | Commit vigente al cierre correctamente identificado |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md y 0002-manejo-bloqueo-sqlite.md con contexto, alternativas, decisión y consecuencias | Cumple | Nombres en kebab-case y numeración de 4 dígitos |
| Tabla de aspectos | docs/aspectos.md con columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia y filas ASP-01 a ASP-06 | Cumple | Cadena de trazabilidad presente |
| Registro de uso de IA | docs/ia.md existe con 14 commits de log (2026-08-08 a 2026-09-06), pero no se muestra su contenido | No verificado | No se pudo verificar las columnas de aceptado/rechazado; haría falta leer docs/ia.md |
| README | README.md con descripción, arranque con scripts/run_s4.ps1 y run_s4.sh, y pruebas con pytest y flutter analyze | Cumple | Arranque con un solo comando documentado |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml existe; sin runs_ci con URL de ejecución | No verificado | Haría falta un run de GitHub Actions o SonarCloud; comando: curl a api.github.com/repos/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `8044215811e53b111888f75b30fc175fb889dc56 2026-09-06T16:05:15-05:00 Merge pull request #32 from ISCOUTB/S5-alinear-redaccion-r07`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene una base sólida de S1-S5 (ADR, arc42 parcial, C4 niveles 1-2, aspectos, IA, README, workflow), pero la entrega S6 está vacía: no hay ningún artefacto de contextos delimitados ni propiedad de datos en HEAD 8044215.

Pendientes que siguen abiertos:
- Mapa de contextos con relaciones tipificadas
- Tabla módulo a datos con dueño único
- Lista de violaciones de propiedad de datos con plan de corrección
- Sección 8 de arc42 con lenguaje ubicuo y mapa de contextos
- C4 nivel 3 y ADR si los límites cambian

## Recuento y nota sugerida

1 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.5 = 1 + 4 × (1/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de docs/ia.md (columnas de aceptado/rechazado)
- Ejecución de pipeline: no hay runs_ci con URL

## Hallazgos para la planilla

- La entrega S6 no contiene artefactos nuevos: no hay mapa de contextos, tabla módulo-datos ni lista de violaciones
- No existe docs/arc42/08* (sección 8 de arc42)
- No existe C4 nivel 3 ni ADR de reajuste de límites
- El commit 8044215 es anterior al cierre pero solo contiene el trabajo de S1-S5
- Los módulos backend distintos de publicaciones están vacíos, por lo que no hay escrituras múltiples detectables
