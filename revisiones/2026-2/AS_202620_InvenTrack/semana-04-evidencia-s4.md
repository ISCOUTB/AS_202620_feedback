# semana-04-evidencia-s4 · InvenTrack

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `d7ba824` (2026-08-30T23:39:33-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md (d7ba824) declara solo secciones 1, 2, 3 y 10 completas; README lista 4-6 como pendientes | No cumple | Faltan secciones 4, 5 y 6 en el commit calificado |
| arc42 sección 9 al día y enlazada con los ADR existentes | Sin encabezado de sección 9 en arc42-template-EN.md (d7ba824); README no la lista | No cumple | Sección 9 ausente; no enlaza ADR |
| arc42 sección 10 coherente con los escenarios de la semana 2 | arc42-template-EN.md sección Quality Requirements; docs/utility-tree.md lista ESC-01 a ESC-05 | Cumple | Coherente con escenarios de semana 2 |
| Glosario iniciado con términos del dominio | Sin sección 12 en arc42-template-EN.md (d7ba824); README marca Glossary pendiente | No cumple | Glosario no iniciado |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/context.md y docs/c4/containers.md; actores Dueño/Vendedor/Empleado coinciden; flechas HTTPS/SMTP etiquetadas | Cumple | Diagramas en Mermaid (código), con leyenda |
| Límites del C4 nivel 2 correspondientes a la estructura del código | containers.md tabla: API Backend ↔ app/; Interfaz web y BD 'no existen en el repositorio' | No cumple | Web y BD dibujadas sin código; API Backend sí corresponde a app/ |
| Corte vertical que atraviesa interfaz, lógica y persistencia | app/productos/infrastructure/router.py (interfaz), app/productos/application/crear_producto.py (lógica), app/productos/infrastructure/in_memory_repository.py (persistencia); tests/productos/test_api_corte_vertical.py | Cumple | Recorrido productos atraviesa las tres capas |
| Arranque documentado con un solo comando | docs/adr/0001-...md cita 'python -m uvicorn app.main:app --reload' como comando en README | No verificado | No ejecutado; README truncado impide verificación directa |
| Prueba automatizada del recorrido completo, en verde | tests/productos/test_api_corte_vertical.py en d7ba824; run 33357886282 (Run Tests, success, 2026-08-31T04:40:01Z) | Cumple | Pipeline ejecuta pytest; run más cercano al commit calificado en verde |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila ASP-01: Pruebas = 'Pendiente'; C4 = 'C4 de contexto — módulo inventario' sin módulo en context.md | No cumple | Celda Pruebas no navegable; C4 no muestra módulo inventario |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible:true, repo AS_202620_InvenTrack en ISCOUTB; shortlog muestra Josephva24/Jose Vargas, Esteban Peluffo, Felix Taborda/FlexT21/negro, jxviercarta-a11y | Cumple | 4 integrantes identificados tras consolidar identidades |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md en árbol | Cumple | Desviación: docs/adr/0002-... sin extensión .md |
| Estado calificado / versionado | d7ba824 2026-08-30T23:39:33-05:00 (04:39Z) anterior al cierre 05:00Z | Cumple | Entrega semanal sin etiqueta; commit dentro del plazo |
| Convenciones de ADR | docs/adr/0002-usar-monolito-modular-con-hexagonal-por-modulo sin .md y duplicando contenido del 0001 | No cumple | Violación de nomenclatura y de 'un ADR por decisión' |
| Tabla de aspectos | docs/aspectos.md ASP-01 con Pruebas 'Pendiente' y C4 no específico | No cumple | Cadena de trazabilidad con huecos |
| Registro de uso de IA | docs/ia.md con tabla Fecha/Etapa/Uso/Rechazado/Nivel; 9 commits en log | Cumple | Columna de rechazado con motivos técnicos |
| README | README.md con descripción, estructura, stack; ADR-0001 cita comando de arranque | No verificado | Sección de arranque y pruebas no legible en el fragmento disponible |
| Pipeline y análisis estático | .github/workflows/test.yml presente; runs success; sin evidencia de SonarCloud | No cumple | CI en verde; falta análisis estático |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `385fbe223297d02efa18366885bee782091940c1 2026-08-31T01:23:01-05:00 fix: update AI tools section to clarify ChatGPT/Gemini usage and enhance usage log details`
- **Veredicto**: con pendientes
- Resumen: La entrega S4 en el commit del cierre está incompleta (arc42 4-6, 9, 12 ausentes; aspectos con huecos); commits posteriores la completaron parcialmente.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- arc42 actualizado tras el cierre (2fc55e1, b4904bd)
- Módulo de inventario añadido tras el cierre (666c4e4)
- ADR-0002 eliminado tras el cierre (64ab86f)
- aspectos.md y containers.md corregidos tras el cierre (4e6957e, 3de2988)

Pendientes que siguen abiertos:
- Confirmar si arc42 secciones 4-6 y 12 quedaron redactadas a HEAD
- Añadir evidencia de análisis estático SonarCloud
- Completar celda de Pruebas en docs/aspectos.md

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Arranque con un solo comando: comando declarado 'python -m uvicorn app.main:app --reload' vía ADR-0001; no ejecutado y README truncado
- README: sección de arranque y pruebas no legible en el fragmento disponible
- arc42 en HEAD: contenido tras commits post-cierre no disponible para confirmar secciones 4-6 y 12

## Hallazgos para la planilla

- arc42 en d7ba824 solo tiene secciones 1, 2, 3 y 10; faltan 4, 5, 6 y 12
- Sección 9 de arc42 ausente en el commit calificado
- ADR-0002 duplica al 0001 y no sigue la convención de nomenclatura
- Contenedores Web y Base de datos del C4 nivel 2 sin código en el repositorio
- Fila ASP-01 de aspectos.md deja Pruebas en 'Pendiente'
- Commits posteriores al cierre completaron la entrega (arc42, inventario, ADR)
- Sin evidencia de análisis estático SonarCloud
- Commits posteriores al cierre (no calificados): 385fbe2 2026-08-31T01:23:01-05:00 fix: update AI tools section to clarify ChatGPT/Gemini usage and enhance usage log details; 89e3278 2026-08-31T01:18:45-05:00 Merge branch 'main' of https://github.com/ISCOUTB/AS_202620_InvenTrack; 6f2e5e2 2026-08-31T01:18:21-05:00 fix: update README.md for improved clarity and structure in navigation and documentation sections; 45d2fa0 2026-08-31T01:01:24-05:00 fix: update architectural decision record to reflect acceptance and clarify structure; 64ab86f 2026-08-31T00:59:56-05:00 Delete docs/adr/0002-usar-monolito-modular-con-hexagonal-por-modulo
