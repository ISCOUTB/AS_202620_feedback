# semana-04-evidencia-s4 · mapsutb

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `f0d036a` (2026-08-30T22:53:06-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/Arc42/01..06 existen; sección 05 contiene bloques ifdef::arc42help[] con texto de plantilla sin sustituir | No cumple | Secciones 1-4 y 6 redactadas; la 05 conserva plantilla arc42help (Contenido/Motivación/Forma). |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/Arc42/09_architecture_decisions.adoc: tabla con ADR-0001 enlazando a docs/adr/0001-patrones-de-diseno.md | Cumple | Enlaza al ADR existente y no duplica su razonamiento. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/Arc42/10_quality_requirements.adoc: escenarios RE/PR/DI/US/FI/MA/PO alineados con árbol de utilidad y escenarios_calidad.md | Cumple | Coherente con las 7 ramas de calidad de la sección 1.2. |
| Glosario iniciado con términos del dominio | docs/Arc42/12_glossary.adoc: términos MAPSUTB, grafo peatonal, ruteo, tour panorámico, zona, POI, patrones | Cumple | Términos propios del sistema, no genéricos de arquitectura. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/C4/C1.md y docs/C4/C2.md (mermaid) | Cumple | Actores del C1 se consolidan en 'Usuario del campus' en C2; sistemas externos (Maps SDK, Geocoding, sensor) reaparecen conectados. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | C2 dibuja App movil, Datos de zonas, Contenido Panorámico y Plano del Campus; el árbol solo tiene lib/ y assets/data/zonas.json | No cumple | App movil ↔ lib/ y Datos de zonas ↔ assets/data/zonas.json+lib/repositories/zona_repository.dart; faltan Contenido Panorámico y Plano del Campus sin código ni assets. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | lib/features/zonas/presentation/screens/zonas_screen.dart → lib/repositories/zona_repository.dart → assets/data/zonas.json | Cumple | Recorrido de zonas completo: UI lee repositorio que parsea JSON local. |
| Arranque documentado con un solo comando | README.md sección 'Arranque con un solo comando' con ./scripts/start.sh y requisitos previos | No verificado | Documentado; no se ejecutó y no hay runs_ci. Comando declarado: ./scripts/start.sh. |
| Prueba automatizada del recorrido completo, en verde | test/app_smoke_test.dart existe; sin .github/workflows/ ni runs_ci | No verificado | No hay evidencia de ejecución en CI; comando anotado: flutter test. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 con celdas 'Por definir', 'Sin ADR aún', 'Aún no iniciado' | No cumple | La fila describe RA descartada y sus celdas C4/ADR/Código/Pruebas no apuntan a nada; huecos. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_mapsutb en ISCOUTB, público; shortlog con 4 autores | Cumple | Los 4 integrantes declarados aparecen en el historial. |
| Estructura mínima | docs/Arc42/, docs/C4/, docs/adr/, docs/aspectos.md, docs/ia.md, README.md | No cumple | Desviación de nomenclatura: docs/Arc42/ y docs/C4/ con mayúsculas en vez de docs/arc42/ y docs/c4/. |
| Estado del repositorio que se califica (versionado) | f0d036a 2026-08-30T22:53:06-05:00 anterior al cierre; sin etiquetas | No cumple | Sin etiqueta corte-1; se revisó el último commit anterior al cierre. |
| Convenciones de ADR | docs/adr/0001-patrones-de-diseno.md contiene 'Cambio de alcance respecto a la versión anterior de este ADR' | No cumple | ADR aceptado (2026-08-23) fue editado para cambiar alcance en vez de crear ADR 0002; viola la convención. |
| Tabla de aspectos | docs/aspectos.md fila A-01 con celdas 'Por definir'/'Sin ADR aún'/'Aún no iniciado' | No cumple | Fila con huecos y desactualizada respecto al alcance sin RA. |
| Registro de uso de IA | docs/ia.md con 5 entradas (fecha, herramienta, uso, aceptado/rechazado, motivo); 4 commits en su historial | Cumple | Incluye columna de rechazos con motivos técnicos. |
| README | README.md con descripción, estructura, requisitos, arranque con un solo comando y prueba | Cumple | Declara ./scripts/start.sh y flutter test. |
| Pipeline y análisis estático | Sin .github/workflows/ en el árbol; sin runs_ci | No cumple | No hay CI configurado ni evidencia de ejecución; falta SonarCloud. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `f0d036a58248863e5dfe8b18352446dad1bbd59a 2026-08-30T22:53:06-05:00 corte vertical`
- **Veredicto**: con pendientes
- Resumen: Avance sólido en arc42 y C4 con corte vertical de zonas implementado, pero persisten deudas de semanas anteriores (documentos con alcance de RA), ADR editado tras aceptarse, contenedores C2 sin código y ausencia de CI.

Pendientes que siguen abiertos:
- Actualizar ficha-problema.md, escenarios_calidad.md y aspectos.md al alcance sin RA
- Limpiar plantilla arc42 en sección 5
- Implementar o declarar contenedores C2 sin código (panorámicas, plano)
- Añadir CI con runs públicos que ejecuten las pruebas
- Corregir mayúsculas en docs/Arc42 y docs/C4
- Crear etiqueta corte-1
- Registrar cambios de decisión en ADR nuevos, no editando aceptados

## Recuento y nota sugerida

5 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.0 = 1 + 4 × (5/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Arranque con ./scripts/start.sh (no ejecutado; sin runs_ci).
- Prueba test/app_smoke_test.dart en verde (sin runs_ci; no se pudo verificar que ejercite el recorrido completo).

## Hallazgos para la planilla

- docs/Arc42/ y docs/C4/ usan mayúsculas; desviación de la estructura mínima.
- Sección 05 de arc42 conserva bloques de plantilla arc42help sin sustituir.
- Contenedores C2 'Contenido Panorámico 360°' y 'Plano del Campus' sin código ni assets.
- Fila A-01 de docs/aspectos.md desactualizada (describe RA descartada) y con celdas sin enlaces.
- ADR 0001 editado tras su aceptación para cambiar alcance, en vez de crear ADR 0002.
- Sin etiqueta corte-1; se revisó f0d036a como último commit anterior al cierre.
- No hay .github/workflows/ ni runs_ci que evidencien pruebas en verde.
- docs/ia.md reconoce que ficha-problema.md, aspectos.md y escenarios_calidad.md aún describen RA.
