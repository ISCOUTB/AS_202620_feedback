# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Recobra |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Integrantes y su usuario de GitHub | Camilo Andres Conde Corrales · Fernando Isacc Conde Herrera · Miguel Alejandro Iii Jacome Yanez · Veronica Ubarne Reyes — cuentas observadas: `Cconde31`, `MiguelJacome` (correspondencias por confirmar con el docente) |
| URL del sistema desplegado | — |
| Última revisión | 2026-08-23 (S2, commit `d2dac73`) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `da5c15d` · 2026-08-07T17:54:04-05:00 | 3/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `d2dac73` · 2026-08-16T23:44:54-05:00 | 4/9 | no se publica | sí |
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
| `docs/ia` vacío (y sin extensión .md) | S1 | sí (vacío también en S2) | Registrar usos de IA con lo aceptado y lo rechazado |
| `docs/aspectos.md` narrativo, sin tabla ni enlaces a escenarios | S1 | sí (sin cambios en S2) | Tabla de 8 columnas y enlaces a los escenarios |
| Sin diagrama C4 (solo descripción textual) | S1 (estructura ausente) | sí | Diagrama como código, con leyenda y flechas, en `docs/c4/` |
| Fernando Isacc Conde Herrera y Veronica Ubarne Reyes sin aparición en el historial | S1 | sí (2 identidades para 4 integrantes) | Confirmar acceso y contribución |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público (ls-remote sin auth) |
| Estructura mínima | No cumple | Archivos sueltos en `docs/`; sin `docs/arc42/`, `docs/adr/`, `docs/c4/` |
| Convención de nombres de ADR | Cumple (vacuo) | Sin ADR (el primero llega el 22-08) |
| ADR aceptados sin reescribir | Cumple (vacuo) | Sin ADR |
| `docs/ia.md` al día | No cumple | Archivo vacío |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep, .env y `log -S` sin coincidencias |
| Contribución de todos los integrantes | No cumple | 2 identidades para 4 integrantes |
| Pipeline en verde | No verificado | Sin `.github/workflows/` (no exigido aún) |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Camilo Andres Conde Corrales | ¿`Cconde31`? (confirmar) | 10 | — | — | Mayoría de S2 |
| Fernando Isacc Conde Herrera | sin cuenta observada | 0 | — | — | Sin aparición en el historial hasta S2 |
| Miguel Alejandro Iii Jacome Yanez | ¿`MiguelJacome`? (confirmar) | 4 | — | — | Trabajo de S1 |
| Veronica Ubarne Reyes | sin cuenta observada | 0 | — | — | Sin aparición en el historial hasta S2 |

## Preguntas abiertas para la sustentación

- ¿Fernando Isacc Conde Herrera y Veronica Ubarne Reyes tienen acceso al repositorio y cómo contribuirán?
- ¿Cuándo llenarán `docs/ia.md` y entregarán el C4 como diagrama?
