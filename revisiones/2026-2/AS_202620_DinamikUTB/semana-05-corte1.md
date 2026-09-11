# semana-05-corte1 · DinamikUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `72bfc7e` en `origin/master` (2026-09-07T22:28:37-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master 72bfc7e 2026-09-07T22:28:37-05:00; cierre 2026-09-10T17:00:00Z | Cumple | Rama principal master, sin commits posteriores al cierre. |
| correcciones.md existe en la raíz del estado calificado | correcciones.md en árbol de 72bfc7e; commits f89564f..72bfc7e lo crean/actualizan antes del cierre | Cumple | Archivo presente en la raíz del hash calificado. |
| Correcciones trazables y contrastadas | No se incluyó el contenido de correcciones.md en la evidencia | No verificado | Se requiere inspeccionar el archivo en 72bfc7e para contrastar hallazgos S1-S4. |
| S1 al día: equipo, problema y repositorio | README.md con descripción, problema, objetivos, usuarios y equipo; docs/fichadelproblema.md y 01-introduction-and-goals.md en 72bfc7e | Cumple | Equipo consolidado en 4 identidades con participación repartida en el historial. |
| S2 al día: escenarios de calidad y restricciones | 02-architecture-constraints.md presente con restricciones; 10-quality-requirements.md solo listado en el árbol | No verificado | Falta contenido de 10-quality-requirements.md para verificar escenarios Q-01..Q-08. |
| S3 al día: estrategia de solución y decisiones | ADR-0001, 0002 y 0003 completos en docs/adr/; 04-solution-strategy.md con comparación y decisión | Cumple | Decisiones con contexto, alternativas, consecuencias y trazabilidad. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/07-deployment-view.md y 08-cross-cutting-concepts.md vacíos en 72bfc7e | No cumple | arc42 incompleto: secciones 07 y 08 sin contenido; 05 y 06 sí documentados. |
| Corte vertical reproducible y coherente con la arquitectura | backend/app/requisitos/ y frontend/lib/requisitos/ presentes; README documenta start.bat, pytest y flutter test; sin runs_ci | No verificado | Coherencia con C4 visible, pero reproducibilidad no verificada sin run de CI. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml existe en 72bfc7e; no se aportó URL de run | No verificado | Comando pendiente: curl a api.github.com/repos/ISCOUTB/AS_202620_DinamikUTB/actions/runs. |
| Trazabilidad consolidada navegable | docs/aspectos.md listado en el árbol; contenido no disponible | No verificado | Se requiere verificar las 8 columnas y enlaces navegables. |
| PDF u otro adjunto exigido por el aula | Sin evidencia de entrega en Moodle | No verificado | La ficha indica No verificado si no está disponible. |
| Sustentación del corte | Sin sesión de sustentación | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_DinamikUTB público; historial con 4 identidades consolidadas | Cumple | Nombre y visibilidad correctos; integrantes declarados presentes. |
| Estructura mínima | docs/arc42 (12 secciones), docs/adr (3), docs/c4, docs/aspectos.md, docs/ia.md y README.md en 72bfc7e | Cumple | Rutas cumplen la estructura; 07 y 08 vacíos pero presentes. |
| Estado del repositorio calificado | origin/master 72bfc7e anterior al cierre; sin commits posteriores | Cumple | Hash exacto conservado en el informe. |
| Convenciones de ADR | 0001-seleccion-monolito-modular.md, 0002-seleccion-tecnologia-backend-frontend.md y 0003-seleccion-motor-de-base-de-datos.md | Cumple | Nombres en kebab-case numerado; cada ADR con contexto, decisión, consecuencias y trazabilidad. |
| Tabla de aspectos | docs/aspectos.md listado; contenido no disponible | No verificado | No se pudo verificar columnas ni navegabilidad. |
| Registro de uso de IA | docs/ia.md existe con 15 commits de historial; contenido no disponible | No verificado | El log muestra crecimiento, pero falta verificar columnas de aceptado/rechazado. |
| README | README.md con descripción, inicio rápido (start.bat), pruebas (pytest, flutter test) y requisitos | Cumple | Documenta arranque con un comando y cómo probar. |
| Pipeline y análisis estático | .github/workflows/ci.yml presente; sin runs_ci ni SonarCloud | No verificado | Secretos sin coincidencias y autoría repartida, pero ejecución de CI no verificada. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `72bfc7e206eac4147dd244c03fa09b4b32b9a7e7 2026-09-07T22:28:37-05:00 Update correcciones.md`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene estructura y decisiones sólidas, pero arrastra secciones arc42 vacías (07 y 08) y varios artefactos sin verificar (correcciones.md, aspectos.md, 10-quality-requirements.md, CI).

Pendientes que siguen abiertos:
- Completar docs/arc42/07-deployment-view.md y 08-cross-cutting-concepts.md.
- Verificar contenido de correcciones.md, aspectos.md, 10-quality-requirements.md e ia.md.
- Aportar runs de CI del hash 72bfc7e.
- Entregar PDF en Moodle y sustentar.

## Recuento y nota sugerida

4 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.3 = 1 + 4 × (4/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correcciones trazables y contrastadas (falta contenido de correcciones.md).
- S2 al día (falta contenido de 10-quality-requirements.md).
- Corte vertical reproducible (sin runs_ci).
- Pipeline y pruebas (sin runs_ci).
- Trazabilidad consolidada (falta contenido de aspectos.md).
- PDF en Moodle.
- Sustentación.
- Tabla de aspectos (transversal).
- Registro de uso de IA (transversal).
- Pipeline y análisis estático (transversal).

## Hallazgos para la planilla

- docs/arc42/07-deployment-view.md y 08-cross-cutting-concepts.md vacíos en el hash calificado.
- Contenido de correcciones.md no disponible para contrastar trazabilidad.
- Contenido de docs/10-quality-requirements.md no verificado.
- Contenido de docs/aspectos.md no verificado.
- Sin runs de CI en la evidencia; pipeline no verificable.
- docs/ia.md existe con historial, pero contenido no verificado.
- Sin evidencia de PDF en Moodle ni sustentación.
- Secretos: sin coincidencias en el hash (correcto).
- Autoría consolidada en 4 identidades; participación repartida.
