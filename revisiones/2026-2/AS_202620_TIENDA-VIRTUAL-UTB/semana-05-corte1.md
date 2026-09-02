# semana-05-corte1 · Tienda virtual UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `0d401a9` (2026-09-01T09:30:26-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Commit 0d401a9 (2026-09-01T09:30:26-05:00) anterior al cierre; sin salida de `git tag --list` ni `git log -1 corte-1` | No verificado | El commit calificado es anterior al cierre y su mensaje es 'Corte 1', pero no se confirma la existencia de la etiqueta. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Adjunto en Moodle, no accesible desde el repositorio | No verificado | Lo resuelve el docente con la entrega en Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | No se suministró la restricción asignada al equipo; sin ella no se puede juzgar | No verificado | Falta la restricción asignada; en el repositorio no hay apartado de diagnóstico del reto. |
| Línea base medida y verificable antes del cambio | No hay cifra con herramienta y procedimiento en el repositorio | No verificado | Sin la restricción no se sabe qué medir; no se halló medición baseline. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/ solo contiene 0001-monolito-modular.md y .gitkeep | No cumple | No existe un ADR nuevo del reto; el único ADR es de la S3. |
| Cambio implementado y ejecutable de extremo a extremo | No hay commit que implemente un ADR del reto; README.md documenta `docker compose up --build` para el corte vertical S4 | No cumple | Sin ADR del reto no hay cambio que implementar. |
| Límites declarados conservados tras el cambio | docs/c4/context.md y container.md coinciden con la estructura de módulos, pero no hay cambio del reto | No verificado | No hay cambio del reto que evaluar. |
| Prueba que cubre el cambio, en verde en el pipeline | Run 'Pruebas' 33462227003 success (2026-09-01T02:21:21Z, https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/33462227003) ejecuta test_catalog/test_architecture/test_health; ninguna cubre un cambio del reto | No cumple | Los runs verdes son del corte vertical S4. |
| Resultado contrastado con el umbral del escenario y reproducible | No se halló medición con herramienta, carga y procedimiento en el repositorio | No cumple | Falta la medición del reto contrastada con umbral. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md tiene 6 columnas y no hay fila del reto | No cumple | La fila de disponibilidad enlaza escenario→decisión→código→pruebas, pero faltan columnas ID/C4/Evidencia y no hay fila del reto. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md tiene entradas hasta 2026-08-31 (a8c5dcc) referidas a S1-S4 | No cumple | Ninguna entrada se refiere al trabajo del reto del corte 1. |
| Sustentación del reto | Sesión de sustentación, no verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB visible; shortlog HEAD consolida 4 autores (RAZOR7150, Jasen/Jasen Yukopila, pxtroniwnl, shalom-A26) y README.md declara 4 integrantes | Cumple | Jasen y Jasen Yukopila se consolidan como una misma cuenta. |
| Estructura mínima | Árbol HEAD incluye README.md, docs/arc42/arc42-template-EN.md, docs/adr/0001-monolito-modular.md, docs/c4/context.md, docs/c4/container.md, docs/aspectos.md, docs/ia.md | Cumple | Hay además .gitkeep en docs/adr y docs/c4, sin afectar la estructura. |
| Estado del repositorio que se califica | Commit 0d401a9 (2026-09-01T09:30:26-05:00) anterior al cierre; sin salida de `git tag --list` | No verificado | No se puede confirmar la etiqueta `corte-1`; el commit calificado es anterior al cierre. |
| Convenciones de ADR | docs/adr/0001-monolito-modular.md (2026-08-21) con contexto, alternativas, decisión, consecuencias y trazabilidad; nombre según convención | Cumple | Solo hay un ADR; no se observan reescrituras. |
| Tabla de aspectos | docs/aspectos.md tiene columnas Aspecto, Escenario, Prioridad, Decisión, Ubicación, Pruebas; faltan ID, C4 y Evidencia como columnas separadas | No cumple | La cadena no es navegable en el formato de 8 columnas del contrato. |
| Registro de uso de IA | docs/ia.md con tabla de fecha, herramienta, propósito, resultado, descartes y validación; 9 commits en el historial (último a8c5dcc 2026-08-31) | Cumple | Varias celdas de descartes quedan 'Sin declarar'. |
| README | README.md con descripción, requisitos, comando único `docker compose up --build` y sección de pruebas | Cumple | El arranque documentado corresponde al corte vertical S4. |
| Pipeline y análisis estático | .github/workflows/tests.yml solo ejecuta pytest; no hay configuración de SonarCloud en el repositorio | No cumple | Los runs de CI están en verde, pero falta el análisis estático exigido. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `0d401a9a7691cb66b5174edc188ec2f21048aa2d 2026-09-01T09:30:26-05:00 Corte 1`
- **Veredicto**: con pendientes
- Resumen: El corte vertical S4 está en verde y la documentación base existe, pero el reto del corte 1 no se evidencia en el repositorio: sin ADR, sin diagnóstico de la restricción, sin medición ni trazabilidad del cambio.

Pendientes que siguen abiertos:
- Resolver el reto del corte 1: ADR con alternativas y consecuencias, diagnóstico con línea base, cambio implementado y medición contra umbral.
- Completar docs/aspectos.md con las 8 columnas del contrato.
- Configurar SonarCloud en el pipeline.
- Registrar en docs/ia.md los usos de IA del corte 1 con descartes y motivos.

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- Etiqueta `corte-1`: falta salida de `git tag --list` y `git log -1 corte-1`.
- PDF de dos páginas: adjunto en Moodle, no accesible desde el repositorio.
- Impacto de la restricción: falta conocer la restricción asignada al equipo.
- Línea base medida: falta la restricción y el procedimiento de medición.
- Límites conservados tras el cambio: no hay cambio del reto que evaluar.
- Sustentación: se califica en sesión.

## Hallazgos para la planilla

- No se evidencia la etiqueta `corte-1`; el commit calificado 0d401a9 es anterior al cierre.
- No se conoce la restricción asignada al equipo, requisito previo para juzgar el diagnóstico.
- No existe ADR del reto; docs/adr/ solo tiene el 0001 de la S3.
- No hay medición baseline ni resultado contrastado con umbral en el repositorio.
- docs/aspectos.md no tiene las 8 columnas exigidas por el contrato.
- Falta análisis estático en SonarCloud; el workflow solo ejecuta pytest.
- docs/ia.md no registra usos de IA referidos al reto del corte 1.
- Los runs de CI en verde cubren las pruebas del corte vertical S4, no un cambio del reto.
- La tabla de aspectos marca rendimiento y usabilidad como parcialmente cubiertos, pendientes de orders/identity.
- El apartado 11 del contrato no fue incluido en la entrada; la matriz transversal se evalúa con los criterios de las secciones 1-8 del contrato.
