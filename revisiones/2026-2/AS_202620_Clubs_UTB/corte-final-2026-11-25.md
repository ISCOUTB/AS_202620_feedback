# Clubes UTB · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`d49859834981d421b2ac995dfe5aec5bbef1f798`](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/d49859834981d421b2ac995dfe5aec5bbef1f798) · 2026-11-25T21:52:35.888 UTC. Sin cambio de SHA frente a S16.

## Coherencia de arquitectura · C2 y C4

**Discrepancia de configuración.** arc42 §7 indica PostgreSQL 18 del entorno institucional; el Compose versionado define PostgreSQL 16. El ADR-0007 y ambas vistas coinciden en FastAPI y PostgreSQL propio, no en la versión operativa. Distinguir referencia versionada del entorno y acreditar versión efectiva; revisar respaldos y restauración con esa versión.

Evidencia al SHA: [07_vista_de_despliegue.md · L7-L24](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/docs/arc42/07_vista_de_despliegue.md#L7-L24) · [contexto.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/docs/c4/contexto.md) · [0007-migracion-dokploy-postgresql.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/docs/adr/0007-migracion-dokploy-postgresql.md) · [compose.lab.yaml · L8-L34](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/deploy/compose.lab.yaml#L8-L34).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [Backend tests](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/45114446592): pasó · [contrato](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/45114446581): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_Clubs_UTB` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/runs/137494085022) completado el 2026-11-23T04:53:35 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_Clubs_UTB&branch=master). **Quality Gate: Aprobado.** Fuentes declaradas: `backend/src,frontend/linkclub/lib`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/sonar-project.properties). El resumen del proveedor registra 35 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [API institucional](https://api-linkclub.iscoutb.dev/health), no URL del cliente Flutter. [README del SHA](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/d49859834981d421b2ac995dfe5aec5bbef1f798/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
