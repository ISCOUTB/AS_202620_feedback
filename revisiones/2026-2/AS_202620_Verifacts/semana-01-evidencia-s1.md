# Evidencia S1 · Verifacts (Grupo X)

> **Excepción docente**: por decisión del profesor, esta evidencia se evalúa sobre el estado
> actual del repositorio (HEAD `8ded7cf`, 2026-08-23), no sobre el commit al cierre
> (2026-08-10T05:00:00Z), que no existe: el primer commit es del 18-ago. Solo por esta vez.

## Datos

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | HEAD `8ded7cf3f975553a88dd833fd58051ead7965b4d` · 2026-08-23T19:23:38-05:00 (excepción docente) |
| Comandos | `git ls-remote`; clon efímero `--filter=blob:none --no-checkout`; `git ls-tree -r HEAD`; `git show HEAD:…`; `git shortlog -sne HEAD`; `git grep` de secretos; API de colaboradores → 401 sin token |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | `git ls-remote https://github.com/ISCOUTB/AS_202620_Verifacts.git` OK; clon sin autenticación | Cumple | público y con convención; creado tarde (primer commit 2026-08-18) |
| Integrantes del equipo con acceso | API colaboradores → 401 sin token; `git shortlog -sne HEAD`: 1 identidad (`PedroC1213`, 25 commits) | No verificado | el historial solo muestra 1 de 3; hace falta token o sustentación para comprobar acceso |
| Equipo de 3 o 4 personas | EQUIPOS.md declara 3 integrantes | Cumple | Cristian Cardeno · Pedro Castro · Julian Cabeza |
| Ficha del problema con usuarios y alcance | `README.md`: Problema, Objetivo, Alcance; `docs/arc42.md` §1.5-1.6: alcance y usuarios (final, estudiante/docente, analista) | Cumple | — |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | `docs/arc42.md` §1 y `README.md` sin tensiones; `resumen-entrega.pdf` declara una (disponibilidad ante fallos del sitio externo vs escalabilidad) | No cumple | declara una tensión en el PDF, no dos; la ficha del problema no las declara |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | `docs/aspectos.md`: declaración narrativa del aspecto Escalabilidad | No cumple | sin tabla de 8 columnas ni ID |
| `docs/ia.md` iniciado con contenido real | `docs/IA.md`: propósito, estrategia por etapas (reglas → NLP con spaCy → ML con scikit-learn) | Cumple | desviación de nombre (`IA.md`); es estrategia de IA, no registro de uso |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | `docs/arc42.md` archivo único con secciones 1-4 redactadas | No cumple | desviación: no hay `docs/arc42/` con la plantilla de 12 secciones, pero hay contenido real |
| `docs/adr/` y `docs/c4/` creados | `docs/adr/0001-estilo-arquitectonico.md` existe; no hay `docs/c4/` | No cumple | `docs/adr/` sí; el C4 está suelto en `docs/c4-contexto.md` |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `ls-remote` y clon sin autenticación OK | Cumple | — |
| Estructura mínima presente | `git ls-tree -r HEAD`: `docs/arc42.md`, `docs/aspectos.md`, `docs/IA.md`, `docs/adr/`, sin `docs/c4/` | No cumple | `IA.md` en mayúsculas, arc42 en archivo único, sin `docs/c4/` |
| Estado calificado identificable | HEAD `8ded7cf` · 2026-08-23T19:23:38-05:00 (excepción docente) | Cumple | hash y fecha registrados |
| Nombres de ADR según la convención | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | numeración y kebab-case correctos |
| ADR aceptados no reescritos | un solo ADR, sin commits de reescritura | Cumple | estado «Propuesto» |
| `docs/ia.md` al día para la semana | `docs/IA.md`, commit `d42dd18` (2026-08-18) | No cumple | nombre desviado y sin registro de uso (qué se rechazó y por qué) |
| Sin credenciales en el repositorio ni en el historial | `git grep` §9 sin coincidencias, sin `.env` | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: 1 identidad para 3 integrantes | No cumple | solo `PedroC1213` (25 commits); sin atribuir por parecido de nombre |

## Recuento y nota sugerida

4 de 9 criterios Cumple. Propuesta al docente (regla local no publicada): `1 + 4 × (4/9) = 2,8`.

## Hallazgos para la planilla

- Repositorio creado 8 días después del cierre de S1 (excepción docente aplicada).
- 2 de 3 integrantes sin aparición en el historial.
- Estructura desviada: `docs/arc42.md` único, `docs/IA.md`, sin `docs/c4/`.
