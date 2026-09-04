# semana-05-corte1 · Drift

> Revisión manual preliminar completa realizada el 2026-09-03, antes del cierre. El equipo puede modificar el repositorio y la evaluacion definitiva debe repetirse despues de `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `d7a61cc` (2026-08-31T20:45:45-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | revisión manual local, solo lectura; no se ejecutó código |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Consulta manual `git tag --list`: no existe `corte-1`; se revisó el HEAD anterior al cierre | No cumple | Falta la etiqueta exigida por la ficha. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay PDF en el repositorio | No verificado | El PDF se adjunta en Moodle; no es accesible desde el repositorio. |
| Impacto de la restricción localizado en requisitos, C4 y código | No hay diagnóstico de restricción en docs/adr/ ni docs/arc42/ | No verificado | No se proporcionó la restricción asignada al equipo; sin ella no se puede juzgar. |
| Línea base medida y verificable antes del cambio | docs/escenarios.md define medidas (≤3 s p95) pero sin medición real | No cumple | No hay cifra con herramienta y procedimiento de medición. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/ solo contiene 0001 y 0002, ambos de arquitectura base | No cumple | No hay ADR que responda a la restricción del reto. |
| Cambio implementado y ejecutable de extremo a extremo | commits_nuevos_desde_cierre_anterior: sin commits nuevos | No cumple | No hay commit que implemente un ADR del reto. |
| Límites declarados conservados tras el cambio | docs/c4/contenedores.md describe Web/API, Aplicación, Dominio, Adaptadores, Persistencia | No cumple | Sin cambio del reto, no hay límites que contrastar. |
| Prueba que cubre el cambio, en verde en el pipeline | backend/tests/test_health.py y .github/workflows/ci.yml existen | No cumple | No hay runs_ci con URL; no se verifica ejecución en verde. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay herramienta, carga ni procedimiento de medición en el repositorio | No cumple | Falta resultado contrastado con umbral. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md tiene columnas ID, Aspecto, Fuente, Estímulo, Artefacto, Entorno, Respuesta, Medida | No cumple | No tiene columnas Requisito, C4, ADR, Código, Pruebas, Evidencia; enlaces solo a escenarios.md. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md con 5 registros (fecha, herramienta, prompt, uso) | No cumple | No hay columna de aceptado/corregido/rechazado con motivo técnico. |
| Sustentación del reto | No verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible=true, repo=AS_202620_Drift; autores consolidados: JerryDBM/Sherry, JoshuaR01/JoshXX, lmpdiaz12, maufern4ndez | Cumple | 4 personas consolidadas, coincide con los integrantes declarados. |
| Estructura mínima | arbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Desviaciones menores: nombres de archivos arc42 con mayúsculas y 'vista_bloques' vs 'bloques_construccion'. |
| Versionado y estado calificado | Consulta Git manual confirma que no existe la etiqueta `corte-1`; se identifica HEAD como estado preliminar | No cumple | Falta el estado versionado exigido por la ficha. |
| Convenciones de ADR | docs/adr/0001-arquitectura-base.md y 0002-arquitectura-base.md con título 'Selección de Arquitectura Base' | No cumple | El título enuncia el tema, no la decisión; ADR-0001 no está marcado como reemplazado. |
| Tabla de aspectos y trazabilidad | docs/aspectos.md sin columnas Requisito, C4, ADR, Código, Pruebas, Evidencia | No cumple | No cumple el formato de 8 columnas del contrato. |
| Registro de uso de IA | docs/ia.md con registros de uso pero sin sección de rechazado con motivo | No cumple | Falta la columna de lo rechazado y por qué. |
| README y reproducibilidad | README.md presente pero truncado en la evidencia | No verificado | No se ven comandos de arranque en el fragmento disponible. |
| Pipeline, secretos y autoría | .github/workflows/ci.yml existe; secretos sin coincidencias; 4 autores | No verificado | Sin runs_ci no se verifica el pipeline; secretos y autoría cumplen. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `d7a61cc222416b9101abd731bc909a2427c37c29 2026-08-31T20:45:45-05:00 ci: corregir ejecución de pruebas backend`
- **Veredicto**: con pendientes
- Resumen: El repositorio tiene documentación base y código inicial, pero la respuesta al reto del corte 1 (diagnóstico, ADR, cambio, medición, trazabilidad) no está presente en el commit calificado.

Pendientes que siguen abiertos:
- Crear la etiqueta `corte-1` sobre el estado que se someterá antes del cierre.
- Registrar ADR del reto con alternativas y decisión
- Medir línea base con procedimiento
- Completar aspectos.md con 8 columnas
- Añadir rechazos con motivo en ia.md
- Evidenciar run de CI en verde

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia evaluable del reto | 0,00 | No se identifica una respuesta a la restricción nueva; la restricción asignada tampoco está disponible. |
| Alternativas y decisión | Sin evidencia del reto | 0,00 | Los ADR visibles corresponden a decisiones de la línea base o son anteriores al inicio de S5. |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | No hay cambio trazable a una restricción nueva. |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | Las pruebas o el CI de la línea base no demuestran una medición antes/después del reto. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico verificable** |  | **0,00 / 4,00** | No constituye el total sobre 5,00. |

## Recuento

0 de 12 criterios Cumple.

## No verificado / pendientes

- Coincidencia del diagnóstico con la restricción asignada, porque la asignación no está disponible en el kit.
- PDF adjunto en Moodle.
- Sustentación del reto.

## Hallazgos para la planilla

- La consulta Git manual confirma que no existe la etiqueta `corte-1`.
- No hay ADR del reto; solo ADR-0001/0002 de la línea base.
- No hay diagnóstico de la restricción asignada ni línea base medida.
- docs/aspectos.md no tiene las 8 columnas de trazabilidad del contrato.
- docs/ia.md no registra salidas rechazadas con motivo técnico.
- No hay runs de CI verificables para la prueba del cambio.
- README truncado en la evidencia; no se confirma comando de arranque único.
- Los títulos de los ADR enuncian el tema, no la decisión.

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada y dónde se localiza su impacto en requisitos, C4 y código?
2. ¿Cuál fue la cifra de línea base, con qué herramienta y procedimiento se obtuvo, y cuál fue el resultado posterior?
3. ¿Qué ADR y commit implementan el reto, y qué prueba del pipeline demuestra el cambio?
