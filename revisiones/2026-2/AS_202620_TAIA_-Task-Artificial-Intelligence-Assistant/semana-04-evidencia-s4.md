# semana-04-evidencia-s4 · TAIA

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `0f7f4bd` (2026-08-27T10:14:25-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md solo muestra secciones 1 y 2 en el contenido disponible | No verificado | No se pudo comprobar la presencia y redacción de las secciones 3 a 6; haría falta listar los encabezados del archivo completo. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se observa la sección 9 en el contenido parcial de docs/arc42/arc42-template-EN.md | No verificado | No se pudo verificar el enlace a docs/adr/0001.md; falta evidencia de la sección 9. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se observa la sección 10 en el contenido parcial | No verificado | No se pudo contrastar con docs/calidad/escenarios_calidad.md; falta evidencia. |
| Glosario iniciado con términos del dominio | No se observa la sección 12 en el contenido parcial | No verificado | No se pudo comprobar la existencia de términos propios del sistema. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/C4-C1.md y docs/c4/C4-C2.md contienen diagramas Mermaid con actores y contenedores coherentes | Cumple | Los actores externos (estudiante, Telegram, Gemini) reaparecen en ambos niveles; las flechas están etiquetadas. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | El contenedor 'App Móvil' no tiene código en el repositorio; 'API TAIA' corresponde a backend/ | No cumple | Falta el directorio de la app Flutter; solo backend/ está implementado. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | backend/app/main.py existe, pero los módulos solo contienen .gitkeep sin lógica ni persistencia | No cumple | No hay recorrido completo; solo endpoint de health. |
| Arranque documentado con un solo comando | README.md declara requisitos y comando único: .\run.bat | Cumple | El comando está documentado y es ejecutable desde la raíz. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_entrega3.py existe, pero no hay evidencia de que cubra el corte vertical ni de CI | No cumple | No se encontró pipeline (.github/workflows) ni run en verde. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 tiene 'Pendiente' en C4, Código, Pruebas y Evidencia; enlace ADR roto | No cumple | La fila no está completa; el enlace apunta a adr/0001-estilo-arquitectonico.md inexistente. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio público AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant en ISCOUTB; 4 autores en historial | Cumple | Los 4 integrantes declarados aparecen en git shortlog. |
| Estructura mínima | Árbol contiene docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Todas las rutas requeridas están presentes. |
| Estado calificado (versionado) | Hash 0f7f4bd con fecha 2026-08-27T10:14:25-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Commit vigente correcto para evidencia semanal. |
| Convenciones de ADR | docs/adr/0001.md no sigue el patrón NNNN-titulo-en-kebab-case.md y carece de trazabilidad | No cumple | Falta título en el nombre y secciones de contexto/trazabilidad explícitas. |
| Tabla de aspectos | docs/aspectos.md fila A-01 con celdas 'Pendiente' y enlace ADR roto | No cumple | La cadena de trazabilidad no es navegable. |
| Registro de uso de IA | docs/ia.md con tres entradas, cada una incluye herramienta, aceptado y rechazado con motivo | Cumple | Cumple con el requisito de registrar rechazos. |
| README | README.md incluye descripción, requisitos, comando de arranque único y pruebas | Cumple | Documento claro y completo. |
| Pipeline y análisis estático | No existe .github/workflows/ en el árbol ni se proporcionan runs de CI | No cumple | Sin evidencia de ejecución automatizada. |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 3 a 6: falta listar encabezados del archivo completo.
- arc42 sección 9: falta evidencia de su contenido y enlace a ADR.
- arc42 sección 10: falta evidencia de coherencia con escenarios.
- arc42 sección 12 (glosario): falta evidencia de términos del dominio.
- Ejecución de pipeline: no se proporcionaron runs de CI.

## Hallazgos para la planilla

- ADR 0001 no sigue convención de nombre y carece de trazabilidad.
- Fila A-01 de aspectos.md incompleta y con enlace roto.
- No hay corte vertical implementado; solo endpoint de health.
- No existe pipeline de CI ni análisis estático.
- Contenedor App Móvil del C4 no tiene código en el repositorio.
- Secciones 3-6, 9, 10 y 12 de arc42 no verificables con la evidencia disponible.
