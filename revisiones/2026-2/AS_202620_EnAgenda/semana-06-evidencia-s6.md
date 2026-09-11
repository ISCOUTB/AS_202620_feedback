# semana-06-evidencia-s6 · EnAgenda

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `696882e` en `origin/master` (2026-09-07T16:21:16-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | No se encontró mapa de contextos en docs/; docs/arc42/08-conceptos-transversales.md dice 'Esta sección se completará durante el desarrollo del proyecto' (696882e) | No cumple | No se nombran contextos del dominio ni relaciones (núcleo compartido, cliente-proveedor, capa anticorrupción). |
| Tabla módulo a datos con dueño único por entidad | No existe tabla módulo-datos en docs/; única entidad real Invitacion en src/invitaciones/dominio/invitaciones.py (696882e) | No cumple | No se cita tabla alguna con dueño único. |
| La tabla cubre las entidades que existen en el código | Sin tabla, no cubre entidades; esquema real es repositorio en memoria en src/invitaciones/infraestructura/repositorio_memoria.py (696882e) | No cumple | No hay migraciones ni esquema; la tabla ausente no puede contrastarse. |
| Violaciones de propiedad de datos detectadas sobre el código actual | No hay lista de violaciones; grep de escrituras solo muestra el módulo invitaciones escribiendo su entidad (696882e) | No cumple | No se documenta recorrido de verificación, requisito para declarar lista vacía. |
| Plan de corrección por violación | No hay plan de corrección asociado a violaciones porque no hay lista (696882e) | No cumple | Cada violación debería tener acción concreta; no existe. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/08-conceptos-transversales.md está vacío en 696882e | No cumple | Faltan lenguaje ubicuo y mapa de contextos en sección 8. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | No se dispone del hash de S5 para comparar; docs/c4/nivel-3-componentes.md está vacío en 696882e | No verificado | No hay ADR de reajuste; sin hash de S5 no se puede confirmar si los límites cambiaron. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md solo tiene A-01 y no referencia contextos del mapa; no hay mapa (696882e) | No cumple | Los aspectos no se pueden relacionar con contextos inexistentes. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_EnAgenda visible y público; 3 cuentas en shortlog (696882e) | Cumple | Integrantes declarados coinciden en número con cuentas activas. |
| Estructura mínima | README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes en HEAD (696882e) | Cumple | Hay archivos __pycache__ versionados, pero no afecta la estructura mínima. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md con nombre válido y contenido completo (696882e) | Cumple | Un solo ADR; no se observan reescrituras. |
| La tabla de aspectos | docs/aspectos.md fila A-01 con enlaces a C4, ADR, código, pruebas y evidencia (696882e) | Cumple | Solo un aspecto; la fila es navegable. |
| Registro de uso de IA | docs/ia.md con entradas de agosto y septiembre, incluidos rechazos con motivo (696882e) | Cumple | El log muestra 3 commits, crece en el tiempo. |
| README | README.md describe qué es, arranque con un comando y pruebas (696882e) | Cumple | El comando usa backslash de Windows; en Linux requiere ajuste. |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta pytest; runs_ci 'CI' success (https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/34162828625); sin configuración de SonarCloud | No cumple | Falta análisis estático en SonarCloud exigido por el contrato. |
| Secretos | grep de secretos en 696882e solo muestra tokens de invitación; sin .env versionado | Cumple | No hay credenciales en el repositorio. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `696882ecb889c01bdc93170556c90044acf4fcff 2026-09-07T16:21:16-05:00 Update aspectos.md`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene base de invitaciones con pruebas y CI en verde, pero la documentación de arquitectura está incompleta: C4 nivel 3 vacío, arc42 sección 8 vacía, sin mapa de contextos ni tabla de datos.

Pendientes que siguen abiertos:
- C4 nivel 3 sin contenido
- arc42 sección 8 vacía
- Mapa de contextos y tabla módulo-datos ausentes
- SonarCloud no configurado

## Recuento y nota sugerida

0 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Criterio 7 de la ficha (C4 nivel 3 y ADR si límites cambiaron): falta hash de S5 para comparar.

## Hallazgos para la planilla

- No hay mapa de contextos ni tabla módulo-datos en la entrega S6.
- arc42 sección 8 y C4 nivel 3 están vacíos.
- No se documenta recorrido de verificación de violaciones.
- Falta SonarCloud en el pipeline.
- Archivos __pycache__ versionados en src/ y tests/.
- docs/correcciones.md referencia correcciones-feedback.md inexistente.
- Solo un aspecto en docs/aspectos.md para seis módulos declarados.
