# semana-04-evidencia-s4 · PideUtb

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `1636f20` (2026-08-30T22:17:18-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | README.md enlaza a arc42.md (secciones 4 y 6); docs/aspectos.md referencia arc42.md §10 | No verificado | No se aportó el contenido de arc42.md en la evidencia; no se pudo comprobar redacción ni ausencia de plantilla. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/adr/0001-estilo-arquitectonico.md existe; sin sección 9 visible | No verificado | Falta el archivo arc42.md para verificar el enlace al ADR. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/aspectos.md cita ESC-01 a ESC-05 de arc42.md §10.2-10.6 | No verificado | No se pudo contrastar la sección 10 con los escenarios por falta de arc42.md. |
| Glosario iniciado con términos del dominio | Sin sección 12 visible en la evidencia | No verificado | No se pudo localizar el glosario; se requiere arc42.md o docs/arc42/. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | No aparecen archivos en docs/c4/ en el árbol de la evidencia | No verificado | No hay diagramas C4 visibles; no se pudo verificar coherencia entre niveles. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin diagramas C4; README describe backend/app/{pedidos,menu,pagos,usuarios} | No verificado | Sin C4 no se puede contrastar contenedores contra directorios. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md describe flujo: app/main.py → pedidos.service → menu.service → repositorios en memoria | No verificado | El README documenta el recorrido, pero no se aportaron las rutas del código para citarlas; persistencia en memoria con TODO(supabase). |
| Arranque documentado con un solo comando | README.md 'Cómo arrancar el backend': python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt && uvicorn app.main:app --reload | Cumple | Requisito previo declarado (Python 3.11+) y un solo comando de arranque. |
| Prueba automatizada del recorrido completo, en verde | README.md menciona tests/test_pedidos.py; sin runs_ci en la evidencia | No verificado | No hay URL de run de CI que muestre la prueba en verde; comando declarado: pytest tests/test_pedidos.py -v. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md tabla con columnas Aspecto, Escenario, Estímulo→Respuesta, Medida, Táctica, Prueba | No cumple | Faltan las columnas ID, C4, ADR y Código exigidas por la ficha; la fila de Usabilidad llega a Prueba pero con esquema incompleto. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad y estructura mínima del repositorio | Repo ISCOUTB/AS_202620_PideUtb visible; docs/adr, docs/aspectos.md, docs/ia.md, README.md presentes; sin docs/c4/; arc42.md referenciado en raíz | No cumple | Falta docs/c4/ y arc42 no está en docs/arc42/ (desviación de estructura). |
| Versionado: commit vigente al cierre y etiquetas | hash_calificado 1636f20, fecha 2026-08-30T22:17:18-05:00 (antes del cierre); commits_tardios_post_cierre vacío | No verificado | El commit está antes del cierre, pero no hay evidencia de tags (corte-1, etc.). |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md con contexto, alternativas, decisión y consecuencias | No cumple | El nombre cumple la convención, pero falta la trazabilidad exigida (requisito/aspecto, elementos C4, commit/PR, pruebas). |
| Tabla de aspectos con trazabilidad navegable | docs/aspectos.md tabla con 6 columnas; fila Usabilidad con enlaces a arc42.md y tests | No cumple | No incluye las columnas ID, C4, ADR, Código, Evidencia del contrato; celdas no todas navegables. |
| Registro de uso de IA | docs/ia.md documenta usos por entrega con herramienta Claude y revisión del equipo | No cumple | No documenta explícitamente qué se rechazó de la IA y por qué, como exige el contrato. |
| README: qué es, arranque en un comando y pruebas | README.md con descripción, comando único de arranque y sección de pruebas | Cumple | Documenta requisitos previos, arranque y cómo correr pytest. |
| Pipeline y análisis estático | Sin .github/workflows ni runs_ci en la evidencia | No verificado | No hay evidencia de CI en cada push ni de SonarCloud; comando: ls .github/workflows/ y consulta a actions runs. |
| Secretos, autoría y colaboración | Sin .env versionado; grep de secretos solo halla tokens de librerías en .venv-1; autores: daniarriet, Santiago Cuesta/Santiago-C0, ruddy2000utb-droid | Cumple | Tres identidades consolidadas coinciden con el equipo; todos aportan commits; .venv-1 versionado es hallazgo de higiene, no secreto. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `1636f20d14f254dffd9aa9c1eb43e138fba73043 2026-08-30T22:17:18-05:00 Revise diagram legend for clarity and detail`
- **Veredicto**: con pendientes
- Resumen: A HEAD (1636f20) el repositorio tiene README con arranque y corte vertical documentado, ADR 0001, docs/aspectos.md e ia.md, pero faltan los diagramas C4, la tabla de aspectos no cumple el esquema de columnas, el ADR no tiene trazabilidad y no hay evidencia de CI. Varios artefactos de arc42 no se pudieron verificar por falta del archivo en la evidencia.

Pendientes que siguen abiertos:
- C4 niveles 1 y 2 en docs/c4/
- Glosario (sección 12) y secciones 1-6, 9, 10 de arc42 verificables
- Tabla de aspectos con columnas ID, C4, ADR, Código
- Trazabilidad del ADR a commit y pruebas
- docs/ia.md con lo rechazado
- CI con pruebas en verde
- Eliminar .venv-1 del repositorio

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de arc42.md (secciones 1-6, 9, 10 y 12): no aportado en la evidencia.
- Diagramas C4 niveles 1 y 2: no localizados.
- Rutas del corte vertical en backend/: no verificables con la evidencia.
- Ejecución de pruebas en CI: sin runs_ci.
- Etiquetas de versionado: sin evidencia.
- Pipeline/CI: sin archivos de workflow ni runs.

## Hallazgos para la planilla

- Entorno virtual .venv-1 versionado en el repositorio.
- No hay evidencia de diagramas C4 en docs/c4/.
- arc42.md está en la raíz, no en docs/arc42/.
- La tabla de aspectos no tiene las columnas ID, C4, ADR, Código.
- El ADR 0001 carece de trazabilidad a commit, pruebas y elementos C4.
- docs/ia.md no documenta lo rechazado con su motivo.
- Sin runs de CI que evidencien pruebas en verde.
- La persistencia del corte vertical es en memoria (TODO supabase), no una base de datos.
