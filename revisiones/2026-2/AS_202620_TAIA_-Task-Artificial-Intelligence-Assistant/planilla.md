# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | TAIA |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo |
| URL del sistema desplegado | — |
| Última revisión | 2026-08-23 (S1 `76d4a91` + S2 `59590c9`) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `76d4a91` · 2026-08-07T03:34:26-05:00 | 6/9 | no aplica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `59590c9` · 2026-08-16T19:15:15-05:00 | 3/9 | no aplica | sí |
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
| `docs/adr/` inexistente | S1 (08-07) | Sí, en S2 | Crear el directorio (ya se creó el 22-ago con `0001`, fuera del cierre de S2) |
| Tensiones de calidad sin declarar en la ficha | S1 (08-07) | Sí, en S2 | Enfrentar dos atributos de calidad en la ficha del problema |
| `docs/aspectos.md` con la trazabilidad en «Pendiente» y sin enlaces a los escenarios | S1 (08-07) | Sí, en S2 | Enlazar escenarios, C4 y ADR desde cada fila |
| Documentación de calidad fuera del arc42 (`docs/calidad/`) con la sección 10 vacía | S2 (16-ago) | Sí | Mover o enlazar los escenarios y el árbol desde la sección 10 |
| Escenario 5 sin medida numérica; árbol de utilidad sin impacto/riesgo | S2 (16-08) | Sí | Completar la medida del escenario 5 y anotar impacto/riesgo en el árbol |
| C4 solo como imagen (PNG), sin verificar leyenda ni flechas | S2 (16-08) | Sí | Preferir diagrama como código (Mermaid) y confirmar leyenda y etiquetas |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `lsremote.txt:18`; público y con el nombre de la convención |
| Estructura mínima | No cumple | Falta `docs/adr/` en `59590c9` (se crea post-cierre) |
| Convención de nombres de ADR | Cumple | Sin ADR al cierre de S2 |
| ADR aceptados sin reescribir | Cumple | Sin ADR al cierre de S2 |
| `docs/ia.md` al día | Cumple | Entradas 001 y 002 (la 002 sin rechazados) |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 y `git log -S` sin coincidencias |
| Contribución de todos los integrantes | Cumple | Los 4 integrantes constan en el historial al cierre de S2 |
| Pipeline en verde | No aplica todavía | Sin `.github/workflows`; se espera desde el segundo corte |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Valeria Estefania Berrio Payares | val (2 identidades: `@email.com` y `@gmail.com`) | 3 (2+1, consolidadas) | | | También los commits de S3 (22-ago) |
| Deiner De Jesus Gonzalez Paredes | dei0811 | 1 | | | C4 de contexto (16-ago) |
| Luis Eduardo Mendoza Angulo | luis20072002 | 1 | | | arc42 (15-ago) |
| Mark Steven Pastrana Koreia | mark | 1 | | | Escenarios (16-ago); la cuenta «EtienneGW» del listado no aparece en el historial — correspondencia por confirmar |

## Preguntas abiertas para la sustentación

- ¿La cuenta «mark» es la misma persona que «EtienneGW» del listado de EQUIPOS.md?
- ¿El PNG del C4 de contexto incluye leyenda y flechas etiquetadas? (no verificable automáticamente)
- ¿Por qué `README.md` está en UTF-16 LE y el resto del repositorio en UTF-8?
