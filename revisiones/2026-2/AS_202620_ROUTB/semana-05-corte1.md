# semana-05-corte1 · ROUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `83b8c5e` (2026-08-30T19:33:15-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta corte-1 sobre un commit anterior al cierre | hash_calificado 83b8c5e (2026-08-30T19:33:15-05:00); no se observa etiqueta corte-1 en la evidencia | No cumple | Etiqueta ausente; se revisó el último commit anterior al cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No disponible en el repositorio; requiere adjunto de Moodle | No verificado | No se puede comprobar desde el repositorio. |
| Impacto de la restricción localizado en requisitos, C4 y código | docs/arc42/11_riesgos_y_deuda_tecnica.md pendiente; sin ADR nuevo; commit 83b8c5e 'Semana 4' | No cumple | No hay diagnóstico del reto; se desconoce la restricción asignada. |
| Línea base medida y verificable antes del cambio | No se encontraron cifras con herramienta y procedimiento en el repositorio | No cumple | Falta línea base medible. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo docs/adr/0001-usar-monolito-modular.md (semana 3), no ligado al reto | No cumple | No hay ADR del reto. |
| Cambio implementado y ejecutable de extremo a extremo | diff_desde_cierre vacío; sin commits posteriores a la semana 4 | No cumple | No hay implementación del reto. |
| Límites declarados conservados tras el cambio | docs/c4/context.md existe; sin cambio del reto que verificar | No cumple | Sin cambio no hay conservación que comprobar. |
| Prueba que cubre el cambio, en verde en el pipeline | runs_ci success (Backend CI run 33344914286) pero solo backend/tests/test_registro.py | No cumple | La prueba existente no cubre el reto. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay medición con herramienta, carga y procedimiento | No cumple | Falta medición contra umbral. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md filas 1 y 3 con celdas vacías en ADR, Código y Pruebas | No cumple | La cadena no es navegable. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md última entrada 2026-08-30 (semana 4); sin entrada de semana 5 | No cumple | No hay registro de IA del corte. |
| Sustentación del reto | Sesión de sustentación; no verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo visible ISCOUTB/AS_202620_ROUTB; autores: MKeinerrr, diegobrr999-commits, juliandmanjarrez-tech, junior14700 | Cumple | 4 identidades consolidadas coinciden con los integrantes declarados. |
| Estructura mínima | arbol_head incluye README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md | Cumple | Estructura completa. |
| Versionado y estado calificado | hash_calificado 83b8c5e (2026-08-30T19:33:15-05:00); sin etiqueta corte-1 | No cumple | Etiqueta ausente; se revisó el último commit anterior al cierre. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md con nombre válido | Cumple | Un ADR; hay un error de formato en su tabla de trazabilidad. |
| Tabla de aspectos | docs/aspectos.md filas 1 y 3 con celdas vacías en ADR, Código y Pruebas | No cumple | Filas con huecos no defendibles. |
| Registro de uso de IA | docs/ia.md con entradas por semana y secciones de aceptado/rechazado; log con 4 commits | Cumple | Registro presente, aunque sin entrada de la semana 5. |
| README y reproducibilidad | README.md documenta instalación, arranque (uvicorn, flutter run) y pruebas (pytest) | Cumple | Comandos de arranque y prueba documentados. |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta pytest; runs_ci success; sin configuración de SonarCloud | No cumple | CI en verde, falta análisis estático en SonarCloud. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `83b8c5ec2e378713af04a8193dd0981de0032d48 2026-08-30T19:33:15-05:00 Semana 4`
- **Veredicto**: con pendientes
- Resumen: Proyecto con base arquitectónica (estructura, ADR 0001, CI en verde) pero sin respuesta al reto de línea base; la etiqueta corte-1 no existe y no hay cambios desde la semana 4.

Pendientes que siguen abiertos:
- Crear etiqueta corte-1
- Diagnóstico y línea base del reto
- ADR del reto
- Implementación y pruebas
- Medición contra umbral
- Completar arc42 secciones 7, 8 y 11
- Completar celdas vacías de docs/aspectos.md
- Configurar SonarCloud
- Registrar uso de IA de la semana 5

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- PDF de dos páginas (requiere adjunto de Moodle)
- Sustentación del reto (se resuelve en sesión)

## Hallazgos para la planilla

- No existe la etiqueta corte-1; el commit calificado es 83b8c5e (2026-08-30).
- No hay evidencia de diagnóstico, ADR, implementación, pruebas ni medición del reto.
- El repositorio no presenta cambios desde la semana 4 (commit 'Semana 4').
- docs/aspectos.md tiene filas con celdas vacías en ADR, Código y Pruebas.
- docs/ia.md no registra usos de IA de la semana 5.
- El pipeline CI está en verde pero solo cubre el flujo de registro.
- No hay configuración de SonarCloud.
- No se encontraron secretos en el repositorio.
