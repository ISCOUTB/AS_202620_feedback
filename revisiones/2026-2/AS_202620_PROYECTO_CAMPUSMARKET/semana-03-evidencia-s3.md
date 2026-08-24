# Evidencia S3 · CampusMarket

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `4dd857a1e238e50956facd7156b967f03ae30db0` · 2026-08-23T23:54:16-05:00 (`Merge pull request #5 from ISCOUTB/S3-esqueleto-ejecutable`) |
| Fecha/hora de revisión | 2026-08-24 (posterior al cierre 2026-08-24T05:00:00Z) |
| Revisión actualizada tras el cierre | el equipo empujó después de la primera revisión (que vio `9e8281b`); hash calificado definitivo `4dd857a`, último commit ≤ cierre. Sin commits posteriores al cierre. |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until=2026-08-24T05:00:00Z`; `git ls-tree`; `git show`; `git grep`. API de CI usada 1 vez (`actions/runs?per_page=5`). |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/04-estrategia-de-solucion.md` §4.4 (decisión monolito modular) y §4.6 (tácticas por EC-01 a EC-04 con la medida de cada escenario) | Cumple | Tácticas concretas: consultas en el mismo proceso y catálogo (EC-01), validación de propiedad (EC-02), cambios en máx. dos módulos (EC-03), única unidad de despliegue (EC-04). No es descripción abstracta del estilo. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | §4.3 tabla capas / hexagonal / monolito modular × EC-01, EC-02, EC-03, EC-04 con juicios Favorable/Intermedio/Muy favorable por escenario | Cumple | Compara contra los escenarios del equipo con juicios específicos; no es la tabla genérica que la ficha descarta. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-usar-monolito-modular.md` (creado en `dbdd9c4`, incorporado en el merge `4dd857a`) | Cumple | Pasa el filtro; el título enuncia la decisión con verbo. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-usar-monolito-modular.md`: Contexto (§1), Alternativas (§2), Decisión (§3), Justificación (§4), Tácticas y costos (§5), Consecuencias (§6) | Cumple | Contexto liga escenarios y restricciones (EC-03 motivador, R-01/R-02/R-05/R-06); consecuencias positivas y riesgos asumidos. |
| Alternativas descartadas con su motivo | §2.1 (capas) y §2.2 (hexagonal), cada una con «Motivo de descarte» | Cumple | Motivos concretos ligados a EC-03 y al alcance del semestre. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md` ASP-03 → `./adr/0001-usar-monolito-modular.md`; `docs/arc42/10-escenarios-de-calidad.md:67-68` (EC-03 → enlace al ADR) | Cumple | Los dos enlaces existen y apuntan al archivo presente; seguidos sin enlaces rotos. |
| Arranque con un solo comando documentado en el README | `README.md` «Esqueleto ejecutable»: `python -m uvicorn backend.app.main:app --reload` + `backend/requirements.txt` (fastapi, uvicorn, pytest, httpx) | Cumple | Comando único documentado con archivo de soporte. Ejecución real: No verificado por regla del kit (no se ejecuta código del estudiante). |
| Prueba automatizada en verde | `backend/tests/test_health.py` (GET `/health` → 200) + `.github/workflows/backend-tests.yml`; 4 runs «Pruebas del backend» con conclusion `success`, el último creado 2026-08-24T04:54:19Z: https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/32691690794 | Cumple | Prueba automatizada y run en verde dentro del periodo S3, anterior al cierre. |
| Estructura de paquetes correspondiente al estilo del ADR | `backend/app/{usuarios,publicaciones,catalogo,administracion}/__init__.py` + `backend/app/main.py` | Cumple | Los cuatro módulos que declara el ADR existen con su paquete; el frontend (`frontend/campusmarket/`) sigue siendo la plantilla Flutter por defecto, pendiente de modularizar en S4. |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, nombre de convención y público | Cumple | clon sin autenticación de `github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET`. |
| Estructura mínima presente | Cumple | `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`, `README.md` en `4dd857a`. |
| Estado calificado identificable | Cumple | Sin etiquetas; hash `4dd857a` `2026-08-23T23:54:16-05:00`, último ≤ cierre. |
| Nombres de ADR según la convención | Cumple | `ls docs/adr` sin salida en el filtro. |
| ADR aceptados no reescritos | Cumple | Historial del ADR con un único commit (`dbdd9c4`). |
| `docs/ia.md` al día para la semana | No cumple | Último commit 2026-08-16 (periodo S2); sin entradas de S3 (17-23 ago) y sin columna de qué se rechazó y por qué. |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 sin coincidencias (exit 1); sin `.env` versionado. |
| Contribución de todos los integrantes | Cumple | camilixo92 26 · `nilver-garcia` 23 + `Nnigarp` 10 (misma cuenta de GitHub `115980006+…`: 33 consolidados) · Carulla-sd 1 — 3 personas para 3 integrantes. Consolidar la identidad `nilver-garcia`/`Nnigarp` en la planilla. |

## Recuento

**9 de 9** criterios cumplidos.

## No verificado / pendientes

- Ejecución real del arranque: **No verificado** por regla del kit (comando declarado: `python -m uvicorn backend.app.main:app --reload`).

## Hallazgos para la planilla

- La actualización tras el cierre revierte casi todos los huecos de la primera revisión: PR #5 trajo el ADR 0001 completo, el esqueleto backend con los cuatro módulos, el comando único en el README, la prueba y el workflow con 4 runs en verde (el último, run 32691690794, anterior al cierre).
- Arrastre resuelto: ADR enlazado desde `aspectos.md` y desde EC-03; estructura mínima completa; esqueleto con paquetes del ADR; prueba y pipeline en verde.
- Sigue abierto: `docs/ia.md` sin entradas de S3 y sin registro de lo rechazado.
- Observación menor: el frontend sigue siendo la plantilla Flutter por defecto, sin módulos; la estructura del ADR está materializada solo en el backend.
- Sin commits posteriores al cierre.
