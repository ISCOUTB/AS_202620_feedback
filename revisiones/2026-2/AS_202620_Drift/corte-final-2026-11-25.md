# Drift · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`6220c8613b84080764513fb2dbd6f2a6c7cb2de9`](https://github.com/ISCOUTB/AS_202620_Drift/commit/6220c8613b84080764513fb2dbd6f2a6c7cb2de9) · 2026-11-25T21:52:35.956 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_Drift/compare/b841450ce273f440d12d8fe6b5dd75c78e7b9bfb...6220c8613b84080764513fb2dbd6f2a6c7cb2de9). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en el alcance comparado.** C4 y el Compose coinciden en API, frontend y PostgreSQL 17; ADR-0014 explica por qué la base es fuente de verdad y no solo caché. arc42 distingue ensayo de integración y prueba en laboratorio. Adjuntar una restauración ensayada y medición de latencia del despliegue; el pipeline verde no reemplaza esas pruebas.

Evidencia al SHA: [contenedores.md · L14-L27](https://github.com/ISCOUTB/AS_202620_Drift/blob/6220c8613b84080764513fb2dbd6f2a6c7cb2de9/docs/c4/contenedores.md#L14-L27) · [arc42-11-riesgos-y-deuda-tecnica.md · L182-L214](https://github.com/ISCOUTB/AS_202620_Drift/blob/6220c8613b84080764513fb2dbd6f2a6c7cb2de9/docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md#L182-L214) · [0014-postgresql-como-persistencia.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/6220c8613b84080764513fb2dbd6f2a6c7cb2de9/docs/adr/0014-postgresql-como-persistencia.md) · [compose.lab.yaml · L75-L104](https://github.com/ISCOUTB/AS_202620_Drift/blob/6220c8613b84080764513fb2dbd6f2a6c7cb2de9/deploy/compose.lab.yaml#L75-L104).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/45296721038): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_Drift` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_Drift/runs/138120265587) completado el 2026-11-24T00:26:12 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_Drift&branch=master). **Quality Gate: Aprobado.** Fuentes declaradas: `backend/app,frontend`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_Drift/blob/6220c8613b84080764513fb2dbd6f2a6c7cb2de9/sonar-project.properties). El resumen del proveedor registra 31 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [Aplicación web institucional](https://drift.iscoutb.dev); API en el mismo dominio. [README del SHA](https://github.com/ISCOUTB/AS_202620_Drift/blob/6220c8613b84080764513fb2dbd6f2a6c7cb2de9/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
