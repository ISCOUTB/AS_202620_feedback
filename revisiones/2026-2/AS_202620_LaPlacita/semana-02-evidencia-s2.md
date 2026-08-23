# Evidencia S2 · LaPlacita

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `fa7e13bc09e7660661984de2ebaf91662c332a49` · 2026-08-15T18:13:29-05:00 (commit vigente al cierre S2; es también HEAD) |
| Cierre S2 | 2026-08-17T05:00:00Z |
| Comandos principales | `git log -1 --until='2026-08-17T05:00:00Z'`; `git ls-tree -r --name-only fa7e13bc`; `git show fa7e13bc:<ruta>`; `git grep -nIE '<plantilla>' fa7e13bc -- docs/arc42`; `git show a484f1a:docs/aspectos.md` (contraste de historial) |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/arc42-template-EN.md` §1 — objetivo central (1.1), tabla de objetivos de calidad con motivo (1.2.1), criterios de éxito (1.2.2), stakeholders (1.4) | Cumple | Objetivo de negocio explícito («reducir el tiempo de espera en horas pico») e interesados por rol. El mapeo objetivo→interesado es indirecto (tablas separadas) |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/arc42-template-EN.md` §2 — tabla con columna Tipo (Funcional/negocio, Normativa/seguridad, Organizacional, Técnica/producto) y Justificación por fila | Cumple | Clasificación presente con las tres categorías del curso (la legal aparece como «Normativa/seguridad») y justificación en cada fila. Las dos filas tipadas «Funcional/negocio» pesan en la fila siguiente |
| Restricciones separadas de los requisitos | §2 del arc42 — «Plataforma multi-establecimiento» y «Validación de entrega con PIN de 4 dígitos» tipadas «Funcional / negocio» | No cumple | Dos de las seis restricciones están marcadas como funcionales: en realidad son requisitos funcionales del sistema, no restricciones que acoten el diseño |
| arc42 sección 3 con actores y sistemas externos | §3.1 contexto de negocio (usuario, establecimiento, pasarela de pago) y §3.2 contexto técnico | Cumple | Coherente con el C4 de §3.3: mismos actores y sistemas externos (pasarela de pago, notificaciones push) |
| Entre 3 y 5 escenarios de calidad redactados | §10.2 — ESC-01 a ESC-05 | Cumple | 5 escenarios numerados, dentro del rango |
| Cada escenario con sus seis partes y medida numérica | ESC-01 (estímulo, fuente, entorno, respuesta esperada, medida de respuesta, prioridad) — revisión de los 5 | No cumple | Los 5 escenarios tienen 5 de las 6 partes: falta el «artefacto» en todos. Las medidas son numéricas (99 %, <1 %, 0 registros, 2 minutos), pero la condición de carga no está cuantificada («cantidad elevada de usuarios») |
| Árbol de utilidad que prioriza por impacto y riesgo | §10.1 — mermaid del árbol con prioridades Alta/Media por atributo, y línea «Prioridad: X importancia / Y dificultad arquitectónica» en cada escenario | Cumple | Priorización visible (importancia ≈ impacto, dificultad ≈ riesgo). Observación: el par (impacto, riesgo) no aparece dentro del diagrama sino en los escenarios; A-03 figura sin escenario («no incluido en esta entrega») |
| C4 de contexto con leyenda y flechas etiquetadas | §3.3 del arc42 — mermaid con aristas etiquetadas («Ordena, consulta estado…», «Envía solicitud de pago…») | No cumple | Flechas etiquetadas sí, pero sin leyenda (los colores de `style` no se explican). Guardado dentro de `docs/arc42/arc42-template-EN.md` en vez de `docs/c4/` (que sigue vacío salvo `.gitkeep`) — desviación de estructura |
| Escenarios alcanzables desde la fila de su aspecto | `docs/aspectos.md` en el hash calificado: tabla con C4/ADR/Código/Pruebas/Evidencia en «Pendiente», sin enlaces a escenarios | No cumple | El commit `a484f1a` (15-ago) sí añadió a `aspectos.md` una sección «Árbol de Utilidad y Escenarios de Calidad», pero el commit `b1f8da2` (15-ago, posterior) la retiró: en el estado calificado no hay enlaces desde los aspectos a ESC-01…ESC-05 |

## Matriz transversal (CONTRATO)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `lsremote.txt:11` + clon sin autenticación | Cumple | |
| Estructura mínima presente | `ls-tree fa7e13bc`: README.md, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` | Cumple | Las seis rutas; `c4/` sigue sin contenido (solo `.gitkeep`, el C4 vive en el arc42) |
| Estado calificado identificable | `git log -1 --until='2026-08-17T05:00:00Z'` → `fa7e13bc` 2026-08-15T18:13:29-05:00 | Cumple | Sin etiqueta; commit vigente al cierre |
| Nombres de ADR según la convención | `docs/adr/` contiene solo `.gitkeep` | Cumple | Vacuo: sin ADR. Limpiar el `.gitkeep` cuando llegue el primer ADR numerado |
| ADR aceptados no reescritos | Sin ADR | Cumple | Vacuo |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md`: `e5cb8f1`, `082eebc`, `b1f8da2` (15-ago, dentro del periodo); tres entradas nuevas del 15-ago | No cumple | Crece en el periodo, pero ninguna entrada registra qué se rechazó y por qué (la columna «Validación» solo dice «revisado y adaptado») |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE '<regex>' HEAD` sin coincidencias; sin `.env`; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias | Cumple | Limpio |
| Contribución de todos los integrantes | `shortlog -sne fa7e13bc`: Jorge M. Castillo (50), samulssl (15), Isaza927 (12), matbuendia (2+1) | Cumple | Los 4 integrantes. matbuendia consolidado (dos correos, misma persona) |

## Recuento de criterios

5 de 9 criterios cumplidos.

## No verificado / pendientes

Nada pendiente de verificación técnica; los estados se resolvieron con evidencia del repositorio.

## Hallazgos para la planilla

- Sin entregas tardías: HEAD (2026-08-15T18:13) está dentro del cierre S2.
- C4 de contexto sin leyenda y guardado en el arc42 (§3.3), no en `docs/c4/`.
- Escenarios sin la parte «artefacto» (5 de 6 partes).
- En el estado calificado, `aspectos.md` no enlaza los escenarios (la sección de enlaces existió en `a484f1a` y se retiró en `b1f8da2`).
- Dos restricciones tipadas «Funcional / negocio» son requisitos funcionales.
- `ia.md` sin columna de lo rechazado.
- Para el corte 1: los 5 escenarios tienen medida numérica; ninguno declara método de medición con herramienta y umbral más allá de las cifras.
