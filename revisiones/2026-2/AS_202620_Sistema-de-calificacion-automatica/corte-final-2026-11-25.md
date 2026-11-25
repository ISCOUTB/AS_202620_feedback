# QuantIA · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`e8de66ab21828bb4bca3fc5441231d5608cae864`](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/e8de66ab21828bb4bca3fc5441231d5608cae864) · 2026-11-25T21:52:36.435 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/compare/9c4e27831bca32a896254daa4ab135e0186ed0ed...e8de66ab21828bb4bca3fc5441231d5608cae864). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en el alcance comparado.** C4 y arc42 describen API, worker, Redis y PostgreSQL, representados en Compose; el worker integra la cola, y ADR-0016 explica la espera acotada y la idempotencia. Probar recuperación ante una interrupción y comparar huella web y API con este SHA; no se acredita el desafío asignado solo con el diagrama.

Evidencia al SHA: [doc-c4.md · L200-L239](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/e8de66ab21828bb4bca3fc5441231d5608cae864/docs/c4/doc-c4.md#L200-L239) · [arc42-template-ES.md · L460-L470](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/e8de66ab21828bb4bca3fc5441231d5608cae864/docs/arc42/arc42-template-ES.md#L460-L470) · [0016-acotar-la-espera-de-la-cola-y-hacer-idempotente-al-worker.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/e8de66ab21828bb4bca3fc5441231d5608cae864/docs/adr/0016-acotar-la-espera-de-la-cola-y-hacer-idempotente-al-worker.md) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/e8de66ab21828bb4bca3fc5441231d5608cae864/deploy/compose.lab.yaml) · [main.py](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/e8de66ab21828bb4bca3fc5441231d5608cae864/backend/worker/main.py).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/45198295412): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_Sistema-de-calificacion-automatica` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/runs/137774941353) completado el 2026-11-23T14:49:47 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_Sistema-de-calificacion-automatica&branch=master). **Quality Gate: Aprobado.** El alcance completo del análisis no quedó confirmado. El resumen del proveedor registra 46 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [Web institucional](https://calificacion.iscoutb.dev) y [API institucional](https://api-calificacion.iscoutb.dev/health). [README del SHA](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/e8de66ab21828bb4bca3fc5441231d5608cae864/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
