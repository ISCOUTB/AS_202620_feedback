# Evidencia S1 · InvenTrack

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `069202095d44555aedbba96eecc76da1986cd216` · 2026-08-09T16:03:46-05:00 (commit vigente al cierre S1) |
| Cierre S1 | 2026-08-10T05:00:00Z |
| Comandos principales | `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only 06920209`; `git show 06920209:<ruta>`; `git shortlog -sne` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:10` (`AS_202620_InvenTrack OK 6203d46a…`) y clon anónimo exitoso | Cumple | URL `ISCOUTB/AS_202620_InvenTrack`, visible sin autenticación |
| Integrantes del equipo con acceso | `git shortlog -sne 06920209`: solo `Esteban Peluffo` (8) | No verificado | La comprobación de colaboradores exige la API de GitHub, sin cuota (403). Por historial S1: 1 cuenta de 4. Las otras dos cuentas observadas (`Josephva24`, `FlexT21`) empiezan a empujar después del cierre, y no hay ninguna cuenta atribuible a Javier Carta. Haría falta consultar los colaboradores del repositorio |
| Equipo de 3 o 4 personas | `EQUIPOS.md:23` — Javier Alejandro Carta Lacharme · Esteban Javier Peluffo Marquez · Felix Andres Taborda Jimenez · Jose Gabriel Vargas Perez | Cumple | 4 integrantes |
| Ficha del problema con usuarios y alcance | `docs/ficha_problema.md` — §3 Alcance (MVP), §5 Usuarios objetivo | Cumple | Usuarios (dueños y empleados de PYMEs) y alcance declarados |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `git show 06920209:docs/ficha_problema.md` — sin sección de tensiones | No cumple | La ficha declara un único aspecto (consistencia de datos) pero no dos tensiones de calidad enfrentadas |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` (S1) | No cumple | Está en prosa («Aspecto declarado: Consistencia de datos»); no hay tabla de 8 columnas ni fila con ID y Aspecto |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` (S1) — tabla con fecha, etapa, uso y nivel de intervención; herramienta Claude | Cumple | Contenido real con herramienta nombrada. Falta registrar lo rechazado con motivo (anotado en la matriz transversal) |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `git ls-tree 06920209`: no existe `docs/arc42/` | No verificado | Observación de montaje: git no versiona directorios vacíos y no hay `.gitkeep` ni contenido, así que no se puede comprobar la plantilla. Haría falta subirla |
| `docs/adr/` y `docs/c4/` creados | `git ls-tree 06920209`: no existen `docs/adr/` ni `docs/c4/` | No verificado | Ídem: sin contenido versionado ni `.gitkeep` |

## Matriz transversal (CONTRATO)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:10` + clon sin autenticación | Cumple | |
| Estructura mínima presente | `ls-tree 06920209`: solo README.md, `docs/aspectos.md`, `docs/ia.md`, `docs/ficha_problema.md` | No cumple | Faltan `docs/arc42/`, `docs/adr/` y `docs/c4/`. En S1 puede deberse a directorios vacíos sin `.gitkeep` (observación de montaje) |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` → `06920209` 2026-08-09T16:03:46-05:00 | Cumple | Sin etiqueta; commit vigente al cierre |
| Nombres de ADR según la convención | No existe `docs/adr/` | Cumple | Vacuo: sin ADR. El directorio no existe — hallazgo de estructura |
| ADR aceptados no reescritos | Sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md`: `35f6f31` (2026-08-09, dentro del periodo) | No cumple | El archivo creció en el periodo, pero la entrada no registra qué se rechazó y por qué (columna que pide el contrato) |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias | Cumple | Limpio |
| Contribución de todos los integrantes | `shortlog -sne 06920209`: 1 cuenta (`Esteban Peluffo`) de 4 integrantes | No cumple | En S1 solo empuja una persona; Javier Carta no aparece en ningún momento del historial completo |

## Recuento de criterios

4 de 9 criterios cumplidos.

## No verificado / pendientes

- Acceso de los cuatro integrantes: sin API no se pudo consultar la lista de colaboradores; el historial solo muestra a una cuenta en S1.
- Plantilla arc42 y directorios `adr/`/`c4/`: no versionados (posibles directorios vacíos sin `.gitkeep`); haría falta subirlos.

## Hallazgos para la planilla

- Javier Alejandro Carta Lacharme sin ninguna cuenta atribuible en el historial (0 commits).
- `docs/aspectos.md` en prosa, sin la tabla de 8 columnas.
- Ficha del problema sin dos tensiones de calidad.
- Sin `docs/arc42/`, `docs/adr/`, `docs/c4/` en S1.
- Solo un integrante empujó commits en S1 (normal según la ficha si el resto tiene acceso, pendiente de confirmar).
