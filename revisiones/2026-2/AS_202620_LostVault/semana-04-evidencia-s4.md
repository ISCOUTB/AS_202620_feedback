# semana-04-evidencia-s4 · LostVault

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `952af8f` (2026-08-30T22:13:14-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/01_objetivos.md, 02_restricciones.md, 03_contexto.md, 04_estilo_arquitectonico.md, 05_vista_bloques.md, 06_vista_runtime.md con contenido redactado; sin coincidencias de plantilla en extractos | Cumple | Secciones presentes y redactadas |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09_decisiones.md incluye tabla con enlace a docs/adr/0001-estilo-arquitectonico.md | Cumple | Sección 9 cita ADR 0001 |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10_requisitos_calidad.md define 4 escenarios (disponibilidad, usabilidad, seguridad, rendimiento) coherentes con docs/aspectos.md | Cumple | Coherencia verificada |
| Glosario iniciado con términos del dominio | docs/arc42/glosario.md contiene términos propios: LostVault, Monolito modular, Claims, Identity Verification, etc. | Cumple | Glosario con términos del sistema |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/contexto.mmd (nivel1) y docs/c4/C4 nivel 2.jpg (imagen) presentes; no se puede inspeccionar contenido del JPG para verificar actores/contenedores | No verificado | Falta evidencia textual del nivel 2; se requiere diagrama como código o descripción |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Estructura de código lib/features/* coincide con módulos documentados en docs/arc42/05_vista_bloques.md, pero diagrama nivel2 es imagen no inspeccionable | No verificado | No se puede contrastar contenedores del diagrama con directorios |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README describe flujo: lib/main.dart (UI) → lib/features/claims/application/claim_object_use_case.dart (lógica) → lib/features/*/infrastructure/in_memory_* (persistencia) | Cumple | Recorrido completo documentado y archivos existen |
| Arranque documentado con un solo comando | README sección 'Ejecutar el corte vertical' indica 'flutter run -d chrome' y requisitos previos | Cumple | Comando único declarado |
| Prueba automatizada del recorrido completo, en verde | Existen test/claim_object_use_case_test.dart y test/widget_test.dart, pero no se proporciona URL de run de CI | No verificado | Falta evidencia de ejecución en verde |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | README declara 'La entrega actual implementa una fila completa hasta pruebas: AS-03 Seguridad'; docs/aspectos.md contiene fila AS-03 (extracto truncado pero referenciada) | Cumple | Fila AS-03 enlaza ADR, C4, código y pruebas según README |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_LostVault público, visible; autores incluyen Roy Gonzalez, Fausto-4, shamarallorente-blip, Jose Faustino España, weller-rar, Shamara Llorente Tapias (consolidados corresponden a 4 integrantes) | Cumple | Nombre y visibilidad correctos; integrantes aparecen en historial |
| Estructura mínima | Árbol muestra docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura requerida presente |
| Versionado | Commit calificado 952af8f con fecha 2026-08-30T22:13:14-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Commit vigente correcto |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md sigue nombre y tiene contexto, decisión, alternativas, consecuencias, pero no incluye sección de trazabilidad (requisito, C4, commit, pruebas) | No cumple | Falta trazabilidad explícita en ADR |
| La tabla de aspectos | docs/aspectos.md existe con columnas requeridas; fila AS-03 completa hasta pruebas según README; otras filas pendientes pero permitido por semana | Cumple | Formato correcto y al menos una fila completa |
| Registro de uso de IA | docs/ia.md existe y tiene commit, pero contenido no visible en evidencia proporcionada | No verificado | No se puede verificar si incluye qué se rechazó y por qué |
| README | README.md incluye qué es, requisitos, comando de arranque 'flutter run -d chrome' y cómo probar | Cumple | Documentación de arranque y pruebas presente |
| Pipeline y análisis estático | .github/workflows/flutter.yml existe, pero no se proporcionan runs de CI ni URL | No verificado | Falta evidencia de ejecución del pipeline |

## Recuento y nota sugerida

7 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Coherencia C4 nivel1-nivel2 (imagen no inspeccionable)
- Correspondencia C4 nivel2-código (imagen no inspeccionable)
- Prueba automatizada en verde (sin URL de run)
- Registro de IA (contenido no visible)
- Pipeline ejecutado (sin runs)

## Hallazgos para la planilla

- C4 nivel 2 solo como imagen JPG, no verificable
- ADR 0001 sin trazabilidad explícita
- No se evidencia ejecución de CI
- docs/ia.md sin contenido visible
- Autores con identidades duplicadas (mismo correo) requieren consolidación
