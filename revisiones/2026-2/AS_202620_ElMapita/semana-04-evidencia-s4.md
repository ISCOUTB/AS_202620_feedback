# semana-04-evidencia-s4 · ElMapita

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `07b36f4` (2026-08-30T23:31:03-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md: secciones 1-3 visibles con contenido propio; secciones 4-6 no visibles en la evidencia (archivo truncado) | No verificado | Falta evidencia del texto de las secciones 4-6 para confirmar redacción y ausencia de plantilla |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/adr/0001-estilo-arquitectonico-propuesto.md existe; sección 9 no visible en docs/arc42/arc42-template-EN.md | No verificado | No se pudo comprobar que la sección 9 cite el ADR; haría falta el contenido completo del archivo arc42 |
| arc42 sección 10 coherente con los escenarios de la semana 2 | README.md enlaza #section-quality-scenarios; docs/aspectos.md enlaza #ec-01..#ec-04; texto de sección 10 no visible | No verificado | Indicios de existencia de EC-01..EC-04, pero sin el texto no se verifica coherencia |
| Glosario iniciado con términos del dominio | Sección 12 no visible en docs/arc42/arc42-template-EN.md (archivo truncado en la evidencia) | No verificado | No se encontró evidencia del glosario; haría falta revisar el contenido completo del archivo arc42 |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/C4_L1_Context.md (flowchart con actores, sistema, externos, leyenda); docs/c4/C4_L2_Container.md (C4Container con personas, contenedores, externos y relaciones etiquetadas) | Cumple | Actores y externos del nivel 1 reaparecen en el nivel 2; flechas etiquetadas y leyenda presente |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/C4_L2_Container.md: App Móvil Flutter ↔ frontend/lib/features/; Backend API ↔ backend/src/modules/; Supabase DB ↔ backend/src/modules/mapas/infrastructure/persistence/supabase-repositories.ts | Cumple | Contenedores dibujados tienen código correspondiente en el árbol; no se halló contenedor sin código |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Interfaz: backend/src/modules/mapas/interfaces/mapas.controller.ts y frontend/lib/features/mapas/presentation/pages/map_page.dart; Lógica: backend/src/modules/mapas/application/use-cases.ts y frontend/lib/features/mapas/application/load_building_use_case.dart; Persistencia: backend/src/modules/mapas/infrastructure/persistence/supabase-repositories.ts y frontend/lib/features/mapas/infrastructure/storage/model_cache.dart | Cumple | El recorrido mapas (controller → use-case → repositorio Supabase) está presente en backend y frontend |
| Arranque documentado con un solo comando | README.md sección Inicio Rápido: prerrequisitos (Node ≥18, Flutter ≥3.19, Supabase) y scripts/dev.sh como Opción A | Cumple | El README declara requisitos previos y ofrece ./scripts/dev.sh como comando unificado de arranque |
| Prueba automatizada del recorrido completo, en verde | docs/aspectos.md: pruebas EC-01..EC-04 marcadas '(pendiente)'; runs_ci: run CI 33357590091 con conclusion 'failure' | No cumple | No existe prueba que ejercite el recorrido completo y el único run de CI de la semana está en rojo |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila EC-01: Pruebas cita frontend/test/features/mapas/load_building_test.dart y backend/test/mapas.e2e-spec.ts, archivos ausentes del árbol | No cumple | Las rutas de pruebas marcadas '(pendiente)' no existen en el repositorio; celda con huecos |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | visible:true, repo AS_202620_ElMapita en ISCOUTB; shortlog con 3 cuentas (RobotDRMX, Rodrigo Vazquez Rico, dgarza2705) | No verificado | No se pudo confirmar que las 3 cuentas correspondan a los 3 integrantes declarados; falta la lista de miembros de la organización |
| Estructura mínima | docs/arc42/arc42-template-EN.md, docs/adr/0001-*.md, docs/c4/C4_L1_Context.md, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Todos los artefactos mínimos existen en las rutas esperadas |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico-propuesto.md: nombre en convención, título enuncia decisión, incluye contexto, alternativas, decisión y consecuencias | Cumple | Un solo ADR, bien formado; no se observaron ediciones posteriores a su creación |
| Registro de uso de IA | docs/ia.md: dos sesiones (2026-08-30 y 2026-08-31) con instrucciones, artefactos, herramientas y rechazo de Hexagonal con motivo | Cumple | El registro documenta usos y decisiones rechazadas con justificación técnica |
| README | README.md: qué es, stack, arquitectura, inicio rápido con prerrequisitos y comandos, verificación y tests | Cumple | Cubre qué es, cómo se arranca y cómo se prueba |
| Pipeline y análisis estático | .github/workflows/ci.yml existe; runs_ci: run 33357590091 conclusion 'failure'; sin evidencia de SonarCloud | No cumple | El pipeline existe pero el run de la semana falló y no hay análisis estático SonarCloud configurado |
| Secretos | envs_versionados: []; coincidencias de grep son tipos password/token en código y badge de ejemplo en backend/README.md:5 | Cumple | No se hallaron credenciales reales ni .env versionado; los hallazgos son falsos positivos |
| Autoría y colaboración | shortlog: RobotDRMX 9, Rodrigo Vazquez Rico 1, dgarza2705 1; un integrante declarado sin commits visibles | No cumple | Un solo autor concentra 9/11 commits y el historial no muestra participación repartida del equipo |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `07b36f40ecd48b3808e183c60595e8243793f215 2026-08-30T23:31:03-05:00 docs: actualizacion de C4, arc42 y creación de pipeline`
- **Veredicto**: con pendientes
- Resumen: Entrega S4 a tiempo (07b36f4, 2026-08-30T23:31:03-05:00, antes del cierre). Documentación C4 y corte vertical presentes, pero el pipeline falla y las pruebas del recorrido completo están pendientes.

Pendientes que siguen abiertos:
- Run de CI en failure (33357590091)
- Pruebas del recorrido completo pendientes y rutas inexistentes en aspectos.md
- Sin SonarCloud configurado
- Autoría concentrada en una cuenta (9/11 commits)

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 1-6: falta contenido completo de docs/arc42/arc42-template-EN.md (secciones 4-6)
- arc42 sección 9: falta texto que cite los ADR
- arc42 sección 10: falta texto para verificar coherencia con escenarios de semana 2
- Glosario sección 12: falta texto del glosario en el archivo arc42
- Identidad: falta lista de miembros de la organización para confirmar pertenencia de los integrantes

## Hallazgos para la planilla

- Run de CI de la semana en failure (33357590091)
- Pruebas del corte vertical pendientes en docs/aspectos.md
- Rutas de pruebas citadas en aspectos.md no existen en el árbol
- Sin evidencia de SonarCloud en el pipeline
- Autoría concentrada en una cuenta (9/11 commits)
- Secciones 4-6, 9, 10 y 12 de arc42 no verificables con la evidencia entregada
