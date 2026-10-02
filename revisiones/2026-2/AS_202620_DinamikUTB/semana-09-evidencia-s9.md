> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · DinamikUTB

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Estado revisado | `d72a10a` en `origin/master` (`2026-09-28T00:09:14-05:00`) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

> Esta pasada **no tiene cierre**: se califica la punta actual de `origin/master` (`d72a10a`). No hay entrega S9 en el repositorio: la punta coincide con el estado de S8 más un único commit posterior de README (`git log 287c65d..origin/master` = `d72a10a` «Update README.md»). El baseline del periodo es `287c65d` (S8). Bajo CONTRATO §12 la evidencia previa es línea base y no se recalifica por existir, de modo que las filas que dependen de la entrega nueva de S9 quedan en No cumple por ausencia.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | No hay artefacto S9. `git log 287c65d..origin/master` solo devuelve `d72a10a` («Update README.md»); no se identifica en el periodo ninguna porción nueva. | No cumple | La única porción trazable como asistida por IA (`backend/app/requisitos/`, entrada del 30/08 en `docs/ia.md`) es de S4 y no se presenta como evidencia S9. |
| Cadena completa navegable para esa porción | `docs/aspectos.md`: la columna «Evidencia» vale «Pendiente» en las ocho filas (A-01…A-08). | No cumple | La cadena se rompe en el eslabón de evidencia; A-01 sí enlaza código, pruebas y un run, pero deja la evidencia pendiente. |
| ADR con la decisión argumentada por el equipo | `docs/adr/0001`…`0007` existen, pero ninguno se redactó para esta evidencia ni argumenta una decisión de generación verificada. | No cumple | Son ADR de arquitectura/tecnología/plataforma anteriores a S9; no hay ADR nuevo en el periodo. |
| Prueba que falla ante el defecto que cubre | No hay evidencia S9. `docs/api/evidencia-prueba-contrato.md` documenta un run en rojo, pero es línea base de S7. | No cumple | Sin run en rojo, prueba de mutación ni procedimiento nuevo para S9. |
| Medición del escenario asociado | No hay resultado S9 contrastado con umbral. `backend/app/main.py:78` expone `/metrics`, pero sin medición registrada. | No cumple | La métrica existe; no hay valor medido ni comparación con el umbral. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | `docs/ia.md` no se actualizó en el periodo (sin commits entre `287c65d` y `d72a10a`). | No cumple | El archivo sí contiene rechazos motivados previos (p. ej. «Rechazado parcialmente» por sobrecarga visual), pero no hay extracto nuevo para S9. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | La auditoría de propiedad de datos está en `docs/arc42/08-cross-cutting-concepts.md:67` («Violaciones de propiedad de datos detectadas»), fechada en el periodo de S6. | No cumple | Es línea base de S6; no se refrescó para S9 ni acompaña a una generación nueva. |
| Dependencias propuestas verificadas en su registro oficial | `git diff 287c65d..origin/master` sobre `backend/requirements.txt`, `backend/pyproject.toml` y `frontend/pubspec.yaml` está vacío. | No cumple | No se añadieron dependencias en el periodo; no hay lista que verificar. |
| Sin credenciales en código, ejemplos ni documentación generada | `git grep` del barrido de CONTRATO §9 sobre `d72a10a`: única coincidencia `.github/workflows/deploy-pages.yml:11 id-token: write` (permiso de workflow); sin `.env` versionado (solo `.env.example`). | Cumple | Barrido sin credenciales reales en el árbol revisado. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Ningún ADR de `docs/adr/` trata la incorporación de un componente generativo. | No cumple | No hay conjunto de evaluación ni ADR de decisión de no incorporarlo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_DinamikUTB`, clonado sin autenticación. | Cumple | Nombre conforme y público. |
| Estructura mínima presente | Árbol de `d72a10a`: `docs/arc42/01..12`, `docs/adr/0001..0007`, `docs/c4/*.puml`, `docs/aspectos.md`, `docs/ia.md`, `README.md`. | Cumple | Las seis rutas del contrato están presentes. |
| Estado calificado identificable | Rama `origin/master`; hash `d72a10a` (`2026-09-28T00:09:14-05:00`), punta actual. | Cumple | En esta pasada no hay cierre; se califica la punta. |
| Nombres de ADR según la convención | `docs/adr/0001-seleccion-monolito-modular.md` … `0007-persistencia-render-postgres.md`, todos `NNNN-kebab-case.md`. | Cumple | Siete nombres conformes. |
| ADR aceptados no reescritos | `docs/adr/0001`, `0002`, `0005` y `0006` tienen ediciones posteriores a su aceptación y ningún ADR que los reemplace (histórico citado en la revisión S8). | No cumple | Hallazgo arrastrado desde S8; sigue abierto. |
| `docs/ia.md` al día para la semana | Sin commits sobre `docs/ia.md` en el periodo (`287c65d..d72a10a`). | No cumple | La última entrada es del 26/09 (S8); no hay registro de S9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | `sonar-project.properties` (projectKey `ISCOUTB_AS_202620_DinamikUTB`) y job `sonarcloud` con `SonarCloud Scan` en `.github/workflows/ci.yml:55-78`; run `CI` sobre `d72a10a` en verde: https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/36380658219; Quality Gate público `OK` (verificado en S8). | Cumple | Las tres evidencias del contrato §8 presentes; el run verde corresponde al hash revisado. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de CONTRATO §9 sin coincidencias reales; sin `.env` versionado. | Cumple | Única coincidencia `id-token: write` (permiso). |
| Contribución de todos los integrantes | `git shortlog -sne d72a10a` consolida por correo en 4 personas: `404Vargas`+`JuanchisV`+«Juan José Vargas Pérez» (188), `Daniel-dev02`+«LUIS DANIEL» (60), `gillianisperez-prog` (26) y `Eramirezr` (12). | Cumple | Coinciden con los 4 integrantes de `EQUIPOS.md`; desbalance anotado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `d72a10a` (`2026-09-28T00:09:14-05:00`, «Update README.md»), la misma punta que registró la revisión S8.
- **Veredicto**: sin entrega S9.
- Resumen: entre el baseline de S8 (`287c65d`) y la punta actual solo hay un commit de README. No se incorporó ningún artefacto de S9 (porción, ADR, prueba, medición, auditoría de erosión, verificación de dependencias o ADR de componente generativo). El repositorio conserva las piezas de S8 (IaC, logs JSON, `/metrics` ligado a Q-05, costos, arc42 §7/§2, ADR de plataforma, SonarCloud en CI), que son línea base y no se recalifican aquí. Las filas de S8 siguen vigentes salvo lo que esta pasada registra como ausencia de entrega.

Pendientes que siguen abiertos:
- No hay entrega S9 en el repositorio.
- ADR-0001, 0002, 0005 y 0006 editados después de su aceptación, sin ADR de reemplazo (arrastre de S8).
- URL del despliegue y health check: diferidos a la entrega por Moodle (arrastre de S8).

## Recuento y nota sugerida

**1 de 10 criterios.**

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Sustentación: no evaluable desde el repositorio.
- URL del despliegue y health check: diferidos a la entrega por Moodle (no se abrió ninguna URL).
- Fila transversal de ADR aceptados no reescritos: No cumple, arrastrada de S8.

## Hallazgos para la planilla

- No hay entrega S9: la punta `d72a10a` es el estado de S8 más un commit de README. La matriz de S9 se califica por ausencia.
- Se mantiene abierto el hallazgo de ADR aceptados editados después de su aceptación (ADR-0001/0002/0005/0006), sin ADR de reemplazo.
- El repositorio conserva en verde su pipeline y su análisis estático (CI `36380658219` sobre `d72a10a`), pero eso es línea base de S8, no evidencia de S9.
