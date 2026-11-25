# Maps UTB · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`26543815f2e67a5033e1add02e615918484c162c`](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/26543815f2e67a5033e1add02e615918484c162c) · 2026-11-25T21:52:36.918 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_mapsutb/compare/0e21bd155c2c989bcd6fc0f9380e7faabab5460e...26543815f2e67a5033e1add02e615918484c162c). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en el alcance comparado.** La vista C4 en arc42 representa una app Flutter de un solo artefacto; ADR-0007 y el workflow describen Firebase Hosting y el Compose de laboratorio ofrece Nginx alternativo. La rama incluye una sonda de `health.json`, pero una sonda recurrente no demuestra por sí sola el SHA de la compilación publicada. Incorporar la URL institucional y documentar esa huella.

Evidencia al SHA: [05_building_block_view.md · L7-L20](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/26543815f2e67a5033e1add02e615918484c162c/docs/arc42/05_building_block_view.md#L7-L20) · [0007-hosting-web-firebase-hosting.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/26543815f2e67a5033e1add02e615918484c162c/docs/adr/0007-hosting-web-firebase-hosting.md) · [docker-compose.yml](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/26543815f2e67a5033e1add02e615918484c162c/infra/docker-compose.yml) · [firebase.json](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/26543815f2e67a5033e1add02e615918484c162c/firebase.json) · [deploy.yml](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/26543815f2e67a5033e1add02e615918484c162c/.github/workflows/deploy.yml).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** No se localizó una ejecución por push asociada al SHA en la consulta. No se trasladó el resultado de otro SHA.. Se localizó además [una ejecución programada](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/45703806741); no se contabiliza como CI de push ni como publicación.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_mapsutb` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_mapsutb/runs/137960363580) completado el 2026-11-23T19:38:23 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_mapsutb&branch=master). **Quality Gate: Aprobado.** Fuentes declaradas: `lib`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/26543815f2e67a5033e1add02e615918484c162c/sonar-project.properties). El resumen del proveedor registra 1 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [Cliente web externo en Firebase](https://mapsutb.web.app/); `health.json` es estático. [README del SHA](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/26543815f2e67a5033e1add02e615918484c162c/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
