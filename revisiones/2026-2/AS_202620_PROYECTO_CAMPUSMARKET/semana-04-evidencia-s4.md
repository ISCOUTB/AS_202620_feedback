# semana-04-evidencia-s4 · CampusMarket

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `a3e370d` (2026-08-28T18:13:03-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/ARC42.md (sección 1), docs/arc42/02-restricciones.md, 03-contexto.md, 04-estrategia-de-solucion.md, 05-bloques-de-construccion.md, 06-vista-ejecucion.md | Cumple | Secciones redactadas con contenido propio del proyecto. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09-decisiones.md | Cumple | Tabla índice con enlace a ADR-0001. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10-arbol-de-utilidad.md y docs/arc42/10-escenarios-de-calidad.md | Cumple | Escenarios EC-01 a EC-04 coherentes con el árbol de utilidad. |
| Glosario iniciado con términos del dominio | docs/arc42/12-glosario.md | Cumple | Tabla con términos propios del sistema (Publicación, Producto, Modalidad, etc.). |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/01-contexto.puml, docs/c4/02-contenedores.puml | Cumple | Actores y contenedores corresponden entre niveles. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/02-contenedores.puml y estructura backend/app, frontend/campusmarket/lib | Cumple | Contenedores Frontend Web, Backend API y Persistencia local corresponden a directorios. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | docs/arc42/06-vista-ejecucion.md y rutas frontend/campusmarket/lib/publicaciones/publicacion_form_page.dart, backend/app/publicaciones/router.py, service.py, repository.py | Cumple | Recorrido documentado y archivos presentes. |
| Arranque documentado con un solo comando | README.md (extracto no muestra comando único) | No verificado | No se pudo confirmar un comando único de arranque; se requiere ver README completo. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_publicaciones_vertical.py y .github/workflows/backend-tests.yml | No verificado | No se proporciona URL de run ni conclusión; se requiere consultar GitHub Actions. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md (sin contenido) | No verificado | No se incluye contenido del archivo; se requiere inspeccionar la fila. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_PROYECTO_CAMPUSMARKET, visible true | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Rutas requeridas presentes. |
| Estado calificado/versionado | hash a3e370d, fecha 2026-08-28T18:13:03-05:00, cierre 2026-08-31T05:00:00Z | Cumple | Commit anterior al cierre. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md | Cumple | Nombre sigue convención y contenido incluye contexto, alternativas y decisión. |
| Tabla de aspectos | docs/aspectos.md (sin contenido) | No verificado | No se pudo verificar fila completa. |
| Registro de uso de IA | docs/ia.md (sin contenido) | No verificado | No se pudo verificar columnas requeridas. |
| README | README.md (extracto no muestra comando único) | No verificado | No se pudo confirmar arranque con un solo comando. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml | No verificado | No se proporciona run de CI ni conclusión. |

## Recuento y nota sugerida

7 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Arranque documentado con un solo comando: falta ver README completo.
- Prueba automatizada en verde: falta URL de run de GitHub Actions.
- Fila de aspectos completa: falta contenido de docs/aspectos.md.
- Tabla de aspectos (transversal): falta contenido.
- Registro de IA (transversal): falta contenido.
- README (transversal): falta comando único.
- Pipeline (transversal): falta run de CI.

## Hallazgos para la planilla

- arc42 secciones 1-6 redactadas sin texto de plantilla.
- C4 niveles 1 y 2 coherentes y como código.
- Corte vertical documentado con rutas de interfaz, lógica y persistencia.
- No se pudo verificar comando único de arranque en README.
- No se pudo verificar fila completa de aspectos.
- No se pudo verificar ejecución en verde del pipeline.
- No se pudo verificar contenido de docs/ia.md.
