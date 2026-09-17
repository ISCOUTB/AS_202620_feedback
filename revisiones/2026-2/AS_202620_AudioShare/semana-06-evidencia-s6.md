# semana-06-evidencia-s6 · AudioShare

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `4a0eba9` en `origin/master` (2026-09-13T22:01:57-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/contextos-delimitados.md (HEAD 4a0eba9, 2026-09-13): sección 'Mapa de contextos' con Session→Sync→Audio. | No cumple | Las flechas no declaran el tipo de relación con el vocabulario de la semana (núcleo compartido, cliente-proveedor, capa anticorrupción). |
| Tabla módulo a datos con dueño único por entidad | docs/modulos_datos.md: una fila por módulo con columna 'Dueño único' (Session, Sync, Audio, Persistencia, app.ts). | Cumple | Cada conjunto de datos tiene un solo dueño declarado; el contraste con las escrituras reales del código no se aporta. |
| La tabla cubre las entidades que existen en el código | docs/modulos_datos.md incluye 'rooms' y 'participants', coherentes con src/modules/session/infrastructure/persistence/sqlite-room-repository.ts y con docs/arc42/src/05_building_block_view.adoc. | Cumple | Verificación documental: no hay migraciones ni .sql, el esquema vive dentro del repositorio SQLite. |
| No conformidades de propiedad de datos detectadas sobre el código actual | docs/no_conformidades.md (parcial en la evidencia): NC-01 y NC-02 tratan audio simulado y reproducción física. | No cumple | No hay NC de propiedad ni recorrido citado (hash, grep de escrituras); no se reporta que Session persista start_at/estado de reproducción de Sync. |
| Plan de corrección por no conformidad | docs/no_conformidades.md: columna 'Plan de corrección' con acción e impacto por NC (p. ej. NC-01 'Implementar captura de audio real...'). | Cumple | Cada no conformidad visible tiene prioridad y acción concreta. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/src/ no contiene 08_concepts.adoc, aunque docs/arc42/arc42-template.adoc lo incluye con 'include::src/08_concepts.adoc[]'. | No cumple | Lenguaje ubicuo y mapa existen en docs/lenguaje-ubicuo.md y docs/contextos-delimitados.md, pero fuera de la sección 8. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/ solo tiene Nivel 1 y Nivel 2; docs/adr/0001-usar-monolito-modular.md declara 'El C4 Nivel 3 (Componentes) queda pendiente'. | No cumple | El .mmd de Nivel 2 dice reemplazar una versión anterior sin ADR del reajuste; no se aportó el hash de S5 para el diff. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md: la fila A-01 referencia session, audio y sync en la columna de implementación y enlaza ADR, C4 Nivel 2 y pruebas. | Cumple | Ningún aspecto queda sin contexto; solo existe A-01 y sus pruebas cubren EC-01/EC-04, con EC-02 y EC-03 declarados pendientes. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio público 'AS_202620_AudioShare' en la organización ISCOUTB (visible: true); historial con cuatro cuentas: Elian Daniel Perea Vanegas, Yeiver Andrés Vergel Pérez, Santiago Adolfo Camacho Hernández y cardonavincent26-design. | Cumple | La cuenta cardonavincent26-design no se atribuye a ningún integrante declarado por su nombre visible. |
| Estructura mínima | Árbol en 4a0eba9: docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | arc42 se entrega en .adoc en lugar de Markdown y el include de 08_concepts.adoc apunta a un archivo ausente. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md sigue el patrón NNNN-kebab-case e incluye contexto, alternativas, decisión, consecuencias y trazabilidad. | Cumple | El H1 ('Selección del estilo arquitectónico') enuncia el tema; no se aporta el historial por ADR para verificar que no se editó tras aceptarse. |
| Tabla de aspectos | docs/aspectos.md con matriz navegable: aspecto, escenario, métrica, requisito, decisión, ADR, C4, implementación y pruebas. | Cumple | Sin columna explícita de evidencia de calidad; EC-02 y EC-03 declaran la medición pendiente. |
| Registro de uso de IA | docs/ia.md con usos, herramientas y tabla que incluye 'Propuesta de IA rechazada y motivo'; crece hasta el commit 4a0eba9. | Cumple | Todas las filas visibles registran un rechazo con motivo técnico. |
| README | README.md: propósito del sistema, requisito Node.js 22+, arranque con 'npm run dev' y pruebas con 'npm test' y 'npm run verify'. | Cumple | El diagrama del corte A-01 aún nombra data/rooms.json aunque la persistencia documentada es SQLite. |
| Pipeline y análisis estático | Existe .github/workflows/ci.yml, pero la evidencia entregada no incluye runs_ci ni URL pública de SonarCloud con Quality Gate. | No verificado | Falta comprobar con 'curl -s https://api.github.com/repos/ISCOUTB/AS_202620_AudioShare/actions/runs?per_page=5'; no hay sonar-project.properties en el árbol. |
| Secretos | Evidencia sobre HEAD 4a0eba9: 'secretos: (sin coincidencias)' y 'envs_versionados: []'. | Cumple | Solo se versiona .env.example, sin credenciales. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `4a0eba994357cba432178075dd872e0b52643595 2026-09-13T22:01:57-05:00 Revise documentation for week 6 updates`
- **Veredicto**: con pendientes
- Resumen: En HEAD 4a0eba9 (2026-09-13, origin/master) los artefactos de S6 existen, pero quedan sin resolver la tipificación del mapa de contextos, la auditoría de propiedad sobre el código, la sección 8 de arc42 y el C4 nivel 3 con su ADR; además no hay evidencia pública del pipeline ni de SonarCloud.

Pendientes que siguen abiertos:
- C4 nivel 3 y ADR del reajuste de límites
- docs/arc42/src/08_concepts.adoc (y secciones 07 y 11 ausentes)
- Auditoría de propiedad de datos con recorrido citado
- Tipificación de relaciones del mapa de contextos
- Evidencia pública de SonarCloud (configuración, run y Quality Gate)
- Pruebas de EC-02 y EC-03

## Recuento y nota sugerida

4 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.0 = 1 + 4 × (4/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Pipeline y SonarCloud: no hay runs_ci ni URL de Quality Gate; hace falta 'curl -s https://api.github.com/repos/ISCOUTB/AS_202620_AudioShare/actions/runs?per_page=5' y la URL pública del análisis.
- Contenido de .github/workflows/ci.yml no incluido: no se pudo confirmar que invoque el scanner de Sonar; se requiere la línea exacta del workflow.
- Auditoría de escrituras en src/: no se aportó la salida del grep de INSERT/UPDATE/.save() para contrastar la tabla módulo a datos.
- Historial de docs/adr/: no se aportan los commits por ADR para verificar que un ADR aceptado no se editó ni borró.
- diff_desde_cierre y runs_ci no vienen en la evidencia: no se pudo comprobar el reajuste de límites contra el hash revisado en S5.

## Hallazgos para la planilla

- El mapa de contextos muestra direcciones pero no tipifica las relaciones entre contextos.
- La lista de no conformidades no contiene conflictos de propiedad de datos ni el recorrido que los descartó.
- startAt figura como dato de Sync, pero se persiste en las tablas de Session vía RoomRepository sin reportarse como no conformidad.
- No existe la sección 8 de arc42 y su include queda roto en la plantilla.
- Solo hay C4 Nivel 1 y 2; el Nivel 3 sigue declarado pendiente en el ADR-0001.
- No se aporta evidencia pública de SonarCloud ni run de CI para el hash revisado.
- El README describe data/rooms.json en el flujo A-01 mientras la persistencia real es SQLite.
- Hay cuatro cuentas en el historial; una no puede atribuirse a un integrante declarado por su nombre visible.
