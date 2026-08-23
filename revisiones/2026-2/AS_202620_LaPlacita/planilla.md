# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo LaPlacita. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | LaPlacita |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Integrantes y su usuario de GitHub | Mateo Josue Buendia Barrios · Miguel Angel Isaza Montalvo · Samuel David Jimenez Alvarez · Jorge Alberto Martinez Castillo — cuentas abajo |
| URL del sistema desplegado | sin desplegar aún |
| Última revisión | 2026-08-23 (revisión S1 + S2) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `37f1deb8` · 2026-08-08T15:37:16-05:00 | 8/9 | 4,6 * | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `fa7e13bc` · 2026-08-15T18:13:29-05:00 | 5/9 | 3,2 * | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `ia.md` sin registro de lo rechazado y su motivo | S1 | Sí | Añadir por cada uso qué se rechazó y por qué |
| C4 de contexto sin leyenda y guardado dentro del arc42 (§3.3), no en `docs/c4/` | S2 | Sí | Añadir leyenda y mover/versionar el diagrama en `docs/c4/` |
| Escenarios sin la parte «artefacto» | S2 | Sí | Completar las seis partes en cada escenario |
| `aspectos.md` sin enlaces a los escenarios (la sección de enlaces se retiró en `b1f8da2`) | S2 | Sí | Restaurar los enlaces a ESC-01…ESC-05 |
| Ficha del problema sin dos tensiones de calidad (S1) | S1 | Cerrado en S2 parcialmente | Las tensiones aparecen implícitas en el arc42 (objetivos 1.2); declararlas explícitas si vuelven a pedirse |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_LaPlacita`, público |
| Estructura mínima | Cumple | Seis rutas desde S1 (`.gitkeep` en `adr/` y `c4/`) |
| Convención de nombres de ADR | Cumple (vacuo) | Solo `.gitkeep`; limpiar al llegar el primer ADR |
| ADR aceptados sin reescribir | Cumple (vacuo) | Sin ADR todavía |
| `docs/ia.md` al día | No cumple | Crece en cada semana, pero sin lo rechazado y su motivo |
| Sin credenciales en el repositorio ni en el historial | Cumple | Greps limpios |
| Contribución de todos los integrantes | Cumple | Los 4 integrantes empujan desde S1 |
| Pipeline en verde | No verificado | Sin `.github/workflows/`; no exigible en semanas 1 y 2 |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Mateo Josue Buendia Barrios | matbuendia (dos correos: buendiamateo670 y mateo.buendia.barrios) | 3 | 0 | — | Identidad consolidada: 2 + 1 commits |
| Miguel Angel Isaza Montalvo | Isaza927 (correo omitido) | 12 | 0 | — | |
| Samuel David Jimenez Alvarez | samulssl (correo omitido) | 15 | 0 | — | Commits con huso horario +06:00 |
| Jorge Alberto Martinez Castillo | Jorge M. Castillo (correo omitido) | 50 | 0 | — | Mayor contribuidor |

Correspondencia cuenta↔persona inferida del correo de los commits; la confirma el docente.

## Preguntas abiertas para la sustentación

- ¿Por qué se retiró de `aspectos.md` la sección de enlaces a los escenarios (commit `b1f8da2`) que existía en `a484f1a`?
- ¿Cuál es el artefacto (módulo) que recibe el estímulo en cada uno de los cinco escenarios?
