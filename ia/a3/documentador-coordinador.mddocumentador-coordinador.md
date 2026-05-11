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


# Code Review 2

## PR revisada
feature/esp-actividades-3-4-5-add-diagrama-actividad3

---

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
1. Que existan diagramas de actividades para los casos de uso 3, 4 y 5.
2. Que cada diagrama tenga archivo `.puml` y `.png`.
3. Que cada diagrama tenga al menos 10 actividades.
4. Que cada diagrama tenga al menos 3 swimlanes.
5. Que incluya decisiones, bifurcaciones o caminos alternativos cuando corresponda.
6. Que los nombres respeten el formato `04-actividad-nombre-caso-uso-03.puml`.
7. Que exista y esté actualizado `diagramas/04-diagramas-actividades/diagramas_de_actividades.md`.
8. Que la documentación IA exista en `ia/a3/esp-actividades-3-4-5.md`.
9. Que el prompt esté en triple backtick.
10. Que incluya archivos de contexto, output, ajustes e iteraciones.
11. Que `changelog.md` registre la PR con formato correcto.
12. Que la PR esté lista para aprobar o requiera cambios.

Respondé en este formato:
- Qué cumple
- Qué falta o está mal
- Ajustes solicitados
- Veredicto final

### Se verifica que

Existen diagramas de actividades para los casos de uso 3, 4 y 5 con archivos .puml y .png.
Cada diagrama cumple con el mínimo de actividades y swimlanes requeridos.
Los diagramas incluyen decisiones, bifurcaciones y caminos alternativos.
La documentación IA está presente y correctamente estructurada.
changelog.md registra correctamente la PR.

### Observaciones detectadas

diagramas_de_actividades.md contiene enlaces rotos para CU 1 y 2.
El índice apunta a archivos .png en lugar de .puml.
El índice mezcla contribuciones de distintos especialistas sin diferenciación clara.

### Ajustes solicitados

Corregir los enlaces del índice para apuntar a archivos .puml.
Resolver o separar las referencias correspondientes a CU 1 y 2.
Mantener organizado el índice por casos de uso o por especialista.

Veredicto: REQUEST CHANGES