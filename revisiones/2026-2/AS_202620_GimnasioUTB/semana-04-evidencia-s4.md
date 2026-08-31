# semana-04-evidencia-s4 · GimnasioUTB

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `56db96b` (2026-08-30T22:33:47-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42_gimnasio_utb.md (56db96b) muestra secciones 1-3 redactadas; ADR 0001 referencia sección 4 | No verificado | El extracto del arc42 se corta en 3.2; no se pudo comprobar 4-6 ni ausencia de plantilla. |
| arc42 sección 9 al día y enlazada con los ADR existentes | No hay sección 9 visible en el extracto de docs/arc42/arc42_gimnasio_utb.md | No verificado | Falta el contenido de la sección 9 para verificar enlace a docs/adr/0001-arquitectura-hexagonal.md. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | ADR 0001 enlaza ES1-ES4 con anclas del arc42; ia.md semana 2 registra 5 escenarios | No verificado | No se ve la sección 10 en el extracto; la coherencia no se pudo comprobar directamente. |
| Glosario iniciado con términos del dominio | docs/ia.md semana 4 documenta creación de glosario con términos (aforo, estado operativo, registro de excepción) | No verificado | La sección 12 no aparece en el extracto del arc42; falta comprobarla en el documento. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/c4_level1.md y docs/c4/c4_level2.md (56db96b) con actores Estudiante/Encargado/FCM y contenedores App/API/BD | Cumple | Diagramas en Mermaid y PNG; flechas etiquetadas y actores del nivel 1 reaparecen en el 2. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | API Backend (Node/Express) corresponde a src/server.js y src/modules/aforo/; BD y App Móvil dibujadas sin código | Cumple | Correspondencia concreta: contenedor API con src/; App Móvil y BD aún sin implementación (solo .gitkeep). |
| Corte vertical que atraviesa interfaz, lógica y persistencia | src/modules/aforo/ solo contiene .gitkeep; package.json no define db:migrate ni dependencia pg; src/server.js solo expone /health | No cumple | El README describe POST /api/v1/aforo/acceso y GET /api/v1/aforo, pero no existen en el código. |
| Arranque documentado con un solo comando | README.md sección 'Corte Vertical Ejecutable' lista pasos (clone, install, .env, db:migrate, dev); package.json no tiene db:migrate | No cumple | No hay un único comando de arranque para el corte vertical; npm start solo levanta el esqueleto. |
| Prueba automatizada del recorrido completo, en verde | tests/health.test.js solo cubre GET /health; runs CI success ejecutan npm test (health) | No cumple | No existe prueba que ejercite registro de acceso y consulta de aforo de punta a punta. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila S1: Implementación cita AforoRepositoryPort (inexistente) y Pruebas cita script de 20 peticiones (inexistente) | No cumple | La fila existe pero las celdas de código y pruebas apuntan a artefactos que no están en el repositorio. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_GimnasioUTB público; shortlog: PedroPambi 43, RodrigoFacioLince 15, sebastian-caicedo 9 (consolidado) | Cumple | Los 3 integrantes declarados aparecen en el historial. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md presentes en HEAD | Cumple | arc42 en un solo archivo (permitido); C4 en .md y .png. |
| Estado calificado / versionado | Commit 56db96b (2026-08-30T22:33:47-05:00) anterior al cierre 2026-08-31T05:00:00Z; sin commits posteriores | Cumple | HEAD coincide con el estado calificado; diff_desde_cierre vacío. |
| Convenciones de ADR | docs/adr/0001-arquitectura-hexagonal.md tiene contexto, alternativas, decisión y consecuencias | No cumple | Falta trazabilidad a commit/PR que lo implementa y a pruebas que lo cubren, exigida por el contrato. |
| Tabla de aspectos | docs/aspectos.md fila S1 con columnas hasta Pruebas, pero celdas apuntan a AforoRepositoryPort y script de carga inexistentes | No cumple | Fila con huecos: no defendible según el contrato. |
| Registro de uso de IA | docs/ia.md con entradas por semana (herramienta, prompt, salida, verificación, aceptado/rechazado, motivo); 6 commits en su historial | Cumple | Incluye lo rechazado y el motivo, como pide el contrato. |
| README y reproducibilidad | README.md tiene 'npm install && npm start' pero la sección de corte vertical añade pasos manuales y npm run db:migrate inexistente | No cumple | El arranque del corte vertical no es reproducible con un solo comando. |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta npm test en push/PR; 10 runs success (p.ej. 33354233013) | No cumple | No hay configuración de SonarCloud (organización isco-utb) en el repositorio. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `56db96b05a003fd892c71a502a3ed4851cfc6784 2026-08-30T22:33:47-05:00 Fecha actualizada en semana 4`
- **Veredicto**: con pendientes
- Resumen: El repositorio tiene documentación arc42/C4/ADR/IA y un esqueleto backend con CI en verde, pero el corte vertical ejecutable no está implementado y varias trazabilidades apuntan a artefactos inexistentes.

Pendientes que siguen abiertos:
- Implementar corte vertical (interfaz HTTP, lógica de aplicación, persistencia PostgreSQL)
- Añadir prueba automatizada del recorrido completo (registro de acceso y consulta de aforo)
- Corregir README: un solo comando de arranque y scripts existentes en package.json
- Completar trazabilidad de docs/aspectos.md y ADR 0001 con rutas y commits reales
- Verificar y completar secciones 4-6, 9, 10 y 12 del arc42
- Configurar análisis estático con SonarCloud

## Recuento y nota sugerida

2 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.8 = 1 + 4 × (2/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 4-6, 9, 10 y 12: el contenido extraído de docs/arc42/arc42_gimnasio_utb.md está incompleto; se necesita el archivo completo o grep de encabezados.

## Hallazgos para la planilla

- El corte vertical descrito en el README no está implementado: src/modules/aforo solo tiene .gitkeep.
- package.json no define db:migrate ni dependencia pg, pero el README los menciona.
- La única prueba automatizada cubre /health, no el recorrido completo.
- La fila S1 de aspectos apunta a AforoRepositoryPort y a un script de carga inexistentes.
- El ADR 0001 no enlaza commit/PR que lo implementa ni pruebas.
- No hay configuración de SonarCloud en el repositorio.
- Los diagramas C4 están como código Mermaid y como PNG (trazabilidad positiva).
- El arc42 no se pudo verificar completo: el extracto se corta en la sección 3.2.
