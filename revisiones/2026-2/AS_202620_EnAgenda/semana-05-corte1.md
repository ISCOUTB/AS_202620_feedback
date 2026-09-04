# Semana 05 · Primer corte · EnAgenda

> **Revisión manual preliminar completa, previa al cierre.** El cierre es `2026-09-07T05:00:00Z`. El equipo puede cambiar el resultado mientras publique y etiquete evidencia antes de esa fecha.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `1d014016fa875156d4d390bf0d1f164563b3d0ab` · 2026-08-31T00:28:12-05:00 |
| Referencia | `HEAD`, porque no existe la etiqueta `corte-1` |
| Cierre | `2026-09-07T05:00:00Z` |
| Revisor | revisión manual preliminar |
| Restricción asignada | No disponible en el kit; el repositorio tampoco declara un reto de Corte 1 |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` no devuelve `corte-1`; `HEAD` es `1d01401` del 2026-08-31 | No cumple | Deben crear la etiqueta sobre el estado que quieren someter antes del cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Documento adjunto en Moodle | No verificado | El adjunto de Moodle no está disponible en el kit ni en el repositorio. |
| Impacto de la restricción localizado en requisitos, C4 y código | No existe un apartado que declare el reto de Corte 1; `docs/arc42/11-riesgos-y-deuda-técnica.md:81-90` solo registra medición de rendimiento pendiente | No cumple | No se puede afirmar correspondencia con la asignación externa. Falta declarar la restricción y recorrer su impacto. |
| Línea base medida y verificable antes del cambio | `docs/arc42/11-riesgos-y-deuda-técnica.md:81-90` reconoce que la medición de EC-05 está pendiente | No cumple | Hay umbral, pero no cifra inicial obtenida con herramienta y procedimiento. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo existe `docs/adr/0001-usar-monolito-modular.md:1-6`, aceptado el 2026-08-23 como decisión de línea base | No cumple | Falta un ADR propio del reto de Corte 1. |
| Cambio implementado y ejecutable de extremo a extremo | `README.md:52-75` describe el corte vertical de invitaciones de S4; no hay commit ni cambio identificado como respuesta al reto | No cumple | La línea base es ejecutable, pero no demuestra el incremento del corte. |
| Límites declarados conservados tras el cambio | `docs/c4/nivel-2-contenedores.md:8-18` y `README.md:65-75` describen estados distintos de la solución | No verificado | Sin cambio del reto no existe estado posterior que comparar; además, el C4 conserva API y base de datos no presentes en el corte actual. |
| Prueba que cubre el cambio, en verde en el pipeline | CI de `1d01401` en verde: https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/33360647498; `tests/test_invitaciones.py` cubre la línea base | No cumple | El run no contiene una prueba identificada contra un cambio del reto. |
| Resultado contrastado con el umbral del escenario y reproducible | `docs/arc42/11-riesgos-y-deuda-técnica.md:81-90` deja la prueba de carga como plan futuro | No cumple | Falta resultado, herramienta, carga y procedimiento. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md:3-5` tiene las ocho columnas, pero C4, código y pruebas son texto sin enlace y Evidencia dice `Pendiente` | No cumple | No existe una fila para el reto ni una cadena navegable completa. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | La entrada más reciente, `docs/ia.md:27`, corresponde explícitamente al alcance de Semana 4 | No cumple | Falta una entrada del trabajo de Corte 1. |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `https://github.com/ISCOUTB/AS_202620_EnAgenda` | Cumple | El repositorio fue clonado sin autenticación. |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md` aparecen en `git ls-tree` | Cumple | Las seis rutas están presentes. |
| Estado calificado identificable | `git tag --list` sin `corte-1`; `HEAD` `1d01401` del 2026-08-31 | No cumple | El hash preliminar es identificable, pero falta la etiqueta exigida para el corte. |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular.md` | Cumple | Pasa `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | El ADR quedó aceptado en `c38adfb`; los commits posteriores `d5e0710` y `95af2bf` solo lo renombraron | Cumple | No se observó reescritura de contenido después de aceptarlo. |
| `docs/ia.md` al día para la semana | Último commit del archivo `1d01401`; su entrada más reciente se refiere a Semana 4 (`docs/ia.md:27`) | No cumple | No registra una decisión de IA del Corte 1. |
| Sin credenciales en el repositorio ni en el historial | Escaneo de secretos, `.env` y búsquedas históricas sin credenciales | Cumple | Las coincidencias con `token` son nombres de variable y datos ficticios de prueba, no credenciales. |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` muestra tres identidades consolidadas para tres integrantes | Cumple | No se publican correos. |

## Estado global del proyecto en `HEAD`

- **HEAD:** `1d014016fa875156d4d390bf0d1f164563b3d0ab`.
- **Estado general:** línea base funcional con aplicación Flask, módulo de invitaciones, pruebas y CI en verde.
- **Coherencia:** el C4 de contenedores aún presenta cliente, API y base de datos separados, mientras el código y el README describen una aplicación Flask con repositorio en memoria.
- **Trazabilidad:** `docs/aspectos.md:5` todavía deja la evidencia pendiente y varias celdas no son navegables.
- **Corte 1:** no hay respuesta identificable al reto nuevo, medición reproducible ni etiqueta.

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Insuficiente | 0,00 | No se declara el reto ni existe línea base medida. |
| Alternativas y decisión | Insuficiente | 0,00 | El único ADR corresponde a la línea base, no al reto. |
| Aplicación sobre el corte vertical | Insuficiente | 0,00 | No se identifica un cambio implementado para el reto. |
| Pruebas, medición y trazabilidad | Insuficiente | 0,00 | CI de la línea base en verde, sin prueba ni medición del reto y con trazabilidad incompleta. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico preliminar** |  | **0,00 / 4,00** | No equivale a la nota total sobre 5,00. |

## Recuento

**0 de 12 criterios Cumple.** El PDF y la sustentación quedan en No verificado.

## No verificado

- PDF de dos páginas entregado en Moodle.
- Conservación de límites después del cambio, porque no se identifica un cambio del reto.
- Sustentación del equipo.
- Correspondencia con la restricción externa asignada.

## Hallazgos

- Falta la etiqueta `corte-1`.
- No hay diagnóstico, ADR, incremento, prueba ni medición identificados como respuesta al reto.
- El C4 de contenedores no refleja la implementación actual.
- La tabla de aspectos no es navegable hasta una evidencia de calidad.
- El registro de IA no contiene una entrada del corte.

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada y qué cifra midieron antes de cambiar el sistema?
2. ¿Qué alternativa descartaron y qué dato haría revisar la decisión tomada?
3. ¿Qué prueba y qué procedimiento reproducible demuestran que el cambio supera el umbral?
