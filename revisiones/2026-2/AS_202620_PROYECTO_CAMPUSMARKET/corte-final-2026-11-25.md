# CampusMarket · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`5f8928c266e83175a18d99e56c7fd6fe61244c4d`](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/5f8928c266e83175a18d99e56c7fd6fe61244c4d) · 2026-11-25T21:52:36.431 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/compare/c79c73d47936790b0f248bdea5c0a700ce8fe017...5f8928c266e83175a18d99e56c7fd6fe61244c4d). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincide diseño; ejecución con discrepancia.** C4, arc42, ADR-0025 y Compose concuerdan: Flutter Web en `/app/` servido por FastAPI; MySQL separado. La corrida pública dio 8/9: falló la igualdad entre revisión servida y revisión histórica esperada. Revisar huella, digest y expectativa antes de concluir regresión funcional o certificar la publicación del SHA.

Evidencia al SHA: [02-contenedores.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/5f8928c266e83175a18d99e56c7fd6fe61244c4d/docs/c4/02-contenedores.md) · [07-vista-despliegue.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/5f8928c266e83175a18d99e56c7fd6fe61244c4d/docs/arc42/07-vista-despliegue.md) · [0025-servir-flutter-web-con-fastapi-en-servicio-existente.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/5f8928c266e83175a18d99e56c7fd6fe61244c4d/docs/adr/0025-servir-flutter-web-con-fastapi-en-servicio-existente.md) · [compose.prod.yaml](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/5f8928c266e83175a18d99e56c7fd6fe61244c4d/deploy/compose.prod.yaml) · [Actions 45395636283](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/45395636283).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/45395636436): pasó · [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/45395636479): pasó · [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/45395636283): falló · [Validación Flutter MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/45395636376): pasó · [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/45395636342): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_PROYECTO_CAMPUSMARKET` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/runs/138450759483) completado el 2026-11-24T12:39:55 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_PROYECTO_CAMPUSMARKET&branch=master). **Quality Gate: Aprobado.** El alcance completo del análisis no quedó confirmado. El resumen del proveedor registra 25 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [Cliente web institucional](https://campusmarket.iscoutb.dev/app/) y [API institucional en el mismo host](https://campusmarket.iscoutb.dev/docs). [README del SHA](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/5f8928c266e83175a18d99e56c7fd6fe61244c4d/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
