# Documentador y Coordinador - Actividad Obligatoria N°3

## Introducción

Durante la Actividad Obligatoria N°3 se utilizaron herramientas de IA (GitHub Copilot) para asistir el proceso de revisión técnica de Pull Requests del equipo.

Las revisiones se enfocaron en:
- validación de estructura
- coherencia UML
- consistencia documental
- cumplimiento de naming
- trazabilidad entre artefactos
- actualización de changelog y README

---

# Code Review 1

## PR revisada
feature/esp-actividades-3-4-5-add-diagrama-actividad3

## Prompt utilizado

```text
Actuá como revisor técnico de la materia Diseño Orientado a Objetos.

Analizá la rama/PR `feature/esp-actividades-3-4-5-add-diagrama-actividad3` correspondiente al rol Especialista en Diagramas de Actividades - Casos de Uso 3, 4 y 5.

Usá como contexto:
- anexos/introduccion.md
- diagramas/02-casos-de-uso/
- diagramas/03-escenarios-casos-de-uso/
- diagramas/04-diagramas-actividades/
- ia/a3/esp-actividades-3-4-5.md
- changelog.md

Validá específicamente:
- Que existan diagramas de actividades para los casos de uso 3, 4 y 5.
- Que cada diagrama tenga archivo `.puml` y `.png`.
- Que cada diagrama tenga al menos 10 actividades.
- Que cada diagrama tenga al menos 3 swimlanes.
- Que incluya decisiones, bifurcaciones o caminos alternativos.
- Que exista y esté actualizado `diagramas/04-diagramas-actividades/diagramas_de_actividades.md`.
- Que exista documentación IA completa.
- Que el changelog registre correctamente la PR.

Respondé en este formato:
- Qué cumple
- Qué falta o está mal
- Ajustes solicitados
- Veredicto final

## Observaciones detectadas

### Qué cumple
- Existen diagramas de actividades para los casos de uso 3, 4 y 5 con archivos `.puml` y `.png`.
- Cada diagrama incluye al menos 10 actividades.
- Cada diagrama incluye al menos 3 swimlanes.
- Los diagramas incluyen decisiones, bifurcaciones y caminos alternativos.
- Los nombres respetan el formato requerido.
- Existe documentación IA en `esp-actividades-3-4-5.md`.
- El prompt se encuentra documentado utilizando triple backtick.
- Se incluyen archivos de contexto, output, ajustes e iteraciones.
- `changelog.md` registra la PR.

### Qué falta o está mal
- No existe `diagramas/04-diagramas-actividades/diagramas_de_actividades.md`.
- La entrada de `changelog.md` menciona incorrectamente casos de uso 1 y 2 en lugar de 3, 4 y 5.

### Ajustes solicitados
- Crear y actualizar `diagramas/04-diagramas-actividades/diagramas_de_actividades.md`.
- Corregir la entrada correspondiente en `changelog.md`.

### Veredicto publicado
Request Changes

