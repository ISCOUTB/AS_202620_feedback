# semana-04-evidencia-s4 · ElMapita

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `8e30f61` (2026-08-22T16:12:55-06:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md presente, contenido truncado en la evidencia | No verificado | No se pudo comprobar secciones 4-6 ni ausencia de texto de plantilla |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se observa sección 9 en el fragmento de arc42-template-EN.md | No verificado | Se requiere archivo completo para verificar enlace a docs/adr/0001 |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se observa sección 10 en el fragmento | No verificado | Falta confirmar coherencia con escenarios EC-01 a EC-04 |
| Glosario iniciado con términos del dominio | No se observa sección 12 en el fragmento | No verificado | No se puede confirmar glosario |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/C4_Contexto.png existe, no hay archivo de nivel 2 | No cumple | Falta C4 nivel 2 |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No existe C4 nivel 2 | No cumple | Sin nivel 2 no hay límites que contrastar |
| Corte vertical que atraviesa interfaz, lógica y persistencia | frontend/lib/features/mapas/presentation/pages/map_page.dart (interfaz), frontend/lib/features/mapas/application/load_building_use_case.dart (lógica), backend/src/modules/mapas/infrastructure/persistence/supabase-repositories.ts (persistencia) | Cumple | Se identifican las tres capas en el árbol; falta confirmar conexión real |
| Arranque documentado con un solo comando | README.md sección Inicio Rápido, comando ./scripts/dev.sh | Cumple | Cumple con script unificado |
| Prueba automatizada del recorrido completo, en verde | backend/test/app.e2e-spec.ts y frontend/test/widget_test.dart existen, sin URL de run | No verificado | Falta evidencia de ejecución en CI |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 con celdas ADR, Código, Pruebas en 'Pendiente' | No cumple | Fila incompleta y enlace C4 roto |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Autores listados: RobotDRMX, Rodrigo Vazquez Rico; declarados: Angel, Diego, Rodrigo | No cumple | No se puede confirmar identidad de RobotDRMX; faltan Angel y Diego |
| Estructura mínima | Rutas docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Estructura conforme |
| Estado del repositorio que se califica | Hash 8e30f61 fecha 2026-08-22T16:12:55-06:00 anterior al cierre | Cumple | Commit vigente correcto |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico-propuesto.md con nombre correcto | Cumple | Cumple convención |
| Tabla de aspectos | docs/aspectos.md fila A-01 con celdas pendientes y enlace C4 roto | No cumple | Fila no defendible |
| Registro de uso de IA | docs/ia.md vacío | No cumple | Sin registros |
| README | README.md incluye arranque pero no se observa sección de pruebas en el fragmento | No verificado | Falta confirmar instrucciones de prueba |
| Pipeline y análisis estático | No existe .github/workflows en el árbol | No cumple | Sin pipeline |

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 4-6, 9, 10 y 12
- Prueba automatizada en verde (sin URL de run)
- Instrucciones de prueba en README

## Hallazgos para la planilla

- Falta C4 nivel 2
- Fila de aspectos incompleta con celdas Pendiente
- docs/ia.md vacío
- Sin pipeline de CI
- Autores no consolidados: solo dos identidades, una desconocida
- Arc42 secciones 4-6, 9, 10 y 12 no verificables por truncamiento
