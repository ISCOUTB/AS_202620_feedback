# semana-06-evidencia-s6 · PideUtb

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `006edfe` en `origin/master` (2026-09-13T16:37:23-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/ddd-contextos.md §2 (hash 006edfe, 2026-09-13): mapa Mermaid con contextos Catálogo, Pedidos, Pagos y Cuentas, y tabla de relaciones customer/supplier y anticorruption layer. | Cumple | Nombra contextos del dominio propio y tipifica las relaciones con vocabulario de la semana. |
| Tabla módulo a datos con dueño único por entidad | docs/ddd-contextos.md §3 (006edfe): tabla con Dato, Módulo dueño único y módulos lectores. | Cumple | Cada dato tiene un único escritor declarado; los lectores se resuelven vía service/contracts. |
| La tabla cubre las entidades que existen en el código | docs/ddd-contextos.md §3 incluye Ítem de menú (menu/models.py), Pedido (pedidos/models.py), Establecimiento y Cuenta (usuarios/models.py) y Transacción/código (pagos, previsto). | Cumple | Cubre las entidades implementadas y las previstas de pagos. |
| No conformidades de propiedad de datos detectadas sobre el código actual | docs/violaciones.md (006edfe): V-01 y V-02 documentan escrituras indebidas sobre Establecimiento y pedidos; V-05 filtración de modelo. | Cumple | Auditoría sobre código actual, con reproducción y rutas concretas. |
| Plan de corrección por no conformidad | docs/violaciones.md: cada V-01 a V-09 tiene corrección aplicada o plan (p. ej. V-07 centavos, V-08 estados, V-09 persistencia). | Cumple | Plan concreto y pruebas asociadas en las corregidas. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/ddd-contextos.md menciona que se referencia desde arc42.md §8, pero el contenido de arc42 §8 no consta en la evidencia recibida (arc42.md truncado). | No verificado | Falta citar el archivo completo o la sección 8 para verificar lenguaje ubicuo y mapa. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/nivel3-modulos.md (actualización S6) y docs/adr/0002-propiedad-datos-establecimiento.md (aceptada 13/09/2026) documentan el reajuste de límites. | Cumple | No se aporta el hash de S5 para el diff, pero los artefactos exigidos están en el repositorio. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md (006edfe): ESC-01 a ESC-05 enlazan con C4 nivel 3, ADR y código de los módulos menu, pedidos, usuarios y pagos. | Cumple | Los escenarios se relacionan con los contextos del mapa; ESC-04 y ESC-05 pendientes de pagos. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo visible AS_202620_PideUtb, organización ISCOUTB, rama origin/master; autores incluyen Santiago Cuesta, daniarriet y Ruddy (006edfe). | Cumple | Los integrantes declarados aparecen en el historial consolidado. |
| Estructura mínima | árbol incluye docs/arc42/arc42.md, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | Rutas mínimas presentes y documentación en Markdown. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md título "Estilo arquitectónico del backend de PideUTB" y 0002 "Propiedad de los datos de Establecimiento..." enuncian tema, no decisión. | No cumple | Nombres de archivo correctos y ADR con contexto, opciones, decisión, consecuencias y trazabilidad; falta título-decisión. |
| La tabla de aspectos | docs/aspectos.md con 8 columnas: ID, Aspecto, Escenario, Medida, C4, ADR, Código, Pruebas y enlaces navegables. | Cumple | Filas pendientes marcadas con ⏳ según la semana. |
| Registro de uso de IA | docs/ia.md (006edfe) detalla entregas, herramienta y tabla de propuestas rechazadas con motivo. | Cumple | Incluye qué se rechazó y por qué. |
| README | README.md describe el sistema, arranque con un solo comando, pruebas y requisitos previos. | Cumple | Comando único de arranque y suite documentada. |
| Pipeline y análisis estático | .github/workflows/ci.yml está en el árbol, pero no se aportan runs_ci ni URL pública de SonarCloud con Quality Gate para 006edfe. | No verificado | Comando sugerido: consultar runs de Actions y SonarCloud para el hash; falta la triple evidencia del contrato. |
| Secretos | evidencia indica "secretos": "(sin coincidencias)" y "envs_versionados": []. | Cumple | No se hallaron credenciales ni .env versionado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `006edfe555ed809d027d7ed47657efc6a451f325 2026-09-13T16:37:23-05:00 Actualizar la evidencia de CI y reconvertir el documento de linea base`
- **Veredicto**: al dia
- Resumen: Proyecto en HEAD 006edfe (2026-09-13) sobre origin/master; sin commits post-cierre. Mapa de contextos, tabla de propiedad y auditoría de violaciones están documentados; faltan evidencias de SonarCloud y la verificación de arc42 §8, y los títulos de ADR no siguen la convención.

Pendientes que siguen abiertos:
- Evidencia pública de SonarCloud con Quality Gate para el hash revisado
- Títulos de ADR que enuncien la decisión
- Contenido verificable de arc42 §8
- Diff contra hash de S5 para confirmar el reajuste de límites

## Recuento y nota sugerida

7 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 4.5 = 1 + 4 × (7/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 §8 con lenguaje ubicuo y mapa de contextos: falta el contenido de la sección 8 en la evidencia.
- Pipeline y SonarCloud: falta run de CI para 006edfe y URL pública del análisis con Quality Gate.
- Diferencia contra el hash de S5: falta el hash revisado en S5 para contrastar cambios de límites.

## Hallazgos para la planilla

- Mapa de contextos y tabla de propiedad de datos están documentados y auditados sobre el código actual.
- Los ADR 0001 y 0002 tienen títulos de tema, no de decisión, según la convención del contrato.
- No se aporta evidencia pública de SonarCloud (run, URL y Quality Gate) para el hash 006edfe.
- El contenido de arc42 §8 no consta en la evidencia recibida; solo la referencia desde ddd-contextos.
- La tabla de aspectos relaciona ESC-01 a ESC-05 con contextos y módulos.
- No hay commits posteriores al cierre ni secretos detectados.
