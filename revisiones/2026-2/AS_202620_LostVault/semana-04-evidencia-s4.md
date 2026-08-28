# semana-04-evidencia-s4 · LostVault

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `4e20446` (2026-08-24T17:41:15-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/ solo contiene 01,02,03,04,10; faltan 05 y 06 | No cumple | Secciones 5 y 6 ausentes |
| arc42 sección 9 al día y enlazada con los ADR existentes | No existe docs/arc42/09_* | No cumple | Sección 9 no encontrada |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10_requisitos_calidad.md con escenarios 1-4 | Cumple | Coherente con aspectos y ADR 0001 |
| Glosario iniciado con términos del dominio | No existe docs/arc42/12_* | No cumple | Sección 12 ausente |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/ solo tiene contexto.mmd y c4_contexto.png (nivel 1) | No cumple | Falta nivel 2 |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin diagrama de nivel 2 | No cumple | No hay contenedores de nivel 2 que contrastar |
| Corte vertical que atraviesa interfaz, lógica y persistencia | lib/main.dart (interfaz), lib/features/objects/application/object_service.dart (lógica), lib/features/objects/infrastructure/in_memory_object_service.dart (persistencia) | Cumple | Tres capas presentes en el árbol |
| Arranque documentado con un solo comando | README.md declara requisitos y comando 'flutter run' | Cumple | Comando único documentado |
| Prueba automatizada del recorrido completo, en verde | test/architecture_structure_test.dart y test/widget_test.dart existen, pero sin URL de run | No verificado | Falta evidencia de ejecución en CI |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md tiene columnas ID, Aspecto, Prioridad, Justificación, Tensión, Escenario, Medida, Decisión; faltan Requisito, C4, ADR, Código, Pruebas, Evidencia | No cumple | Estructura de tabla no coincide con la requerida |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_LostVault visible, autores consolidados: Roy Gonzalez, Jose Faustino, Shamara, Kiefer (4) | Cumple | Coincide con integrantes declarados |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Estructura completa |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md sin sección de trazabilidad (requisito, C4, commit, pruebas) | No cumple | Falta trazabilidad exigida |
| Tabla de aspectos | docs/aspectos.md no usa las 8 columnas requeridas | No cumple | Columnas incorrectas |
| Registro de uso de IA | docs/ia.md con registros S1-S3, incluye aceptado/rechazado | Cumple | Registro presente |
| README | README.md con requisitos, 'flutter run' y 'flutter test' | Cumple | Arranque y pruebas documentados |
| Pipeline, análisis estático y secretos | .github/workflows/flutter.yml ejecuta analyze y test; sin secretos encontrados; sin URL de run | No verificado | Configuración presente, ejecución no verificada |
| Autoría y colaboración | 4 autores consolidados con commits: Roy 26, Jose 17, Shamara 1, Kiefer 1 | Cumple | Todos contribuyen, distribución desigual |

## Recuento y nota sugerida

3 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.2 = 1 + 4 × (3/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Prueba automatizada en verde: falta URL de run de GitHub Actions
- Pipeline: falta URL de run que muestre analyze y test en verde

## Hallazgos para la planilla

- Faltan secciones arc42 5, 6, 9 y 12
- No hay diagrama C4 nivel 2
- Tabla de aspectos no sigue las columnas requeridas
- ADR sin trazabilidad completa
- Sin evidencia de ejecución de CI en verde
