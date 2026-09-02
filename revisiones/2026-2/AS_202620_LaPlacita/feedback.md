# Retroalimentación publicable · LaPlacita

## Semana 1 · Equipo, problema y repositorio

Muy buen montaje: estructura completa desde el primer día, ficha del problema clara con usuarios y alcance, tabla de aspectos con seis filas y una bitácora de IA con herramienta, prompt y validación. Los cuatro integrantes ya aparecen en el historial, que es lo ideal.

Solo dos ajustes: declaren en la ficha las dos tensiones de calidad enfrentadas (hoy tienen criterios de éxito, que no es lo mismo), y en la bitácora de IA añadan por cada uso qué se rechazó y por qué, que es la columna que más se valora.

## Semana 2 · Escenarios de calidad y restricciones

Buen contenido: arc42 con secciones 1, 2, 3 y 10 redactadas, cinco escenarios con medidas numéricas, árbol de utilidad con prioridades y un C4 de contexto como código con flechas etiquetadas.

Antes del corte 1 conviene: (1) completar las seis partes de cada escenario — les falta el «artefacto» en los cinco; (2) añadir la leyenda al diagrama C4 y guardarlo en `docs/c4/`; (3) restaurar en `aspectos.md` los enlaces a los escenarios (existieron y se retiraron en un commit posterior); (4) sacar de las restricciones las dos que están marcadas como funcionales — son requisitos; y (5) cuantificar la condición de carga de las medidas (hoy dice «cantidad elevada de usuarios»).

## Semana 3

Qué está bien: sección 4 con matriz comparativa por escenario, ADR 0001 con alternativas descartadas y trazabilidad, esqueleto de módulos por dominio y enlaces del ADR desde `aspectos.md` y desde cada escenario.

Qué corregir antes del corte 1 (semana 5):
1. Ratifiquen el ADR 0001 como «aceptado» (hoy dice «propuesto»).
2. Monten el pipeline en `.github/workflows/` para que la prueba en verde deje de descansar solo en la declaración de `docs/ia.md`.
3. Enlacen la columna Requisito (RF-xx) de `docs/aspectos.md` a los escenarios correspondientes.

## Semana 4 · S4

Buen avance: C4 como código, corte vertical con pruebas en CI verde y trazabilidad A-01 completa. Para el primer corte, alineen los contenedores del diagrama con lo implementado (Redis, PostgreSQL, App/Web Cliente y Portal aún no existen en el repo) y completen docs/ia.md con lo rechazado y su motivo. Revisen que los ADR pendientes enlacen el commit que los implementa. Las secciones 5-12 de arc42 no se pudieron verificar en esta revisión; asegúrense de que estén redactadas sin texto de plantilla.

## Semana 5 · CORTE1

El repositorio tiene una base sólida: estructura completa, CI en verde y README reproducible. Para el corte 1 falta lo esencial del reto: crear la etiqueta `corte-1`, declarar la restricción asignada y registrar el diagnóstico, la decisión y la medición. Completen la tabla de aspectos (celdas Pendiente), documenten en docs/ia.md qué salidas de IA rechazaron y por qué, y concreten SonarCloud. Sin esos elementos, la trazabilidad no se puede defender. El PDF de dos páginas debe entregarse en Moodle con los enlaces de trazabilidad.
