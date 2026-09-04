# semana-05-corte1 · Clubs UTB

> Revisión manual preliminar completa realizada el 2026-09-03, antes del cierre. El equipo puede modificar el repositorio y la evaluación definitiva debe repetirse después de `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado preliminar revisado | `91323d6b4e4cfccbc66add5802b29f100dc34be6` (`2026-08-30T23:21:56-05:00`) |
| Referencia | `HEAD`; no existe la etiqueta `corte-1` |
| Cierre | `2026-09-07T05:00:00Z` |
| Revisor | revisión manual local, solo lectura; no se ejecutó código |

No hay commits desde el inicio de S5 (`2026-08-31T05:00:00Z`). La restricción asignada y el PDF de Moodle no estuvieron disponibles.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` sin salida; `HEAD` `91323d6b`, anterior al inicio de S5 | No cumple | Se usa `HEAD` como estado preliminar. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | El adjunto de Moodle no está disponible en el kit | No verificado | Debe comprobarse en Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | La sección de decisiones declara pendiente formalizar el manejo del fallo de BD (`docs/arc42/09_decisiones_de_diseno.md:13-15`) | No cumple | No existe diagnóstico S5; además se desconoce la restricción asignada. |
| Línea base medida y verificable antes del cambio | U2 define el objetivo, pero el repositorio no aporta resultado inicial con herramienta y procedimiento | No cumple | Falta línea base medida. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo existe `docs/adr/0001-hexagonal.md`; `docs/arc42/09_decisiones_de_diseno.md:15` exige un futuro ADR-0002 | No cumple | El ADR del reto no fue creado. |
| Cambio implementado y ejecutable de extremo a extremo | `README.md:90` declara que no hay desarrollo de código activo; no hay commits S5 | No cumple | No se implementó un cambio del reto. |
| Límites declarados conservados tras el cambio | No hay cambio S5 que contrastar con el C4 | No verificado | Requiere primero identificar e implementar el cambio. |
| Prueba que cubre el cambio, en verde en el pipeline | `backend/tests/test_health.py`; run base exitoso `33356832664` para `91323d6b` | No cumple | El run cubre el health check de la línea base, no un cambio S5. |
| Resultado contrastado con el umbral del escenario y reproducible | No existe medición S5 en el repositorio | No cumple | Falta herramienta, carga, procedimiento y resultado. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md:26-33` tiene ocho columnas, pero omite `Evidencia` y mantiene múltiples celdas “Pendiente” | No cumple | La fila U2 llega a una prueba base, no a evidencia de calidad del reto. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md:7-14` solo registra S1–S4 | No cumple | Falta entrada S5. |
| Sustentación del reto | Requiere la sesión de sustentación | No verificado | Lo fija el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `github.com/ISCOUTB/AS_202620_Clubs_UTB` completado | Cumple | Nombre y visibilidad comprobados por Git. |
| Estructura mínima presente | Seis rutas del contrato presentes en `91323d6b` | Cumple | Estructura completa. |
| Estado calificado identificable | `HEAD` `91323d6b4e4cfccbc66add5802b29f100dc34be6`, `2026-08-30T23:21:56-05:00` | Cumple | Estado preliminar identificable; falta la etiqueta. |
| Nombres de ADR según la convención | `docs/adr/0001-hexagonal.md` | Cumple | Nombre conforme. |
| ADR aceptados no reescritos | ADR aceptado el 2026-08-23; historial muestra modificación posterior `c6c46e3` del 2026-08-30 | No cumple | Un ADR aceptado fue reescrito sin reemplazo. |
| `docs/ia.md` al día para la semana | Última entrada S4 (`docs/ia.md:9-14`); no hay commit S5 | No cumple | Falta S5. |
| Sin credenciales en el repositorio ni en el historial | `git grep`, `.env` y búsqueda histórica de clave privada sin coincidencias | Cumple | Comprobado sobre HEAD e historial. |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: cuatro personas consolidadas; dos firmas pertenecen a la misma identidad | Cumple | Coincide con cuatro integrantes; no se publican correos. |

## Estado global del proyecto (overall · HEAD)

- **HEAD revisado:** `91323d6b4e4cfccbc66add5802b29f100dc34be6`, anterior al inicio de S5.
- **Veredicto:** línea base conservada; no existe entrega técnica S5 en el repositorio.
- El README documenta arranque y pruebas (`README.md:97-116`) y el pipeline base terminó en verde.
- El sistema todavía no implementa el escenario de fallo de base de datos que la propia documentación deja pendiente (`docs/arc42/09_decisiones_de_diseno.md:15`).
- La tabla de aspectos carece de Evidencia y mantiene cinco de seis filas con código o pruebas pendientes (`docs/aspectos.md:28-33`).

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sin evidencia | 0,00 | No hay commits ni diagnóstico S5. |
| Alternativas y decisión | Sin evidencia | 0,00 | No existe ADR del reto. |
| Aplicación sobre el corte vertical | Sin evidencia | 0,00 | No hay cambio S5. |
| Pruebas, medición y trazabilidad | Sin evidencia del reto | 0,00 | El run verde cubre solo la línea base. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico verificable** |  | **0,00 / 4,00** | No constituye total sobre 5,00. |

## Recuento

**0 de 12 criterios Cumple.** Revisión preliminar; no se propone total sobre 5,00 sin sustentación.

## No verificado

- Restricción asignada y correspondencia del diagnóstico.
- PDF adjunto en Moodle.
- Conservación de límites tras un cambio inexistente.
- Sustentación.

## Hallazgos

- No existe etiqueta `corte-1` ni commits S5.
- Falta diagnóstico, ADR, implementación y medición del reto.
- La tabla de aspectos no llega a evidencia de calidad.
- El pipeline base está verde, pero no prueba un cambio del reto.
- El ADR aceptado fue editado después de su aceptación.

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada y por qué no aparece una respuesta a ella en el repositorio?
2. ¿Qué cambio concreto iban a aplicar al corte vertical y qué ADR registra sus alternativas?
3. ¿Cómo medirán el estado inicial y el resultado contra el umbral del escenario elegido?
