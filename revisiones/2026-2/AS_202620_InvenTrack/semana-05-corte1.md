# Semana 05 · Primer corte · InvenTrack

> **Revisión manual preliminar completa, previa al cierre.** El cierre es `2026-09-07T05:00:00Z`. El resultado puede cambiar con evidencia publicada y etiquetada antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `ee484bf6bac153697bd6f2f703eefc8b637d74b8` · 2026-09-03T17:06:22-05:00 |
| Referencia | `HEAD`, porque no existe la etiqueta `corte-1` |
| Cierre | `2026-09-07T05:00:00Z` |
| Revisor | revisión manual preliminar |
| Restricción asignada | No disponible en el kit; el repositorio no declara un reto de Corte 1 |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` no devuelve `corte-1`; `HEAD` es `ee484bf` del 2026-09-03 | No cumple | Deben crear la etiqueta antes del cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Documento adjunto en Moodle | No verificado | El adjunto no está disponible en el kit ni en el repositorio. |
| Impacto de la restricción localizado en requisitos, C4 y código | No hay apartado que declare el reto; `docs/aspectos.md:17-19` solo traza ASP-01 de la línea base | No cumple | No se puede afirmar correspondencia con la restricción externa asignada. |
| Línea base medida y verificable antes del cambio | `docs/arc42/arc42-template-EN.md:637-646` define el umbral de rendimiento, sin resultado inicial obtenido | No cumple | Hay criterio futuro, no una línea base medida con procedimiento ejecutado. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo existe `docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md:1-18`, decisión de línea base | No cumple | Falta un ADR del reto nuevo. |
| Cambio implementado y ejecutable de extremo a extremo | `app/productos/` y `app/inventario/` están implementados, pero ningún commit, documento o ADR los identifica como respuesta al reto asignado | No cumple | El avance acumulado no sustituye la evidencia del reto de Corte 1. |
| Límites declarados conservados tras el cambio | `docs/c4/containers.md:80-98` mapea la línea base; no hay estado posterior al reto para comparar | No verificado | Sin cambio identificado no puede verificarse la conservación de límites. |
| Prueba que cubre el cambio, en verde en el pipeline | Run de `ee484bf` en verde: https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/33811437677; la suite cubre productos e inventario | No cumple | No hay prueba enlazada a una respuesta explícita al reto. |
| Resultado contrastado con el umbral del escenario y reproducible | `docs/arc42/arc42-template-EN.md:646` solo define `≤ 400 ms p95` con 20 usuarios; no consta resultado | No cumple | Falta medición ejecutada, herramienta, carga observada y resultado. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md:17-19` tiene las ocho columnas para ASP-01, pero no existe fila del reto ni del nuevo módulo de inventario | No cumple | La evidencia de calidad es una afirmación de suite en verde, no un resultado medido del reto. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md:22` registra S4 el 2026-08-30; no existe entrada de Corte 1 | No cumple | Falta el registro de IA de esta entrega. |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `https://github.com/ISCOUTB/AS_202620_InvenTrack` | Cumple | Visible sin autenticación. |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md` en `git ls-tree` | Cumple | Las seis rutas están presentes. |
| Estado calificado identificable | `git tag --list` sin `corte-1`; `HEAD` `ee484bf` del 2026-09-03 | No cumple | El hash preliminar se identifica, pero falta la etiqueta de corte. |
| Nombres de ADR según la convención | `docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md` | Cumple | Pasa la convención. |
| ADR aceptados no reescritos | El ADR estuvo propuesto, fue eliminado y restaurado; quedó aceptado en `45d2fa0` y no tuvo cambios posteriores | Cumple | El churn ocurrió antes de la aceptación. |
| `docs/ia.md` al día para la semana | Último commit del archivo `385fbe2` del 2026-08-31; última fila S4 (`docs/ia.md:22`) | No cumple | No registra el trabajo del Corte 1. |
| Sin credenciales en el repositorio ni en el historial | Escaneo de secretos, `.env` y búsquedas históricas sin coincidencias | Cumple | No se encontraron credenciales. |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` consolida cuatro personas para cuatro integrantes | Cumple | Se agruparon las variantes de firma; no se publican correos. |

## Estado global del proyecto en `HEAD`

- **HEAD:** `ee484bf6bac153697bd6f2f703eefc8b637d74b8`.
- **Estado general:** aplicación FastAPI con módulos de productos e inventario, pruebas automatizadas, README y CI en verde.
- **Coherencia:** el C4 declara interfaz web y base de datos aún por definir; el estado actual usa API y adaptadores en memoria.
- **Trazabilidad:** `docs/aspectos.md` traza productos, pero el módulo de inventario añadido en HEAD no aparece como nueva fila ni como evidencia del reto.
- **Navegación:** `README.md:42` enlaza `docs/c4/container.md`, mientras el archivo real es `docs/c4/containers.md`.
- **Corte 1:** no hay etiqueta, diagnóstico, ADR ni medición asociados al reto nuevo.

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Insuficiente | 0,00 | No se declara el reto ni se mide su línea base. |
| Alternativas y decisión | Insuficiente | 0,00 | El ADR disponible corresponde al estilo base. |
| Aplicación sobre el corte vertical | Insuficiente | 0,00 | Hay avance funcional, pero no se identifica como respuesta al reto. |
| Pruebas, medición y trazabilidad | Insuficiente | 0,00 | CI en verde, sin prueba del reto ni resultado contra umbral. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico preliminar** |  | **0,00 / 4,00** | No equivale a la nota total sobre 5,00. |

## Recuento

**0 de 12 criterios Cumple.** El PDF y la sustentación quedan en No verificado.

## No verificado

- PDF de dos páginas entregado en Moodle.
- Conservación de límites después del cambio del reto.
- Sustentación.
- Correspondencia con la restricción externa asignada.

## Hallazgos

- Falta la etiqueta `corte-1`.
- No existe una respuesta explícita al reto nuevo.
- El umbral de rendimiento está definido, pero no medido.
- El módulo de inventario de HEAD no está incorporado a la tabla de aspectos.
- El registro de IA no tiene entrada del corte y hay un enlace roto al C4 de contenedores en el README.

## Preguntas para la sustentación

1. ¿Qué restricción recibió el equipo y dónde está el diagnóstico que conecta requisito, C4 y módulos afectados?
2. ¿Qué cambio de productos o inventario responde específicamente al reto y por qué se eligió sobre las alternativas?
3. ¿Qué comando reproduce la medición y cuál fue el resultado frente al umbral?
