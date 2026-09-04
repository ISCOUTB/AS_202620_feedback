# Semana 05 · Primer corte · LaPlacita

> **Revisión manual preliminar completa, previa al cierre.** El cierre es `2026-09-07T05:00:00Z`. El resultado puede cambiar con evidencia publicada y etiquetada antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `812d22707b2033b2edc296f1df621a1c6e93072d` · 2026-09-02T11:39:24-05:00 |
| Referencia | `HEAD`, porque no existe la etiqueta `corte-1` |
| Cierre | `2026-09-07T05:00:00Z` |
| Revisor | revisión manual preliminar |
| Restricción asignada | No disponible en el kit; el repositorio declara que aún debe identificarla |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` no devuelve `corte-1`; `HEAD` es `812d227` del 2026-09-02 | No cumple | `correciones.md:109-123` también registra la etiqueta como pendiente. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Documento adjunto en Moodle | No verificado | El adjunto no está disponible. |
| Impacto de la restricción localizado en requisitos, C4 y código | `correciones.md:109-116` dice que aún se debe declarar la restricción asignada y crear su ADR | No cumple | El propio repositorio confirma que el diagnóstico del reto no existe. |
| Línea base medida y verificable antes del cambio | `correciones.md:116` deja pendiente una medición reproducible | No cumple | Falta cifra inicial con herramienta, carga y procedimiento. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Hay tres ADR de línea base; `docs/adr/0003-despliegue-railway-docker-sonarcloud.md:97-100` deja su implementación pendiente y `correciones.md:112` pide crear el ADR del reto | No cumple | Ningún ADR se identifica como respuesta a la restricción asignada de Corte 1. |
| Cambio implementado y ejecutable de extremo a extremo | `README.md:187-225` describe el corte vertical de S4; el ADR 0003 deja Docker, SonarCloud y el commit de implementación pendientes | No cumple | No se identifica un cambio aplicado para el reto nuevo. |
| Límites declarados conservados tras el cambio | `docs/c4/contenedores.md:14-35` declara web, portal, Redis, PostgreSQL, pagos y push; el árbol actual implementa Next.js y módulos locales | No verificado | Sin cambio del reto no existe comparación; el C4 incluye componentes futuros. |
| Prueba que cubre el cambio, en verde en el pipeline | Run de `812d227` en verde: https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/33656270650; las pruebas visibles cubren la línea base | No cumple | No hay prueba vinculada al reto asignado. |
| Resultado contrastado con el umbral del escenario y reproducible | `correciones.md:116` reconoce que falta la medición reproducible | No cumple | No hay resultado contra umbral. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md:9-16` tiene nueve columnas y deja `Evidencia` pendiente; no existe fila del reto | No cumple | A-01 recorre parte de la línea base, no la respuesta al reto. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | La última entrada es del 2026-08-30 (`docs/ia.md:19-22`) y pertenece al trabajo de S4 | No cumple | Falta una entrada del Corte 1. |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `https://github.com/ISCOUTB/AS_202620_LaPlacita` | Cumple | Visible sin autenticación. |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md` en `git ls-tree` | Cumple | Las seis rutas están presentes. |
| Estado calificado identificable | `git tag --list` sin `corte-1`; `HEAD` `812d227` del 2026-09-02 | No cumple | El hash preliminar se identifica, pero falta la etiqueta de corte. |
| Nombres de ADR según la convención | `0001-adopcion-monolito-modular.md`, `0002-ratificacion-monolito-modular.md` y `0003-despliegue-railway-docker-sonarcloud.md` | Cumple | Los tres pasan la convención. |
| ADR aceptados no reescritos | Los ADR 0002 y 0003 figuran aceptados y cada uno tiene un único commit; el ADR 0001 sigue propuesto | Cumple | No se observaron reescrituras posteriores a la aceptación. |
| `docs/ia.md` al día para la semana | Último commit del archivo `26a9210` del 2026-08-30; no hay entrada de Corte 1 | No cumple | Falta actualizar la bitácora para esta entrega. |
| Sin credenciales en el repositorio ni en el historial | Escaneo de secretos, `.env` y búsquedas históricas sin coincidencias | Cumple | No se encontraron credenciales. |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` consolida cuatro personas para cuatro integrantes | Cumple | Se agruparon variantes de firma; no se publican correos. |

## Estado global del proyecto en `HEAD`

- **HEAD:** `812d22707b2033b2edc296f1df621a1c6e93072d`.
- **Estado general:** aplicación Next.js con módulos de dominio, corte vertical de pedidos, pruebas automatizadas, README y CI en verde.
- **Coherencia:** el C4 presenta contenedores y servicios todavía no implementados. El ADR 0003 afirma Railway, Docker y SonarCloud como decisión aceptada, pero sus propias líneas 97-100 declaran los artefactos y el commit pendientes.
- **Trazabilidad:** A-01 enlaza código y pruebas de S4, pero deja la evidencia pendiente; las demás filas siguen incompletas.
- **Corte 1:** `correciones.md:109-123` reconoce que todavía faltan restricción, diagnóstico, ADR, etiqueta y medición.

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Insuficiente | 0,00 | El repositorio declara pendiente identificar la restricción y medir la línea base. |
| Alternativas y decisión | Insuficiente | 0,00 | Los ADR existentes son de línea base; falta el ADR del reto. |
| Aplicación sobre el corte vertical | Insuficiente | 0,00 | No se identifica incremento del reto; el ADR 0003 no está implementado. |
| Pruebas, medición y trazabilidad | Insuficiente | 0,00 | CI en verde para la línea base, sin medición ni cadena del reto. |
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
- El propio archivo de correcciones confirma que el reto aún no está declarado ni implementado.
- ADR 0003 está aceptado, pero sus artefactos de implementación siguen pendientes.
- La tabla de aspectos deja la evidencia pendiente y no tiene fila del reto.
- El registro de IA no contiene una entrada del Corte 1.

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada y qué evidencia inicial midieron antes de modificar el sistema?
2. ¿El reto corresponde a despliegue y análisis estático o a otra restricción? ¿Dónde está el ADR específico?
3. ¿Qué resultado reproducible demuestra que el incremento cumple el umbral?
