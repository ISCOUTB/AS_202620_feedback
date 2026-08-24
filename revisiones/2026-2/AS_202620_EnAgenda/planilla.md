# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo EnAgenda. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | EnAgenda |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Integrantes y su usuario de GitHub | Eliab Josue Arnedo Conde · Jeimy Yulieth Mendez Altamiranda · Gabriela Morales Cancino — cuentas abajo |
| URL del sistema desplegado | sin desplegar aún |
| Última revisión | 2026-08-24 (revisión S3, actualizada tras el cierre) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `13f61b10` · 2026-08-09T05:34:14-05:00 | 8/9 | 4,6 * | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `5b6f7a8e` · 2026-08-16T23:33:20-05:00 | 5/9 | 3,2 * | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `c38adfb94` · 2026-08-23T23:49:01-05:00 | 3/9 | no se publica | sí (actualizada tras el cierre) |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Nombres de archivo con espacio antes de la extensión (`docs/aspectos .md`, `docs/ia .md`, `docs/ficha-problema .md`, ADR, arc42, matriz) | S1 | Sí (el ADR además ya no corresponde a su nombre: el archivo dice «monolito modular» y se llama «app-movil-y-web…») | Renombrar a la convención; el ADR no pasa el filtro de nombres |
| Integrante Eliab Josue Arnedo Conde sin commits en S1 (primer commit 2026-08-16) | S1 | Cerrado en S2 (2 commits); reabierto en S3 (0 commits en el periodo) | Se resolvió solo; vigilar que la contribución siga repartida |
| `aspectos.md` sin enlaces a escenarios (C4/ADR/Código/Pruebas/Evidencia en «Pendiente») | S2 | Parcialmente cerrado: ya tiene la tabla de 8 columnas y enlaza escenarios; sigue «Pendiente» la columna ADR | Enlazar el ADR 0001 desde su fila y desde los escenarios EC que lo motivan |
| C4 de contexto sin leyenda | S2 | Sí | Añadir leyenda al mermaid |
| Evidencia S3 sin estrategia ni esqueleto: §4 en placeholder, sin matriz de estilos, sin código, pruebas ni workflow; ADR 0001 es de producto, no la decisión de estilo | S3 | Cerrado en documentación (§4 completa, ADR de estilo aceptado, matriz propia); sigue abierto el esqueleto | El esqueleto prometido (`src/` con 6 módulos + pruebas) no existe: solo `docs/Esqueleto.py` demo y `docs/main.py` con import roto; README sin comando de arranque |
| Esqueleto ejecutable inexistente: sin comando de arranque en README, sin prueba, paquetes del monolito modular ausentes | S3 | Sí | Crear `src/` con los módulos del ADR, prueba en verde y comando único en README |
| Matriz comparativa sin filas de los escenarios EC-01…EC-05 | S3 | Sí | Fila por escenario contra el árbol de utilidad |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_EnAgenda`, público, verificable sin autenticación |
| Estructura mínima | Cumple | Con desviación de nombres (espacios antes de `.md`) |
| Convención de nombres de ADR | No cumple | `0001-app-movil-y-web-de-invitaciones .md`: espacio y nombre que ya no corresponde al contenido (decide monolito modular) |
| ADR aceptados sin reescribir | Cumple | El anterior estaba «propuesto»; reemplazado en `c38adfb` por la decisión de estilo ya «Aceptada» |
| `docs/ia.md` al día | Cumple | Entradas del 07, 08, 15 y 17 de agosto con rechazos y motivos |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` de secretos sin coincidencias; sin `.env` versionado |
| Contribución de todos los integrantes | No cumple en S3 | 2 de 3 en el periodo: Daoisttl0FB3 (4), Jein-12 (5); Eliab 0 |
| Pipeline en verde | No cumple | Sin `.github/workflows/` y sin ninguna prueba en el árbol |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Eliab Josue Arnedo Conde | eliabarnedocondef10-gif (correo omitido) | 0 (S3) | 0 | — | Último commit `45ab58e` (2026-08-16, S2); sin commits en S3 |
| Jeimy Yulieth Mendez Altamiranda | Jein-12 (correo omitido) | 5 (S3) | 0 | — | C4 nivel 2, ia.md y archivos por upload |
| Gabriela Morales Cancino | Daoisttl0FB3 (correo omitido) | 4 (S3) | 0 | — | §4, matriz comparativa y ADR de estilo |

Correspondencia cuenta↔persona inferida del correo de los commits, no de parecidos de nombre; la confirma el docente.

## Preguntas abiertas para la sustentación

- ¿El tercer integrante (Eliab) tenía acceso al repositorio desde la semana 1? (la lista de colaboradores no se pudo consultar por límite de API).
- ¿Cómo justificaría el equipo la priorización del árbol de utilidad en términos de riesgo?
- ¿Por qué el ADR decide «monolito modular» pero el archivo conserva el nombre de la decisión de producto, y por qué sus enlaces internos apuntan a archivos que no existen?
- ¿Cuándo montarán el esqueleto prometido (`src/` con los 6 módulos, prueba y comando de arranque) para llegar al corte 1 con el montaje listo?
