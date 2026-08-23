# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo EnAgenda. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | EnAgenda |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Integrantes y su usuario de GitHub | Eliab Josue Arnedo Conde · Jeimy Yulieth Mendez Altamiranda · Gabriela Morales Cancino — cuentas abajo |
| URL del sistema desplegado | sin desplegar aún |
| Última revisión | 2026-08-23 (revisión S1 + S2) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `13f61b10` · 2026-08-09T05:34:14-05:00 | 8/9 | 4,6 * | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `5b6f7a8e` · 2026-08-16T23:33:20-05:00 | 5/9 | 3,2 * | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Nombres de archivo con espacio antes de la extensión (`docs/aspectos .md`, `docs/ia .md`, `docs/ficha-problema .md`, ADR, arc42) | S1 | Sí | Renombrar a la convención; el ADR no pasa el filtro de nombres |
| Integrante Eliab Josue Arnedo Conde sin commits en S1 (primer commit 2026-08-16) | S1 | Cerrado en S2 (2 commits) | Se resolvió solo; vigilar que la contribución siga repartida |
| `aspectos.md` sin enlaces a escenarios (C4/ADR/Código/Pruebas/Evidencia en «Pendiente») | S2 | Sí | Enlazar cada escenario desde su fila de aspecto |
| C4 de contexto sin leyenda | S2 | Sí | Añadir leyenda al mermaid |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_EnAgenda`, público, verificable sin autenticación |
| Estructura mínima | Cumple | Con desviación de nombres (espacios antes de `.md`) |
| Convención de nombres de ADR | No cumple | `0001-app-movil-y-web-de-invitaciones .md` con espacio |
| ADR aceptados sin reescribir | Cumple | Un solo commit de creación (`e1219bf`) |
| `docs/ia.md` al día | Cumple | Entradas del 07, 08 y 15 de agosto con rechazos y motivos; commit posterior al cierre S2 anotado |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` de secretos sin coincidencias; sin `.env` versionado |
| Contribución de todos los integrantes | Cumple en S2 | 3 cuentas / 3 integrantes: 32 + 5 + 2 commits |
| Pipeline en verde | No verificado | Sin `.github/workflows/` todavía; no exigible en semanas 1 y 2 |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Eliab Josue Arnedo Conde | eliabarnedocondef10-gif (correo omitido) | 2 | 0 | — | Primer commit 2026-08-16; no aparece en S1 |
| Jeimy Yulieth Mendez Altamiranda | Jein-12 (correo omitido) | 6 | 0 | — | |
| Gabriela Morales Cancino | Daoisttl0FB3 (correo omitido) | 32 | 0 | — | Autora de la mayoría del contenido |

Correspondencia cuenta↔persona inferida del correo de los commits, no de parecidos de nombre; la confirma el docente.

## Preguntas abiertas para la sustentación

- ¿El tercer integrante (Eliab) tenía acceso al repositorio desde la semana 1? (la lista de colaboradores no se pudo consultar por límite de API).
- ¿Cómo justificaría el equipo la priorización del árbol de utilidad en términos de riesgo?
