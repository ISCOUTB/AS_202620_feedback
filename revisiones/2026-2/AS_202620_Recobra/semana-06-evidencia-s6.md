# semana-06-evidencia-s6 · Recobra

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `47fb44b` en `origin/master` (2026-09-13T16:58:53-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/context-map.md en 47fb44b: diagrama Mermaid con Publicaciones, Reclamaciones, Emparejamiento, Notificaciones e Identidad; relaciones Cliente/Proveedor, Conformista y Capa anticorrupción. | Cumple | Usa dominios núcleo/soporte/genérico; no aparece 'núcleo compartido', pero sí los patrones exigidos. |
| Tabla módulo a datos con dueño único por entidad | docs/modulo-datos.md en 47fb44b: tabla con Publicacion, Coincidencia, Notificacion, Usuario y Reclamacion, un dueño por fila. | Cumple | Declara regla de un dato/un dueño y consulta por id/puerto. |
| La tabla cubre las entidades que existen en el código | Árbol 47fb44b: solo src/domain/entities/publicacion.ts; docs/modulo-datos.md incluye Publicacion y marca el resto como planeado. | Cumple | No hay otras entidades en src/. |
| No conformidades de propiedad de datos detectadas sobre el código actual | docs/no-conformidades.md en 47fb44b (extracto): lista token Coveralls, correcciones.md y arc42 fragmentada. | No verificado | El extracto no muestra auditoría de propiedad de datos; falta el resto del archivo o el recorrido de escrituras. |
| Plan de corrección por no conformidad | docs/no-conformidades.md (extracto) trae planes para los tres puntos visibles. | No verificado | No se puede confirmar plan para no conformidades de propiedad de datos por extracto truncado. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/arc42.md en 47fb44b; el extracto visible llega hasta secciones 6, 9 y 10. | No verificado | No se observa la sección 8; hace falta el archivo completo o cita de línea de 08*. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/C4-C3.md existe en 47fb44b; ADR-0001/0002/0003 no mencionan reajuste de contextos. | No verificado | Falta hash S5 y diff; no se puede saber si los límites cambiaron ni si el ADR corresponde. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md en 47fb44b: A1/A4 conectan con Publicaciones, A3 con Reclamaciones; A2 es transversal. | Cumple | Emparejamiento, Notificaciones e Identidad no tienen fila de aspecto. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_Recobra visible en 47fb44b; historial con 5 cuentas autoras. | Cumple | 4 integrantes declarados y una cuenta autora adicional; no se atribuyen cuentas a personas por nombre. |
| Estructura mínima | Árbol 47fb44b: docs/arc42/arc42.md, docs/adr/0001-0003, docs/c4/C4-C1/C2/C3, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Los artefactos mínimos están presentes, algunos en rutas no idénticas a la plantilla. |
| Estado del repositorio calificado | origin/master; hash calificado 47fb44b con fecha 2026-09-13T16:58:53-05:00. | Cumple | Commit anterior al cierre de S6; no se reportan commits posteriores al cierre. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md, 0002-arquitectura-y-stack.md y 0003-reto-corte1-stack-obligatorio.md en 47fb44b. | Cumple | Nombres numerados en kebab-case; ADR-0001 figura reemplazada por ADR-0002. |
| La tabla de aspectos | docs/aspectos.md en 47fb44b con 8 columnas y filas A1-A4. | Cumple | La fila A3 contiene celdas de implementación futura; el alcance de la semana no pide más. |
| Registro de uso de IA | docs/ia.md en 47fb44b con tabla de usos, herramientas, aceptado y rechazado; historial de commits del archivo. | Cumple | El registro crece a lo largo del semestre y documenta criterios de rechazo. |
| README | README.md en 47fb44b: qué es, arranque con un comando para backend y pasos para Flutter, y comandos de prueba. | Cumple | Declara requisitos previos y remite a CI para pruebas automatizadas. |
| Pipeline y análisis estático | Existen .github/workflows/ci.yml y sonar-project.properties en 47fb44b, pero no se aportan runs_ci ni URL pública de SonarCloud. | No verificado | Falta run exitoso para el hash revisado y URL del Quality Gate; comprobar con el comando de runs de GitHub Actions. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `47fb44bb7c5cca9b1c7a6d020649a086600ee619 2026-09-13T16:58:53-05:00 Rename file to 'restricciones_justificadas.md'`
- **Veredicto**: con pendientes
- Resumen: Proyecto completo en origin/master 47fb44b; S6 aporta mapa de contextos y tabla módulo-datos, pero quedan sin verificar la sección 8, el diff contra S5, la auditoría de propiedad de datos y la evidencia auditable de SonarCloud, además del incidente de token abierto.

Pendientes que siguen abiertos:
- Token de Coveralls expuesto en el historial, declarado abierto en docs/no-conformidades.md.
- Run de CI y URL pública de SonarCloud con Quality Gate para 47fb44b.
- arc42 sección 8 con lenguaje ubicuo y mapa de contextos.
- Diff contra hash S5, C4 nivel 3 y ADR si cambiaron los límites.
- Auditoría de no conformidades de propiedad de datos y su plan de corrección.
- Verificación de correspondencia entre integrantes declarados y cuentas del historial.

## Recuento y nota sugerida

4 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 3.0 = 1 + 4 × (4/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- No conformidades de propiedad de datos sobre el código actual: falta el archivo completo o el recorrido de escrituras.
- Plan de corrección de esas no conformidades: no visible en el extracto.
- arc42 sección 8: no visible en el extracto.
- C4 nivel 3 y ADR de reajuste: falta hash S5 y diff.
- Pipeline/SonarCloud: falta run de CI y URL pública del análisis con Quality Gate.
- Identidad/membresía de integrantes: no se aporta .mailmap ni pertenencia a la organización.

## Hallazgos para la planilla

- El repositorio está en ISCOUTB, es público y la rama calificada es origin/master en 47fb44b (2026-09-13).
- docs/context-map.md tipifica relaciones Cliente/Proveedor, Conformista y Capa anticorrupción.
- docs/modulo-datos.md asigna dueño único a Publicacion, Coincidencia, Notificacion, Usuario y Reclamacion.
- No hay evidencia de runs_ci ni URL pública de SonarCloud con Quality Gate.
- docs/no-conformidades.md declara abierto un token de Coveralls expuesto en el historial.
- No se aporta diff contra S5 ni hash de S5 para verificar reajuste de límites y ADR.
- El extracto de arc42 no muestra la sección 8.
- La auditoría de no conformidades de propiedad de datos no es verificable con el extracto.
