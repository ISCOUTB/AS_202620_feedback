# semana-02-evidencia-s2 · InvenTrack

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `db90ff2` (2026-08-16T21:22:20-05:00) |
| Cierre | 2026-08-17T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | docs/arc42/arc42-template-EN.md contiene 'Requirements Overview', 'Quality Goals' y 'Stakeholders' con tabla de interesados y expectativas (db90ff2). | Cumple | Objetivos redactados como problemas de negocio y no como funcionalidades. |
| arc42 sección 2 con restricciones clasificadas y justificadas | docs/arc42/arc42-template-EN.md incluye tabla de restricciones C1-C7 con tipo, justificación y quién la impone (db90ff2). | Cumple | Clasifica en legal, organizativa y técnica. |
| Restricciones separadas de los requisitos | En sección 2 se explica la diferencia y las restricciones no incluyen funciones del MVP, que están en la sección 1 (db90ff2). | Cumple | No se identificaron restricciones que sean requisitos funcionales. |
| arc42 sección 3 con actores y sistemas externos | docs/arc42/arc42-template-EN.md sección 3 y docs/c4/context.md listan Dueño, Empleado, InvenTrack y Servicio de notificaciones (db90ff2). | Cumple | Coherente con el diagrama C4. |
| Entre 3 y 5 escenarios de calidad redactados | docs/arc42/arc42-template-EN.md sección 10 y docs/utility-tree.md documentan ESC-01 a ESC-05 (db90ff2). | Cumple | Hay 5 escenarios. |
| Cada escenario con sus seis partes y medida numérica | ESC-01 en arc42 sección 10 incluye fuente, estímulo, artefacto, entorno, respuesta y medida '0 casos de stock negativo y 0 de doble descuento en 100 % de prueba con 50 transacciones simultáneas' (db90ff2). | Cumple | Los otros escenarios también tienen medida numérica. |
| Árbol de utilidad que prioriza por impacto y riesgo | docs/utility-tree.md incluye diagrama Mermaid y tabla con prioridad (A/M) por impacto y riesgo para cada escenario (db90ff2). | Cumple | Los escenarios priorizados coinciden con los redactados. |
| C4 de contexto con leyenda y flechas etiquetadas | docs/c4/context.md incluye diagrama Mermaid con leyenda de colores y flechas etiquetadas 'Usa (HTTPS)' y 'Envía alerta (SMTP/API)' (db90ff2). | Cumple | Diagrama en código, renderizable. |
| Escenarios alcanzables desde la fila de su aspecto | docs/aspectos.md enlaza a arc42 y utility-tree para ESC-01 y ESC-02; dos filas recorridas hasta el escenario (db90ff2). | Cumple | Trazabilidad funcionante. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio visible AS_202620_InvenTrack en ISCOUTB; integrantes en historial: Jose Vargas, Josephva24, Esteban Peluffo, Felix Taborda, FlexT21, jxviercarta-a11y (db90ff2). | Cumple | Identidades consolidadas en 4 personas declaradas. |
| Estructura mínima | Árbol contiene README.md, docs/arc42/, docs/c4/, docs/aspectos.md, docs/ia.md, docs/adr/ (db90ff2). | Cumple | El arc42 es un solo archivo con plantilla; se anota la desviación del nombre pero el artefacto está. |
| Qué estado del repositorio se califica | Hash calificado db90ff2 2026-08-16T21:22:20-05:00 es anterior al cierre 2026-08-17T05:00:00Z. | Cumple | Hay commits posteriores registrados en overall. |
| Convenciones de ADR | En db90ff2 docs/adr solo contiene README.md; no hay ADR que validar. | No verificado | Faltan archivos NNNN-titulo.md para comprobar convención. |
| La tabla de aspectos | docs/aspectos.md tiene fila con ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia (db90ff2). | Cumple | Celdas pendientes marcadas para ADR/código/pruebas, acorde a la semana. |
| Registro de uso de IA | docs/ia.md registra herramientas, fechas, propósitos y lo rechazado con motivo (db90ff2). | Cumple | Incluye criterio del equipo. |
| README | README.md describe el sistema, estructura, documentación y equipo (db90ff2). | Cumple | Aún no hay código ni comando de arranque que documentar. |
| Pipeline y análisis estático | No hay runs_ci citables y en db90ff2 no aparece .github/workflows ni sonar-project.properties. | No verificado | Faltan workflow y ejecución de CI para verificar. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `ac951e3fc2acf849f2cc89ffb622d392b268672a 2026-09-08T10:11:58-05:00 Update and rename feedback.md to correcciones.md`
- **Veredicto**: con pendientes
- Resumen: A HEAD el proyecto avanzó mucho después del cierre de s2: hay código del corte vertical, ADR-0001 y ADR-0002, pipeline CI, medición del reto y correcciones de documentación. La entrega s2 en db90ff2 cumplía los criterios de la ficha, aunque sin CI ni ADR que verificar.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- La corrección 'Update and rename feedback.md to correcciones.md' (ac951e3, 2026-09-08) es posterior al cierre.
- Se añadieron ADR-0001 y ADR-0002, código, CI y trazabilidad en commits posteriores al cierre (7b0aad5, bcb133d, 8d149c1).
- El commit cf9d7d3 define Flutter como frontend, decisión de stack posterior a la entrega s2.

Pendientes que siguen abiertos:
- No hay runs_ci citables que confirmen la ejecución del pipeline a HEAD.
- Faltaba CI/ADR en s2; a HEAD ya existen, pero la evidencia de ejecución no está registrada.

## Recuento y nota sugerida

9 de 9 criterios Cumple.

## No verificado / pendientes

- Convenciones de ADR: faltan ADR en el commit calificado.
- Pipeline y análisis estático: faltan workflow y runs de CI en el commit calificado.

## Hallazgos para la planilla

- El arc42 está en un solo archivo de plantilla en lugar de archivos por sección (01*, 02*, 03*, 10*).
- No hay ADR en el estado calificado, aunque a HEAD ya existen 0001 y 0002.
- No hay evidencia de pipeline/CI en el estado calificado; a HEAD existe .github/workflows pero sin runs_ci.
- Hay commits posteriores al cierre de s2 que desarrollan código, ADR, CI y correcciones (7b0aad5, cf9d7d3, ac951e3).
- La autoría está repartida, con múltiples identidades de correo que se consolidan en 4 personas.
- Commits posteriores al cierre (no calificados): ac951e3 2026-09-08T10:11:58-05:00 Update and rename feedback.md to correcciones.md; c837d7d 2026-09-07T01:12:16-05:00 datalle; cf9d7d3 2026-09-07T00:59:16-05:00 docs: definir Flutter como frontend; 3defc32 2026-09-07T00:59:16-05:00 Pequenos detalles; 2988b03 2026-09-06T23:35:40-05:00 docs: remover marcadores de texto residuales en el README
