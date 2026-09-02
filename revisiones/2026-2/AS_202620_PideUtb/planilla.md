# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | PideUtb |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Integrantes y su usuario de GitHub | Daniela Sofia Arrieta Guardo · Santiago Jose Cuesta Maza · Ruddy Rodriguez Romero — cuentas observadas: `daniarriet`, `Santiago Cuesta`/`Santiago-C0` (misma persona, EQUIPOS.md:95); sin cuenta para Ruddy |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-02 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `48cfbe3` · 2026-08-08T15:12:35-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `9b5f214` · 2026-08-16T12:47:26-05:00 | 9/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `b5f0310` · 2026-08-23T19:42:42-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `1636f20` (2026-08-30T22:17:18-05:00) | 1/10 | 1.4 | si |
| 5 | CORTE1 | `1636f20` (2026-08-30T22:17:18-05:00) | 0/12 | no aplica | si |
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
| Estructura fuera de convención: `arc42.md` en raíz, C4 dentro de arc42, sin `docs/c4/`, ficha en PDF | S1 | sí (S3: `docs/adr/` ya existe) | Mover arc42 y C4 a `docs/arc42/` y `docs/c4/`; ficha en Markdown |
| `docs/ia.md` sin registro de lo rechazado | S1 | sí | Incluir la columna de rechazos con motivo en cada uso |
| Ruddy Rodriguez Romero sin aparición en el historial | S1 | sí (2 personas de 3 en S3) | Confirmar acceso y contribución del integrante |
| Sección 4 sin tácticas por escenario; matriz comparativa sin filas por escenario | S3 | sí | Ligar estrategia y matriz a ESC-01/02/03 del árbol de utilidad |
| `docs/aspectos.md` sin enlace al ADR ni tabla de 8 columnas | S3 | sí | Completar la tabla de trazabilidad y enlazar el ADR desde el aspecto y el escenario |
| Sin workflow ni evidencia de prueba en verde | S3 | sí | Añadir `.github/workflows/` con `pytest` y aportar el run |
| C4 niveles 1 y 2 en docs/c4/ | S4 | si | |
| Glosario (sección 12) y secciones 1-6, 9, 10 de arc42 verificables | S4 | si | |
| Tabla de aspectos con columnas ID, C4, ADR, Código | S4 | si | |
| Trazabilidad del ADR a commit y pruebas | S4 | si | |
| docs/ia.md con lo rechazado | S4 | si | |
| CI con pruebas en verde | S4 | si | |
| Eliminar .venv-1 del repositorio | S4 | si | |
| Confirmar etiqueta corte-1 | S5 | si | |
| Documentar restricción y diagnóstico | S5 | si | |
| Crear ADR del reto | S5 | si | |
| Completar docs/arc42/ y docs/c4/ | S5 | si | |
| Reestructurar docs/aspectos.md a 8 columnas | S5 | si | |
| Evidencia de CI y medición | S5 | si | |
| Entrada de IA del corte en docs/ia.md | S5 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público hoy; estuvo privado al inicio (EQUIPOS.md:49-52) |
| Estructura mínima | No cumple | `arc42.md` en raíz; C4 dentro de arc42 §3.2; sin `docs/c4/`; ficha en PDF |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico.md` pasa el filtro; título temático (no decisión) |
| ADR aceptados sin reescribir | Cumple | ADR creado en `b5f0310`, sin reescrituras |
| `docs/ia.md` al día | No cumple | Actualizado en S3 (`b5f0310`), pero sin lo rechazado |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep y `.env` sin coincidencias |
| Contribución de todos los integrantes | No cumple | 2 personas (daniarriet; Santiago Cuesta=Santiago-C0) de 3 |
| Pipeline en verde | No verificado | Sin `.github/workflows/` ni evidencia de ejecución |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Daniela Sofia Arrieta Guardo | ¿`daniarriet`? (confirmar) | 5 | — | — | Concentra la documentación S2 |
| Santiago Jose Cuesta Maza | `Santiago Cuesta` / `Santiago-C0` (misma persona) | 5 | — | — | Entrega S3 completa (ADR, esqueleto, README) |
| Ruddy Rodriguez Romero | sin cuenta observada | 0 | — | — | Sin aparición en el historial hasta S3 |

## Preguntas abiertas para la sustentación

- ¿Ruddy Rodriguez Romero tiene acceso al repositorio y cómo contribuirá?
- ¿Cuándo moverán `arc42.md` y el C4 a la estructura mínima y la ficha a Markdown?
- ¿Quién ejecutó `pytest` en verde y pueden aportar la evidencia del run?
