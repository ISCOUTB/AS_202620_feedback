# PideUtb · Evaluación técnica de entrega

**Definitivo al corte del 25 de noviembre de 2026, sujeto a comentarios de los estudiantes.**

[Índice del corte](../resumen-corte-final-2026-11-25.md) · [Evaluación histórica S16](semana-16-final.md)

**Referencia observada:** rama `master` · [`b5f20dce5e1643da632f5a6b5d903b5f699426bb`](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/b5f20dce5e1643da632f5a6b5d903b5f699426bb) · 2026-11-25T21:52:36.507 UTC. SHA distinto de la referencia S16. [Comparación entre revisiones](https://github.com/ISCOUTB/AS_202620_PideUtb/compare/e5f40775dc255ed5db8b1b32eb3c2e56610316db...b5f20dce5e1643da632f5a6b5d903b5f699426bb). No reemplaza la evidencia histórica de S16.

## Coherencia de arquitectura · C2 y C4

**Coincide en el alcance comparado.** Vistas y ADR-0008 separan el sitio del backend y PostgreSQL privado. Compose define API y base y el sitio se sirve desde nginx. README distingue cliente, mostrador y API. Conservar prueba de la versión desplegada y de un pedido con fallo de un proveedor de notificación; una ruta health no acredita el pedido.

Evidencia al SHA: [nivel2-contenedores.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/b5f20dce5e1643da632f5a6b5d903b5f699426bb/docs/c4/nivel2-contenedores.md) · [arc42.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/b5f20dce5e1643da632f5a6b5d903b5f699426bb/docs/arc42/arc42.md) · [0008-despliegue-en-el-servidor-del-laboratorio.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/b5f20dce5e1643da632f5a6b5d903b5f699426bb/docs/adr/0008-despliegue-en-el-servidor-del-laboratorio.md) · [compose.lab.yaml](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/b5f20dce5e1643da632f5a6b5d903b5f699426bb/deploy/compose.lab.yaml) · [nginx.conf](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/b5f20dce5e1643da632f5a6b5d903b5f699426bb/sitio/nginx.conf).

## Implementación, calidad y despliegue · C1 y C3

- **Actions:** [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/45218510456): pasó.
- **SonarQube:** SonarQube Cloud · `ISCOUTB_AS_202620_PideUtb` · rama `master` · [check asociado al SHA](https://github.com/ISCOUTB/AS_202620_PideUtb/runs/137847393864) completado el 2026-11-23T16:37:43 UTC · [tablero](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_PideUtb&branch=master). **Quality Gate: Aprobado.** Fuentes declaradas: `backend/app`, con exclusiones según [configuración](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/b5f20dce5e1643da632f5a6b5d903b5f699426bb/sonar-project.properties). El resumen del proveedor registra 47 incidencias nuevas y 0 alertas de seguridad (*hotspots*) nuevas; no es el inventario de hallazgos abiertos. No se verificó un inventario completo de hallazgos abiertos de severidad alta o superior ni su clasificación individual: **sin bonificación de calidad acreditada a partir de este check**.
- **Publicación documentada:** [Sitio y mostrador](https://pideutb.iscoutb.dev) y [API](https://api-pideutb.iscoutb.dev/docs) en subdominios institucionales. [README del SHA](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/b5f20dce5e1643da632f5a6b5d903b5f699426bb/README.md). La URL, la disponibilidad medida y el SHA servido son evidencias distintas. No se acreditó aquí la ejecución funcional de punta a punta de este SHA.

## Rúbrica y observaciones

C1 (1,25) requiere confirmar el escenario funcional y respuesta al desafío. C2 (1,00), C3 (1,00) y C4 (0,75) se sustentan en las evidencias y reservas anteriores y en la matriz histórica, sin trasladar automáticamente su valoración a este SHA. C5 (1,00), sustentación, demostración y colaboración, queda con el docente; **pendiente no equivale a cero**. No se publican notas personales ni un total inferido.

Una observación sustentada puede motivar una corrección trazable. Para contrastarla, indicar el apartado, el enlace a la evidencia y el SHA correspondiente, y aclarar si la evidencia estaba disponible al corte o se añadió después.
