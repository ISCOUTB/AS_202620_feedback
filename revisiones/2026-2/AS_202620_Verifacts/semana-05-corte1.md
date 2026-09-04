# Primer corte · reto de línea base arquitectónica · Verifacts

> Revisión manual preliminar completa, realizada antes del cierre. El equipo puede cambiar el repositorio y la valoración debe repetirse después del 2026-09-07T05:00:00Z.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `8764f9f1684560bddb9a61e07ffa0d1249b8199d` (2026-09-02T13:32:53-05:00) |
| Etiqueta `corte-1` | Ausente |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | Revisión manual con Codex, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` no devolvió etiquetas; HEAD `8764f9f` | No cumple | La valoración preliminar usa HEAD. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | `VeriFacts-resumen-entrega-final c1.pdf` tiene una página y describe el incremento S4, no el reto S5 | No verificado | Moodle no está disponible; el PDF versionado no satisface la evidencia solicitada. |
| Impacto de la restricción localizado en requisitos, C4 y código | Los commits S5 corrigen la línea base S4; no hay diagnóstico de una restricción nueva | No cumple | La restricción asignada tampoco está en el kit. |
| Línea base medida y verificable antes del cambio | `docs/arc42/10-requisitos-de-calidad.md:43-53` reconoce que falta la medición P95 | No cumple | No hay cifra inicial con procedimiento ejecutado. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo existe `docs/adr/0001-estilo-arquitectonico.md`, correspondiente a la elección de estilo | No cumple | Falta ADR del reto S5. |
| Cambio implementado y ejecutable de extremo a extremo | `README.md:284-326` y `docs/arc42/06-vista-de-ejecucion.md:58-109` documentan `POST /analysis`, una corrección tardía de S4 | No cumple | No se identifica cambio distinto asociado al reto. |
| Límites declarados conservados tras el cambio | C4 y código describen el corte vertical actual, pero no existe cambio S5 que comparar | No verificado | Requiere identificar el reto y su implementación. |
| Prueba que cubre el cambio, en verde en el pipeline | `tests/test_analysis.py` cubre la base; la consulta pública de Actions devolvió 404 | No cumple | No hay prueba del reto ni run citable. |
| Resultado contrastado con el umbral del escenario y reproducible | La documentación declara pendiente la medición formal (`docs/arc42/10-requisitos-de-calidad.md:43`) | No cumple | Falta resultado y procedimiento ejecutado. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md:22` completa A-03 para la base S4; A-02 queda pendiente en `docs/aspectos.md:21` | No cumple | No existe una fila del reto S5. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md:6-79` contiene decisiones anteriores; último cambio `8ad4574`, 2026-08-24 | No cumple | Falta registro del corte. |
| Sustentación del reto | Requiere la sesión con el equipo | No verificado | Lo fija el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `ISCOUTB/AS_202620_Verifacts` | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | Las seis rutas obligatorias están presentes en HEAD | Cumple | También quedan binarios y duplicados que deben limpiarse. |
| Estado calificado identificable | HEAD `8764f9f`, sin etiqueta `corte-1` | No cumple | En el corte se exige etiqueta. |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | Nombre correcto. |
| ADR aceptados no reescritos | El ADR aceptado fue modificado, borrado y recreado entre `313b6a2` y `d932855` | No cumple | La evolución debió registrarse sin reescribir la decisión aceptada. |
| `docs/ia.md` al día para la semana | Último cambio `8ad4574`, 2026-08-24 | No cumple | Sin registro S5. |
| Sin credenciales en el repositorio ni en el historial | Barridos en HEAD e historial sin patrones de credenciales | Cumple | Sin hallazgos. |
| Contribución de todos los integrantes | Historial consolidado: dos identidades de una persona, una segunda persona y ningún commit del tercer integrante | No cumple | La autoría continúa concentrada. |

## Estado global del proyecto en HEAD

- **Veredicto:** la base S4 mejoró tarde, pero el corte 1 aún no está presentado.
- El repositorio ahora documenta un corte vertical completo con persistencia y su prueba.
- No hay etiqueta, reto, línea base medida, ADR del reto, resultado ni registro de IA S5.
- El PDF versionado tiene una página y corresponde a S4; el CI sigue sin run público citable.

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje preliminar | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Insuficiente | 0,00 | No existe diagnóstico ni línea base medida. |
| Alternativas y decisión | Insuficiente | 0,00 | No hay ADR del reto. |
| Aplicación sobre el corte vertical | Insuficiente | 0,00 | El cambio visible completa S4, no responde a un reto S5. |
| Pruebas, medición y trazabilidad | Insuficiente | 0,00 | Sin run citable, medición ni cadena del reto. |
| Sustentación del reto | Pendiente del docente | — | No verificable desde el repositorio. |
| **Subtotal técnico preliminar** |  | **0,00 / 4,00** | No es la nota final del corte. |

## Recuento

0 de 12 criterios de la ficha cumplen. El recuento no se convierte mediante la fórmula semanal porque este corte tiene rúbrica propia.

## Pendientes y preguntas para la sustentación

- ¿Cuál fue la restricción asignada y dónde está su diagnóstico?
- ¿Qué cambio responde al reto, distinto de completar el corte vertical S4?
- ¿Dónde están la línea base y la medición final reproducibles?
- ¿Dónde está el run de CI del commit evaluado y por qué falta la etiqueta `corte-1`?
