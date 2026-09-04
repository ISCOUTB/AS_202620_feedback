# Primer corte · reto de línea base arquitectónica · TRACTAR

> Revisión manual preliminar completa, realizada antes del cierre. El equipo puede cambiar el repositorio y la valoración debe repetirse después del 2026-09-07T05:00:00Z.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849` (2026-08-31T12:27:23-05:00) |
| Etiqueta `corte-1` | Ausente |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | Revisión manual con Codex, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` no devolvió etiquetas; HEAD `7cfb872` | No cumple | La valoración preliminar usa HEAD; falta fijar el estado con `corte-1`. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | El adjunto de Moodle no está disponible en el repositorio | No verificado | Debe comprobarse en Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | Los commits posteriores al inicio de S5 (`292aea7`, `7cfb872`) corrigen texto del C4; no aparece un diagnóstico del reto | No cumple | La restricción asignada tampoco está en el kit, por lo que no puede validarse su correspondencia. |
| Línea base medida y verificable antes del cambio | `docs/arc42/arc42.md` declara escenarios y umbrales, pero no presenta una medición del reto con herramienta y procedimiento | No cumple | Un umbral declarado no sustituye el resultado de línea base. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo existen `docs/adr/0001-estilo-arquitectonico.md` y `0002-cambio-stack-fastapi-flutter.md`; ninguno corresponde a un reto S5 | No cumple | Falta un ADR identificable del corte. |
| Cambio implementado y ejecutable de extremo a extremo | Los cambios S5 visibles son documentales; `README.md:13-39` describe el corte vertical de S4 | No cumple | No hay commit atribuible a la respuesta del reto. |
| Límites declarados conservados tras el cambio | `docs/c4/C2.md` y el código muestran la línea base actual, pero no existe un cambio del reto que comparar | No verificado | Requiere identificar primero el cambio evaluado. |
| Prueba que cubre el cambio, en verde en el pipeline | `.github/workflows/ci.yml:28-30` ejecuta pytest; la consulta pública de Actions redirigió y no permitió citar un run del repo evaluado | No cumple | Las pruebas existentes cubren S4, no un cambio del reto. |
| Resultado contrastado con el umbral del escenario y reproducible | No se encontró resultado con herramienta, carga y procedimiento | No cumple | Falta la medición posterior al cambio. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md:72` completa una cadena para A-06, pero corresponde al corte vertical S4 | No cumple | Falta una fila vinculada con el reto S5. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | El último commit de `docs/ia.md` es `e84871f` del 2026-08-16; `docs/ia.md:13` registra trabajo anterior | No cumple | No hay entrada del corte. |
| Sustentación del reto | Requiere la sesión con el equipo | No verificado | Lo fija el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | El clon anónimo desde `ISCOUTB/AS_202620_TRACTAR` respondió; GitHub redirige el proyecto renombrado | Cumple | El nombre conserva el prefijo requerido; conviene actualizar la referencia canónica en EQUIPOS.md. |
| Estructura mínima presente | HEAD contiene `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md` | Cumple | Las seis rutas están presentes. |
| Estado calificado identificable | HEAD `7cfb872`, sin etiqueta `corte-1` | No cumple | En un corte se exige la etiqueta. |
| Nombres de ADR según la convención | `0001-estilo-arquitectonico.md` y `0002-cambio-stack-fastapi-flutter.md` | Cumple | Ambos siguen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | El historial de `docs/adr/` muestra modificaciones posteriores y el cambio de proyecto reescribió decisiones aceptadas | No cumple | Debió declararse reemplazo en un ADR nuevo. |
| `docs/ia.md` al día para la semana | Último cambio `e84871f`, 2026-08-16 | No cumple | Sin registro S5. |
| Sin credenciales en el repositorio ni en el historial | `git grep` en HEAD y `git log -G` histórico sin patrones de credenciales | Cumple | Las menciones a variables son nombres de configuración, no valores. |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` muestra tres identidades consolidadas de una misma persona; tres integrantes no aparecen | No cumple | Falta contribución verificable del resto del equipo. |

## Estado global del proyecto en HEAD

- **Veredicto:** con pendientes.
- El corte vertical y su documentación llegaron después del cierre de S4 y ahora forman una base más completa.
- S5 no presenta etiqueta, diagnóstico, ADR del reto, cambio, prueba específica ni medición.
- El registro de IA sigue desactualizado y la autoría está concentrada en una persona.

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje preliminar | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Insuficiente | 0,00 | No hay diagnóstico ni línea base del reto. |
| Alternativas y decisión | Insuficiente | 0,00 | No existe ADR identificable del reto. |
| Aplicación sobre el corte vertical | Insuficiente | 0,00 | No se identifica un cambio S5. |
| Pruebas, medición y trazabilidad | Insuficiente | 0,00 | No hay prueba específica ni medición contra umbral. |
| Sustentación del reto | Pendiente del docente | — | No verificable desde el repositorio. |
| **Subtotal técnico preliminar** |  | **0,00 / 4,00** | No es la nota final del corte. |

## Recuento

0 de 12 criterios de la ficha cumplen. El recuento no se convierte mediante la fórmula semanal porque este corte tiene rúbrica propia.

## Pendientes y preguntas para la sustentación

- ¿Cuál fue la restricción asignada y dónde está su diagnóstico?
- ¿Qué alternativas se descartaron y por qué?
- ¿Cómo se reproduce la línea base y el resultado posterior?
- ¿Por qué no existe la etiqueta `corte-1` y cómo se distribuyó el trabajo entre los cuatro integrantes?
