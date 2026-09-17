# semana-06-evidencia-s6 · Calificación automática

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Estado revisado | `a47d5bd` en `origin/master` (2026-09-13T23:21:55-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/adr/0007-declarar-los-contextos-delimitados-y-la-regla-de-dueno-unico.md, secciones Decisión 1 y 2; hash a47d5bd (2026-09-13T23:21:55-05:00). | Cumple | Tipifica siete contextos y relaciones de núcleo compartido, cliente-proveedor y capa anticorrupción; la tabla citada en arc42 §8.1 no se incluyó en la evidencia. |
| Tabla módulo a datos con dueño único por entidad | docs/arc42/08-propiedad-de-datos.md, tabla «Tabla módulo → dato» con seis entidades y un dueño por fila. | Cumple | Cada entidad tiene un único módulo dueño; se distingue propiedad de ubicación. |
| La tabla cubre las entidades que existen en el código | Árbol incluye backend/infraestructura/modelo.py y backend/infraestructura/cola.py; la tabla lista ArchivoCargado, HojaAceptada, ArchivoRechazado, ResultadoRecepcion, EntradaDeBitacora y Trabajo. | Cumple | Cobertura declarada en el recorrido manual; no se aportó el contenido de los archivos de código para verificación independiente. |
| No conformidades de propiedad de datos detectadas sobre el código actual | No se incluyó la sección de violaciones de docs/arc42/08-propiedad-de-datos.md ni docs/evidencia/hallazgos-y-correcciones.md; solo ADR-0007 cita V-5. | No verificado | Hace falta la lista con entidad, dueño esperado y ubicación observada, o el recorrido que concluyó ausencia. |
| Plan de corrección por no conformidad | No se incluyó la sección con planes de corrección; ADR-0007 solo menciona la corrección de V-5 como pendiente de implementar. | No verificado | Hace falta la acción concreta asociada a cada no conformidad de propiedad. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | No se incluyó la sección 8 del arc42; docs/arc42/08-propiedad-de-datos.md trata propiedad de datos, no el mapa ni el glosario ubicuo. | No verificado | Se necesita el contenido de docs/arc42/08* con lenguaje ubicuo y mapa de contextos. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | No se aportó diff contra el hash revisado en S5 ni el contenido de docs/c4; ADR-0007 existe pero no se puede confirmar si responde a un cambio de límites. | No verificado | Falta el diff docs/c4, docs/arc42, docs/adr contra el hash de S5 y el ADR de reajuste si aplicara. |
| Aspectos relacionables con los contextos del mapa | No se incluyó el contenido de docs/aspectos.md ni el mapa; ADR-0007 solo referencia la tabla de trazabilidad. | No verificado | Hace falta contrastar las filas de aspectos.md con los contextos del mapa. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo AS_202620_Sistema-de-calificacion-automatica, visible=true, cuatro cuentas en el historial; hash a47d5bd. | Cumple | No se aporta prueba de membresía a ISCOUTB, pero el repo y el flujo corresponden a la organización. |
| Estructura mínima | Árbol contiene docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | La documentación arc42 está en Markdown y los ADR siguen la ruta esperada. |
| Convenciones de ADR | docs/adr/0001..0007 con nombres kebab-case; 0001 marcado como reemplazado por 0002; 0004 y 0005 declaran no editar ADR aceptados. | Cumple | Los títulos enuncian decisiones y los ADR incluyen contexto, alternativas, decisión y consecuencias. |
| La tabla de aspectos | docs/aspectos.md existe en el árbol, pero no se incluyó su contenido. | No verificado | Hace falta verificar filas, ocho columnas y cadena aspecto-requisito-C4-ADR-código-pruebas-evidencia. |
| Registro de uso de IA | docs/ia.md existe y muestra historial de commits, pero no se incluyó su contenido. | No verificado | Hace falta comprobar las columnas de uso, herramienta, aceptado y rechazado con motivo. |
| README | README.md describe el sistema, el arranque con docker compose up, las pruebas con pytest/flutter test y los requisitos previos. | Cumple | Cumple con lo mínimo de reproducibilidad y descripción. |
| Pipeline y análisis estático | .github/workflows/ci.yml existe, pero no se aportaron runs_ci, URL pública de SonarCloud ni línea del scanner. | No verificado | Para Cumple se requiere run exitoso, URL del análisis con Quality Gate y rama/hash revisados. |
| Secretos | La evidencia reporta «sin coincidencias» en el patrón de secretos y envs_versionados vacío. | Cumple | No se hallaron secretos ni .env versionado en HEAD. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `a47d5bd660abb2d220071430f869e8ee8ee17bd2 2026-09-13T23:21:55-05:00 docs: corregir el estado del C4 y registrar la decision del nombre`
- **Veredicto**: con pendientes
- Resumen: A HEAD a47d5bd hay avances en contextos, propiedad de datos y ADR, pero la ausencia de runs_ci/SonarCloud y de contenido verificable de aspectos, IA y arc42 §8 impide declarar cumplimiento pleno.

Pendientes que siguen abiertos:
- Aportar runs de CI y URL pública de SonarCloud con Quality Gate para el hash a47d5bd.
- Incluir contenido de docs/aspectos.md y verificar sus ocho columnas.
- Incluir contenido de docs/ia.md con lo aceptado y lo rechazado.
- Incluir arc42 §8 con lenguaje ubicuo y mapa de contextos.
- Aportar lista de no conformidades de propiedad con ubicación y plan, o el recorrido que concluyó ausencia.
- Aportar diff contra el hash de S5 y C4 nivel 3/ADR si los límites cambiaron.

## Recuento y nota sugerida

3 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 2.5 = 1 + 4 × (3/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Lista de no conformidades de propiedad de datos y sus planes de corrección.
- Contenido de docs/aspectos.md y contraste con los contextos del mapa.
- Contenido de docs/ia.md con lo aceptado y lo rechazado.
- Sección 8 del arc42 con lenguaje ubicuo y mapa de contextos.
- C4 nivel 3 actualizado y ADR de reajuste si los límites cambiaron desde el primer corte.
- Runs de CI y URL pública de SonarCloud con Quality Gate para el hash a47d5bd.

## Hallazgos para la planilla

- ADR-0007 declara siete contextos y tipifica relaciones con vocabulario de núcleo compartido, cliente-proveedor y capa anticorrupción.
- docs/arc42/08-propiedad-de-datos.md contiene tabla módulo→dato con seis entidades y un dueño único por entidad.
- No se aportaron runs_ci ni URL pública de SonarCloud; solo existe .github/workflows/ci.yml.
- No se incluyó el contenido de docs/aspectos.md ni de docs/ia.md.
- No se incluyó la sección 8 del arc42 ni el diff contra S5 para verificar C4 nivel 3 y ADR de reajuste.
- La evidencia de secretos no encontró coincidencias ni .env versionado.
- README documenta arranque, pruebas y requisitos previos.
