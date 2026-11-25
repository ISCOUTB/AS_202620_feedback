# InvenTrack · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `main` · [`51f353704cabdd0100c082d6af3912d18dc83795`](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/51f353704cabdd0100c082d6af3912d18dc83795) · 2026-11-25T21:52:35.892 UTC. Sin cambio de SHA frente a S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en el alcance comparado.** C4 actual y arc42 distinguen modo efímero y persistencia SQLite en volumen; el Compose fija la ruta durable y el ADR-0024 deja Dokploy institucional como destino. No inferir soporte de múltiples réplicas de un único archivo. Verificar la copia y la restauración, además de un flujo de inventario.

Evidencia al SHA: [02-contenedores.md · L33-L48](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/c4-actual/02-contenedores.md#L33-L48) · [arc42-template-EN.md · L390-L450](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/arc42/arc42-template-EN.md#L390-L450) · [0024-usar-solo-dokploy-institucional.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/adr/0024-usar-solo-dokploy-institucional.md) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/deploy/compose.lab.yaml).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/45112616914): pasó · [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/45112590983): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_InvenTrack` · rama `main` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_InvenTrack/runs/137488541611) completado el 2026-11-23T04:35:13 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_InvenTrack&branch=main). **Quality Gate: Aprobado.** Fuentes declaradas: `app`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/sonar-project.properties). El resumen del proveedor registra 0 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. La fecha del check es anterior a la marca temporal del commit; GitHub sí asocia el check al SHA exacto. No se infiere la fecha efectiva del análisis. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [API institucional](https://inventrack.iscoutb.dev/health). [README del SHA](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
