# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Recobra |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Integrantes y su usuario de GitHub | Camilo Andres Conde Corrales · Fernando Isacc Conde Herrera · Miguel Alejandro Iii Jacome Yanez · Veronica Ubarne Reyes — cuentas consolidadas: `Cconde31` (incluye la identidad `Steamlinker`, unificada por `.mailmap` el 05/09), `MiguelJacome`, `vylrir` (Verónica Ubarne), y el commit real de Fernando Isacc Conde Herrera (`fconde@utb.edu.co`) |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-07 (revisión definitiva post-cierre) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `da5c15d` · 2026-08-07T17:54:04-05:00 | 3/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `d2dac73` · 2026-08-16T23:44:54-05:00 | 4/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `cb5c579` · 2026-08-23T23:44:12-05:00 | 4/9 | no se publica | sí |
| 4 | S4 | `2268b33` (2026-08-30T22:34:56-05:00) | 2/10 | 1.8 | si |
| 5 | Primer corte · reto de línea base | `corte-1` → `f7c1a6c` (2026-09-07T14:59:41Z, **posterior al cierre**) | 10/12 | subtotal técnico 4,00/4,00; sustentación pendiente; **versionado No cumple por entrega tardía de la etiqueta** | revisión definitiva post-cierre 2026-09-07 |
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
| `docs/ia` vacío (y sin extensión .md) | S1 | no (resuelto: `docs/ia.md` con entradas por integrante y por semana, incluida S5) | Borrar el `docs/ia` vacío y completar el registro con todos los integrantes |
| `docs/aspectos.md` narrativo, sin tabla ni enlaces | S1 | no (resuelto: tabla de 8 columnas, filas A1-A4, navegable) | Tabla de 8 columnas y enlaces a escenarios y ADR |
| Sin diagrama C4 (solo descripción textual) | S1 | no (resuelto: `docs/c4/README.md`) | Borrar el C4 textual antiguo |
| Fernando Isacc Conde Herrera y Veronica Ubarne Reyes sin aparición en el historial | S1 | parcial (Verónica consolidada como `vylrir`, 9 commits; Fernando sigue con 1 solo commit en todo el semestre) | Confirmar acceso, contribución sustantiva y reparto real de trabajo con Fernando |
| ADR fuera de convención (`docs/ADR/01-…`, sin motivo de descarte); el ADR viejo se borró sin marcarlo reemplazado | S3 | no (resuelto: ADR-0001 ahora dice explícitamente "Reemplazada por ADR-0002 - 2026-09-05" en vez de borrarse) | Mantener la práctica en ADR futuros: nunca borrar un ADR aceptado |
| Matriz comparativa genérica, no contra el árbol de utilidad | S3 | sin verificar en esta pasada (foco de esta revisión fue el reto de S5) | Revisar en el próximo corte |
| Sin esqueleto ejecutable (código, prueba, comando de arranque) | S3 | no (resuelto: NestJS + Flutter ejecutables, con pruebas y CI) | — |
| `node_modules/` completo versionado | S3 (cierre) | no en HEAD, pero **el token de Coveralls que contenía sigue en el historial sin rotar** (`905f546:node_modules/debug/.coveralls.yml`) | Rotar el token de Coveralls y confirmarlo en la sustentación; valorar limpiar el historial con `git filter-repo` si el docente lo pide |
| Implementar el corte vertical real (src/domain, src/application, src/infrastructure, tests/) | S4 | no (resuelto en la migración a NestJS de S5) | — |
| Corregir secciones 5 y 6 de arc42 y añadir la sección 9 | S4 | parcial (`docs/arc42.md` suelto convive con `docs/arc42/04-estrategia-solucion.md`) | Consolidar en una sola ubicación (`docs/arc42/` con secciones) |
| Completar tabla de aspectos con las 8 columnas | S4 | no (resuelto) | — |
| Alinear C4 con el código real o reducir alcance | S4 | no (resuelto: C4 refleja NestJS/Flutter) | — |
| Configurar CI y ejecutar pruebas en verde | S4 | no (resuelto: `.github/workflows/ci.yml`, runs en verde antes y después del cierre) | — |
| Eliminar node_modules del repositorio y rotar el token expuesto | S4 | parcial (node_modules ya no se versiona; el token sigue sin rotar) | Rotar el token — sigue pendiente |
| Confirmar etiqueta corte-1 | S5 | sí, con matiz: existe pero es **posterior al cierre** | La etiqueta debe fijarse antes del cierre, no seguir moviéndose después |
| PDF de dos páginas | S5 | no (resuelto: `docs/entrega-corte1-moodle.pdf`, 2 páginas, en el propio repo) | Regenerar el PDF: la página 2 todavía cita la latencia vieja "8-15 ms" en vez de la medición reproducible corregida |
| ADR del reto con alternativas y consecuencias | S5 | no (resuelto: ADR-0003, nivel sobresaliente) | — |
| Línea base medida y reproducible | S5 | no (resuelto: `docs/medicion-corte1.md` con script y 3 corridas) | — |
| Pipeline con pruebas en verde | S5 | no (resuelto: runs verdes antes y después del cierre) | — |
| docs/aspectos.md con 8 columnas | S5 | no (resuelto) | — |
| Registro de IA del corte | S5 | no (resuelto: entradas del 05/09 con rechazos justificados) | — |
| Rotar token de Coveralls | S5 | sí | Rotar el token — no se ha confirmado |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público (clon sin auth) |
| Estructura mínima | Cumple (con desviación) | Las seis rutas están, pero `docs/arc42.md` suelto convive con `docs/arc42/` |
| Convención de nombres de ADR | Cumple | 0001, 0002, 0003 en kebab-case con la decisión en el título |
| ADR aceptados sin reescribir | Cumple | ADR-0001 marcado "Reemplazada" en vez de editado o borrado |
| `docs/ia.md` al día | Cumple | Entradas del 05/09 con aceptado/corregido/rechazado y motivo |
| Sin credenciales en el repositorio ni en el historial | **No cumple** | Token de Coveralls recuperable en el historial (`905f546`); no confirmado que se haya rotado |
| Contribución de todos los integrantes | Cumple, con reserva | 4 identidades para 4 integrantes, pero Fernando con 1 solo commit en todo el semestre |
| Pipeline en verde | Cumple | Runs `success` antes (`6ee5b66`, 06/09 01:27Z) y después (`f7c1a6c`, 07/09 15:00Z) del cierre |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits (HEAD) | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Camilo Andres Conde Corrales | `Cconde31` (incluye `Steamlinker`, consolidado) | 26 | — | — | Autor de casi todo el reto S5 |
| Fernando Isacc Conde Herrera | commit con nombre real, `fconde@utb.edu.co` | 1 | — | — | Contribución mínima persistente |
| Miguel Alejandro Iii Jacome Yanez | `MiguelJacome` | 7 | — | — | — |
| Veronica Ubarne Reyes | `vylrir` | 9 | — | — | Consolidada desde S3-S4 |

## Preguntas abiertas para la sustentación

- ¿Rotaron el token de Coveralls expuesto en el historial? Muestren evidencia.
- ¿Por qué se siguió moviendo la etiqueta `corte-1` después del cierre en vez de fijarla antes?
- ¿Cómo va a contribuir Fernando de forma sustantiva en los próximos cortes?
