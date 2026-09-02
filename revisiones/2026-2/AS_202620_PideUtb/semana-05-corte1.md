# semana-05-corte1 · PideUtb

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `1636f20` (2026-08-30T22:17:18-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | hash_calificado 1636f20 2026-08-30T22:17:18-05:00 anterior al cierre; no se confirma existencia de la etiqueta en la evidencia | No verificado | Falta ejecutar git tag --list y git log -1 corte-1 |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | adjunto en Moodle, no accesible desde el repositorio | No verificado | Revisar entrega en Moodle |
| Impacto de la restricción localizado en requisitos, C4 y código | no se proporcionó la restricción asignada al equipo; documentos visibles no mencionan restricción nueva | No verificado | Sin la restricción no se puede juzgar el diagnóstico |
| Línea base medida y verificable antes del cambio | no hay cifra con herramienta y procedimiento en los documentos visibles | No verificado | Falta evidencia de medición inicial |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | docs/adr/ solo contiene 0001-estilo-arquitectonico.md (23/08/2026), anterior al reto; no hay ADR nuevo del corte | No cumple | El ADR existente es de la semana 3/4, no del reto |
| Cambio implementado y ejecutable de extremo a extremo | README.md documenta arranque con un comando y corte vertical, pero no se puede asociar al reto sin conocer la restricción | No verificado | Falta confirmar que el cambio corresponde a la restricción |
| Límites declarados conservados tras el cambio | no hay docs/c4/ en el árbol; no se pueden verificar límites | No cumple | Falta documentación C4 |
| Prueba que cubre el cambio, en verde en el pipeline | existen backend/tests/test_pedidos.py y test_health.py, pero no hay runs_ci en la evidencia | No verificado | Falta URL de run anterior a la etiqueta |
| Resultado contrastado con el umbral del escenario y reproducible | no hay medición con herramienta, carga y procedimiento | No verificado | Falta evidencia de medición |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md no tiene las 8 columnas del contrato; solo Usabilidad llega a Prueba, sin columna Evidencia | No cumple | Fila con huecos no defendible |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md tiene entradas de segunda y tercera entrega; el log muestra commit 2026-08-30 pero el contenido visible no muestra entrada del corte | No verificado | Revisar contenido completo de docs/ia.md en HEAD |
| Sustentación del reto | sesión de sustentación, no verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_PideUtb en ISCOUTB, visible; autores consolidados: daniarriet, Santiago Cuesta/Santiago-C0, ruddy2000utb-droid (3 personas) | Cumple | Coincide con los 3 integrantes declarados |
| Estructura mínima | árbol visible no incluye docs/arc42/ ni docs/c4/; README.md y docs/adr/ sí existen | No cumple | Faltan secciones arc42 y diagramas C4 |
| Estado del repositorio que se califica (versionado) | hash 1636f20 anterior al cierre, pero no se confirma etiqueta corte-1 | No verificado | Falta git tag --list |
| Convenciones de ADR | 0001-estilo-arquitectonico.md cumple nombre y tiene contexto/alternativas/decisión/consecuencias, pero sin sección de trazabilidad (requisito, C4, commit, pruebas) | No cumple | ADR aceptado no debe editarse; falta trazabilidad |
| Tabla de aspectos | docs/aspectos.md con 6 columnas en vez de 8 (ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia); solo Usabilidad completa hasta Prueba | No cumple | Celdas con '—' y pendientes |
| Registro de uso de IA | docs/ia.md existe con 4 commits; contenido visible cubre segunda y tercera entrega, sin entrada clara del corte 1 | No verificado | Falta ver entrada de este corte con aceptado/corregido/rechazado y motivo |
| README y reproducibilidad | README.md documenta arranque con un solo comando (python3 -m venv ... uvicorn) y cómo probar (pytest) | Cumple | Comando reproducible |
| Pipeline y análisis estático | no hay .github/workflows ni runs_ci en la evidencia | No verificado | Falta evidencia de ejecución de CI |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `1636f20d14f254dffd9aa9c1eb43e138fba73043 2026-08-30T22:17:18-05:00 Revise diagram legend for clarity and detail`
- **Veredicto**: con pendientes
- Resumen: Proyecto con corte vertical ejecutable y README reproducible, pero la entrega del reto no está completa: falta ADR del reto, C4, trazabilidad y evidencia de CI/medición.

Pendientes que siguen abiertos:
- Confirmar etiqueta corte-1
- Documentar restricción y diagnóstico
- Crear ADR del reto
- Completar docs/arc42/ y docs/c4/
- Reestructurar docs/aspectos.md a 8 columnas
- Evidencia de CI y medición
- Entrada de IA del corte en docs/ia.md

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- Etiqueta corte-1 (falta git tag --list).
- PDF de dos páginas (adjunto Moodle).
- Restricción asignada al equipo.
- Línea base medida antes del cambio.
- Pruebas en pipeline (runs_ci).
- Medición contra umbral reproducible.
- Salida de IA del corte 1 en docs/ia.md.
- Sustentación del reto (sesión).

## Hallazgos para la planilla

- No se confirma la existencia de la etiqueta corte-1 en la evidencia.
- No se proporcionó la restricción asignada al equipo, imprescindible para evaluar el reto.
- No hay ADR nuevo del reto; el único ADR es de la semana 3/4.
- docs/aspectos.md no cumple la estructura de 8 columnas del contrato.
- Faltan docs/arc42/ y docs/c4/ en el árbol del repositorio.
- No hay evidencia de runs de CI en la evidencia proporcionada.
- El repositorio versiona .venv-1 (entorno virtual), mala práctica.
- Los secretos detectados son falsos positivos de librerías en .venv-1.
