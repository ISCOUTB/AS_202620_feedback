# Planilla de equipo · Verifacts

## Identificación

| | |
|---|---|
| Equipo | Verifacts |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Integrantes y su usuario de GitHub | Ver [EQUIPOS.md](../../../EQUIPOS.md); historial actual: `PedroC1213` (240 commits, dos correos consolidados) y `Cristian Cardeño` (31 commits, dos correos con la misma firma), sin correspondencia individual confirmada; falta una tercera identidad atribuible. |
| URL del sistema desplegado | `https://verifacts-web.onrender.com` · API: `https://verifacts-api.onrender.com` (pendiente de comprobación externa fechada) |
| Ultima revision | 2026-09-24 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 8 | S8 | `ef48c08` (2026-09-23T21:28:43-05:00) | 10/12 | 4.3 (propuesta preliminar) | sí (actualizada) |
| 7 | S7 | `635f9b7` (2026-09-16T00:52:52-05:00) | 8/10 | 4.2 (prelim.) | si |
| 6 | S6 | `5941c33` (2026-09-12T02:00:20-05:00) | 8/8 | 5.0 (prelim.) | si |
| 1 | S1 | `(sin commits)` () | sin actividad | no aplica | si |
| 2 | S2 | `(sin commits)` () | sin actividad | no aplica | si |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `8259b75` · 2026-08-23T23:50:00-05:00 | 4/9 | no se publica | sí |
| 4 | Evidencia S4 · arc42, C4 y corte vertical | `443e908` · 2026-08-29T18:17:18-05:00 | 7/10 | 3.8 | sí |
| 5 | CORTE1 | `67f8cea` (2026-09-09T16:30:01-05:00) | 8/12 | 3.7 | si |

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
| Incluir a Julian Samuel Cabeza Pena en README.md y Equipo.md y evidenciar su contribución en el historial. | S5 | si | |
| Contrastar correcciones.md con los hallazgos S1-S4. | S5 | si | |
| Aportar run de CI en verde para el hash calificado. | S5 | si | |
| Cerrar A-02 con prueba de modificación de regla. | S5 | si | |
| Actualizar glosario, vista de bloques, C4 de componentes y enlaces rotos. | S5 | si | |
| Medición formal de P95 para Q-01 (docs/escenarios-de-calidad.md la declara pendiente). | S7 | si | |
| Prueba de usuario 4 de 5 para Q-04 (declarada pendiente). | S7 | si | |
| Prueba automatizada de componente para el frontend: la fila A-04 solo tiene verificación manual. | S7 | si | |
| Marcador de CI en la fila A-00 de docs/aspectos.md, que el propio documento pide reemplazar por la URL real. | S7 | si | |
| Contradicción sobre Q-03 entre docs/escenarios-de-calidad.md ('Pendiente') y docs/aspectos.md A-02 (prueba en verde). | S7 | si | |
| Evidencia de run del pipeline y URL pública de SonarCloud con Quality Gate. | S7 | si | |
| Filas A-04 y A-05 en docs/aspectos.md (b5d9068, 2026-09-16T00:51:03-05:00) | S6 | no (resuelto tarde) | — |
| ADR-0003 y especificación OpenAPI del API (fa29e9a y f3caf45, 2026-09-16) | S6 | no (resuelto tarde) | — |
| Pruebas de contrato de endpoints (9fdf092, 2026-09-16T00:47:30-05:00) | S6 | no (resuelto tarde) | — |
| Actualizaciones de README (8e24d72 y 635f9b7, 2026-09-16) | S6 | no (resuelto tarde) | — |
| pyyaml y jsonschema en requirements (2bf64ca, 2026-09-16) | S6 | no (resuelto tarde) | — |
| Ajustes de vistas de bloques y ejecución y de decisiones (3d07ec5, 122273b, 89b1928, 2026-09-16) | S6 | no (resuelto tarde) | — |
| Evidencia de CI con URL de run para el hash revisado | S6 | si | |
| URL pública de SonarCloud con estado del Quality Gate | S6 | si | |
| Entrada de lo rechazado con motivo técnico en docs/ia.md | S6 | si | |
| Reemplazo del marcador [PENDIENTE] en A-00 y fila propia para A-04 | S6 | si | |
| Commits del tercer integrante declarado | S6 | si | |
| Enlaces del README a documentos inexistentes | S6 | si | |
| Medición de P95 (Q-01) y prueba de usuario (Q-04) | S6 | si | |
| Comprobar URL y /health con hora y código de respuesta. | S8 | si | |
| Aportar run de CI en verde y URL pública de SonarCloud con Quality Gate. | S8 | parcial | Los runs de Tests y SonarCloud del hash actual están en verde y la URL es pública, pero el propio documento declara el Quality Gate general en rojo. |
| Actualizar arc42 §7 con una caja por pieza y su ubicación de ejecución. | S8 | no (resuelto) | La sección muestra web, API y SQLite dentro de Render, además de las piezas del CI. |
| Añadir límite de costo y restricción de tarjeta en arc42 §2. | S8 | no (resuelto) | R-TEC-05 recoge costo cero y ausencia de tarjeta. |
| Registrar un ADR por decisión de plataforma con alternativa descartada y capa gratuita verificada. | S8 | no (resuelto) | ADR 0004 decide Render y compara Terraform y AWS Lambda. |
| Asociar la métrica /metrics a un escenario de calidad y completar la medición de P95. | S8 | parcial | La métrica ya está ligada a Q-01; la medición formal del P95 sigue pendiente. |
| Cerrar los huecos de docs/aspectos.md y corregir las secciones 3 y 10 desactualizadas. | S8 | si | |
| Incluir un integrante declarado que aún no aparece en el historial. | S8 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_Verifacts` respondió al clon público sin autenticación el 2026-09-24. |
| Estructura mínima | Cumple | Las seis rutas están presentes; el glosario está numerado como sección 12. |
| Convención de nombres de ADR | Cumple | Cuatro ADR con nombres `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados sin reescribir | No cumple | el ADR aceptado fue modificado, borrado y recreado |
| `docs/ia.md` al día | Cumple | Entrada del 22–23 de septiembre sobre despliegue, observabilidad y decisiones aceptadas/descartadas. |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep y `.env` sin coincidencias |
| Contribución de todos los integrantes | No cumple | dos personas visibles; el tercer integrante sigue sin commits |
| Pipeline en verde | Cumple | Tests y SonarCloud concluyeron `success` para `ef48c08`; el Quality Gate general documentado en rojo sigue como no conformidad transversal. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Cristian David Cardeno Gulloso | `Cristian Cardeño` (sin atribuir por parecido de nombre) | 31 | | | Dos correos con la misma firma; correspondencia individual pendiente. |
| Pedro Jose Castro Blanquicett | sin atribuir (`PedroC1213` en el historial, dos correos consolidados) | 240 | | | — |
| Julian Samuel Cabeza Pena | sin aparición | 0 | | | — |

## Preguntas abiertas para la sustentación

- ¿Qué cuentas de GitHub corresponden a los integrantes que no aparecen en el historial?
- ¿El esqueleto arranca con `python run.py` y la prueba `pytest tests/` pasa en el entorno del equipo? (no ejecutado por regla del kit; el README no lo documenta)
- ¿Por qué se borraron y recrearon los documentos a las 00:xx del 24-ago, después del cierre? ¿Cuál es la versión canónica?
- ¿Dónde está el run de CI que verifica `tests/test_health.py` en verde? La URL citada en `docs/aspectos.md` (run 33235835069) devuelve 404 y la API no reporta runs del repositorio.
