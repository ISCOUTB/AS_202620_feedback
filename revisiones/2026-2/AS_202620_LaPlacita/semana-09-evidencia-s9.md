> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# Semana 9 · Generación verificada y trazable · LaPlacita


| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `b03a797` en `origin/master` (`2026-09-27T19:00:57-05:00`) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |
| Línea base del periodo | `b03a79783e5675b6251d14af5edee077de86e3bd` (hash calificado de S8) |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | `git rev-list --count b03a797..origin/master` = **0**: no hay commits entre el hash calificado de S8 y la punta. La última entrada de `docs/ia.md` es `4f38051` (2026-09-27), línea base de S8. | No cumple | No hay porción construida con IA **del periodo S9**; el trabajo existente es de S8 y no se recalifica por existir (`CONTRATO.md` §12). |
| Cadena completa navegable para esa porción | `docs/aspectos.md` no cambió en el periodo (sin commits); no hay fila nueva del periodo recorrible hasta código, prueba y medición. | No cumple | El archivo existe, pero su contenido es línea base de semanas anteriores. |
| ADR con la decisión argumentada por el equipo | Los ADR `0001`…`0011` son todos anteriores al periodo; el más reciente es `4f38051` (2026-09-27). No hay ADR nuevo en el periodo S9. | No cumple | Sin decisión de S9 que argumentar. |
| Prueba que falla ante el defecto que cubre | No hay run en rojo, prueba de mutación ni procedimiento documentado del periodo; el repo no tiene commits de S9 donde buscarla. | No verificado | No hay ninguna de las tres evidencias: queda como pregunta de sustentación (la ficha lo manda así). |
| Medición del escenario asociado | No hay medición del periodo; `scripts/medir-aislamiento.js` es de S5 (línea base). | No cumple | Resultado contrastado con umbral ausente para S9. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | `git log -3 -- docs/ia.md` termina en `4f38051` (2026-09-27): sin actualización dentro del periodo S9. | No cumple | El extracto citado tendría que ser de S9; el actual es de S8. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Sin hallazgos ni correcciones del periodo; `git grep` de escrituras no aporta nada nuevo porque no hay código generado en S9. | No cumple | No hay generación de S9 que auditar. |
| Dependencias propuestas verificadas en su registro oficial | `git diff b03a797..origin/master -- package.json requirements.txt pyproject.toml pom.xml go.mod Gemfile` vacío: no se añadieron dependencias en el periodo. | No cumple | Nada que verificar contra npm/PyPI en S9. |
| Sin credenciales en código, ejemplos ni documentación generada | `git grep` de los patrones del contrato sin coincidencias (exit 1) sobre `origin/master`; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` vacío. | Cumple | Barrido sobre el estado de la punta (fila decidida sobre el tip). |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No hay ADR del periodo que decida sobre el componente generativo. | No cumple | Silencio no es la decisión de no incorporarlo; falta el ADR que lo justifique. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia y observaciones | Estado |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_LaPlacita`, clonado sin autenticación. | Cumple |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`. | Cumple |
| Estado calificado identificable | `origin/master` `b03a79783e5675b6251d14af5edee077de86e3bd`, 2026-09-27T19:00:57-05:00 (punta actual; en la pasada temprana no hay cierre que acote). | Cumple |
| Nombres de ADR según la convención | `docs/adr/0001`…`0011` cumplen `NNNN-titulo-en-kebab-case.md`. | Cumple |
| ADR aceptados no reescritos | ADR-0001 (`bf94244`→`95ec841`), ADR-0003 (`745e799`→`95ec841`), ADR-0009 (`9452e43`→`4f38051`) y ADR-0010 (`c46fd36`→`c99f542`) fueron editados tras su aceptación sin reemplazo declarado (`git log --follow` por archivo). | No cumple |
| `docs/ia.md` al día para la semana | Sin commits sobre el archivo en el periodo S9; última actualización `4f38051` (2026-09-27, S8). | No cumple |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Run del tip `36360634637` (`CI LaPlacita`, `master`, `completed/success`), pero el job `sonar` es informativo (`continue-on-error: true`, ci.yml) y no se aporta la URL pública del Quality Gate; ADR-0010 declara el vínculo org/proyecto pendiente. | No cumple |
| Sin credenciales en el repositorio ni en el historial | `git grep` sin coincidencias, sin `.env` versionado, `git log -S'BEGIN PRIVATE KEY'` vacío. | Cumple |
| Contribución de todos los integrantes | 4 identidades consolidadas / 4 integrantes: Jorge 64, Samuel 34, Isaza 18+11 (mismo correo), Mateo 19+1 (dos correos). | Cumple |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `b03a797` en `origin/master` (2026-09-27T19:00:57-05:00). Coincide exactamente con el hash calificado de S8.
- **Periodo S9:** `git rev-list --count b03a797..origin/master` = 0. No hay ningún commit posterior al estado de S8 en la rama principal.
- **Veredicto:** sin entrega S9 al momento de la pasada preliminar. La matriz queda 1/10 (solo el barrido de credenciales, que se decide sobre la punta). El proyecto conserva el estado S8; no hay código, ADR, prueba, medición ni registro de IA del periodo S9.
- La nota sube sola cuando el equipo empuje la entrega antes del 2026-10-05T05:00:00Z.

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- «Prueba que falla ante el defecto que cubre»: No verificado — no hay run en rojo, mutación ni procedimiento documentado (queda como pregunta de sustentación).
- Toda la matriz de la ficha, salvo el barrido de credenciales: pendiente de evidencia del periodo S9.
- URL pública del análisis de SonarCloud y estado del Quality Gate (deuda transversal abierta desde S6).

## Hallazgos para la planilla

- Cero commits entre el hash calificado de S8 (`b03a797`) y la punta: la entrega S9 no ha sido empujada a `origin/master` al momento de esta pasada.
- El barrido de credenciales sobre la punta está limpio y los cuatro integrantes siguen contribuyendo.
- Se mantienen las no conformidades transversales de S8: ADR aceptados editados sin reemplazo declarado y Quality Gate de SonarCloud sin URL pública.
