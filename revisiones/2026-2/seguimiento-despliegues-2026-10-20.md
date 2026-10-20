# README y despliegues · 20 de octubre de 2026

Revisión de los 23 README raíz, 09:34–09:37 COT (UTC−5). **Criterio confirmado por el docente:** el README debe publicar la URL del sitio desplegado y utilizar un subdominio de `iscoutb.dev`.

Se separan tres aspectos: URL documentada, dominio requerido y disponibilidad. No se inventan subdominios ni se interpreta una carencia documental como ausencia de despliegue. Este seguimiento no modifica notas ni aplica retroactivamente este criterio a cierres históricos.

## Resultado documental

- **8** publican al menos un endpoint institucional. Esto no significa que las ocho interfaces de usuario estén en ese dominio: hay API/backend y cumplimiento parcial.
- **6** publican únicamente URLs de otros dominios.
- **9** no publican una URL pública vigente y concreta en el README raíz.

| Proyecto / README fuente | URL documentada | Clasificación | Alcance y pendiente |
|---|---|---|---|
| [AudioShare](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/master/README.md) | https://audioshare.iscoutb.dev | Institucional | Cliente legado; no acredita Flutter web. |
| [QuantIA](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/master/README.md) | https://quantia-utb.onrender.com ; https://quantia-utb-api.onrender.com/health | Externo | Frontend y API en Render. |
| [CampusMarket](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/master/README.md) | https://campusmarket.iscoutb.dev ; https://nnigarp.github.io/AS_202620_PROYECTO_CAMPUSMARKET/ | Institucional | Cumple la API; frontend en GitHub Pages, cumplimiento parcial del sitio. |
| [Clubs UTB](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/master/README.md) | — | Sin URL vigente | Sin dirección pública concreta. |
| [Dinamik](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/master/README.md) | https://iscoutb.github.io/AS_202620_DinamikUTB/ ; https://dinamikutb-api.onrender.com | Externo | Frontend y API fuera del dominio requerido. |
| [Drift](https://github.com/ISCOUTB/AS_202620_Drift/blob/master/README.md) | https://drift.iscoutb.dev | Institucional | Frontend y backend; Vercel/Azure como alternativas. |
| [ElMapita](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/main/README.md) | — | Sin URL vigente | Solo localhost y placeholder de Supabase; funcionamiento confirmado por docente. |
| [EnAgenda](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/master/README.md) | — | Sin URL vigente | Declara contenedor desplegado, pero dirección pendiente de asignar. |
| [GimnasioUTB](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/main/README.md) | https://gimnasio-utb.iscoutb.dev | Institucional | URL del backend, no prueba de interfaz pública. |
| [InvenTrack](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/main/README.md) | https://inventrack.iscoutb.dev ; https://inventrack-api.onrender.com | Institucional | Servicio/API institucional y alternativa Render; distinguir interfaz de API. |
| [LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/master/README.md) | — | Sin URL vigente | La URL Azure histórica se declara retirada el 13/oct; falta la vigente de Dokploy. |
| [LostVault](https://github.com/ISCOUTB/AS_202620_LostVault/blob/main/README.md) | — | Sin URL vigente | No publica dirección HTTP/HTTPS de despliegue. |
| [MapsUTB](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/master/README.md) | https://mapsutb.web.app/ | Externo | Firebase; pendiente dominio institucional. |
| [PideUtb](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/master/README.md) | https://pideutb.iscoutb.dev ; https://api-pideutb.iscoutb.dev/docs | Institucional | Sitio y API; actualización y despliegues confirmados por docente. |
| [Recobra](https://github.com/ISCOUTB/AS_202620_Recobra/blob/master/README.md) | https://recobra.iscoutb.dev ; https://recobra.iscoutb.dev/app/ | Institucional | Presentación confirmada por docente; no se infiere demostración funcional adicional. |
| [ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/master/README.md) | https://routb.iscoutb.dev | Institucional | Backend; avance presentado confirmado por docente. |
| [ShareU](https://github.com/ISCOUTB/AS_202620_ShareU/blob/master/README.md) | — | Sin URL vigente | Campos «URL Vercel» y «URL Render» sin completar. |
| [TAIA](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/main/README.md) | http://taia-sistema-jkbo9i-ec2cd4-144-24-4-187.sslip.io ; https://taia-backend-latest.onrender.com/health | Externo | Actualizar URL oficial; el docente confirmó avance y despliegue funcionando. |
| [Tienda Virtual](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/main/README.md) | — | Sin URL vigente | Declara URL definitiva pendiente en Dokploy. |
| [UTB Tracker](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/main/README.md) | — | Sin URL vigente | Solo dirección local 127.0.0.1. |
| [uniTeam](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/master/README.md) | https://uniteam-web.onrender.com ; https://uniteam-api.onrender.com | Externo | Frontend y API en Render. |
| [Verifacts](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/master/README.md) | — | Sin URL vigente | Solo URLs locales; enlaza guía, pero no dirección pública en README raíz. |
| [XALD](https://github.com/ISCOUTB/AS_202620_XALD/blob/master/README.md) | https://xald-backend.onrender.com | Externo | Backend en Render. |

## Disponibilidad observada, separada de documentación

- Los ocho dominios institucionales y la API de PideUtb devolvieron **403 / Cloudflare 1010** al cliente automatizado. Es un bloqueo de esa comprobación, **no evidencia de caída**. No se eludió el bloqueo.
- Respondieron HTTP 200 los frontend documentados de QuantIA, CampusMarket (GitHub Pages), Dinamik (GitHub Pages) y MapsUTB (Firebase). XALD `/health` respondió 200 con `status: ok`. Esto no valida todos los flujos.
- La URL `sslip.io` exacta del README de TAIA respondió 404 en raíz, `/docs` y `/health`; el respaldo Render agotó 20 segundos de espera. Puede ser una dirección desactualizada respecto al despliegue que vio el docente. **TAIA sí presentó avance y despliega bien según confirmación docente.** Corresponde actualizar su URL oficial, no afirmar ausencia de despliegue.
- uniTeam devolvió 503 en frontend y `/health` de API durante la consulta; no se determinó causa ni permanencia.
- Los equipos sin URL pública concreta no fueron probados. **ElMapita presentó avance y está funcionando según el docente**; falta reflejar la dirección vigente en el README.

La comprobación fue HTTP de lectura, con TLS normal, sin iniciar sesión, introducir datos ni ejecutar software estudiantil. No es una prueba funcional integral.

## Qué debe quedar en cada README

Publicar la URL oficial exacta y vigente bajo `iscoutb.dev`, identificar si corresponde al sitio/interfaz o a la API/backend y, si son diferentes, documentar ambas. Diferenciar direcciones alternativas e históricas. Añadir rutas de documentación o salud cuando existan, sin sustituir con ellas el enlace al sitio. Registrar la presentación docente por separado del estado de issues.

[Presentaciones confirmadas](avances-presentados-2026-10-20.md) · [Issues](seguimiento-issues-2026-10-20.md) · [S12 preliminar](resumen-s12.md)
