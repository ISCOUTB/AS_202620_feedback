# LaPlacita · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`69c2b5b84c95e7b96f993dc616b9d6b00b530022`](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/69c2b5b84c95e7b96f993dc616b9d6b00b530022) · 2026-11-25T21:52:36.493 UTC. Sin cambio de SHA frente a S16.

## Coherencia de arquitectura · C2 y C4

**Discrepancia de alcance.** C4 y arc42 distinguen PostgreSQL opcional; el texto del ADR-0026 sobre confirmación durable debe limitarse a ese modo: el código permite resolver sin despachador cuando no se configuró base. El último flujo de Dokploy localizado falló en el redeploy del backend; el último éxito con huellas es de otro SHA. Ajustar ADR y documentar la revisión servida en ambas URLs.

Evidencia al SHA: [contenedores.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/docs/c4/contenedores.md) · [arc42-template-EN.md · L182-L226](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/docs/arc42/arc42-template-EN.md#L182-L226) · [0026-escrituras-at-least-once-y-creacion-confirmada.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/docs/adr/0026-escrituras-at-least-once-y-creacion-confirmada.md) · [index.js · L464-L497](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/backend/src/persistencia/index.js#L464-L497) · [Actions 43611208946](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/43611208946) · [Actions 42288072311](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/42288072311).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/45081133410): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_LaPlacita` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_LaPlacita/runs/137390243983) completado el 2026-11-22T23:06:41 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_LaPlacita&branch=master). **Quality Gate: Aprobado.** Fuentes declaradas: `src,app`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/backend/sonar-project.properties). El resumen del proveedor registra 4 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [PWA institucional](https://laplacita-app.iscoutb.dev) y [API institucional de pruebas](https://laplacita-test.iscoutb.dev/api/v1/health); no confundir con aceptación de producción. [README del SHA](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/69c2b5b84c95e7b96f993dc616b9d6b00b530022/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
