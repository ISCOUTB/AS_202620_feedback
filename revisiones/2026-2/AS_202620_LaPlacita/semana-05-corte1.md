# semana-05-corte1 · LaPlacita

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `745e799` (2026-08-30T21:52:41-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Sin etiqueta `corte-1` en la evidencia; estado calificado es el commit 745e799 (2026-08-30T21:52:41-05:00). | No cumple | Falta la salida de `git tag --list`; se revisa el último commit anterior al cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No accesible desde el repositorio; se entrega como adjunto en Moodle. | No verificado | Requiere el adjunto de la entrega para verificar contenido. |
| Impacto de la restricción localizado en requisitos, C4 y código | No se declara la restricción asignada al equipo en la evidencia. | No verificado | Sin la restricción no se puede juzgar el diagnóstico. |
| Línea base medida y verificable antes del cambio | No hay cifra con herramienta y procedimiento en el repositorio. | No verificado | Se requiere la restricción y la medición inicial. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | ADR existentes (0001-0003) son de semanas previas; no se identifica ADR del reto. | No verificado | Falta la restricción para localizar el ADR correspondiente. |
| Cambio implementado y ejecutable de extremo a extremo | No se identifica commit que implemente el ADR del reto. | No verificado | README documenta `npm run dev`, pero sin cambio identificado no se verifica. |
| Límites declarados conservados tras el cambio | Sin cambio identificado, no hay correspondencia C4-código a verificar. | No verificado | Requiere el commit del cambio. |
| Prueba que cubre el cambio, en verde en el pipeline | Runs CI en verde (p.ej. 33352046552 success), pero sin prueba específica del cambio. | No verificado | Falta identificar la prueba que cubre el reto. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay medición con herramienta, carga y procedimiento. | No verificado | Se requiere la medición del escenario afectado. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md tiene 'Pendiente' en Pruebas (A-02 a A-06) y Evidencia (todas las filas). | No cumple | La cadena se rompe en Pruebas/Evidencia. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md solo dice 'Revisado y adaptado por el equipo'; sin motivo técnico de rechazo. | No cumple | No hay entrada de este corte con justificación técnica. |
| Sustentación del reto | Se resuelve en sesión de sustentación. | No verificado | No verificable desde el repositorio. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_LaPlacita en ISCOUTB, público; 4 integrantes en historial (consolidando matbuendia e isaza927). | Cumple | Ninguna. |
| Estructura mínima | Existen docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md. | Cumple | Ninguna. |
| Versionado | No se encontró la etiqueta `corte-1`; se revisa el commit 745e799. | No cumple | Falta la etiqueta del corte. |
| Convenciones de ADR | ADR-0001 y ADR-0003 dejan 'Pendiente' en implementación; trazabilidad incompleta. | No cumple | La convención exige commit o PR que implementa. |
| Tabla de aspectos | Celdas 'Pendiente' en Pruebas y Evidencia en docs/aspectos.md. | No cumple | Filas no defendibles de punta a punta. |
| Registro de uso de IA | docs/ia.md sin motivos técnicos de rechazo; solo 'Revisado y adaptado'. | No cumple | Falta la columna de lo rechazado con justificación. |
| README | README.md documenta `npm install`, `npm run dev` y `npm test` con Node 22. | Cumple | Ninguna. |
| Pipeline y análisis estático | CI ejecuta `npm test` en verde (run 33352046552), pero no hay SonarCloud configurado. | No cumple | ADR-0003 lo declara pendiente; falta sonar-project.properties. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `745e7998f189857a5fe3fee644dcb9f438161c0d 2026-08-30T21:52:41-05:00 Cambios de redacción dentro de la informació en el README, escritura del adr-0003 y los subtitulos del 6 - 9 del Arc42`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene documentación y CI en verde, pero el reto del corte 1 no es verificable: falta la etiqueta, la restricción no se declara y la trazabilidad tiene huecos.

Pendientes que siguen abiertos:
- Etiqueta corte-1
- Declarar restricción asignada
- Completar trazabilidad en aspectos.md
- Registrar motivos técnicos en ia.md
- Configurar SonarCloud
- Aportar mediciones reproducibles

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- PDF de dos páginas (adjunto Moodle)
- Impacto de la restricción (falta restricción asignada)
- Línea base medida
- ADR del reto
- Cambio implementado
- Límites conservados
- Prueba del cambio
- Medición contra umbral
- Sustentación

## Hallazgos para la planilla

- No se encontró la etiqueta `corte-1` en la evidencia.
- Falta la restricción asignada al equipo para evaluar el reto.
- La tabla de aspectos tiene celdas 'Pendiente' en Pruebas y Evidencia.
- docs/ia.md no registra salidas rechazadas con motivo técnico.
- ADR-0001 y ADR-0003 dejan la implementación como 'Pendiente'.
- El pipeline no incluye SonarCloud pese a lo declarado en ADR-0003.
- No hay mediciones reproducibles con herramienta, carga y procedimiento.
