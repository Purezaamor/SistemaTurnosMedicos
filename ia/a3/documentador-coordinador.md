# Documentador y Coordinador - Actividad Obligatoria N°3

## Introducción

En la Actividad Obligatoria N°3 se utilizaron herramientas de IA (GitHub Copilot) para asistir en el proceso de revisión técnica de Pull Requests del equipo.

Las revisiones técnicas validaron los siguientes aspectos:
- Validación de estructura de diagramas
- Coherencia UML
- Consistencia documental
- Cumplimiento de convenciones de naming
- Trazabilidad entre artefactos
- Actualización correcta de changelog y README

---

## Code Review 1

### PR revisada

`feature/esp-actividades-3-4-5-add-diagrama-actividad3`

### Prompt utilizado

```text
Actúa como revisor técnico de la materia Diseño Orientado a Objetos.

Analiza la rama/PR `feature/esp-actividades-3-4-5-add-diagrama-actividad3` 
correspondiente al rol Especialista en Diagramas de Actividades - Casos de Uso 3, 4 y 5.

Usa como contexto:
- anexos/introduccion.md
- diagramas/02-casos-de-uso/
- diagramas/03-escenarios-casos-de-uso/
- diagramas/04-diagramas-actividades/
- ia/a3/esp-actividades-3-4-5.md
- changelog.md

Valida específicamente:
- Que existan diagramas de actividades para los casos de uso 3, 4 y 5.
- Que cada diagrama tenga archivos `.puml` y `.png`.
- Que cada diagrama contenga al menos 10 actividades.
- Que cada diagrama incluya al menos 3 swimlanes.
- Que incluya decisiones, bifurcaciones o caminos alternativos.
- Que exista y esté actualizado `diagramas/04-diagramas-actividades/diagramas_de_actividades.md`.
- Que exista documentación IA completa.
- Que el changelog registre correctamente la PR.

Responde en este formato:
- Qué cumple
- Qué falta o está mal
- Ajustes solicitados
- Veredicto final
```

### Resultados de la revisión

#### Qué cumple
- Existen diagramas de actividades para los casos de uso 3, 4 y 5 con archivos `.puml` y `.png`.
- Cada diagrama incluye al menos 10 actividades.
- Cada diagrama incluye al menos 3 swimlanes.
- Los diagramas incluyen decisiones, bifurcaciones y caminos alternativos.
- Los nombres de archivos respetan el formato requerido.
- Existe documentación IA en `esp-actividades-3-4-5.md`.
- El prompt está documentado correctamente utilizando triple backtick.
- Se incluyen archivos de contexto, outputs, ajustes e iteraciones.
- El changelog registra la PR.

#### Qué falta o está mal
- No existe el archivo `diagramas/04-diagramas-actividades/diagramas_de_actividades.md`.
- La entrada en changelog menciona incorrectamente casos de uso 1 y 2 en lugar de 3, 4 y 5.

#### Ajustes solicitados
- Crear y actualizar `diagramas/04-diagramas-actividades/diagramas_de_actividades.md`.
- Corregir la entrada correspondiente en `changelog.md`.

#### Veredicto
**REQUEST CHANGES**

---

## Code Review 2

### PR revisada

`feature/esp-actividades-3-4-5-add-diagrama-actividad3`

### Prompt utilizado

```text
Actúa como revisor técnico de la materia Diseño Orientado a Objetos.

Analiza la rama/PR `feature/esp-actividades-3-4-5-add-diagrama-actividad3` 
correspondiente al rol Especialista en Diagramas de Actividades - Casos de Uso 3, 4 y 5.

Usa como contexto:
- anexos/introduccion.md
- diagramas/02-casos-de-uso/
- diagramas/03-escenarios-casos-de-uso/
- diagramas/04-diagramas-actividades/
- ia/a3/esp-actividades-3-4-5.md
- changelog.md

Valida específicamente:
1. Que existan diagramas de actividades para los casos de uso 3, 4 y 5.
2. Que cada diagrama tenga archivos `.puml` y `.png`.
3. Que cada diagrama contenga al menos 10 actividades.
4. Que cada diagrama incluya al menos 3 swimlanes.
5. Que incluya decisiones, bifurcaciones o caminos alternativos cuando corresponda.
6. Que los nombres respeten el formato `04-actividad-nombre-caso-uso-03.puml`.
7. Que exista y esté actualizado `diagramas/04-diagramas-actividades/diagramas_de_actividades.md`.
8. Que la documentación IA exista en `ia/a3/esp-actividades-3-4-5.md`.
9. Que el prompt esté en triple backtick.
10. Que incluya archivos de contexto, outputs, ajustes e iteraciones.
11. Que `changelog.md` registre la PR con formato correcto.
12. Que la PR esté lista para aprobar o requiera cambios.

Responde en este formato:
- Qué cumple
- Qué falta o está mal
- Ajustes solicitados
- Veredicto final
```

### Observaciones detectadas

#### Qué cumple
- Existen diagramas de actividades para los casos de uso 3, 4 y 5 con archivos `.puml` y `.png`.
- Cada diagrama cumple con el mínimo de actividades y swimlanes requeridos.
- Los diagramas incluyen decisiones, bifurcaciones y caminos alternativos.
- La documentación IA está presente y correctamente estructurada.
- El changelog registra correctamente la PR.

#### Qué falta o está mal
- El archivo `diagramas_de_actividades.md` contiene enlaces rotos para CU 1 y 2.
- El índice apunta a archivos `.png` en lugar de `.puml`.
- El índice mezcla contribuciones de distintos especialistas sin diferenciación clara.

#### Ajustes solicitados
- Corregir los enlaces del índice para que apunten a archivos `.puml`.
- Resolver o separar las referencias correspondientes a CU 1 y 2.
- Organizar el índice diferenciando por casos de uso o por especialista.

#### Veredicto
**REQUEST CHANGES**

---

## Code Review 3

### PR revisada

`feature/esp-actividades-1-2-add-diagrama-actividad-1`

### Prompt utilizado

```text
Actúa como revisor técnico de la materia Diseño Orientado a Objetos.

Analiza la rama/PR `feature/esp-actividades-1-2-add-diagrama-actividad-1` 
correspondiente al rol Especialista en Diagramas de Actividades - Casos de Uso 1 y 2.

Usa como contexto:
- anexos/introduccion.md
- diagramas/02-casos-de-uso/
- diagramas/03-escenarios-casos-de-uso/
- diagramas/04-diagramas-actividades/
- ia/a3/esp-actividades-1-2.md
- changelog.md

Valida específicamente:
1. Que existan diagramas de actividades para los casos de uso 1 y 2.
2. Que cada diagrama tenga archivos `.puml` y `.png`.
3. Que cada diagrama contenga al menos 10 actividades.
4. Que cada diagrama incluya al menos 3 swimlanes.
5. Que incluya decisiones, bifurcaciones o caminos alternativos.
6. Que los nombres respeten el formato:
   - `04-actividad-registrar-turno-medico-01.puml`
   - `04-actividad-reprogramar-turno-existente-02.puml`
7. Que exista y esté actualizado `diagramas/04-diagramas-actividades/diagramas_de_actividades.md`.
8. Que los enlaces del índice apunten a archivos `.puml`.
9. Que la documentación IA exista en `ia/a3/esp-actividades-1-2.md`.
10. Que el prompt esté documentado utilizando triple backtick.
11. Que incluya contexto, outputs, ajustes e iteraciones.
12. Que `changelog.md` registre correctamente la PR.
13. Que la PR esté lista para aprobar o requiera cambios.

Responde en este formato:
- Qué cumple
- Qué falta o está mal
- Ajustes solicitados
- Veredicto final
```

### Observaciones detectadas

#### Qué cumple
- Existen diagramas de actividades para los casos de uso 1 y 2.
- Los nombres de archivos respetan el formato requerido.
- Ambos diagramas cumplen con el mínimo de actividades solicitado.
- Cada diagrama incluye 3 swimlanes.
- Los diagramas incluyen decisiones y caminos alternativos.
- Existe `diagramas_de_actividades.md` correctamente organizado.
- Los enlaces del índice apuntan a archivos `.puml`.
- Existe documentación IA completa en `esp-actividades-1-2.md`.
- Los diagramas están alineados con los escenarios documentados.

#### Qué falta o está mal
- No existen los archivos `.png` correspondientes a ambos diagramas.
- El output del Caso de Uso 2 no está envuelto en triple backtick.
- El changelog utiliza `PR: [#???]` en lugar del número de PR correcto.

#### Ajustes solicitados
- Generar y agregar los archivos PNG:
  - `04-actividad-registrar-turno-medico-01.png`
  - `04-actividad-reprogramar-turno-existente-02.png`
- Corregir el bloque de código del output del CU 2 utilizando triple backtick.
- Actualizar la referencia de PR en changelog con el número `#118`.

#### Veredicto
**REQUEST CHANGES**

---

## Code Review 4

### PR revisada

`feature/esp-actividades-1-2-add-diagrama-actividad-1`

### Motivo de la segunda revisión

Se realizó una nueva revisión técnica después de que el autor aplicara las correcciones solicitadas en la revisión anterior:
- Incorporación de archivos `.png`
- Corrección de referencias en `changelog.md`
- Actualización de documentación IA

### Prompt utilizado

```text
Actúa como revisor técnico de la materia Diseño Orientado a Objetos.

Revisa nuevamente la PR `feature/esp-actividades-1-2-add-diagrama-actividad-1` luego de las correcciones realizadas.

Valida:
- existencia de archivos `.puml` y `.png`,
- swimlanes,
- actividades mínimas,
- bifurcaciones,
- índice actualizado,
- documentación IA,
- uso de triple backticks,
- y registro correcto en changelog.md.

Responde:
- Qué cumple
- Qué falta o está mal
- Ajustes solicitados
- Veredicto final
```

### Observaciones detectadas

#### Qué cumple
- Existen diagramas de actividades para los casos de uso 1 y 2.
- Cada diagrama posee archivos `.puml` y `.png`.
- Ambos diagramas cumplen con el mínimo de actividades requerido.
- Los diagramas utilizan correctamente al menos 3 swimlanes.
- Incluyen decisiones, bifurcaciones y caminos alternativos.
- El índice `diagramas_de_actividades.md` se encuentra actualizado.
- Los enlaces del índice apuntan a archivos `.puml`.
- La documentación IA incluye contexto, outputs, ajustes e iteraciones.
- `changelog.md` registra correctamente la PR #118.

#### Qué falta o está mal
- El prompt documentado en `ia/a3/esp-actividades-1-2.md` no está encerrado dentro de un bloque de código utilizando triple backticks.

#### Ajustes solicitados
- Encerrar el prompt utilizado dentro de un bloque de código Markdown utilizando triple backticks para mantener consistencia con el formato solicitado.

#### Veredicto
**REQUEST CHANGES**

---

## Code Review 5

### PR revisada

`feature/esp-actividades-1-2-add-diagrama-actividad-1`

### Motivo de la tercera revisión

Se realizó una revisión final después de que el autor corrigiera todas las observaciones detectadas en revisiones anteriores:
- Incorporación de archivos `.png`
- Corrección de prompts utilizando triple backticks
- Actualización del changelog
- Validación final de diagramas e índice de actividades

### Prompt utilizado

```text
Actúa como revisor técnico de la materia Diseño Orientado a Objetos.

Revisa nuevamente la PR `feature/esp-actividades-1-2-add-diagrama-actividad-1` luego de las correcciones finales realizadas.

Valida:
- diagramas de actividades CU 1 y 2,
- archivos `.puml` y `.png`,
- swimlanes,
- actividades mínimas,
- bifurcaciones,
- índice actualizado,
- documentación IA,
- triple backticks,
- changelog,
- y estado final de aprobación.

Responde:
- Qué cumple
- Qué falta o está mal
- Ajustes solicitados
- Veredicto final
```

### Observaciones detectadas

#### Qué cumple
- Existen diagramas de actividades para los casos de uso 1 y 2.
- Cada diagrama posee archivos `.puml` y `.png`.
- Ambos diagramas cumplen con el mínimo de actividades requerido.
- Los diagramas utilizan correctamente al menos 3 swimlanes.
- Incluyen decisiones, bifurcaciones y caminos alternativos.
- El índice `diagramas_de_actividades.md` se encuentra actualizado.
- Los enlaces del índice apuntan correctamente a archivos `.puml`.
- La documentación IA incluye prompts, outputs, ajustes e iteraciones.
- Los prompts y outputs están correctamente documentados utilizando triple backticks.
- El archivo `changelog.md` registra correctamente la PR #118.

#### Qué falta o está mal
- No se detectaron problemas pendientes.

#### Ajustes solicitados
- No se requieren ajustes adicionales.

#### Veredicto
**APPROVE**

---

## Code Review 6

### PR revisada

`feature/esp-actividades-3-4-5-add-diagrama-actividad3`

### Motivo de la revisión final

Se realizó una validación final luego de que el autor corrigiera las observaciones detectadas en revisiones anteriores:
- Corrección de enlaces en `diagramas_de_actividades.md`
- Validación de archivos `.puml` y `.png`
- Revisión de documentación IA
- Verificación de consistencia general de los diagramas

### Prompt utilizado

```text
Actúa como revisor técnico de la materia Diseño Orientado a Objetos.

Revisa nuevamente la PR `feature/esp-actividades-3-4-5-add-diagrama-actividad3` luego de las correcciones finales realizadas.

Valida:
- diagramas de actividades CU 3, 4 y 5,
- archivos `.puml` y `.png`,
- swimlanes,
- actividades mínimas,
- decisiones y bifurcaciones,
- documentación IA,
- changelog,
- índice actualizado,
- y estado final de aprobación.

Responde:
- Qué cumple
- Qué falta o está mal
- Ajustes solicitados
- Veredicto final
```

### Observaciones detectadas

#### Qué cumple
- Existen diagramas de actividades para los casos de uso 3, 4 y 5.
- Todos los diagramas poseen archivos `.puml` y `.png`.
- Los diagramas cumplen con el mínimo de actividades requerido.
- Los diagramas utilizan correctamente al menos 3 swimlanes.
- Incluyen decisiones, bifurcaciones y caminos alternativos.
- La documentación IA se encuentra correctamente estructurada.
- El prompt está documentado utilizando triple backticks.
- `changelog.md` registra correctamente la PR #124.
- El índice `diagramas_de_actividades.md` apunta correctamente a archivos `.puml`.

#### Qué falta o está mal
- No se detectaron problemas pendientes.

#### Ajustes solicitados
- No se requieren ajustes adicionales.

#### Veredicto
**APPROVE**


## Code Review 7

### PR revisada

`feature/esp-secuencia-add-diagrama-secuencia-1`

### Motivo de la revisión final

Se realizó una validación completa de los diagramas de secuencia y de toda la documentación asociada correspondiente al rol Especialista en Diagramas de Secuencia.

La revisión incluyó:

* Validación de los 5 diagramas de secuencia.
* Verificación de archivos `.puml` y `.png`.
* Revisión de participantes e interacciones UML.
* Validación de mensajes en `camelCase`.
* Verificación de operaciones `create` y `destroy`.
* Revisión de documentación IA.
* Validación de índice de diagramas.
* Verificación de `changelog.md`.
* Revisión de estructura general y naming conventions.

### Prompt utilizado

```text
Actúa como revisor técnico de la materia Diseño Orientado a Objetos.

Revisa la rama `feature/esp-secuencia-add-diagrama-secuencia-1`.

Valida:
- estructura de carpetas,
- diagramas de secuencia,
- archivos `.puml` y `.png`,
- cantidad mínima de participantes,
- cantidad mínima de mensajes,
- nomenclatura camelCase,
- uso correcto de create/destroy,
- coherencia cronológica,
- documentación IA,
- changelog,
- índice de diagramas,
- y consistencia general de la entrega.

Responde:
- Qué cumple
- Qué falta o está mal
- Ajustes solicitados
- Veredicto final
```

### Observaciones detectadas

#### Qué cumple

* Existe la carpeta `diagramas/05-diagramas-secuencia/`.
* Los 5 diagramas de secuencia requeridos están presentes en formato `.puml`.
* Cada diagrama posee su correspondiente exportación `.png`.
* Todos los diagramas cumplen con el mínimo de participantes requerido.
* Todos los diagramas cumplen con el mínimo de interacciones/mensajes requerido.
* Los mensajes utilizan correctamente nomenclatura `camelCase`.
* Se utilizan correctamente actores y participantes UML.
* Las operaciones `create` y `destroy` fueron implementadas correctamente donde corresponde.
* Los flujos cronológicos son coherentes con los escenarios funcionales.
* La sintaxis PlantUML es válida en todos los diagramas.
* Existe un índice `diagramas_de_secuencias.md` correctamente estructurado.
* Los enlaces del índice apuntan correctamente a archivos `.puml` y `.png`.
* Existe documentación IA completa en `esp-secuencia.md`.
* La documentación IA incluye prompts, contexto, ajustes, iteraciones y validaciones.
* `changelog.md` registra correctamente los cambios realizados.
* La nomenclatura de archivos y rama respeta las convenciones establecidas.

#### Qué falta o está mal

* No se detectaron problemas pendientes.

#### Ajustes solicitados

* No se requieren ajustes obligatorios.
* Como mejora opcional, podría agregarse documentación para regenerar los archivos `.png`.

#### Veredicto

**APPROVE**


