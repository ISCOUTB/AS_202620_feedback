# Evidencia S3 · ROUTB

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `1ed002b23d61201d004f69dd7a6a4b07f71015b4` · `2026-08-23T20:31:54-05:00` («ROUTB - Semana 3») |
| Cierre S3 | 2026-08-24T05:00:00Z (medianoche Colombia). Revisión hecha **antes** del cierre: si el equipo empuja antes de medianoche, el hash calificado puede cambiar |
| Fecha/hora de revisión | 2026-08-23 ~23:00 UTC-5 |
| Comandos | `git clone --filter=blob:none --no-checkout`; `git log -1 --until=2026-08-24T05:00:00Z`; lecturas con `git show H:ruta` y `git grep H` |
| API de GitHub | No usada (sin `.github/workflows/`) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/arc42-template-EN.md:248-260` «Enfoque para alcanzar los objetivos de calidad clave»: tácticas por objetivo priorizado (rendimiento: consultas geoespaciales indexadas ≤2 s; seguridad: hashing con salt + JWT + HTTPS; disponibilidad: backend stateless; usabilidad: flujos ≤3 pasos) | Cumple | Tácticas concretas ligadas a las prioridades del árbol de utilidad, no descripción abstracta del estilo. Matiz: se ligan al objetivo priorizado, no al escenario individual de 10.2 |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/adr/0001-usar-monolito-modular.md` «Matriz de decisión»: capas / hexagonal / monolito modular × los 8 atributos del árbol (rendimiento, seguridad, disponibilidad, escalabilidad, portabilidad, mantenibilidad, privacidad, usabilidad) con Favorece/Neutral/Perjudica y razón | Cumple | Compara contra el árbol del equipo con juicios contextuales (Ley 1581, portabilidad Flutter, cupos). Matiz: por atributo, no por escenario con su medida |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-usar-monolito-modular.md` (pasa el filtro); título «0001 - Arquitectura de monolito modular para el backend de ROUTB» enuncia la decisión | Cumple | Convención y título correctos |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | ídem: Contexto, Decisión (con criterios), Alternativas consideradas, Consecuencias (positivas y negativas/riesgos) | Cumple | Consecuencias incluyen riesgos reales (degeneración a «monolito enredado», fallo global) y trazabilidad en tabla |
| Alternativas descartadas con su motivo | ídem, «Alternativas consideradas»: hexagonal (abstracciones adicionales no necesarias para el alcance) y capas (dificulta trabajo paralelo de 4 integrantes) | Cumple | Motivos específicos del equipo, no genéricos |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md` fila 2 (Organización del backend) → `adr/0001-usar-monolito-modular.md` ✓; `arc42-template-EN.md:380` (§9) y `:255,257` (§4 objetivos) también enlazan. La tabla de escenarios 10.2 **no** enlaza el ADR | No cumple | El enlace desde aspectos.md funciona; falta el segundo: ningún escenario de calidad (10.2) enlaza la decisión que lo motiva (los enlaces de §4 son de objetivo de calidad, no de escenario) |
| Arranque con un solo comando documentado en el README | `README.md`: instalación en 6 pasos separados (clone → cd → venv → activate → pip install) + ejecución en pasos separados (`uvicorn app.main:app --reload`, `pytest`) | No cumple | El comando de arranque existe como paso, pero **no hay un solo comando** documentado como pide la ficha. Archivos soporte presentes: `backend/requirements.txt`, `backend/app/main.py`. Ejecución: No verificado (regla del kit) |
| Prueba automatizada en verde | `backend/tests/test_health.py:5-10` (`test_health_check` con TestClient); sin `.github/workflows/`; sin evidencia de ejecución aportada | No verificado | La prueba existe y es razonable, pero el «verde» no se puede comprobar: no hay run de CI ni URL/captura. Haría falta ejecutar `pytest` (prohibido por regla del kit) o que el equipo aporte el run |
| Estructura de paquetes correspondiente al estilo del ADR | `backend/app/modules/{auth,users,trips,requests,notifications,admin}/` cada uno con `domain/`, `application/`, `adapters/` + `backend/app/shared/` | Cumple | Monolito modular con módulos por dominio y separación interna declarada, coherente con el ADR |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, nombre de convención y público | clon sin autenticación de `github.com/ISCOUTB/AS_202620_ROUTB` | Cumple | — |
| Estructura mínima presente | ls-tree `1ed002b`: `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/context.md`, `docs/aspectos.md`, `docs/ia.md` | Cumple | Las seis rutas presentes |
| Estado calificado identificable | sin etiquetas; `1ed002b` `2026-08-23T20:31:54-05:00` ≤ cierre | Cumple | Revisión anterior al cierre: hash provisional |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md` pasa el filtro | Cumple | — |
| ADR aceptados no reescritos | `git log --follow` del ADR: 2 commits (`df174b9`, `1ed002b`), ambos de construcción en S3 antes de la entrega | Cumple | Sin reescrituras posteriores a la aceptación |
| `docs/ia.md` al día para la semana | commit `1ed002b` (2026-08-23) añade «Semana 3» con qué se aceptó, qué se rechazó y justificación | Cumple | El mejor registro de IA visto en este barrido |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE` en `1ed002b` sin coincidencias; sin `.env` versionado | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: MKeinerrr 20+2 (dos correos, consolidado), diegobrr999-commits 6, juliandmanjarrez-tech 3, junior14700 2 | Cumple | 4 personas para 4 integrantes |

Recuento: **6 de 9** criterios cumplidos (1 No verificado). La nota la fija el profesor.

## No verificado / pendientes

- Ejecución del arranque: **No verificado** (regla del kit). Además el README no documenta un comando único (multi-paso).
- Prueba en verde: **No verificado** — sin workflow ni evidencia de ejecución aportada; falta un run de `pytest` o CI.
- Nada que dependa de la API de GitHub (sin workflows; no se consumió cupo).

## Hallazgos para la planilla

- La entrega S3 es sólida: ADR con alternativas, motivos de descarte y matriz contra el árbol; paquetes de módulos con frontera interna; ia.md con rechazos; estructura mínima completa.
- Arrastre resuelto: `docs/ia.md` (ahora con rechazos, S1→S3), `docs/aspectos.md` (tabla de 8 columnas), escenarios con seis partes y medidas con carga en 10.2, sección 10 poblada.
- Nuevos huecos: enlace del ADR desde el escenario motivador (10.2) ausente; README sin comando único de arranque; sin workflow/evidencia de prueba en verde.
- Pendiente previo: C4 de contexto (ver leyenda/etiquetas, detectado en S2) — verificar si se corrigió en `docs/c4/context.md` actual.
