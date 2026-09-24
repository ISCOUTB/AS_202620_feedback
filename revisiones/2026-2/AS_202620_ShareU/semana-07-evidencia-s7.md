# Semana 07 · Evidencia S7 · ShareU

> Revisión definitiva auditada localmente. Se corrigieron el estado elegible y la correspondencia contrato–API frente al informe automático.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `29184bc` en `origin/master` (2026-09-20T23:34:09-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Contrato ejecutable versionado | El repositorio contiene un contrato OpenAPI versionado. | Cumple | Archivo estructurado, no prosa. |
| Rutas y esquemas de datos | El contrato declara `/health`, `/busqueda/ping`, `/busqueda/documentos` y sus respuestas. | Cumple | Las operaciones son concretas. |
| Correspondencia contrato–API | `main.py:35-36` implementa `/health`; el router de búsqueda implementa `/busqueda/ping` y `/busqueda/documentos`. | Cumple | El cotejo directo coincide con el contrato. |
| Versión e historial | La versión y la incorporación del contrato son trazables en Git. | Cumple | Estado elegible identificado. |
| Prueba de contrato presente | No existe `tests/test_contrato.py` ni otra prueba automática equivalente. | No cumple | La referencia posterior en arc42 apunta a un archivo inexistente. |
| Pipeline ejecuta la prueba | El workflow ejecuta pruebas, pero no una prueba contractual. | No cumple | Un pipeline verde no acredita esta fila sin la comprobación específica. |
| Falla ante cambio incompatible | No se encontró run rojo ni salida versionada causada por una incompatibilidad deliberada del contrato. | No cumple | Falta evidencia reproducible del fallo esperado. |
| ADR de integración ligado a escenario | `docs/adr/` documenta la decisión de integración, alternativa y consecuencias. | Cumple | La decisión está enlazada con el escenario. |
| arc42 sección 6 | La sección 6 describe los flujos de búsqueda y sus participantes. | Cumple | Incluye recorrido principal y manejo de error. |
| C4 nivel 2 etiquetado | El C4 no rotula todas las relaciones con protocolo y formato. | No cumple | La exigencia aplica a cada flecha. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia u observación |
|---|---|---|
| Repositorio público con nombre de convención | Cumple | Clon público `ISCOUTB/AS_202620_ShareU`. |
| Estructura mínima | No cumple | Aspectos e IA están en subdirectorios (`docs/aspectos/aspectos.md`, `docs/ia/ia.md`) y no en las rutas contractuales. |
| Estado calificado identificable | Cumple | `origin/master`, `29184bc`, fecha y cierre consignados. |
| Nombres de ADR | No cumple | Un PDF en `docs/adr/` rompe la convención exclusiva de Markdown numerado. |
| ADR aceptados sin reescribir | Cumple | Las decisiones Markdown conservan historial. |
| `docs/ia.md` al día | Cumple | El contenido S7 existe, aunque en una ruta no convencional. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | No se acreditó scanner ni Quality Gate de SonarCloud. |
| Sin credenciales expuestas | Cumple | No se hallaron credenciales reales versionadas. |
| Contribución de todo el equipo | Cumple | El historial permite identificar aportes de todos los integrantes. |

## Estado global del proyecto

La punta actual incorpora cambios posteriores al cierre solo en documentación. Esa versión afirma una prueba contractual que no existe en el árbol, por lo que no corrige las no conformidades S7. La correspondencia contrato–API sí es verificable por cotejo directo.

## Recuento y nota sugerida

**6 de 10 criterios Cumple.**

**Nota sugerida (propuesta al docente; la nota final se fija en Moodle): 3.4 = 1 + 4 × (6/10).**
