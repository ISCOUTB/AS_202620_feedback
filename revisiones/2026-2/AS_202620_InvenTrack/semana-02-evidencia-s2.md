# Evidencia S2 · InvenTrack

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `db90ff2f20c6f53bed0a5f49393529447865e296` · 2026-08-16T21:22:20-05:00 (commit vigente al cierre S2) |
| Cierre S2 | 2026-08-17T05:00:00Z |
| Comandos principales | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only db90ff2f`; `git show db90ff2f:<ruta>`; `git grep -nIE '<plantilla>' db90ff2f -- docs/arc42`; `git grep -nIE '<secretos>' HEAD` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/arc42-template-EN.md` — Quality Goals (atributo, pregunta guía, respuesta, prioridad), Stakeholders con rol, perspectiva y expectativas; trade-off explícito | Cumple | Objetivos con prioridad y la pregunta guía de clase; interesados por rol. El objetivo de negocio queda en Requirements Overview |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/arc42-template-EN.md` — tabla C1–C7 con columna Tipo (Legal / Organizativa / Técnica) y «Quién la impone / justificación» | Cumple | Las tres categorías presentes (C1 legal, C2–C4 organizativas, C5–C7 técnicas), cada una con origen y justificación |
| Restricciones separadas de los requisitos | `docs/arc42/arc42-template-EN.md` — párrafo «Una restricción es distinta de un requisito» con ejemplo del propio proyecto | Cumple | Explican la distinción y la aplican: los requisitos viven en la sección 1 y las restricciones en la 2 |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42/arc42-template-EN.md` — Business Context (tabla de actores y sistemas externos) y Technical Context | Cumple | Mismos actores que el C4 (Dueño, Empleado) y un sistema externo (notificaciones por correo); coherente |
| Entre 3 y 5 escenarios de calidad redactados | `docs/arc42/arc42-template-EN.md` — ESC-01 a ESC-05 | Cumple | 5 escenarios numerados, dentro del rango |
| Cada escenario con sus seis partes y medida numérica | `docs/arc42/arc42-template-EN.md` — ESC-01 (fuente, estímulo, artefacto, entorno, respuesta, medida: 0 casos en 100 % de prueba con 50 transacciones simultáneas); ESC-02 a ESC-05 con lo mismo | Cumple | Las seis partes en los 5, con cifra, unidad y condición. ESC-04 declara método completo (p95 ≤ 400 ms, 20 usuarios concurrentes, población, ventana); ESC-03 (≥ 99 % mensual, ≤ 5 min) |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/utility-tree.md` — mermaid del árbol con prioridades (A, A)/(A, M)/(M, M)/(M, B) y tabla con la justificación de cada prioridad | Cumple | Priorización por (impacto de negocio, riesgo técnico) explícita y justificada; las hojas coinciden con los escenarios redactados |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4/context.md` — código mermaid con «**Leyenda:**» explícita y aristas etiquetadas («Usa (HTTPS)», «Envía alerta de stock bajo (SMTP / API)») | Cumple | Como código, en `docs/c4/context.md`, con leyenda de colores y flechas etiquetadas |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` — sección «Escenarios de calidad (Semana 2)» con enlaces a `arc42/arc42-template-EN.md` y `utility-tree.md` para ESC-01 y ESC-02 | Cumple | Los dos escenarios del aspecto declarado son alcanzables desde `aspectos.md`. Observación: está en prosa, no en la tabla de 8 columnas del contrato (solo hay un aspecto declarado) |

## Matriz transversal (CONTRATO)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:10` + clon sin autenticación | Cumple | |
| Estructura mínima presente | `ls-tree db90ff2f`: README.md, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` | Cumple | Estructura completa desde S2 (faltaba en S1) |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` → `db90ff2f` 2026-08-16T21:22:20-05:00 | Cumple | Sin etiqueta; commit vigente al cierre |
| Nombres de ADR según la convención | `docs/adr/` contiene solo `README.md` | Cumple | Vacuo: sin ADR, nada viola la convención. Observación: el placeholder `README.md` (como el `.gitkeep` de otros equipos) haría fallar el filtro literal del contrato; conviene sacarlo o renombrarlo cuando llegue el primer ADR numerado |
| ADR aceptados no reescritos | Sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md`: `771e732` y `59019a8` (2026-08-16, dentro del periodo); entrada del 16-ago con correcciones a la IA y motivos | Cumple | El registro describe qué se corrigió/rechazó y por qué (dos correcciones de contenido), aunque no en columna propia. Hay además dos commits sobre el archivo el 22-ago, posteriores al cierre (anotados) |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias | Cumple | Limpio |
| Contribución de todos los integrantes | `shortlog -sne db90ff2f`: Josephva24 (41), Esteban Peluffo (8), FlexT21 (6) | No cumple | 3 cuentas de 4 integrantes. No aparece ninguna cuenta atribuible a Javier Carta Lacharme en todo el historial |

## Recuento de criterios

9 de 9 criterios cumplidos.

## No verificado / pendientes

Nada pendiente de verificación técnica; todos los criterios se resolvieron con evidencia del repositorio.

## Hallazgos para la planilla

- Commits posteriores al cierre S2 (corresponden a la semana 3, no afectan esta calificación): `0b6d6ab` «Entrega semanal», `d84523e`, `6203d46` (2026-08-22).
- Javier Carta Lacharme sigue sin aparecer en el historial.
- `docs/adr/README.md` hace fallar el filtro de nombres de ADR (placeholder, cosmético).
- `aspectos.md` en prosa (sin la tabla de 8 columnas del contrato), aunque con enlaces funcionales a los escenarios.
- Para el corte 1: los 5 escenarios tienen medida comprobable; ESC-01, ESC-03 y ESC-04 declaran cómo se medirán (carga, umbral, método).
