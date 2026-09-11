# semana-05-corte1 · Verifacts

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `67f8cea` en `origin/master` (2026-09-09T16:30:01-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master en 67f8cea (2026-09-09T16:30:01-05:00), anterior al cierre 2026-09-10T17:00:00Z | Cumple | Rama principal declarada por el remoto: origin/master. |
| correcciones.md existe en la raíz del estado calificado | git ls-tree 67f8cea incluye correcciones.md en la raíz | Cumple | Archivo presente en el hash calificado. |
| Correcciones trazables y contrastadas | correcciones.md listado en el árbol pero contenido no incluido en la evidencia del repositorio | No verificado | No se pudo contrastar cada hallazgo S1-S4 con el contenido del archivo; se requiere el texto de correcciones.md en 67f8cea. |
| S1 al día: equipo, problema y repositorio | README.md y Equipo.md declaran 2 integrantes (Pedro Jose Castro Blanquicett, Cristian David Cardeno Gulloso); el equipo declarado en la ficha incluye a Julian Samuel Cabeza Pena | No cumple | Falta Julian Samuel Cabeza Pena en README.md y Equipo.md; el historial solo muestra a PedroC1213 y Cristian Cardeño. |
| S2 al día: escenarios de calidad y restricciones | docs/escenarios-de-calidad.md con Q-01 a Q-05 completos; docs/arc42/02-restricciones.md con R-ORG, R-TEC, R-ALC y R-DAT | Cumple | Escenarios y restricciones presentes y coherentes con el ADR. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-estilo-arquitectonico.md (Aceptado, 2026-08-24); docs/arc42/04-estrategia-de-solucion.md; docs/matriz-estilos.md | Cumple | Decisión de monolito modular documentada con alternativas y consecuencias. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/ con secciones 01-11; docs/c4/ con niveles 1-3; tests/test_analysis.py, tests/test_health.py, tests/test_analysis_history.py, tests/test_url_ingestion.py | Cumple | Documentación arc42 y C4 presentes; corte vertical cubierto por pruebas. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta arranque con python run.py y npm run dev; app/ implementa API, Content, Analysis, Scoring y Persistencia; tests cubren POST /analysis, GET /analysis y GET /health | Cumple | Coherente con C4 Nivel 2 y ADR-0001. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/tests.yml presente; docs/aspectos.md cita run 33476637583/job 99757163051 pero no se aportó la URL ni conclusión del run en la evidencia | No verificado | No hay runs_ci con nombre, conclusión y URL verificables para 67f8cea. |
| Trazabilidad consolidada navegable | docs/aspectos.md con columnas ID, Aspecto, Escenario, C4, ADR, Código, Medida, Evidencia; enlaces a escenarios, C4, ADR y pruebas | Cumple | La tabla de aspectos es navegable; A-02 queda pendiente de prueba. |
| PDF u otro adjunto exigido por el aula | VeriFacts-resumen-entrega-final c1.pdf presente en la raíz del estado calificado | Cumple | El PDF está versionado en el repositorio; la entrega en Moodle no es verificable desde aquí. |
| Sustentación del corte | No hay evidencia de sesión de sustentación en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_Verifacts visible; nombre y organización correctos | Cumple | Visibilidad pública declarada en la evidencia. |
| Estructura mínima | README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes en el árbol de 67f8cea | Cumple | Estructura mínima cumplida. |
| Estado del repositorio que se califica | Hash 67f8cea en origin/master anterior al cierre; sin commits posteriores al cierre en la rama | Cumple | commits_tardios_post_cierre vacío. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md con nombre NNNN-titulo-en-kebab-case; ADR-0001 aceptado con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Un solo ADR; no se observan reescrituras posteriores. |
| Tabla de aspectos | docs/aspectos.md con 8 columnas y filas A-00 a A-04 enlazadas a escenarios, C4, ADR, código y pruebas | Cumple | A-02 declarada pendiente; el resto tiene evidencia citable. |
| Registro de uso de IA | docs/ia.md con bitácora por interacción, herramienta, propósito, resultado, validación y rechazos; 4 commits en su historial | Cumple | Incluye rechazo de LLM como clasificador con motivo técnico. |
| README | README.md describe el sistema, integrantes, arquitectura, arranque con python run.py y npm run dev, y pruebas con pytest | Cumple | Arranque y pruebas documentados. |
| Pipeline y análisis estático | .github/workflows/tests.yml presente y sonar-project.properties presente; sin runs_ci con URL y conclusión verificables | No verificado | Se requiere URL de run en verde asociado al hash o anterior al corte. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `67f8cea03e6a7b827aced6b60d3af8cf4307b237 2026-09-09T16:30:01-05:00 feat: integrate backend URL analysis contract and align frontend`
- **Veredicto**: con pendientes
- Resumen: A HEAD (67f8cea, sin commits posteriores al cierre) el proyecto cumple la mayoría de criterios de documentación y corte vertical, pero persisten hallazgos de semanas anteriores: equipo incompleto, CI sin run verificable, correcciones.md sin contrastar y documentación desactualizada.

Pendientes que siguen abiertos:
- Incluir a Julian Samuel Cabeza Pena en README.md y Equipo.md y evidenciar su contribución en el historial.
- Contrastar correcciones.md con los hallazgos S1-S4.
- Aportar run de CI en verde para el hash calificado.
- Cerrar A-02 con prueba de modificación de regla.
- Actualizar glosario, vista de bloques, C4 de componentes y enlaces rotos.

## Recuento y nota sugerida

8 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.7 = 1 + 4 × (8/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correcciones trazables y contrastadas: falta el contenido de correcciones.md en 67f8cea.
- Pipeline y pruebas respaldan el estado calificado: falta URL y conclusión de run de CI.
- Sustentación del corte: depende de la sesión del docente.

## Hallazgos para la planilla

- Equipo incompleto: Julian Samuel Cabeza Pena no aparece en README.md ni Equipo.md.
- Historial de contribuciones solo muestra a PedroC1213 y Cristian Cardeño; falta evidencia de participación del tercer integrante.
- correcciones.md no se pudo contrastar por falta de contenido en la evidencia.
- Pipeline CI sin run verificable para el hash calificado.
- A-02 (modificación de regla) sigue pendiente de prueba en docs/aspectos.md.
- docs/arc42/11-glosario.md está titulado como Sección 12 en lugar de Sección 11.
- README.md menciona docs/decisiones-arquitectonicas-explicadas.md pero el árbol muestra docs/decisiones-arquitectonicas-explicadas.md ausente; el enlace apunta a un archivo que no está en el árbol.
- docs/arc42/08-conceptos-transversales.md contiene un bloque de instrucciones 'DÓNDE VA' que parece copiado de una guía.
- docs/c4/03-componentes.md declara endpoints de historial como 'previsto, no implementado' aunque el código y las pruebas los implementan.
- docs/arc42/05-vista-de-bloques.md aún describe rutas solo GET /health y POST /analysis como pendiente, desactualizado frente al código.
