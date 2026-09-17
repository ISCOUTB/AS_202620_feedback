# semana-06-evidencia-s6 · ROUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `5b48dd0` en `origin/master` (2026-09-13T23:43:22-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/arc42/08_conceptos_transversales.md, sección '8.2 Mapa de contextos funcionales' (diagrama mermaid + tabla con 'Relación principal' de cada contexto). | Cumple | Nombra contextos del dominio (Identidad y Usuarios, Gestión de Recorridos, Solicitudes y Reservas, Notificaciones, Administración) y tipifica relaciones, pero no usa literalmente el vocabulario núcleo compartido/cliente-proveedor/capa anticorrupción. |
| Tabla módulo a datos con dueño único por entidad | docs/propiedad_de_datos.md aparece en el árbol pero su contenido no se incluye en la evidencia entregada. | No verificado | No se pudo comprobar el dueño único por entidad; haría falta extraer la tabla del archivo citado en docs/aspectos.md fila 4. |
| La tabla cubre las entidades que existen en el código | Modelos y migraciones existen (backend/app/modules/*/models.py; backend/migrations/versions/001_crear_users_y_trips.py, 002_update_trips_requests.py) pero no se aporta el contenido de la tabla. | No verificado | No es contrastable la cobertura entidad a entidad frente al esquema real. |
| No conformidades de propiedad de datos detectadas sobre el código actual | docs/evidencia/hallazgos.md y correcciones.md están en el árbol; su contenido no se incluye en la evidencia. | No verificado | No hay lista citable de entidad, módulo dueño esperado y ubicación observada para el hash 5b48dd0. |
| Plan de corrección por no conformidad | No se aporta el contenido de las no conformidades ni de su plan (docs/evidencia/hallazgos.md, correcciones.md). | No verificado | Imposible asociar acciones concretas a cada hallazgo sin el contenido. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/08_conceptos_transversales.md contiene '8.1 Lenguaje ubicuo técnico' y '8.2 Mapa de contextos funcionales'. | Cumple | El lenguaje definido es mayormente técnico; los términos de dominio están en el glosario (docs/arc42/12_glosario.md). |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/context.md incluye 'Nivel 3 - Componentes' y docs/adr/0003-control-atomico-de-cupos.md documenta el cambio. | Cumple | No se aportó el hash de S5, por lo que el diff contra el primer corte no es verificable; el documento afirma 'Límites conservados tras el cambio'. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md incluye columna 'Contextos relacionados' que referencia Identidad y Usuarios, Gestión de Recorridos, Solicitudes y Reservas, Notificaciones y Administración. | Cumple | Los enlaces apuntan a docs/c4/context.md aunque el mapa de contextos funcional está en arc42/08; la correspondencia de nombres es válida. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima | El árbol incluye docs/arc42/, docs/adr/ (0001-0003), docs/c4/context.md, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Se cumple la estructura del contrato; no se observan desviaciones. |
| Estado del repositorio calificado | Hash 5b48dd0 en origin/master, fecha 2026-09-13T23:43:22-05:00, anterior al cierre 2026-09-14T05:00:00Z. | Cumple | Rama principal origin/master; existe un commit posterior al cierre (dcd3317) que no se computa. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md, 0002-usar-arquitectura-interna-por-capas.md, 0003-control-atomico-de-cupos.md con nombres NNNN-kebab y títulos que enuncian la decisión. | Cumple | Cada ADR trae contexto, opciones, decisión, consecuencias y trazabilidad. |
| La tabla de aspectos | docs/aspectos.md con columnas ID, Aspecto, Requisito, Contextos relacionados, C4, ADR, Código, Pruebas y Evidencia en 4 filas. | Cumple | Incluye las 8 columnas del curso más una de contextos; las celdas enlazan a artefactos navegables. |
| Registro de uso de IA | docs/ia.md existe y crece (7 registros en ia_log, último 2026-09-13T18:16:59-05:00), pero su contenido no se incluye. | No verificado | No se puede comprobar la columna de lo rechazado y su motivo técnico. |
| README | README.md describe el sistema, requisitos previos (venv, pip install, flutter pub get), arranque (uvicorn app.main:app --reload; flutter run) y pruebas (pytest). | Cumple | El arranque se documenta por pasos más un comando, no como un único comando empaquetado. |
| Pipeline y análisis estático | .github/workflows/ci.yml en el árbol; no existe sonar-project.properties y no se cita URL pública de SonarCloud ni Quality Gate; la evidencia no aporta runs_ci. | No cumple | Faltan las tres evidencias exigidas en S6 (configuración/línea del scanner, run exitoso para el hash y URL del Quality Gate). |
| Secretos | Los aciertos del patrón son campos y funciones de contraseña/token (backend/app/modules/users/models.py, auth/service.py, tests) y no credenciales reales; envs_versionados = []. | Cumple | No se hallaron claves, tokens ni .env versionados; coincidencias son falsos positivos del patrón. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `dcd33171ef4ef022278626ea0c0a2c418997afe3 2026-09-16T21:46:43-05:00 s7 - early`
- **Veredicto**: con pendientes
- Resumen: En la punta de origin/master (5b48dd0, previo al cierre) el proyecto entrega mapa de contextos, lenguaje ubicuo, C4 nivel 3 y ADRs coherentes; sin embargo falta evidencia auditable de SonarCloud y varias piezas centrales de S6 (propiedad de datos, no conformidades, IA) no son verificables con lo aportado.

Pendientes que siguen abiertos:
- Evidencia pública de SonarCloud (scanner, run y Quality Gate) para el hash 5b48dd0
- Contenido de docs/propiedad_de_datos.md (tabla módulo a datos con dueño único)
- Lista de no conformidades y plan (docs/evidencia/hallazgos.md)
- Contenido de docs/ia.md (uso de IA y lo rechazado)

## Recuento y nota sugerida

4 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.0 = 1 + 4 × (4/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Tabla módulo a datos (docs/propiedad_de_datos.md): contenido no incluido en la evidencia; haría falta extraer el archivo.
- No conformidades y su plan (docs/evidencia/hallazgos.md, correcciones.md): contenido no incluido.
- Registro de IA (docs/ia.md): contenido no incluido; no verificable la columna de lo rechazado.
- Ejecución de CI/SonarCloud para el hash 5b48dd0: falta runs_ci (nombre, conclusión, URL); comprobar con git ls-tree y la API de actions/runs del repositorio.

## Hallazgos para la planilla

- No hay sonar-project.properties ni URL pública de SonarCloud; el Quality Gate no es auditable.
- El README cita un run de CI pero la evidencia no aporta runs_ci con nombre y conclusión.
- No se incluyó el contenido de docs/propiedad_de_datos.md ni de docs/evidencia/hallazgos.md, clave para S6.
- Existe un commit posterior al cierre (dcd3317, 2026-09-16, 's7 - early'); no altera la nota de S6.
- El mapa de contextos no usa literalmente el vocabulario de tipos de relación de la semana.
- Las coincidencias de secretos corresponden a nombres de campos de contraseña/token, no a credenciales reales.
- Commits posteriores al cierre (no calificados): dcd3317 2026-09-16T21:46:43-05:00 s7 - early
