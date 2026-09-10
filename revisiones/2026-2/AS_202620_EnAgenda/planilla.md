# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo EnAgenda. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | EnAgenda |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Integrantes y su usuario de GitHub | Eliab Josue Arnedo Conde · Jeimy Yulieth Mendez Altamiranda · Gabriela Morales Cancino — cuentas abajo |
| URL del sistema desplegado | sin desplegar aún |
| Ultima revision | 2026-09-10 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 5 | CORTE1 | `942e112` (2026-09-06T23:56:39-05:00) | 7/12 | no aplica | si |
| 4 | S4 | `df724b8` (2026-08-30T23:57:42-05:00) | 8/10 | 4.2 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `13f61b10` · 2026-08-09T05:34:14-05:00 | 8/9 | 4,6 * | sí |
| 2 | S2 | `5b6f7a8` (2026-08-16T23:33:20-05:00) | 5/9 | no aplica | si |
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
| Commit 1d01401 (2026-08-31T00:28:12-05:00) actualiza docs/ia.md después del cierre. | S4 | no (resuelto tarde) | — |
| Ajustar C4 nivel 2 para reflejar el monolito Flask y el repositorio en memoria. | S4 | si | |
| Agregar SonarCloud al pipeline. | S4 | si | |
| Hacer navegable la celda C4 de docs/aspectos.md. | S4 | si | |
| Verificar redacción de arc42 01, 04, 05 y 06. | S4 | si | |
| Etiqueta `corte-1` ausente | S5 | No (creada 2026-09-06, `31773ad`) | Se resolvió; vigilar que en cortes futuros se etiquete con más antelación al cierre. |
| Respuesta al reto sin diagnóstico, ADR, cambio ni medición reproducible | S5 | Sí | El equipo dedicó el cierre a corregir feedback de S4 (C4, aspectos) y así lo documenta en `docs/correcciones.md`; sigue faltando diagnóstico, ADR, cambio y medición del reto de Corte 1. |
| Cadena de `docs/aspectos.md` no navegable y evidencia pendiente | S5 | Parcial (mejoró, celda Evidencia rota) | La fila A-01 ya enlaza C4/ADR/código/pruebas, pero "Evidencia" apunta a `correcciones-feedback.md`, archivo inexistente (el real es `docs/correcciones.md`); corregir el enlace y crear la fila del reto de Corte 1. |
| C4 de contenedores desactualizado frente al monolito Flask y el repositorio en memoria | S4 | Sí | Alinear el diagrama con el estado ejecutable. |
| Registro de IA sin entrada del Corte 1 | S5 | Sí | `docs/ia.md` sigue sin entradas posteriores al 30/08/2026; registrar el uso de IA (si lo hubo) en las correcciones del cierre y en el reto de Corte 1. |
| 13fdc8e Cambios C4 | S2 | no (resuelto tarde) | — |
| 66fb6e4 Cambios C4 | S2 | no (resuelto tarde) | — |
| 1d01401 Update documentation with recent project changes | S2 | no (resuelto tarde) | — |
| 696882e Update aspectos.md | S2 | no (resuelto tarde) | — |
| Falta docs/arc42/01* | S2 | si | |
| Trazabilidad de aspectos pendiente | S2 | si | |
| Sin integración continua | S2 | si | |
| docs/aspectos.md actualizado en commits 03c855c y 696882e (post-cierre) para corregir trazabilidad | S5 | no (resuelto tarde) | — |
| docs/evidencia.md agregado en commit 5a8a5c5 (post-cierre) como evidencia de corte vertical | S5 | no (resuelto tarde) | — |
| correcciones.md en la raíz | S5 | si | |
| Completar arc42 secciones 07, 08 y 11 | S5 | si | |
| Completar C4 nivel 3 | S5 | si | |
| Corregir enlace roto en aspectos.md | S5 | si | |
| Configurar SonarCloud | S5 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_EnAgenda`, público, verificable sin autenticación |
| Estructura mínima | No cumple | Las seis rutas del contrato están presentes en HEAD. |
| Convención de nombres de ADR | Cumple | `0001-usar-monolito-modular.md`. |
| ADR aceptados sin reescribir | Cumple | Aceptado en `c38adfb`; después solo fue renombrado. |
| `docs/ia.md` al día | No cumple | La entrada más reciente corresponde a Semana 4; falta Corte 1. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin credenciales; coincidencias con `token` son identificadores de dominio y datos de prueba. |
| Contribución de todos los integrantes | Cumple | Tres identidades consolidadas para tres integrantes en HEAD. |
| Pipeline en verde | No cumple | Run de HEAD `33360647498` en verde; no demuestra todavía el reto. |

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
