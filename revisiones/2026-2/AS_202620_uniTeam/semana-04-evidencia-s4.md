# semana-04-evidencia-s4 · uniTeam

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `ca44917` (2026-08-23T13:38:40-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-uniteam.md: encabezado 'Estado' indica solo secciones 1,2,3,9,10,11 redactadas | No cumple | Faltan secciones 4,5,6 redactadas. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se pudo acceder al contenido de la sección 9 en la evidencia proporcionada | No verificado | Haría falta el texto de la sección 9 para comprobar enlaces a ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se pudo acceder al contenido de la sección 10 | No verificado | Haría falta el texto de la sección 10 y su correspondencia con escenarios. |
| Glosario iniciado con términos del dominio | Encabezado de arc42-uniteam.md no menciona sección 12; no hay archivo de glosario | No cumple | Sección 12 no redactada. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Solo existe docs/c4/nivel1-contexto.md; no hay archivo de nivel 2 | No cumple | Falta C4 nivel 2. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No hay C4 nivel 2 para contrastar | No cumple | Sin nivel 2 no se puede verificar correspondencia. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README indica app/domain, app/application, app/infrastructure vacíos; solo app/main.py y app/api/__init__.py | No cumple | No hay lógica ni persistencia implementadas. |
| Arranque documentado con un solo comando | README solo documenta pasos para clonar, instalar y ejecutar pytest; no hay comando de arranque de la aplicación | No cumple | Falta comando único para iniciar el sistema. |
| Prueba automatizada del recorrido completo, en verde | Solo existe test/prueba_test.py (probablemente health check); no hay evidencia de CI | No cumple | No hay prueba del recorrido completo ni run en verde. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md tiene tabla con columnas ID, Aspecto, RF, Atributo, Escenario, Por qué; faltan C4, ADR, Código, Pruebas, Evidencia | No cumple | La tabla no llega a la columna Pruebas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Autores en git: super-gremlin, Ian Novoa, Julio Cesar Emiliani (3) vs 4 integrantes declarados | No cumple | Falta al menos un integrante en el historial. |
| Estructura mínima | Árbol incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura conforme. |
| Estado calificado | No hay etiqueta corte-1; se usó commit ca44917 anterior al cierre | No cumple | Etiqueta ausente. |
| Convenciones de ADR | docs/adr/ADR-003-seleccion-estilo-arquitectonico (1).md no sigue kebab-case | No cumple | Nombre con espacios y paréntesis. |
| Tabla de aspectos | docs/aspectos.md no tiene las 8 columnas requeridas | No cumple | Faltan C4, ADR, Código, Pruebas, Evidencia. |
| Registro de IA | docs/ia.md existe con commits, pero contenido no disponible | No verificado | Haría falta revisar el contenido para verificar rechazos. |
| README | README no documenta un comando único de arranque de la aplicación | No cumple | Solo muestra cómo ejecutar pruebas. |
| Pipeline y análisis estático | No hay .github/workflows/ ni evidencia de runs de CI | No cumple | Sin pipeline configurado. |

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 sección 9
- arc42 sección 10
- Registro de IA

## Hallazgos para la planilla

- Faltan secciones arc42 4-6 y glosario
- No hay C4 nivel 2
- Corte vertical no implementado
- Tabla de aspectos incompleta
- ADR-003 con nombre incorrecto
- Falta integrante en historial
- Sin pipeline CI
- README sin comando de arranque
