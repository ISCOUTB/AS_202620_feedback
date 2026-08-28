# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Recobra |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Integrantes y su usuario de GitHub | Camilo Andres Conde Corrales · Fernando Isacc Conde Herrera · Miguel Alejandro Iii Jacome Yanez · Veronica Ubarne Reyes — cuentas observadas: `Cconde31`, `MiguelJacome`, `Steamlinker` (nueva, sin atribuir; correspondencias por confirmar con el docente) |
| URL del sistema desplegado | — |
| Ultima revision | 2026-08-28 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `da5c15d` · 2026-08-07T17:54:04-05:00 | 3/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `d2dac73` · 2026-08-16T23:44:54-05:00 | 4/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `cb5c579` · 2026-08-23T23:44:12-05:00 | 4/9 | no se publica | sí |
| 4 | S4 | `50d601c` (2026-08-25T09:14:56-05:00) | 2/10 | 1.8 | si |
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
| `docs/ia` vacío (y sin extensión .md) | S1 | parcial: `docs/ia.md` ya tiene entrada S3 con rechazado/motivo; queda el archivo `docs/ia` residual | Borrar el `docs/ia` vacío y completar el registro con todos los integrantes |
| `docs/aspectos.md` narrativo, sin tabla ni enlaces | S1 | sí (sin cambios en S3) | Tabla de 8 columnas y enlaces a escenarios y ADR |
| Sin diagrama C4 (solo descripción textual) | S1 | no (resuelto: `docs/c4/README.md` con Mermaid); queda `docs/C4.md` viejo duplicado | Borrar el C4 textual antiguo |
| Fernando Isacc Conde Herrera y Veronica Ubarne Reyes sin aparición en el historial | S1 | sí (3 identidades para 4 integrantes en S3; apareció `Steamlinker`, sin atribuir) | Confirmar acceso, contribución y a quién corresponde `Steamlinker` |
| ADR fuera de convención (`docs/ADR/01-…`, sin motivo de descarte) | S3 | parcial: renombrado a `docs/adr/0001-…` con motivos de descarte; pero el ADR viejo se **borró sin marcarlo reemplazado** y la decisión cambió (híbrido → hexagonal puro) | Si la decisión cambia: nuevo ADR y el anterior marcado «reemplazado», nunca borrado (CONTRATO §4) |
| Matriz comparativa genérica, no contra el árbol de utilidad | S3 | parcial: nueva matriz ponderada en §4.2; sigue sin filas por escenario S1–S7 y `matriz_arquitectura.md` vieja contradice el ADR | Filas por escenario: qué mejora/empeora cada estilo; borrar o alinear la matriz vieja |
| Sin esqueleto ejecutable (código, prueba, comando de arranque) | S3 | parcial: ya hay código, prueba y comando; faltan los paquetes `domain/` y `application/` declarados y evidencia del verde | Crear archivos en `domain/ports`, `application/use-cases` y el adaptador de persistencia; subir run del verde |
| `node_modules/` completo versionado | S3 (cierre) | sí | Añadir `.gitignore` y sacarlo del historial; higiene de repo |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público (clon sin auth) |
| Estructura mínima | Cumple | Las seis rutas en `cb5c579`; residuos: `docs/ia` vacío y `docs/C4.md` duplicado |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico.md` |
| ADR aceptados sin reescribir | No cumple | `01-arquitectura-base.md` borrado en `cb5c579` sin marcarlo reemplazado (decisión cambió) |
| `docs/ia.md` al día | Cumple | Entrada del 23-ago con rechazado/motivo; una sola fila y dos integrantes |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep sin coincidencias; `.env.example` solo con puerto |
| Contribución de todos los integrantes | No cumple | 3 identidades (Cconde31, MiguelJacome, Steamlinker) para 4 integrantes |
| Pipeline en verde | No verificado | Sin `.github/workflows/`; prueba sin evidencia de ejecución |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Camilo Andres Conde Corrales | ¿`Cconde31`? (confirmar) | 12 | — | — | ADR nuevo y esqueleto en S3 |
| Fernando Isacc Conde Herrera | sin cuenta observada (¿`Steamlinker`? — sin confirmar, correo `camilandre0510`) | 0 (¿o 1 vía `Steamlinker`?) | — | — | Atribución por confirmar |
| Miguel Alejandro Iii Jacome Yanez | ¿`MiguelJacome`? (confirmar) | 4 | — | — | Sección 4 en S3 |
| Veronica Ubarne Reyes | sin cuenta observada | 0 | — | — | Sin aparición en el historial hasta S3 |

## Preguntas abiertas para la sustentación

- ¿A quién corresponde la cuenta `Steamlinker` (`camilandre0510`) y quién de los cuatro integrantes sigue sin aparecer en el historial?
- ¿Por qué se borró el ADR anterior en lugar de marcarlo «reemplazado», si la decisión cambió?
- ¿Cuándo crearán los paquetes `domain/` y `application/` que declaran el ADR y el README, y sacarán `node_modules/` del repo?
