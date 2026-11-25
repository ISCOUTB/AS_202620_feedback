# DinamikUTB · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`fa14e6ad79f190f9654768d6a4c1b95c66ecba54`](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/fa14e6ad79f190f9654768d6a4c1b95c66ecba54) · 2026-11-25T21:52:35.911 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_DinamikUTB/compare/2dd324ea6a9f53d5be48f20ababd21a541c83d52...fa14e6ad79f190f9654768d6a4c1b95c66ecba54). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en el alcance comparado.** C4, arc42 §7 y ADR-0012 separan Flutter Web en GitHub Pages de FastAPI con PostgreSQL 16 en el laboratorio. El Compose reproduce el lado API/BD. CI y publicación de Pages pasan en el SHA, a diferencia de parte de la evidencia S16; no prueban qué revisión sirve la API. Documentar huellas separadas de frontend y backend.

Evidencia al SHA: [contenedores.puml · L12-L24](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/fa14e6ad79f190f9654768d6a4c1b95c66ecba54/docs/c4/contenedores.puml#L12-L24) · [07-deployment-view.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/fa14e6ad79f190f9654768d6a4c1b95c66ecba54/docs/arc42/07-deployment-view.md) · [0012-despliegue-en-servidor-del-laboratorio.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/fa14e6ad79f190f9654768d6a4c1b95c66ecba54/docs/adr/0012-despliegue-en-servidor-del-laboratorio.md) · [compose.lab.yaml · L40-L50](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/fa14e6ad79f190f9654768d6a4c1b95c66ecba54/deploy/compose.lab.yaml#L40-L50).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/45428557812): pasó · [Auditoría de dependencias](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/45428557747): pasó · [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/45428558154): pasó. GitHub Pages reporta éxito en su workflow para el frontend; no verifica la revisión de backend.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_DinamikUTB` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_DinamikUTB/runs/138570446678) completado el 2026-11-24T15:46:56 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_DinamikUTB&branch=master). **Quality Gate: Aprobado.** Fuentes declaradas: `backend/app,frontend/lib`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/fa14e6ad79f190f9654768d6a4c1b95c66ecba54/sonar-project.properties). El resumen del proveedor registra 76 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [API institucional](https://api-dinamikutb.iscoutb.dev/health); [cliente web externo, GitHub Pages](https://iscoutb.github.io/AS_202620_DinamikUTB/). [README del SHA](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/fa14e6ad79f190f9654768d6a4c1b95c66ecba54/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
