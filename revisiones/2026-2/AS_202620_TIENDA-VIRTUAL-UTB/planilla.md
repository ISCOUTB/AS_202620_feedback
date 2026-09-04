# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo a lo largo del semestre.

## Identificación

| | |
|---|---|
| Equipo | Tienda virtual UTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Integrantes y su usuario de GitHub | Shalom Jhoanna Arrieta Marrugo (shalom-A26) · Levis Adrian Ortiz Cano (RAZOR7150) · Alejandro Patron Montero (pxtroniwnl) · Jasen Mihovil Yukopila Escobar (Jmyukopila) — correspondencias por los correos de los commits, por confirmar con el docente |
| URL del sistema desplegado | sin URL (sin despliegue todavía) |
| Ultima revision | 2026-09-03 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `d414ecf` · 2026-08-09T14:08:31-05:00 | 7/9 | 4.1 (propuesta) | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `456365b` · 2026-08-15T14:07:47-05:00 | 6/9 | 3.7 (propuesta) | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `f4602a3` · 2026-08-21T13:22:16-05:00 | 6/9 | no se publica | sí |
| 4 | S4 | `0d208a2` (2026-08-29T21:37:39-05:00) | 6/10 | 3.4 | si |
| 5 | Primer corte · reto de línea base | HEAD `0d401a9` (sin etiqueta) | 0/12 | subtotal técnico preliminar 0,00/4,00; sustentación pendiente | revisión manual preliminar 2026-09-03 |
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
| `docs/aspectos.md` sin la tabla de 8 columnas del curso (tabla de 2 columnas, sin ID ni enlaces a escenarios) | S1 | sí | Ajustar la tabla a las 8 columnas, enlazar cada escenario y ahora también el ADR 0001 (S3: sigue igual, sin ADR) |
| `docs/ia.md` sin registro de «qué se rechazó y por qué» | S1 | sí | Añadir las entradas de rechazo con motivo técnico (S3: el commit tocó el archivo, pero sigue sin rechazados) |
| Shalom Jhoanna Arrieta Marrugo sin commits en el historial | S1 (y S2) | No (cerrado en S3: commit `f4602a3` 21-ago) | Primer commit el 2026-08-21 (ya dentro del cierre S3) |
| Matriz comparativa de estilos genérica, no contra el árbol de utilidad | S3 (21-ago) | sí | Rehacer la tabla contra los escenarios del árbol: qué escenario mejora/empeora con cada estilo |
| Verificar secciones 5, 6, 9, 10 y 12 del arc42 | S4 | si | |
| Trazabilidad del ADR 0001 | S4 | si | |
| Columnas de docs/aspectos.md | S4 | si | |
| Columna de rechazos en docs/ia.md | S4 | si | |
| SonarCloud en pipeline | S4 | si | |
| Resolver el reto del corte 1: ADR con alternativas y consecuencias, diagnóstico con línea base, cambio implementado y medición contra umbral. | S5 | si | |
| Completar docs/aspectos.md con las 8 columnas del contrato. | S5 | si | |
| Configurar SonarCloud en el pipeline. | S5 | si | |
| Registrar en docs/ia.md los usos de IA del corte 1 con descartes y motivos. | S5 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB`, público |
| Estructura mínima | Cumple | seis rutas presentes; desviación: escenarios en `docs/escenarios-calidad.md` con arc42 §10 vacía |
| Convención de nombres de ADR | Cumple | `0001-monolito-modular.md` |
| ADR aceptados sin reescribir | Cumple | un solo commit sobre el ADR (`f4602a3`) |
| `docs/ia.md` al día | No cumple | commit en el periodo, pero sin registro de rechazos con motivo |
| Sin credenciales en el repositorio ni en el historial | Cumple | greps limpios; `compose.yaml:7` lleva contraseña de desarrollo del Postgres local |
| Contribución de todos los integrantes | Cumple | 4 identidades consolidadas = 4 integrantes (Shalom ya aparece) |
| Pipeline en verde | No cumple | run «Pruebas» success 2026-08-21T18:36Z (actions/runs/32514183233) |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Jasen Mihovil Yukopila Escobar | Jmyukopila (firma «Jasen» y «Jasen Yukopila», mismo correo) | 4 | — | — | base de S1 y S3 |
| Levis Adrian Ortiz Cano | RAZOR7150 | 2 | — | — | — |
| Alejandro Patron Montero | pxtroniwnl | 2 | — | — | S2 |
| Shalom Jhoanna Arrieta Marrugo | shalom-A26 | 1 | — | — | primer commit 2026-08-21 (S3) |

## Preguntas abiertas para la sustentación

- ¿Los cuatro integrantes tienen acceso de escritura al repositorio? (sin API no se pudo listar colaboradores).
- ¿Por qué la sección 10 del arc42 está vacía si los escenarios existen en `docs/escenarios-calidad.md`?
- ¿El arranque real con `docker compose up --build` funciona en el entorno del equipo? (no ejecutado por regla del kit)
