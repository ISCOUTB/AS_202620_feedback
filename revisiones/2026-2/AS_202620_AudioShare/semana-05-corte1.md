# semana-05-corte1 · AudioShare

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `dd2025c` (2026-09-01T09:56:35-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | estado calificado dd2025c 2026-09-01T09:56:35-05:00 anterior al cierre; sin salida de `git tag --list` ni `git log -1 corte-1` | No verificado | Falta confirmar existencia de la etiqueta. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay acceso al adjunto de Moodle en la evidencia del repositorio | No verificado | Revisar en la plataforma Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | No se informa cuál fue la restricción asignada al equipo | No verificado | Sin la restricción no se puede juzgar el diagnóstico. |
| Línea base medida y verificable antes del cambio | No se halló cifra con herramienta y procedimiento en el repositorio; PDF no disponible | No verificado | Revisar PDF o arc42 sección 11. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/0001-usar-monolito-modular.md existe con alternativas y consecuencias, pero no se puede ligar al reto sin la restricción | No verificado | ADR en estado propuesto y con implementación pendiente. |
| Cambio implementado y ejecutable de extremo a extremo | Commit dd2025c implementa corte vertical A-01; README documenta npm install/npm run dev/npm test; runs_ci vacío | No verificado | Falta evidencia de ejecución real. |
| Límites declarados conservados tras el cambio | docs/c4/Contenedor - Nivel 2.mmd declara WebApp, DiscoverySvc, SignalingSvc y MediaEngine; src/ implementa un único proceso Express con módulos session/audio/sync | No cumple | Los límites del C4 no corresponden con la implementación. |
| Prueba que cubre el cambio, en verde en el pipeline | tests/a01.test.ts y tests/health.test.ts existen; runs_ci vacío | No verificado | Falta URL de run en verde anterior a la etiqueta. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay medición con herramienta, carga y procedimiento en el repositorio; PDF no disponible | No verificado | Revisar PDF. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md usa columnas ID, Aspecto, Escenario, Objetivo/métrica, Decisión, ADR, Implementación, Pruebas; faltan Requisito, C4 y Evidencia; pruebas específicas pendientes | No cumple | Cadena no navegable de punta a punta. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md registra hasta Semana 4; sin entrada del corte 1 (semana 5) | No cumple | Falta uso de IA de este corte. |
| Sustentación del reto | La sustentación se resuelve en sesión | No verificado | Lo fija el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo ISCOUTB/AS_202620_AudioShare visible; shortlog muestra 4 autores | Cumple | Ninguna. |
| Estructura mínima | README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md presentes | Cumple | arc42 en .adoc, se acepta como desviación menor. |
| Estado del repositorio que se califica | hash dd2025c anterior al cierre; sin evidencia de etiqueta corte-1 | No verificado | Falta salida de git tag --list. |
| Convenciones de ADR | ADR 0001 en estado propuesto; trazabilidad con 'Pendiente por resolver' y 'Pendiente de implementar la prueba' | No cumple | La trazabilidad exigida no está completa. |
| Tabla de aspectos | docs/aspectos.md no tiene columnas Requisito, C4 y Evidencia; celdas de pruebas pendientes | No cumple | Formato no coincide con el contrato. |
| Registro de uso de IA | docs/ia.md con tabla de usos, resultados y propuestas rechazadas con motivo | Cumple | Sin entradas del corte actual. |
| README | README.md con descripción, requisitos, comandos de arranque y prueba | Cumple | Ninguna. |
| Pipeline y análisis estático | sin .github/workflows/ en el árbol; runs_ci vacío | No cumple | No hay CI configurada ni runs. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `dd2025cf5ebd8d637a4ca1bbdca3532fafcaf84a 2026-09-01T09:56:35-05:00 Merge pull request #2 from ISCOUTB/feature/A01-corte-vertical`
- **Veredicto**: con pendientes
- Resumen: El repositorio tiene documentación y corte vertical, pero la entrega del reto carece de evidencia verificable en varios criterios clave.

Pendientes que siguen abiertos:
- Confirmar etiqueta corte-1
- Obtener restricción asignada
- Completar trazabilidad en docs/aspectos.md
- Actualizar ADR 0001 a aceptado con implementación y pruebas
- Agregar entrada de IA del corte 1
- Configurar pipeline y aportar runs
- Conciliar C4 Nivel 2 con la implementación
- Aportar medición de línea base y resultado contra umbral

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- Etiqueta corte-1 sobre un commit anterior al cierre
- PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad
- Impacto de la restricción localizado en requisitos, C4 y código
- Línea base medida y verificable antes del cambio
- ADR del reto con alternativas, fuerzas, decisión y consecuencias
- Cambio implementado y ejecutable de extremo a extremo
- Prueba que cubre el cambio, en verde en el pipeline
- Resultado contrastado con el umbral del escenario y reproducible
- Sustentación del reto

## Hallazgos para la planilla

- No hay evidencia de la etiqueta corte-1 en la evidencia proporcionada.
- Falta la restricción asignada al equipo para juzgar el diagnóstico.
- docs/aspectos.md no tiene las columnas Requisito, C4 y Evidencia exigidas.
- El ADR 0001 está en estado propuesto con implementación y pruebas pendientes.
- No hay runs_ci que confirmen pruebas en pipeline.
- El C4 Nivel 2 declara contenedores que no corresponden con el código monolítico.
- docs/ia.md no registra usos de IA del corte 1 (semana 5).
- No hay medición de línea base ni resultado contrastado con umbral en el repositorio.
