# semana-06-evidencia-s6 · TAIA

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `c0c3adb` en `origin/main` (2026-09-13T20:01:35-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/mapa_contextos_s6.md y docs/arc42/08-conceptos-transversales.md §8.2-8.3 (c0c3adb). | Cumple | Nombra Usuario, Academic, AI y Reminders y relaciones por contratos explícitos; descarta núcleo compartido y usa adaptadores como capa anticorrupción, aunque la relación cliente-proveedor no se etiqueta literalmente. |
| Tabla módulo a datos con dueño único por entidad | docs/propiedad_datos_s6.md y docs/arc42/08-conceptos-transversales.md §8.4 (c0c3adb). | Cumple | Tabla contexto propietario → datos con un solo responsable por entidad. |
| La tabla cubre las entidades que existen en el código | Árbol c0c3adb: domain/entities task.py, usuario.py, conversation.py, messages.py, reminder.py, notification.py, reminder_schedule.py frente a §8.4. | Cumple | Cubre tareas, usuario y token de vinculación, conversación/intención y recordatorios/notificaciones. |
| No conformidades de propiedad de datos detectadas sobre el código actual | docs/auditoria_violaciones_s6.md y docs/arc42/08-conceptos-transversales.md §8.6 (V-01 a V-04, c0c3adb). | Cumple | Reporta cuatro violaciones de dependencia entre contextos con ubicación y corrección; no son de doble escritura y §8.4 declara que ninguna entidad tiene dos dueños. |
| Plan de corrección por no conformidad | §8.6 tabla con 'Corrección aplicada' y estado 'Corregida'; puertos presentes en el árbol (identity.py, academic_task_lookup.py, academic_gateway.py). | Cumple | Cada caso tiene acción concreta y se declara aplicada, no solo planificada. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/08-conceptos-transversales.md §8.1 (tabla de términos), §8.2-8.3 con enlaces al mapa. | Cumple | Lenguaje ubicuo con contexto principal por término y enlace a mapa y propiedad de datos. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | Árbol c0c3adb: docs/adr/ solo contiene 0001-estilo-arquitectonico.md; no se aportó el hash revisado en S5 para correr git diff --stat <HASH_S5>..c0c3adb -- docs/c4 docs/arc42 docs/adr. | No cumple | §8.6 documenta reajuste de fronteras entre contextos sin ADR que lo explique; C4-C3.md existe pero no se acredita su actualización. |
| Aspectos relacionables con los contextos del mapa | docs/arc42/08-conceptos-transversales.md §8.8 y docs/aspectos.md (c0c3adb). | Cumple | A-01 a A-04 mapeados a contextos; el contenido completo de aspects.md no es visible en el extracto. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Organización ISCOUTB, repo AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant, visibilidad pública; historial con nombres visibles val, valeria-estefania, luis20072002, Luis Mendoza, dei0811 y mark (c0c3adb). | Cumple | Cuatro integrantes declarados y seis nombres visibles; no se consolidan cuentas por parecido de nombre. |
| Estructura mínima | Árbol c0c3adb: docs/arc42/01 a 12 más arc42.md, docs/adr/0001, docs/c4/C4-C1 a C3, docs/aspectos.md, docs/ia.md y README.md. | Cumple | correcciones.md y lista_problemas.md en la raíz son desviación de estructura, no ausencia de artefacto. |
| Qué estado del repositorio se califica | origin/main, commit c0c3adb del 2026-09-13T20:01:35-05:00, anterior al cierre 2026-09-14T05:00:00Z; posteriores 0a12f0c, 3c2ae72, 7b32b3f, 5a4e8dc, 2837b47. | Cumple | Los commits posteriores al cierre no se califican. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md cumple el patrón NNNN-kebab-case, enuncia la decisión e incluye contexto, opciones, decisión, consecuencias y trazabilidad. | Cumple | No se aporta el log de ediciones posteriores al aceptarse; solo hay un ADR y ninguno del reajuste de fronteras. |
| La tabla de aspectos | docs/aspectos.md en c0c3adb y mapeo de aspectos A-01 a A-04 en docs/arc42/08-conceptos-transversales.md §8.8. | Cumple | No se puede verificar en el extracto que las ocho columnas estén completas y navegables. |
| Registro de uso de IA | docs/ia.md con nueve entradas de 2026-08-07 a 2026-09-12 (log de ia.md, c0c3adb). | Cumple | El crecimiento está acreditado; la columna de lo rechazado y su motivo no es verificable en el extracto. |
| README | README.md: qué es, integrantes, requisitos (Python), arranque con .\run.bat y pruebas con pytest backend/tests. | Cumple | docs/arc42/02 anota que el README está codificado en UTF-16 LE, lo que dificulta su revisión. |
| Pipeline y análisis estático | Solo consta .github/workflows/ci.yml en el árbol; no se aportan runs_ci, URL pública de SonarCloud ni estado del Quality Gate, y no aparece sonar-project.properties. | No verificado | Comando anotado: curl -s https://api.github.com/repos/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs?per_page=5 y revisión de la línea del scanner en ci.yml. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `0a12f0c04df6943f1f5c39ebf8ca67400d7c6ada 2026-09-17T15:27:54-05:00 docs: adding evidence week 7`
- **Veredicto**: con pendientes
- Resumen: A HEAD de main el proyecto mantiene un monolito modular con cuatro contextos documentados, tabla de propiedad de datos y auditoría de dependencias; la entrega S6 llegó al cierre en c0c3adb y cumple 7 de 8 criterios de la ficha. Quedan abiertos el ADR del reajuste de fronteras y la evidencia auditable de CI/SonarCloud, y se subieron commits después del cierre.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 2837b47 2026-09-15T20:43:43-05:00 feat(api): add OpenAPI contract and contract tests (posterior al cierre).
- 5a4e8dc 2026-09-15T20:48:07-05:00 Merge pull request #13 (posterior al cierre).
- 7b32b3f 2026-09-16T20:31:46-05:00 docs: completa evidencia de contrato y CI (posterior al cierre).
- 3c2ae72 2026-09-16T21:40:14-05:00 Merge pull request #15 (posterior al cierre).
- 0a12f0c 2026-09-17T15:27:54-05:00 docs: adding evidence week 7 (posterior al cierre).

Pendientes que siguen abiertos:
- ADR del reajuste de fronteras entre contextos y, si aplica, C4 nivel 3 actualizado en el mismo cambio.
- Evidencia auditable de CI y SonarCloud: configuración del scanner, run del hash revisado y Quality Gate público.
- Columnas completas y navegables en docs/aspectos.md y columna de lo rechazado en docs/ia.md.
- Persistencia PostgreSQL aún no integrada; los repositorios siguen en memoria.

## Recuento y nota sugerida

7 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 4.5 = 1 + 4 × (7/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido completo de docs/mapa_contextos_s6.md, docs/propiedad_datos_s6.md, docs/auditoria_violaciones_s6.md y docs/aspectos.md, ausentes del extracto.
- Presencia del scanner de SonarCloud en .github/workflows/ci.yml, run exitoso y URL pública del análisis con Quality Gate.
- Diff de docs/c4, docs/arc42 y docs/adr contra el hash revisado en S5, no provisto.
- Ejecución real de la suite declarada (74 pruebas) al no citarse runs_ci.
- Historial de ediciones del ADR-0001 posterior a su aceptación.

## Hallazgos para la planilla

- La auditoría S6 reporta violaciones de dependencia entre contextos (V-01 a V-04), no doble escritura de datos.
- No hay ADR del reajuste de fronteras aunque §8.6 documenta cambios en las dependencias permitidas.
- La evidencia de CI y SonarCloud no es auditable con lo entregado: sin run, sin URL de análisis y sin Quality Gate.
- La persistencia real sigue en memoria; PostgreSQL continúa pendiente según README y §7.2.3.
- Se registraron commits posteriores al cierre hasta el 2026-09-17, fuera del estado calificado.
- Las coincidencias de la búsqueda de secretos son nombres de variables de entorno, no credenciales en claro.
- Commits posteriores al cierre (no calificados): 0a12f0c 2026-09-17T15:27:54-05:00 docs: adding evidence week 7; 3c2ae72 2026-09-16T21:40:14-05:00 Merge pull request #15 from ISCOUTB/val; 7b32b3f 2026-09-16T20:31:46-05:00 docs: completa evidencia de contrato y CI; 5a4e8dc 2026-09-15T20:48:07-05:00 Merge pull request #13 from ISCOUTB/val; 2837b47 2026-09-15T20:43:43-05:00 feat(api): add OpenAPI contract and contract tests
