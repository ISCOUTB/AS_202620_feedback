# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | LostVault |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Integrantes y su usuario de GitHub | Jose Faustino Espana Noriega · Roy Andres Gonzalez Blanco · Shamara Llorente Tapias · Kiefer Monterroza Manjarres — historial con una sola identidad de commits: «Roy Gonzalez» (EQUIPOS.md observa `RGBlanco18`; correspondencia por confirmar con el docente) |
| URL del sistema desplegado | — |
| Última revisión | 2026-08-23 (S2, commit `af94a300`) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `560ba89` · 2026-08-09T21:10:31-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `af94a30` · 2026-08-16T22:09:43-05:00 | 7/9 | no se publica | sí |
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
| Historial con una sola identidad de commits; 3 de 4 integrantes sin aparición | S1 | sí (S2: 13/13 commits de la misma identidad) | Registrar quién no aparece; verificar acceso de todos los integrantes a la organización |
| `docs/ia.md` sin registro de lo rechazado ni de uso de IA en S2 | S1 | sí | Incluir por cada uso qué se rechazó y por qué; actualizar al documentar arc42 |
| Estructura incompleta: sin `docs/adr/` ni `docs/c4/`; C4 en `docs/arc42/` | S1 | sí | Crear las carpetas con `.gitkeep`; mover el C4 a `docs/c4/` |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `github.com/ISCOUTB/AS_202620_LostVault`, público (ls-remote sin auth) |
| Estructura mínima | No cumple | Sin `docs/adr/` ni `docs/c4/`; C4 en `docs/arc42/c4_contexto.png` |
| Convención de nombres de ADR | Cumple (vacuo) | Sin ADR todavía |
| ADR aceptados sin reescribir | Cumple (vacuo) | Sin ADR |
| `docs/ia.md` al día | No cumple | Único commit 2026-08-09; sin lo rechazado |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep, .env y `log -S` sin coincidencias |
| Contribución de todos los integrantes | No cumple | Una sola identidad en todo el historial |
| Pipeline en verde | No verificado | Sin `.github/workflows/` (no exigido aún) |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Jose Faustino Espana Noriega | sin cuenta observada | 0 | — | — | Sin aparición en el historial hasta S2 |
| Roy Andres Gonzalez Blanco | «Roy Gonzalez» en commits (¿`RGBlanco18`?) — confirmar | 13 (HEAD) | — | — | Único autor observado |
| Shamara Llorente Tapias | sin cuenta observada | 0 | — | — | Sin aparición en el historial hasta S2 |
| Kiefer Monterroza Manjarres | sin cuenta observada | 0 | — | — | Sin aparición en el historial hasta S2 |

## Preguntas abiertas para la sustentación

- ¿Los tres integrantes sin commits tienen acceso a la organización y en qué se espera que contribuyan?
- C4 de contexto: ¿tiene leyenda y flechas etiquetadas? Solo existe como imagen.
