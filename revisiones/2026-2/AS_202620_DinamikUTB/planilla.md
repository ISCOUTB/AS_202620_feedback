# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | DinamikUTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Integrantes y su usuario de GitHub | Luis Daniel Padilla Leottau (`Daniel-dev02`) · Gillianis Del Carmen Perez Revolledo (`gillianisperez-prog`) · Esteban Ramirez Rios (`Eramirezr`) · Juan Jose Vargas Perez (`JuanchisV`, firma también como «Juan José Vargas Pérez» con el mismo correo) |
| URL del sistema desplegado | sin desplegar todavía |
| Última revisión | 2026-08-24 (Evidencia S3, actualizada tras el cierre) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `769f970` · 2026-08-09T21:24:49-05:00 | 7/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `58734e1c` · 2026-08-16T23:33:53-05:00 | 9/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `fe52ab594` · 2026-08-23T23:20:33-05:00 | 5/9 | no se publica | sí (actualizada tras el cierre) |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Ficha del problema entregada en PDF, no en Markdown | S1 | sí | Ver feedback S1/S2 |
| Solo una tensión de calidad declarada (se pedían dos) | S1 | sí | Ver feedback S1/S2 |
| Trabajo del periodo concentrado en un integrante | S2 | sí (en S3, JuanchisV firma 21 de 46 commits) | Ver feedback S1/S2 y S3 |
| Esteban sin commits en el periodo (S1; reaparece en S3) | S1 | cerrado en S3 (2 commits: `2c78be9`, `fe52ab5`) | Ver feedback S3 |
| Matriz de estilos sin referencia a los escenarios del árbol de utilidad | S3 | sí | Ver feedback S3 |
| `docs/aspectos.md` con la columna ADR en «Pendiente» aun existiendo el ADR 0001 (la tabla de 8 columnas y los enlaces a escenarios ya llegaron) | S3 | sí (parcialmente cerrado: tabla y enlaces a escenarios OK; columna ADR sigue pendiente) | Ver feedback S3 |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `AS_202620_DinamikUTB`, público. |
| Estructura mínima | Cumple | Las seis rutas presentes; arc42 con 12 secciones. |
| Convención de nombres de ADR | Cumple | `0001-seleccion-monolito-modular.md` conforme. |
| ADR aceptados sin reescribir | Cumple | Creado e iterado el mismo día (2026-08-23, 04:00–04:48), sin reescrituras posteriores. |
| `docs/ia.md` al día | Cumple | Entradas del 23/08 con rechazos («Rechazado parcialmente») y motivo. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | Cumple | 4 de 4 en S3 (Juan 21, Gillianis 11, Luis 12, Esteban 2); desbalance anotado. |
| Pipeline en verde | No verificado | Sin pipeline; hay pruebas locales (`backend/tests/test_main.py`, `frontend/test/widget_test.dart`) sin evidencia de ejecución. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Juan Jose Vargas Perez | `JuanchisV` (+ firma «Juan José Vargas Pérez») | 21 (S3) | — | — | Autor del ADR y del esqueleto |
| Gillianis Del Carmen Perez Revolledo | `gillianisperez-prog` | 11 (S3) | — | — | Enlaces de escenarios en aspectos.md |
| Luis Daniel Padilla Leottau | `Daniel-dev02` (+ firma «LUIS DANIEL») | 12 (S3) | — | — | README y merges de ramas |
| Esteban Ramirez Rios | `Eramirezr` | 2 (S3) | — | — | Estructura del proyecto e ia.md; reapareció tras S1/S2 sin commits |

## Preguntas abiertas para la sustentación

- ¿Por qué la ficha del problema declara una sola tensión de calidad cuando se pedían dos?
- ¿Cómo se repartirá el trabajo de las próximas entregas para equilibrar la contribución del historial?
- ¿Por qué la columna ADR de `docs/aspectos.md` sigue en «Pendiente» si el ADR 0001 existe desde el 23 de agosto (y la nota dice que los elementos «todavía no existen»)?
- ¿Qué tácticas concretas aplicarán a Q-01, Q-02 y Q-03 para la semana 4?
