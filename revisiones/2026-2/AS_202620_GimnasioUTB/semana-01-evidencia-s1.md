# Evidencia S1 · GimnasioUTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `a45615e9df3263b9cfb9637e8f28c3598da2732d` · 2026-08-08T21:41:21-05:00 (commit vigente al cierre S1) |
| Cierre S1 | 2026-08-10T05:00:00Z |
| Comandos principales | `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only a45615e9`; `git show a45615e9:<ruta>`; `git shortlog -sne`; `git log -S'<patrón>'` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:9` (`AS_202620_GimnasioUTB OK 1b30b7a4…`) y clon anónimo exitoso | Cumple | URL `ISCOUTB/AS_202620_GimnasioUTB`, visible sin autenticación |
| Integrantes del equipo con acceso | `git shortlog -sne a45615e9`: solo `PedroPambi` (5) | No verificado | La comprobación de colaboradores exige la API de GitHub, sin cuota (403). Por historial S1: 1 de 3 cuentas. `RodrigoFacioLince` aparece recién el 2026-08-16 y no hay ninguna cuenta atribuible a Sebastián Caicedo en todo el historial. Haría falta consultar los colaboradores del repositorio |
| Equipo de 3 o 4 personas | `EQUIPOS.md:22` — Sebastian Felipe Caicedo Acosta · Rodrigo Andres Facio Lince Beltran · Pedro Luis Pallares De La Hoz | Cumple | 3 integrantes. Ojo: la propia documentación del equipo (OC5, S2) dice «Equipo de 4 personas» |
| Ficha del problema con usuarios y alcance | `docs/problema.md` — Problema real y acotado, Stakeholders y beneficiarios (estudiantes, encargado, Bienestar), Alcance inicial | Cumple | Usuarios y alcance declarados |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | Revisión de `docs/problema.md` | No cumple | La ficha no declara tensiones de calidad enfrentadas. La tensión «consistencia de datos vs. facilidad de operación» aparece en `docs/aspectos.md`, no en la ficha del problema |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` (S1) | No cumple | Está en prosa («Aspecto declarado: Consistencia de datos»); no hay tabla de 8 columnas ni fila con ID y Aspecto |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` — Propósito, Uso realizado, Validación, Registro futuro | Cumple | Contenido real, aunque genérico: no nombra la herramienta concreta ni registra lo rechazado con motivo (anotado en la matriz transversal) |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `git ls-tree a45615e9`: no existe `docs/arc42/` | No verificado | Anotado como observación de montaje: git no versiona directorios vacíos y no hay `.gitkeep` ni contenido, así que no se puede comprobar la plantilla. Haría falta subirla (o un `.gitkeep`) |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree a45615e9`: no existen `docs/adr/` ni `docs/c4/` | No verificado | Ídem: sin contenido versionado ni `.gitkeep`; en S2 el C4 aparece en `docs/C4.jpg`, fuera de `docs/c4/` |

## Matriz transversal (CONTRATO)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:9` + clon sin autenticación | Cumple | |
| Estructura mínima presente | `ls-tree a45615e9`: solo README.md, `docs/aspectos.md`, `docs/ia.md` (más `docs/problema.md`) | No cumple | Faltan `docs/arc42/`, `docs/adr/` y `docs/c4/`. En S1 puede deberse a directorios vacíos sin `.gitkeep` (observación de montaje) |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` → `a45615e9` 2026-08-08T21:41:21-05:00 | Cumple | Sin etiqueta; commit vigente al cierre |
| Nombres de ADR según la convención | No existe `docs/adr/` | Cumple | Vacuo: sin ADR, nada viola la convención. El directorio no existe — hallazgo de estructura |
| ADR aceptados no reescritos | Sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md`: único commit `a45615e` (2026-08-08, dentro del periodo) | No cumple | El archivo creció en el periodo, pero el contenido no registra entradas por uso (herramienta, aceptado, rechazado y motivo) como pide el contrato |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env`; `git log -S` sin coincidencias para 10 patrones de credenciales (incluye blobs subidos y borrados) | Cumple | Limpio |
| Contribución de todos los integrantes | `shortlog -sne a45615e9`: 1 cuenta (`PedroPambi`) de 3 integrantes | No cumple | Sebastián Caicedo no aparece en ningún momento del historial; Rodrigo Facio Lince aparece desde el 2026-08-16 |

## Recuento de criterios

4 de 9 criterios cumplidos.

## No verificado / pendientes

- Acceso de los tres integrantes: sin API no se pudo consultar la lista de colaboradores; el historial solo muestra a una cuenta en S1.
- Plantilla arc42 y directorios `adr/`/`c4/`: no versionados (posibles directorios vacíos sin `.gitkeep`); haría falta subirlos.

## Hallazgos para la planilla

- Sebastián Caicedo Acosta sin ninguna cuenta atribuible en el historial (0 commits en S1 y S2).
- `docs/aspectos.md` en prosa, sin la tabla de 8 columnas.
- Ficha del problema sin tensiones de calidad (la tensión está en `aspectos.md`).
- Sin `docs/arc42/`, `docs/adr/`, `docs/c4/`.
- El propio documento del equipo dice «Equipo de 4 personas» (son 3 según EQUIPOS.md).
