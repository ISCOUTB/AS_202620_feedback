# Evidencia S1 · Tienda virtual UTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `d414ecff589f1f1f6db99c5b86f66e34d42bcc34` · `2026-08-09T14:08:31-05:00` («Tambien se incluye el nombre del cuarto integrante…») |
| Cierre de la actividad | `2026-08-10T05:00:00Z` (domingo 9 de agosto, medianoche Colombia) |
| Visibilidad | pública, comprobada con `git ls-remote` sin autenticación (revisiones/2026-2/_meta/lsremote.txt, línea de `AS_202620_TIENDA-VIRTUAL-UTB`) y con `git clone` sin autenticación |

Comandos principales ejecutados: `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only d414ecf`; `git show d414ecf:docs/…`; `git shortlog -sne HEAD`; `git grep -nIE '<secreto>'`; `git tag --list`.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `git clone` sin autenticación OK; `lsremote.txt` línea `AS_202620_TIENDA-VIRTUAL-UTB OK` | Cumple | Nombre sigue `AS_202620_<PROYECTO>`. |
| Integrantes del equipo con acceso | `git shortlog -sne HEAD` en el cierre: solo `Jasen Yukopila` y `RAZOR7150` | No verificado | Sin API de GitHub (403, sin token) no se puede listar colaboradores. Qué haría falta: la lista de colaboradores del repo o confirmación del docente. El historial S1 muestra 2 de 4 cuentas, lo que la ficha no penaliza si los demás tienen acceso (no comprobable por protocolo git). |
| Equipo de 3 o 4 personas | `EQUIPOS.md` declara 4 integrantes | Cumple | Shalom Jhoanna Arrieta Marrugo · Levis Adrian Ortiz Cano · Alejandro Patron Montero · Jasen Mihovil Yukopila Escobar. |
| Ficha del problema con usuarios y alcance | `docs/problema.md` (secciones «Usuarios» y «Alcance inicial») | Cumple | Tres tipos de usuario y alcance con inclusiones y exclusiones explícitas. |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `docs/problema.md`, sección «Tensiones de calidad»: facilidad de uso vs. seguridad; precisión de inventario vs. disponibilidad/rendimiento | Cumple | Cada tensión enfrenta dos atributos con su argumento. |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md:6-8`: tabla de 2 columnas («Aspecto de calidad | Descripción inicial»), sin columna ID | No cumple | La ficha pide la tabla de ocho columnas del curso con al menos una fila con ID y aspecto; aquí la tabla tiene 2 columnas, sin ID. El aspecto «Seguridad» sí está declarado. |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md`: entrada del 2026-08-09 (ChatGPT/Codex, propósito, resultado y validación humana) | Cumple | Contenido real, no un encabezado vacío. |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `docs/arc42/arc42-template-EN.md` con los 12 encabezados de sección | Cumple | 12 secciones presentes y sin rellenar, como se espera esta semana. |
| `docs/adr/` y `docs/c4/` creados | `docs/adr/.gitkeep` y `docs/c4/.gitkeep` | Cumple | Directorios versionados con `.gitkeep`. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clone y ls-remote sin autenticación | Cumple | — |
| Estructura mínima presente | `git ls-tree -r d414ecf`: `README.md`, `docs/arc42/`, `docs/adr/.gitkeep`, `docs/c4/.gitkeep`, `docs/aspectos.md`, `docs/ia.md` | Cumple | Las seis rutas presentes. |
| Estado calificado identificable | sin etiquetas (`git tag --list` vacío); hash `d414ecff…` + `%cI 2026-08-09T14:08:31-05:00` | Cumple | Las evidencias semanales se califican en el commit vigente al cierre, identificado y citado. |
| Nombres de ADR según la convención | `docs/adr/` sin ADR todavía | Cumple | Nada que viole la convención. |
| ADR aceptados no reescritos | sin ADR en el periodo | Cumple | Nada que reescribir. |
| `docs/ia.md` al día para la semana | commits sobre el archivo el 2026-08-09 (`87da711`, `4a1bcec`, `8355076`) | No cumple | El registro no incluye qué se rechazó y por qué (CONTRATO §6): solo fecha, herramienta, propósito, resultado y validación humana. |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin salida | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: 2 identidades (Jasen, RAZOR7150) de 4 integrantes | No verificado | La comprobación de acceso exige la lista de colaboradores (API, no disponible). La ficha S1 no penaliza que solo haya empujado una persona si el resto tiene acceso; ese acceso no se pudo comprobar. |

## Recuento de criterios

7 de 9 criterios de la ficha cumplidos (1 No cumple, 1 No verificado).

## No verificado / pendientes

- Acceso de los 4 integrantes al repositorio: sin API no se puede listar colaboradores. Hace falta la lista de colaboradores o la confirmación del docente.
- La correspondencia cuenta↔estudiante se deja para el docente; los correos de los commits (`correo omitido`, `correo omitido`, `correo omitido`, `correo omitido`) hacen evidente la atribución, pero no se da por cerrada aquí.

## Hallazgos para la planilla

- `docs/aspectos.md` con tabla de 2 columnas sin ID, en lugar de la tabla de 8 columnas del curso (S1, se arrastra).
- `docs/ia.md` sin registro de «qué se rechazó y por qué» (S1, se arrastra).
- Integrantes sin aparición en el historial al cierre S1: Shalom Jhoanna Arrieta Marrugo y Alejandro Patron Montero (normal en semana 1 si tienen acceso, pendiente de confirmar).
- Sin entregas tardías relativas a S1: el siguiente commit tras el cierre es `0f9ff92` (2026-08-15, «Evidencia S2»).
