# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | LostVault |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Integrantes y su usuario de GitHub | Jose Faustino Espana Noriega · Roy Andres Gonzalez Blanco · Shamara Llorente Tapias · Kiefer Monterroza Manjarres — identidades del historial: Roy Gonzalez (¿`RGBlanco18`?), `shamarallorente-blip`, `Fausto-4` (correo `ganonimo2504`), `weller-rar` (correo `pelu.kiefer`); correspondencias por confirmar con el docente |
| URL del sistema desplegado | — |
| Última revisión | 2026-08-24 (S3 actualizada tras el cierre, commit `1ddb826`) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `560ba89` · 2026-08-09T21:10:31-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `af94a30` · 2026-08-16T22:09:43-05:00 | 7/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `1ddb826` · 2026-08-23T23:57:37-05:00 | 4/9 | no se publica | sí |
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
| Historial con una sola identidad de commits | S1 | no (S3 cierre: 4 identidades) | `weller-rar` apareció vía PR #4 en la actualización; confirmar la atribución de `Fausto-4` y `weller-rar` |
| `docs/ia.md` sin registro de lo rechazado ni de uso de IA en S3 | S1 | Sí (última entrada 08-ago) | Actualizar con los usos de S3 y lo rechazado con motivo |
| Estructura incompleta: sin `docs/c4/`; C4 en `docs/arc42/c4_contexto.png` | S1 | Sí | Mover el C4 a `docs/c4/` |
| Sección 4 y matriz comparativa genéricas, sin comparar contra los escenarios 1-4 | S3 | Sí | Reescribir la matriz fila por escenario del árbol de utilidad y ligar la estrategia a los escenarios |
| Paquetes de módulos del ADR inexistentes (solo `lib/main.dart`) | S3 | Sí | Crear `lib/<modulo>/` con la frontera `public/` que declara el ADR; el checklist del README los da por creados |
| ADR no alcanzable desde `aspectos.md` ni desde los escenarios | S3 | Sí | Enlazar el ADR desde la fila del aspecto y desde el escenario que lo motiva |
| Archivos basura en la raíz (`front_end`, `ejecutable`, 1 byte) | S3 (cierre) | Sí | Borrar los residuos de los zips subidos en `cd5ee95`…`1ddb826` |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `github.com/ISCOUTB/AS_202620_LostVault`, público (ls-remote sin auth) |
| Estructura mínima | No cumple | Sin `docs/c4/`; C4 en `docs/arc42/c4_contexto.png` |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico.md` |
| ADR aceptados sin reescribir | Cumple | Creación (`723d9e6`) + renombrado (`d0e7078`), sin reescritura |
| `docs/ia.md` al día | No cumple | Última entrada 08-ago; sin lo rechazado |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep, .env y `log -S` sin coincidencias |
| Contribución de todos los integrantes | Cumple | 4 identidades de 4 en `1ddb826`; atribución de `Fausto-4` y `weller-rar` por confirmar |
| Pipeline en verde | No verificado | Sin `.github/workflows/`; prueba localizada sin evidencia de ejecución |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---|---:|---:|---:|---|
| Jose Faustino Espana Noriega | ¿`Fausto-4`? (correo `ganonimo2504`, sin confirmar) | 1 (via PR #3) | — | — | Apareció en S3 con «Add files via upload»; correspondencia por confirmar con el docente |
| Roy Andres Gonzalez Blanco | «Roy Gonzalez» en commits (¿`RGBlanco18`?) — confirmar | 24 (HEAD) | 2 PR mergeados (#1, #3) | — | Principal autor; hace los merges |
| Shamara Llorente Tapias | `shamarallorente-blip` (correo institucional `shllorente@utb.edu.co`) | 1 (via PR #1) | 0 | — | Autora del ADR 0001 |
| Kiefer Monterroza Manjarres | ¿`weller-rar`? (correo `pelu.kiefer`, sin confirmar) | 1 (via PR #4) | 0 | — | Primera aparición en la actualización S3 (PR #4: «Create ejecutable») |

## Preguntas abiertas para la sustentación

- ¿Quién es la cuenta `Fausto-4` (correo `ganonimo2504`) y la cuenta `weller-rar` (correo `pelu.kiefer`)?
- C4 de contexto: ¿tiene leyenda y flechas etiquetadas? Solo existe como imagen.
- ¿Por qué la matriz comparativa de S3 no usa los escenarios 1-4 del equipo (tabla genérica)?
- ¿Cuándo van a crear los paquetes `lib/<modulo>/` que declara el ADR (hoy solo `lib/main.dart`) y a mover el C4 a `docs/c4/`?
