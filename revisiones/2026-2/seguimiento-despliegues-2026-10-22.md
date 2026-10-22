# README y despliegues · 22 de octubre de 2026

Consulta del 22 de octubre de 2026, aproximadamente 09:38–09:43 COT (UTC−5), sobre las ramas principales de los 23 repositorios. Es una instantánea de seguimiento, no una nueva calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia (límite exclusivo: 26/oct 05:00 UTC). Se conservan matrices, planillas y notas anteriores.

**Requisito docente:** publicar en el README raíz la URL exacta del sitio desplegado con un subdominio de **iscoutb.dev**. Identificar interfaz y API por separado cuando sean distintas. No se deducen ni inventan dominios.

## Resultado documental

- **9** README incluyen al menos un endpoint institucional. Hay varios backend/API: no equivale a nueve interfaces web conformes.
- **7** incluyen solo direcciones externas al dominio requerido.
- **7** no incluyen URL pública vigente y concreta. Localhost, placeholders y direcciones declaradas retiradas no cuentan.

Frente al [20 de octubre](seguimiento-despliegues-2026-10-20.md), TAIA pasa de externo a institucional (API); Tienda Virtual y VeriFacts pasan de sin URL concreta a externo (sslip). Los restantes mantienen su clasificación documental.

| Proyecto / README inmutable | URL documentada | Clasificación | Alcance y pendiente |
|---|---|---|---|
| [AudioShare](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/README.md) | https://audioshare.iscoutb.dev | Institucional | URL institucional del cliente legado; no acredita despliegue de Flutter web. |
| [QuantIA](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/98a9dcc8f22c77ac5d0dfcea4055865e7727a21e/README.md) | https://quantia-utb.onrender.com ; https://quantia-utb-api.onrender.com/health | Externo | Frontend y API en Render, fuera del dominio requerido. |
| [CampusMarket](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/README.md) | https://campusmarket.iscoutb.dev ; https://nnigarp.github.io/AS_202620_PROYECTO_CAMPUSMARKET/ | Institucional | API institucional; frontend en GitHub Pages. Cumplimiento parcial del sitio. |
| [Clubs UTB](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/b82c8e511133a868e8b1c321fb7be3b70d6afed5/README.md) | — | Sin URL concreta | Sin URL pública concreta en el README raíz. |
| [Dinamik](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/README.md) | https://iscoutb.github.io/AS_202620_DinamikUTB/ ; https://dinamikutb-api.onrender.com | Externo | Frontend en GitHub Pages y API en Render. Expiración del 27/oct y plan del 25/oct declarados por el equipo, no verificados con el proveedor. |
| [Drift](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/README.md) | https://drift.iscoutb.dev | Institucional | URL institucional para frontend/backend; no se repitió prueba funcional del sitio. |
| [ElMapita](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/0421885424d13478cf33c717fdd933a4748d9025/README.md) | — | Sin URL concreta | Solo localhost y un placeholder de Supabase. El docente confirmó presentación y funcionamiento; falta reflejar la URL. |
| [EnAgenda](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/6e546a956d3235ce820c9909edbf13f9415f1d93/README.md) | — | Sin URL concreta | README declara contenedor desplegado, pero no publica dirección concreta. |
| [GimnasioUTB](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/1a706525f6a660c216bc11655c754f65bbbe8bfe/README.md) | https://gimnasio-utb.iscoutb.dev | Institucional | Backend, no URL web de Flutter demostrada. README sigue negando integración funcional aunque el commit 2227faf incorpora llamadas HTTP de Flutter. |
| [InvenTrack](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/28506a8eabcde2234e56698d13ae1d8ae8d0ee24/README.md) | https://inventrack.iscoutb.dev ; https://inventrack-api.onrender.com | Institucional | API únicamente, Flutter pendiente; RAM almacén primario, no caché. |
| [LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/0c9ce082b5850baf1ecda75e82d20757d0101234/README.md) | — | Sin URL concreta | README declara Azure retirado13-oct y Dokploy actual, dice URL arriba sin darla. No afirmar ausencia de despliegue: CI Deploy Dokploy success. |
| [LostVault](https://github.com/ISCOUTB/AS_202620_LostVault/blob/e19be366f7e922a8a9c9abd4a808899f14b2999b/README.md) | — | Sin URL concreta | README raíz sin URL pública. Nueva api/ no implica despliegue. |
| [MapsUTB](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/README.md) | https://mapsutb.web.app/ | Externo | Firebase, no subdominio iscoutb.dev. MapsUTB NO es ElMapita. |
| [PideUtb](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/913847779bdf2ec398ce0aca35a822b6f8217cfc/README.md) | https://pideutb.iscoutb.dev ; https://pideutb.iscoutb.dev/panel.html ; https://api-pideutb.iscoutb.dev/docs | Institucional | Docente confirmó actualización presentada y despliegues. |
| [Recobra](https://github.com/ISCOUTB/AS_202620_Recobra/blob/aacc1ec4094573e15758a245e6c6954a5b76fd48/README.md) | https://recobra.iscoutb.dev ; https://recobra.iscoutb.dev/app/ | Institucional | Docente confirmó presentación, no una certificación de funcionamiento por auditoría. |
| [ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/1bd9425e2675bd7531426b6e31e78546b3e55f2e/README.md) | https://routb.iscoutb.dev | Institucional | Backend; README mantiene pasos antiguos de Render. Docente confirmó presentación. |
| [ShareU](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/README.md) | — | Sin URL concreta | Los campos URL Vercel/URL Render siguen sin completar. |
| [TAIA](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/6565118773cadbffd41c213358facc5735c9783c/README.md) | https://taia-sistema.iscoutb.dev ; https://taia-sistema.iscoutb.dev/health ; https://taia-sistema.iscoutb.dev/docs ; https://taia-backend-latest.onrender.com/health | Institucional | Ahora publica API institucional, salud y documentación; no acredita entrega de una interfaz Flutter. Despliegue funcionando confirmado por docente. |
| [Tienda Virtual](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/d66926b932b47490fede78be66091e7823dffacf/README.md) | https://tiendautb-sistema-n0ojjk-fde272-144-24-4-187.sslip.io/ | Externo | Ahora publica URL sslip concreta; falta dominio institucional. |
| [UTB Tracker](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/7ee2d75a385eb2fb312dae9b938d3fd126895635/README.md) | — | Sin URL concreta | Solo localhost; falta URL pública concreta. |
| [uniTeam](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/README.md) | https://uniteam-web.onrender.com ; https://uniteam-api.onrender.com ; https://uniteam-api.onrender.com/health | Externo | README conserva Render aunque hay configuración Dokploy; no inventar el dominio actual. |
| [VeriFacts](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/9cac28456536b832d475e006a957d50fbd874756/README.md) | http://verifacts-sistema-ju3vi7-444522-144-24-4-187.sslip.io | Externo | URL pública HTTP sslip; falta dominio institucional con certificado válido. |
| [XALD](https://github.com/ISCOUTB/AS_202620_XALD/blob/405a39e0feff40a8414841b6936d5a2dc4488ba4/README.md) | https://xald-backend.onrender.com ; https://xald-backend.onrender.com/health | Externo | Backend Render, fuera del dominio requerido. |

## Disponibilidad y evidencia docente

Esta actualización vuelve a leer los README completos; **no repite una prueba HTTP ni una auditoría funcional de los 23 despliegues**. Los resultados HTTP del 20/oct quedan como historia, no se presentan como mediciones de hoy. Un 403/Cloudflare en una consulta automatizada no demuestra caída. El antiguo 404 del dominio sslip de TAIA no contradice la confirmación docente ni describe su nuevo dominio institucional.

- TAIA y ElMapita: presentación y funcionamiento confirmados por el docente.
- PideUtb: actualización presentada y despliegues confirmados por el docente.
- ROUTB y Recobra: presentación/avance confirmado, sin añadir una certificación funcional no declarada.
- uniTeam: el sondeo programado del 22/oct a las 07:38 COT falló en seis comprobaciones de las URLs Render documentadas. No acredita caída permanente ni el estado de un posible dominio Dokploy no publicado.
- MapsUTB: su sonda programada del 22/oct a las 14:32 UTC terminó correctamente; no valida todos los flujos. Es distinto de ElMapita.

Las fuentes de los sondeos y CI están en el [seguimiento técnico por equipo](seguimiento-s12-2026-10-22.md). [Confirmaciones docentes originales](avances-presentados-2026-10-20.md).
