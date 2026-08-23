# Evidencia S2 · CampusMarket

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Estado revisado | `4f72799a8f92ac5f25687ef7afa9b7c783bc47db` · `2026-08-16T22:01:41-05:00` (último commit ≤ cierre 2026-08-17T05:00:00Z) |
| Comandos principales | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only <hash>`; `git show <hash>:docs/*`; `git show --stat 708a785 5b6f572`; `git grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template'`; `git grep -nI -E '<regex secretos>'`; `git log -- docs/ia.md` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/ARC42.md` §1.2–1.3 | No cumple | §1.2 «Objetivos funcionales» es una lista de funcionalidades (registrar usuarios, crear publicaciones…), no objetivos de negocio, y no hay tabla de interesados ni «a quién le importa cada uno» |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/restricciones.md` (Tipo, Origen y Justificación por restricción; sección «Restricciones legales») | Cumple | Clasificación organizativa/técnica y justificación clara. Incoherencia: `docs/ARC42.md` R-02 dice «dos integrantes» y `docs/restricciones.md` R-02 dice «tres» (el equipo real son 3). R-06 sin Tipo/Origen |
| Restricciones separadas de los requisitos | `docs/restricciones.md` (el propio resumen declara que las restricciones se distinguen de los requisitos funcionales) | Cumple | No mezcla requisitos funcionales; R-05 es una restricción de alcance, aceptable como tal |
| arc42 sección 3 con actores y sistemas externos | `docs/ARC42.md` §3.1–3.3 (Estudiante, Administrador; acceso por navegador con HTTPS) | Cumple | Coherente con el C4 de `docs/c4.md`: mismos actores, sin sistemas externos |
| Entre 3 y 5 escenarios de calidad redactados | `docs/escenarios de calidad.md` (EC-01 a EC-04) | Cumple | 4 escenarios numerados |
| Cada escenario con sus seis partes y medida numérica | `docs/escenarios de calidad.md` (Fuente/Estímulo/Artefacto/Entorno/Respuesta/Medida verificable en los 4) | Cumple | Medidas con cifra y unidad: 9 de 10 búsquedas ≤2 s (catálogo de 1.000 publicaciones); 10 de 10 rechazos; máx. 2 módulos; ≤10 min |
| Árbol de utilidad que prioriza por impacto y riesgo | `docs/arbolU.md` (Impacto, Riesgo técnico y Prioridad por escenario + tabla resumen) | Cumple | Priorización explícita por impacto y riesgo, y los escenarios priorizados son los 4 redactados |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/c4.md` (PlantUML con bloque `legend` y `Rel` etiquetadas, p. ej. «Consulta productos… [HTTPS]») | Cumple | Como código, con leyenda explícita y flechas etiquetadas. Está en `docs/c4.md` (archivo suelto), no en `docs/c4/` (desviación de estructura) |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` (sin cambios desde S1: texto narrativo de Mantenibilidad, sin tabla ni enlaces) | No cumple | No hay filas que enlacen a los escenarios; el archivo quedó igual que en S1 |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `revisiones/2026-2/_meta/lsremote.txt:12`; clon sin autenticación | Cumple | Sin cambios respecto a S1 |
| Estructura mínima presente | árbol de `4f72799` | No cumple | Sin `docs/arc42/` (hay `docs/ARC42.md` suelto), sin `docs/adr/`, sin `docs/c4/` (hay `docs/c4.md`); archivos con espacios («escenarios de calidad.md») |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` | Cumple | `4f72799a8f92ac5f25687ef7afa9b7c783bc47db` · `2026-08-16T22:01:41-05:00` |
| Nombres de ADR según la convención | sin `docs/adr/` → filtro vacío | Cumple | Vacuo: sin ADR. El archivo `docs/adr` creado el 11-08 terminó renombrado a «escenarios de calidad.md» (`623f6e5`) |
| ADR aceptados no reescritos | sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md` → `2026-08-16 56e8b1f`; tablas de S1 y S2 | No cumple | Registro de usos completo y dentro del periodo, pero sin entradas de lo rechazado y su motivo (CONTRATO §6) |
| Sin credenciales en el repositorio ni en el historial | `git grep -nI -E '<regex>' 4f72799` (sin salida); sin `.env`; `git log -S'BEGIN PRIVATE KEY'` (vacío) | Cumple | Sin coincidencias |
| Contribución de todos los integrantes | `git shortlog -sne HEAD` → 23 commits, una sola identidad (`camilixo92`) | No cumple | 1 de 3 integrantes con commits en todo el historial |

## Recuento de criterios

7 de 9 criterios de la ficha cumplidos.

## No verificado / pendientes

- Nada quedó sin verificar: todo lo evaluable estaba en texto (Markdown/PlantUML) dentro del repositorio.

## Hallazgos para la planilla

- Entregas tardías: ninguna posterior al cierre S2 (el último commit es el calificado).
- Contribución: todo el historial (23 commits) firmado por una sola cuenta; Nilver Garcia Pimentel y Joshua Jose Tenorio Alvarez sin aparición.
- Estructura: documentación en archivos sueltos (`docs/ARC42.md`, `docs/c4.md`, `docs/arbolU.md`, `docs/restricciones.md`, `docs/escenarios de calidad.md`) en lugar de `docs/arc42/`, `docs/c4/`, `docs/adr/`.
- Incoherencia interna: tamaño del equipo «dos» (ARC42.md) vs «tres» (restricciones.md y README).
- `docs/aspectos.md` sin actualizar desde S1 (sin tabla ni enlaces a escenarios).
- `docs/ia.md` sin columna de lo rechazado.
- Para el corte 1: los 4 escenarios tienen medida comprobable; EC-01 y EC-02 declaran además condición de carga/prueba (catálogo de 1.000 publicaciones; 10 intentos), pero ninguno declara herramienta con la que se medirá.
