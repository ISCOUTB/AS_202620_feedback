# semana-05-corte1 · EnAgenda

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `1d01401` (2026-08-31T00:28:12-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | git tag --list sin corte-1; hash calificado 1d01401 (2026-08-31T00:28:12-05:00) | No cumple | Etiqueta ausente; se revisó el último commit anterior al cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Adjunto de Moodle no presente en el repositorio | No verificado | Requiere el PDF de dos páginas para verificar su contenido. |
| Impacto de la restricción localizado en requisitos, C4 y código | No se halló apartado de diagnóstico en docs/adr/ ni en documentos inspeccionados; docs/arc42/11 no disponible en la muestra | No verificado | Se desconoce la restricción asignada; falta el contenido de docs/arc42/11 y el PDF. |
| Línea base medida y verificable antes del cambio | Sin cifra con herramienta y procedimiento en los documentos disponibles | No verificado | Falta docs/arc42/11 y PDF para comprobar la medición inicial. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | ls docs/adr/ muestra solo 0001-usar-monolito-modular.md | No cumple | No hay ADR nuevo que registre alternativas, fuerzas, decisión y consecuencias del reto. |
| Cambio implementado y ejecutable de extremo a extremo | No hay commit que implemente un ADR del reto; README.md documenta arranque con 'python app\web.py' y 'pytest -q' | No cumple | El arranque de la línea base existe, pero no el cambio del reto. |
| Límites declarados conservados tras el cambio | Sin cambio del reto; docs/c4/nivel-2-contenedores.md declara API/Backend y BD ausentes en app/web.py y src/invitaciones/infraestructura/repositorio_memoria.py | No verificado | No verificable tras el cambio; además el C4 nivel 2 no refleja el código real. |
| Prueba que cubre el cambio, en verde en el pipeline | tests/test_invitaciones.py cubre invitaciones; runs CI success 33360647498, 33358856832, 33357478772 | No cumple | No hay prueba que cubra un cambio del reto. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay medición con herramienta, carga y procedimiento en el repo | No verificado | Falta PDF y docs/arc42/11 para contrastar con umbral. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md fila A-01: C4 sin enlace, Pruebas 'tests', Evidencia 'Pendiente' | No cumple | La fila no es navegable de punta a punta. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md entradas 29/08 y 30/08/2026 con aceptado/rechazado y verificación (pytest 6 passed, arranque Flask) | Cumple | Cumple con salidas rechazadas y motivo técnico. |
| Sustentación del reto | Sesión de sustentación, no verificable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_EnAgenda público; autores Daoisttl0FB3, Jein-12, eliabarnedocondef10-gif en shortlog | Cumple | Tres cuentas activas; nombres visibles no coinciden exactamente con los declarados. |
| Estructura mínima | Árbol HEAD incluye docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md | Cumple | Hay archivos __pycache__ versionados. |
| Estado del repositorio que se califica | Sin etiqueta corte-1; se revisó 1d01401 | No cumple | Etiqueta ausente; hash anotado. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md cumple nomenclatura; sin reescrituras | Cumple | No hay ADR del reto, pero eso es de la ficha. |
| Tabla de aspectos | docs/aspectos.md A-01 con celdas no navegables y Evidencia 'Pendiente' | No cumple | Cadena con huecos. |
| Registro de uso de IA | docs/ia.md con entradas de agosto y motivos de rechazo | Cumple | Evidencia de criterio. |
| README | README.md documenta qué es, arranque y pruebas | Cumple | Comando con backslash puede fallar en Linux. |
| Pipeline y análisis estático | .github/workflows/ci.yml presente; runs success; sin SonarCloud | No cumple | Falta análisis estático. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `1d014016fa875156d4d390bf0d1f164563b3d0ab 2026-08-31T00:28:12-05:00 Update documentation with recent project changes`
- **Veredicto**: con pendientes
- Resumen: Proyecto en etapa temprana con línea base documentada y CI en verde, pero sin respuesta al reto del corte 1 y con pendientes de coherencia en C4 y aspectos.

Pendientes que siguen abiertos:
- Etiqueta corte-1 ausente
- ADR del reto no creado
- Diagnóstico y medición no localizados
- Cadena de aspectos con huecos
- C4 nivel 2 desactualizado
- SonarCloud no configurado

## Recuento y nota sugerida

1 de 12 criterios Cumple.

## No verificado / pendientes

- PDF de dos páginas (adjunto Moodle no disponible).
- Impacto de la restricción (falta restricción asignada y docs/arc42/11).
- Línea base medida (falta docs/arc42/11 y PDF).
- Límites conservados tras el cambio (no hay cambio del reto).
- Resultado contrastado con umbral (falta PDF y sección 11).
- Sustentación del reto (sesión).

## Hallazgos para la planilla

- Etiqueta corte-1 ausente; se calificó 1d01401.
- No hay ADR del reto ni cambio implementado.
- Sin diagnóstico ni medición localizables en el repositorio.
- Fila A-01 de aspectos con huecos de navegación.
- C4 nivel 2 desactualizado respecto al código real.
- SonarCloud no configurado.
- Archivos __pycache__ versionados.
- Se desconoce la restricción asignada al equipo.
