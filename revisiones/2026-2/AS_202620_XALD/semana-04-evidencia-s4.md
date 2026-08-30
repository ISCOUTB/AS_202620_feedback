# semana-04-evidencia-s4 · XALD

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `6985f5b` (2026-08-29T22:36:55-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md presente pero contenido truncado en la evidencia | No verificado | No se pudo comprobar secciones 3-6; solo se observan 1 y 2 en el extracto. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No visible en el extracto de arc42-template-EN.md | No verificado | Se requiere inspeccionar el archivo completo. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No visible en el extracto | No verificado | Se requiere verificar la sección 10 y su correspondencia con escenarios. |
| Glosario iniciado con términos del dominio | No visible sección 12 | No verificado | Se requiere confirmar presencia de glosario con términos propios. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/c4.md solo contiene diagrama C1; menciona C2 pero no lo dibuja | No cumple | Falta el diagrama de nivel 2. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No hay C4 nivel 2 para contrastar | No cumple | Sin nivel 2 no se puede verificar correspondencia. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Existen módulos app, corefinanciero, parser, syncqueue, aigemini y test Cortevertical.kt, pero sin contenido | No verificado | No se pudo inspeccionar el código para confirmar las tres capas. |
| Arranque documentado con un solo comando | README.md incluye comando PowerShell con variables de entorno y requisitos previos | Cumple | Comando declarado: $env:JAVA_HOME=...; $env:ANDROID_HOME=...; .\XALDAPP\gradlew.bat -p XALDAPP test |
| Prueba automatizada del recorrido completo, en verde | .github/workflows/ci.yml ejecuta ./gradlew testDebugUnitTest, pero no hay URL de run | No verificado | Se requiere evidencia de ejecución en verde. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md tiene columnas CÓDIGO, PRUEBAS, EVIDENCIA con '*Pendiente*' en todas las filas | No cumple | Ninguna fila está completa. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_XALD público; autores listados coinciden con 4 integrantes | Cumple | Sin observaciones |
| Estructura mínima | docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Sin observaciones |
| Estado del repositorio calificado | hash 6985f5b fecha 2026-08-29T22:36:55-05:00 anterior al cierre; no se listan tags | No verificado | No se pudo comprobar existencia de etiqueta corte-1 |
| Convenciones de ADR | ADRs 0001-0005 carecen de sección 'Opciones evaluadas' y trazabilidad explícita | No cumple | ADR-0006 sí las incluye; los demás no cumplen el formato completo. |
| Tabla de aspectos | docs/aspectos.md con celdas CÓDIGO, PRUEBAS, EVIDENCIA en 'Pendiente' | No cumple | Filas con huecos no defendibles. |
| Registro de uso de IA | docs/ia.md con tabla que incluye qué se rechazó y por qué | Cumple | Sin observaciones |
| README | README.md describe sistema, requisitos y comando único | Cumple | Sin observaciones |
| Pipeline y análisis estático | .github/workflows/ci.yml solo ejecuta pruebas, sin paso de SonarCloud | No cumple | Falta análisis estático requerido. |

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 3-6, 9, 10, 12: archivo truncado en evidencia
- Corte vertical: no se inspeccionó código de MainActivity, Coremanager, persistencia
- Prueba automatizada en verde: falta URL de run de CI
- Etiqueta de versionado: no se listaron tags del repositorio

## Hallazgos para la planilla

- C4 nivel 2 ausente en docs/c4/c4.md
- Tabla de aspectos incompleta: columnas Código, Pruebas y Evidencia en Pendiente
- ADRs 0001-0005 no incluyen opciones evaluadas ni trazabilidad
- Pipeline CI sin análisis estático SonarCloud
- No se pudo verificar contenido completo de arc42 (secciones 3-6, 9, 10, 12)
- No se pudo verificar corte vertical ni prueba en verde por falta de contenido de código y runs
