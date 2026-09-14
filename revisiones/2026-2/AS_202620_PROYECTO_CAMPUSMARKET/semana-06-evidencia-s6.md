# semana-06-evidencia-s6 · CampusMarket

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `dc548c0` en `origin/master` (2026-09-13T01:19:54-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/arc42/08-conceptos-transversales.md sección 8.3 (diagrama mermaid con Customer/Supplier y ACL; shared kernel declarado ausente) en HEAD dc548c0 | Cumple | Relaciones tipificadas con vocabulario de la semana; marcadas como previstas para contextos no materializados. |
| Tabla módulo a datos con dueño único por entidad | docs/arc42/05-bloques-de-construccion.md sección 5.6 y docs/arc42/08-conceptos-transversales.md sección 8.4; tabla campo-propietario para publicaciones | Cumple | Dueño único: Gestión de Publicaciones; única entidad materializada. |
| La tabla cubre las entidades que existen en el código | Árbol HEAD dc548c0: solo backend/app/publicaciones/repository.py contiene lógica de persistencia; módulos usuarios/catalogo/administracion solo __init__.py | Cumple | No hay migraciones ni .sql; la entidad publicaciones es la única existente y está cubierta. |
| Violaciones de propiedad de datos detectadas sobre el código actual | README.md sección 'Pruebas automatizadas' declara verificación de propiedad única y ausencia de acceso directo a SQLite; árbol HEAD dc548c0 no muestra otros escritores | Cumple | No se detectaron violaciones; recorrido documentado en README y test_modularidad_s6.py (contenido no proporcionado). |
| Plan de corrección por violación | README.md declara pruebas de modularidad que verifican propiedad única y dirección de dependencias; sin violaciones no hay plan | Cumple | Plan vacío justificado por la verificación automatizada declarada. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/08-conceptos-transversales.md con 8.1 lenguaje ubicuo, 8.2 contextos, 8.3 mapa, 8.4 propiedad | Cumple | Incluye términos del dominio y mapa de contextos. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/03-componentes-backend.md y .puml en HEAD; commits 0de9b45 y 930ae03 documentan C4 Nivel 3; sin cambio de límites no se requiere ADR de reajuste | Cumple | Límites del monolito se mantienen desde ADR-0001; C4 Nivel 3 actualizado. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md existe en el árbol HEAD dc548c0 pero su contenido no fue proporcionado | No verificado | No se pudo contrastar los contextos con las filas de aspectos.md. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET visible; autores consolidados: nilver-garcia/Nnigarp, camilixo92, Carulla-sd | Cumple | Tres integrantes declarados aparecen en el historial. |
| Estructura mínima | Árbol HEAD dc548c0: docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura mínima presente. |
| Estado del repositorio calificado | origin/master, hash dc548c0 2026-09-13T01:19:54-05:00 anterior al cierre 2026-09-14T05:00:00Z | Cumple | Commit vigente al cierre. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md y 0002-manejo-bloqueo-sqlite.md con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Nombres en kebab-case y numerados. |
| Tabla de aspectos | docs/aspectos.md en el árbol; contenido no proporcionado | No verificado | Requiere revisar las 8 columnas y navegabilidad. |
| Registro de uso de IA | docs/ia.md con log de 16 commits (2026-08-08 a 2026-09-13); contenido no proporcionado | No verificado | Requiere revisar columnas de aceptado/rechazado. |
| README y reproducibilidad | README.md con descripción, arranque con un solo comando (scripts/run_s4.sh/.ps1) y pruebas pytest | Cumple | Requisitos previos declarados. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml y .sonarcloud.properties existen; sin runs_ci con URL | No verificado | Se requiere enlace a ejecución de GitHub Actions y SonarCloud. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `dc548c068ea3b60ae6edc672208a425748759bdf 2026-09-13T01:19:54-05:00 Actualizar registro de IA con cierre S6`
- **Veredicto**: al dia
- Resumen: Entrega S6 completa en su mayoría; mapa de contextos, propiedad de datos y arc42 sección 8 bien documentados. Quedan sin verificar aspectos.md, ia.md y ejecución de pipeline por falta de evidencia en la revisión.

Pendientes que siguen abiertos:
- Verificar contenido de docs/aspectos.md
- Verificar contenido de docs/ia.md
- Aportar runs_ci del pipeline

## Recuento y nota sugerida

7 de 8 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.5 = 1 + 4 × (7/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- docs/aspectos.md (contenido no proporcionado)
- docs/ia.md (contenido no proporcionado)
- runs_ci (sin URLs de ejecución)
- docs/evidencias/auditoria-modularidad-s6-2026-09-12.md (contenido no proporcionado)

## Hallazgos para la planilla

- docs/aspectos.md no verificable por falta de contenido en la evidencia.
- docs/ia.md no verificable su contenido (solo el log de commits).
- Sin runs_ci no se puede verificar la ejecución del pipeline.
- La evidencia de auditoría S6 (docs/evidencias/auditoria-modularidad-s6-2026-09-12.md) no fue proporcionada; se infiere de README y árbol.
- No hay commits posteriores al cierre; entrega a tiempo.
