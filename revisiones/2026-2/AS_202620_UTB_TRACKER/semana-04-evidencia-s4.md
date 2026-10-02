# semana-04-evidencia-s4 · TRACTAR

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | `2b16439` (2026-08-30T15:02:33-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42.md en 2b16439 muestra secciones 1-4; el preámbulo conserva 'About arc42' y 'Template Version 9.0-EN' | No cumple | No se localizan secciones 5 y 6 en el commit calificado; el diff posterior modifica arc42.md |
| arc42 sección 9 al día y enlazada con los ADR existentes | Sin sección 9 en docs/arc42/arc42.md de 2b16439; docs/adr/0001-estilo-arquitectonico.md existe | No cumple | ADR-0001 presente pero no hay sección 9 que lo enlace |
| arc42 sección 10 coherente con los escenarios de la semana 2 | Sin sección 10 en docs/arc42/arc42.md de 2b16439; escenarios QS-01 a QS-05 en docs/aspectos.md | No cumple | Los escenarios existen en aspectos.md pero no en arc42 |
| Glosario iniciado con términos del dominio | Sin sección 12 en docs/arc42/arc42.md de 2b16439 | No cumple | No hay glosario con términos del dominio |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | Solo docs/c4/c4_nivel1.md en 2b16439; docs/c4/C2.md aparece en HEAD e88a3d6 | No cumple | Falta el nivel 2 en el commit calificado |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin C4 nivel 2 en 2b16439; estructura app/routers/{users,loans,resources}.py | No cumple | No hay diagrama nivel 2 que contrastar con el código |
| Corte vertical que atraviesa interfaz, lógica y persistencia | app/main.py y app/routers/*.py en 2b16439; sin app/database.py ni app/models.py (aparecen en HEAD) | No cumple | El recorrido no llega a persistencia en el commit calificado |
| Arranque documentado con un solo comando | README.md sección 'Cómo arrancar' documenta ./run.sh; run.sh presente en 2b16439 | No verificado | No se ejecutó el arranque en esta revisión; el CI ejecuta pytest, no run.sh |
| Prueba automatizada del recorrido completo, en verde | app/tests/test_main.py solo verifica /salud/; run 33332531233 success en 2b16439 | No cumple | La prueba no ejercita interfaz-lógica-persistencia; no hay corte vertical |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 con ID, aspecto, requisito, C4, ADR, código y pruebas; app/routers/users.py y ADR-0001 existen | Cumple | Celda Pruebas es descriptiva ('health check') y no enlaza el archivo de prueba |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_TRACTAR público; shortlog HEAD: 19 commits todos de Sebastian Garcia Devoz | No cumple | 3 integrantes declarados sin commits en el historial; runs_ci referencian AS_202620_UTB_TRACKER |
| Estructura mínima | docs/arc42/arc42.md, docs/adr/0001 y 0002, docs/c4/c4_nivel1.md, docs/aspectos.md, docs/ia.md, README.md en 2b16439 | Cumple | docs/adr/0002.md vacío pero presente |
| Estado calificado / versionado | Commit 2b16439 2026-08-30T15:02:33-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin etiqueta; hay 1 commit posterior e88a3d6 que no afecta la nota de S4 |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md válido; docs/adr/0002.md vacío y nombre fuera de patrón NNNN-titulo-kebab-case.md | No cumple | ADR-0002 no cumple convención de nombre ni contenido |
| Tabla de aspectos | docs/aspectos.md con 5 filas; celdas Código/Pruebas '—' en A-03/A-04 y Evidencia '—' en todas | No cumple | La cadena hasta Evidencia no es navegable en el commit calificado |
| Registro de uso de IA | docs/ia.md con 2 entradas del 2026-08-16; ninguna documenta qué se rechazó y por qué | No cumple | Falta la columna de lo rechazado con motivo técnico |
| README y reproducibilidad | README.md documenta ./run.sh y pytest; run.sh presente | No verificado | No se ejecutó el arranque en esta revisión |
| Pipeline, secretos y autoría | .github/workflows/ci.yml ejecuta pytest; run 33332531233 success en 2b16439, run 33373654206 failure en HEAD; sin SonarCloud; sin secretos; shortlog con un solo autor | No cumple | CI sin análisis estático, HEAD en rojo y autoría concentrada |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `e88a3d675be7702da4ad7e16495d38bbf132f1ae 2026-08-31T03:35:36-05:00 feat: S4 Advances`
- **Veredicto**: con pendientes
- Resumen: En el commit calificado 2b16439 la S4 está incompleta (arc42 parcial, sin C4 nivel 2, sin corte vertical con persistencia, sin glosario). El commit e88a3d6 posterior al cierre añade los artefactos faltantes, pero el CI de HEAD falla y la autoría sigue concentrada en un solo integrante.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- e88a3d6 (2026-08-31T03:35:36-05:00) añade C4 nivel 2, ADR 0002, persistencia y pruebas de loans/resources después del cierre de S4
- El run CI 33373654206 en HEAD concluye en failure, por lo que las pruebas nuevas no están en verde

Pendientes que siguen abiertos:
- Pipeline en rojo a HEAD
- Autoría: 3 integrantes declarados sin commits en el historial
- Sin análisis estático SonarCloud
- Glosario y secciones 5/6/9/10 de arc42 no verificados en HEAD

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Arranque con ./run.sh: no ejecutado en esta revisión; comando documentado en README
- Secciones 5, 6, 9, 10 y 12 de arc42 en el commit calificado: no localizadas en el contenido disponible

## Hallazgos para la planilla

- arc42.md en 2b16439 solo muestra secciones 1-4; faltan 5, 6, 9, 10 y 12 en el commit calificado
- Preámbulo de arc42 conserva texto de plantilla sin sustituir
- docs/adr/0002.md está vacío y con nombre fuera de convención
- C4 nivel 2 ausente en el commit calificado; se añade en e88a3d6 post cierre
- Corte vertical sin persistencia en 2b16439; database.py, models.py y schemas.py aparecen solo en HEAD
- Prueba existente solo cubre /salud/, no un recorrido completo
- CI en verde en 2b16439 (run 33332531233) pero en rojo en HEAD (run 33373654206)
- Historial con un solo autor: Sebastian Garcia Devoz; 3 integrantes sin commits
- docs/ia.md no documenta rechazos de IA
- Sin análisis estático SonarCloud
- ADR-0001 describe Django pero el código implementado es FastAPI; el cambio se documenta en ADR-0002 solo en HEAD
- Commits posteriores al cierre (no calificados): e88a3d6 2026-08-31T03:35:36-05:00 feat: S4 Advances
