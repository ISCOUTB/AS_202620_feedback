# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo InvenTrack. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | InvenTrack |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Integrantes y su usuario de GitHub | Javier Alejandro Carta Lacharme · Esteban Javier Peluffo Marquez · Felix Andres Taborda Jimenez · Jose Gabriel Vargas Perez — cuentas abajo |
| URL del sistema desplegado | sin desplegar aún |
| Última revisión | 2026-08-24 (revisión S3, actualizada tras el cierre) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `06920209` · 2026-08-09T16:03:46-05:00 | 4/9 | 2,8 * | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `db90ff2f` · 2026-08-16T21:22:20-05:00 | 9/9 | 5,0 * | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `dd4ea1cb8` · 2026-08-23T23:46:24-05:00 | 9/9 | no se publica | sí (actualizada tras el cierre) |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Javier Carta Lacharme sin commits ni cuenta atribuible | S1 | Cerrado en S3: `jxviercarta-a11y` firma 3 commits en el periodo (atribución por confirmar con el docente) | Verificar acceso al repositorio y empezar a contribuir (la contribución individual se califica en el final) |
| `docs/aspectos.md` en prosa, sin la tabla de 8 columnas del contrato | S1 | Cerrado en S3 (`8ba799f`): tabla de 8 columnas con enlace al ADR desde ASP-01 | Convertir a tabla ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia; además enlazar el ADR 0001 desde la fila del aspecto y desde ESC-01/ESC-02 |
| `docs/adr/README.md` haría fallar el filtro de nombres de ADR (placeholder) | S2 | Cerrado en S3 (`2abab34` lo eliminó) | Resuelto |
| ADR 0001 en estado «propuesto» y no alcanzable desde `aspectos.md` ni desde los escenarios que lo motivan | S3 | Parcialmente cerrado: los dos enlaces ya existen (ASP-01 y ESC-01); sigue «propuesto, pendiente de ratificación» | Ratificar (aceptar) el ADR |
| `ia.md` sin lo rechazado y su motivo en la entrada S3 | S3 | Cerrado en S3 (`8ba799f`): columna «Rechazado / motivo» llena | Resuelto |
| Prueba sin pipeline ni evidencia de ejecución | S3 | Cerrado en S3 (`3e2a54b`): workflow añadido y CI en verde sobre el hash calificado | Resuelto |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_InvenTrack`, público |
| Estructura mínima | Cumple | Seis rutas presentes; arc42 en `docs/arc42/arc42-template-EN.md` |
| Convención de nombres de ADR | Cumple | `0001-usar-monolito-modular-con-hexagonal-por-modulo.md`; placeholder eliminado |
| ADR aceptados sin reescribir | Cumple | Estado «propuesto»; churn pre-aceptación anotado (borrado `1375411` y restaurado por merge) |
| `docs/ia.md` al día | Cumple | Entrada S3 con «Rechazado / motivo» llena |
| Sin credenciales en el repositorio ni en el historial | Cumple | Greps limpios |
| Contribución de todos los integrantes | Cumple | 4 identidades consolidadas de 4; `jxviercarta-a11y` (Javier Carta, por confirmar) con 3 commits en S3 |
| Pipeline en verde | Cumple | Run «Run Tests» success sobre `dd4ea1cb` (https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/32691253620) |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---|---:|---:|---:|---|
| Javier Alejandro Carta Lacharme | `jxviercarta-a11y` (atribución por confirmar) | 3 (S3) | 0 | — | Apareció en S3 (ficha, README, C4) |
| Esteban Javier Peluffo Marquez | Esteban Peluffo (correo omitido) | 3 (S3) | 0 | — | ia.md y entrega semanal |
| Felix Andres Taborda Jimenez | FlexT21 + «Felix Taborda» (mismo noreply, consolidado) | 1 (S3) | 0 | — | Correspondencia por confirmar con el docente |
| Jose Gabriel Vargas Perez | Josephva24 + «Jose Vargas» (mismo correo `jgabrielvp24@gmail.com`, consolidado) | 6 (S3) | 0 | — | ADR, esqueleto, workflow de CI y ajustes de trazabilidad |

## Preguntas abiertas para la sustentación

- ¿`jxviercarta-a11y` corresponde efectivamente a Javier Carta Lacharme?
- ¿`FlexT21` corresponde efectivamente a Felix Taborda?
- ¿Por qué el ADR 0001 sigue «propuesto» y cuándo lo ratifican como aceptado?
