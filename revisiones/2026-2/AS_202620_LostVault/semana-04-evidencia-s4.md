# semana-04-evidencia-s4 · LostVault

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `952af8f` (2026-08-30T22:13:14-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/01_objetivos.md a 06_vista_runtime.md con contenido propio de LostVault | Cumple | Sin rastros de plantilla; secciones 5 y 6 descomponen módulos y describen escenario de ejecución |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09_decisiones.md enlaza a docs/adr/0001-estilo-arquitectonico.md | Cumple | El ADR 0001 existe y está citado con su estado |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10_requisitos_calidad.md con árbol de utilidad y 4 escenarios medibles | Cumple | Escenarios 1-4 coherentes con AS-01 a AS-04 y con el ADR 0001 |
| Glosario iniciado con términos del dominio | docs/arc42/glosario.md con términos propios del sistema | Cumple | Incluye LostVault, módulos, corte vertical, escenarios de calidad y ADR |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/contexto.mmd, c4_contexto.png y C4 nivel 2.jpg presentes | No verificado | El nivel 2 es solo imagen JPG; la coherencia entre niveles no es verificable sin inspección visual |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/C4 nivel 2.jpg sin contenido inspeccionable en la evidencia | No verificado | Haría falta el diagrama como código o inspección de la imagen para contrastar con lib/features/ |
| Corte vertical que atraviesa interfaz, lógica y persistencia | lib/main.dart → lib/features/claims/application/claim_object_use_case.dart → adaptadores infrastructure/ | Cumple | Recorrido documentado en README y todos los archivos citados existen en el árbol |
| Arranque documentado con un solo comando | README.md sección 'Ejecutar el corte vertical' con 'flutter run -d chrome' | No verificado | Comando documentado con requisitos previos, pero no ejecutado en la revisión |
| Prueba automatizada del recorrido completo, en verde | test/widget_test.dart y test/claim_object_use_case_test.dart; run Flutter checks 33353142312 success | Cumple | CI ejecutó flutter test en verde el 2026-08-31T03:13:20Z, justo tras el commit calificado |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila AS-03 con celdas verificadas hasta Pruebas | Cumple | Rutas a escenario 3, ADR 0001, código del corte y los tres tests existen y son navegables |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_LostVault público; historial con 4 identidades consolidadas | Cumple | Roy Gonzalez, Jose Faustino España, Shamara Llorente y weller-rar presentes en el historial |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md presentes | Cumple | Estructura conforme al contrato |
| Versionado (estado que se califica) | 952af8f 2026-08-30T22:13:14-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin commits posteriores al cierre; diff_desde_cierre vacío |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Nombre y formato correctos; un solo ADR sin reescrituras |
| Tabla de aspectos | docs/aspectos.md con fila AS-03 completa hasta Pruebas | Cumple | Celdas navegables verificadas hasta su destino |
| Registro de uso de IA | docs/ia.md con registros S1-S3 y columna de rechazos con motivo | Cumple | Incluye herramienta, aceptado y rechazado; crece a lo largo del semestre |
| README | README.md con descripción, estructura, arranque, pruebas y requisitos previos | Cumple | Documenta flutter run -d chrome y flutter test |
| Pipeline y análisis estático | .github/workflows/flutter.yml ejecuta flutter analyze y flutter test; runs en verde | No cumple | Falta la integración con SonarCloud que exige el contrato; no hay configuración en el repositorio |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `952af8f4f2230a4cd2258d361629579da8a6ade6 2026-08-30T22:13:14-05:00 Se realiza el corte vertical y la fila de aspectos`
- **Veredicto**: al dia
- Resumen: Proyecto a HEAD (952af8f) cumple la entrega de la semana 4: 7/10 criterios de ficha verificados y 7/8 de la transversal; los no verificados son limitaciones de revisión (imagen JPG del C4 nivel 2, arranque no ejecutado). Sin commits posteriores al cierre.

Pendientes que siguen abiertos:
- Integración con SonarCloud pendiente según contrato
- C4 nivel 2 sin código fuente que permita verificar coherencia y límites
- Arranque documentado pero sin verificación ejecutada
- Cortes ejecutables para AS-01, AS-02 y AS-04 pendientes según docs/aspectos.md

## Recuento y nota sugerida

7 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- C4 nivel 2 coherencia entre niveles: imagen JPG no inspeccionable; haría falta el diagrama como código o inspección visual
- Límites del C4 nivel 2 vs estructura de código: imagen JPG no inspeccionable; haría falta el diagrama como código
- Arranque con un solo comando: no ejecutado; comando declarado: flutter run -d chrome

## Hallazgos para la planilla

- El C4 nivel 2 está solo como imagen JPG, sin código fuente, lo que impide verificar coherencia y correspondencia con el código
- El arranque documentado (flutter run -d chrome) no fue ejecutado en la revisión
- El pipeline no incluye SonarCloud, requisito del contrato
- El C4 nivel 1 sí está como código (contexto.mmd), el nivel 2 no
- La fila AS-03 de aspectos.md está completa y trazable hasta pruebas
