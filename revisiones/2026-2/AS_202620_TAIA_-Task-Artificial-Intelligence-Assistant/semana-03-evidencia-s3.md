# Evidencia S3 · TAIA

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `46257a03d1fd6804739216ee8a32282e890c60e7` · 2026-08-23T16:47:00-05:00 (último commit ≤ cierre 2026-08-24T05:00Z) |
| Fecha/hora de revisión | 2026-08-23T21:35-05:00 (ANTES del cierre) |
| Comandos | clon efímero con `--filter=blob:none --no-checkout`; lecturas con `git -C "$DIR" show "$HASH:…"`; sin ejecutar código del estudiante. Si el equipo empuja antes de medianoche, el hash calificado puede cambiar. |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/arc42-template-EN.md:250-306` | Cumple | 4.1-4.3: monolito modular + hexagonal selectivo; tabla de Quality-Driven Strategy liga S1-S5 a mecanismos concretos (autorización centralizada, puertos/adaptadores, módulo de recordatorios separado). |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/adr/0001.md:1-41` | Cumple | Tabla capas/hexagonal/monolito modular contra S1-S5 del árbol (`docs/calidad/arbol_utilidad.md`) con justificación por escenario, no tabla genérica. Está en el ADR, no en arc42: se acepta, la ficha no exige ubicación. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001.md` | No cumple | `0001.md` no sigue `NNNN-titulo-en-kebab-case.md` (filtro §4 del CONTRATO). |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001.md` (89 líneas) | No cumple | Sin título H1 que enuncie la decisión y sin sección de contexto; sí hay opciones (matriz + beneficios/costos), decisión y consecuencias. |
| Alternativas descartadas con su motivo | `docs/adr/0001.md:53-63, 88-89` | Cumple | Microservicios descartado explícitamente con motivo; hexagonal completo rechazado en «Costos aceptados»; capas queda implícito en la matriz. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md:6,26`; `docs/calidad/escenarios_calidad.md` | No cumple | `aspectos.md` enlaza a `adr/0001-estilo-arquitectonico.md` (no existe; el archivo es `0001.md`) y al escenario con `ruta/al/escenario.md` (placeholder). `escenarios_calidad.md` no enlaza al ADR. El README repite el enlace roto. |
| Arranque con un solo comando documentado en el README | `README.md` («.\run.bat» desde la raíz); `run.bat` presente | Cumple | `run.bat` contiene `python -m uvicorn backend.app.main:app --reload`. Ejecución real: **No verificado** (regla del kit: no se ejecuta código del estudiante); comando anotado. |
| Prueba automatizada en verde | `backend/tests/test_entrega3.py` (test_health) | No verificado | La prueba existe, pero no hay `.github/workflows/` (sin CI) y el repo no aporta evidencia de ejecución local. Haría falta un run de pipeline o captura de `pytest` con resultado. |
| Estructura de paquetes correspondiente al estilo del ADR | `backend/app/modules/{academic,ai,reminders}/{domain,application,adapters}/` | Cumple | Coincide con el ADR: monolito modular con organización hexagonal selectiva (domain/application/adapters por módulo). |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clonado sin autenticación; nombre `AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant`. |
| Estructura mínima presente | Cumple | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` en el hash calificado. |
| Estado calificado identificable | Cumple | `46257a03` · 2026-08-23T16:47:00-05:00, último commit ≤ cierre; sin etiqueta (evidencia semanal). |
| Nombres de ADR según la convención | No cumple | `docs/adr/0001.md` no pasa el filtro `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$`. |
| ADR aceptados no reescritos | Cumple | `git log --follow -- docs/adr/0001.md` → un solo commit (`decaa36`, 2026-08-22), sin reescrituras posteriores. |
| `docs/ia.md` al día para la semana | No cumple | Commits dentro del periodo (`e977adb` 08-23), pero la Entrada 03 (ClaudeCode, 08-23) está incompleta: sin «Aceptado» ni «Rechazado o modificado». |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 sin coincidencias; sin `.env` versionado. |
| Contribución de todos los integrantes | Cumple | 4 identidades consolidadas: val (2 correos), dei0811, luis20072002, mark = los 4 integrantes del equipo. |

## Recuento

**5 de 9** criterios de la ficha cumplidos. La nota la fija el profesor.

## No verificado / pendientes

- Ejecución real del arranque (`.\run.bat`): no ejecutado por regla del kit; comando documentado y archivo presente.
- Test en verde: sin CI y sin evidencia de ejecución aportada.
- Pipeline: no hay `.github/workflows/`; se espera desde el segundo corte.

## Hallazgos para la planilla

- Renombrar el ADR a `0001-…-en-kebab-case.md` y corregir TODOS los enlaces rotos (`docs/aspectos.md`, `README.md`, escenario en `docs/calidad/escenarios_calidad.md`).
- El ADR no tiene título H1 ni contexto; completar también la Entrada 03 de `docs/ia.md` (aceptado/rechazado).
- Sin CI: montar workflow para que la prueba corra en cada push.
