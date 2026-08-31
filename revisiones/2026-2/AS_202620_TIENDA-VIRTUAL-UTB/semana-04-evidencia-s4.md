# semana-04-evidencia-s4 · Tienda virtual UTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `0d208a2` (2026-08-29T21:37:39-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md en 0d208a2; secciones 1-4 visibles en español; README declara 1-6 | No verificado | El extracto se trunca antes de las secciones 5 y 6; se requiere inspeccionar el archivo completo. |
| arc42 sección 9 al día y enlazada con los ADR existentes | README.md sección Evidencia S4 declara sección 9; commit 2f619cc | No verificado | Contenido de la sección 9 no visible en la evidencia; no se pudo comprobar el enlace a docs/adr/. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | README.md declara sección 10; docs/escenarios-calidad.md existe | No verificado | Contenido de la sección 10 no visible; no se pudo contrastar con los escenarios. |
| Glosario iniciado con términos del dominio | README.md declara glosario en arc42 | No verificado | Sección 12 no visible en el extracto; no se pudo verificar términos propios del dominio. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/context.md y docs/c4/container.md en 0d208a2 | Cumple | Los tres actores del nivel 1 reaparecen en el nivel 2 conectados al cliente web; flechas etiquetadas. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/container.md vs frontend/app/page.tsx, backend/app/modules/catalog/, compose.yaml | Cumple | Cliente web ↔ frontend/, API ↔ backend/, PostgreSQL ↔ servicio db en compose.yaml. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md: frontend/app/page.tsx → backend/app/modules/catalog/router.py → repository.py/models.py → seed.py | Cumple | Interfaz, lógica y persistencia citadas con rutas existentes. |
| Arranque documentado con un solo comando | README.md sección 'Arranque con un solo comando': docker compose up --build | Cumple | Requisito previo (Docker Compose) declarado; no se ejecutó. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_catalog.py; run 'Pruebas' 33288435368 success 2026-08-30T02:37:54Z | Cumple | El run posterior al commit 0d208a2 ejecuta pytest en verde. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila 'Disponibilidad — consulta del catálogo' | Cumple | Celdas hasta Pruebas con rutas existentes y pruebas citadas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB visible; shortlog: RAZOR7150, Jasen (consolidado), pxtroniwnl, shalom-A26 | Cumple | Cuatro identidades consolidadas coinciden con los integrantes declarados. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md en 0d208a2 | Cumple | Rutas mínimas presentes. |
| Versionado / commit al cierre | 0d208a2 2026-08-29T21:37:39-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin etiqueta; no requerida para evidencias semanales. |
| Convenciones de ADR | docs/adr/0001-monolito-modular.md | No cumple | Falta trazabilidad con commit/PR que lo implementa y pruebas que lo cubren. |
| Tabla de aspectos | docs/aspectos.md | No cumple | Usa 6 columnas; faltan ID, C4, ADR y Evidencia de las 8 del curso. |
| Registro de uso de IA | docs/ia.md | No cumple | No hay columna de 'qué se rechazó y por qué' con motivo técnico. |
| README y reproducibilidad | README.md: arranque con docker compose up --build y pruebas con pytest | Cumple | Requisitos previos declarados y comandos documentados. |
| Pipeline y análisis estático | .github/workflows/tests.yml | No cumple | Solo ejecuta pytest; no hay SonarCloud configurado. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `0d208a27c8017e6cd260082bdc05baa0a6394901 2026-08-29T21:37:39-05:00 Corregir S4: arc42 completo en espanol y ajustes de consistencia`
- **Veredicto**: con pendientes
- Resumen: La S4 cumple 6 de 10 criterios de la ficha; C4, corte vertical, arranque y pruebas verificados. Quedan pendientes de contrato: trazabilidad del ADR, columnas de aspectos, rechazos de IA y SonarCloud.

Pendientes que siguen abiertos:
- Verificar secciones 5, 6, 9, 10 y 12 del arc42
- Trazabilidad del ADR 0001
- Columnas de docs/aspectos.md
- Columna de rechazos en docs/ia.md
- SonarCloud en pipeline

## Recuento y nota sugerida

6 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.4 = 1 + 4 × (6/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Secciones 5, 6, 9, 10 y 12 de docs/arc42/arc42-template-EN.md: el extracto disponible se trunca; se requiere inspeccionar el archivo completo en 0d208a2.

## Hallazgos para la planilla

- El arc42 conserva el nombre 'arc42-template-EN.md' aunque su contenido está en español.
- Las secciones 5, 6, 9, 10 y 12 del arc42 no pudieron verificarse por truncamiento de la evidencia.
- El ADR 0001 carece de trazabilidad con commit/PR y pruebas.
- docs/aspectos.md no implementa las 8 columnas del curso.
- docs/ia.md no registra rechazos con motivo técnico.
- El pipeline no integra SonarCloud.
- C4 nivel 2 coherente con la estructura de frontend/, backend/ y compose.yaml.
- Corte vertical de catálogo documentado y con prueba en verde.
