# Recobra · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`8aeffba5675ba4a9e3466a98cfac7408d2cd8049`](https://github.com/ISCOUTB/AS_202620_Recobra/commit/8aeffba5675ba4a9e3466a98cfac7408d2cd8049) · 2026-11-25T21:52:36.379 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_Recobra/compare/703d44471795910de17d8b2b8d57df5ae5df7d50...8aeffba5675ba4a9e3466a98cfac7408d2cd8049). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincidencia con condición operativa.** C4, arc42 y ADR-0010 describen Flutter/NestJS con PostgreSQL aparte. El Compose no administra ese contenedor y la aplicación selecciona memoria si no recibe `DATABASE_URL`. Acreditar la persistencia en el entorno con readiness y reinicio controlado; el fallback no demuestra una caída ni almacenamiento durable.

Evidencia al SHA: [C4-C2.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/8aeffba5675ba4a9e3466a98cfac7408d2cd8049/docs/c4/C4-C2.md) · [arc42.md · L147-L175](https://github.com/ISCOUTB/AS_202620_Recobra/blob/8aeffba5675ba4a9e3466a98cfac7408d2cd8049/docs/arc42/arc42.md#L147-L175) · [0010-despliegue-en-dokploy-servidor-del-laboratorio.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/8aeffba5675ba4a9e3466a98cfac7408d2cd8049/docs/adr/0010-despliegue-en-dokploy-servidor-del-laboratorio.md) · [compose.lab.yaml · L1-L24](https://github.com/ISCOUTB/AS_202620_Recobra/blob/8aeffba5675ba4a9e3466a98cfac7408d2cd8049/deploy/compose.lab.yaml#L1-L24) · [publicaciones.module.ts · L38-L45](https://github.com/ISCOUTB/AS_202620_Recobra/blob/8aeffba5675ba4a9e3466a98cfac7408d2cd8049/src/publicaciones/publicaciones.module.ts#L38-L45).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/45193701084): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_Recobra` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_Recobra/runs/137759120476) completado el 2026-11-23T14:24:40 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_Recobra&branch=master). **Quality Gate: Aprobado.** Fuentes declaradas: `.`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_Recobra/blob/8aeffba5675ba4a9e3466a98cfac7408d2cd8049/sonar-project.properties). El resumen del proveedor registra 113 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [Cliente web institucional](https://recobra.iscoutb.dev/app/) y [API del mismo host](https://recobra.iscoutb.dev/health). [README del SHA](https://github.com/ISCOUTB/AS_202620_Recobra/blob/8aeffba5675ba4a9e3466a98cfac7408d2cd8049/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
