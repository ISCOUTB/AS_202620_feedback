# Evidencia S1 · EnAgenda

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `13f61b10596b3c8bab614f622dca8b647eeeea09` · 2026-08-09T05:34:14-05:00 (commit vigente al cierre S1) |
| Cierre S1 | 2026-08-10T05:00:00Z |
| Comandos principales | `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only <HASH>`; `git show <HASH>:<ruta>`; `git shortlog -sne` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:8` (`AS_202620_EnAgenda OK 6ff7f9ad…`) y clon anónimo por HTTPS exitoso | Cumple | URL con prefijo `ISCOUTB/` y nombre `AS_202620_EnAgenda`; visible sin autenticación |
| Integrantes del equipo con acceso | `git shortlog -sne 13f61b10`: `Daoisttl0FB3` (23) y `Jein-12` (1) | No verificado | La comprobación de colaboradores exige la API de GitHub, sin cuota (403). Por historial: 2 de 3 cuentas aparecen antes del cierre; `eliabarnedocondef10-gif` firma su primer commit recién el 2026-08-16 (`7af2ee0`). Haría falta consultar los colaboradores del repositorio para confirmar el acceso del tercero |
| Equipo de 3 o 4 personas | `EQUIPOS.md:21` — Eliab Josue Arnedo Conde · Jeimy Yulieth Mendez Altamiranda · Gabriela Morales Cancino | Cumple | 3 integrantes |
| Ficha del problema con usuarios y alcance | `docs/ficha-problema .md:3-29` (Problema, Propuesta, Alcance inicial) | Cumple | Declara usuarios (propietario del evento, invitado) y alcance del MVP. Ojo: nombre de archivo con espacio antes de la extensión |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `docs/ficha-problema .md:31-38` (Tensiones preliminares) | Cumple | Tres tensiones: privacidad vs. facilidad de acceso, funcionalidad vs. alcance, consistencia vs. rapidez |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos .md:3-5` — tabla de 8 columnas, fila A-01 con ID y Aspecto (y Requisito) rellenos | Cumple | El resto de columnas en «Pendiente», permitido esta semana |
| `docs/ia.md` iniciado con contenido real | `docs/ia .md:13,17-18` — dos usos de Perplexity con qué se aceptó y qué se rechazó y por qué | Cumple | Cumple también la regla del contrato de registrar lo rechazado con motivo |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `ls-tree` S1: `docs/arc42/01-…` a `12-…`, 12 archivos `.md` | Cumple | El 01 tiene texto de plantilla («Esta sección se completará…»), que es lo esperado esta semana. Nombres con espacio antes de la extensión (desviación anotada en la matriz transversal) |
| `docs/adr/` y `docs/c4/` creados | `ls-tree` S1: `docs/adr/0001-app-movil-y-web-de-invitaciones .md`, `docs/c4/nivel-1-contexto .md` y niveles 2 y 3 | Cumple | Directorios con contenido, no vacíos |

## Matriz transversal (CONTRATO)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:8` + clon sin autenticación | Cumple | |
| Estructura mínima presente | `ls-tree 13f61b10`: README.md, docs/arc42/, docs/adr/, docs/c4/, `docs/aspectos .md`, `docs/ia .md` | Cumple | Desviación de estructura (no ausencia): `aspectos .md`, `ia .md`, `ficha-problema .md` y varios arc42 llevan espacio antes de `.md`; el filtro exacto del contrato no los alcanza |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` → `13f61b10` 2026-08-09T05:34:14-05:00 | Cumple | Sin etiqueta; para evidencia semanal se califica el commit del cierre (sin tag esperado) |
| Nombres de ADR según la convención | `docs/adr/0001-app-movil-y-web-de-invitaciones .md` | No cumple | Espacio antes de la extensión: el filtro `^[0-9]{4}-…\.md$` no lo acepta |
| ADR aceptados no reescritos | `git log --follow -- docs/adr/0001-… .md` → único commit `e1219bf` 2026-08-08 (creación) | Cumple | Sin reescrituras posteriores |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia .md`: `ae676f6` 2026-08-09 (creación, antes del cierre) | Cumple | Contenido con entradas del 07 y 08 de agosto, con rechazos y motivos |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex del contrato>' HEAD` y sobre `13f61b10` sin coincidencias; `ls-files` sin `.env`; `log -S'BEGIN PRIVATE KEY'` sin coincidencias | Cumple | Resultado limpio en los tres comandos |
| Contribución de todos los integrantes | `shortlog -sne 13f61b10`: 2 cuentas de 3 integrantes | No cumple | No aparece ningún commit atribuible a Eliab Arnedo antes del cierre S1 (su primer commit es `7af2ee0`, 2026-08-16). Normal para la semana 1 según la ficha, pero el criterio transversal no se satisface; se vigila en la planilla |

## Recuento de criterios

8 de 9 criterios cumplidos.

## No verificado / pendientes

- Acceso de los tres integrantes: sin API no se pudo consultar la lista de colaboradores. Por historial se ven 2 de 3 cuentas en S1; el tercero aparece el 16 de agosto.

## Hallazgos para la planilla

- Estructura con nombres de archivo desviados (espacio antes de `.md` en `aspectos`, `ia`, `ficha-problema`, `adr/0001-…` y varios arc42).
- Eliab Josue Arnedo Conde sin commits en S1 (primero el 2026-08-16).
- ADR `0001-app-movil-y-web-de-invitaciones .md` no pasa el filtro de convención.
