# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | mapsutb |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Integrantes y su usuario de GitHub | Carlos Alberto Galvis Zuluaga · Carlos David Manrique Fals · Nerlis Nikol Otero Perez · Isabel Sofia Paez Matallana — cuentas observadas en el historial: `charlygz21`, `nerlis-otero`, `CarlosManrique-1397` (correspondencias por confirmar con el docente) |
| URL del sistema desplegado | — |
| Última revisión | 2026-08-23 (S2, commit `1cf15768`) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `7e56ad3` · 2026-08-09T23:27:46-05:00 | 5/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `1cf1576` · 2026-08-16T21:26:05-05:00 | 4/9 | no se publica | sí |
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
| Estructura fuera de convención: sin `docs/arc42/`, `docs/adr/`, `docs/c4/` | S1 | sí (S2: arc42 en un único `docs/arc42.md`, contexto en `docs/c4_contexto.md`) | Mover a la estructura mínima del contrato |
| Sin tensiones de calidad en la ficha (S1) → árbol de utilidad sin impacto/riesgo (S2) | S1 | sí | Priorizar atributos por impacto y riesgo y vincularlos a los escenarios |
| Isabel Sofia Paez Matallana sin aparición en el historial | S1 | sí (3 identidades para 4 integrantes) | Confirmar acceso y contribución de la integrante |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `github.com/ISCOUTB/AS_202620_mapsutb`, público (ls-remote sin auth) |
| Estructura mínima | No cumple | Arc42 en archivo único; sin `docs/adr/` ni `docs/c4/` |
| Convención de nombres de ADR | Cumple (vacuo) | Sin ADR todavía |
| ADR aceptados sin reescribir | Cumple (vacuo) | Sin ADR |
| `docs/ia.md` al día | No cumple en S2 | Único commit 2026-08-09; sin uso de IA registrado en S2 (sí tiene Aceptado/Rechazado) |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep, .env y `log -S` sin coincidencias |
| Contribución de todos los integrantes | No cumple | 3 identidades; sin cuenta para Isabel Sofia Paez Matallana |
| Pipeline en verde | No verificado | Sin `.github/workflows/` (no exigido aún) |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Carlos Alberto Galvis Zuluaga | ¿`charlygz21`? (confirmar) | 3 | — | — | Commits entre S1 y S2 |
| Carlos David Manrique Fals | ¿`CarlosManrique-1397`? (confirmar) | 1 | — | — | Solo el commit de la entrega S2 |
| Nerlis Nikol Otero Perez | ¿`nerlis-otero`? (confirmar) | 4 | — | — | Mayoría de la documentación S1 |
| Isabel Sofia Paez Matallana | sin cuenta observada | 0 | — | — | Sin aparición en el historial hasta S2 |

## Preguntas abiertas para la sustentación

- ¿Isabel Sofia Paez Matallana tiene acceso al repositorio y cómo contribuirá?
- ¿Dónde está el diagrama C4 de contexto (tabla no es diagrama)?
- Etiqueta `corte-1` colocada sobre el commit de S1: ¿se moverá al commit del corte real?
