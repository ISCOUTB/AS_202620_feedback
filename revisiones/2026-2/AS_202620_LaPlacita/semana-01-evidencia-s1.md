# Evidencia S1 · LaPlacita

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `37f1deb8c8bfc3e6396baa85da4f9fd0cf147e32` · 2026-08-08T15:37:16-05:00 (commit vigente al cierre S1) |
| Cierre S1 | 2026-08-10T05:00:00Z |
| Comandos principales | `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-10T05:00:00Z'`; `git ls-tree -r --name-only 37f1deb8`; `git show 37f1deb8:<ruta>`; `git shortlog -sne` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `revisiones/2026-2/_meta/lsremote.txt:11` (`AS_202620_LaPlacita OK fa7e13bc…`) y clon anónimo exitoso | Cumple | URL `ISCOUTB/AS_202620_LaPlacita`, visible sin autenticación |
| Integrantes del equipo con acceso | `git shortlog -sne 37f1deb8`: las 4 cuentas del equipo empujan antes del cierre (Jorge M. Castillo 48, samulssl 15, Isaza927 6, matbuendia 3) | Cumple | Verificado por historial de contribuidores (la lista de colaboradores no se pudo consultar por límite de API). Correspondencia evidente por los correos de los commits |
| Equipo de 3 o 4 personas | `EQUIPOS.md:24` — Mateo Josue Buendia Barrios · Miguel Angel Isaza Montalvo · Samuel David Jimenez Alvarez · Jorge Alberto Martinez Castillo | Cumple | 4 integrantes |
| Ficha del problema con usuarios y alcance | `docs/ficha_del_problema.md` — §1.2 A quién afecta, §2 Propuesta de solución | Cumple | Usuarios (comunidad universitaria, establecimientos) y alcance declarados |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | Revisión de `docs/ficha_del_problema.md` | No cumple | La ficha no declara dos tensiones de calidad enfrentadas; tiene criterios de éxito con métricas, que no es lo mismo |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md` — tabla de 8 columnas con filas A-01 a A-06 (ID, Aspecto y Requisito rellenos) | Cumple | Más de lo pedido: 6 filas con ID y Aspecto |
| `docs/ia.md` iniciado con contenido real | `docs/ia.md` — bitácora con fecha, herramienta, propósito, prompt, resultado y validación (Gemini y ChatGPT) | Cumple | Contenido real. Falta registrar lo rechazado con motivo (anotado en la matriz transversal) |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `docs/arc42/arc42-template-EN.md` — plantilla v9.0-EN sin rellenar (esperado en S1) | Cumple | Presente en Markdown |
| `docs/adr/` y `docs/c4/` creados | `docs/adr/.gitkeep` y `docs/c4/.gitkeep` versionados | Cumple | Directorios versionados con `.gitkeep`, como recomienda la ficha |

## Matriz transversal (CONTRATO)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:11` + clon sin autenticación | Cumple | |
| Estructura mínima presente | `ls-tree 37f1deb8`: README.md, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` | Cumple | Las seis rutas desde S1 |
| Estado calificado identificable | `git log -1 --until='2026-08-10T05:00:00Z'` → `37f1deb8` 2026-08-08T15:37:16-05:00 | Cumple | Sin etiqueta; commit vigente al cierre |
| Nombres de ADR según la convención | `docs/adr/` contiene solo `.gitkeep` | Cumple | Vacuo: sin ADR. El `.gitkeep` es el mecanismo recomendado por la ficha para versionar el directorio; el filtro literal del contrato lo marcaría, conviene limpiarlo cuando llegue el primer ADR |
| ADR aceptados no reescritos | Sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md`: commits 05–08 de agosto (antes del cierre) | No cumple | Crece en el periodo, pero las entradas no registran qué se rechazó y por qué (columna que pide el contrato) |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias | Cumple | Limpio |
| Contribución de todos los integrantes | `shortlog -sne 37f1deb8`: 4 cuentas — Jorge M. Castillo (48), samulssl (15), Isaza927 (6), matbuendia (2+1 con dos correos) | Cumple | Los 4 integrantes contribuyen desde S1. Identidades consolidadas: matbuendia firma con dos correos (buendiamateo670 y mateo.buendia.barrios), misma persona |

## Recuento de criterios

8 de 9 criterios cumplidos.

## No verificado / pendientes

- Lista de colaboradores no consultable por límite de API; el acceso se verificó por el historial (los 4 contribuyen antes del cierre).

## Hallazgos para la planilla

- Ficha del problema sin dos tensiones de calidad (solo criterios de éxito).
- `ia.md` sin columna de lo rechazado.
- Estructura completa desde S1 (`.gitkeep` en `adr/` y `c4/`) — sin hallazgos de montaje.
