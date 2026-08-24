# Evidencia S3 · ShareU

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `0833272a568fa1bd2fb2c4a2b805250841006662` · 2026-08-23T22:46:30-05:00 (`README.md`) |
| Fecha/hora de revisión | 2026-08-24 (posterior al cierre 2026-08-24T05:00:00Z) |
| Revisión actualizada tras el cierre | el equipo empujó después de la primera revisión (que no encontró commits nuevos de S3); hash calificado definitivo `0833272`, último commit ≤ cierre. Sin commits posteriores al cierre. |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until=2026-08-24T05:00:00Z`; `git ls-tree`; `git show`; `git grep`. Sin API de CI (no hay `.github/workflows/`). |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42-template-EN.md` §Solution Strategy: decisión motivada por el escenario de usabilidad, módulos resultantes y tácticas por atributo (tabla en el ADR, sección «Tácticas seleccionadas») | Cumple | La estrategia está ligada al escenario priorizado (usabilidad, <3 interacciones) y a los objetivos de calidad; las tácticas con su costo viven en el ADR y la sección 4 las referencia. No es descripción abstracta del estilo. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/arc42-template-EN.md` §Solution Strategy: tabla capas / hexagonal / monolito modular con filas Frontera, Atributo que favorece, Costo, Se rompe cuando y «Ajuste a ShareU» | Cumple | Compara contra el escenario y los objetivos del equipo con juicios concretos, no genéricos. Observación: no hay árbol de utilidad formal en el repo (arrastre de S2); la comparación se apoya en el escenario de `docs/aspectos.md` y en los quality goals. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | Pasa el filtro. El título («Estilo arquitectónico de ShareU») enuncia el tema, no la decisión con verbo. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-estilo-arquitectonico.md`: Contexto, Decisión, Alternativas consideradas, Consecuencias (+ Tácticas, Referencia) | Cumple | Contexto liga el escenario de usabilidad y los dominios del sistema; consecuencias con ganancias, riesgos asumidos y puertas abiertas (extracción futura de búsqueda). |
| Alternativas descartadas con su motivo | ídem: capas («descartada»: cambios transversales al crecer el dominio) y hexagonal («descartada por ahora»: indirección y curva de aprendizaje no sostenibles en esta fase) | Cumple | Motivos concretos y con criterio de reapertura para hexagonal. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md` (escenario de usabilidad, sin enlace al ADR); la sección 4 y el ADR sí se referencian entre sí | No cumple | Ni `aspectos.md` ni el escenario enlazan al ADR; además `aspectos.md` sigue sin la tabla de 8 columnas del curso. |
| Arranque con un solo comando documentado en el README | `README.md` termina en el encabezado «## Esqueleto ejecutable — arranque» **sin ningún comando debajo**; no hay `requirements.txt` ni `pyproject.toml` que declare fastapi | No cumple | La sección de arranque está vacía y no hay manifest de dependencias: el esqueleto no se puede instalar/arrancar siguiendo el repo. Ejecución: no aplica (no hay comando declarado). |
| Prueba automatizada en verde | `tests/test_esqueleto.py` (health + montaje de los 5 módulos) | No verificado | La prueba existe, pero no hay `.github/workflows/` ni evidencia de ejecución aportada. Haría falta un run de CI o la evidencia de Moodle. |
| Estructura de paquetes correspondiente al estilo del ADR | `app/{usuarios,documentos,busqueda,calificaciones,administracion}/router.py` + `app/main.py` montando los cinco routers | Cumple | Los cinco módulos del ADR existen con su router y frontera declarada; `main.py` es el composition root. |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, nombre de convención y público | Cumple | clon sin autenticación de `github.com/ISCOUTB/AS_202620_ShareU`. |
| Estructura mínima presente | No cumple | Faltan `docs/arc42/` (la plantilla sigue en `docs/arc42-template-EN.md`) y `docs/c4/`; presentes `docs/adr/`, `docs/aspectos.md`, `docs/ia.md`, `README.md`. |
| Estado calificado identificable | Cumple | Sin etiquetas; hash `0833272` `2026-08-23T22:46:30-05:00`, último ≤ cierre. |
| Nombres de ADR según la convención | Cumple | `ls docs/adr` sin salida en el filtro. |
| ADR aceptados no reescritos | Cumple | Historial del ADR: creación (`66a8988`) y ajuste (`ef884f8`), ambos el 23-ago antes de la aceptación/cierre; sin reescrituras posteriores. |
| `docs/ia.md` al día para la semana | No cumple | Se actualizó en S3 (`2f55a7b`) con dos entradas, pero sin la columna de qué se rechazó y por qué; ambas entradas quedan con estado «Pendiente de revisión por el equipo». |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 sin coincidencias (exit 1); sin `.env` versionado. |
| Contribución de todos los integrantes | No cumple | 3 identidades / 4 integrantes: Dayana 19 · Nicolas-HH 8 · steven 1. Luis Carlos Corredor Altamiranda sigue sin aparición en el historial. |

## Recuento

**6 de 9** criterios cumplidos.

## No verificado / pendientes

- Prueba en verde: sin pipeline ni evidencia de ejecución; haría falta el run de CI o la evidencia de Moodle.
- Ejecución real del arranque: no aplica — el README no tiene comando declarado.

## Hallazgos para la planilla

- El empujón de última hora trajo casi toda la S3: ADR 0001 con alternativas descartadas, sección Solution Strategy con matriz contextualizada y tácticas por atributo, esqueleto FastAPI con los cinco módulos del ADR y prueba automatizada.
- Huecos concretos: la sección de arranque del README quedó vacía (solo el encabezado) y no hay manifest de dependencias (fastapi no está declarado en ningún archivo).
- Sin enlaces al ADR desde `aspectos.md` ni desde el escenario que lo motiva; `aspectos.md` sigue sin la tabla de 8 columnas.
- Estructura mínima incompleta: falta `docs/arc42/` (plantilla suelta en `docs/`) y `docs/c4/`.
- `docs/ia.md` sin columna de rechazados; las entradas de S3 están «pendientes de revisión».
- Un integrante sigue sin aparecer en el historial (3 identidades para 4 integrantes).
- Sin commits posteriores al cierre.
