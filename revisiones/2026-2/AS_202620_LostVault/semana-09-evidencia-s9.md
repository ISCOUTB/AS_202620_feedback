> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# Semana 9 · Generación verificada y trazable · LostVault


| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `a5faf6a` en `origin/main` (`2026-09-28T00:11:11-05:00`) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |
| Línea base del periodo | `4a9ecc944731d0af243724b26a08d5deee22d7e3` (hash calificado de S8) |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | Periodo `4a9ecc94..origin/main` = 2 commits (`ccad9ad`, `a5faf6a`) que tocan **solo** `backend/DEPLOY_VERCEL.md` (documentación de Swagger UI). No hay código del sistema construido en el periodo. | No cumple | La documentación de Swagger es línea base/editorial, no una porción del sistema; no satisface la fila (`CONTRATO.md` §12). |
| Cadena completa navegable para esa porción | `docs/aspectos.md` no cambió en el periodo; no hay fila nueva recorrible hasta código, prueba y medición. | No cumple | Sin cadena de S9 que recorrer. |
| ADR con la decisión argumentada por el equipo | No hay ADR nuevo en el periodo; el último es `b561576` (2026-09-27) y el tip solo toca `DEPLOY_VERCEL.md`. | No cumple | Sin decisión de S9 que argumentar. |
| Prueba que falla ante el defecto que cubre | No hay run en rojo, prueba de mutación ni procedimiento documentado del periodo. | No verificado | No hay ninguna de las tres evidencias: queda como pregunta de sustentación (la ficha lo manda así). |
| Medición del escenario asociado | No hay medición del periodo; los cálculos p95 son de S8 (línea base). | No cumple | Resultado contrastado con umbral ausente para S9. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | `git log -3 -- docs/ia.md` termina en `5a96601` (2026-09-27): sin actualización dentro del periodo S9. | No cumple | El extracto citado tendría que ser de S9; el actual es de S8. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Sin hallazgos ni correcciones del periodo; no hay código generado en S9 que auditar. | No cumple | Sin generación de S9. |
| Dependencias propuestas verificadas en su registro oficial | `git diff 4a9ecc94..origin/main -- package.json requirements.txt pyproject.toml pom.xml go.mod Gemfile` vacío (el único archivo modificado es `backend/DEPLOY_VERCEL.md`). | No cumple | Nada que verificar contra npm/PyPI en S9. |
| Sin credenciales en código, ejemplos ni documentación generada | `git grep` del contrato sobre `origin/main` solo halla lecturas de entorno (`JWT_SECRET`, cabecera `authorization`, `var.vercel_api_token`); sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` vacío. | Cumple | Barrido sobre el estado de la punta (fila decidida sobre el tip). |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No hay ADR del periodo que decida sobre el componente generativo. | No cumple | Silencio no es la decisión de no incorporarlo; falta el ADR que lo justifique. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia y observaciones | Estado |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_LostVault`, clonado sin autenticación. | Cumple |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`. | Cumple |
| Estado calificado identificable | `origin/main` `a5faf6af28302f5d265c29c71c4a47741ef96708`, 2026-09-28T00:11:11-05:00 (punta actual; en la pasada temprana no hay cierre que acote). | Cumple |
| Nombres de ADR según la convención | `docs/adr/000.3-despliegue-busqueda-lostvault.md` no cumple `NNNN-titulo-en-kebab-case.md`. | No cumple |
| ADR aceptados no reescritos | ADR-0001 (`723d9e6`→`edd78d7`) y ADR-0002 (`c91a71e`→`b561576`) fueron editados tras su aceptación sin reemplazo declarado (`git log --follow` por archivo). | No cumple |
| `docs/ia.md` al día para la semana | Sin commits sobre el archivo en el periodo S9; última actualización `5a96601` (2026-09-27, S8). | No cumple |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Runs del tip `a5faf6a` en verde: Backend `36380804756`, Flutter `36380804799` y Build (con paso de Quality Gate) `36380804782`; hay `sonar-project.properties` y el workflow invoca el scanner, pero no se aporta la URL pública del análisis/Quality Gate (`evidencias-profesor.md` solo remite a `sonarcloud.io`). | No cumple |
| Sin credenciales en el repositorio ni en el historial | `git grep` sin credenciales reales, sin `.env` versionado, `git log -S'BEGIN PRIVATE KEY'` vacío. | Cumple |
| Contribución de todos los integrantes | 4 personas consolidadas / 4 integrantes: Roy 45+1, Fausto-4 33+2+1 (mismo correo), Shamara 19+4, Kiefer 9+2 (mismo correo). | Cumple |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada:** `a5faf6a` en `origin/main` (2026-09-28T00:11:11-05:00).
- **Periodo S9:** 2 commits tras el hash calificado de S8 (`4a9ecc94`), ambos sobre `backend/DEPLOY_VERCEL.md` («Update DEPLOY_VERCEL.md with Swagger UI documentation», «Revise Swagger UI documentation section»). No hay artefactos de S9.
- **Veredicto:** sin entrega S9 al momento de la pasada preliminar. La matriz queda 1/10 (solo el barrido de credenciales, que se decide sobre la punta). El pipeline del tip está en verde, pero eso sostiene una fila transversal que falla por la falta de URL pública del Quality Gate, no la entrega de S9.
- La nota sube sola cuando el equipo empuje la entrega antes del 2026-10-05T05:00:00Z.

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- «Prueba que falla ante el defecto que cubre»: No verificado — no hay run en rojo, mutación ni procedimiento documentado (queda como pregunta de sustentación).
- Toda la matriz de la ficha, salvo el barrido de credenciales: pendiente de evidencia del periodo S9.
- URL pública del análisis de SonarCloud y estado del Quality Gate (deuda transversal abierta desde S6).
- Convención del ADR `000.3` y reescritura de ADR-0001/ADR-0002 sin reemplazo declarado (persisten desde S8).

## Hallazgos para la planilla

- El único cambio del periodo S9 (`4a9ecc94..a5faf6a`) es documentación de Swagger UI en `backend/DEPLOY_VERCEL.md`: no hay porción de sistema, ADR, prueba ni medición de la semana.
- El barrido de credenciales sobre la punta está limpio y los cuatro integrantes siguen contribuyendo.
- Se mantienen las no conformidades transversales de S8: `000.3` fuera de convención, ADR aceptados editados sin reemplazo y Quality Gate de SonarCloud sin URL pública.
