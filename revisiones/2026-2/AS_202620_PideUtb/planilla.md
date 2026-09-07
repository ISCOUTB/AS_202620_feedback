# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | PideUtb |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Integrantes y su usuario de GitHub | Daniela Sofia Arrieta Guardo · Santiago Jose Cuesta Maza · Ruddy Rodriguez Romero — cuentas observadas: `daniarriet`, `Santiago Cuesta`/`Santiago-C0` (mismo correo, misma persona), `ruddy2000utb-droid` |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-07 (revisión definitiva post-cierre) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `48cfbe3` · 2026-08-08T15:12:35-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `9b5f214` · 2026-08-16T12:47:26-05:00 | 9/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `b5f0310` · 2026-08-23T19:42:42-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `1636f20` (2026-08-30T22:17:18-05:00) | 1/10 | 1.4 | si |
| 5 | Primer corte · reto de línea base | sin etiqueta; último commit ≤ cierre `1636f20` (30/08); HEAD post-cierre `c198b7a` (07/09, después de las 05:00 UTC) | 0/12 | subtotal técnico 0,00/4,00; sustentación pendiente | revisión definitiva post-cierre 2026-09-07 |
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
| Estructura fuera de convención: `arc42.md` en raíz, C4 dentro de arc42, sin `docs/c4/`, ficha en PDF | S1 | sí (post-cierre movieron `arc42.md` a `docs/` y crearon `docs/C4/`, pero en mayúsculas y sin fusionar en `docs/arc42/`) | Mover arc42 y C4 a `docs/arc42/` y `docs/c4/` en minúsculas |
| `docs/ia.md` sin registro de lo rechazado | S1 | sí | Incluir la columna de rechazos con motivo en cada uso |
| Ruddy Rodriguez Romero sin aparición en el historial | S1 | no (resuelto en S4) | En HEAD aparece `ruddy2000utb-droid`; mantener contribución distribuida |
| Sección 4 sin tácticas por escenario; matriz comparativa sin filas por escenario | S3 | sí | Ligar estrategia y matriz a ESC-01/02/03 del árbol de utilidad |
| `docs/aspectos.md` sin enlace al ADR ni tabla de 8 columnas | S3 | sí (confirmado en HEAD post-cierre: sigue siendo narrativo por atributo, no tabla de 8 columnas) | Completar la tabla de trazabilidad y enlazar el ADR desde el aspecto y el escenario |
| Sin workflow ni evidencia de prueba en verde | S3 | sí (confirmado post-cierre: sigue sin `.github/workflows/`) | Añadir `.github/workflows/` con `pytest` y aportar el run |
| C4 niveles 1 y 2 en docs/c4/ | S4 | sí (creado post-cierre pero como `docs/C4/`, mayúsculas) | Renombrar a minúsculas |
| Glosario (sección 12) y secciones 1-6, 9, 10 de arc42 verificables | S4 | si | |
| Tabla de aspectos con columnas ID, C4, ADR, Código | S4 | si | |
| Trazabilidad del ADR a commit y pruebas | S4 | si | |
| docs/ia.md con lo rechazado | S4 | si | |
| CI con pruebas en verde | S4 | si | |
| Eliminar .venv-1 del repositorio | S4 | sí (sigue versionado en HEAD) | Añadir `.gitignore` y sacarlo del historial |
| Etiqueta `corte-1` ausente; HEAD sigue en S4 | S5 | sí (confirmado post-cierre: nunca se creó, tampoco tras seguir trabajando el 07/09 después del cierre) | Crear la etiqueta sobre el commit real del corte antes del cierre — no se hizo |
| Documentar restricción y diagnóstico | S5 | si | |
| Crear ADR del reto | S5 | si | |
| Completar docs/arc42/ y docs/c4/ | S5 | si | |
| Reestructurar docs/aspectos.md a 8 columnas | S5 | si | |
| Evidencia de CI y medición | S5 | si | |
| Entrada de IA del corte en docs/ia.md | S5 | si | |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público hoy; estuvo privado al inicio (EQUIPOS.md) |
| Estructura mínima | No cumple | En el estado calificado (`1636f20`), `arc42.md` en raíz y sin `docs/c4/`; en HEAD post-cierre mejoró parcialmente (`docs/C4/`, mayúsculas) pero sigue sin `docs/arc42/` |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico.md` pasa el filtro; título temático (no decisión) |
| ADR aceptados sin reescribir | Cumple | ADR creado en `b5f0310`, sin reescrituras hasta HEAD |
| `docs/ia.md` al día | No cumple | Sin entrada de S5 ni post-cierre |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep y `.env` sin coincidencias reales en HEAD |
| Contribución de todos los integrantes | Cumple | 3 personas consolidadas en HEAD: daniarriet, Santiago Cuesta/Santiago-C0, ruddy2000utb-droid |
| Pipeline en verde | No verificado | Sin `.github/workflows/` en ningún punto del historial |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits (HEAD) | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Daniela Sofia Arrieta Guardo | ¿`daniarriet`? (confirmar) | 21 | — | — | Autora de casi toda la actividad post-cierre del 07/09 |
| Santiago Jose Cuesta Maza | `Santiago Cuesta` / `Santiago-C0` (mismo correo) | 10 | — | — | Entrega S3 completa (ADR, esqueleto, README) |
| Ruddy Rodriguez Romero | `ruddy2000utb-droid` | 2 | — | — | Apareció desde S3/S4 |

## Preguntas abiertas para la sustentación

- ¿Por qué no se creó la etiqueta `corte-1`, ni antes ni después del cierre, pese a seguir trabajando el mismo día 7/09?
- ¿Cuándo terminarán de mover `arc42.md` y C4 a la estructura mínima en minúsculas?
- ¿Quién ejecutó `pytest` en verde y pueden aportar la evidencia del run?
