# semana-04-evidencia-s4 · TAIA

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `c087303` (2026-08-30T18:54:10-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md (secciones 1-2 visibles); commit 0152345 actualiza 5, 6, 10 y 12 | No verificado | Contenido de secciones 3-4 no inspeccionable en la evidencia; falta ejecutar grep de plantilla. |
| arc42 sección 9 al día y enlazada con los ADR existentes | Sin contenido visible de la sección 9 en la evidencia | No verificado | Falta inspeccionar la sección 9 y su enlace a docs/adr/0001-estilo-arquitectonico.md. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | Commit 0152345 actualiza sección 10; escenarios en docs/calidad/escenarios_calidad.md | No verificado | Sin el texto de la sección 10 no se confirma la coherencia con S1-S5. |
| Glosario iniciado con términos del dominio | Commit 0152345 inicia sección 12 de arc42 | No verificado | Sin el texto del glosario no se confirman términos propios del sistema. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/C4-C1.md y docs/c4/C4-C2.md (hash c087303) | Cumple | Actor estudiante y sistemas externos Telegram/LLM coherentes entre niveles; flechas etiquetadas y leyenda; diagramas como código Mermaid. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/C4-C2.md vs árbol backend/ | Cumple | API TAIA corresponde a backend/app/modules/academic/adapters/api.py; App Móvil y Base de Datos dibujadas sin código (objetivo declarado en README). |
| Corte vertical que atraviesa interfaz, lógica y persistencia | backend/app/modules/academic/adapters/api.py, application/register_task.py, adapters/in_memory_task_repository.py, domain/task.py | Cumple | Recorrido HTTP → caso de uso → dominio → persistencia en memoria. |
| Arranque documentado con un solo comando | README.md sección Requisitos/Ejecución; run.bat en el árbol | Cumple | Comando declarado: .\run.bat; no se ejecutó por ausencia de runs_ci. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_academic_register_task.py existe; runs_ci vacío | No verificado | Sin run en verde; docs/ia.md entrada 05 declara pendiente ejecutar pytest. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 (hash c087303) | Cumple | Celdas ID→Evidencia verificadas; todas las rutas existen en el árbol. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant en ISCOUTB, visible; autores: val, dei0811, mark, luis20072002 | Cumple | 4 identidades consolidadas coinciden con los integrantes declarados. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | arc42 en un solo archivo; desviación menor permitida por la ficha. |
| Estado del repositorio que se califica | c087303 2026-08-30T18:54:10-05:00 anterior al cierre 2026-08-31T05:00:00Z; sin commits post cierre | Cumple | Sin etiqueta, pero es evidencia semanal y el commit es anterior al cierre. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md existe y nombra la decisión | No cumple | Falta sección de trazabilidad (requisito/aspecto, C4, commit, pruebas) exigida por el contrato. |
| Tabla de aspectos | docs/aspectos.md fila A-01 con 8 columnas y rutas verificadas | Cumple | Cadena aspecto→requisito→C4→ADR→código→pruebas→evidencia navegable. |
| Registro de uso de IA | docs/ia.md con entradas 001-005, cada una con aceptado/rechazado y verificación | Cumple | Log crece de 2026-08-06 a 2026-08-30. |
| README | README.md con descripción, requisitos, comando .\run.bat y pytest backend/tests | Cumple | Ejecución no verificada por ausencia de runs_ci. |
| Pipeline y análisis estático | Sin .github/workflows/ en el árbol; runs_ci vacío | No cumple | No hay CI en cada push ni SonarCloud; sin enlace a run alternativo. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `c0873031acbab61c644e1fac546915b7dde5d1cb 2026-08-30T18:54:10-05:00 docs: change prueba  (readme) add ia entry (ia.md) change c2 text`
- **Veredicto**: con pendientes
- Resumen: Proyecto con corte vertical ejecutable y documentación arc42/C4 en avance, pero con pendientes de la semana 4 sin resolver: sin evidencia de pruebas en CI, ADR sin trazabilidad y pipeline ausente.

Pendientes que siguen abiertos:
- Ejecutar pytest y evidenciar run en verde
- Completar trazabilidad del ADR-0001
- Verificar contenido de secciones arc42 3, 4, 9, 10 y 12
- Configurar CI/SonarCloud o evidenciar plataforma alternativa
- Alinear C4 nivel 2 con el código actual

## Recuento y nota sugerida

5 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.0 = 1 + 4 × (5/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de secciones 3, 4, 9, 10 y 12 de arc42 (evidencia truncada; falta inspeccionar el archivo completo).
- Ejecución de pytest en CI (runs_ci vacío; comando: pytest backend/tests).

## Hallazgos para la planilla

- docs/arc42/arc42-template-EN.md conserva el nombre y front matter de plantilla ('Template').
- Sin runs_ci: la prueba del corte vertical no tiene evidencia de ejecución en verde.
- docs/ia.md entrada 05 declara pendiente ejecutar pytest.
- ADR-0001 carece de trazabilidad explícita (requisito, C4, commit, pruebas).
- No hay .github/workflows/ ni evidencia de CI/SonarCloud.
- C4-C2 dibuja App Móvil y Base de Datos sin código en el repositorio.
- Sin secretos ni .env versionados.
- Historial con 4 identidades; todos los integrantes contribuyen.
