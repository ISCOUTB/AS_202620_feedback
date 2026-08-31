# Planilla de equipo · Verifacts

## Identificación

| | |
|---|---|
| Equipo | Verifacts |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md); historial: `PedroC1213` (30 commits) y `Cristian Cardeño` (4 commits tardíos), sin atribuir oficialmente |
| URL del sistema desplegado | |
| Última revisión | 2026-08-31 (S4 definitiva, commit `443e908` ≤ cierre) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | HEAD `8ded7cf` (excepción docente) | 4/9 | 2,8 | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | HEAD `8ded7cf` (excepción docente) | 2/9 | 1,9 | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `8259b75` · 2026-08-23T23:50:00-05:00 | 4/9 | no se publica | sí |
| 4 | Evidencia S4 · arc42, C4 y corte vertical | `443e908` · 2026-08-29T18:17:18-05:00 | 7/10 | 3.8 | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Repositorio creado tarde (primer commit 18-ago, después de los cierres de S1 y S2) | S1 | sí | excepción docente aplicada; no repetible |
| El PDF de entrega referencia archivos que no están en el repositorio | S2 | sí | el repositorio es la entrega; subir los escenarios (S3: ya subidos como `docs/arc42/05-escenarios-de-calidad.md`) |
| 2 de 3 integrantes sin aparición en el historial | S1 | sí | urgente antes del corte 1; en S3 solo aparecen `PedroC1213` y `Cristian Cardeño` (tardío) |
| Estructura desviada: `docs/c4-contexto.md` fuera de `docs/c4/`, `docs/IA.md` | S1 | sí | — |
| arc42 §4 con principios genéricos, no tácticas ligadas a los escenarios Q-01…Q-05 | S3 | sí | nombrar tácticas concretas por escenario |
| Matriz comparativa genérica, no contra el árbol de utilidad | S3 | sí | rehacer contra las ramas del árbol, escenario por escenario |
| ADR sin enlazar desde `aspectos.md` ni desde el escenario | S3 | sí | añadir los dos enlaces |
| README sin comando de arranque documentado (existe `run.py`, no se menciona) | S3 | sí | documentar el comando único |
| Título del ADR enuncia el tema, no la decisión; estado «Propuesto» | S3 | sí | «Usar monolito modular», estado aceptado |
| Test sin CI ni evidencia de ejecución (verde no verificable) | S3 | sí | montar `.github/workflows/` o aportar el run |
| **15 commits tardíos** (00:06–00:58 COT del 24-ago, tras el cierre 05:00Z): borrado y recreación de documentos | S3 | sí | respetar el cierre de la actividad; lo tardío no se califica |
| Corte vertical completo (interfaz→lógica→persistencia) y su prueba llegaron el lunes 31-ago 10:00–11:24 COT, después del cierre de S4 | S4 | sí | lo tardío no se califica; sí cuenta como avance para el corte 1 |
| `__pycache__/`, `*.pyc` y archivos duplicados `« (1).py»` versionados; PDFs en la raíz | S4 | sí | limpiar con `git rm`; el `.gitignore` ya se corrigió (tardío) |
| Tabla de aspectos con columnas fuera de las 8 del curso (falta la cadena C4/ADR/código) | S4 | sí | adoptar las 8 columnas y hacer navegable la fila hasta Pruebas |
| CI sin runs verificables: la URL citada en `aspectos.md` da 404 y la API no reporta runs | S4 | sí | aportar el enlace del run o ejecutarlo en la sustentación |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | público y con convención |
| Estructura mínima | Cumple | las seis rutas presentes (`docs/arc42/`, `docs/adr/`, `docs/c4/`, `aspectos.md`, `ia.md`, README); glosario numerado 11 en vez de 12 |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico.md` |
| ADR aceptados sin reescribir | Cumple | creación + renombrado, sin reescritura; estado «Aceptado» |
| `docs/ia.md` al día | Cumple | registro con aceptado/rechazado y motivo; commit dentro del periodo S4 |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep y `.env` sin coincidencias |
| Contribución de todos los integrantes | No cumple | PedroC1213 (110 consolidados) y Cristian Cardeño (12); el tercer integrante sigue sin commits |
| Pipeline en verde | No verificado | `tests.yml` existe pero la API no reporta runs; la URL citada en `aspectos.md` da 404 |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Cristian David Cardeno Gulloso | `Cristian Cardeño` (sin atribuir por parecido de nombre) | 12 | | | commits dentro del periodo S4; los de la madrugada del 24-ago fueron tardíos de S3 |
| Pedro Jose Castro Blanquicett | sin atribuir (`PedroC1213` en el historial, dos correos consolidados) | 110 | | | — |
| Julian Samuel Cabeza Pena | sin aparición | 0 | | | — |

## Preguntas abiertas para la sustentación

- ¿Qué cuentas de GitHub corresponden a los integrantes que no aparecen en el historial?
- ¿El esqueleto arranca con `python run.py` y la prueba `pytest tests/` pasa en el entorno del equipo? (no ejecutado por regla del kit; el README no lo documenta)
- ¿Por qué se borraron y recrearon los documentos a las 00:xx del 24-ago, después del cierre? ¿Cuál es la versión canónica?
- ¿Dónde está el run de CI que verifica `tests/test_health.py` en verde? La URL citada en `docs/aspectos.md` (run 33235835069) devuelve 404 y la API no reporta runs del repositorio.
