# semana-05-corte1 · Clubs UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `91323d6` (2026-08-30T23:21:56-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Sin etiqueta en git tag --list; commit calificado 91323d6 (2026-08-30T23:21:56-05:00) | No cumple | Se revisa el último commit anterior al cierre por ausencia de etiqueta. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Adjunto de Moodle no accesible desde el repositorio | No verificado | Depende de la entrega en Moodle; no verificable aquí. |
| Impacto de la restricción localizado en requisitos, C4 y código | Sin sección 11 en docs/arc42/ ni ADR nuevo; solo docs/adr/0001-hexagonal.md (2026-08-23) | No cumple | No hay diagnóstico del reto en el repositorio; se desconoce la restricción asignada. |
| Línea base medida y verificable antes del cambio | No hay cifra con herramienta y procedimiento en el repositorio | No cumple | Falta medición inicial. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/ solo contiene 0001-hexagonal.md; sin ADR nuevo del corte | No cumple | El ADR existente es de semanas anteriores. |
| Cambio implementado y ejecutable de extremo a extremo | Commit 91323d6 solo corrige README y sección 6.1; sin cambios de código del reto | No cumple | No hay implementación nueva. |
| Límites declarados conservados tras el cambio | Sin cambio del reto que evaluar; C4 en docs/c4/contexto.md | No verificado | No aplica por ausencia de cambio. |
| Prueba que cubre el cambio, en verde en el pipeline | backend/tests/test_health.py cubre health check base; run success 33356832664 | No cumple | La prueba no cubre un cambio del reto. |
| Resultado contrastado con el umbral del escenario y reproducible | Sin medición con herramienta, carga y procedimiento en el repositorio | No cumple | No hay contraste con umbral. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md tiene celdas 'Pendiente' y carece de columna Evidencia | No cumple | La fila U2 no es navegable de punta a punta. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md registra S1-S4; sin entradas de la semana 5 | No cumple | No hay registro de IA de este corte. |
| Sustentación del reto | Sesión de sustentación no verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_Clubs_UTB visible; shortlog: Zavod Dev, Josh Ortega, Luis-Salas-Reyes, deortahollman-star | Cumple | 4 identidades consolidadas coinciden con los integrantes declarados. |
| Estructura mínima | Árbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura completa. |
| Estado del repositorio que se califica | Sin etiqueta corte-1; commit 91323d6 (2026-08-30T23:21:56-05:00) | No cumple | Etiqueta ausente; se revisa último commit anterior al cierre. |
| Convenciones de ADR | docs/adr/0001-hexagonal.md con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Cumple formato y contenido; sin reescrituras. |
| La tabla de aspectos | docs/aspectos.md tiene columnas ID, Aspecto, Escenario, Requisito, C4, ADR, Código, Pruebas; sin Evidencia y con 'Pendiente' | No cumple | Falta la columna Evidencia del contrato y hay huecos. |
| Registro de uso de IA | docs/ia.md con entradas S1-S4; sin entradas de la semana 5 | No cumple | No crece en este corte. |
| README | README.md describe el sistema, arranque (venv, pip, uvicorn) y pruebas (pytest) | Cumple | Arranque reproducible aunque en varios pasos. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml corre pytest; runs success; sin SonarCloud | No cumple | Falta análisis estático SonarCloud (isco-utb). |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `91323d6b4e4cfccbc66add5802b29f100dc34be6 2026-08-30T23:21:56-05:00 Correción de parrafo en sección 6.1 y corrección del readme`
- **Veredicto**: con pendientes
- Resumen: El proyecto conserva la documentación base, pero la entrega del corte 1 no implementa el reto: faltan etiqueta, ADR, diagnóstico, cambio, medición y trazabilidad.

Pendientes que siguen abiertos:
- Etiqueta corte-1 ausente
- ADR del reto no creado
- Diagnóstico y línea base no documentados
- Cambio no implementado
- Medición no aportada
- Tabla de aspectos incompleta
- Registro IA sin entrada de S5
- Análisis estático SonarCloud ausente

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- PDF de dos páginas (adjunto Moodle no accesible)
- Límites declarados conservados tras el cambio (sin cambio del reto)
- Sustentación del reto (sesión presencial)

## Hallazgos para la planilla

- No existe la etiqueta corte-1; se revisa el commit 91323d6.
- No hay ADR nuevo del reto; solo 0001-hexagonal de semanas anteriores.
- docs/aspectos.md no tiene la columna Evidencia y varias celdas están en Pendiente.
- docs/ia.md no registra usos de la semana 5.
- No hay medición ni línea base verificable en el repositorio.
- El pipeline corre en verde pero solo cubre el health check de la línea base.
- Falta análisis estático SonarCloud.
