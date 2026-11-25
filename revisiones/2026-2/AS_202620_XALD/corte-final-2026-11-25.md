# XALD · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`166693dee5d49e408782cfb0fcd278320338dd27`](https://github.com/ISCOUTB/AS_202620_XALD/commit/166693dee5d49e408782cfb0fcd278320338dd27) · 2026-11-25T21:52:36.991 UTC. Sin cambio de SHA frente a S16.

## Coherencia de arquitectura · C2 y C4

**Discrepancia documental.** arc42 §1 atribuye a la base local una propiedad que C4 niega. La implementación de la base y la cola usa Room; ajustar las afirmaciones en las vistas a lo que la configuración efectiva permite demostrar. Por separado, el ADR de PostgreSQL remoto y `render.yaml` son compatibles; eso no acredita la instancia activa ni un dominio institucional.

Evidencia al SHA: [c2.md · L20-L35](https://github.com/ISCOUTB/AS_202620_XALD/blob/166693dee5d49e408782cfb0fcd278320338dd27/docs/c4/c2.md#L20-L35) · [01-introduction goals.md · L15-L23](https://github.com/ISCOUTB/AS_202620_XALD/blob/166693dee5d49e408782cfb0fcd278320338dd27/docs/arc42/01-introduction%20goals.md#L15-L23) · [0015-persistencia-remota-postgres.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/166693dee5d49e408782cfb0fcd278320338dd27/docs/adr/0015-persistencia-remota-postgres.md) · [render.yaml](https://github.com/ISCOUTB/AS_202620_XALD/blob/166693dee5d49e408782cfb0fcd278320338dd27/render.yaml) · [CoreDatabase.kt](https://github.com/ISCOUTB/AS_202620_XALD/blob/166693dee5d49e408782cfb0fcd278320338dd27/XALDAPP/corefinanciero/src/main/java/com/proyecto/xald/corefinanciero/CoreDatabase.kt).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/45113474971): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_XALD` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_XALD/runs/137491088379) completado el 2026-11-23T04:43:27 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_XALD&branch=master). **Quality Gate: Aprobado.** El alcance completo del análisis no quedó confirmado. El resumen del proveedor registra 51 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [API externa en Render](https://xald-backend.onrender.com/health); no acredita subdominio institucional ni cliente Android. [README del SHA](https://github.com/ISCOUTB/AS_202620_XALD/blob/166693dee5d49e408782cfb0fcd278320338dd27/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
