# GimnasioUTB · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `main` · [`5a1044133267d7018714741211e0f3c0354815ec`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/5a1044133267d7018714741211e0f3c0354815ec) · 2026-11-25T21:52:35.872 UTC. Sin cambio de SHA frente a S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en el alcance comparado.** El retorno a PostgreSQL propio del ADR-0011 se ve en C4, arc42 y Compose, con inicialización antes de la API y dependencias de arranque. Esta revisión no valida un escaneo QR real ni el cliente Flutter. Mostrar una lectura y un rechazo de QR de un solo uso sin datos reales.

Evidencia al SHA: [c4_level2.md · L6-L26](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/c4/c4_level2.md#L6-L26) · [arc42_gimnasio_utb.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/arc42/arc42_gimnasio_utb.md) · [0011-volver-a-postgresql-propio-y-login-local.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/docs/adr/0011-volver-a-postgresql-propio-y-login-local.md) · [compose.lab.yaml · L20-L95](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/deploy/compose.lab.yaml#L20-L95).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/45114911596): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_GimnasioUTB` · rama `main` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/runs/137495617699) completado el 2026-11-23T04:58:50 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_GimnasioUTB&branch=main). **Quality Gate: Aprobado.** El alcance completo del análisis no quedó confirmado. El resumen del proveedor registra 8 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [API institucional](https://gimnasio-utb.iscoutb.dev/health), no URL del cliente Flutter. [README del SHA](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/5a1044133267d7018714741211e0f3c0354815ec/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
