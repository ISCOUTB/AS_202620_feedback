# Evidencia S6 · DinamikUTB · rectificación aprobada

Sincronización: 19 de octubre de 2026. Se reemplaza la evaluación fragmentaria anterior con la revisión aprobada por el docente, sobre la misma evidencia de cierre.

| Campo | Valor |
|---|---|
| Repositorio | [DinamikUTB](https://github.com/ISCOUTB/AS_202620_DinamikUTB) |
| Estado de cierre | `265e652bb3c34c6b90d6d8c1e70db4d75e20a18e` · origin/master · 2026-09-13T23:29:49-05:00 |
| Límite exclusivo | 2026-09-14T05:00:00Z |
| Base S5 | `72bfc7e206eac4147dd244c03fa09b4b32b9a7e7` |

## Matriz de la ficha

| Criterio | Estado | Evidencia y fundamento |
|---|---|---|
| Mapa de contextos con relaciones tipificadas | Cumple | §8.2 contiene diagrama y tabla de núcleo compartido, cliente/proveedor y justificación de ACL no aplicable. [Sección 8 completa](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/265e652bb3c34c6b90d6d8c1e70db4d75e20a18e/docs/arc42/08-cross-cutting-concepts.md#L15-L43). |
| Tabla módulo a datos con dueño único por entidad | Cumple | §8.4 asigna Requisito y Estudiante a sus módulos; distingue contextos diseñados sin entidad implementada. [Sección 8 completa](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/265e652bb3c34c6b90d6d8c1e70db4d75e20a18e/docs/arc42/08-cross-cutting-concepts.md#L55-L65). |
| La tabla cubre las entidades que existen en el código | Cumple | Requisito y Estudiante corresponden a backend/app/requisitos/models.py y backend/app/estudiantes/models.py; los demás módulos siguen como diseño. [Sección 8 completa](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/265e652bb3c34c6b90d6d8c1e70db4d75e20a18e/docs/arc42/08-cross-cutting-concepts.md#L55-L65). |
| Violaciones de propiedad detectadas sobre el código actual | Cumple | §8.5 registra comando, resultados y clasificación: requisitos/service.py escribe su entidad; seed.py es carga de desarrollo, no un flujo de negocio de otro módulo. [Sección 8 completa](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/265e652bb3c34c6b90d6d8c1e70db4d75e20a18e/docs/arc42/08-cross-cutting-concepts.md#L67-L87). |
| Plan de corrección por violación | Cumple | §8.5 justifica ausencia de violaciones y fija plan preventivo para consultas entre módulos y repetición del barrido. [Sección 8 completa](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/265e652bb3c34c6b90d6d8c1e70db4d75e20a18e/docs/arc42/08-cross-cutting-concepts.md#L89-L95). |
| arc42 sección 8 con lenguaje ubicuo y mapa | Cumple | §8.1 y §8.2 están completos; la revisión inicial solo dispuso de un fragmento. [Sección 8 completa](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/265e652bb3c34c6b90d6d8c1e70db4d75e20a18e/docs/arc42/08-cross-cutting-concepts.md#L3-L43). |
| C4 nivel 3 y ADR si cambiaron límites desde el primer corte | Cumple | §8.6 justifica que no cambiaron los cinco límites frente a S5 72bfc7e. Incorporar código dentro de esos límites no exige un ADR nuevo de reajuste. [Sección 8 completa](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/265e652bb3c34c6b90d6d8c1e70db4d75e20a18e/docs/arc42/08-cross-cutting-concepts.md#L97-L99). |
| Aspectos relacionables con los contextos del mapa | Cumple | §8.7 relaciona cinco aspectos, identifica A-04 transversal y declara sin decisión A-03/A-08. Se acepta la correspondencia explícita y honesta aprobada en la apelación, no se declara resuelto todo el diseño. [Sección 8 completa](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/265e652bb3c34c6b90d6d8c1e70db4d75e20a18e/docs/arc42/08-cross-cutting-concepts.md#L100-L113). |

## Alcance, transversal y seguimiento

El [registro IA](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/265e652bb3c34c6b90d6d8c1e70db4d75e20a18e/docs/ia.md) ya contenía la entrada del 13 de septiembre sobre esta revisión. No se acredita trabajo tardío. La rectificación resuelve los ocho criterios semanales; no certifica ejecución en producción, seguridad completa ni Quality Gate. El contraste de límites se documenta en la [comparación S5–S6](https://github.com/ISCOUTB/AS_202620_DinamikUTB/compare/72bfc7e206eac4147dd244c03fa09b4b32b9a7e7...265e652bb3c34c6b90d6d8c1e70db4d75e20a18e). Los modelos [Requisito](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/265e652bb3c34c6b90d6d8c1e70db4d75e20a18e/backend/app/requisitos/models.py#L6-L12) y [Estudiante](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/265e652bb3c34c6b90d6d8c1e70db4d75e20a18e/backend/app/estudiantes/models.py#L6-L12) permiten contrastar cobertura. Los pendientes transversales de CI, identidad e inmutabilidad deben leerse en las revisiones posteriores con su propia fecha. El estado actual del proyecto se registra en [S11](semana-11-evidencia-s11.md) y [S12 preliminar](semana-12-evidencia-s12.md), sin trasladarlo retroactivamente a S6.

## Recuento y nota sugerida

**8 de 8 criterios Cumple. Nota sugerida aprobada: 5.0 = 1 + 4 × (8/8).** Sustituye 0/8 y 1.0 de la lectura parcial. La nota final del curso corresponde al docente.

La [versión histórica anterior](https://github.com/ISCOUTB/AS_202620_feedback/blob/1e097657880c87f72241c7f0fb20690e64b7625a/revisiones/2026-2/AS_202620_DinamikUTB/semana-06-evidencia-s6.md) se conserva en Git; sus afirmaciones de ausencia de contenido quedan superadas por esta rectificación.
