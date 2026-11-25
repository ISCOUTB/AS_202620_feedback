# EnAgenda · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`bbd3e01a06aefb220b2a74cce40a4b4a7f4a9086`](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/bbd3e01a06aefb220b2a74cce40a4b4a7f4a9086) · 2026-11-25T21:52:35.903 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_EnAgenda/compare/a6dde3025c6864eb8c2871c6e9732b205f68001b...bbd3e01a06aefb220b2a74cce40a4b4a7f4a9086). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en persistencia; faltan pruebas de ejecución.** El C4 distingue memoria heredada de persistencia de eventos e invitaciones. ADR y Compose coinciden en Flask/PostgreSQL 17. La vista de despliegue describe Dokploy y el README sigue marcando una URL pendiente; no se puede derivar un host ni dar la transición productiva por cerrada. Separar el recorrido persistente del legado en la guía de prueba.

Evidencia al SHA: [nivel-2-contenedores.md · L7-L20](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/bbd3e01a06aefb220b2a74cce40a4b4a7f4a9086/docs/c4/nivel-2-contenedores.md#L7-L20) · [07-vista-de-despliegue.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/bbd3e01a06aefb220b2a74cce40a4b4a7f4a9086/docs/arc42/07-vista-de-despliegue.md) · [0004-persistir-datos-en-postgresql.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/bbd3e01a06aefb220b2a74cce40a4b4a7f4a9086/docs/adr/0004-persistir-datos-en-postgresql.md) · [docker-compose.yml · L2-L24](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/bbd3e01a06aefb220b2a74cce40a4b4a7f4a9086/docker-compose.yml#L2-L24).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [Auditoria de dependencias](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/45243353421): pasó · [Taller mensajes y consistencia](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/45243353564): pasó · [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/45243353549): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_EnAgenda` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_EnAgenda/runs/137933880914) completado el 2026-11-23T18:55:16 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_EnAgenda&branch=master). **Quality Gate: No aprobado.** El alcance completo del análisis no quedó confirmado. El proveedor marcó incumplimiento en código nuevo; revisar en el tablero sin publicar el detalle de los hallazgos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** Sin URL pública concreta en README; el host indicado es un marcador. [README del SHA](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/bbd3e01a06aefb220b2a74cce40a4b4a7f4a9086/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
