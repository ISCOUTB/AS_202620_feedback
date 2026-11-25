# ElMapita · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `main` · [`834a79c2db765f93c38fc41840e09ead5001c6df`](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/834a79c2db765f93c38fc41840e09ead5001c6df) · 2026-11-25T21:52:35.888 UTC. Sin cambio de SHA frente a S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en topología; faltan pruebas de ejecución.** C4 y arc42 sitúan almacenamiento y datos en Supabase; Compose configura el backend Node contra Supabase externo y ADR-0015 reemplaza el hosting API por Dokploy. No interpretar el contenedor o el enlace de un ADR como aplicación verificada. Documentar la URL institucional efectiva en README y repetir la medición EC-01 con la CI corregida.

Evidencia al SHA: [C4_L2_Container.md · L14-L29](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/c4/C4_L2_Container.md#L14-L29) · [arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/arc42/arc42-template-EN.md) · [0015-reemplazo-adr-0012-despliegue-dokploy.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/docs/adr/0015-reemplazo-adr-0012-despliegue-dokploy.md) · [compose.lab.yaml · L3-L28](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/deploy/compose.lab.yaml#L3-L28).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/45077520811): falló.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_ElMapita` · rama `main` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_ElMapita/runs/137378137090) completado el 2026-11-22T22:24:46 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_ElMapita&branch=main). **Quality Gate: No aprobado.** Fuentes declaradas: `backend/src,frontend/lib`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/sonar-project.properties). El proveedor marcó incumplimiento en código nuevo; revisar en el tablero sin publicar el detalle de los hallazgos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** Sin URL pública concreta en README; las referencias son locales o de ejemplo. [README del SHA](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/834a79c2db765f93c38fc41840e09ead5001c6df/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
