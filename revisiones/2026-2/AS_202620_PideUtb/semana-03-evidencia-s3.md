# Evidencia S3 · PideUtb

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `b5f03107acc0c247536a31df9f6b0387d60c857e` · `2026-08-23T19:42:42-05:00` («Entrega 3: arc42 sección 4, matriz comparativa, ADR 0001 y esqueleto ejecutable (monolito modular)») |
| Cierre S3 | 2026-08-24T05:00:00Z (medianoche Colombia). Revisión hecha **antes** del cierre: si el equipo empuja antes de medianoche, el hash calificado puede cambiar |
| Fecha/hora de revisión | 2026-08-23 ~23:00 UTC-5 |
| Comandos | `git clone --filter=blob:none --no-checkout`; `git log -1 --until=2026-08-24T05:00:00Z`; lecturas con `git show H:ruta` y `git grep H` |
| API de GitHub | No usada (sin `.github/workflows/`) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `arc42.md:275-364` §4: estilo elegido en 4.2, motivación por objetivo de calidad en 4.3, consecuencias estructurales en 4.4 | No cumple | La estrategia está bien explicada, pero la motivación de §4.3 se liga a **atributos** del árbol de utilidad (usabilidad, confiabilidad) y no a los **escenarios priorizados** (ESC-01/02/03, prioridad A/M), y no hay tácticas con medida por escenario como exige la ficha |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/comparativa-arquitectura.md:30-55` puntúa capas 20, hexagonal 19, monolito modular 24 sobre criterios de ingeniería | No cumple | Los criterios (testing, acoplamiento, curva de aprendizaje, despliegue Vercel) son contextuales del proyecto, pero **no son los escenarios del árbol de utilidad**: ninguna fila dice qué escenario (ESC-XX) mejora o empeora con cada estilo, que es lo que pide la ficha |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-estilo-arquitectonico.md` (pasa el filtro `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$`) | Cumple | El **título** enuncia el tema («Estilo arquitectónico del backend»), no la decisión («Usar monolito modular»), contra CONTRATO §4 |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-estilo-arquitectonico.md` — Contexto, Alternativas consideradas, Decisión, Consecuencias | Cumple | Contexto con equipo, plazo y tecnologías reales; decisión explícita; consecuencias con riesgos (degeneración del monolito) y ruta de evolución a puerto/adaptador |
| Alternativas descartadas con su motivo | ídem, «Alternativas consideradas» §1 y §2 | Cumple | Capas descartada por acoplamiento negocio-datos; hexagonal por curva de aprendizaje y ceremonia injustificada para el tamaño/plazo |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `git grep adr 9e8281b -- docs/aspectos.md` sin coincidencias; escenarios 10.2–10.6 de `arc42.md` sin enlace; solo `arc42.md:295` (4.2) enlaza el ADR | No cumple | `aspectos.md` no enlaza el ADR en ningún aspecto; el escenario que motiva la decisión no existe como enlace. Además `aspectos.md` no usa la tabla de 8 columnas del curso |
| Arranque con un solo comando documentado en el README | `README.md:23-37`: `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt && uvicorn app.main:app --reload`; soportado por `backend/requirements.txt` y `backend/app/main.py` | Cumple | Comando único con requisitos previos declarados (Python 3.11+) y verificación documentada (`/health`). **Ejecución: No verificado** (regla del kit: no se ejecuta código del estudiante); comando anotado |
| Prueba automatizada en verde | `backend/tests/test_health.py:17-21` (`test_health_check_returns_ok`); sin `.github/workflows/`; sin evidencia de ejecución aportada | No verificado | La prueba existe y es razonable (TestClient de FastAPI), pero el «verde» no se puede comprobar: no hay run de CI ni captura/URL de ejecución en el repo. Haría falta ejecutar `pytest` (prohibido por regla del kit) o que el equipo aporte el run |
| Estructura de paquetes correspondiente al estilo del ADR | `backend/app/pedidos/__init__.py`, `menu/`, `pagos/`, `usuarios/` + `app/main.py` | Cumple | Paquetes vacíos de dominio con docstring que declara la frontera (`backend/app/pedidos/__init__.py:1-7`), coherente con monolito modular |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, nombre de convención y público | clon sin autenticación de `github.com/ISCOUTB/AS_202620_PideUtb` | Cumple | — |
| Estructura mínima presente | ls-tree `b5f0310`: `README.md`, `docs/adr/`, `docs/aspectos.md`, `docs/ia.md` presentes; `arc42.md` en la raíz (desviación); sin `docs/c4/` pero el C4 nivel 1 vive en `arc42.md:217-241` (desviación, no ausencia) | No cumple | 4 rutas exactas; 2 desviaciones de ruta registradas |
| Estado calificado identificable | sin etiquetas (`git tag --list` vacío); `b5f0310` `2026-08-23T19:42:42-05:00` ≤ cierre | Cumple | Revisión anterior al cierre: hash provisional |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico.md` pasa el filtro | Cumple | Título temático, no decisión (ver ficha) |
| ADR aceptados no reescritos | `git log -- docs/adr/` un único commit (`b5f0310`) | Cumple | Creado en la entrega S3, sin reescrituras |
| `docs/ia.md` al día para la semana | commit `b5f0310` toca `docs/ia.md` (2026-08-23) con sección «Uso de IA en la tercera entrega» | No cumple | Actualizado en el periodo, pero sin registrar qué se **rechazó** y por qué |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE` en `b5f0310` sin coincidencias; sin `.env` versionado | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: daniarriet 5 · Santiago Cuesta 4 · Santiago-C0 1 (mismo correo: consolidado 2 personas) | No cumple | 2 de 3 integrantes; no aparece ninguna cuenta atribuible a Ruddy Rodriguez Romero |

Recuento: **5 de 9** criterios cumplidos (1 No verificado). La nota la fija el profesor.

## No verificado / pendientes

- Ejecución del comando de arranque: **No verificado** (regla del kit). Comando declarado: `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt && uvicorn app.main:app --reload` desde `backend/`.
- Prueba en verde: **No verificado** — sin workflow ni evidencia de ejecución aportada; falta un run de `pytest` o CI.
- Nada que dependa de la API de GitHub (sin workflows; no se consumió cupo).

## Hallazgos para la planilla

- La entrega S3 está bien redactada y el esqueleto (paquetes de dominio, prueba base, comando de arranque) es el mejor punto de partida posible para la S4.
- Huecos de la ficha: sección 4 sin tácticas por escenario; matriz comparativa sin filas por escenario del árbol de utilidad; `aspectos.md` sin enlace al ADR y sin tabla de 8 columnas.
- Sigue abierto: estructura (arc42.md en raíz, C4 dentro de arc42, ficha en PDF), `docs/ia.md` sin rechazos, Ruddy sin cuenta en el historial.
