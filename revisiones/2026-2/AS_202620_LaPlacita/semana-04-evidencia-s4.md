# semana-04-evidencia-s4 · LaPlacita

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `d8cc718` (2026-08-28T14:43:46-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md muestra secciones 1-4 redactadas; contenido truncado antes de secciones 5 y 6 | No verificado | No se puede confirmar la redacción de las secciones 5 y 6 porque el extracto termina en 4.1 |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se muestra la sección 9 en el contenido proporcionado | No verificado | Falta evidencia de la sección 9 y sus enlaces a ADR |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/aspectos.md enlaza a anclas de escenarios en arc42 (ej. #esc-01--picos-de-demanda-entre-clases), pero no se ve el contenido de la sección 10 | No verificado | No se puede evaluar coherencia sin el texto completo de la sección 10 |
| Glosario iniciado con términos del dominio | No se muestra la sección 12 en el contenido de arc42 | No verificado | No hay evidencia de glosario con términos propios |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/contexto.md contiene solo diagrama de contexto (nivel 1); no existe archivo de nivel 2 | No cumple | Falta el diagrama de contenedores (nivel 2) |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No hay C4 nivel 2, por lo que no se puede contrastar con src/modules/* | No cumple | Sin nivel 2 no hay correspondencia que evaluar |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Existen src/index.js y src/modules/*, pero no se proporciona el contenido de esos archivos | No verificado | No se puede seguir el recorrido sin el código fuente |
| Arranque documentado con un solo comando | README.md no muestra sección de arranque en el extracto; package.json tiene scripts start y test | No verificado | No se confirma que el README declare requisitos previos y un comando único |
| Prueba automatizada del recorrido completo, en verde | Solo existe tests/health.test.js; docs/aspectos.md indica 'Pendiente (solo existe prueba genérica health.test.js)' para todos los aspectos | No cumple | No hay prueba que ejercite el corte vertical de punta a punta |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md tiene celdas 'Pendiente' en C4, Pruebas y Evidencia para todas las filas | No cumple | Ninguna fila está completa hasta Pruebas |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_LaPlacita visible, público, en ISCOUTB; autores consolidados: Jorge, Miguel, Samuel, Mateo (4 personas) | Cumple | Coincide con integrantes declarados |
| Estructura mínima | Existen docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura conforme al contrato |
| Estado del repositorio calificado | Commit d8cc718 con fecha 2026-08-28T14:43:46-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Commit vigente correcto |
| Convenciones de ADR | docs/adr/0001-adopcion-monolito-modular.md y 0002-ratificacion-monolito-modular.md siguen patrón; ADR-0002 ratifica sin editar ADR-0001 | Cumple | Nombres y numeración correctos |
| Tabla de aspectos | docs/aspectos.md tiene columnas requeridas pero celdas 'Pendiente' en C4, Pruebas y Evidencia | No cumple | Hay huecos no navegables; no cumple cadena completa |
| Registro de uso de IA | docs/ia.md incluye entradas con herramienta, propósito, prompt, resultado, validación y rechazos con motivo | Cumple | Registro completo y con rechazos justificados |
| README | README.md no muestra sección de arranque en el extracto proporcionado | No verificado | No se puede confirmar comando único documentado |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta npm test, pero no incluye SonarCloud | No cumple | Falta análisis estático requerido |

## Recuento y nota sugerida

0 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.0 = 1 + 4 × (0/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 5 y 6: contenido truncado
- arc42 sección 9: no visible
- arc42 sección 10: no se muestra texto completo
- arc42 sección 12 (glosario): no visible
- Corte vertical: falta contenido de src/
- Arranque documentado: falta sección en README

## Hallazgos para la planilla

- Falta C4 nivel 2 (solo hay contexto)
- No existe prueba del recorrido completo, solo health.test.js
- Tabla de aspectos con celdas Pendiente en todas las filas
- Pipeline sin SonarCloud
- arc42 incompleto o no verificable en secciones 5,6,9,12
- README sin sección de arranque visible
