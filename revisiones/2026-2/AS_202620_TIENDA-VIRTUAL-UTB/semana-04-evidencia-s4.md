# semana-04-evidencia-s4 · Tienda virtual UTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `d4b6e43` (2026-08-25T09:50:26-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md (hash d4b6e43) muestra secciones 1-4; contenido truncado antes de secciones 5 y 6 | No verificado | No se pudo comprobar secciones 5 y 6; haría falta ver archivo completo. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No se observa sección 9 en el contenido proporcionado de docs/arc42/arc42-template-EN.md | No verificado | Contenido truncado; no se puede confirmar presencia o ausencia. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No se observa sección 10 en el contenido proporcionado | No verificado | Contenido truncado; no se puede evaluar coherencia. |
| Glosario iniciado con términos del dominio | No se observa sección 12 en el contenido proporcionado | No verificado | Contenido truncado; no se puede confirmar glosario. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/context.md existe (nivel 1); no hay archivo de nivel 2 en docs/c4/ | No cumple | Falta diagrama C4 nivel 2. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | No existe C4 nivel 2; estructura de código solo tiene módulos vacíos (backend/app/modules/*/__init__.py) | No cumple | Sin nivel 2 no hay correspondencia que evaluar. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README indica 'En esta entrega no se incluye lógica de negocio'; backend/app/main.py solo define salud; módulos sin lógica | No cumple | No hay recorrido interfaz-lógica-persistencia. |
| Arranque documentado con un solo comando | README.md sección 'Arranque con un solo comando' declara requisito Docker y comando 'docker compose up --build' | Cumple | Cumple. |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_health.py y test_architecture.py no ejercitan recorrido completo; no hay prueba de corte vertical | No cumple | Falta prueba de punta a punta. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md solo tiene tabla inicial de 2 columnas y tensiones; no tiene las 8 columnas requeridas | No cumple | Falta tabla de trazabilidad completa. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo AS_202620_TIENDA-VIRTUAL-UTB, visible true, autores: RAZOR7150, Jasen Yukopila (mismo correo), pxtroniwnl, shalom-A26 = 4 integrantes | Cumple | Cumple. |
| Estructura mínima | Árbol incluye docs/arc42/, docs/adr/0001..., docs/c4/context.md, docs/aspectos.md, docs/ia.md, README.md | Cumple | Cumple. |
| Versionado (commit calificado) | No se evidencia etiqueta corte-1; hash calificado d4b6e43 (2026-08-25) | No cumple | Etiqueta ausente; se revisa último commit anterior al cierre. |
| Convenciones de ADR | docs/adr/0001-monolito-modular.md sigue nombre, pero carece de sección de trazabilidad (requisito/aspecto, C4, commit/PR, pruebas) | No cumple | Falta trazabilidad en ADR. |
| Tabla de aspectos | docs/aspectos.md no tiene las 8 columnas; solo tabla inicial de 2 columnas | No cumple | Falta estructura de trazabilidad. |
| Registro de uso de IA | docs/ia.md tiene tabla con fecha, herramienta, propósito, resultado, validación, pero no columna 'qué se rechazó y por qué' | No cumple | Falta registro de rechazos. |
| README | README.md incluye qué es, arranque con un solo comando, pruebas, requisitos | Cumple | Cumple. |
| Pipeline y análisis estático | .github/workflows/tests.yml ejecuta pytest, pero no hay configuración de SonarCloud ni análisis estático | No cumple | Falta SonarCloud. |

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 5 y 6: contenido truncado
- arc42 sección 9: contenido truncado
- arc42 sección 10: contenido truncado
- arc42 sección 12 (glosario): contenido truncado

## Hallazgos para la planilla

- Falta C4 nivel 2
- No hay corte vertical implementado
- Tabla de aspectos no tiene columnas requeridas
- ADR sin trazabilidad
- Registro de IA sin rechazos
- Pipeline sin SonarCloud
- No hay etiqueta corte-1
- Contenido de arc42 truncado en evidencia, secciones 5,6,9,10,12 no verificables
