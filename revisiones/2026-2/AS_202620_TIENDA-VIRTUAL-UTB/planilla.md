# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo a lo largo del semestre.

## Identificación

| | |
|---|---|
| Equipo | Tienda virtual UTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Integrantes y su usuario de GitHub | Shalom Jhoanna Arrieta Marrugo (shalom-A26) · Levis Adrian Ortiz Cano (RAZOR7150) · Alejandro Patron Montero (pxtroniwnl) · Jasen Mihovil Yukopila Escobar (Jmyukopila) — correspondencias por los correos de los commits, por confirmar con el docente |
| URL del sistema desplegado | sin URL (sin despliegue todavía) |
| Última revisión | 2026-08-23 (S1 y S2) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `d414ecf` · 2026-08-09T14:08:31-05:00 | 7/9 | 4.1 (propuesta) | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `456365b` · 2026-08-15T14:07:47-05:00 | 6/9 | 3.7 (propuesta) | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | | | no aplica | |
| 4 | Evidencia S4 · arc42, C4 y corte vertical | | | no aplica | |
| 5 | Primer corte · reto de línea base | `corte-1` | | | |
| 6 | Evidencia S6 · Contextos delimitados y propiedad de datos | | | no aplica | |
| 7 | Evidencia S7 · Contrato de API y prueba de contrato | | | no aplica | |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | | | no aplica | |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 9 | Evidencia S9 · Generación verificada y trazable | | | no aplica | |
| 10 | Segundo corte · reto aplicado sobre el MVP | `corte-2` | | | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/aspectos.md` sin la tabla de 8 columnas del curso (tabla de 2 columnas, sin ID ni enlaces a escenarios) | S1 | sí | ajustar la tabla a las 8 columnas y enlazar cada escenario desde su fila (S2: sigue igual) |
| `docs/ia.md` sin registro de «qué se rechazó y por qué» | S1 | sí | añadir la columna/entradas de rechazo con motivo técnico (S2: sin commits sobre el archivo en el periodo) |
| Shalom Jhoanna Arrieta Marrugo sin commits en el historial | S1 (y S2) | sí | primer commit el 2026-08-21 (`f4602a3`, fuera del cierre S2); urge que aparezca antes del corte 1 |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB`, público |
| Estructura mínima | Cumple | seis rutas presentes; desviación: escenarios en `docs/escenarios-calidad.md` con arc42 §10 vacía |
| Convención de nombres de ADR | Cumple | sin ADR todavía |
| ADR aceptados sin reescribir | Cumple | sin ADR todavía |
| `docs/ia.md` al día | No cumple | sin commits en el periodo S2 y sin registro de rechazos |
| Sin credenciales en el repositorio ni en el historial | Cumple | greps limpios |
| Contribución de todos los integrantes | No cumple | al cierre S2, 3 de 4 en el historial |
| Pipeline en verde | No verificado | sin pipeline todavía (no exigido aún) |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---:|---:|---:|---|
| Jasen Mihovil Yukopila Escobar | Jmyukopila (firma «Jasen» y «Jasen Yukopila», mismo correo) | 4 | — | — | toda la base de S1 |
| Levis Adrian Ortiz Cano | RAZOR7150 | 2 | — | — | — |
| Alejandro Patron Montero | pxtroniwnl | 2 | — | — | S2 |
| Shalom Jhoanna Arrieta Marrugo | shalom-A26 | 1 | — | — | primer commit 2026-08-21 (tras el cierre S2) |

## Preguntas abiertas para la sustentación

- ¿Los cuatro integrantes tienen acceso de escritura al repositorio? (sin API no se pudo listar colaboradores).
- ¿Por qué la sección 10 del arc42 está vacía si los escenarios existen en `docs/escenarios-calidad.md`?
