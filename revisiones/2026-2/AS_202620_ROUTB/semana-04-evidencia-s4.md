# semana-04-evidencia-s4 · ROUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado revisado | `83b8c5e` (2026-08-30T19:33:15-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/01_introduccion_y_objetivos.md a 06_vista_de_ejecucion.md con contenido propio de ROUTB; 05 descompone en bloques con responsabilidades; 06 describe escenarios de registro y login con diagramas | Cumple | Sin rastros de plantilla en 1-6; secciones 7, 8 y 11 quedan pendientes (no exigidas esta semana) |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/09_decisiones_arquitectonicas.md con tabla que enlaza a docs/adr/0001-usar-monolito-modular.md | Cumple | Un solo ADR hasta ahora; la sección lo referencia correctamente |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/10_requisitos_de_calidad.md con árbol de utilidad y 5 escenarios (rendimiento, usabilidad, seguridad, disponibilidad, escalabilidad) | Cumple | Coherente con los objetivos de calidad de la sección 1.4 |
| Glosario iniciado con términos del dominio | docs/arc42/12_glosario.md con 8 términos propios del dominio (conductor, pasajero, viaje, cupo, reserva, etc.) | Cumple | Términos del dominio ROUTB, no genéricos de arquitectura |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/context.md contiene Nivel 1 y Nivel 2 en Mermaid; actores y externos coinciden entre niveles; flechas etiquetadas y leyenda | Cumple | Diagramas como código (Mermaid), positivo para trazabilidad del corte |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Contenedor API Backend corresponde a backend/app/; módulos auth, users, trips, requests, notifications, admin, shared existen en backend/app/modules/; frontend/ para la app Flutter | Cumple | No hay contenedor dibujado sin código; servicios externos son dependencias, no código propio |
| Corte vertical que atraviesa interfaz, lógica y persistencia | Interfaz: frontend/lib/features/auth/screens/register_screen.dart y frontend/lib/features/users/services/user_service.dart; lógica: backend/app/modules/users/{router,service,schemas}.py; persistencia: backend/app/modules/users/models.py y backend/app/core/database.py | Cumple | Recorrido de registro completo identificable en el código |
| Arranque documentado con un solo comando | README.md sección Ejecución: 'uvicorn app.main:app --reload' (backend) y 'flutter run' (frontend), con requisitos previos de instalación | Cumple | Documentado por lectura; no se ejecutó localmente, CI valida backend (run 33344914286) |
| Prueba automatizada del recorrido completo, en verde | backend/tests/test_registro.py; run Backend CI 33344914286 success (https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/33344914286) | Cumple | El README cita además el run 33334594339; ambos en verde |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila 2 (Organización del backend) con ID, aspecto, requisito, C4, ADR, Código y Pruebas; rutas existentes | Cumple | Filas 1 y 3 tienen huecos en ADR/Código/Pruebas, pero la semana exige al menos una fila completa |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_ROUTB visible; shortlog HEAD: MKeinerrr, diegobrr999-commits, juliandmanjarrez-tech, junior14700 (MKeinerrr consolida dos correos) | Cumple | Los 4 integrantes declarados aparecen en el historial |
| Estructura mínima | docs/arc42/ (12 secciones), docs/adr/0001-*.md, docs/c4/context.md, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Estructura coincide con la mínima del contrato |
| Estado calificado / versionado | Commit calificado 83b8c5e (2026-08-30T19:33:15-05:00) anterior al cierre 2026-08-31T05:00:00Z; sin commits posteriores al cierre | Cumple | Sin etiqueta, pero es evidencia semanal; el commit vigente al cierre es el correcto |
| Convenciones ADR | docs/adr/0001-usar-monolito-modular.md con nombre según convención, contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Un solo ADR; no se observan reescrituras posteriores |
| Tabla de aspectos | docs/aspectos.md con 8 columnas; fila 2 completa y navegable hasta Pruebas | Cumple | Filas 1 y 3 con celdas vacías; la exigencia semanal de una fila completa se cumple |
| Registro de uso de IA | docs/ia.md con registro por semana (1-4), herramienta, contexto, aceptado, rechazado y justificación; log con commits 90f5542, b9b4ee8, 1ed002b, d9f67e4 | Cumple | Incluye lo rechazado con motivo técnico, como pide el contrato |
| README y reproducibilidad | README.md con descripción, equipo, tecnologías, instalación, ejecución (comandos únicos) y pruebas | Cumple | Documenta arranque de backend y frontend; no se ejecutó localmente |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta pytest en push/PR; runs_ci success (p.ej. 33344914286); sin archivos ni runs de SonarCloud | No cumple | Falta el análisis estático en SonarCloud exigido por el contrato |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `83b8c5ec2e378713af04a8193dd0981de0032d48 2026-08-30T19:33:15-05:00 Semana 4`
- **Veredicto**: al dia
- Resumen: Entrega S4 cumple 10/10 criterios de la ficha; transversal 7/8 (falta SonarCloud); sin commits posteriores al cierre

Pendientes que siguen abiertos:
- Completar arc42 secciones 7, 8 y 11
- Completar filas 1 y 3 de docs/aspectos.md
- Integrar SonarCloud al pipeline
- Enlazar ADR 0001 con commit de implementación
- Registrar medición de línea base

## Recuento y nota sugerida

10 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 5.0 = 1 + 4 × (10/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución local del arranque (backend y frontend) no realizada; verificado por lectura del README y CI del backend
- Análisis estático SonarCloud: no se pudo comprobar porque no hay configuración ni runs; haría falta sonar-project.properties o un run de SonarCloud (se evalúa como No cumple en la transversal)

## Hallazgos para la planilla

- Secciones 7, 8 y 11 de arc42 siguen como plantilla pendiente (fuera del alcance de la semana 4)
- docs/aspectos.md filas 1 y 3 tienen celdas vacías en ADR, Código y Pruebas
- Sin evidencia de SonarCloud en el repositorio ni en los runs de CI
- El ADR 0001 no enlaza un commit de implementación específico (pendiente para el corte)
- Sin medición de línea base registrada (pendiente para el corte)
- Diagramas C4 como código Mermaid, favorable para la trazabilidad del corte
