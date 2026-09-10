# semana-05-corte1 · PideUtb

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `1636f20` en `origin/master` (2026-08-30T22:17:18-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama origin/master, hash 1636f20, fecha 2026-08-30T22:17:18-05:00 (anterior al cierre 2026-09-07T05:00:00Z) | Cumple | El estado calificado es identificable y anterior al cierre. |
| correcciones.md existe en la raíz del estado calificado | árbol del hash 1636f20 no incluye correcciones.md; solo aparece en commits posteriores (f9a3304 2026-09-07T16:12:06-05:00) | No cumple | El archivo fue añadido después del cierre, no en el estado calificado. |
| Correcciones trazables y contrastadas | sin correcciones.md en el hash calificado, no hay índice de correcciones; los commits posteriores (f9a3304, f9a903f) no son parte del estado evaluado | No cumple | No se puede contrastar ninguna corrección en el estado calificado. |
| S1 al día: equipo, problema y repositorio | README.md describe el problema y la arquitectura; autores: daniarriet, Santiago Cuesta, ruddy2000utb-droid, Santiago-C0 (consolidado a 3 identidades) | Cumple | El repositorio es público y los integrantes aparecen en el historial. |
| S2 al día: escenarios de calidad y restricciones | docs/aspectos.md incluye escenarios ESC-01 a ESC-05 y atributos de calidad (usabilidad, confiabilidad, seguridad, disponibilidad, rendimiento) | Cumple | Los escenarios están documentados y enlazados a arc42. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-estilo-arquitectonico.md (aceptada 23/08/2026) y docs/comparativa-arquitectura.md con matriz comparativa | Cumple | La decisión de monolito modular está documentada con alternativas y consecuencias. |
| S4 al día: arc42, C4 y corte vertical | arc42.md (secciones 4, 6, 10.2), README.md describe el corte vertical con flujo pedidos-menu y pruebas en backend/tests/test_pedidos.py | Cumple | El corte vertical es ejecutable y coherente con la arquitectura. |
| Corte vertical reproducible y coherente con la arquitectura | README.md incluye comando único de arranque y pruebas; backend/tests/test_pedidos.py cubre casos exitoso y de error | Cumple | El flujo cruza módulos pedidos y menu según la arquitectura. |
| Pipeline y pruebas respaldan el estado calificado | no se proporcionan runs_ci para el hash 1636f20; solo commits posteriores mencionan CI (c665562, a5fe113) | No verificado | Falta evidencia de un run de CI asociado al estado calificado. |
| Trazabilidad consolidada navegable | docs/aspectos.md tiene filas con huecos (Confiabilidad, Seguridad, Disponibilidad, Rendimiento sin táctica ni prueba) y no hay tabla de trazabilidad completa | No cumple | La tabla de aspectos no está completa hasta la columna 'Prueba' para todos los aspectos. |
| PDF u otro adjunto exigido por el aula | no se dispone del documento entregado en Moodle | No verificado | El PDF no está disponible en el repositorio; depende del aula. |
| Sustentación del corte | no hay sesión de sustentación registrada | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repositorio AS_202620_PideUtb en ISCOUTB, público, con integrantes en historial | Cumple | Nombre y organización correctos. |
| Estructura mínima | falta docs/ia.md en el árbol del hash 1636f20; docs/arc42, docs/adr, docs/c4 y README.md presentes | No cumple | docs/ia.md no existe en el estado calificado. |
| Estado del repositorio calificado | hash 1636f20 en origin/master, anterior al cierre | Cumple | Se usó la rama principal declarada. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md con nombre correcto y contenido completo | Cumple | Un ADR, aceptado, sin reescrituras posteriores. |
| Tabla de aspectos | docs/aspectos.md tiene filas con huecos (Confiabilidad, Seguridad, Disponibilidad, Rendimiento sin táctica ni prueba) | No cumple | La trazabilidad no está completa para todos los aspectos. |
| Registro de uso de IA | docs/ia.md no existe en el hash 1636f20; solo aparece en commits posteriores (f9a3304) | No cumple | Falta el registro de IA en el estado calificado. |
| README | README.md incluye qué es, cómo arrancar con un comando y cómo probar | Cumple | Cumple con los requisitos de reproducibilidad. |
| Pipeline y análisis estático | no hay runs_ci para el hash calificado; solo commits posteriores mencionan CI | No verificado | Falta evidencia de ejecución de CI. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `bbefae828185e9baa4df757ea073cbe84539cd3f 2026-09-08T10:37:21-05:00 Actualizar las referencias restantes al run de CI`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene una arquitectura bien documentada y un corte vertical funcional, pero la entrega del corte carece de correcciones.md y docs/ia.md, y la trazabilidad está incompleta.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- correcciones.md añadido en commit f9a3304 (2026-09-07T16:12:06-05:00), posterior al cierre
- docs/ia.md añadido en commit f9a3304 (2026-09-07T16:12:06-05:00), posterior al cierre
- CI configurado en commits c665562 y a5fe113 (2026-09-07), posterior al cierre

Pendientes que siguen abiertos:
- correcciones.md no estaba en el estado calificado
- docs/ia.md no estaba en el estado calificado
- Tabla de aspectos incompleta en el estado calificado
- Sin evidencia de CI en el estado calificado

## Recuento y nota sugerida

6 de 12 criterios Cumple.

## No verificado / pendientes

- Pipeline y pruebas respaldan el estado calificado
- PDF u otro adjunto exigido por el aula
- Sustentación del corte
- Pipeline y análisis estático (transversal)

## Hallazgos para la planilla

- correcciones.md no existe en el estado calificado (hash 1636f20), solo en commits posteriores.
- docs/ia.md no existe en el estado calificado.
- La tabla de aspectos tiene huecos en varias filas.
- No hay evidencia de CI para el estado calificado.
- Se versionó el entorno virtual .venv-1 en el repositorio.
- El historial muestra commits posteriores al cierre que corrigen la entrega.
- Commits posteriores al cierre (no calificados): bbefae8 2026-09-08T10:37:21-05:00 Actualizar las referencias restantes al run de CI; ca2c641 2026-09-08T10:33:54-05:00 Actualizar la referencia del run de CI tras la reescritura del historial; 51a8122 2026-09-08T10:04:11-05:00 Anadir .mailmap para unificar la identidad de Santiago-C0; 2dbc8a1 2026-09-08T09:54:45-05:00 Anadir .mailmap para unificar la identidad de Santiago Cuesta; c665562 2026-09-07T16:55:42-05:00 Instalar dependencias en CI desde un lock con versiones exactas y hashes
