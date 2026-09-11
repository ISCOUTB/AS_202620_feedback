# Planilla de equipo · Verifacts

## Identificación

| | |
|---|---|
| Equipo | Verifacts |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md); historial: `PedroC1213` (30 commits) y `Cristian Cardeño` (4 commits tardíos), sin atribuir oficialmente |
| URL del sistema desplegado | |
| Ultima revision | 2026-09-11 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 6 | S6 | `67f8cea` (2026-09-09T16:30:01-05:00) | 6/8 | 4.0 (prelim.) | si |
| 1 | S1 | `(sin commits)` () | sin actividad | no aplica | si |
| 2 | S2 | `(sin commits)` () | sin actividad | no aplica | si |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `8259b75` · 2026-08-23T23:50:00-05:00 | 4/9 | no se publica | sí |
| 4 | Evidencia S4 · arc42, C4 y corte vertical | `443e908` · 2026-08-29T18:17:18-05:00 | 7/10 | 3.8 | sí |
| 5 | CORTE1 | `3120e06` (2026-09-06T18:36:46-05:00) | 4/12 | no aplica | si |

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
| Etiqueta `corte-1` y respuesta explícita al reto | S5 | sí | falta diagnóstico, ADR, cambio y evidencia del reto asignado |
| Línea base y resultado reproducibles contra umbral | S5 | sí | la documentación reconoce que la medición P95 está pendiente |
| Registro de IA del corte | S5 | sí | último cambio del archivo fue el 24-ago |
| **El repositorio `ISCOUTB/AS_202620_Verifacts` desapareció de la organización** (404 vía API y clon; ausente de los 191 repos públicos listados de ISCOUTB) | S5 (detectado en la revisión definitiva) | sí — crítico | escalado al docente; el equipo debe restablecer el acceso público con el historial intacto antes de que se pueda calificar el corte 1 |
| Limpieza de __pycache__, archivos con sufijos '(3).py'/' (4).py' y data/verifacts.db realizada después del cierre (diff_desde_cierre 3120e06→67f8cea); el PDF en raíz persiste. | S5 | no (resuelto tarde) | — |
| SonarCloud y workflow 'Tests and SonarCloud' añadidos después del cierre (commits a1d23eb, 2a90b44, ab978d3, efbad6b), pero los runs 34407270858 y siguientes fallan. | S5 | no (resuelto tarde) | — |
| Frontend y soporte de URL incorporados después del cierre (commits 5fc30ce, 04d625d, 67f8cea), ampliando el corte vertical. | S5 | no (resuelto tarde) | — |
| Julian Samuel Cabeza Pena sigue sin commits en HEAD. | S5 | si | |
| arc42 incompleto: falta sección 11 (riesgos) y docs/c4/03-componentes.md es plantilla sin completar. | S5 | si | |
| CI en rojo: runs_ci de 'Tests and SonarCloud' posteriores al cierre concluyen failure. | S5 | si | |
| docs/aspectos.md A-02 pendiente y enlaces rotos (docs/decisiones-arquitectonicas.md). | S5 | si | |
| PDF en la raíz del repositorio persiste en HEAD. | S5 | si | |
| Fila A-02 de aspectos.md sin evidencia de prueba | S6 | si | |
| aspectos.md sin relación explícita con contextos del mapa | S6 | si | |
| Posible ADR de reajuste de límites si cambiaron | S6 | si | |
| Integrante declarado sin commits | S6 | si | |
| Evidencia de runs de CI | S6 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | No cumple | el repositorio ya no existe en la organización ISCOUTB (404 vía API/clon; ausente de los 191 repos públicos listados el 2026-09-07); único repo público relacionado por nombre (`PedroC1213/Verifacts`) es un borrador ajeno de agosto, anterior al propio repositorio de curso |
| Estructura mínima | Cumple | las seis rutas presentes (`docs/arc42/`, `docs/adr/`, `docs/c4/`, `aspectos.md`, `ia.md`, README); glosario numerado 11 en vez de 12 |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico.md` |
| ADR aceptados sin reescribir | No cumple | el ADR aceptado fue modificado, borrado y recreado |
| `docs/ia.md` al día | No cumple | sin entrada S5; último cambio 2026-08-24 |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep y `.env` sin coincidencias |
| Contribución de todos los integrantes | No cumple | dos personas visibles; el tercer integrante sigue sin commits |
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
