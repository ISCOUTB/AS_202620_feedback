# semana-04-evidencia-s4 · mapsutb

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `f0d036a` (2026-08-30T22:53:06-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/Arc42/05_building_block_view.adoc contiene bloques ifdef::arc42help[] con texto de plantilla sin sustituir | No cumple | Secciones 1-4 y 6 redactadas, pero la 5 incluye texto de plantilla |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/Arc42/09_architecture_decisions.adoc enlaza a ../adr/0001-patrones-de-diseno.md | Cumple | Tabla con ADR-0001 aceptado |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/Arc42/10_quality_requirements.adoc referencia docs/escenarios_calidad.md y enlaza escenarios | Cumple | Coherente con atributos de sección 1.2 |
| Glosario iniciado con términos del dominio | docs/Arc42/12_glossary.adoc existe pero no se incluyó contenido | No verificado | Falta comprobar términos propios del sistema |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/C4/C1.md y C2.md existen, sin contenido en evidencia | No verificado | No se pudo verificar coherencia de actores/contenedores |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin contenido de C4 para contrastar con lib/ | No verificado | Falta comparar contenedores con directorios |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Solo lib/features/zonas/presentation/screens/zonas_screen.dart, lib/repositories/zona_repository.dart y lib/models/; README declara 'Sin lógica de negocio todavía' | No cumple | No hay capa de lógica que decida; falta servicio o caso de uso |
| Arranque documentado con un solo comando | README.md sección 'Arranque con un solo comando' con ./scripts/start.sh; script existe en scripts/start.sh | Cumple | Requisitos previos declarados |
| Prueba automatizada del recorrido completo, en verde | test/app_smoke_test.dart existe, pero sin contenido ni URL de run | No verificado | No se pudo comprobar cobertura del recorrido ni ejecución en CI |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md existe, sin contenido | No verificado | Falta verificar celdas navegables |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_mapsutb público, 4 autores en historial | No verificado | Falta mapear cuentas a integrantes declarados y confirmar pertenencia a ISCOUTB |
| Estructura mínima | README.md, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md presentes; docs/Arc42/ con mayúscula | Cumple | Desviación de ruta docs/arc42/ a docs/Arc42/ |
| Estado del repositorio (versionado) | Commit f0d036a fecha 2026-08-30T22:53:06-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin etiqueta requerida para evidencia semanal |
| Convenciones de ADR | docs/adr/0001-patrones-de-diseno.md cumple patrón de nombre | Cumple | Sin evidencia de edición posterior |
| Tabla de aspectos | docs/aspectos.md existe, sin contenido | No verificado | Falta verificar columnas y filas |
| Registro de uso de IA | docs/ia.md existe con commits, sin contenido | No verificado | Falta comprobar qué se rechazó y por qué |
| README | README.md incluye requisitos previos, arranque con un solo comando y cómo probar | Cumple | Cumple |
| Pipeline y análisis estático | No existe .github/workflows/ en el árbol | No cumple | Sin CI configurada |

## Recuento y nota sugerida

3 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.2 = 1 + 4 × (3/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Glosario: falta contenido de docs/Arc42/12_glossary.adoc
- C4 niveles 1 y 2: falta contenido de docs/C4/C1.md y C2.md
- Correspondencia C4-código: falta contenido de C4 para contrastar
- Prueba del recorrido completo: falta contenido de test y URL de run
- Fila de aspectos: falta contenido de docs/aspectos.md
- Identidad: falta mapeo de cuentas a integrantes
- Tabla de aspectos: falta contenido
- Registro de IA: falta contenido de docs/ia.md

## Hallazgos para la planilla

- Texto de plantilla arc42 sin sustituir en sección 5
- No hay capa de lógica en el corte vertical; README admite 'Sin lógica de negocio todavía'
- No existe pipeline de CI (.github/workflows/)
- Contenido de glosario, aspectos, IA y C4 no verificable por falta de datos
- Ruta docs/Arc42/ con mayúscula, desviación de estructura
