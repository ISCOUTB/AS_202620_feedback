# UTB Tracker · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `main` · [`d7b3c78996ef00bff9443e440bfcccea295ecccf`](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/d7b3c78996ef00bff9443e440bfcccea295ecccf) · 2026-11-25T21:52:36.924 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/compare/2510dfc50292a4d85cd651403146120a495688e3...d7b3c78996ef00bff9443e440bfcccea295ecccf). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Discrepancia operativa.** C4 y arc42 conservan PostgreSQL, API, cliente y worker como topología. Compose incluye worker, pero el runbook afirma que el job `deploy` lo reinicia y el workflow de este SHA solo prueba. CI pasó; esto no garantiza operación del worker. Corregir runbook y evidenciar reinicio/estado en producción; verificar por separado publicación y firma del APK anunciado.

Evidencia al SHA: [C2.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d7b3c78996ef00bff9443e440bfcccea295ecccf/docs/c4/C2.md) · [arc42.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d7b3c78996ef00bff9443e440bfcccea295ecccf/docs/arc42/arc42.md) · [0013-identidad-propia-y-servidor-unico.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d7b3c78996ef00bff9443e440bfcccea295ecccf/docs/adr/0013-identidad-propia-y-servidor-unico.md) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d7b3c78996ef00bff9443e440bfcccea295ecccf/deploy/compose.lab.yaml) · [worker.md · L78-L85](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d7b3c78996ef00bff9443e440bfcccea295ecccf/docs/despliegue/worker.md#L78-L85) · [ci.yml](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d7b3c78996ef00bff9443e440bfcccea295ecccf/.github/workflows/ci.yml).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/45231776814): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_UTB_TRACKER` · rama `main` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/runs/137893193795) completado el 2026-11-23T17:49:50 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_UTB_TRACKER&branch=main). **Quality Gate: Aprobado.** Fuentes declaradas: `app`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d7b3c78996ef00bff9443e440bfcccea295ecccf/sonar-project.properties). El resumen del proveedor registra 0 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [API institucional](https://api-tractar.iscoutb.dev/docs); README anuncia cliente Android como release, sin comprobación de v1.0.4. [README del SHA](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d7b3c78996ef00bff9443e440bfcccea295ecccf/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
