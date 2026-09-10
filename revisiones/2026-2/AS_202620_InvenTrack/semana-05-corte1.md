# semana-05-corte1 · InvenTrack

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `2988b03` en `origin/main` (2026-09-06T23:35:40-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/main; hash 2988b03; fecha 2026-09-06T23:35:40-05:00 (2026-09-07T04:35:40Z) anterior al cierre 2026-09-07T05:00:00Z | Cumple | Rama principal main; no se usaron etiquetas. |
| correcciones.md existe en la raíz del estado calificado | Árbol de 2988b03 no incluye correcciones.md; solo feedback.md; ac951e3 (2026-09-08) lo renombra tras el cierre | No cumple | Archivo añadido después del cierre no cumple la fila. |
| Correcciones trazables y contrastadas | No hay correcciones.md en 2988b03; sin respuestas a hallazgos S1-S4 | No cumple | Imposible contrastar correcciones en el estado calificado. |
| S1 al día: equipo, problema y repositorio | docs/ficha_problema.md; README.md con equipo; shortlog muestra Jose Vargas, Esteban Peluffo, Felix Taborda, Javier Carta | Cumple | Repositorio ISCOUTB/AS_202620_InvenTrack público. |
| S2 al día: escenarios de calidad y restricciones | docs/utility-tree.md con ESC-01 a ESC-05; arc42 sección 2 con C1-C7 | Cumple | Escenarios medibles y restricciones tipificadas. |
| S3 al día: estrategia de solución y decisiones | docs/matriz-comparativa-estilos.md; docs/adr/0001 y 0002 con contexto, alternativas, decisión, consecuencias | Cumple | Dos ADR aceptados. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-EN.md; docs/c4/context.md y containers.md; app/productos/ con domain/application/infrastructure; tests/productos/test_api_corte_vertical.py | Cumple | Corte vertical funcional en productos. |
| Corte vertical reproducible y coherente con la arquitectura | README documenta arranque (uvicorn) y pruebas (pytest); tests en tests/; run CI success https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/34083473400 | Cumple | Coherente con ADR-0001 y C4. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/test.yml ejecuta pytest; runs success (34083473400, 34089801823) | Cumple | Runs anteriores al cierre en verde. |
| Trazabilidad consolidada navegable | docs/aspectos.md con tabla de 8 columnas enlazando ASP-01 y ASP-02 a requisito, C4, ADR, código, pruebas y evidencia | Cumple | Cadena navegable completa. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; adjunto de Moodle no accesible | No verificado | Requeriría acceso al aula. |
| Sustentación del corte | Sesión de sustentación no disponible | No verificado | Lo resuelve el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima | docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md en 2988b03 | Cumple | Incluye además docs/retos y docs/ficha_problema.md. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md y 0002-control-concurrencia-memoria-inventario.md; nombres kebab-case; contenido con contexto, alternativas, decisión, consecuencias, trazabilidad | Cumple | Sin evidencia de reescritura post-aceptación. |
| Tabla de aspectos | docs/aspectos.md con columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia; enlaces a artefactos | Cumple | Dos aspectos ASP-01 y ASP-02. |
| Registro de uso de IA | docs/ia.md con tabla de usos, aceptado/rechazado y motivo; historial con 11 commits (2026-08-09 a 2026-09-06) | Cumple | Columna de rechazos con justificación técnica. |
| README | README.md con descripción, stack, arranque (python -m uvicorn app.main:app --reload) y pruebas (pytest) | Cumple | Incluye enlaces a documentación. |
| Pipeline y análisis estático | .github/workflows/test.yml solo ejecuta pytest; no hay paso de SonarCloud; sonar-project.properties presente pero sin run | No cumple | Falta integración de SonarCloud exigida por el contrato. |
| Secretos | git grep sin coincidencias de credenciales; sin .env versionados | Cumple | Repositorio público sin secretos detectados. |
| Autoría y colaboración | shortlog consolida 4 identidades (Jose Vargas, Esteban Peluffo, Felix Taborda, Javier Carta); actividad desde 2026-08 | Cumple | Distribución desigual: un integrante concentra la mayoría de commits. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `ac951e3fc2acf849f2cc89ffb622d392b268672a 2026-09-08T10:11:58-05:00 Update and rename feedback.md to correcciones.md`
- **Veredicto**: con pendientes
- Resumen: Proyecto con documentación arquitectónica completa y corte vertical funcional; la entrega S5 no incluyó correcciones.md en el estado calificado y el pipeline carece de SonarCloud.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- correcciones.md creado en ac951e3 (2026-09-08) tras el cierre, renombrando feedback.md.
- Frontend definido como Flutter en cf9d7d3 (2026-09-07) tras el cierre, actualizando README y containers.md.

Pendientes que siguen abiertos:
- Integrar SonarCloud al pipeline de CI.
- Verificar que correcciones.md responda a todos los hallazgos S1-S4.
- Equilibrar la distribución de contribuciones.

## Recuento y nota sugerida

8 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula (no accesible desde el repositorio).
- Sustentación del corte (sesión docente).
- Contenido de correcciones.md en HEAD (no disponible en la evidencia).

## Hallazgos para la planilla

- correcciones.md ausente en el estado calificado 2988b03; se añadió en ac951e3 tras el cierre.
- Commits post-cierre (3defc32, cf9d7d3, c837d7d, ac951e3) modifican README, containers.md y crean correcciones.md.
- El pipeline de CI no ejecuta SonarCloud; solo pytest.
- La contribución está muy concentrada: un integrante acumula la mayoría de commits.
- El frontend pasó de 'Por definir' a Flutter en docs tras el cierre, sin implementación.
- Commits posteriores al cierre (no calificados): ac951e3 2026-09-08T10:11:58-05:00 Update and rename feedback.md to correcciones.md; c837d7d 2026-09-07T01:12:16-05:00 datalle; cf9d7d3 2026-09-07T00:59:16-05:00 docs: definir Flutter como frontend; 3defc32 2026-09-07T00:59:16-05:00 Pequenos detalles
