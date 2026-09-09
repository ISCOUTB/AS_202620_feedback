# semana-05-corte1 · TAIA

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Estado revisado | `a3f4d82` (2026-09-06T04:13:11-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | Commit a3f4d82 (2026-09-06T04:13:11-05:00) en rama master, anterior al cierre 2026-09-07T05:00:00Z | Cumple | Hash calificado a3f4d82 identificado y fechado antes del cierre S5 |
| correcciones.md existe en la raíz del estado calificado | git ls-tree a3f4d82 incluye correcciones.md en la raíz | Cumple | correcciones.md existe en el hash calificado |
| Correcciones trazables y contrastadas | No se proporciona contenido de correcciones.md; sin evidencia del enlace a hallazgos S1-S4 | No verificado | No hay evidencia de que el archivo responda a hallazgos reales; solo se cita su existencia |
| S1 al día: equipo, problema y repositorio | docs/ficha_problema.md presente; README lista a los 4 integrantes (Valeria, Deiner, Luis, Mark) | Cumple | Problema y propuesta coherentes con la ficha del proyecto |
| S2 al día: escenarios de calidad y restricciones | docs/calidad/arbol_utilidad.md y escenarios_calidad.md con S1-S5; docs/arc42/arc42.md incluye restricciones técnicas, organizacionales y legales | Cumple | Escenarios de calidad presentes y priorizados |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001-estilo-arquitectonico.md documenta decisión de monolito modular hexagonal selectiva con contexto, alternativas y consecuencias | Cumple | ADR-0001 presente y detallado |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42.md, docs/c4/C4-C1.md, C4-C2.md; backend/app/modules/academic con dominio, aplicación y adaptadores | Cumple | El corte vertical implementa registro y consulta de tareas; documentación al día |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta endpoints y ejemplo curl; run CI 34024480875 success (2026-09-06T09:22:42Z) | Cumple | La estructura backend coincide con el C4 y ADR-0001 |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml ejecuta pytest backend/tests; run 34024480875 success asociado al estado calificado | Cumple | El pipeline CI pasó para commits cercanos al hash calificado; run asociado a 2026-09-06 |
| Trazabilidad consolidada navegable | docs/aspectos.md con fila A-01 y enlaces a C4, ADR, código y pruebas | Cumple | La tabla de aspectos tiene una fila completa para A-01 |
| PDF u otro adjunto exigido por el aula | El repositorio no contiene el PDF; adjunto solo entregado en Moodle, no disponible para revisión | No verificado | Se requiere acceso al aula o el enlace al PDF para verificar |
| Sustentación del corte | No hay evidencia de sesión de sustentación | No verificado | Lo resuelve el docente en la sesión |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura del repositorio | README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md presentes en a3f4d82 | Cumple | Estructura mínima del contrato cumplida |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md sigue convención de nombre y estructura; no hay ADR reescritos | Cumple | Un ADR presente, con contexto, decisión y trazabilidad |
| Trazabilidad de aspectos | docs/aspectos.md con fila A-01: aspecto, requisito RF-01/RF-02, C4-C1/C4-C2, ADR-0001, código, pruebas | Cumple | Una fila navegable para A-01 |
| Registro de uso de IA | docs/ia.md con entradas 001-006 e historial de commits que crece (76d4a91 a a3f4d82) | Cumple | Incluye aceptado, rechazado y verificación por cada entrada |
| README | README.md documenta qué es, requisitos, ejecución con run.bat y pruebas con pytest backend/tests | Cumple | Provee comando de arranque para Windows y comandos de prueba |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta pytest en cada push; runs CI 34024480875 y 34287877842 con conclusión success | Cumple | El pipeline corre en GitHub Actions; análisis estático SonarCloud no evidenciado en repositorio |
| Secretos | git grep sin coincidencias de patrones de secretos; sin archivos .env versionados | Cumple | No se encontraron secretos en HEAD |
| Autoría y colaboración | shortlog en a3f4d82 muestra 19 commits de val, 8 de dei0811, 3 de mark, 2 de val, 1 de luis20072002 | Cumple | No consolidable por identidades duplicadas (val aparece con dos correos); hay contribución de 4 personas |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `915e4996c5f252b0a35e6a0405935e665d2cfa66 2026-09-08T17:42:02-05:00 fix: harden dependency installation for SonarCloud`
- **Veredicto**: con pendientes
- Resumen: Estado calificado a3f4d82 anterior al cierre muestra proyecto TAIA con ficha de problema, escenarios de calidad, ADR, arc42, C4, aspectos y corte vertical funcional. Pipeline CI en verde para commits cercanos al hash calificado. Quedan pendientes: verificación del contenido de correcciones.md, adjunto PDF del aula y sustentación del corte.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 3cf6bfc y 915e499 (2026-09-08) corrigen pipeline de SonarCloud tras el cierre del 2026-09-07; no forman parte del estado calificado
- El diff desde cierre modifica .github/workflows/ci.yml y backend/requirements.txt para blindar la instalación de dependencias

Pendientes que siguen abiertos:
- Verificación del contenido de correcciones.md en estado calificado
- Evidencia del PDF u adjunto entregado en Moodle
- Sustentación del corte
- Consolidar identidades de git (val con dos correos)
- Análisis estático SonarCloud sin evidencia concreta

## Recuento y nota sugerida

9 de 12 criterios Cumple.

## No verificado / pendientes

- Correcciones trazables y contrastadas - falta contenido de correcciones.md
- PDF u otro adjunto exigido por el aula - falta acceso al adjunto
- Sustentación del corte - falta sesión

## Hallazgos para la planilla

- correcciones.md presente en hash calificado pero su contenido no fue verificado
- PDF del aula ausente en repositorio y no disponible para revisión
- Sustentación del corte sin evidencia
- Docs ia.md: entrada 006 inconclusa
- Identidad de val duplicada (dos correos)
- Análisis estático SonarCloud no evidenciado
- No hay commits de 4 integrantes en el hash calificado (val aparece con dos correos consolidados)
- Commits post cierre 3cf6bfc y 915e499 corrigen pipeline SonarCloud
- Commits posteriores al cierre (no calificados): 915e499 2026-09-08T17:42:02-05:00 fix: harden dependency installation for SonarCloud; 3cf6bfc 2026-09-08T17:34:01-05:00 fix: lock dependencies for SonarCloud security gate
