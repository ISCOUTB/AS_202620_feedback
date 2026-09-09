# semana-02-evidencia-s2 · EnAgenda

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `5b6f7a8` (2026-08-16T23:33:20-05:00) |
| Cierre | 2026-08-17T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | docs/arc42/01-introducción-y-objetivos .md no existe en el árbol calificado (5b6f7a8), solo aparece en árboles posteriores | No cumple | Falta el archivo 01* en el commit vigente al cierre. |
| arc42 sección 2 con restricciones clasificadas y justificadas | docs/arc42/02- restricciones .md lista R-01..R-06 con impacto arquitectónico | No cumple | Redactadas y justificadas, pero no se clasifican en técnicas, organizativas y legales. |
| Restricciones separadas de los requisitos | docs/arc42/02- restricciones .md y docs/ficha-problema .md; sección 2 no incluye funcionalidades como requisitos | Cumple | Las restricciones están separadas del alcance funcional descrito en la ficha de problema. |
| arc42 sección 3 con actores y sistemas externos | docs/arc42/03-contexto y alcance .md identifica organizador e invitado y declara que no hay sistemas externos obligatorios | Cumple | El contenido es coherente con el C4 de contexto aunque el archivo tenga espacios en el nombre. |
| Entre 3 y 5 escenarios de calidad redactados | docs/arc42/10-requisitos-de-calidad .md contiene EC-01 a EC-05 numerados | Cumple | Hay 5 escenarios, dentro del rango pedido. |
| Cada escenario con sus seis partes y medida numérica | EC-01..EC-05 en docs/arc42/10-requisitos-de-calidad .md; EC-05 mide 'percentil 95... menor de 2 segundos' y EC-01 '100 % de intentos... rechazado' | Cumple | Los cinco escenarios incluyen fuente, estímulo, artefacto, entorno, respuesta y medida numérica con unidad. |
| Árbol de utilidad que prioriza por impacto y riesgo | docs/arc42/10-requisitos-de-calidad .md muestra atributos etiquetados Alta/Media, sin columna de riesgo | No cumple | Hay impacto pero no nivel de riesgo ni una priorización explícita por impacto-riesgo. |
| C4 de contexto con leyenda y flechas etiquetadas | docs/c4/nivel-1-contexto .md es un diagrama mermaid C4Context con relaciones etiquetadas | Cumple | El diagrama define actores y sistema con flechas etiquetadas; no se aprecia leyenda separada. |
| Escenarios alcanzables desde la fila de su aspecto | docs/aspectos .md fila A-01 tiene 'Pendiente' en todas las columnas y no enlaza a ningún escenario | No cumple | No hay trazabilidad navegable desde la tabla de aspectos hasta los escenarios de calidad. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Sin dependencias ocultas | No se evidencian en el estado calificado 5b6f7a8 (sin archivo de dependencias formal; solo README) | No verificado | Faltaría declarar dependencias y cómo se instalan. |
| Sin secretos | git grep en HEAD no muestra credenciales; .env no está versionado | Cumple | No se encontraron secretos en el commit calificado. |
| Configuración correcta | No aparecen archivos de configuración en el árbol calificado | No verificado | Falta evidencia de configuración del sistema. |
| Historias de usuario trazables | No se encuentran archivos de historias en docs/ en el commit calificado | No cumple | Solo hay requisitos funcionales descritos en README y ficha-problema. |
| Ramas y tiempos | Commits posteriores al cierre 2026-08-17T05:00:00Z: 13fdc8e, 66fb6e4, 696882e, entre otros | No cumple | Existen commits tardíos que corrigen documentación de semanas anteriores; no se evidencia flujo de ramas. |
| Ejecución de pruebas | No hay .github/workflows/ci.yml en 5b6f7a8; runs_ci vacío | No cumple | Aunque existen tests locales, no hay evidencia de ejecución automatizada. |
| Integración continua | No hay workflow de CI en el estado calificado | No cumple | Sin pipeline, badge o run que demuestre integración continua. |
| Despliegue | No se observan archivos de despliegue ni URL en el estado calificado | No verificado | No hay evidencia de despliegue. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `696882ecb889c01bdc93170556c90044acf4fcff 2026-09-07T16:21:16-05:00 Update aspectos.md`
- **Veredicto**: con pendientes
- Resumen: A HEAD el proyecto incluye documentación arc42 considerable y código inicial de invitaciones, pero arrastra correcciones tardías de la semana 2 y no hay CI ni evidencias de ejecución.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 13fdc8e Cambios C4
- 66fb6e4 Cambios C4
- 1d01401 Update documentation with recent project changes
- 696882e Update aspectos.md

Pendientes que siguen abiertos:
- Falta docs/arc42/01*
- Trazabilidad de aspectos pendiente
- Sin integración continua

## Recuento y nota sugerida

5 de 9 criterios Cumple.

## No verificado / pendientes

- Sin dependencias ocultas: falta archivo de dependencias
- Configuración correcta: sin archivos de configuración visibles
- Despliegue: sin evidencia de despliegue

## Hallazgos para la planilla

- Falta docs/arc42/01* en el commit calificado
- Fila A-01 en docs/aspectos .md toda 'Pendiente', sin enlace a escenarios
- Árbol de utilidad sin nivel de riesgo ni priorización por riesgo
- Sección 2 sin clasificación técnicas/organizativas/legales
- Commits tardíos posteriores al cierre corrigen la entrega
- Sin CI en el estado calificado
- Rama principal sin evidencia de flujo de ramas
- Commits posteriores al cierre (no calificados): 696882e 2026-09-07T16:21:16-05:00 Update aspectos.md; 5a8a5c5 2026-09-07T16:17:20-05:00 Evidencias de corte vertical funcional; 1643eb7 2026-09-07T16:09:07-05:00 Merge branch 'master' of https://github.com/ISCOUTB/AS_202620_EnAgenda; 03c855c 2026-09-07T16:08:01-05:00 Cambios de aspectos; 942e112 2026-09-06T23:56:39-05:00 Fix formatting in ia.md documentation
