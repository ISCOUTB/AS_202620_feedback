> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · Drift

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Estado revisado | `8a00556` en `origin/master` (`2026-09-30T22:34:57-05:00`) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

> Esta pasada **no tiene cierre**: se califica la punta actual de `origin/master` (`8a00556`). El baseline del periodo es `74709aa` (S8). La entrega S9 está compilada en `docs/evidencias/evidencias_semana9.md` (commit `cb835fe`), con el ADR-0007 (`48f7236`) y la corrección de erosión (`0ebb19e`) dentro del periodo. Parte de la cadena (adaptador de Steam, prueba de contrato y medición) proviene de S6–S7 y se cita aquí como evidencia del sistema, no como trabajo nuevo del periodo.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | `backend/app/infrastructure/external/steam/steam_game_repository.py`, creado en `b9ff5b0` (2026-09-03) y modificado en `a4b2d3c` (2026-09-13); implementa el puerto `GameRepository` dentro del backend. Apoyo de IA documentado en `docs/ia.md` Registros 25–28. | Cumple | Es parte del sistema (integración externa), no un ejercicio aparte. Ambos commits son ancestros de `origin/master`. |
| Cadena completa navegable para esa porción | `docs/aspectos.md` fila E1 → `docs/escenarios.md#escenario-1` → `docs/adr/0006-despliegue-serverless-api-busqueda.md` → `scripts/k6_baseline.js` → `docs/evidencias/e1-linea-base.md` → `steam_game_repository.py`. | Cumple | La fila E1 de `docs/aspectos.md` enlaza código, script y evidencia con el p95 medido. |
| ADR con la decisión argumentada por el equipo | `docs/adr/0004-estrategia-de-integracion.md`: estado `Aceptado`, `Decisores: Equipo DRIFT`, con tres alternativas (síncrona, asíncrona, híbrida) y sus consecuencias; enlaza el adaptador de Steam. | Cumple | La decisión es del equipo y argumenta con las restricciones de mantenibilidad del proyecto, no solo lo propuesto por la herramienta. |
| Prueba que falla ante el defecto que cubre | `9c102df` cambia `"name"` por `"tittle"` en `backend/app/main.py`; run `CI` en rojo `36301332490`; `9750878` restaura y el run `36301421472` queda en verde. | Cumple | Verificado por API: `conclusion=failure` en `9c102df` y `success` en `9750878`. |
| Medición del escenario asociado | `docs/evidencias/e1-linea-base.md`: medición inicial p95 `14.63 s` (> umbral 3 s) y medición posterior a la optimización p95 `1.24 s` (≤ 3 s); `scripts/k6_baseline.js` fija `p(95)<3000` con 50 VUs. | Cumple | Resultado contrastado con el umbral del escenario E1. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | `docs/ia.md` Registros 24–40, cada uno con «Alternativa descartada»; p. ej. Registro 31 descarta bajar el umbral para aceptar la medición inicial y mantiene p95 ≤ 3 s. | Cumple | Extracto citado con rechazos motivados; el archivo se actualizó en el periodo (`d4c2fe7`, 2026-09-30). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | `docs/evidencias/evidencias_semana9.md` §2.7: dependencia de `application` hacia `infrastructure` en `sync_playstation_catalog.py`; se creó el puerto `backend/app/domain/ports/game_catalog_repository.py` y se corrigió en `0ebb19e`; `git grep '^from app\.infrastructure' backend/app/application` sin resultados en la punta. | Cumple | Hallazgo, corrección y verificación citados; confirmado sobre el código en la punta (grep sin coincidencias). |
| Dependencias propuestas verificadas en su registro oficial | `docs/evidencias/evidencias_semana9.md` §2.8 lista las dependencias y sus registros. Verificado sin autenticar: PyPI `fastapi 0.141.1`, `schemathesis 4.27.5`, `gunicorn 23.0.0`; npm `next`, `react`, `react-dom`. | Cumple | **Ninguna dependencia se añadió en el periodo** (`git diff 74709aa..8a00556` sobre `requirements.txt`/`package.json` vacío); la lista verificada es el conjunto preexistente. Los nombres son legítimos. |
| Sin credenciales en código, ejemplos ni documentación generada | `git grep` de CONTRATO §9 sobre `8a00556`: única coincidencia real `id-token: write` (permiso de workflow); las demás son las cadenas de ejemplo del barrido en `docs/evidencias/evidencias_semana9.md:722-725`; sin `.env` versionado. | Cumple | Sin credenciales en el árbol ni en el diff del periodo. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | `docs/adr/0007-evaluacion-de-incorporación-coponente-generativo.md` (commit `48f7236`): decisión de **no incorporar** IA generativa, con alternativas (chatbot, recomendaciones, lógica convencional) y consecuencias. | Cumple | La decisión de no incorporarlo está argumentada en ADR, como exige la ficha. El nombre del archivo incumple la convención (ver matriz transversal). |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_Drift`, clonado sin autenticación. | Cumple | Nombre conforme y público. |
| Estructura mínima presente | Árbol de `8a00556`: `docs/arc42/` (12 secciones), `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`, `README.md`. | Cumple | Las seis rutas presentes; arc42 usa prefijo `arc42_N_` (desviación de forma, no de contenido). |
| Estado calificado identificable | Rama `origin/master`; hash `8a00556` (`2026-09-30T22:34:57-05:00`), punta actual. | Cumple | En esta pasada no hay cierre; se califica la punta. |
| Nombres de ADR según la convención | `docs/adr/0007-evaluacion-de-incorporación-coponente-generativo.md` contiene `ó` acentuada y no satisface `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$` del contrato §4 (commits `48f7236` y `1a3d833`, 2026-09-30). | No cumple | Los ADR 0001–0006 sí son conformes; el 0007 nuevo rompe la convención. |
| ADR aceptados no reescritos | `docs/adr/0002-adoptar-nextjs-fastapi-arquitectura-hexagonal.md:3` está `Aceptado`; `git log --follow` muestra ediciones posteriores a su creación (`45b5987`, 2026-08-24): `70e52e2` (2026-09-05) y `9488544` (2026-09-13), sin ADR que lo reemplace. | No cumple | Arrastre de S8; sigue abierto. ADR-0007 solo se renombró (`.mdm`→`.md`) el mismo día de su creación. |
| `docs/ia.md` al día para la semana | `d4c2fe7` (2026-09-30, «Add multiple architecture and performance review records») actualiza `docs/ia.md` dentro del periodo; los registros incluyen rechazos con motivo. | Cumple | Registro de S9 presente. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Run `CI` en verde sobre `8a00556` (`36811171291`) y `Build and deploy ... Azure` en verde (`36811171283`); `sonar-project.properties` existe, pero ningún workflow invoca el scanner ni referencia `SONAR_TOKEN` (`git grep` de `sonar` en `.github/workflows` sin coincidencias). | No cumple | Contrato §8: falta la línea del workflow que ejecuta el scanner y el run asociado al hash; un proyecto con Quality Gate no prueba que el análisis corra en CI. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de CONTRATO §9 sin coincidencias reales; sin `.env` versionado ni en el historial; pickaxe `-S'BEGIN PRIVATE KEY'` y `-S'AKIA'` sobre el periodo sin resultados. | Cumple | Sin credenciales en el árbol revisado ni en el diff del periodo. |
| Contribución de todos los integrantes | `git shortlog -sne 8a00556` consolida por correo en 4 personas: `JerryDBM`+«Sherry» (123), `JoshuaR01`+`JoshXX` (104), `lmpdiaz12`+«Luis Mario Perez Diaz» (85) y `maufern4ndez`+«Mauricio Andres Fernandez Espinosa» (66). | Cumple | Coinciden con los 4 integrantes de `EQUIPOS.md`; aportes repartidos. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `8a00556` (`2026-09-30T22:34:57-05:00`, «Update links and formatting in evidencias_semana9.md»).
- **Veredicto**: con pendientes.
- Resumen: la punta conserva las piezas de S8 (Bicep de Azure, serverless de Vercel, observabilidad con logs JSON y `/metrics` ligado a E1, costos, arc42 §7/§2 y ADR de plataforma) y añade la evidencia S9: `docs/evidencias/evidencias_semana9.md`, el ADR-0007, la corrección de erosión `0ebb19e` y los registros 24–40 de `docs/ia.md`. Los commits del periodo tocan además `main.py`, el catálogo de PlayStation y el frontend. Los runs `CI` y de despliegue a Azure del hash revisado están en verde.

Pendientes que siguen abiertos:
- Nombres de ADR: el ADR-0007 no sigue la convención kebab-case (acento en el nombre).
- ADR-0002 (vigente, aceptado) editado después de su aceptación, sin ADR de reemplazo.
- SonarCloud: falta un paso del workflow que ejecute el scanner y el run asociado al hash revisado.
- URL del despliegue y health check: diferidos a la entrega por Moodle.

## Recuento y nota sugerida

**10 de 10 criterios.**

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 5.0 = 1 + 4 × (10/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Sustentación: no evaluable desde el repositorio.
- URL del despliegue y health check: diferidos a la entrega por Moodle (no se abrió ninguna URL).
- Filas transversales abiertas: Nombres de ADR (No cumple), ADR aceptados no reescritos (No cumple) y Pipeline/SonarCloud (No cumple).

## Hallazgos para la planilla

- La entrega S9 está compilada y es trazable: porción, cadena E1, ADR-0004, prueba de contrato en rojo, medición p95, registros de IA, corrección de erosión y ADR-0007.
- La prueba que falla ante el defecto se verificó por API (`36301332490` en rojo sobre `9c102df`; `36301421472` en verde sobre `9750878`).
- El ADR-0007 no cumple la convención de nombres (`ó` acentuada en el nombre del archivo) y además tiene un typo («coponente»); conviene renombrarlo a kebab-case ASCII.
- No se añadieron dependencias en el periodo (diff `74709aa..8a00556` vacío); la verificación de §2.8 es sobre el conjunto preexistente, y todas existen en PyPI/npm.
- SonarCloud sigue sin integrarse al pipeline: no hay paso del workflow que invoque el scanner pese a existir `sonar-project.properties`; hallazgo abierto desde S6.
- El ADR-0002 (vigente, aceptado) fue editado el 05/09 y el 13/09 sin ADR de reemplazo → fila transversal en No cumple.
