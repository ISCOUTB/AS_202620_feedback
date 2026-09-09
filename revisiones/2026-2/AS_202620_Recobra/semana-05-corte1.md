# semana-05-corte1 · Recobra

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `6ee5b66` (2026-09-05T20:26:56-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama master; hash 6ee5b66, 2026-09-05T20:26:56-05:00 < cierre 2026-09-07T05:00:00Z | Cumple | Último commit en master antes del cierre correctamente identificado. |
| correcciones.md existe en la raíz del estado calificado | Árbol de 6ee5b66 no incluye correcciones.md; git show 6ee5b66:correcciones.md no disponible | No cumple | Falta el archivo exigido en la raíz del commit calificado. |
| Correcciones trazables y contrastadas | Sin correcciones.md en 6ee5b66 no hay índice trazable de correcciones S1-S4 | No cumple | No es posible contrastar afirmaciones porque el archivo índice no existe. |
| S1 al día: equipo, problema y repositorio | README.md:5-28; docs/Restricciones_justificadas.md:1-37; docs/escenarios_calidad.md:1-13 | Cumple | Equipo, problema y repositorio coherentes en el estado calificado. |
| S2 al día: escenarios de calidad y restricciones | docs/escenarios_calidad.md:1-13; docs/Restricciones_justificadas.md:1-37; docs/arbol_utilidad.md:1-53 | Cumple | Escenarios medibles y restricciones justificadas presentes. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0002-arquitectura-y-stack.md:1-148 Aceptada; docs/arc42/04-estrategia-solucion.md:1-38 decisión hexagonal | Cumple | ADR-0002 y ADR-0003 documentan la decisión; ADR-0001 reemplazada. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42.md:1-89; docs/c4/README.md:1-67 diagramas C4; README.md:69-104 rutas del corte vertical | Cumple | arc42 y C4 presentes; corte vertical backend y cliente Flutter documentados. |
| Corte vertical reproducible y coherente con la arquitectura | README.md:46-77 comandos npm install/start/test, endpoints POST/GET; src/domain/entities/publicacion.ts; src/application/use-cases/crear-publicacion.ts; mobile/lib/main.dart | Cumple | Estructura hexagonal visible en código y comandos para arrancar/probar. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml:1-25; runs_ci success 2026-09-05T18:21:52Z y 2026-09-05T18:08:43Z posteriores al hash 6ee5b66 | Cumple | CI ejecuta npm test, e2e, build y flutter test; runs en verde. |
| Trazabilidad consolidada navegable | docs/aspectos.md:1-15 tabla con 8 columnas; enlaces a escenarios, ADR, C4, código y pruebas | Cumple | La cadena aspecto→requisito→C4→ADR→código→pruebas→evidencia es navegable. |
| PDF u otro adjunto exigido por el aula | docs/entrega-corte1-moodle.pdf existe en el árbol pero no se accede al adjunto de Moodle | No verificado | La entrega en Moodle no está disponible para el revisor. |
| Sustentación del corte | Sin evidencia de sesión de sustentación en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura del repositorio | docs/arc42.md es un único archivo sin las 12 secciones; docs/arc42/ solo contiene 04-estrategia-solucion.md; no hay docs/adr/ con NNNN-titulo.md completo? Sí existe; falta README con arranque en un comando | No cumple | arc42 no sigue la plantilla de 12 secciones; desviación de estructura mínima. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md, 0002-arquitectura-y-stack.md, 0003-reto-corte1-stack-obligatorio.md; nombres con patrón NNNN-titulo-kebab | Cumple | Un archivo por decisión; ADR-0001 marcada 'Reemplazada por ADR-0002'. |
| Tabla de aspectos con trazabilidad navegable | docs/aspectos.md:1-15 enlaces a escenarios_calidad.md, c4/README.md, adr/0002, código y pruebas | Cumple | Las filas A1-A4 tienen 8 columnas con enlaces. |
| Registro de uso de IA | docs/ia.md:1-15 con fechas, herramientas, aceptado y rechazado con motivo; log de commits 2026-08-23 a 2026-09-05 | Cumple | Incluye columna de descartes y registro individual por integrante. |
| README con arranque y prueba en un comando | README.md:46-77 usa npm install, npm run start, flutter pub get, flutter run; no hay comando único para todo el sistema | No cumple | Se requieren pasos manuales separados backend/mobile y requisitos declarados. |
| Pipeline y análisis estático en CI | .github/workflows/ci.yml:1-25 corre tests/build/analyze pero no define jobs SonarCloud; sin archivo .github/workflows con sonar; sonar-project.properties existe pero sin ejecución visible | No cumple | No hay step de SonarCloud ni runs que lo evidencien. |
| Secretos y credenciales fuera del repositorio | secretos '(sin coincidencias)'; envs_versionados []; .env.example en lugar de .env | Cumple | Sin secretos detectados en HEAD. |
| Autoría y colaboración en el historial | autores: 25 Cconde31, 9 vylrir, 7 MiguelJacome, 1 fconde, 1 Steamlinker; .mailmap al final consolidando identidades | Cumple | Los 4 integrantes tienen commits en master; identidades consolidadas con .mailmap. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `f7c1a6c7c4371f1e9df38ca268895544cca43c17 2026-09-07T09:59:41-05:00 Enlazar ADR a sus commits y cubrir criterios 1-3 de la rúbrica del reto`
- **Veredicto**: con pendientes
- Resumen: El proyecto tiene avance real: arquitectura hexagonal, corte vertical funcional, pruebas y CI en verde; pero el compendio S5 incumple correcciones.md y quedan pendientes transversales de estructura, README y Sonar.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- f7c1a6c 2026-09-07T09:59:41-05:00 enlaza ADR y cubre criterios 1-3 de la rúbrica, pero es posterior al cierre del corte 1.

Pendientes que siguen abiertos:
- correcciones.md no existe en HEAD.
- arc42 no está completo en HEAD.
- CI sin SonarCloud en HEAD.
- README sin comando único de arranque en HEAD.

## Recuento y nota sugerida

8 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula: no se pudo acceder a Moodle.
- Sustentación del corte: sin evidencia de sesión.
- SonarCloud: no hay run que muestre análisis estático, solo archivo de configuración.

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado 6ee5b66.
- Sin correcciones.md no se puede verificar trazabilidad de correcciones S1-S4.
- arc42.md es un resumen sin las 12 secciones exigidas.
- docs/arc42/ solo contiene 04-estrategia-solucion.md; secciones 1-3 y 5-12 ausentes como archivos de la plantilla.
- CI no evidencia análisis estático SonarCloud; la organización isco-utb no aparece en workflows.
- README no permite arrancar todo el sistema con un solo comando.
- Un commit posterior al cierre (f7c1a6c 2026-09-07T09:59:41-05:00) modifica ADR y aspectos, pero no cierra hallazgos del corte.
- Commits posteriores al cierre (no calificados): f7c1a6c 2026-09-07T09:59:41-05:00 Enlazar ADR a sus commits y cubrir criterios 1-3 de la rúbrica del reto
