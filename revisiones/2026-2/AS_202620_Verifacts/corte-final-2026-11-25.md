# Verifacts · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`96538d855c16d4f8c7ed8bb161d59823c34cc442`](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/96538d855c16d4f8c7ed8bb161d59823c34cc442) · 2026-11-25T21:52:36.947 UTC. Sin cambio de SHA frente a S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en el alcance comparado.** C4 y arc42 representan Nginx sirviendo React y reenviando al backend FastAPI con SQLite. Coincide con el ADR-0010, Compose y la configuración del proxy. Probar una extracción y un error seguro en la revisión publicada, no solo una respuesta de salud.

Evidencia al SHA: [02-contenedores.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/docs/c4/02-contenedores.md) · [07-despliegue.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/docs/arc42/07-despliegue.md) · [0010-despliegue-laboratorio-dokploy.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/docs/adr/0010-despliegue-laboratorio-dokploy.md) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/deploy/compose.lab.yaml) · [nginx.conf](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/frontend/nginx.conf).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/44844061979): pasó · [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/44844062023): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_Verifacts` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_Verifacts/runs/136659729655) completado el 2026-11-21T00:29:40 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_Verifacts&branch=master). **Quality Gate: Aprobado.** Fuentes declaradas: `app`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/sonar-project.properties). El resumen del proveedor registra 13 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [Web institucional](https://verifacts.iscoutb.dev) y [API en el mismo host](https://verifacts.iscoutb.dev/docs). [README del SHA](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/96538d855c16d4f8c7ed8bb161d59823c34cc442/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
