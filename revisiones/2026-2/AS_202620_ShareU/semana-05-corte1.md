# semana-05-corte1 · ShareU

> Revisión manual preliminar completa realizada el 2026-09-03, antes del cierre. El equipo puede modificar el repositorio y la evaluacion definitiva debe repetirse despues de `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `7c027f0` (2026-08-31T15:08:39-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | revisión manual local, solo lectura; no se ejecutó código |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta corte-1 sobre un commit anterior al cierre | Consulta manual `git tag --list`: no existe `corte-1`; se revisó el HEAD anterior al cierre | No cumple | Falta la etiqueta exigida por la ficha. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | adjunto de Moodle no incluido en la evidencia del repositorio | No verificado | depende de la entrega en Moodle |
| Impacto de la restricción localizado en requisitos, C4 y código | no se conoce la restricción asignada al equipo; no hay apartado de diagnóstico en el repositorio | No verificado | sin la restricción no se puede juzgar si el diagnóstico localiza lo debido |
| Línea base medida y verificable antes del cambio | el árbol no contiene ningún documento de diagnóstico o medición; solo docs/adr/0001-estilo-arquitectonico.md | No cumple | no hay cifra con herramienta y procedimiento |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/ solo contiene 0001-estilo-arquitectonico.md | No cumple | no hay ADR del reto ligado al escenario de calidad |
| Cambio implementado y ejecutable de extremo a extremo | commit 7c027f0 es 'Create README.md'; no hay commits que implementen un ADR del reto | No cumple | el arranque documentado es uvicorn app.main:app --reload, pero no se ejecutó (runs_ci vacío) |
| Límites declarados conservados tras el cambio | existen docs/c4/nivel1.mmd, nivel-2.md, nivel2.mmd y NIVEL2.png; no hay cambio del reto que comparar | No cumple | haría falta el commit del cambio y la correspondencia C4-código |
| Prueba que cubre el cambio, en verde en el pipeline | runs_ci vacío; existen tests/test_busqueda.py y tests/test_esqueleto.py | No cumple | haría falta URL de run anterior a la etiqueta; comando: curl -s https://api.github.com/repos/ISCOUTB/AS_202620_ShareU/actions/runs?per_page=30 |
| Resultado contrastado con el umbral del escenario y reproducible | no hay medición con herramienta, carga y procedimiento en el repositorio | No cumple | sin umbral ni reproducción de la medición |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos/aspectos.md existe pero no se incluye su contenido | No cumple | haría falta recorrer la fila celda a celda |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md existe; ia_log sin commits sobre el archivo; contenido no incluido | No cumple | haría falta ver una entrada aceptada/corregida/rechazada con motivo técnico |
| Sustentación del reto | sesión de sustentación, no verificable desde el repositorio | No verificado | lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible true, repo AS_202620_ShareU en ISCOUTB | Cumple | solo 2 autores visibles (Nicolas-HH, steven) para 4 integrantes declarados |
| Estructura mínima | árbol incluye README.md, docs/arc42/arc42.md, docs/adr/0001-*.md, docs/c4/, docs/ia.md y docs/aspectos/aspectos.md | Cumple | desviación: docs/aspectos.md está en docs/aspectos/aspectos.md |
| Versionado | Consulta Git manual confirma que no existe la etiqueta `corte-1`; se identifica HEAD como estado preliminar | No cumple | Falta el estado versionado exigido por la ficha. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md cumple el patrón de nombre; contenido no verificado | No verificado | no se pudo comprobar contexto, opciones, decisión, consecuencias y trazabilidad |
| Tabla de aspectos | docs/aspectos/aspectos.md existe; contenido no incluido | No verificado | haría falta verificar las 8 columnas y navegabilidad |
| Registro de IA | docs/ia.md existe; ia_log sin commits; contenido no incluido | No verificado | haría falta ver una entrada con aceptado/rechazado y motivo |
| README | README.md documenta qué es, arranque con uvicorn y pruebas con pytest | Cumple | requiere pasos de instalación documentados |
| Pipeline y análisis estático | .github/workflows/tests.yml existe; runs_ci vacío | No verificado | haría falta URL de run; comando: curl -s https://api.github.com/repos/ISCOUTB/AS_202620_ShareU/actions/runs?per_page=30 |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `7c027f0c6b3573313b42d47c710414d97d2f5bd4 2026-08-31T15:08:39-05:00 Create README.md`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene una línea base de monolito modular con README y estructura documental, pero el reto del primer corte no fue abordado: no hay ADR del reto, diagnóstico, implementación, pruebas ni medición. HEAD coincide con el commit calificado 7c027f0.

Pendientes que siguen abiertos:
- Responder al reto de restricción asignada
- Crear ADR del reto con alternativas y decisión
- Implementar el cambio y probarlo
- Medir contra umbral
- Subir PDF de dos páginas
- Crear etiqueta corte-1
- Evidenciar pipeline en verde
- Completar docs/ia.md y docs/aspectos.md

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

- No se confirmó la etiqueta corte-1 en el repositorio.
- No hay ADR del reto; solo existe 0001-estilo-arquitectonico.md.
- No hay diagnóstico, línea base ni medición del reto en el repositorio.
- runs_ci vacío: sin evidencia de pipeline en verde.
- docs/aspectos.md está en ruta desviada docs/aspectos/aspectos.md.
- Solo 2 autores en el historial para 4 integrantes declarados.
- docs/ia.md existe pero sin contenido verificado ni commits.
- El commit calificado es 'Create README.md', sin implementación del reto.

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada y dónde se localiza su impacto en requisitos, C4 y código?
2. ¿Cuál fue la cifra de línea base, con qué herramienta y procedimiento se obtuvo, y cuál fue el resultado posterior?
3. ¿Qué ADR y commit implementan el reto, y qué prueba del pipeline demuestra el cambio?
