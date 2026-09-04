# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo a lo largo del semestre.

## Identificación

| | |
|---|---|
| Equipo | uniTeam |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Integrantes y su usuario de GitHub | Julio Cesar Emiliani Ramos (commits con nombre propio) · Ian Novoa Carrillo (firma «Ian Novoa», correo omitido; la cuenta `iansx` del listado no aparece) · Juan Jose Bustamante More (sin commits atribuibles) · Daniel Isaac Manjarres Herrera (sin commits atribuibles). `super-gremlin` (noreply) sin atribuir a persona. |
| URL del sistema desplegado | sin URL (sin despliegue todavía) |
| Ultima revision | 2026-09-03 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `4b4c5c0` · 2026-08-09T11:22:38-05:00 | 6/9 | 3.7 (propuesta) | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `ca7726a` · 2026-08-16T13:01:06-05:00 | 9/9 | 5.0 (propuesta) | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `ca44917` · 2026-08-23T13:38:40-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `dc14298` (2026-08-29T11:49:10-05:00) | 6/10 | 3.4 | si |
| 5 | Primer corte · reto de línea base | HEAD `dc14298` (sin etiqueta) | 1/12 | subtotal técnico preliminar 0,60/4,00; sustentación pendiente | revisión manual preliminar 2026-09-03 |
| 6 | Evidencia S6 · Contextos delimitados y propiedad de datos | | | no aplica | |
| 7 | Evidencia S7 · Contrato de API y prueba de contrato | | | no aplica | |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | | | no aplica | |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 9 | Evidencia S9 · Generación verificada y trazable | | | no aplica | |
| 10 | Segundo corte · reto aplicado sobre el MVP | `corte-2` | | | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Cuenta `super-gremlin` sin atribuir a persona y 2 integrantes sin commits atribuibles | S1 (y S2) | sí | urgente: la contribución individual se califica sobre el historial en el proyecto final (S3: solo Ian Novoa firmó commits) |
| `docs/aspectos.md` sin la tabla de 8 columnas del curso (S1: sin tabla; S2: tabla propia de 6 columnas sin C4/ADR/Código/Pruebas/Evidencia) | S1 | sí | ajustar a las 8 columnas; en S3 además falta enlazar el ADR-003 desde la tabla |
| Ficha sin tensiones de calidad | S1 | sí | añadir las dos tensiones enfrentadas |
| Nombres de ADR fuera de convención (`ADR-00N-…`, el 003 con « (1)») | S3 (23-ago) | sí | renombrar a `NNNN-titulo-en-kebab-case.md`; marcar ADR-001 como reemplazado por ADR-002 |
| README sin comando de arranque (solo documenta la prueba) y `requirements.txt` con el paquete inexistente `httpx2` | S3 (23-ago) | sí | documentar `uvicorn` y corregir dependencias |
| `docs/ia.md` sin entradas del periodo S3 | S3 (23-ago) | sí | registrar el uso de IA de esta semana con rechazados y motivo |
| Prueba sin CI: verde no verificable (solo lo declara el README) | S3 (23-ago) | sí | montar `.github/workflows/` o aportar evidencia de ejecución |
| Confirmar contenido de secciones 9, 10 y 12 de arc42 | S4 | si | |
| Aportar URL de run de CI en verde | S4 | si | |
| Verificar contenido de docs/ia.md | S4 | si | |
| Etiqueta `corte-1` y respuesta explícita a la restricción asignada | S5 | sí | fijar el estado y enlazar diagnóstico, ADR, cambio y evidencia |
| Medición posterior al cambio comparada con la línea base | S5 | sí | existe línea base reproducible, falta el resultado del reto |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_uniTeam`, público |
| Estructura mínima | Cumple | seis rutas presentes |
| Convención de nombres de ADR | Cumple | cinco ADR con nombres `NNNN-titulo-en-kebab-case.md` |
| ADR aceptados sin reescribir | Cumple | ADR 0001 declara reemplazo por 0002; los demás conservan su decisión |
| `docs/ia.md` al día | No cumple | último cambio 2026-08-29, antes del periodo S5 |
| Sin credenciales en el repositorio ni en el historial | Cumple | barridos limpios; menciones de token son identificadores de código |
| Contribución de todos los integrantes | No verificado | identidades suficientes, pero dos no pueden atribuirse sin confirmación docente |
| Pipeline en verde | Cumple | run de HEAD exitoso: `actions/runs/33263993238` |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| super-gremlin (persona sin atribuir) | super-gremlin (noreply) | 15 | — | — | autor principal de S1/S2; el docente debe confirmar a quién corresponde |
| Ian Novoa Carrillo | firma «Ian Novoa» (correo omitido) | 9 | — | — | toda la S3 (ADR-003, matriz, esqueleto) el 23-ago; la cuenta `iansx` del listado no aparece |
| Julio Cesar Emiliani Ramos | firma con nombre propio (correo omitido) | 2 | — | — | S2 |
| Juan Jose Bustamante More | — | 0 | — | — | sin commits atribuibles |
| Daniel Isaac Manjarres Herrera | — | 0 | — | — | sin commits atribuibles |

## Preguntas abiertas para la sustentación

- ¿A quién corresponde la cuenta `super-gremlin`? Con eso se cierra el contraste de contribución.
- ¿Qué pasó con el proyecto anterior cuyos artefactos se borraron del repo (historial público)?
- ¿El esqueleto arranca y la prueba pasa en el entorno del equipo? (no ejecutado por regla del kit; el README no documenta el arranque y `requirements.txt` trae el paquete inexistente `httpx2`)
