# Retroalimentación publicable · ElMapita

## Semana 1

- Está bien: repositorio con el nombre correcto y público; estructura montada desde el inicio (arc42 con plantilla, adr, c4); `docs/aspectos.md` con la tabla de 8 columnas y el aspecto A-01 bien descrito.
- Falta: la ficha del problema (usuarios, alcance), las dos tensiones de calidad, y contenido en `docs/ia.md` (está vacío).
- Corregir antes del corte 1: crear la ficha, declarar las tensiones, llenar `docs/ia.md`, y que los tres integrantes firmen commits (el historial solo muestra una cuenta).

## Semana 2

- Está bien: secciones 1, 2 y 3 redactadas con cuidado (restricciones clasificadas y separadas de requisitos, interesados con preocupaciones); 4 escenarios con seis partes, medidas numéricas con carga y evidencia prevista de medición; árbol de utilidad con impacto/riesgo; enlaces desde `docs/aspectos.md` a los escenarios.
- Falta: `docs/ia.md` sigue vacío; el C4 solo existe como imagen y el enlace a `docs/c4/contexto.md` está roto; la ficha del problema y las tensiones siguen pendientes; en la semana solo hubo un commit de una persona.
- Corregir antes del corte 1: publicar el diagrama de contexto como código con leyenda, crear la ficha con las dos tensiones, llenar `docs/ia.md` y repartir la contribución entre los tres.

## Semana 3

Qué está bien: el ADR 0001 está completo (contexto ligado a EC-01…EC-04, alternativas con pros/contras, consecuencias con mitigaciones), el esqueleto BE/FE respeta el monolito modular y `./scripts/dev.sh` está documentado como arranque único.

Qué corregir antes del corte 1 (semana 5):
1. La sección 4 de arc42 está vacía (solo el encabezado): trasladen allí la estrategia con tácticas ligadas a los escenarios; que no viva solo en el ADR y la matriz.
2. La matriz comparativa (bien ponderada) debe comparar contra los escenarios EC-01…EC-04 del árbol de utilidad, no contra criterios propios.
3. Hagan alcanzable el ADR: la columna ADR de `docs/aspectos.md` sigue «Pendiente» y los escenarios no lo enlazan.
4. `docs/ia.md` sigue vacío: registren usos reales y rechazos con motivo.
5. Repartan la contribución: en S3 solo una cuenta firma commits; procuren que todos aparezcan en el historial.
6. Evidencien el verde de las pruebas existentes con un pipeline o capturas de ejecución.

## Semana 4 · S4

Buen avance en documentación: C4 niveles 1 y 2 completos y coherentes, corte vertical con interfaz, lógica y persistencia, y README con arranque por script. El pipeline de CI está en rojo y las pruebas del recorrido completo siguen pendientes: las rutas citadas en docs/aspectos.md no existen. Se recomienda crear una prueba e2e del flujo de mapas y dejarla en verde, configurar SonarCloud y revisar la distribución de commits para que el historial refleje participación del equipo. También conviene verificar que las secciones 4-6, 9, 10 y 12 de arc42 estén redactadas con contenido propio.
