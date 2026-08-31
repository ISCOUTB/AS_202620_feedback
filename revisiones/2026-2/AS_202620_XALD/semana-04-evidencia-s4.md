# semana-04-evidencia-s4 · XALD

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `0205e44` (2026-08-30T23:12:03-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md existe con secciones 1 y 2 redactadas en español | No verificado | El extracto del archivo no muestra las secciones 3 a 6; se necesita inspeccionar el archivo completo |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/adr/0001-0006 existen | No verificado | La sección 9 no es visible en el extracto del arc42; no se pudo comprobar que cite los ADR |
| arc42 sección 10 coherente con los escenarios de la semana 2 | El arc42 menciona ESC-01 a ESC-05 en Quality Goals | No verificado | La sección 10 no es visible en el extracto; no se pudo verificar su contenido |
| Glosario iniciado con términos del dominio | docs/arc42/arc42-template-EN.md es el único archivo arc42 | No verificado | La sección 12 no es visible en el extracto; no se pudo comprobar el glosario |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/c1.md y docs/c4/c2.md con diagramas Mermaid, leyenda y flechas etiquetadas | Cumple | Actores externos (Usuario, Android/SMS, Gemini) y contenedores coherentes entre C1 y C2 |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Módulos :app, :parser, :corefinanciero, :syncqueue, :aigemini corresponden a directorios en XALDAPP/ | No cumple | El contenedor Backend XALD dibujado en C2 no tiene código en el repositorio |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md describe el flujo a través de los 5 módulos; Cortevertical.kt existe en XALDAPP/app/src/test/java/com/proyecto/xald/ | No verificado | No se pudo inspeccionar Cortevertical.kt para confirmar que invoca Coremanager.kt (persistencia) |
| Arranque documentado con un solo comando | README.md sección 'Comandos de Ejecución y Verificación' con requisitos (JDK 17, Android SDK) y comando .\XALDAPP\gradlew.bat -p XALDAPP test | Cumple | Hay variantes para entornos sin variables configuradas, pero el comando de arranque es único |
| Prueba automatizada del recorrido completo, en verde | XALDAPP/app/src/test/java/com/proyecto/xald/Cortevertical.kt; run Android CI 33352959352 success 2026-08-31T03:10:13Z ejecuta testDebugUnitTest | Cumple | El pipeline ejecutó la suite en verde antes del cierre |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 con enlaces a RT-04, C1, ESC-03, ADR-0002/0003, Parser.kt y README sección corte vertical | Cumple | Cada celda de la fila A-01 apunta a un archivo existente |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_XALD visible; 4 cuentas en shortlog coinciden con los integrantes declarados | Cumple | Nombre y organización correctos |
| Estructura mínima | docs/arc42/, docs/adr/ (6 ADR), docs/c4/, docs/aspectos.md, docs/ia.md y README.md presentes en HEAD | Cumple | El arc42 se entrega en un único archivo, permitido por la ficha |
| Versionado (commit vigente al cierre) | Commit 0205e44 fechado 2026-08-30T23:12:03-05:00 (04:12Z), anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin etiqueta, pero es evidencia semanal y no requiere tag |
| Convenciones de ADR | docs/adr/0001-0006 con nombres en kebab-case y contexto/decisión/consecuencias | No cumple | Carecen de opciones evaluadas (excepto 0006) y de trazabilidad a commits/pruebas exigida por el contrato |
| Tabla de aspectos | docs/aspectos.md con fila A-01 completa hasta Pruebas y enlaces verificados | Cumple | Incluye columna ESCENARIO adicional a las 8 del contrato; las filas A-02 a A-05 tienen Pendiente |
| Registro de uso de IA | docs/ia.md con tabla de contribuciones, decisiones y rechazos; 5 commits en su historial | Cumple | Incluye justificación de lo rechazado, como pide el contrato |
| README y reproducibilidad | README.md con descripción, requisitos previos y comando de arranque | Cumple | El comando de arranque ejecuta las pruebas del corte vertical |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta testDebugUnitTest con éxito (run 33352959352) | No cumple | No hay configuración ni runs de SonarCloud en el repositorio |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `0205e4407765ba9895025c332c5206815358ef7b 2026-08-30T23:12:03-05:00 Update ficha del problema.md`
- **Veredicto**: con pendientes
- Resumen: Entrega antes del cierre con C4 completo, CI en verde y aspectos con fila A-01 completa; quedan secciones arc42 sin verificar, un contenedor sin código y ADR sin trazabilidad.

Pendientes que siguen abiertos:
- Verificar secciones 3-6, 9, 10 y glosario del arc42
- Confirmar que Cortevertical.kt atraviesa persistencia
- Implementar o justificar Backend XALD
- Añadir SonarCloud al pipeline
- Completar ADR con opciones evaluadas y trazabilidad

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 3 a 6: el extracto del archivo no las muestra
- arc42 sección 9: no visible en el extracto
- arc42 sección 10: no visible en el extracto
- Glosario (sección 12): no visible en el extracto
- Corte vertical: no se pudo inspeccionar Cortevertical.kt para confirmar el tramo de persistencia

## Hallazgos para la planilla

- Backend XALD dibujado en C1/C2 sin código correspondiente en el repositorio
- ADR carecen de opciones evaluadas (excepto 0006) y de trazabilidad a commits/pruebas
- Sin configuración ni ejecución de SonarCloud en el pipeline
- README describe el corte vertical a través de 5 módulos pero la prueba solo menciona parser y DTO
- docs/aspectos.md incluye columna ESCENARIO adicional a las 8 del contrato
- El arc42 se entrega en un único archivo con nombre de plantilla; el extracto no permite verificar secciones 3-6, 9, 10 y glosario
