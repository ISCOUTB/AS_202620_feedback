# semana-04-evidencia-s4 · InvenTrack

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `d7ba824` (2026-08-30T23:39:33-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md (HEAD d7ba824): las secciones 1-4 y 10 están redactadas en un solo archivo; las secciones 5, 6, 9 no tienen encabezados propios redactados (el README dice que están 'marcadas como pendientes', líneas que se citan en el mismo arc42). En el hash calificado no hay secciones 5, 6, 9 redactadas. | No cumple | La instrucción pide secciones 1 a 6 redactadas; en el commit d7ba824 (2026-08-30T23:39:33-05:00) no hay evidencia de secciones 5 y 6; el propio arc42 dice 'Building Block View, Runtime View... están marcadas como pendientes'. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se encontró sección 9 (Decisiones) en docs/arc42/arc42-template-EN.md en el commit d7ba824; los ADR 0001 y 0002 no están citados en ninguna sección 9. | No cumple | La ficha pide que la sección 9 apunte a ADR existentes; al no estar redactada, no cumple. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/arc42-template-EN.md incluye sección 'Quality Requirements' con árbol de utilidad y escenarios ESC-01 a ESC-05; ver también docs/utility-tree.md en d7ba824. | Cumple | La sección 10 existe y está redactada con escenarios coherentes con la semana 2. |
| Glosario iniciado con términos del dominio | No se encontró sección 12 (Glosario) en docs/arc42/arc42-template-EN.md en d7ba824; el archivo no contiene un glosario con términos del dominio. | No cumple | La ficha pide glosario iniciado (sección 12); no aparece en el commit calificado. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/context.md (nivel 1) y docs/c4/containers.md (nivel 2) existen en d7ba824; los actores Dueño/Vendedor/Empleado y el sistema externo Notificaciones coinciden en ambos niveles. | Cumple | Coherentes; los actores y el flujo de notificación son consistentes. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/containers.md (d7ba824) declara un contenedor 'API Backend' que corresponde a app/ (carpeta completa); los módulos productos, proveedores, inventario, usuarios y alertas están bajo app/ en el árbol del commit. | Cumple | La correspondencia es correcta según el texto del propio archivo; no hay contenedores dibujados sin código. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | En d7ba824: interfaz: app/productos/infrastructure/router.py (endpoint HTTP); lógica: app/productos/application/crear_producto.py y eliminar_producto.py; persistencia: app/productos/infrastructure/in_memory_repository.py. | Cumple | El recorrido de creación/eliminación de producto atraviesa las tres capas; la persistencia es en memoria. |
| Arranque documentado con un solo comando | README.md (d7ba824) documenta el comando 'python -m uvicorn app.main:app --reload' en la sección de arranque y requisitos previos en el texto del README. | Cumple | El comando es único y está declarado. |
| Prueba automatizada del recorrido completo, en verde | No se encontró en el commit d7ba824 la prueba de recorrido completo; tests/productos/test_api_corte_vertical.py no aparece en el árbol del commit (solo tests/test_health.py). En runs_ci los runs visibles con éxito comienzan el 2026-09-07, posteriores al cierre y al commit calificado; no hay run de la semana anterior al cierre que ejecute la prueba. | No cumple | La prueba de corte vertical se agregó después del cierre (aparece en HEAD pero no en d7ba824); el pipeline en verde es posterior al cierre. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md (d7ba824) fila ASP-01: las columnas Pruebas y Evidencia dicen 'Pendiente'; no hay celdas que apunten a pruebas reales. | No cumple | La fila llega hasta ADR y código, pero Pruebas y Evidencia están pendientes; la ficha pide completa hasta la columna Pruebas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima del repositorio | En d7ba824 existen README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md. | Cumple | Hay una desviación: docs/adr contiene un archivo '0002-usar-monolito-modular-con-hexagonal-por-modulo' sin extensión .md (no sigue la convención de nombre). |
| Convenciones de ADR | docs/adr/ contiene '0002-usar-monolito-modular-con-hexagonal-por-modulo' sin extensión .md; además es duplicado del ADR-0001 con estado 'Aceptado' en lugar de un ADR propio (en d7ba824). | No cumple | El nombre del archivo ADR-0002 no cumple el patrón NNNN-titulo.md y parece un duplicado del 0001. |
| Tabla de aspectos trazable | docs/aspectos.md (d7ba824) fila ASP-01: columnas Pruebas y Evidencia en 'Pendiente'; el ADR citado no lleva a la implementación (el mecanismo de concurrencia no está decidido). | No cumple | La fila no se puede defender completa hasta la columna Pruebas en el estado calificado. |
| Registro de uso de IA | docs/ia.md contiene tabla con fecha, etapa, uso, rechazado y motivo para S1, S2, S3/S4; el log de commits del archivo muestra actividad. | Cumple | El registro incluye la columna de rechazos con motivos técnicos. |
| README con arranque de un solo comando y pruebas | README.md (d7ba824) declara el comando de arranque y sección de pruebas; el pipeline .github/workflows/test.yml ejecuta pytest. | Cumple | El comando está documentado; no se ejecutó en esta revisión. |
| Pipeline y análisis estático | Existe .github/workflows/test.yml en d7ba824; no se encontró configuración de SonarCloud en el commit calificado (sonar-project.properties solo aparece en HEAD). | No verificado | No hay evidencia de análisis estático en la semana 4; se necesitaría ver el archivo sonar-project.properties y un run de SonarCloud. |
| Secretos | Comando de búsqueda de secretos en HEAD no arroja coincidencias; no hay .env versionado en el árbol. | Cumple | No se hallaron credenciales en el estado revisado. |
| Autoría y colaboración | git shortlog en HEAD muestra 4 contribuyentes con actividad: Jose Vargas, Josephva24, Esteban Peluffo, Felix Taborda, FlexT21 y jxviercarta (consolidando identidades: Jose Vargas/Josephva24, Felix Taborda/FlexT21/negro, Esteban Peluffo, Javier Carta). | Cumple | Los cuatro integrantes declarados aparecen en el historial. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `ac951e3fc2acf849f2cc89ffb622d392b268672a 2026-09-08T10:11:58-05:00 Update and rename feedback.md to correcciones.md`
- **Veredicto**: con pendientes
- Resumen: En HEAD, el proyecto ha avanzado bastante: se agregaron las secciones de arc42 pendientes (5, 6, 9, 12), la lógica de inventario con concurrencia (ADR-0002), pruebas de recorrido completo y configuración de SonarCloud. Sin embargo, este avance ocurrió en commits posteriores al cierre de la semana 4 (por ejemplo, 2988b03, 7b0aad5, 81dc010, bcb133d), por lo que el estado calificado (d7ba824) no los incluye.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Secciones 5, 6 y glosario de arc42: se agregaron después del cierre (commits 22bd660, c870f2b y otros entre 2026-09-06 y 2026-09-08).
- Prueba de corte vertical: tests/productos/test_api_corte_vertical.py se agregó en HEAD pero no existe en d7ba824.
- Fila de aspectos con columna Pruebas completa: se resolvió en HEAD con la trazabilidad del corte 1 (commit bb4ef0c).
- SonarCloud: sonar-project.properties se agregó en HEAD, no en el commit calificado.

Pendientes que siguen abiertos:
- En HEAD aún no se verifica ejecución de SonarCloud en un run; no hay evidencia de análisis estático en los runs disponibles.

## Recuento y nota sugerida

5 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.0 = 1 + 4 × (5/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Criterio Transversal 'Pipeline y análisis estático': no se pudo comprobar porque no hay run de CI anterior o igual al cierre (2026-08-31T05:00:00Z) que ejecute la prueba de corte vertical, ni archivo sonar-project.properties en d7ba824; se necesitaría un run de Actions de la semana 4 y el archivo de configuración de SonarCloud.

## Hallazgos para la planilla

- arc42 secciones 5, 6 y 9 no redactadas en el commit calificado; el arc42 en d7ba824 las marca pendientes.
- Glosario (sección 12) ausente en d7ba824.
- docs/aspectos.md fila ASP-01 deja Pruebas y Evidencia en 'Pendiente'.
- La prueba de corte vertical (test_api_corte_vertical.py) no existe en el commit calificado; se agregó después del cierre.
- docs/adr/0002-usar-monolito-modular-con-hexagonal-por-modulo no sigue la convención de nombre y duplica al ADR-0001.
- Pipeline en verde solo se evidencia en runs posteriores al cierre; el commit d7ba824 no tiene run asociado en la ventana de la semana.
- No hay configuración de SonarCloud en el commit calificado (sonar-project.properties aparece solo en HEAD).
- Correcciones de semanas anteriores se hicieron después del cierre (commits post-cierre hasta 2026-09-08).
- Commits posteriores al cierre (no calificados): ac951e3 2026-09-08T10:11:58-05:00 Update and rename feedback.md to correcciones.md; c837d7d 2026-09-07T01:12:16-05:00 datalle; cf9d7d3 2026-09-07T00:59:16-05:00 docs: definir Flutter como frontend; 3defc32 2026-09-07T00:59:16-05:00 Pequenos detalles; 2988b03 2026-09-06T23:35:40-05:00 docs: remover marcadores de texto residuales en el README
