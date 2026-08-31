# Retroalimentación publicable · InvenTrack

## Semana 1 · Equipo, problema y repositorio

Buen arranque: la ficha del problema está bien escrita, con usuarios y alcance claros, y el registro de IA ya nombra la herramienta y el uso concreto. El repositorio es público y correcto.

Para cerrar la semana: declaren en la ficha las dos tensiones de calidad enfrentadas (hoy solo está el aspecto de consistencia), conviertan `aspectos.md` a la tabla de ocho columnas del curso, y monten `docs/arc42/` con la plantilla más `docs/adr/` y `docs/c4/` (suban contenido o un `.gitkeep`, git no guarda carpetas vacías). Revisen también que los cuatro integrantes tengan acceso al repositorio: el historial de la semana solo muestra a una persona.

## Semana 2 · Escenarios de calidad y restricciones

Excelente semana: arc42 con secciones 1, 2, 3 y 10 completas, restricciones clasificadas por tipo y origen, cinco escenarios con sus seis partes y medidas verificables, árbol de utilidad con priorización por impacto y riesgo, y C4 de contexto como código con leyenda y flechas etiquetadas. De lo mejorcito del corte.

Solo dos detalles: (1) `docs/adr/README.md` no sigue la convención de nombres y hace fallar el filtro — sáquenlo o renómbrenlo; (2) conviertan `aspectos.md` a la tabla de ocho columnas (los enlaces a los escenarios ya están bien). Y por favor verifiquen que los cuatro integrantes estén empujando commits: uno de ustedes todavía no aparece en el historial.

## Semana 3

Qué está bien: entrega completa: ADR 0001 con contexto, alternativas y consecuencias, matriz comparativa por escenario, esqueleto modular con arranque documentado, enlaces del ADR desde `aspectos.md` y ESC-01, `docs/ia.md` al día y CI en verde.

Qué corregir antes del corte 1 (semana 5):
1. Ratifiquen el ADR 0001 como «aceptado» (hoy dice «propuesto, pendiente de ratificación») y ajusten el título para que enuncie la decisión.
2. Mantenimiento: conserven el pipeline en verde en cada entrega y sigan enlazando cada decisión desde su aspecto y su escenario.

## Semana 4 · S4

La entrega S4 se evaluó en d7ba824, dentro del plazo, pero el equipo siguió subiendo cambios hasta las 06:23Z. En el commit calificado faltan secciones 4, 5, 6 y 12 de arc42, la sección 9 no está redactada y la fila de aspectos deja Pruebas pendiente. El C4 nivel 2 dibuja Web y Base de datos sin código. El corte vertical de productos y su prueba en verde son el punto fuerte. Se recomienda completar arc42 dentro del horario de la entrega, corregir el ADR-0002 duplicado y añadir evidencia de SonarCloud. Para el primer corte, mantengan los diagramas como código y enlacen cada ADR con su commit de implementación.
