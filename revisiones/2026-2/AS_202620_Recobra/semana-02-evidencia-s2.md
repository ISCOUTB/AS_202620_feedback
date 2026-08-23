# Evidencia S2 · Recobra

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `d2dac73a11e83654e3500b561ff896932e10b4bb` · `2026-08-16T23:44:54-05:00` (último commit ≤ cierre 2026-08-17T05:00:00Z) |
| Comandos principales | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only <hash>`; `git show <hash>:docs/*`; `git grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template'`; `git grep -nI -E '<regex secretos>'`; `git log -- docs/ia` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42.md` §1 («Lo que buscamos» + «Interesados principales») | Cumple | Objetivos de negocio (centralizar, notificar, trazabilidad, reducir fraude) e interesados declarados, sin mapeo uno a uno. La referencia a `ficha-problema.md` está rota: ese archivo no existe en el repo |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/Restricciones_justificadas.md` (técnicas, organizativas, legales y de privacidad; columna «Por qué» y escenario que la verifica) | Cumple | Cada restricción dice de dónde viene y cómo se comprueba |
| Restricciones separadas de los requisitos | `docs/Restricciones_justificadas.md` (distingue explícitamente funcionalidad de restricción) | Cumple | Sin requisitos funcionales mezclados |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42.md` §3 + `docs/C4.md` (2 personas, administrador, sistema Recobra, servicio de notificaciones) | Cumple | Coherentes entre sí: mismos actores y mismo sistema externo |
| Entre 3 y 5 escenarios de calidad redactados | `docs/escenarios_calidad.md` (S1 a S7, con S4a y S4b) | No cumple | Hay 7 escenarios principales (9 entradas con los sub-escenarios): por encima del rango de 3 a 5 que pide la ficha |
| Cada escenario con sus seis partes y medida numérica | `docs/escenarios_calidad.md` (Fuente/Estímulo/Artefacto/Entorno/Respuesta/Medida en todos) | No cumple | Los 7 tienen las seis partes, y S1, S3–S7 tienen cifra + unidad + condición de carga (95 % ≤400 ms p95 con 200 usuarios; 95 % ≤60 s; 99 % mensual; 100 %; RTO ≤5 min; ≤2 días; 5× usuarios). Pero S2 (seguridad en reclamación) no tiene medida numérica: «ninguna reclamación pasa… sin completar la verificación», sin cifra ni unidad |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arbol_utilidad.md` (árbol con Impacto/Riesgo por hoja + tabla de priorización + justificación) | Cumple | Priorización explícita por impacto y riesgo, y los escenarios del árbol son los redactados |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/C4.md` (solo texto: personas, sistema, sistema externo y lista de relaciones con `→`) | No cumple | No hay diagrama (ni código ni imagen): es una descripción textual. Sin leyenda ni flechas etiquetadas como tal |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` (sin cambios desde S1: solo texto narrativo sobre seguridad) | No cumple | Sin tabla ni enlaces a los escenarios; `docs/arc42.md` dice que los atributos están en `aspectos.md`, pero ese archivo solo cubre uno |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `revisiones/2026-2/_meta/lsremote.txt:15`; clon sin autenticación | Cumple | Sin cambios respecto a S1 |
| Estructura mínima presente | árbol de `d2dac73` | No cumple | Sin `docs/arc42/` (hay `docs/arc42.md` suelto), sin `docs/adr/`, sin `docs/c4/` (hay `docs/C4.md`); `docs/ia` sin extensión |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` | Cumple | `d2dac73a11e83654e3500b561ff896932e10b4bb` · `2026-08-16T23:44:54-05:00` |
| Nombres de ADR según la convención | sin `docs/adr/` → filtro vacío | Cumple | Vacuo: sin ADR hasta el 22-08 (posterior al cierre) |
| ADR aceptados no reescritos | sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `docs/ia` en `d2dac73` (sigue vacío, 1 byte; único commit `2026-08-07 da5c15d`) | No cumple | Sin registro de uso de IA pese a que toda la documentación S2 se escribió en una semana |
| Sin credenciales en el repositorio ni en el historial | `git grep -nI -E '<regex>' d2dac73` (sin salida); sin `.env`; `git log -S'BEGIN PRIVATE KEY'` (vacío) | Cumple | Sin coincidencias |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` → `Cconde31` 10, `MiguelJacome` 4 | No cumple | 2 identidades para 4 integrantes; Fernando Isacc Conde Herrera y Veronica Ubarne Reyes sin aparición |

## Recuento de criterios

4 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Nada quedó sin verificar: todo lo evaluable estaba en texto dentro del repositorio.

## Hallazgos para la planilla

- Entregas tardías: nada posterior al cierre S2 con contenido de S2 (los commits del 22-08 — `f5586b3` sección 4, `f45f002` ADR, `f31607e` matriz — son trabajo de S3).
- `docs/ia` vacío también en S2: la documentación de la semana no registra ningún uso de IA.
- Enlace roto: `docs/arc42.md` remite a `ficha-problema.md`, que no existe en el repositorio.
- C4 sin diagrama: `docs/C4.md` es solo texto descriptivo.
- `docs/aspectos.md` sin actualizar desde S1 (sin tabla ni enlaces).
- 7 escenarios (más 2 sub-escenarios) cuando la ficha pide entre 3 y 5.
- Contribución: 2 de 4 integrantes con commits.
- Para el corte 1: 6 de 7 escenarios tienen medida comprobable; S1 y S7 declaran condición de carga explícita. Ninguno declara todavía herramienta y umbral de la medición.
