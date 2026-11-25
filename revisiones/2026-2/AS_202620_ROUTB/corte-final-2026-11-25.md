# ROUTB · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`eb38d11f34fdf647c840072d47fea49df7a845d1`](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/eb38d11f34fdf647c840072d47fea49df7a845d1) · 2026-11-25T21:52:36.493 UTC. Sin cambio de SHA frente a S16.

## Coherencia de arquitectura · C2 y C4

**Discrepancia de alcance.** La vista de despliegue centra el cliente móvil y el backend Dokploy con PostgreSQL remoto; el descriptor de laboratorio solo configura backend, mientras el árbol también tiene Dockerfile y nginx para Flutter Web. C4/arc42 deben marcar qué topología web es ejecutable o publicada y cuál es solo una alternativa. No inferir frontend al abrir la URL base de la API.

Evidencia al SHA: [context.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/c4/context.md) · [07_vista_de_despliegue.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/arc42/07_vista_de_despliegue.md) · [0015-dokploy-plataforma-de-despliegue.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/docs/adr/0015-dokploy-plataforma-de-despliegue.md) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/compose.lab.yaml) · [nginx.conf](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/frontend/nginx.conf).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/45113237913): pasó. Se localizó además [una ejecución programada](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/45573975537); no se contabiliza como CI de push ni como publicación.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_ROUTB` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_ROUTB/runs/137490311821) completado el 2026-11-23T04:40:51 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_ROUTB&branch=master). **Quality Gate: Aprobado.** Fuentes declaradas: `backend/app, frontend/lib`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/sonar-project.properties). El resumen del proveedor registra 36 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [API institucional](https://routb.iscoutb.dev/health); no equivale a un cliente web publicado. [README del SHA](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/eb38d11f34fdf647c840072d47fea49df7a845d1/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
