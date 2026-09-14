# semana-06-evidencia-s6 · LaPlacita

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `2c0eb01` en `origin/master` (2026-09-13T21:28:00-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/dominio/mapa-de-contextos.md (diagrama Mermaid y tabla de relaciones Customer/Supplier, OHS) | Cumple | Incluye SK tiendaId declarado en ADR-0005 y aspectos.md. |
| Tabla módulo a datos con dueño único por entidad | docs/dominio/propiedad-de-datos.md (tabla Contexto/Almacén/Datos propios/Acceso externo) | Cumple | Cada contexto declara un solo dueño por almacén. |
| La tabla cubre las entidades que existen en el código | docs/dominio/auditoria-modularidad.md pasos 1-2 (sin SQL; almacenes Map cubiertos) | Cumple | Cubre productos, pedidosPorTienda, pagosConfirmados, notificacionesEnviadas. |
| Violaciones de propiedad de datos detectadas sobre el código actual | docs/dominio/auditoria-modularidad.md (V-01 a V-06 con ubicaciones) | Cumple | V-01 y V-03 corregidos el 13/09; V-02/V-04/V-05/V-06 pendientes. |
| Plan de corrección por violación | docs/dominio/auditoria-modularidad.md y propiedad-de-datos.md (deuda con prioridades P1/P2/P3) | Cumple | Cada violación tiene acción concreta y prioridad. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | No hay docs/arc42/08*; el extracto de arc42-template-EN.md no muestra §8 | No verificado | ADR-0005 afirma que se añadió §8, pero no se pudo comprobar en el commit 2c0eb01. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/componentes.md y docs/adr/0005-reajuste-contextos-propiedad.md | Cumple | ADR-0005 documenta reajuste de precisión; contenedores intactos. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md (Mapa Aspecto -> Contexto) y docs/dominio/auditoria-modularidad.md | Cumple | Los 6 aspectos mapean a contextos; sin huérfanos. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo visible ISCOUTB/AS_202620_LaPlacita; autores consolidados: Jorge M. Castillo, samulssl, Isaza927/isaza927, matbuendia | Cumple | 4 integrantes con commits en el historial. |
| Estructura mínima | Árbol con docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md | Cumple | arc42 en un solo archivo plantilla (desviación menor, no ausencia). |
| Estado del repositorio que se califica | Hash 2c0eb01 2026-09-13T21:28:00-05:00 en origin/master, anterior al cierre | Cumple | Sin commits posteriores al cierre. |
| Convenciones de ADR | docs/adr/0001-0005 con nombres kebab-case y numeración de 4 dígitos | Cumple | Títulos enuncian la decisión; ADR-0002 ratifica sin reescribir el 0001. |
| Tabla de aspectos | docs/aspectos.md con filas A-01 a A-06 y columnas trazables | Cumple | Incluye columna extra 'Escenarios' y mapa aspecto->contexto. |
| Registro de uso de IA | docs/ia.md con bitácora y columna Rechazado; log de commits del archivo | Cumple | Rechazos con motivo técnico; el archivo crece a lo largo del semestre. |
| README | README.md con descripción, cómo ejecutar y cómo probar | Cumple | Incluye guía paso a paso y enlaces a documentación. |
| Pipeline y análisis estático | .github/workflows/ci.yml y sonar-project.properties existen, pero sin runs_ci | No verificado | Comando: curl -s 'https://api.github.com/repos/ISCOUTB/AS_202620_LaPlacita/actions/runs?per_page=5'; SonarCloud pendiente de token. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `2c0eb0127e0405a61b482c388677b319e219d741 2026-09-13T21:28:00-05:00 se actualiza propiedad-de-datos post V-01/V-03`
- **Veredicto**: con pendientes
- Resumen: La entrega S6 cumple 6/8 criterios de la ficha y 7/8 transversales; quedan sin verificar arc42 §8 y la ejecución de CI, y persiste el pendiente de SonarCloud desde S4.

Pendientes que siguen abiertos:
- Configurar SONAR_TOKEN y projectKey para activar SonarCloud (desde S4)
- Verificar que arc42 §8 contenga lenguaje ubicuo y mapa de contextos
- Evidenciar la ejecución del pipeline CI en el commit actual
- Deuda de propiedad V-02/V-04/V-05/V-06 planificada para Corte 2

## Recuento y nota sugerida

7 de 8 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.5 = 1 + 4 × (7/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 sección 8 con lenguaje ubicuo y mapa de contextos
- Pipeline y análisis estático (ejecución de CI)

## Hallazgos para la planilla

- No se localizó docs/arc42/08*; la sección 8 de arc42 no es verificable en el commit 2c0eb01.
- Sin runs de CI en la evidencia; la ejecución del pipeline no se pudo comprobar.
- SonarCloud sigue pendiente de configuración (token/projectKey) desde S4 según README y ADR-0003.
- V-01 y V-03 fueron corregidos el 13/09; V-02/V-04/V-05/V-06 quedan como deuda planificada para Corte 2.
- Identidades consolidadas: 4 integrantes con actividad en el historial; sin commits post-cierre.
