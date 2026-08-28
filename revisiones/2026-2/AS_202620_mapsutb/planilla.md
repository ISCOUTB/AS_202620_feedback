# Planilla de equipo · mapsutb

## Identificación

| | |
|---|---|
| Equipo | mapsutb |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Integrantes y su usuario de GitHub | Carlos Alberto Galvis Zuluaga · Carlos David Manrique Fals · Nerlis Nikol Otero Perez · Isabel Sofia Paez Matallana — cuentas observadas en el historial: `charlygz21`, `nerlis-otero`, `CarlosManrique-1397` (correspondencias por confirmar con el docente) |
| URL del sistema desplegado | — |
| Ultima revision | 2026-08-28 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `7e56ad3` · 2026-08-09T23:27:46-05:00 | 5/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `1cf1576` · 2026-08-16T21:26:05-05:00 | 4/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `ed55eda` · 2026-08-23T21:44:05-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `75ca174` (2026-08-28T10:17:59-05:00) | 1/10 | 1.4 | si |
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
| Estructura fuera de convención: `docs/arc42.md` único y `docs/c4_contexto.md` fuera de `docs/c4/` | S1 | sí | Mover a la estructura mínima del contrato |
| Sin tensiones de calidad en la ficha (S1) → árbol de utilidad sin impacto/riesgo (S2) | S1 | sí | Priorizar atributos por impacto y riesgo y vincularlos a los escenarios |
| Isabel Sofia Paez Matallana sin aparición en el historial | S1 | sí (S3: 3 identidades para 4 integrantes; toda la S3 de una sola cuenta) | Confirmar acceso y contribución de la integrante |
| Etiqueta `corte-1` sobre el commit de S1 | S2 | sí | moverla al commit real del corte 1 |
| `docs/aspectos.md` desactualizado («Sin ADR aún») y sin enlace al ADR 0001; `escenarios_calidad.md` con enlace roto al árbol | S3 | sí | actualizar la tabla y enlazar el ADR desde el escenario que lo motiva |
| Sin matriz comparativa de los tres estilos contra el árbol de utilidad (el ADR la declina; el «corte anterior» no existe en el repo) | S3 | sí | escribir la matriz de estilos que pide la ficha |
| Estructura de paquetes del ADR no materializada (`lib/` solo tiene `main.dart`; faltan carpetas y `.gitkeep`) | S3 | sí | crear las carpetas del ADR antes de la S4 |
| `docs/ia.md` sin entradas del trabajo S3 | S3 | sí | registrar el uso de IA de la semana con rechazados y motivo |
| Prueba de humo sin CI ni evidencia de verde | S3 | sí | pipeline o run aportado |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `github.com/ISCOUTB/AS_202620_mapsutb`, público (ls-remote sin auth) |
| Estructura mínima | No cumple | `docs/arc42.md` único; `docs/c4_contexto.md` fuera de `docs/c4/`; `docs/adr/` ya existe |
| Convención de nombres de ADR | Cumple | `0001-patrones-de-diseno.md` |
| ADR aceptados sin reescribir | Cumple | un solo commit sobre el ADR |
| `docs/ia.md` al día | No cumple | tocado en S3 solo con cambio de saltos de línea; sin entradas nuevas |
| Sin credenciales en el repositorio ni en el historial | Cumple | greps limpios |
| Contribución de todos los integrantes | No cumple | 3 identidades; sin cuenta para Isabel Sofia Paez Matallana; S3 de una sola cuenta |
| Pipeline en verde | No verificado | sin `.github/workflows/` ni evidencia de ejecución |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Carlos Alberto Galvis Zuluaga | ¿`charlygz21`? (confirmar) | 3 | — | — | Commits de S1 |
| Carlos David Manrique Fals | ¿`CarlosManrique-1397`? (confirmar) | 6 | — | — | toda la entrega S3 (21:32–21:44 del 23/08) |
| Nerlis Nikol Otero Perez | ¿`nerlis-otero`? (confirmar) | 4 | — | — | documentación S1 |
| Isabel Sofia Paez Matallana | sin cuenta observada | 0 | — | — | Sin aparición en el historial hasta S3 |

## Preguntas abiertas para la sustentación

- ¿Isabel Sofia Paez Matallana tiene acceso al repositorio y cómo contribuirá?
- ¿Dónde está el diagrama C4 de contexto (tabla no es diagrama)?
- ¿La app compila y la prueba de humo pasa en verde en el entorno del equipo? (sin CI ni evidencia)
- ¿Cuándo se creará la estructura `lib/{adapters,repositories,strategies,services,features}` que declara el ADR?
