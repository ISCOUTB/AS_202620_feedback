# README y despliegues · 17 de noviembre de 2026

Todas las soluciones deben documentar URL en README y usar subdominios de iscoutb.dev. Se diferencia frontend de API, documentación de comprobación viva, y URL ausente de ausencia de trabajo. No se inventan hosts. Ver [informe principal](seguimiento-2026-11-17.md) para CI y límites de comprobación.

## AudioShare

Frontend y API: https://audioshare.iscoutb.dev. README conserva una referencia histórica a /health sin commit; docs/despliegue.md declara redespliegue de 11d3972 el 17/nov.

## Clubs_UTB

README ahora documenta API https://api-linkclub.iscoutb.dev y /health. Declara interfaz móvil Flutter, no frontend web publicado.

## DinamikUTB

API https://api-dinamikutb.iscoutb.dev; frontend externo https://iscoutb.github.io/AS_202620_DinamikUTB/. API institucional no convierte Pages en frontend institucional.

## Drift

README ahora documenta https://drift.iscoutb.dev para frontend/backend/PostgreSQL en laboratorio; API con prefijo /api. Se retiran los despliegues Azure/Vercel.

## ElMapita

README no ofrece URL pública concreta. Los nuevos docs/adr/0013-despliegue-iscoutb-dev.md y docs/despliegue-iscoutb-dev.md documentan backend https://elmapita.iscoutb.dev; interfaz móvil Flutter. La documentación fuera de README no se cuenta como URL en README.

## EnAgenda

README conserva URL pública pendiente de asignar y marcadores http://[host-asignado]/health, no URL real.

## GimnasioUTB

API https://gimnasio-utb.iscoutb.dev. No frontend web público documentado.

## InvenTrack

API https://inventrack.iscoutb.dev y API externa https://inventrack-api.onrender.com. README no da URL de frontend.

## LaPlacita

Frontend https://laplacita-app.iscoutb.dev; API https://laplacita-test.iscoutb.dev/api/v1.

## LostVault

Sin URL pública concreta en README. La API externa https://backend-nu-self-91.vercel.app aparece en docs/medicion/s14-medicion-atributos.md, no en README ni dominio institucional.

## PROYECTO_CAMPUSMARKET

Frontend https://campusmarket.iscoutb.dev/app/; API https://campusmarket.iscoutb.dev. Pages/Azure se conservan como históricos.

## PideUtb

Frontend https://pideutb.iscoutb.dev; API https://api-pideutb.iscoutb.dev/docs.

## ROUTB

README:117–118 documenta https://routb.iscoutb.dev y /health como backend; no documenta frontend web independiente.

## Recobra

README:35–37 distingue https://recobra.iscoutb.dev/ (vitrina), /app/ (Flutter Web) y /publicaciones, /health, /health/ready, /metrics (API).

## ShareU

README:141–144 ahora identifica https://shareu.iscoutb.dev y https://api-shareu.iscoutb.dev, pero el propio equipo los registra con HTTP 404 al 16/nov. Es documentación nueva, no comprobación viva de esta revisión.

## Sistema de calificación automática

README:19–21 y 267–269 identifica https://calificacion.iscoutb.dev, https://api-calificacion.iscoutb.dev/health y frontend /revision.txt; conserva alternativas históricas Render, que no sustituyen los endpoints institucionales.

## TAIA

README:9–12 y 118–120 documenta https://taia-sistema.iscoutb.dev como API, /health, /metrics y /docs; Render es alternativa. No equivale a URL frontend web.

## Tienda virtual UTB

README:7 y 150 conserva https://tiendautb-sistema-n0ojjk-fde272-144-24-4-187.sslip.io/; no documenta subdominio iscoutb.dev. URLs localhost son instrucciones locales.

## UTB_TRACKER

Externo: API y Swagger en https://129-80-171-141.nip.io; README menciona iscoutb.dev genéricamente, sin subdominio institucional concreto. Cliente móvil no equivale a frontend web publicado.

## Verifacts

Institucional: frontend https://verifacts.iscoutb.dev; API /analysis (POST), salud /health, Swagger /docs y métricas /metrics en el mismo origen.

## XALD

Externo: API https://xald-backend.onrender.com, salud /health y /docs. README mantiene cliente Android y requiere configurar endpoint/clave localmente; no documenta subdominio iscoutb.dev.

## mapsutb

Externo: frontend Firebase https://mapsutb.web.app y salud /health.json; la métrica histórica se publica en rama metricas, no es una API institucional. README no documenta subdominio iscoutb.dev.

## uniTeam

Externo: frontend https://uniteam-web.duckdns.org y API https://uniteam-api.duckdns.org. La sonda configura uniteam-web.onrender.com y uniteam-api.onrender.com: sus seis fallos no prueban caída de los hosts DuckDNS.

