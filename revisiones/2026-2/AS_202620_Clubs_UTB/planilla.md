# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Clubs UTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Integrantes y su usuario de GitHub | Hollman Jose De Orta Gonzalez (`deortahollman-star`) · Josh Robinson Ortega Castellon (`Josh4OP`) · Diego Andres Ramos De Avila (`Zavod Dev`, atribución sin confirmar) · Luis Daniel Salas Reyes (`Luis-Salas-Reyes`) |
| URL del sistema desplegado | sin desplegar todavía |
| Última revisión | 2026-08-24 (Evidencia S3, actualizada tras el cierre) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `c92595ed` · 2026-08-09T13:25:24-05:00 | 2/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `69cfe68f` · 2026-08-16T18:33:10-05:00 | 7/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `5bf86ead1` · 2026-08-23T23:05:10-05:00 | 6/9 | no se publica | sí (actualizada tras el cierre) |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/aspectos.md` sin la tabla de 8 columnas del curso | S1 | sí (en S3 rompe el enlace hacia el ADR) | Ver feedback S1/S2 y S3 |
| Ficha del problema sin tensiones de calidad | S1 | sí | Ver feedback S1/S2 |
| Estructura con desviaciones: `docs/C4/` en mayúscula; en S3 aparece `docs/adr/.temp` residual | S1 (C4), S3 (.temp) | sí | Ver feedback S1/S2 y S3 |
| `docs/ia.md` sin usos reales ni rechazos, sin commits en S2 ni S3 | S2 | sí | Ver feedback S1/S2 y S3 |
| Sin esqueleto ejecutable al cierre: `main.py` y `test_health.py` vacíos en `5bf86ead1`, README sin comando de arranque; el esqueleto real llegó TARDÍO (`8d69f62`, 00:21, 21 min después del cierre) | S3 | sí (llegó fuera del cierre) | Ver feedback S3 |
| ADR no alcanzable desde `aspectos.md` ni desde el escenario U2 | S3 | sí | Ver feedback S3 |
| Josh sin commits en S3 (primera revisión) | S3 | cerrado: `5bf86ea` (23:05) firmado por Josh Ortega, mismo correo que Josh4OP | Contribución 4/4 en S3 |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `AS_202620_Clubs_UTB`, público. |
| Estructura mínima | Cumple | Las seis rutas existen; `docs/C4/` en mayúscula (desviación de ruta). |
| Convención de nombres de ADR | Cumple | `0001-hexagonal.md` conforme; `docs/adr/.temp` residual a borrar. |
| ADR aceptados sin reescribir | Cumple | Aceptado en `2c316f4`, sin reescrituras posteriores. |
| `docs/ia.md` al día | No cumple | Último commit `c92595e` (2026-08-09). |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | Cumple | 4 de 4 en S3: Luis 2, Diego 2, Hollman 1, Josh 1 (Josh4OP = «Josh Ortega», mismo correo). |
| Pipeline en verde | No cumple | Sin workflow; la prueba estaba vacía en el hash calificado (contenido tardío). |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Diego Andres Ramos De Avila | `Zavod Dev` (atribución sin confirmar) | 2 (S3) | — | — | Matriz comparativa y corrección de enlaces |
| Luis Daniel Salas Reyes | `Luis-Salas-Reyes` | 2 (S3) | — | — | Autor del ADR y su revisión |
| Hollman Jose De Orta Gonzalez | `deortahollman-star` | 1 (S3) | — | — | Matriz comparativa |
| Josh Robinson Ortega Castellon | `Josh4OP` (firma también como «Josh Ortega», mismo correo) | 1 (S3) | — | — | Carpetas hexagonales (`5bf86ea`) y esqueleto ejecutable (`8d69f62`, tardío) |

## Preguntas abiertas para la sustentación

- Confirmar que `Zavod Dev` es Diego Andres Ramos De Avila.
- ¿Existen restricciones legales aplicables o hay que declarar que no aplican?
- ¿Por qué `docs/aspectos.md` no usa la tabla de 8 columnas y no enlaza el ADR 0001?
- ¿Por qué el esqueleto ejecutable (main.py + prueba) llegó 21 minutos después del cierre, con archivos vacíos en el commit calificado?
- De los 6 escenarios (U1–U3, C1–C3), ¿cuáles se conservarán si el rango pedido es 3–5?
