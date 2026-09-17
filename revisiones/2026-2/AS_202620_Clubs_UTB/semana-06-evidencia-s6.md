# semana-06-evidencia-s6 · Clubs UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `743cc1f` en `origin/master` (2026-09-13T23:55:10-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/arc42/mapa-contextos-fundamentacion.md y docs/arc42/08_conceptos_transversales.md §8.2 (mermaid + tabla de tipos de relación), en 743cc1f | Cumple | Tres contextos internos (Clubes, Publicaciones, Usuarios) más Supabase Auth externo, con núcleo compartido, cliente-proveedor y capa anticorrupción. |
| Tabla módulo a datos con dueño único por entidad | docs/arc42/tabla_modulo.md (columnas contexto / datos administrados / referencias / operaciones), en 743cc1f | Cumple | No hay migraciones ni esquema SQL; el contraste se hizo contra la única entidad implementada (backend/src/linkclub/domain/publicacion.py). |
| La tabla cubre las entidades que existen en el código | tabla_modulo.md §'Cobertura frente al código actual' cita domain/publicacion.py como única entidad y declara Usuarios y Clubes sin entidad, coherente con el árbol de 743cc1f | Cumple | No existe entidad Actividad ni Notificacion en el código revisado. |
| No conformidades de propiedad de datos detectadas sobre el código actual | docs/arc42/lista_errores.md NC-01 (datos de clubes en frontend/linkclub/lib/clubs_page.dart) y docs/adr/0002-hexagonal.md, trazabilidad: 'fuera del contexto Clubes' | Cumple | Entidad, dueño esperado y ubicación están; el patrón/alcance del recorrido de auditoría no se documenta. |
| Plan de corrección por no conformidad | lista_errores.md columna 'plan de corrección': NC-01 'usar los datos de la base de datos cuando esté lista'; NC-02 'agregar estados de carga y error' | Cumple | Acciones concretas pero sin fecha ni responsable. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/08_conceptos_transversales.md §8.1 (glosario por contexto) y §8.2 (diagrama mermaid), en 743cc1f | Cumple | §8.3 mantiene como pendiente una alineación con tabla_modulo.md que el archivo ya refleja. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/adr/0002-hexagonal.md (13/09/2026) documenta el reajuste y docs/c4/contexto.md incluye un diagrama de componentes (nivel 3) | No verificado | Falta el hash revisado en S5 para ejecutar git diff --stat <HASH_S5>..743cc1f -- docs/c4 docs/arc42 docs/adr y confirmar la actualización del nivel 3. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md: columnas ID/Aspecto/Escenario/Requisito/C4/ADR/Código/Pruebas, sin columna de contexto; la columna C4 apunta a docs/c4/contexto.md (niveles 1-2) | No cumple | U3 es atribuible a Usuarios y C1 a Publicaciones, pero la correspondencia no está escrita; U1, C2 y C3 quedan sin contexto asignado. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Árbol y README.md §5 de 743cc1f: organización ISCOUTB, repositorio AS_202620_Clubs_UTB público, 6 identidades git en el historial | Cumple | Josh Ortega y Josh4OP comparten una misma cuenta de correo (una sola identidad); no se fusionan por parecido de nombre las dos variantes 'Luis'. |
| Estructura mínima | 743cc1f contiene docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md | Cumple | Faltan las secciones arc42 07 y 11; toda la documentación está en Markdown revisable. |
| Estado del repositorio que se califica | origin/master 743cc1f 2026-09-13T23:55:10-05:00, anterior o igual al cierre 2026-09-14T05:00:00Z; no hay rama main | Cumple | HEAD d2d1450 (2026-09-15) es posterior al cierre y no altera la matriz. |
| Convenciones de ADR | docs/adr/0001-hexagonal.md y docs/adr/0002-hexagonal.md cumplen el patrón NNNN-kebab-case y 0002 no edita el 0001 | Cumple | 0002 repite el sufijo 'hexagonal' y tabla_modulo.md enlaza a docs/adr/0002-ajuste-contextos-publicaciones.md, archivo inexistente. |
| La tabla de aspectos | docs/aspectos.md (743cc1f): encabezado sin columna 'Evidencia' y celdas 'Pendiente' en Código/Pruebas de U1, C1, C2 y C3; ADR '—' en U1, U3 y C2 | No cumple | Filas con huecos según la regla del contrato: no son defendibles de punta a punta. |
| Registro de uso de IA | docs/ia.md (743cc1f) con tabla por semana: para qué, herramienta, cómo se usó y motivo, incluyendo 'no incorporado' y 'se usó parcialmente' | Cumple | Documenta lo aceptado y lo rechazado; se amplió tras el cierre en d2d1450. |
| README | README.md §7: requisitos previos (Python 3.10+), arranque con 'uvicorn linkclub.main:app --app-dir src' y pruebas con 'PYTHONPATH=src pytest tests/ -v' | Cumple | El arranque no se ejecutó localmente; la evidencia indirecta es el run de pruebas exitoso de CI. |
| Pipeline y análisis estático | .github/workflows/backend-tests.yml solo define pytest; no hay sonar-project.properties ni paso del scanner. runs_ci: 'Backend tests' success https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/34801426289 (2026-09-14T03:06:24Z) | No cumple | Falta la URL pública de SonarCloud con estado del Quality Gate exigida desde S6. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `d2d14508c71639a2adb9acc53be97f50039ed0d8 2026-09-15T10:14:52-05:00 Update IA usage log for week 6`
- **Veredicto**: con pendientes
- Resumen: En HEAD (d2d1450) se mantiene lo entregado en S6: mapa de contextos, tabla de dueño único, ADR 0002 y lista_errores.md; sin embargo fallan la tabla de aspectos y el análisis SonarCloud exigido desde S6, el mapeo aspectos-contextos no está documentado y quedan no conformidades de semanas previas sin cerrar sobre la rama master.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- d2d1450 'Update IA usage log for week 6' (2026-09-15T10:14:52-05:00), único cambio en diff_desde_cierre: docs/ia.md, con run 'Backend tests' success del 2026-09-15T15:14:55Z (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/34987143230).

Pendientes que siguen abiertos:
- NC-01: datos de clubes hardcodeados en frontend/linkclub/lib/clubs_page.dart, sin consumir el contexto Clubes.
- NC-02: ausencia de manejo de errores de conexión en el backend.
- Enlace roto a docs/adr/0002-ajuste-contextos-publicaciones.md y documentos que declaran pendiente una alineación ya aplicada.
- Análisis estático SonarCloud ausente del pipeline y sin URL pública con Quality Gate.
- docs/aspectos.md con celdas 'Pendiente' y sin columna de evidencia; sin mapeo a los contextos del mapa.
- Secciones arc42 07 y 11 no presentes en el repositorio.

## Recuento y nota sugerida

6 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 4.0 = 1 + 4 × (6/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Actualización del C4 nivel 3 tras el reajuste de límites: hace falta el hash revisado en S5 para ejecutar git diff --stat <HASH_S5>..743cc1f -- docs/c4 docs/arc42 docs/adr.
- Arranque del backend no verificado por ejecución; evidencia indirecta: run 'Backend tests' conclusion success (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/34801426289); comando anotado: uvicorn linkclub.main:app --app-dir src.
- URL pública de SonarCloud y estado del Quality Gate: no encontrados; se buscó scanner en .github/workflows/backend-tests.yml y archivo de configuración del análisis en el árbol de 743cc1f.

## Hallazgos para la planilla

- Ambas matrices quedan en 6 de 8 criterios cumplidos.
- El mapa de contextos tipifica relaciones con vocabulario DDD (núcleo compartido, cliente-proveedor, ACL).
- ADR 0002 documenta la fusión de Actividades y Notificaciones en el contexto Publicaciones.
- lista_errores.md reporta NC-01 sobre clubs_page.dart como violación de propiedad del contexto Clubes.
- No hay SonarCloud: el pipeline solo ejecuta pytest, sin scanner ni URL de análisis.
- docs/aspectos.md omite la columna 'Evidencia' y deja celdas 'Pendiente' en U1, C1, C2 y C3.
- La correspondencia entre contextos del mapa y filas de aspectos no está escrita en ningún documento.
- tabla_modulo.md enlaza a docs/adr/0002-ajuste-contextos-publicaciones.md, que no existe en el árbol.
- ADR 0002 y arc42 §8.3 declaran pendiente una alineación que tabla_modulo.md ya aplica.
- Faltan las secciones arc42 07 y 11.
- Sin coincidencias de secretos ni archivos .env versionados (743cc1f).
- Commits posteriores al cierre (no calificados): d2d1450 2026-09-15T10:14:52-05:00 Update IA usage log for week 6
