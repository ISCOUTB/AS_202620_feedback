# semana-04-evidencia-s4 · CampusMarket

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `f3f4367` (2026-08-30T22:55:30-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/ARC42.md (secciones 1-4), 02-restricciones.md, 03-contexto.md, 04-estrategia-de-solucion.md, 05-bloques-de-construccion.md, 06-vista-ejecucion.md | Cumple | Contenido propio de CampusMarket; sin rastros de plantilla arc42. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09-decisiones.md enlaza a docs/adr/0001-usar-monolito-modular.md | Cumple | Sección 9 funciona como índice trazable del ADR-0001. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10-escenarios-de-calidad.md y 10-arbol-de-utilidad.md con EC-01 a EC-04 | Cumple | Escenarios con medidas verificables y coherentes con ADR-0001. |
| Glosario iniciado con términos del dominio | docs/arc42/12-glosario.md | Cumple | Términos propios: Publicación, Producto, Modalidad, Estado del producto, Corte vertical. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/01-contexto.puml y 02-contenedores.puml | Cumple | Actores Estudiante y Administrador coherentes entre niveles; flechas etiquetadas y leyenda. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/02-contenedores.md; frontend/campusmarket/lib/, backend/app/, backend/app/publicaciones/repository.py | Cumple | Frontend Web ↔ frontend/campusmarket/lib/, Backend API ↔ backend/app/, Persistencia ↔ repository.py. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | frontend/campusmarket/lib/publicaciones/publicacion_form_page.dart, backend/app/publicaciones/router.py, service.py, repository.py | Cumple | Recorrido Flutter Web → FastAPI → lógica → SQLite documentado en README. |
| Arranque documentado con un solo comando | README.md sección 'Arranque con un solo comando'; scripts/run_s4.sh y run_s4.ps1 | No verificado | Documentado pero no ejecutado por el agente; comando declarado: bash scripts/run_s4.sh. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_publicaciones_vertical.py; run 'Pruebas del backend' success 2026-08-31T03:55:33Z (https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/33355385223) | Cumple | Prueba crea, persiste y consulta publicación; pipeline en verde. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila ASP-05 | Cumple | ASP-05 enlaza requisito, C4, ADR, código y prueba; rutas verificadas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET visible; historial con Nnigarp, camilixo92, Carulla-sd | Cumple | Tres integrantes con commits; identidades consolidadas. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Rutas mínimas presentes. |
| Versionado y estado calificado | Commit f3f4367 2026-08-30T22:55:30-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin commits posteriores al cierre. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md | Cumple | Nombre en kebab-case, título enuncia decisión, incluye contexto, alternativas y trazabilidad. |
| Tabla de aspectos | docs/aspectos.md con 8 columnas; fila ASP-05 completa | Cumple | ASP-05 navegable hasta Pruebas; otras filas con huecos permitidos según semana. |
| Registro de uso de IA | docs/ia.md con 5 commits entre 2026-08-08 y 2026-08-30 | Cumple | Incluye herramienta, uso, verificación y qué se rechazó con motivo. |
| README | README.md con descripción, arranque, pruebas, CI y trazabilidad | Cumple | Documenta qué es, cómo arrancar y cómo probar. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml solo ejecuta pytest; sin SonarCloud | No cumple | Falta análisis estático SonarCloud exigido por contrato sección 8 y R-04. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `f3f436713bc79a7da4d5792c4f0876cc85fcdd3c 2026-08-30T22:55:30-05:00 Merge pull request #13 from ISCOUTB/S4-registro-ia-cierre`
- **Veredicto**: con pendientes
- Resumen: La entrega S4 cumple 9/10 criterios de la ficha; el único no verificado es el arranque por falta de ejecución. La matriz transversal tiene 7/8, con SonarCloud pendiente. No hay correcciones tardías ni commits posteriores al cierre.

Pendientes que siguen abiertos:
- Integrar SonarCloud al pipeline
- Verificar arranque con un solo comando mediante ejecución
- Enlazar ADR-0001 con commit que lo implementa
- Definir medición de línea base

## Recuento y nota sugerida

9 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.6 = 1 + 4 × (9/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Arranque con un solo comando: no ejecutado; comando declarado: bash scripts/run_s4.sh.

## Hallazgos para la planilla

- Falta integración con SonarCloud en el pipeline.
- Arranque documentado pero no ejecutado por el agente.
- Diagramas C4 versionados como código PlantUML.
- ADR-0001 no enlaza commit que lo implementa.
- Sin medición de línea base todavía.
- Sin secretos ni .env versionados.
- Autoría distribuida entre los tres integrantes.
