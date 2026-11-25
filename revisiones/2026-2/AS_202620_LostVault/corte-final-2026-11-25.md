# LostVault · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `main` · [`4b8b463acffa1f677ae1f1511da46adc7f73dfe4`](https://github.com/ISCOUTB/AS_202620_LostVault/commit/4b8b463acffa1f677ae1f1511da46adc7f73dfe4) · 2026-11-25T21:52:36.480 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_LostVault/compare/c54471bfb164c3825010d51b9ad9a246fad99ff7...4b8b463acffa1f677ae1f1511da46adc7f73dfe4). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Discrepancia.** El ADR-0008 sustituye Vercel por el servidor universitario; C4, arc42 §7 y README siguen presentando Vercel. El Compose levanta backend, no acredita un PostgreSQL operativo, y el backend auditado declara pendiente conectarlo. Actualizar la vista objetivo frente a la ejecutable y publicar host institucional con revisión demostrable.

Evidencia al SHA: [c4_nivel2.md · L18-L25](https://github.com/ISCOUTB/AS_202620_LostVault/blob/4b8b463acffa1f677ae1f1511da46adc7f73dfe4/docs/c4/c4_nivel2.md#L18-L25) · [07_vista_despliegue.md · L37-L49](https://github.com/ISCOUTB/AS_202620_LostVault/blob/4b8b463acffa1f677ae1f1511da46adc7f73dfe4/docs/arc42/07_vista_despliegue.md#L37-L49) · [0008-plataforma-despliegue-universidad.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/4b8b463acffa1f677ae1f1511da46adc7f73dfe4/docs/adr/0008-plataforma-despliegue-universidad.md) · [docker-compose.yml](https://github.com/ISCOUTB/AS_202620_LostVault/blob/4b8b463acffa1f677ae1f1511da46adc7f73dfe4/docker-compose.yml) · [main.py · L1-L11](https://github.com/ISCOUTB/AS_202620_LostVault/blob/4b8b463acffa1f677ae1f1511da46adc7f73dfe4/backend/main.py#L1-L11).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/45243938178): pasó · [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/45243938437): pasó · [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/45243938388): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_LostVault` · rama `main` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_LostVault/runs/137937129164) completado el 2026-11-23T19:00:36 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_LostVault&branch=main). **Quality Gate: Aprobado.** Fuentes declaradas: `lib,backend`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_LostVault/blob/4b8b463acffa1f677ae1f1511da46adc7f73dfe4/sonar-project.properties). El resumen del proveedor registra 11 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [API externa de referencia](https://backend-nu-self-91.vercel.app), no dominio institucional ni URL pública del panel descrito. [README del SHA](https://github.com/ISCOUTB/AS_202620_LostVault/blob/4b8b463acffa1f677ae1f1511da46adc7f73dfe4/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
