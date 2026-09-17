# semana-06-evidencia-s6 · mapsutb

> Revisión manual de contingencia: `dominio_y_modularidad.md` está en la raíz y no fue incluido por el recolector automático. Se inspeccionó el repositorio público sin ejecutar código. Los hashes y la nota son preliminares, propuesta al docente.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `8aee879` en `origin/master` (2026-09-13T18:14:14-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | revisión manual estática |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | `dominio_y_modularidad.md` presenta Catálogo, Posicionamiento, Ruteo y Tour; el diagrama tipifica las relaciones Ruteo/Tour → Catálogo como customer/supplier de solo lectura. | Cumple | Declara explícitamente que aún no hay ACL porque Google Maps/Geocoding no está integrado. |
| Tabla módulo a datos con dueño único por entidad | Tabla “módulo → datos” de `dominio_y_modularidad.md`: `ZonaRepository` para Zona/Piso/Espacio/Salon y `UbicacionService` para Ubicacion. | Cumple | Los repositorios de Ruteo y Tour se distinguen como pendientes, no como implementados. |
| La tabla cubre las entidades que existen en el código | Árbol de `8aee879`: `lib/models/zona.dart`, `piso.dart`, `espacio.dart`, `salon.dart`, `ubicacion.dart`, `lib/repositories/zona_repository.dart`, `lib/services/ubicacion_service.dart` y `assets/data/zonas.json`. | Cumple | Las entidades y sus dueños están cubiertos por la tabla. |
| No conformidades de propiedad de datos detectadas sobre el código actual | `dominio_y_modularidad.md` NC-01 a NC-04 cita glosario, modelos, C4 y la duplicación de documento dentro de `lib/models/`. | Cumple | Identifica términos inconsistentes, clase inexistente, riesgo de doble escritor y documento duplicado. |
| Plan de corrección por no conformidad | Cada NC incluye acción concreta: corregir glosario, decidir el dueño de Punto de interés, separar `tour.json` y eliminar la copia de arc42. | Cumple | El plan asocia la acción a la ubicación observada. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | `docs/arc42/08_concepts.adoc` permanece como plantilla de arc42, con `<Concepto 1>` y sin mapa de contextos. | No cumple | Se esperaba lenguaje ubicuo y mapa incorporados en §8; no se encontraron. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | `docs/c4/C3.md` enumera componentes futuros, pero no hay ADR S6 que registre el reajuste de límites descrito en `dominio_y_modularidad.md`. | No cumple | Se esperaba ADR de reajuste y contraste explícito frente al estado S5; no se encontró. |
| Aspectos relacionables con los contextos del mapa | `docs/aspectos.md` solo tiene una fila A-01 y no tiene columna de contexto; Catálogo, Posicionamiento, Ruteo y Tour no quedan mapeados de forma escrita. | No cumple | La relación se puede inferir, pero la ficha exige que sea comprobable. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio público `ISCOUTB/AS_202620_mapsutb`, rama `master`. | Cumple | El historial muestra cuatro cuentas; las correspondencias personales las confirma el docente. |
| Estructura mínima | `8aee879` contiene README, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | La documentación usa mayúsculas en algunos archivos C4, observación previa del equipo. |
| Estado calificado identificable | Último commit de `origin/master` anterior al cierre: `8aee879`, 2026-09-13T18:14:14-05:00. | Cumple | No se usaron etiquetas para elegir el estado. |
| Nombres de ADR según convención | ADR `0001` a `0004` usan numeración y kebab-case. | Cumple | Persiste la observación histórica de reescritura de ADR 0001. |
| Tabla de aspectos | `docs/aspectos.md` tiene una sola fila, sin contexto, y declara Código parcial, sin prueba específica ni evidencia CI. | No cumple | No es trazable de punta a punta para los cuatro contextos S6. |
| `docs/ia.md` al día | `docs/ia.md` existe, pero no documenta de forma verificable la elaboración del material S6. | No verificado | Haría falta una entrada con herramienta, uso, validación y decisión de la semana. |
| README utilizable | `README.md` está versionado y describe el proyecto Flutter. | Cumple | No se ejecutaron comandos ni pruebas. |
| Pipeline y análisis estático | Hay `ci.yml` y `sonar-sync-issues.yml`, pero no se encontró scanner, run citable del hash ni URL pública de SonarCloud/Quality Gate. | No cumple | Se esperaba la triple evidencia pública requerida desde S6. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `8aee879`, igual al estado calificado.
- **Veredicto**: con pendientes.
- Resumen: el documento de raíz ofrece una auditoría S6 concreta y verificable, pero arc42 §8 sigue siendo una plantilla, el C4/ADR no registra el reajuste y no hay evidencia pública de SonarCloud.

Pendientes que siguen abiertos:

- Trasladar el mapa y lenguaje ubicuo a arc42 §8.
- Registrar en ADR el reajuste de límites y conectar C3 con ese cambio.
- Mapear las filas de aspectos a los contextos y completar pruebas/evidencia.
- Configurar scanner SonarCloud, run y Quality Gate público.

## Recuento y nota sugerida

5 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.5 = 1 + 4 × (5/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- No se ejecutaron Flutter ni pruebas; se revisaron únicamente archivos versionados.
- No se verificó un run público ni análisis SonarCloud con Quality Gate.

## Hallazgos para la planilla

- La evidencia S6 existe en `dominio_y_modularidad.md` en la raíz y fue omitida por el recolector automático anterior.
- Faltan arc42 §8 aplicado, ADR de reajuste, mapeo explícito de aspectos y evidencia SonarCloud pública.
