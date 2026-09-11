# semana-05-corte1 · LostVault

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `c0c17c1` en `origin/main` (2026-09-07T16:46:16-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/main c0c17c1 2026-09-07T16:46:16-05:00, anterior al cierre 2026-09-10T17:00:00Z | Cumple | Rama principal declarada origin/main; sin commits posteriores al cierre. |
| correcciones.md existe en la raíz del estado calificado | git ls-tree del hash c0c17c1 no incluye correcciones.md; solo REVISION_CORREGIDA.md | No cumple | El archivo REVISION_CORREGIDA.md no sustituye a correcciones.md. |
| Correcciones trazables y contrastadas | No existe correcciones.md en el estado calificado; REVISION_CORREGIDA.md no es el archivo exigido | No cumple | No hay índice de verificación de hallazgos S1-S4. |
| S1 al día: equipo, problema y repositorio | README.md, docs/ficha_problema.md; autores: Roy Gonzalez, Jose Faustino España, Kiefer Monterroza, Shamara Llorente | Cumple | Los 4 integrantes declarados aparecen en el historial. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/10_requisitos_calidad.md con 4 escenarios medibles; docs/arc42/02_restricciones.md | Cumple | Escenarios con medidas numéricas y restricciones documentadas. |
| S3 al día: estrategia de solución y decisiones | docs/arc42/04_estilo_arquitectonico.md; docs/adr/0001-estilo-arquitectonico.md | Cumple | ADR con contexto, alternativas, decisión y consecuencias. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/01-06,09,10 y glosario; docs/c4/contexto.mmd, c4_contexto.png, C4 nivel 2.jpg; lib/features/claims | Cumple | arc42 parcial pero suficiente para la línea base; C4 contexto y nivel 2 presentes. |
| Corte vertical reproducible y coherente con la arquitectura | README.md secciones Ejecutar y Analizar; test/claim_object_use_case_test.dart, widget_test.dart, architecture_structure_test.dart | Cumple | README documenta arranque y pruebas; flujo vertical coincide con la arquitectura. |
| Pipeline y pruebas respaldan el estado calificado | Run Flutter checks 34164327182 success 2026-09-07T21:46:19Z; Run Build 34164327299 success | Cumple | Run asociado al hash calificado con conclusión success. |
| Trazabilidad consolidada navegable | docs/aspectos.md fila AS-03 sin columna C4; cadena aspecto→requisito→C4→ADR→código→pruebas incompleta | No cumple | Falta enlazar C4 en la fila AS-03 de docs/aspectos.md. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; se entrega en Moodle | No verificado | Requiere verificación en Moodle. |
| Sustentación del corte | Sesión de sustentación pendiente | No verificado | Depende de la sesión oral. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima | README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md presentes | Cumple | Hay archivos residuales sin documentar: ejecutable, front_end, lib/search/domain/entities/lost_object.dart. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md con nombre válido y contenido completo | Cumple | Un solo ADR; no hay reescrituras. |
| Tabla de aspectos | docs/aspectos.md sin columna C4 ni Requisito explícita | No cumple | La fila AS-03 no enlaza a ningún diagrama C4. |
| Registro de uso de IA | docs/ia.md con registros S1-S3, aceptados y rechazados | Cumple | Crece con el semestre; último commit 2026-08-24. |
| README | README.md con qué es, arranque y pruebas | Cumple | Incluye recorrido manual del corte vertical. |
| Pipeline y análisis estático | .github/workflows/flutter.yml y build.yml; runs success 34164327182 y 34164327299 | Cumple | SonarQube scan configurado con sonar-project.properties. |
| Secretos | git grep sin coincidencias; sin .env versionado | Cumple | Repositorio público sin credenciales. |
| Autoría y colaboración | shortlog: Roy Gonzalez 31, Jose Faustino España 19, Kiefer Monterroza 6, Shamara Llorente 4 | Cumple | Actividad repartida entre los 4 integrantes. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `c0c17c1e9c3387ac915767cd706e8b785a3deadf 2026-09-07T16:46:16-05:00 Change build target from Windows to Web`
- **Veredicto**: con pendientes
- Resumen: Estado calificado c0c17c1 (2026-09-07) anterior al cierre; pipeline en verde; faltan correcciones.md y trazabilidad C4.

Pendientes que siguen abiertos:
- Crear correcciones.md en la raíz
- Completar trazabilidad con C4 en docs/aspectos.md
- Limpiar archivos residuales

## Recuento y nota sugerida

7 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.3 = 1 + 4 × (7/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF adjunto en Moodle (no disponible en el repositorio).
- Sustentación del corte (sesión oral).
- Contenido de REVISION_CORREGIDA.md (no incluido en la evidencia).

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado; solo existe REVISION_CORREGIDA.md.
- docs/aspectos.md no incluye el eslabón C4 en la trazabilidad de AS-03.
- Archivos residuales sin documentar: ejecutable, front_end, lib/search/domain/entities/lost_object.dart.
- Runs de CI Build fallaron en commits previos, pero el run del hash calificado es success.
