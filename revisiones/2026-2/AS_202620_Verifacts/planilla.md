# Planilla de equipo · Verifacts

## Identificación

| | |
|---|---|
| Equipo | Verifacts |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md); historial: `PedroC1213` (30 commits) y `Cristian Cardeño` (4 commits tardíos), sin atribuir oficialmente |
| URL del sistema desplegado | |
| Última revisión | 2026-08-24 (S3 actualizada, commit `8259b75` ≤ cierre) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | HEAD `8ded7cf` (excepción docente) | 4/9 | 2,8 | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | HEAD `8ded7cf` (excepción docente) | 2/9 | 1,9 | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `8259b75` · 2026-08-23T23:50:00-05:00 | 4/9 | no se publica | sí |

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

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | público y con convención |
| Estructura mínima | No cumple | `docs/c4-contexto.md` fuera de `docs/c4/`; `docs/IA.md`; ya existe `docs/arc42/` |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico.md` |
| ADR aceptados sin reescribir | Cumple | un solo commit (`313b6a2`); estado «Propuesto» |
| `docs/ia.md` al día | No cumple | no es registro de uso; sin aceptado/rechazado |
| Sin credenciales en el repositorio ni en el historial | Cumple | — |
| Contribución de todos los integrantes | No cumple | `PedroC1213` (30) y `Cristian Cardeño` (4, tardíos); 1 de 3 sin aparición |
| Pipeline en verde | No verificado | sin `.github/workflows/` ni evidencia de ejecución |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Cristian David Cardeno Gulloso | `Cristian Cardeño` (sin atribuir por parecido de nombre) | 4 | | | todos tardíos (post-corte, 24-ago 00:xx) |
| Pedro Jose Castro Blanquicett | sin atribuir (`PedroC1213` en el historial, 30 commits) | 30 | | | — |
| Julian Samuel Cabeza Pena | sin aparición | 0 | | | — |

## Preguntas abiertas para la sustentación

- ¿Qué cuentas de GitHub corresponden a los integrantes que no aparecen en el historial?
- ¿El esqueleto arranca con `python run.py` y la prueba `pytest tests/` pasa en el entorno del equipo? (no ejecutado por regla del kit; el README no lo documenta)
- ¿Por qué se borraron y recrearon los documentos a las 00:xx del 24-ago, después del cierre? ¿Cuál es la versión canónica?
