# semana-06-evidencia-s6 · Clubs UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `4ede977` en `origin/master` (2026-09-06T22:41:55-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | No existe mapa de contextos en el árbol; docs/c4/contexto.md solo tiene C4 nivel 1 y 2 (personas y contenedores, no contextos delimitados). | No cumple | Faltan relaciones tipificadas (núcleo compartido, cliente-proveedor, capa anticorrupción). |
| Tabla módulo a datos con dueño único por entidad | No hay tabla módulo-datos en ningún archivo del repositorio. | No cumple | Se requiere tabla que asigne dueño único a cada entidad. |
| La tabla cubre las entidades que existen en el código | Entidad Publicacion en backend/src/linkclub/domain/publicacion.py; no hay migraciones ni esquema SQL en el árbol. | No cumple | Sin tabla no hay cobertura; faltan archivos .sql o migraciones. |
| Violaciones de propiedad de datos detectadas sobre el código actual | No hay lista de violaciones; escrituras a Publicacion en backend/src/linkclub/application/use_cases/crear_publicacion.py y backend/src/linkclub/adapters/outbound/persistence/in_memory_publicacion_adapter.py sin auditoría. | No cumple | La auditoría sobre el código actual no está documentada. |
| Plan de corrección por violación | No existe ningún plan de corrección en el repositorio. | No cumple | Cada violación debe tener acción concreta asociada. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/ no contiene 08*; solo 01-06, 09, 10, 12. | No cumple | Falta la sección 8 completa. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/contexto.md solo tiene niveles 1 y 2; único ADR es docs/adr/0001-hexagonal.md (sin reajuste de límites). | No cumple | No hay C4 nivel 3 ni ADR de reajuste; no se pudo comparar con S5 por falta de hash. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md tiene 6 filas (U1-U3, C1-C3) pero no hay mapa de contextos al cual relacionarlas. | No cumple | Los aspectos quedan sin contexto delimitado. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_Clubs_UTB público; autores consolidados: deortahollman-star, Josh4OP/Josh Ortega, devZavod, Luis-Salas-Reyes/Luis Daniel. | Cumple | Los 4 integrantes declarados tienen commits. |
| Estructura mínima | Faltan docs/arc42/07, 08 y 11; el resto de la estructura mínima existe. | No cumple | La sección 8 es además requerida por la ficha S6. |
| Estado del repositorio que se califica | Hash 4ede977 (2026-09-06T22:41:55-05:00) anterior al cierre 2026-09-14T05:00:00Z; sin commits posteriores. | Cumple | Rama master. |
| Convenciones de ADR | docs/adr/0001-hexagonal.md sigue NNNN-titulo-kebab-case.md con contexto, alternativas, decisión, consecuencias y trazabilidad. | Cumple | Un solo ADR, sin reescrituras. |
| La tabla de aspectos | docs/aspectos.md tiene 8 columnas pero filas U1, U3, C1, C2, C3 con celdas 'Pendiente' o '—'. | No cumple | Filas con huecos no defendibles. |
| Registro de uso de IA | docs/ia.md registra 7 usos con herramienta, para qué y motivo; log crece desde 2026-08-09. | Cumple | La columna de rechazo está implícita en 'Motivo'. |
| README | README.md documenta arranque en 4 pasos (venv, activate, pip install, uvicorn); no hay un solo comando. | No cumple | El contrato exige arranque con un solo comando. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml ejecuta pytest con éxito (runs_ci); no hay SonarCloud configurado. | No cumple | Falta análisis estático SonarCloud. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `4ede977c7cccc335d878019ce06cba2e23cf76d2 2026-09-06T22:41:55-05:00 quite el C2 y lo reemplaze con el C3`
- **Veredicto**: con pendientes
- Resumen: La entrega de la semana 6 no contiene ninguno de los artefactos requeridos. El repositorio tiene documentación parcial de semanas anteriores (arc42 01-06, 09, 10, 12; ADR 0001; aspectos; IA; CI) pero la ficha S6 está completamente pendiente a HEAD (4ede977).

Pendientes que siguen abiertos:
- Mapa de contextos con relaciones tipificadas
- Tabla módulo a datos con dueño único
- Lista de violaciones con plan de corrección
- arc42 sección 8
- C4 nivel 3 y ADR de reajuste
- Completar secciones 07 y 11 de arc42
- SonarCloud en pipeline

## Recuento y nota sugerida

0 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Comparación con S5: no se proporcionó el hash de la revisión de S5, por lo que no se pudo verificar si los límites cambiaron desde el primer corte.

## Hallazgos para la planilla

- No existe docs/arc42/08* (sección 8) requerida por la ficha S6.
- No hay mapa de contextos delimitados con relaciones tipificadas.
- No hay tabla módulo a datos con dueño único.
- No hay lista de violaciones de propiedad de datos ni plan de corrección.
- No hay C4 nivel 3 ni ADR de reajuste de límites.
- docs/aspectos.md tiene filas con celdas Pendiente (huecos).
- Faltan secciones 07 y 11 de arc42.
- Pipeline sin SonarCloud; solo GitHub Actions.
- Matriz transversal: 4 de 8 criterios cumplidos.
