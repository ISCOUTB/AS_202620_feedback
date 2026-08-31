# semana-04-evidencia-s4 · LaPlacita

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | `745e799` (2026-08-30T21:52:41-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/arc42/arc42-template-EN.md: secciones 1-4 visibles y redactadas; el extracto se corta en la sección 4.4 | No verificado | No se pudo inspeccionar 5-6; README las declara completadas pero no sustituye la revisión del contenido |
| arc42 sección 9 al día y enlazada con los ADR existentes | docs/arc42/arc42-template-EN.md (sección 9 no visible en el extracto) | No verificado | Se requiere leer la sección 9 en el archivo completo para confirmar enlaces a docs/adr/ |
| arc42 sección 10 coherente con los escenarios de la semana 2 | docs/arc42/arc42-template-EN.md (sección 10 no visible en el extracto) | No verificado | Se requiere comparar la sección 10 con los escenarios ESC-01..05 |
| Glosario iniciado con términos del dominio | docs/arc42/arc42-template-EN.md (sección 12 no visible en el extracto) | No verificado | README menciona glosario inicial; falta verificar que contenga términos propios del dominio |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/c4/contexto.md y docs/c4/contenedores.md (Mermaid); actores Usuario/Establecimiento y externos Pasarela/Push coinciden en ambos niveles | Cumple | Diagramas como código con leyenda y flechas etiquetadas |
| Límites del C4 nivel 2 correspondientes a la estructura del código | docs/c4/contenedores.md dibuja App/Web Cliente, Portal Establecimiento, Redis y PostgreSQL; el árbol solo tiene app/health/route.js y src/modules/* | No cumple | Solo API Backend Central tiene correspondencia (app/ y src/); contenedores sin código: App/Web Cliente, Portal, Redis, PostgreSQL |
| Corte vertical que atraviesa interfaz, lógica y persistencia | src/corte-vertical.js y src/modules/* existen; contenido no disponible en el extracto | No verificado | README describe flujo catálogo→pedidos→pagos→entrega→notificaciones; falta confirmar persistencia real (no se ve BD en el árbol) |
| Arranque documentado con un solo comando | README.md sección 'Cómo ejecutar': requisito Node.js 22+, `npm install` y `npm run dev` | Cumple | npm install es preparación; el arranque es `npm run dev` |
| Prueba automatizada del recorrido completo, en verde | tests/corte-vertical.test.js; run CI success 2026-08-31T02:52:55Z https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/33352046552 | Cumple | Pipeline .github/workflows/ci.yml ejecuta `npm test` en Node 22 |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01: enlaza RF-01, ESC-01, c4/contexto.md, c4/contenedores.md, adr/0001 y 0003, src/modules/pedidos/index.js, tests/modulos.test.js y tests/corte-vertical.test.js | Cumple | Rutas verificadas en el árbol; celda Evidencia queda 'Pendiente' (no exigida esta semana) |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_LaPlacita visible; shortlog: Jorge M. Castillo 57, samulssl 22, Isaza927 23, matbuendia 7 (identidades consolidadas) | Cumple | 4 integrantes declarados presentes en el historial |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md en el árbol | Cumple | arc42 en un solo archivo (arc42-template-EN.md), permitido por la ficha |
| Versionado / estado calificado | Commit 745e799 2026-08-30T21:52:41-05:00 anterior al cierre 2026-08-31T05:00:00Z | Cumple | Sin etiqueta, pero las evidencias semanales se califican en el commit vigente al cierre |
| Convenciones de ADR | docs/adr/0001, 0002, 0003 con nombres NNNN-kebab-case; cada uno con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | ADR-0001 'propuesto' y ADR-0002 lo ratifica; ADR-0003 deja Dockerfile y sonar-project.properties pendientes |
| Tabla de aspectos | docs/aspectos.md con 6 filas (A-01..A-06); A-01 completa hasta Pruebas con rutas existentes | Cumple | A-02..A-06 tienen celdas 'Pendiente', aceptable para la semana 4 que exige una fila |
| Registro de uso de IA | docs/ia.md tabla con Fecha, Herramienta, Propósito, Prompt, Resultado, Validación; sin columna de 'qué se rechazó y por qué' | No cumple | El contrato exige registrar lo rechazado con motivo técnico; no aparece en el extracto |
| README | README.md con descripción, estructura, cómo ejecutar (Node 22+, npm install, npm run dev) y estado del proyecto | Cumple | Incluye enlaces a documentación y sección de pruebas |
| Pipeline, secretos y autoría | .github/workflows/ci.yml ejecuta npm test; runs success; sin secretos ni .env; 4 autores en historial | Cumple | SonarCloud pendiente (ADR-0003); pipeline no bloquea aún, pero no se exige hasta segundo corte |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `745e7998f189857a5fe3fee644dcb9f438161c0d 2026-08-30T21:52:41-05:00 Cambios de redacción dentro de la informació en el README, escritura del adr-0003 y los subtitulos del 6 - 9 del Arc42`
- **Veredicto**: al dia
- Resumen: Proyecto con C4 niveles 1-2 en código, corte vertical con CI verde y trazabilidad A-01; persisten contenedores dibujados sin implementar y registro IA incompleto

Pendientes que siguen abiertos:
- Contenedores C4 sin código
- docs/ia.md sin columna de rechazo
- Trazabilidad ADR-0001/0003 pendiente
- Verificación de secciones arc42 5-12

## Recuento y nota sugerida

4 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 5-6, 9, 10 y 12: requiere inspeccionar docs/arc42/arc42-template-EN.md completo
- Corte vertical: requiere leer src/corte-vertical.js y src/modules/* para confirmar interfaz, lógica y persistencia

## Hallazgos para la planilla

- C4 nivel 2 dibuja contenedores (Redis, PostgreSQL, App/Web Cliente, Portal) sin código en el repositorio
- docs/ia.md no registra lo rechazado con motivo, como exige el contrato
- Secciones 5, 6, 9, 10 y 12 de arc42 no pudieron inspeccionarse en el extracto
- ADR-0001 y ADR-0003 dejan trazabilidad pendiente (commit, Dockerfile, sonar-project.properties)
- CI en verde para el commit calificado (run 33352046552)
