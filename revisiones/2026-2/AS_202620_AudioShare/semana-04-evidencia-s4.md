# semana-04-evidencia-s4 · AudioShare

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `24a5023` (2026-08-30T23:48:29-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/src/01_introduction_and_goals.adoc ... 06_runtime_view.adoc | Cumple | Contenido redactado, sin rastros de plantilla |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/src/09_section_desing_decisions.adoc | No cumple | No cita docs/adr/NNNN-*.md; repite decisiones sin enlazar |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/src/10_quality_requirements.adoc | Cumple | Referencia EC-01 a EC-04 coherentes con escenarios_calidad.md |
| Glosario iniciado con términos del dominio | docs/arc42/src/12_glossary.adoc existe | No verificado | No se pudo comprobar contenido; falta texto del glosario |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/Context - Nivel 1.mmd y Contenedor - Nivel 2.mmd | No verificado | Archivos presentes pero sin contenido para verificar coherencia |
| Límites del C4 nivel 2 correspondientes a la estructura del código | src/modules/{audio,session,sync,shared} | No verificado | Sin contenido del diagrama no se puede contrastar |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README describe corte A-01 | No verificado | Falta código de las tres rutas; no se pudo verificar persistencia |
| Arranque documentado con un solo comando | README.md: 'npm run dev' | Cumple | Requisitos previos declarados y comando único de arranque |
| Prueba automatizada del recorrido completo, en verde | tests/a01.test.ts existe | No verificado | Sin URL de run de CI no se puede confirmar verde |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md existe | No verificado | Sin contenido no se puede verificar completitud |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_AudioShare público en ISCOUTB | Cumple | 4 autores en historial coinciden con integrantes declarados |
| Estructura mínima | docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md | Cumple | Rutas requeridas presentes |
| Versionado | commit 24a5023 2026-08-30T23:48:29-05:00 | Cumple | Anterior al cierre 2026-08-31T05:00:00Z |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md | Cumple | Nombre sigue convención y contiene contexto, opciones, decisión, consecuencias, trazabilidad |
| Tabla de aspectos | docs/aspectos.md existe | No verificado | Sin contenido no se puede verificar cadena completa |
| Registro de uso de IA | docs/ia.md con commits | No verificado | Sin contenido no se puede verificar columnas de aceptado/rechazado |
| README | README.md con secciones de arranque y pruebas | Cumple | Incluye requisitos y comandos |
| Pipeline y análisis estático | sin .github/workflows/ en árbol | No cumple | No hay configuración de CI ni evidencia de runs |

## Recuento y nota sugerida

3 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.2 = 1 + 4 × (3/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Glosario: falta contenido del archivo 12_glossary.adoc
- C4 coherencia: falta contenido de los diagramas .mmd
- Corte vertical: falta código de interfaz, lógica y persistencia
- Prueba en verde: falta URL de run de CI
- Aspectos: falta contenido de docs/aspectos.md
- IA: falta contenido de docs/ia.md

## Hallazgos para la planilla

- Sección 9 de arc42 no enlaza a los ADR existentes
- No se encontró pipeline de CI ni análisis estático
- Falta evidencia de ejecución de pruebas en verde
- Contenido de glosario, C4, aspectos y código no disponible para verificación
- Corte vertical descrito en README pero sin código citado
