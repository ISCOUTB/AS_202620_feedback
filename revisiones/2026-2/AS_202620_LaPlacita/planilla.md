# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo LaPlacita. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | LaPlacita |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Integrantes y su usuario de GitHub | Mateo Josue Buendia Barrios · Miguel Angel Isaza Montalvo · Samuel David Jimenez Alvarez · Jorge Alberto Martinez Castillo — cuentas abajo |
| URL del sistema desplegado | sin desplegar aún |
| Ultima revision | 2026-08-29 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 4 | S4 | `745e799` (2026-08-30T21:52:41-05:00) | 2/10 | 1.8 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `37f1deb8` · 2026-08-08T15:37:16-05:00 | 8/9 | 4,6 * | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `fa7e13bc` · 2026-08-15T18:13:29-05:00 | 5/9 | 3,2 * | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `014751df` · 2026-08-23T19:30:17-05:00 | 9/9 | no se publica | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `ia.md` sin registro de lo rechazado y su motivo | S1 | Cerrado en S3 (entradas del 23/08 con rechazos y motivos) | Resuelto |
| C4 de contexto sin leyenda y guardado dentro del arc42 (§3.3), no en `docs/c4/` | S2 | Cerrado en S3 (`docs/c4/contexto.md` con leyenda, `340c22a`) | Resuelto |
| Escenarios sin la parte «artefacto» | S2 | Cerrado en S3 (ESC-01…ESC-05 con artefacto) | Resuelto |
| `aspectos.md` sin enlaces a los escenarios | S2 | Sí (parcial: ya es tabla de 8 columnas con enlaces al ADR y al código; la columna Requisito sigue sin enlazar a los escenarios) | Enlazar RF-xx a los escenarios correspondientes |
| Ficha del problema sin dos tensiones de calidad (S1) | S1 | Cerrado en S2 parcialmente | Las tensiones aparecen implícitas en el arc42 (objetivos 1.2); declararlas explícitas si vuelven a pedirse |
| ADR 0001 en estado «propuesto» | S3 | Sí | Ratificar y marcar como aceptado |
| Sin pipeline: el verde descansa en evidencia declarada en `ia.md` | S3 | Sí | Añadir `.github/workflows/` antes del corte 1 |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_LaPlacita`, público |
| Estructura mínima | Cumple | Seis rutas; C4 en `docs/c4/contexto.md` con leyenda |
| Convención de nombres de ADR | Cumple | `0001-adopcion-monolito-modular.md` |
| ADR aceptados sin reescribir | Cumple | Único commit `bf94244`; estado «propuesto» anotado |
| `docs/ia.md` al día | Cumple | Entradas del 23/08 con lo rechazado y su motivo |
| Sin credenciales en el repositorio ni en el historial | Cumple | Greps limpios |
| Contribución de todos los integrantes | Cumple | 4 identidades consolidadas / 4 integrantes (53+21+18+3) |
| Pipeline en verde | No verificado | Sin `.github/workflows/`; verde según declaración del equipo en `docs/ia.md` |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Mateo Josue Buendia Barrios | matbuendia (dos correos consolidados) | 3 | 0 | — | Sin commits en S3 |
| Miguel Angel Isaza Montalvo | Isaza927 + `isaza927` (mismo correo, consolidado) | 21 | 0 | — | Motor de S3: esqueleto, §4, enlaces del ADR |
| Samuel David Jimenez Alvarez | samulssl (correo omitido) | 18 | 0 | — | Creó el ADR 0001 (`bf94244`) |
| Jorge Alberto Martinez Castillo | Jorge M. Castillo (correo omitido) | 53 | 0 | — | Mayor contribuidor; redacción final de S3 |

Correspondencia cuenta↔persona inferida del correo de los commits; la confirma el docente.

## Preguntas abiertas para la sustentación

- ¿Por qué se retiró de `aspectos.md` la sección de enlaces a los escenarios (commit `b1f8da2`) que existía en `a484f1a`? (parcialmente resuelto: la tabla ya enlaza ADR y código; los RF-xx siguen sin enlazar a los escenarios).
- ¿Cuál es el artefacto (módulo) que recibe el estímulo en cada uno de los cinco escenarios? (resuelto en S3: la sección 4.3 asigna módulo por escenario).
- ¿Cuándo piensan montar el pipeline para que la prueba en verde deje de descansar en la declaración de `ia.md`?
- ¿Ratifican el ADR 0001 como «aceptado» (hoy dice «propuesto»)?
