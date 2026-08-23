# Evidencia S2 · Clubs UTB

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `69cfe68f2605d24c5de71e81346619955b05f3eb` · 2026-08-16T18:33:10-05:00 · «Enhance C4 Context Diagram with detailed elements» |
| Cierre | 2026-08-17T05:00:00Z (domingo 16 de agosto medianoche, UTC-5) |
| Comandos principales ejecutados | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only 69cfe68f`; `git show 69cfe68f:docs/...`; `git grep -nIE '<[a-z ]+>|TODO|lorem ipsum'`; `git grep` de secretos; `git shortlog -sne 69cfe68f` |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/01_introduccion_y_metas.md` | Cumple | Metas de calidad priorizadas con motivación (§1.2) y tabla de stakeholders con expectativas (§1.3): estudiante interesado, miembro, administrador, equipo, docente. |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/02_restricciones.md` | Cumple | Clasificadas: técnicas T1–T4, organizacionales O1–O3, de tiempo C1–C2 y convenciones CV1; cada una con justificación. Observación: no hay categoría legal — si no aplica, conviene declararlo. |
| Restricciones separadas de los requisitos | 02 frente a requisitos de calidad en `10_requisitos_de_calidad.md` | Cumple | Separación correcta; no se detectan requisitos funcionales presentados como restricciones. |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42/03_contexto_y_alcance.md` frente a `docs/C4/contexto.md` | Cumple | Actores: estudiante, miembro, administrador — los mismos del C4. Divergencia menor: la base de datos aparece como socio en §3 pero no en el diagrama, y el proveedor de autenticación del C4 no se menciona en §3. |
| Entre 3 y 5 escenarios de calidad redactados | `docs/arc42/10_requisitos_de_calidad.md` | No cumple | Son 6 (U1–U3 de uso y C1–C3 de cambio), por encima del máximo de 5. Todos numerados y con medida. |
| Cada escenario con sus seis partes y medida numérica | tabla de escenarios en `10_requisitos_de_calidad.md` (Fuente·Estímulo·Artefacto·Entorno·Respuesta·Medida) | Cumple | Los 6 tienen las seis columnas. Medidas numéricas con unidad y condición: U1 «latencia ≤800 ms en camino crítico», U2/U3 «100% de los endpoints», C1 «≤3 módulos», C2 «5x clubes/eventos», C3 «≤2 módulos». |
| Árbol de utilidad que prioriza por impacto y riesgo | «Árbol de Utilidades» en `10_requisitos_de_calidad.md` (diagramas Mermaid) | Cumple | Hojas con pares (Importancia, Dificultad) H/M/L: impacto y riesgo explícitos. Las hojas enlazan los escenarios redactados (U1–U3, C1–C3): coinciden. |
| C4 de contexto con leyenda y flechas etiquetadas | `docs/C4/contexto.md` (código Mermaid) | Cumple | Ruta desviada: `docs/C4/` en mayúscula (el contrato espera `docs/c4/`). Flechas etiquetadas («Busca y consulta clubes y eventos», etc.) y sistema externo (proveedor de autenticación). Sin bloque de leyenda dedicado, pero los tipos van rotulados en cada nodo (Persona / Sistema Central / Sistema Externo). |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` en `69cfe68f` | No cumple | `docs/aspectos.md` sigue siendo la descripción general (problema, tecnologías, autores): no tiene filas de aspecto ni enlaces a escenarios. Los enlaces «../aspectos.md» de las secciones 01 y 02 apuntan a un archivo que no contiene la tabla. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt` OK; clon sin autenticación OK | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | `git ls-tree -r --name-only 69cfe68f` | No cumple | 5 de 6 rutas literales: `README.md` ✓, `docs/arc42/` ✓, `docs/adr/` ✓ (con `.temp` como marcador), `docs/aspectos.md` ✓, `docs/ia.md` ✓. El C4 está en `docs/C4/` (mayúscula), no en `docs/c4/`: desviación de ruta registrada; el artefacto se evaluó donde está. |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` | Cumple | Hash `69cfe68f…` con `%cI` 2026-08-16T18:33:10-05:00; es además el HEAD actual (sin commits posteriores al cierre). |
| Nombres de ADR según la convención | `docs/adr/` solo contiene `.temp` | Cumple (vacuo) | Sin ADR todavía. |
| ADR aceptados no reescritos | sin ADR | Cumple (vacuo) | Ídem. |
| `docs/ia.md` al día para la semana | `git log --format='%cI %h' -- docs/ia.md` | No cumple | Único commit del archivo: `c92595e` (2026-08-09). Sin commits en el periodo S2, y el contenido no registra usos reales de la semana 2 ni «qué se rechazó y por qué» (CONTRATO §6). |
| Sin credenciales en el repositorio ni en el historial | `git grep` (regex §9), `.env`, `git log -S'BEGIN PRIVATE KEY'` | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | `git shortlog -sne 69cfe68f` | Cumple | 4 identidades: `Zavod Dev` (21), `Josh4OP` (5), `Luis-Salas-Reyes` (4), `deortahollman-star` (3). Atribuciones: Josh4OP→Josh Robinson Ortega Castellon (correo `correo omitido`), Luis-Salas-Reyes→Luis Daniel Salas Reyes, deortahollman-star→Hollman Jose De Orta Gonzalez, Zavod Dev→Diego Andres Ramos De Avila (por correo y eliminación; sin confirmación oficial). |

## Recuento de criterios

- Ficha: **7 de 9** criterios Cumple.

## No verificado / pendientes

- Confirmación oficial de la correspondencia cuenta↔persona (sobre todo `Zavod Dev`).
- La categoría «legal» de restricciones: no aparece; el equipo debería declarar si no aplica.

## Hallazgos para la planilla

- Sin entregas tardías: HEAD = `69cfe68f`, idéntico al hash del cierre S2.
- `docs/aspectos.md` nunca se convirtió en la tabla de 8 columnas: arrastre de S1 que rompe el enlace aspecto→escenario (criterio 9 de la ficha S2).
- 6 escenarios (fuera del rango 3–5 pedido), aunque todos con seis partes y medida.
- C4 en `docs/C4/` (desviación de ruta frente a `docs/c4/` del contrato).
- `docs/ia.md` sin actualizar en la semana 2.
- La sección 10 está titulada «4. REQUISITOS DE CALIDAD» (numeración interna errónea, menor).
- Para el primer corte: los 6 escenarios declaran medida comprobable; U1, U2, U3 y C1–C3 indican además cómo verificarla (camino crítico, revisión de código/capas): buen punto de partida para el criterio de diagnóstico.
