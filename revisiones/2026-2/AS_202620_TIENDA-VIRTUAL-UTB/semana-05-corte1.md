# semana-05-corte1 · Tienda virtual UTB

> Revisión DEFINITIVA post-cierre, realizada el 2026-09-07. Reemplaza la revisión manual preliminar del 2026-09-03. Cierre de la actividad: `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | No existe la etiqueta `corte-1`. Se revisó el último commit ≤ cierre: `20ab43f0df750705950895e0ee6e2a11fe3c95f9` (2026-09-06T07:56:34-05:00 = 2026-09-06T12:56:34Z), *"Evidencia S6"*, que también es HEAD |
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log` (fallback, HEAD, ventana S4→HEAD); `git show --stat` del commit "Corte 1"; `git ls-tree` de `docs/adr`; `git grep` (patrón de credenciales, §9); `git shortlog -sne` |
| Revisor | revisión manual local, solo lectura; no se ejecutó código estudiantil |
| `correcciones.md` | No existe en HEAD. Se omite la sección de adjudicación. |

## Qué se hizo en la ventana del corte (S4 → cierre)

```
20ab43f 2026-09-06T07:56:34-05:00 (12:56:34Z)  Evidencia S6            ← último commit ≤ cierre; adelanta trabajo de S6
0d401a9 2026-09-01T09:30:26-05:00 (14:30:26Z)  Corte 1                  ← solo agrega 2 líneas al README
a8c5dcc 2026-08-31T21:21:17-05:00              Corregir S2: objetivos de negocio en arc42 §1 y aspectos para los 4 escenarios
e8ae57d 2026-08-31T21:13:34-05:00              Cerrar trazabilidad escenarios-estilo-ADR y poner al día el registro de IA
e747742 2026-08-31T20:40:06-05:00              arreglos de S4
```
El commit literalmente llamado *"Corte 1"* (`0d401a9`, 2026-09-01) **solo modifica el README en 2 líneas** ("Added a note about the progress related to the first cut"): no toca ADR, código, pruebas ni documentación de aspectos. Después de esa fecha el equipo trabajó en correcciones de S2/S4 y adelantó evidencia de S6, pero nunca volvió a tocar el reto del corte 1.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` → vacío, no hay ninguna etiqueta en el repositorio | No cumple | Se revisó el último commit admisible, `20ab43f` (2026-09-06T12:56:34Z) |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No accesible desde el repositorio | No verificado | Depende del adjunto de Moodle |
| Impacto de la restricción localizado en requisitos, C4 y código | El commit "Corte 1" solo añade una nota al README; ningún documento nombra una restricción nueva | No cumple | Sin indicio de diagnóstico de una restricción nueva en toda la ventana S4→HEAD |
| Línea base medida y verificable antes del cambio | Sin archivo de medición ni cifra en el árbol | No cumple | No hay herramienta ni procedimiento documentado |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `git ls-tree HEAD:docs/adr` → solo `.gitkeep` y `0001-monolito-modular.md` (de la S3) | No cumple | No existe ADR del reto |
| Cambio implementado y ejecutable de extremo a extremo | Ningún commit de la ventana modifica el backend del catálogo | No cumple | El único commit rotulado "Corte 1" es un cambio de 2 líneas en el README |
| Límites declarados conservados tras el cambio | Sin cambio del reto que comparar contra `docs/c4/context.md` / `container.md` | No cumple | No aplica: sin cambio no hay límites que verificar |
| Prueba que cubre el cambio, en verde en el pipeline | Los runs de CI corresponden al corte vertical de S4 (`docker compose`/pytest); ninguno posterior cubre un cambio del reto | No cumple | Sin prueba nueva que ejercite una restricción nueva |
| Resultado contrastado con el umbral del escenario y reproducible | Sin medición en el árbol | No cumple | No hay umbral ni cifra que contrastar |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md` sin fila nueva desde S4; la corrección del 31-ago solo actualizó objetivos de negocio y trazabilidad existente | No cumple | No hay fila del reto que recorrer |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md` actualizado el 31-ago ("poner al día el registro de IA"), antes del commit "Corte 1"; sin entrada posterior referida al reto | No cumple | Ninguna entrada posterior al 31-ago se refiere al reto de este corte |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| a. Repositorio en la organización, con el nombre de la convención y público | `ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB`, clon anónimo exitoso | Cumple | — |
| b. Estructura mínima presente | README.md, docs/arc42, docs/adr (con `.gitkeep`), docs/c4 (context.md, container.md), docs/aspectos.md, docs/ia.md | Cumple | — |
| c. Estado calificado identificable | Sin etiqueta; se usó el último commit ≤ cierre, `20ab43f`, identificable y documentado | Cumple | Identificable pese a no haber etiqueta |
| Versionado (commit anterior al cierre) | No existe `corte-1` | No cumple | Falta el estado versionado exigido por la ficha |
| d. Nombres de ADR según la convención | `0001-monolito-modular.md` cumple el patrón | Cumple | Único ADR del repositorio, de la S3 |
| e. ADR aceptados no reescritos | Sin commits nuevos sobre el ADR en la ventana | Cumple | Sin reescrituras detectadas |
| f. `docs/ia.md` al día para la semana | Última actualización el 31-ago, antes del cierre del corte 1, sin referencia al reto | No cumple | No está al día para el corte 1 |
| g. Sin credenciales en el repositorio ni en el historial | `git grep` (patrón AKIA/BEGIN.../ghp_/xox.../sk-/password/secret/token/api_key) sobre HEAD: sin coincidencias en código; `compose.yaml` mantiene una contraseña de desarrollo local de Postgres, ya señalada en revisiones previas | Cumple, con nota | La contraseña es de un contenedor local de desarrollo, no una credencial real de un servicio externo; se mantiene como observación, no como incidente nuevo |
| h. Contribución de todos los integrantes | `git shortlog -sne HEAD`: RAZOR7150 (8), pxtroniwnl (5), Jasen/Jasen Yukopila (4+3, mismo correo), shalom-A26 (1) — los 4 integrantes declarados | Cumple | Jasen y "Jasen Yukopila" se consolidan como una sola cuenta por el correo |

## Estado global del proyecto (overall · revisado en HEAD)

- **HEAD revisado**: `20ab43f0df750705950895e0ee6e2a11fe3c95f9` (2026-09-06T07:56:34-05:00), *"Evidencia S6"*
- **Veredicto**: con pendientes
- Resumen: entre el cierre de S4 y el cierre del corte 1 el equipo corrigió pendientes de S2 y S4 (objetivos de negocio, trazabilidad escenario-estilo-ADR, registro de IA) y luego adelantó trabajo de la semana 6, pero el commit específicamente rotulado "Corte 1" es un cambio cosmético de 2 líneas en el README. No hay ninguna señal, en todo el rango revisado, de que se haya trabajado el reto de este corte: ni restricción diagnosticada, ni ADR, ni cambio de código, ni medición.

Pendientes que siguen abiertos:
- Resolver el reto del corte 1: diagnóstico con línea base medida, ADR con alternativas y consecuencias, cambio implementado y medición contra umbral.
- Crear la etiqueta `corte-1` sobre el commit que efectivamente resuelva el reto.
- Completar `docs/aspectos.md` con las 8 columnas del contrato (pendiente desde S1/S4).
- Configurar SonarCloud en el pipeline (solo corre pytest hoy).
- Registrar en `docs/ia.md` los usos de IA del corte 1, con al menos un rechazo y su motivo técnico.

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia evaluable del reto | 0,00 | El único commit rotulado "Corte 1" es una nota de 2 líneas en el README |
| Alternativas y decisión | Sin evidencia del reto | 0,00 | El único ADR es de la S3 (monolito modular), sin relación con un reto nuevo |
| Aplicación sobre el corte vertical | Sin evidencia del reto | 0,00 | Ningún commit de la ventana toca el backend del catálogo |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | Sin medición ni prueba nueva atribuible al reto |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio |
| **Subtotal técnico verificable** | | **0,00 / 4,00** | No constituye el total sobre 5,00 |

## Recuento

0 de 12 criterios Cumple (2 No verificado, 10 No cumple).

## No verificado / pendientes

- PDF adjunto en Moodle.
- Sustentación del reto.

## Hallazgos para la planilla

- No existe ninguna etiqueta en el repositorio (`git tag --list` vacío); se revisó el último commit admisible, `20ab43f` (2026-09-06T12:56:34Z).
- El commit rotulado "Corte 1" (`0d401a9`) solo agrega 2 líneas al README; no hay ADR, código, prueba ni medición del reto en ningún commit de la ventana.
- El equipo sí corrigió pendientes reales de S2 y S4 (objetivos de negocio, trazabilidad, registro de IA) entre el 31 de agosto y el cierre, y luego adelantó "Evidencia S6" antes de cerrar el corte 1: hay actividad, pero no dirigida al reto.
- Mejora respecto a la preliminar: los 4 integrantes siguen presentes en el historial y no se detectaron credenciales nuevas.
- Contraseña de desarrollo local en `compose.yaml` (Postgres del contenedor), ya señalada en la revisión de S4; se mantiene como observación de higiene, no como hallazgo nuevo.

## Preguntas para la sustentación

1. ¿Qué restricción se les asignó, y por qué el commit rotulado "Corte 1" no contiene ningún diagnóstico, ADR ni cambio de código?
2. Entre el 31 de agosto y el cierre se corrigieron pendientes de S2 y S4 y se adelantó evidencia de S6: ¿por qué el reto del corte 1 no se trabajó en esa misma ventana?
3. ¿Qué cambiaría en el diseño actual (monolito modular, ADR-0001) si tuvieran que responder hoy mismo al reto?
