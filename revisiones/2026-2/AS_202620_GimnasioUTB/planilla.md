# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo GimnasioUTB. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | GimnasioUTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Integrantes y su usuario de GitHub | Sebastian Felipe Caicedo Acosta · Rodrigo Andres Facio Lince Beltran · Pedro Luis Pallares De La Hoz — cuentas abajo |
| URL del sistema desplegado | sin desplegar aún |
| Última revisión | 2026-08-23 (revisión S1 + S2) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `a45615e9` · 2026-08-08T21:41:21-05:00 | 4/9 | 2,8 * | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `1b30b7a4` · 2026-08-16T21:04:17-05:00 | 5/9 | 3,2 * | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Sin `docs/arc42/`, `docs/adr/` ni `docs/c4/` (arc42 en un solo archivo `docs/Evidencia S2…md`, C4 en `docs/C4.jpg`) | S1 | Sí | Montar la estructura mínima del contrato y repartir el contenido en las rutas convenidas |
| Sebastián Caicedo Acosta sin commits ni cuenta atribuible | S1 | Sí | Verificar acceso al repositorio y empezar a contribuir (la contribución individual se califica en el final) |
| `docs/aspectos.md` en prosa, sin la tabla de 8 columnas ni enlaces a escenarios | S1 | Sí | Convertir a tabla ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia y enlazar cada escenario |
| `docs/ia.md` sin entradas por uso (herramienta, aceptado, rechazado con motivo) | S1 | Sí | Registrar cada uso con lo rechazado y por qué |
| Inconsistencia «Equipo de 4 personas» (OC5) | S2 | Sí | El equipo es de 3 según matrícula; corregir el documento |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_GimnasioUTB`, público |
| Estructura mínima | No cumple | Faltan `docs/arc42/`, `docs/adr/`, `docs/c4/` |
| Convención de nombres de ADR | Cumple (vacuo) | Sin ADR todavía |
| ADR aceptados sin reescribir | Cumple (vacuo) | Sin ADR todavía |
| `docs/ia.md` al día | No cumple | Único commit el 08-ago; sin entradas con rechazos y motivos |
| Sin credenciales en el repositorio ni en el historial | Cumple | Greps limpios, incluidos blobs borrados |
| Contribución de todos los integrantes | No cumple | 2 cuentas de 3; Sebastián Caicedo sin aparición |
| Pipeline en verde | No verificado | Sin `.github/workflows/`; no exigible en semanas 1 y 2 |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Sebastian Felipe Caicedo Acosta | sin cuenta atribuible | 0 | 0 | — | No aparece en el historial ni en S1 ni en S2 |
| Rodrigo Andres Facio Lince Beltran | RodrigoFacioLince (correo omitido) | 3 | 0 | — | Primer commit 2026-08-16 |
| Pedro Luis Pallares De La Hoz | PedroPambi (correo omitido) | 8 | 0 | — | Único contribuidor en S1 |

Correspondencia cuenta↔persona inferida del correo institucional de los commits; la confirma el docente.

## Preguntas abiertas para la sustentación

- ¿Sebastián Caicedo tiene acceso al repositorio? Si no, ¿cómo va a cumplir el criterio de contribución del proyecto final?
- ¿El diagrama C4 (imagen) tiene leyenda y flechas etiquetadas? (no se pudo inspeccionar desde el repositorio).
- ¿Por qué 8 escenarios si la ficha pedía entre 3 y 5?
