# Tienda Virtual UTB · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `main` · [`56e4597a96d067113a6e2d377cf8fdbfbaee036f`](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/56e4597a96d067113a6e2d377cf8fdbfbaee036f) · 2026-11-25T21:52:36.970 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/compare/6bd72149d51f81285145bccf65719abcdba0dd42...56e4597a96d067113a6e2d377cf8fdbfbaee036f). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en el alcance comparado.** C4, arc42 y ADR-0007 coinciden en Next.js público, FastAPI interno y PostgreSQL 17; Compose separa preparación/migración del backend. No interpretar volumen persistente como recuperación ante pérdida del host. Adjuntar prueba de restauración y medición del flujo de stock en el despliegue.

Evidencia al SHA: [container.md · L24-L61](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/56e4597a96d067113a6e2d377cf8fdbfbaee036f/docs/c4/container.md#L24-L61) · [11-riesgos-y-deuda-tecnica.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/56e4597a96d067113a6e2d377cf8fdbfbaee036f/docs/arc42/11-riesgos-y-deuda-tecnica.md) · [0007-despliegue-dokploy.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/56e4597a96d067113a6e2d377cf8fdbfbaee036f/docs/adr/0007-despliegue-dokploy.md) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/56e4597a96d067113a6e2d377cf8fdbfbaee036f/deploy/compose.lab.yaml).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/45323945257): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_TIENDA-VIRTUAL-UTB` · rama `main` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/runs/138209134764) completado el 2026-11-24T04:06:11 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_TIENDA-VIRTUAL-UTB&branch=main). **Quality Gate: Aprobado.** Fuentes declaradas: `backend/app,frontend/app,frontend/components,frontend/lib`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/56e4597a96d067113a6e2d377cf8fdbfbaee036f/sonar-project.properties). El resumen del proveedor registra 119 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [Web institucional](https://tiendautb.iscoutb.dev/); la arquitectura prevé API privada. [README del SHA](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/56e4597a96d067113a6e2d377cf8fdbfbaee036f/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
