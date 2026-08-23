# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo a lo largo del semestre.

## Identificación

| | |
|---|---|
| Equipo | XALD |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Integrantes y su usuario de GitHub | Xavier Yesid Garcia Diaz (xaviergarciadiaz20-commits) · Dilan Joan Gonzalez Bejarano (dilanbejarano011) · Luis Estheban Lozano Colmenares (colmenares2007-crypto) · Axel Jair Ruiz Bolano (axeljruiz717-hash) — correspondencias por los correos de los commits (nombres explícitos), por confirmar con el docente |
| URL del sistema desplegado | sin URL (sin despliegue todavía) |
| Última revisión | 2026-08-23 (S1 y S2) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `bf81545` · 2026-08-08T13:39:21-05:00 | 5/9 | 3.2 (propuesta) | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `8c37887` · 2026-08-16T13:45:27-05:00 | 1/9 | 1.4 (propuesta) | sí |
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
| Ficha del problema sin usuarios, sin alcance y sin tensiones de calidad enfrentadas | S1 | sí | completar la ficha (S2: sigue igual) |
| Restos de edición de herramientas de IA («```[cite: 1]») en `docs/aspectos.md` | S1 | sí | limpiar el archivo |
| Restricciones sin clase legal y con decisiones presentadas como restricciones | S2 | sí | clasificar técnicas/organizativas/legales con origen |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_XALD`, público (antes privado: EQUIPOS.md) |
| Estructura mínima | Cumple | seis rutas presentes desde S2 (en S1 faltaban `docs/adr/` y `docs/c4/`) |
| Convención de nombres de ADR | No cumple | `ADR-001.md`…`ADR-005.md` (deben ser `NNNN-titulo-en-kebab-case.md`) |
| ADR aceptados sin reescribir | Cumple | creados una vez, sin ediciones posteriores |
| `docs/ia.md` al día | Cumple | registra rechazos con motivo técnico |
| Sin credenciales en el repositorio ni en el historial | Cumple | greps limpios |
| Contribución de todos los integrantes | Cumple | 4 identidades = 4 integrantes, con PR en el historial |
| Pipeline en verde | No verificado | sin pipeline todavía (no exigido aún) |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---:|---:|---:|---|
| Dilan Joan Gonzalez Bejarano | dilanbejarano011 | 28 | — | — | autor principal |
| Luis Estheban Lozano Colmenares | colmenares2007-crypto | 17 | — | — | — |
| Xavier Yesid Garcia Diaz | xaviergarciadiaz20-commits | 9 | — | — | actividad post-cierre el 23/08 (create/delete PROYECTO_XALD) |
| Axel Jair Ruiz Bolano | axeljruiz717-hash | 4 | — | — | — |

## Preguntas abiertas para la sustentación

- ¿Los commits del 23/08 («Create/Delete PROYECTO_XALD») fueron accidentales? Conviene aclararlo para no confundirlos con entregas.
- ¿Dónde quedaron los escenarios de calidad de seis partes y el árbol de utilidad de la entrega S2?
