# Semana 05 · Primer corte · GimnasioUTB

> **Revisión manual preliminar completa, previa al cierre.** El cierre es `2026-09-07T05:00:00Z`. El resultado puede cambiar con evidencia publicada y etiquetada antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `38f00318edff1334fe5092eba6bff30658fc4e97` · 2026-09-01T12:07:42-05:00 |
| Referencia | `HEAD`, porque no existe la etiqueta `corte-1` |
| Cierre | `2026-09-07T05:00:00Z` |
| Revisor | revisión manual preliminar |
| Restricción asignada | No disponible en el kit; el repositorio no declara un reto de Corte 1 |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` no devuelve `corte-1`; `HEAD` es `38f0031` del 2026-09-01 | No cumple | Deben crear la etiqueta antes del cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Documento adjunto en Moodle | No verificado | El adjunto de Moodle no está disponible. |
| Impacto de la restricción localizado en requisitos, C4 y código | No hay sección que declare la restricción asignada ni su impacto; `docs/adr/0001-arquitectura-hexagonal.md:7-16` trata la arquitectura de línea base | No cumple | No se puede comprobar correspondencia con la asignación externa. |
| Línea base medida y verificable antes del cambio | `docs/arc42/arc42_gimnasio_utb.md:370-406` define umbrales, pero no aporta un resultado inicial medido | No cumple | Faltan cifra observada, herramienta y procedimiento. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo existe `docs/adr/0001-arquitectura-hexagonal.md`, decisión de arquitectura creada en S3 y ajustada en S4 | No cumple | No hay ADR del reto de Corte 1. |
| Cambio implementado y ejecutable de extremo a extremo | `docs/aspectos.md:34-36` describe el corte vertical de aforo de S4 y deja PostgreSQL y concurrencia como pendientes | No cumple | No se identifica un incremento aplicado para el reto nuevo. |
| Límites declarados conservados tras el cambio | `docs/c4/c4_level2.md:8-21` declara app Flutter, PostgreSQL y FCM; el árbol contiene solo backend con adaptador en memoria | No verificado | Sin cambio del reto no existe comparación posterior; la línea base ya tiene componentes declarados no implementados. |
| Prueba que cubre el cambio, en verde en el pipeline | Run de `38f0031` en verde: https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/33535934343; las pruebas citadas en `docs/aspectos.md:34-36` cubren S4 | No cumple | No hay prueba vinculada al reto nuevo. |
| Resultado contrastado con el umbral del escenario y reproducible | `docs/aspectos.md:36` deja la prueba concurrente con PostgreSQL como pendiente | No cumple | No existe resultado contrastado con los umbrales definidos. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md:3-5` usa columnas de escenario, no las ocho del contrato; `docs/aspectos.md:34-36` omite C4 y evidencia como eslabones | No cumple | No hay fila navegable del reto. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | La entrada más reciente es Semana 4 (`docs/ia.md:61-72`) y deja `Rechazado o ajustado` como `N/A` | No cumple | Falta registro de IA del Corte 1 con decisión técnica concreta. |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` | Cumple | Visible sin autenticación. |
| Estructura mínima presente | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md` y `docs/ia.md` en `git ls-tree` | Cumple | Las seis rutas están presentes. |
| Estado calificado identificable | `git tag --list` sin `corte-1`; `HEAD` `38f0031` del 2026-09-01 | No cumple | El hash preliminar se identifica, pero falta la etiqueta del corte. |
| Nombres de ADR según la convención | `docs/adr/0001-arquitectura-hexagonal.md` | Cumple | Pasa la convención de nombre. |
| ADR aceptados no reescritos | El ADR ya figuraba aceptado en `92f4a53` y fue editado en `c271073`, `b556737`, `59b6d3e` y `47a18d0` | No cumple | Un ADR aceptado debe conservarse y cualquier cambio de decisión debe registrarse en otro ADR. |
| `docs/ia.md` al día para la semana | Último commit del archivo `56db96b` del 2026-08-30; última entrada Semana 4 | No cumple | Falta una entrada del Corte 1. |
| Sin credenciales en el repositorio ni en el historial | Escaneo de secretos, `.env` y búsquedas históricas sin coincidencias | Cumple | Solo existe `.env.example`, que no contiene credenciales reales. |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` consolida tres personas para los tres integrantes | Cumple | Las dos firmas del mismo integrante se consolidaron; no se publican correos. |

## Estado global del proyecto en `HEAD`

- **HEAD:** `38f00318edff1334fe5092eba6bff30658fc4e97`.
- **Estado general:** backend Node.js con corte vertical de aforo, pruebas unitarias y de integración, README reproducible y CI en verde.
- **Coherencia:** el C4 incluye aplicación Flutter, PostgreSQL y FCM, pero el código visible implementa el backend con persistencia en memoria.
- **Trazabilidad:** la tabla de aspectos no usa las ocho columnas contractuales y deja la prueba concurrente real como pendiente.
- **Gobernanza:** el ADR aceptado fue reescrito varias veces y además declara equipo de cuatro personas en `docs/adr/0001-arquitectura-hexagonal.md:16`, mientras `EQUIPOS.md` registra tres.
- **Corte 1:** no hay reto declarado, línea base medida, incremento ni etiqueta.

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Insuficiente | 0,00 | No se declara el reto ni se mide un estado inicial. |
| Alternativas y decisión | Insuficiente | 0,00 | No existe ADR del reto. |
| Aplicación sobre el corte vertical | Insuficiente | 0,00 | La implementación visible corresponde a la línea base de S4. |
| Pruebas, medición y trazabilidad | Insuficiente | 0,00 | CI en verde para S4, sin prueba ni medición del reto y sin cadena completa. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico preliminar** |  | **0,00 / 4,00** | No equivale a la nota total sobre 5,00. |

## Recuento

**0 de 12 criterios Cumple.** El PDF y la sustentación quedan en No verificado.

## No verificado

- PDF entregado en Moodle.
- Conservación de límites después del cambio del reto.
- Sustentación.
- Correspondencia con la restricción externa asignada.

## Hallazgos

- Falta la etiqueta `corte-1`.
- No existe una respuesta identificable al reto nuevo.
- La medición concurrente con PostgreSQL está explícitamente pendiente.
- El C4 contiene contenedores aún no implementados.
- El ADR aceptado fue reescrito y el registro de IA no está actualizado para el corte.

## Preguntas para la sustentación

1. ¿Cuál fue la restricción asignada y cuál fue la medición inicial obtenida antes del cambio?
2. ¿Qué cambio distingue este corte de la línea base de aforo entregada en S4?
3. ¿Cómo reproducirían la prueba concurrente y qué umbral debe superar?
