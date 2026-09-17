# semana-06-evidencia-s6 · Verifacts

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `5941c33` en `origin/master` (2026-09-12T02:00:20-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/mapa-contextos.md @5941c33 (2026-09-12): diagrama mermaid con tres contextos y tabla de relaciones. | Cumple | Tipifica Customer/Supplier, Published Language y Conformist; no usa 'núcleo compartido' ni 'capa anticorrupción' del vocabulario de la semana. |
| Tabla módulo a datos con dueño único por entidad | docs/propiedad-datos.md @5941c33: tabla dato-módulo con dueño único de escritura y lectores permitidos. | Cumple | Afirma que la lectura del historial es de un 'endpoint aún no implementado', pero GET /analysis ya existe (README y arc42 §6). |
| La tabla cubre las entidades que existen en el código | app/persistence/repository.py define la tabla de análisis y docs/propiedad-datos.md la cubre con sus columnas principales @5941c33. | Cumple | No lista created_at ni source_type, columnas que el propio repo documenta en docs/implementacion-backend.md §1 y arc42 §6. |
| No conformidades de propiedad de datos detectadas sobre el código actual | docs/violaciones-modularidad.md y docs/propiedad-datos.md ('Estado verificado') @5941c33: registro sin violaciones, con método y archivos revisados. | Cumple | El recorrido solo busca sqlite3.connect fuera de repository.py; no documenta búsqueda de INSERT/UPDATE/.save en módulos de negocio y no fue re-ejecutable (la evidencia no incluye el contenido de app/). |
| Plan de corrección por no conformidad | docs/violaciones-modularidad.md @5941c33: sección de registro y método a repetir por cada módulo o endpoint nuevo. | Cumple | No hay no conformidades declaradas, por lo que no existe acción asociada; queda preparado el formato de registro. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/08-conceptos transversales.md, apartado 'Modelo de dominio y contextos delimitados (S6)' con tabla de lenguaje ubicuo y enlaces al mapa y a la propiedad @5941c33. | Cumple | El bloque se insertó con el comentario de plantilla HTML y un texto cortado al final del archivo. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/adr/0002-contextos-sin-cambios.md (2026-09-11) y docs/c4/03-componentes.md con correspondencia a código @5941c33. | Cumple | No se aportó el hash revisado en S5 ni el diff contra él; la evidencia es el ADR que declara límites sin cambio. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md: columna 'Contexto (mapa-contextos.md)' con Ingesta y Presentación, Análisis de Contenido e Historial en A-00 a A-03 @5941c33. | Cumple | El texto menciona A-04 sin fila propia a la fecha calificada (la fila se agregó el 2026-09-16). |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio público en la organización ISCOUTB con el nombre AS_202620_<PROYECTO> | Árbol @5941c33: repo AS_202620_Verifacts visible; historial con solo dos cuentas (PedroC1213, con dos identidades consolidadas, y Cristian Cardeño). | No cumple | El tercer integrante declarado no registra commits a 5941c33; sin secretos ni .env versionados (sin coincidencias). |
| Estructura mínima (docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md) | Árbol @5941c33 con docs/arc42/01 a 11, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Falta un archivo 12-* (el glosario vive en 11-glosario.md titulado 'Sección 12') y el README enlaza documentos inexistentes. |
| Estado calificado: último commit de master/main anterior o igual al cierre | origin/master 5941c33, 2026-09-12T02:00:20-05:00, anterior al cierre 2026-09-14T05:00:00Z. | Cumple | Existen diez commits posteriores al cierre (2026-09-16) que no cambian la matriz. |
| Convenciones de ADR (numeración, título-decisión, inmutabilidad, trazabilidad) | docs/adr/0001-estilo-arquitectonico.md y docs/adr/0002-contextos-sin-cambios.md siguen el patrón NNNN-titulo-en-kebab-case @5941c33. | Cumple | ADR-0001 no trae trazabilidad con commit/PR ni pruebas, y no se aportó el log de reescrituras posteriores a su aceptación. |
| Tabla de aspectos con la cadena navegable de ocho columnas | docs/aspectos.md @5941c33: ocho columnas más una de contexto, con A-00 a A-03. | No cumple | A-00 remite a la pestaña Actions genérica y la propia nota admite un marcador [PENDIENTE]; A-04 se cita sin fila y la evidencia de A-02/Q-03 se contradice entre documentos. |
| Registro de uso de IA con lo aceptado y lo rechazado y su motivo | docs/ia.md @5941c33: bitácora por interacción con fecha, herramienta, propósito, resultado y validación. | No cumple | No aparece la entrada de lo rechazado con su motivo técnico; solo se declara dentro de una celda de validación que ese rechazo estaría documentado. |
| README con qué es, cómo se arranca y cómo se prueba | README.md @5941c33: descripción, estado, arranque (python run.py y npm run dev) y pruebas (python -m pytest -q). | Cumple | Documenta dos comandos de arranque (backend y frontend), no uno, y enlaza docs/decisiones-arquitectonicas-explicadas.md y docs/09-decisiones-arquitectonicas.md, que no existen. |
| Pipeline de pruebas y análisis estático en SonarCloud (scanner, run exitoso y URL pública con Quality Gate) | Árbol @5941c33 incluye .github/workflows/tests.yml, .github/workflows/sonarcloud.yml y sonar-project.properties, pero la evidencia no aporta runs_ci ni URL de SonarCloud. | No verificado | Falta el run del scanner para el hash revisado y el Quality Gate público; comprobar con curl -s "https://api.github.com/repos/ISCOUTB/AS_202620_Verifacts/actions/runs?per_page=5". |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `635f9b7b26764de3c9636d01f4500b7c1660dfa8 2026-09-16T00:52:52-05:00 Update README with new API endpoints and usage`
- **Veredicto**: con pendientes
- Resumen: A HEAD los ocho criterios de la ficha S6 se sostienen, pero la matriz transversal deja pendientes: integrante declarado sin historial, evidencia de CI y SonarCloud sin URL de run, marcador pendiente en la tabla de aspectos, registro de IA sin lo rechazado y notas de propiedad desactualizadas; además diez commits llegaron dos días después del cierre.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Filas A-04 y A-05 en docs/aspectos.md (b5d9068, 2026-09-16T00:51:03-05:00)
- ADR-0003 y especificación OpenAPI del API (fa29e9a y f3caf45, 2026-09-16)
- Pruebas de contrato de endpoints (9fdf092, 2026-09-16T00:47:30-05:00)
- Actualizaciones de README (8e24d72 y 635f9b7, 2026-09-16)
- pyyaml y jsonschema en requirements (2bf64ca, 2026-09-16)
- Ajustes de vistas de bloques y ejecución y de decisiones (3d07ec5, 122273b, 89b1928, 2026-09-16)

Pendientes que siguen abiertos:
- Evidencia de CI con URL de run para el hash revisado
- URL pública de SonarCloud con estado del Quality Gate
- Entrada de lo rechazado con motivo técnico en docs/ia.md
- Reemplazo del marcador [PENDIENTE] en A-00 y fila propia para A-04
- Commits del tercer integrante declarado
- Enlaces del README a documentos inexistentes
- Medición de P95 (Q-01) y prueba de usuario (Q-04)

## Recuento y nota sugerida

8 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 5.0 = 1 + 4 × (8/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución real de la suite y del arranque en el hash 5941c33: la evidencia no incluye runs_ci; hace falta la URL del run en verde o el log de python -m pytest -q.
- SonarCloud: existen el workflow y sonar-project.properties, pero faltan el run del scanner para el hash revisado y la URL pública del análisis con su Quality Gate.
- Contraste de escrituras por entidad sobre el código: no se incluyó el contenido de app/ ni la salida de git grep -nIE '(INSERT INTO|UPDATE |\.save\(|\.create\(|\.update\()' HEAD, por lo que la ausencia de violaciones no pudo re-ejecutarse.
- Diferencia contra el corte anterior: no se aportó el hash de master/main revisado en S5 ni el diff de docs/c4, docs/arc42 y docs/adr contra él.

## Hallazgos para la planilla

- Solo dos cuentas aparecen en el historial a 5941c33 (PedroC1213, con dos identidades consolidadas, y Cristian Cardeño); el tercer integrante declarado no registra commits.
- docs/aspectos.md conserva el marcador [PENDIENTE] de evidencia de CI en A-00 y cita A-04 sin fila propia a la fecha calificada.
- docs/propiedad-datos.md afirma que la lectura del historial es de un endpoint 'aún no implementado' cuando GET /analysis ya existe.
- README enlaza documentos que no están en el árbol (decisiones-arquitectonicas-explicadas.md y docs/09-decisiones-arquitectonicas.md).
- docs/violaciones-modularidad.md audita solo conexiones sqlite3 directas, no escrituras INSERT/UPDATE/.save desde otros módulos.
- Diez commits se subieron el 2026-09-16, dos días después del cierre, con ADR-0003, contrato OpenAPI, pruebas de contrato y filas A-04/A-05.
- arc42 §8 quedó con un comentario de plantilla HTML y texto cortado en el bloque añadido en S6.
- docs/ia.md no contiene una entrada explícita de lo rechazado con su motivo técnico.
- Commits posteriores al cierre (no calificados): 635f9b7 2026-09-16T00:52:52-05:00 Update README with new API endpoints and usage; 8e24d72 2026-09-16T00:51:41-05:00 Enhance README with detailed API and feature descriptions; b5d9068 2026-09-16T00:51:03-05:00 Add aspects A-04 and A-05 to aspectos.md; 3d07ec5 2026-09-16T00:50:36-05:00 Enhance database entry details and API status; 89b1928 2026-09-16T00:50:04-05:00 Enhance execution view documentation for scenarios
