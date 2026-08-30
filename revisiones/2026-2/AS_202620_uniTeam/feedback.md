# Retroalimentación publicable · uniTeam

## Semanas 1 y 2

## Evidencia S1

Bien: repositorio con el nombre de la convención, ficha del problema con usuarios y alcance, plantilla arc42 descomprimida, `docs/adr/` y `docs/c4/` creados, y registro de IA iniciado.

Corregir: la ficha del problema debe declarar las dos tensiones de calidad enfrentadas (dos atributos en conflicto); `docs/aspectos.md` debe ser la tabla de ocho columnas del curso con al menos una fila con ID y aspecto; y en `docs/ia.md` conviene registrar entradas por uso y qué se rechazó y por qué. Confirmen también que todos los integrantes tienen acceso al repositorio y hagan que cada uno firme commits con su propia cuenta.

## Evidencia S2

Bien: secciones 1, 2 y 3 del arc42 redactadas y coherentes, restricciones clasificadas (técnicas, organizativas, legales) y justificadas, cinco escenarios con sus seis partes y medida numérica —y además con método de verificación—, árbol de utilidad priorizado con justificación, C4 de contexto como código con leyenda y flechas etiquetadas, y aspectos enlazados a sus escenarios. Nivel sobresaliente.

Corregir antes del corte 1: renombrar el ADR a la convención `NNNN-titulo-en-kebab-case.md` (sin el prefijo «ADR-»), asegurar que los cuatro integrantes aparezcan en el historial de commits, y revisar que el historial del repositorio no conserve archivos de un proyecto anterior.

## Semana 3

Qué está bien: la sección 4 de arc42 trae tácticas por escenario, la matriz compara los tres estilos contra sus propios escenarios, el ADR-003 justifica la decisión con alternativas descartadas y la estructura de paquetes es coherente con el estilo elegido.

Qué corregir antes del corte 1 (semana 5):
1. Renombrar los ADR a la convención `NNNN-titulo-en-kebab-case.md` (quitar «ADR-» y el « (1)») y marcar ADR-001 como reemplazado por ADR-002.
2. Enlazar el ADR-003 desde `docs/aspectos.md` y desde el escenario que lo motiva.
3. Documentar en el README el comando único de arranque de la app (hoy solo está el de la prueba) y corregir el paquete `httpx2` de `requirements.txt`.
4. Registrar en `docs/ia.md` el uso de IA de esta semana con lo rechazado y su motivo.
5. Contribución: solo una persona firmó los commits de esta semana; todos los integrantes deben aparecer en el historial antes del corte 1.

## Semana 4 · S4

El repositorio muestra avances sólidos en estructura, corte vertical y documentación base. Se recomienda incluir en la evidencia los contenidos de las secciones 9, 10 y 12 de arc42 y los diagramas C4 para poder verificar su coherencia. También es necesario adjuntar la URL de un run de CI en verde que ejecute la prueba del corte vertical, y configurar SonarCloud para cumplir el criterio de pipeline. La tabla de aspectos y el README están bien logrados.
