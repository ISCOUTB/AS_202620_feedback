# semana-04-evidencia-s4 · EnAgenda

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `df724b8` (2026-08-30T23:57:42-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/01-introducción-y-objetivos.md, 02- restricciones.md, 03-contexto y alcance.md, 04-estrategia-de-solución.md, 05-vista-de-bloques-de-construcción.md, 06-vista-de-ejecución.md en árbol df724b8; contenido verificado solo de 02 y 03 | No verificado | Falta contenido de 01, 04, 05 y 06 en la evidencia; no se pudo descartar texto de plantilla. |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09-decisiones-de-arquitectura.md cita ../adr/0001-usar-monolito-modular.md; ADR existe en docs/adr/0001-usar-monolito-modular.md | Cumple | Sección 9 resume ADR-0001 y enlaza correctamente. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10-requisitos-de-calidad.md con árbol de utilidad y escenarios EC-01 a EC-05; ADR-0001 referencia los mismos EC | Cumple | Coherencia verificada con ADR-0001. |
| Glosario iniciado con términos del dominio | docs/arc42/12-glosario.md define términos propios: EnAgenda, Invitación, Token, EstadoInvitacion, GestionarInvitacion, Repositorio en memoria, etc. | Cumple | Glosario específico del dominio, no genérico. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/nivel-1-contexto.md y docs/c4/nivel-2-contenedores.md; actores Organizador/Invitado aparecen en ambos niveles; diagramas en Mermaid (código) | Cumple | Coherencia de actores y sistema; diagramas como código. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | C4 nivel 2 dibuja Aplicación Web, Portal del Invitado, API/Backend y Base de Datos; código real: app/web.py, src/invitaciones/ (aplicacion, dominio, infraestructura), repositorio_memoria.py | No cumple | app/web.py y src/invitaciones/ corresponden a interfaz y lógica; pero 'Base de Datos' no tiene código (solo repositorio en memoria) y 'API/Backend' como contenedor separado contradice el ADR de monolito modular sin API pública. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md documenta flujo Interfaz web → GestionarInvitacion → Invitacion → RepositorioInvitacionesMemoria; rutas: app/web.py, src/invitaciones/aplicacion/gestionar_invitacion.py, src/invitaciones/dominio/invitaciones.py, src/invitaciones/infraestructura/repositorio_memoria.py | Cumple | Recorrido completo identificado en el árbol df724b8. |
| Arranque documentado con un solo comando | README.md secciones Requisitos, Instalación y 'Ejecutar la aplicación' con comando 'python app\web.py' | Cumple | No se ejecutó; comando declarado: python app/web.py. |
| Prueba automatizada del recorrido completo, en verde | tests/test_invitaciones.py; run CI 33358856832 success (2026-08-31T04:57:45Z) en https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/33358856832 | Cumple | CI ejecuta pytest -q y concluyó success en el commit calificado. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 con ID, Aspecto, Requisito, C4, ADR (docs/adr/0001-usar-monolito-modular.md), Código (src/invitaciones/), Pruebas (tests/) | Cumple | Celda C4 es descriptiva ('C4 nivel 1 y nivel 2 de EnAgenda') y no enlaza directamente a los diagramas; rutas de ADR, código y pruebas existen. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_EnAgenda visible; historial con 3 autores: Daoisttl0FB3, Jein-12, eliabarnedocondef10-gif | Cumple | Tres integrantes con actividad en el historial. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md presentes en árbol df724b8 | Cumple | Se versionan archivos .pyc en src/ y tests/ (basura); no afecta la estructura mínima. |
| Versionado y estado calificado | Commit calificado df724b8 2026-08-30T23:57:42-05:00 anterior al cierre; HEAD 1d01401 2026-08-31T00:28:12-05:00 posterior | Cumple | Hay un commit post-cierre (1d01401) que modifica docs/ia.md; la entrega se califica en df724b8. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md con nombre según convención, contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Un solo ADR, bien formado. |
| Tabla de aspectos navegable | docs/aspectos.md fila A-01; celda C4 dice 'C4 nivel 1 y nivel 2 de EnAgenda' sin ruta navegable | No cumple | La celda C4 no lleva a un archivo concreto; el contrato exige eslabones navegables. |
| Registro de uso de IA | docs/ia.md con entradas de 07-Ago, 08-Ago y 15-Ago; incluye qué se aceptó y qué se rechazó con motivo; log con commits 53df749 y 1d01401 | Cumple | Registro crece y documenta rechazos con justificación. |
| README | README.md describe el sistema, requisitos, instalación, arranque (python app\web.py) y pruebas (pytest -q) | Cumple | Documentación de arranque y prueba presente. |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta pytest; runs CI success; no hay configuración de SonarCloud en el árbol | No cumple | Falta el análisis estático en SonarCloud exigido por el contrato. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `1d014016fa875156d4d390bf0d1f164563b3d0ab 2026-08-31T00:28:12-05:00 Update documentation with recent project changes`
- **Veredicto**: con pendientes
- Resumen: Entrega S4 en df724b8 con 8/10 criterios de ficha cumplidos; C4 nivel 2 incoherente con el código y falta SonarCloud.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Commit 1d01401 (2026-08-31T00:28:12-05:00) actualiza docs/ia.md después del cierre.

Pendientes que siguen abiertos:
- Ajustar C4 nivel 2 para reflejar el monolito Flask y el repositorio en memoria.
- Agregar SonarCloud al pipeline.
- Hacer navegable la celda C4 de docs/aspectos.md.
- Verificar redacción de arc42 01, 04, 05 y 06.

## Recuento y nota sugerida

8 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.2 = 1 + 4 × (8/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 1, 4, 5 y 6: no se pudo comprobar su redacción ni descartar texto de plantilla; se necesita el contenido de docs/arc42/01-introducción-y-objetivos.md, 04-estrategia-de-solución.md, 05-vista-de-bloques-de-construcción.md y 06-vista-de-ejecución.md.
- Arranque de la aplicación: no se ejecutó; comando declarado en README: python app/web.py.

## Hallazgos para la planilla

- C4 nivel 2 dibuja API/Backend y Base de Datos que no corresponden al monolito Flask con repositorio en memoria.
- Archivos .pyc versionados en src/ y tests/.
- Commit post-cierre 1d01401 actualiza docs/ia.md después del cierre.
- Celda C4 de docs/aspectos.md no es navegable.
- Falta análisis estático SonarCloud.
- Contenido de arc42 01, 04, 05 y 06 no verificado en la evidencia.
- Nombre de archivo '02- restricciones.md' contiene un espacio inusual.
- Commits posteriores al cierre (no calificados): 1d01401 2026-08-31T00:28:12-05:00 Update documentation with recent project changes
