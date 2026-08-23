# Evidencia S2 · EnAgenda

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `5b6f7a8eb7c1f4a48d85cb6390bfe2df23255f9f` · 2026-08-16T23:33:20-05:00 (commit vigente al cierre S2) |
| Cierre S2 | 2026-08-17T05:00:00Z |
| Comandos principales | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only 5b6f7a8`; `git show 5b6f7a8:docs/arc42/…`; `git grep -nIE '<plantilla>' 5b6f7a8 -- docs/arc42`; `git grep -nIE '<secretos>' HEAD` y `5b6f7a8` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/01-introducción-y-objetivos .md:23-45` — stakeholders con rol y necesidad (1.2), objetivos del sistema (1.3), objetivos de calidad con prioridad (1.4) | Cumple | Los objetivos no son funcionalidades. El mapeo explícito objetivo→interesado es implícito (tabla de stakeholders + objetivos); se puede hacer más directo |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/02- restricciones .md:3-58` — R-01 a R-06, cada una con «Impacto arquitectónico» | No cumple | Hay justificación del impacto, pero no clasificación en técnicas/organizativas/legales ni declaración del origen de cada restricción (salvo R-01 y R-04, que insinúan su fuente) |
| Restricciones separadas de los requisitos | `docs/arc42/02- restricciones .md:21-33` (R-03) y `:52-58` (R-06) frente al alcance de `docs/arc42/03-contexto y alcance .md:15-27` | No cumple | R-03 (invitaciones sin cuenta, estados y vencimiento) y R-06 (roles y permisos) están redactadas como requisitos funcionales, no como restricciones |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42/03-contexto y alcance .md:3-31` — organizador e invitado; declara que no hay sistemas externos obligatorios | Cumple | Coherente con el C4: mismos actores (Organizador, Invitado), solo el sistema EnAgenda |
| Entre 3 y 5 escenarios de calidad redactados | `docs/arc42/10-requisitos-de-calidad .md:32-86` — EC-01 a EC-05 | Cumple | 5 escenarios numerados |
| Cada escenario con sus seis partes y medida numérica | `docs/arc42/10-requisitos-de-calidad .md:34-43` (EC-01 completo: fuente, estímulo, artefacto, entorno, respuesta, medida «100 % de los intentos…») | Cumple | Las seis partes en los 5 escenarios, con cifra y unidad. Observación: solo EC-05 declara condición de carga (10 usuarios concurrentes, p95 < 2 s); EC-01 a EC-04 condicionan al conjunto de pruebas, no a una carga |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arc42/10-requisitos-de-calidad .md:3-30` — árbol con atributos y prioridades [Alta]/[Media] | Cumple | No es lista plana y la priorización es visible. Falta un eje explícito de riesgo; los escenarios redactados corresponden a hojas del árbol |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/nivel-1-contexto .md:3-23` — código mermaid (Person/System/Rel), flechas con etiquetas | No cumple | Está como código (bien) en `docs/c4/`, con flechas etiquetadas; pero no tiene leyenda |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos .md:5` — única fila A-01 con C4, ADR, Código, Pruebas y Evidencia en «Pendiente» | No cumple | Ningún escenario se enlaza desde `aspectos.md`; ni siquiera se menciona el escenario del aspecto |

## Matriz transversal (CONTRATO)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:8` + clon sin autenticación | Cumple | |
| Estructura mínima presente | `ls-tree 5b6f7a8`: README.md, docs/arc42/ (12), docs/adr/, docs/c4/, `docs/aspectos .md`, `docs/ia .md` | Cumple | Sigue la desviación de S1: espacio antes de `.md` en varios nombres |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` → `5b6f7a8` 2026-08-16T23:33:20-05:00 | Cumple | Sin etiqueta; commit vigente al cierre |
| Nombres de ADR según la convención | `docs/adr/0001-app-movil-y-web-de-invitaciones .md` | No cumple | Espacio antes de la extensión; no pasa el filtro del contrato |
| ADR aceptados no reescritos | `git log --follow -- docs/adr/0001-… .md` → único commit `e1219bf` 2026-08-08 | Cumple | Sin reescrituras |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia .md`: `89e4494`, `c0a23d5`, `24e1a13` (2026-08-15, dentro del periodo); entrada del 15-ago sobre Mermaid en `docs/ia .md:22` | Cumple | Contenido con rechazos y motivos. Además hay un commit `6ff7f9a` (2026-08-17T13:43:49-05:00) posterior al cierre — entrega tardía anotada |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` y sobre `5b6f7a8` sin coincidencias; `ls-files` sin `.env`; `log -S'BEGIN PRIVATE KEY'` sin coincidencias | Cumple | Limpio en los tres comandos |
| Contribución de todos los integrantes | `shortlog -sne 5b6f7a8`: Daoisttl0FB3 (32), Jein-12 (5), eliabarnedocondef10-gif (2) | Cumple | Tres cuentas, tres integrantes. Correspondencia por el correo de los commits, evidente: gabimoralesc30 ↔ Gabriela Morales, jeimy4637 ↔ Jeimy Méndez, eliabarnedocondef10 ↔ Eliab Arnedo |

## Recuento de criterios

5 de 9 criterios cumplidos.

## No verificado / pendientes

Nada pendiente de verificación técnica; los estados se resolvieron con evidencia del repositorio.

## Hallazgos para la planilla

- Entrega tardía: `6ff7f9a` 2026-08-17T13:43:49-05:00 «Update ia .md» (posterior al cierre S2).
- Sin leyenda en el C4 de contexto (código mermaid en `docs/c4/nivel-1-contexto .md`).
- `aspectos.md` con una sola fila y sin enlaces a escenarios.
- Restricciones sin clasificación técnica/organizativa/legal; R-03 y R-06 son requisitos funcionales.
- Persisten los nombres de archivo con espacio antes de la extensión (estructura y ADR).
- Para el corte 1: los 5 escenarios tienen medida numérica; solo EC-05 declara cómo se medirá (p95, < 2 s, 10 usuarios concurrentes).
