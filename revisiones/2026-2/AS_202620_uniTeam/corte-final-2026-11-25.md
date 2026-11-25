# uniTeam · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`0e2044f8fb815c490a553ce8c4ed5c53928620fc`](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/0e2044f8fb815c490a553ce8c4ed5c53928620fc) · 2026-11-25T21:52:36.959 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_uniTeam/compare/469517a59d8bb1f8a1c31db118bfac2934b44624...0e2044f8fb815c490a553ce8c4ed5c53928620fc). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en el alcance comparado.** El C4 y arc42 separan Next.js/FastAPI/MySQL e identidad externa. El ADR-0016 ratifica MySQL y Compose confirma el motor en desarrollo; no inferir que el proveedor de identidad local o la base local sean los de producción. Adjuntar huellas web/API y una prueba de notificación/autorización en el entorno real.

Evidencia al SHA: [nivel2-contenedores.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0e2044f8fb815c490a553ce8c4ed5c53928620fc/docs/c4/nivel2-contenedores.md) · [arc42-uniteam.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0e2044f8fb815c490a553ce8c4ed5c53928620fc/docs/arc42/arc42-uniteam.md) · [0016-conservar-mysql-como-fuente-de-verdad.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0e2044f8fb815c490a553ce8c4ed5c53928620fc/docs/adr/0016-conservar-mysql-como-fuente-de-verdad.md) · [compose.yaml](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0e2044f8fb815c490a553ce8c4ed5c53928620fc/compose.yaml).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [seguridad-dependencias](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/45115373646): pasó · [CI](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/45115373553): pasó. Se localizó además [una ejecución programada](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/45674330595); no se contabiliza como CI de push ni como publicación.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_uniTeam` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_uniTeam/runs/137497085020) completado el 2026-11-23T05:03:42 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_uniTeam&branch=master). **Quality Gate: Aprobado.** Fuentes declaradas: `app,web/app,web/lib,scripts`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0e2044f8fb815c490a553ce8c4ed5c53928620fc/sonar-project.properties). El resumen del proveedor registra 105 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [Web institucional](https://uniteam-web.iscoutb.dev) y [API institucional](https://uniteam-api.iscoutb.dev/health). [README del SHA](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/0e2044f8fb815c490a553ce8c4ed5c53928620fc/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
