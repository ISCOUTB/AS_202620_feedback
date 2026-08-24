# Evidencia S3 · Verifacts

## Datos

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `8259b75f60ed8a94d4ae0d10a693b17d6e73648d` · 2026-08-23T23:50:00-05:00 («Delete docs/arc42/docs directory») |
| Cierre | 2026-08-24T05:00:00Z |
| Fecha/hora de revisión | 2026-08-24 (posterior al cierre) |
| Comandos | clon efímero con `--filter=blob:none --no-checkout`; lecturas con `git -C "$DIR" show "$HASH:…"`; sin ejecutar código del estudiante. Sin llamadas a la API (no hay `.github/workflows/`). |
| Nota de actualización | **Revisión actualizada tras el cierre: el equipo empujó después de la primera revisión; hash calificado definitivo.** La primera revisión fue sobre `8ded7cf` (19:23 COT); el equipo siguió empujando hasta las 23:50, dentro del cierre. **Hay 15 commits TARDÍOS** (posteriores a 2026-08-24T05:00:00Z), entre 00:06 y 00:58 COT del 24-ago: serie de «Delete docs/…» (`arc42.md`, `aspectos.md`, `escenarios-de-calidad.md`, `arbol_utilidad.md`, `c4-contexto.md`, `matriz-estilos.md`, `restricciones.md`, `IA.md`) y creación de versiones alternativas (`06-arbol-utilidad.md`, `07-aspectos.md`, ADR, matriz). No se califican: el estado vigente al cierre es `8259b75`. |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/04-estrategia-de-solucion.md` (4.1–4.4) | No cumple | Avance real: ya existe 4.3 «Tácticas» con una línea por atributo priorizado (mantenibilidad, escalabilidad, rendimiento, confiabilidad). Pero son principios genéricos («alta cohesión y bajo acoplamiento», «pruebas automatizadas»), no tácticas concretas atacando cada escenario (Q-01…Q-05 de `05-escenarios-de-calidad.md`), y no se enlazan a los escenarios. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/matriz-estilos.md` | No cumple | Filas con criterios genéricos (simplicidad, testabilidad, evolución…) con escala 1–5. No compara escenario por escenario del árbol (`docs/arbol_utilidad.md`), ni usa las ramas del árbol; solo «Incorporación de nuevos analizadores» alude a Q-02. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | kebab-case correcto. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | Contexto, Decisión, Alternativas consideradas, Consecuencias positivas/negativas/deuda aceptada. Observación: el título («Selección del estilo arquitectónico») enuncia el tema, no la decisión (CONTRATO §4), y el estado sigue en «Propuesto». |
| Alternativas descartadas con su motivo | `docs/adr/0001-estilo-arquitectonico.md` («Alternativas consideradas») | Cumple | Capas descartada por cambios transversales en el motor de análisis; hexagonal por indirección desproporcionada para el alcance. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | búsqueda `adr|0001` en `docs/aspectos.md`, `docs/arc42/05-escenarios-de-calidad.md`, `docs/escenarios-de-calidad.md`, `docs/matriz-estilos.md`, `docs/arbol_utilidad.md` | No cumple | Ningún archivo del repo enlaza el ADR. `docs/aspectos.md` es un texto en prosa sobre escalabilidad sin tabla ni enlaces; los escenarios Q-01…Q-05 no referencian la decisión. |
| Arranque con un solo comando documentado en el README | `README.md` (termina en la activación del venv) | No cumple | El README no documenta el comando de arranque; `run.py` existe pero no se menciona. En el cierre sigue igual que en la primera revisión. |
| Prueba automatizada en verde | `tests/test_health.py` (`test_health_check`) | No verificado | La prueba existe, pero no hay `.github/workflows/` ni evidencia de ejecución aportada. Haría falta el run de un pipeline o captura de `pytest`. |
| Estructura de paquetes correspondiente al estilo del ADR | `app/api/` (routes, main), `app/modules/{analysis,content,scoring}/` | Cumple | Coincide con el monolito modular del ADR (API, Content, Analysis, Scoring). |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clonado sin autenticación; `ISCOUTB/AS_202620_Verifacts`. |
| Estructura mínima presente | No cumple | Desviaciones: `docs/c4-contexto.md` fuera de `docs/c4/`; `docs/IA.md` con mayúsculas. Mejora respecto a la revisión previa: ya existe `docs/arc42/` como carpeta con secciones 01–05. Los artefactos se evalúan donde están. |
| Estado calificado identificable | Cumple | `8259b75` · 2026-08-23T23:50:00-05:00 ≤ cierre; sin etiqueta (evidencia semanal). |
| Nombres de ADR según la convención | Cumple | `0001-estilo-arquitectonico.md` pasa el filtro. |
| ADR aceptados no reescritos | Cumple | Un solo commit sobre el ADR (`313b6a2`). Estado «Propuesto» en el propio ADR: a aceptar en la revisión del equipo. |
| `docs/ia.md` al día para la semana | No cumple | `docs/IA.md` describe la estrategia de IA del producto, no el registro de uso con aceptado/rechazado; sin entradas del trabajo de la semana. |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 sin coincidencias; sin `.env` versionado. |
| Contribución de todos los integrantes | No cumple | `git shortlog -sne` → PedroC1213 (30 commits) y Cristian Cardeño (4 commits, todos el 24-ago tardíos); Julian Samuel Cabeza Pena sin aparición. |

## Recuento

**4 de 9** criterios de la ficha cumplidos (4 no cumplidos, 1 no verificado).

## No verificado / pendientes

- Test en verde: sin pipeline ni evidencia de ejecución (no se llama a la API: no hay workflows). Vale la captura de `pytest tests/` que aporte el equipo.
- Ejecución real del arranque: ni siquiera está documentado en el README (falta el paso de `python run.py` o equivalente).

## Hallazgos para la planilla

- **15 commits tardíos** (posteriores al cierre 05:00Z): serie de borrados y recreaciones de documentos (`docs/arc42.md`→carpeta, `aspectos.md`, `arbol_utilidad.md`, `matriz-estilos.md`, etc.) entre 00:06 y 00:58 COT. Lo calificado es `8259b75` (23:50). El equipo debe respetar el cierre: lo que entra después no se evalúa.
- Reorganización documental incompleta al cierre: quedan `docs/arc42.md` y `docs/arc42/01-…05` conviviendo, más `docs/escenarios-de-calidad.md` y `docs/arc42/05-escenarios-de-calidad.md` duplicados (el commit tardío los borra, pero no cuenta).
- Completar la §4 de arc42 con tácticas concretas por escenario (hoy son principios genéricos).
- Rehacer la matriz comparativa contra las ramas del árbol de utilidad, escenario por escenario.
- Enlazar el ADR desde `aspectos.md` y desde el escenario que lo motiva (hoy ningún archivo lo enlaza).
- README: documentar el comando único de arranque (existe `run.py`, no se menciona).
- Título del ADR como decisión («Usar monolito modular») y pasarlo de «Propuesto» a «Aceptado».
- `docs/IA.md` debe ser el registro de uso de IA con aceptado/rechazado; hoy describe la estrategia del producto.
- Contribución: `Julian Samuel Cabeza Pena` sigue sin aparecer en el historial; 2 de 3 integrantes contribuyen antes del corte 1.

## Estado del contrato del repositorio

Ver la matriz transversal arriba.
