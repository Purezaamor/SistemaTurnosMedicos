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

### PR Revisada #124
- Rama: `feature/esp-actividades-3-4-5-add-diagrama-actividad3`

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

## Iteración 1:

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

## Iteración 2:

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


## Iteración 3:

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


## Code Review 2

### PR revisada #118

- Rama: `feature/esp-actividades-1-2-add-diagrama-actividad-1`

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
## Iteración 1:

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

## Iteración 2:

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

## Iteración 3:

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

## Code Review 3 POST-MERGE

### PR revisada #120

- Rama: `feature/doc-coord-update-readme-a3`

### Prompt utilizado

```
Actúa como revisor técnico senior de la materia Diseño Orientado a Objetos.

Realiza una revisión técnica retrospectiva de una Pull Request ya mergeada. PR #120

Analiza los artefactos incorporados por la PR y valida consistencia técnica, documental y cumplimiento de convenciones.

INSTRUCCIONES IMPORTANTES

- Evalúa únicamente problemas reales observables
- No inventes hallazgos hipotéticos
- Enumera cada observación de forma independiente
- Sé técnico, concreto y objetivo
- Considera que se trata de una revisión post-merge

Valida especialmente:

- Estructura de carpetas
- Existencia y nomenclatura de archivos
- Consistencia UML
- Coherencia entre diagramas y escenarios
- Correctitud de documentación IA
- Uso correcto de formato Markdown
- Actualización de changelog
- Trazabilidad entre artefactos

Para cada hallazgo usa EXACTAMENTE esta estructura:

==================================================

HALLAZGO #<número>

Archivo:

Tipo de problema:
(documentación | UML | nomenclatura | trazabilidad | consistencia | otro)

Severidad:
(baja | media | alta)

Explicación técnica:
Por qué representa una inconsistencia real.

Sugerencia de mejora:
Corrección concreta recomendada.

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia
[ ] Rechazar sugerencia

Justificación del revisor humano:

---
Al finalizar agrega:

RESUMEN GENERAL DE LA PR

- Qué cumple correctamente
- Riesgos detectados
- Calidad general de la entrega

VEREDICTO TÉCNICO RETROSPECTIVO

APPROVE / OBSERVACIONES POST-MERGE / REQUIERE AJUSTES DOCUMENTALES

No completes la sección "DECISIÓN DEL REVISOR HUMANO".
Debe quedar vacía para edición manual.
```

### Resultados de la IA

### REVISIÓN TÉCNICA RETROSPECTIVA - PR #120
- PR Analizada: feature/doc-coord-update-readme-a3 (#120)
- Rama: feature/doc-coord-update-readme-a3 → develop
- Autor: @nachonervi-design (Documentador y Coordinador)
- Estado: MERGEADA (Commit: f82ecff)
- Fecha de merge: 2026-05-07

==================================================

### HALLAZGO #1

Archivo:
changelog.md:12

Tipo de problema:
trazabilidad

Severidad:
media

### Explicación técnica:

La entrada para PR #120 en changelog.md utiliza una descripción muy genérica: "Actualización de documentación, navegación e integración de componentes de la Actividad Obligatoria N°3". Contrasta con otras PRs de coordinación en la misma release (PR #124, PR #118, PR #130) que especifican archivos, funcionalidades y cambios concretos. Más importantemente, no menciona que agregó el archivo documentador-coordinador.md, que es un artefacto de 458 líneas con revisiones técnicas críticas. Esto afecta la trazabilidad de qué artefactos fueron introducidos por esta PR.

### Sugerencia de mejora:

Actualizar la entrada en changelog.md para incluir:


- [feature/doc-coord-update-readme-a3] Actualización de documentación A3:   correcciones de rutas IA (ia/a2/primer-parcial/ → ia/primer-parcial/),   actualización de README con secciones de Diagramas de Actividades y Secuencia,   incorporación de ia/a3/documentador-coordinador.md (documentación de reviews técnicos   de PR #124, #118, #130) e índice en diagramasUML.md.   PR: #120 — @nachonervi-design (Documentador y Coordinador)

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia

[ ] Rechazar sugerencia

Justificación del revisor humano:

==================================================

### HALLAZGO #2

Archivo:
- `documentador-coordinador.md`:283 (Iteración 3, Code Review 1)

Tipo de problema:
consistencia | documentación

Severidad:
media

### Explicación técnica:

El documento documentador-coordinador.md registra en su Iteración 3 (Code Review 1, PR #124) que "El índice diagramas_de_actividades.md apunta correctamente a archivos .puml" como condición de aprobación.

Sin embargo, la realidad actual es que el índice apunta a archivos .png, no .puml.

Verificación:

diagramas_de_actividades.md - Todos los 5 enlaces apuntan a archivos .png
Este cambio fue introducido explícitamente por PR #137 (fix/reordenar-archivos-diagramas), que describe: "Correcciones de archivos diagramas_de_actividades.md y README.md, para que apunten a los archivos .png y no a los .puml."

Esto genera una discrepancia entre la conclusión documentada en el Veredicto APPROVE y la implementación actual post-merge.

### Sugerencia de mejora:

Agregar una sección de "Notas Post-Merge" o "Cambios Posteriores" al documentador-coordinador.md que registre que la PR #137 modificó intencionalmente los índices para apuntar a .png en lugar de .puml, documentando esta decisión de diseño.

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia

[ ] Rechazar sugerencia

Justificación del revisor humano:

==================================================

### HALLAZGO #3

Archivo:
README.md (secciones agregadas por PR #120)

Tipo de problema:
Trazabilidad | Documentación

Severidad:
Baja

### Explicación técnica:

Aunque este hallazgo es de naturaleza post-merge, es relevante para la evaluación retrospectiva: La PR #120 agregó dos secciones completas al README:

"## Diagramas de Actividades" (5 enlaces a archivos .puml)
"## Diagramas de Secuencia" (5 enlaces a archivos .puml)
Estas secciones fueron posteriormenteremovidas o consolidadas en la PR #141 (fix/readme). El README actual es significativamente más simple que lo que la PR #120 propuso, manteniendo solo la estructura original sin las nuevas secciones expandidas.

Esto no es necesariamente un problema de la PR #120, pero indica que la decisión de agregar secciones extensas al README fue revisada (posiblemente por feedback del profesor o decisión de diseño). La trazabilidad de esta decisión no está documentada en el changelog o en comentarios de PR.

### Sugerencia de mejora:

Si la remoción de esas secciones fue intencional (decisión de diseño), registrar en changelog.md la PR que las removió (PR #141) con justificación explícita. Si fue accidental, restaurar las secciones o documentar por qué el acceso a diagramas debe hacerse solo a través del índice centralizado en diagramasUML.md.

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia

[ ] Rechazar sugerencia

Justificación del revisor humano:

==================================================

### HALLAZGO #4

Archivo:
- `documentador-coordinador.md`

Tipo de problema:
Trazabilidad

Severidad:
Baja

### Explicación técnica:

El documento documentador-coordinador.md fue creado por la PR #120 como artefacto principal de esta PR. Sin embargo, el propio documento no incluye una sección de revisión o validación de sus propios cambios (PR #120).

El documento registra 3 Code Reviews completos (PR #124, #118, #130), cada uno con múltiples iteraciones y análisis técnico exhaustivo. Por consistencia, podría esperarse que incluya una sección que documente la validación del propio archivo y los cambios que introdujo.

Nota: Esto puede no ser requerido según las especificaciones del rol, pero se menciona por completitud de trazabilidad.

### Sugerencia de mejora:

(Opcional) Agregar una sección "Code Review 0" o "Autorevisión de PR #120" que incluya:

Validación de que las rutas IA fueron corregidas correctamente
Verificación de que el changelog registra la PR
Confirmación de que los archivos IA contextuales existen
Validación de formato y estructura de este documento
DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia

[ ] Rechazar sugerencia

Justificación del revisor humano:

==================================================

### HALLAZGO #5

Archivo:
- `diagramasUML.md`

Tipo de problema:
Nomenclatura | Consistencia

Severidad:
Baja

### Explicación técnica:

El archivo diagramasUML.md fue actualizado por la PR #120 para incluir enlaces a las nuevas secciones de actividades y secuencias:


- [Diagramas de Actividades](04-diagramas-actividades/diagramas_de_actividades.md)- [Diagramas de Secuencia](05-diagramas-secuencia/diagramas_de_secuencias.md)
Observación: Los títulos de los enlaces no son idénticos en formato:

"Diagramas de Actividades" (minúsculas después del prefijo)
"Diagramas de Secuencia" (minúsculas después del prefijo)
Comparado con las secciones anteriores:

"Diagramas de Casos de Uso" (consistent)
"Escenarios de Casos de Uso" (consistent)
Los enlaces en PR #120 son consistentes con el patrón existente, por lo que no es un problema. Sin embargo, se registra como observación de que la convención de nomenclatura en índices utiliza "Diagramas de [Tipo]" como patrón uniforme.

### Sugerencia de mejora:

No aplica - la implementación es correcta y consistente.

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia

[ ] Rechazar sugerencia

Justificación del revisor humano:

==================================================

### RESUMEN GENERAL DE LA PR

✅ Qué cumple correctamente

- Correcciones de rutas: Las correcciones de rutas de archivos IA (ia/a2/primer-parcial/ → ia/primer-parcial/) se aplicaron correctamente en README.md
- Creación de documentación IA: El archivo documentador-coordinador.md fue creado exitosamente con 3 
- Code Reviews bien estructurados
- Estructura de diagramas: Se integraron correctamente referencias a carpetas de diagramas de actividades y secuencia en el índice central
- Trazabilidad de versiones: Se registró correctamente en changelog.md la PR #120
- Links y referencias: Los enlaces en diagramasUML.md apuntan correctamente a índices existentes
- Formato de documentación IA: Los prompts están documentados con triple backticks, contexto está presente, y las iteraciones son claras

⚠️ Riesgos detectados

- Trazabilidad incompleta en changelog: La descripción de PR #120 no menciona el archivo crítico documentador-coordinador.md, lo que podría causar confusión sobre el alcance de los cambios
- Consistencia post-merge: La decisión de cambiar índices de .puml a .png (PR #137) generó una discrepancia con lo documentado en el Veredicto APPROVE, sin anotación en el documento de revisión
- Decisiones de diseño no documentadas: La remoción de secciones del README (PR #141) no está registrada en el histórico con justificación clara

📊 Calidad general de la entrega

Calidad Técnica: ✅ Buena

Los archivos de diagramas existen y son válidos
La estructura de carpetas es correcta
Los índices funcionan correctamente
Calidad Documental: ⚠️ Media-Alta

La documentación de revisión es exhaustiva y bien estructurada. Sin embargo, la trazabilidad en changelog es incompleta.

La documentación interna de cambios post-merge está ausente.

Cumplimiento de Convenciones: ✅ Correcto

Nomenclatura de archivos es consistente
Formato de markdown es correcto
Estructura de enlaces es uniforme

VEREDICTO TÉCNICO RETROSPECTIVO
OBSERVACIONES POST-MERGE

### Justificación:

La PR #120 incorporó artefactos válidos y correctamente estructurados (documentador-coordinador.md, actualizaciones de índices, correcciones de rutas). Sin embargo, detecta:

Trazabilidad incompleta - El changelog no refleja completamente los archivos incorporados
Inconsistencia documentada - Las conclusiones de revisión (archivos .puml) fueron contradictadas por cambios posteriores (PR #137 → .png) sin anotación
Decisiones posteriores no rastreadas - La remoción de secciones del README (PR #141) carece de documentación clara
Estos hallazgos no invalidan la calidad técnica de la PR #120 (los diagramas existen, los índices funcionan), pero señalan oportunidades de mejora en documentación de trazabilidad y consistencia post-merge.

## Code Review 4 POST-MERGE
### PR revisada #130

- Rama: `feature/esp-secuencia-add-diagrama-secuencia-1`

### Prompt utilizado

```
Actúa como revisor técnico senior de la materia Diseño Orientado a Objetos.

Realiza una revisión técnica retrospectiva de una Pull Request ya mergeada. PR #130

Analiza los artefactos incorporados por la PR y valida consistencia técnica, documental y cumplimiento de convenciones.

INSTRUCCIONES IMPORTANTES

- Evalúa únicamente problemas reales observables
- No inventes hallazgos hipotéticos
- Enumera cada observación de forma independiente
- Sé técnico, concreto y objetivo
- Considera que se trata de una revisión post-merge

Valida especialmente:

- Estructura de carpetas
- Existencia y nomenclatura de archivos
- Consistencia UML
- Coherencia entre diagramas y escenarios
- Correctitud de documentación IA
- Uso correcto de formato Markdown
- Actualización de changelog
- Trazabilidad entre artefactos

Para cada hallazgo usa EXACTAMENTE esta estructura:

==================================================

HALLAZGO #<número>

Archivo:

Tipo de problema:
(documentación | UML | nomenclatura | trazabilidad | consistencia | otro)

Severidad:
(baja | media | alta)

Explicación técnica:
Por qué representa una inconsistencia real.

Sugerencia de mejora:
Corrección concreta recomendada.

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia
[ ] Rechazar sugerencia

Justificación del revisor humano:

---
Al finalizar agrega:

RESUMEN GENERAL DE LA PR

- Qué cumple correctamente
- Riesgos detectados
- Calidad general de la entrega

VEREDICTO TÉCNICO RETROSPECTIVO

APPROVE / OBSERVACIONES POST-MERGE / REQUIERE AJUSTES DOCUMENTALES

No completes la sección "DECISIÓN DEL REVISOR HUMANO".
Debe quedar vacía para edición manual.
```
### Resultados de la IA

He repasado los artefactos de la PR #130 y a continuación presento los hallazgos observables y el resumen final.

==================================================

### HALLAZGO #1

Archivo:
`05-secuencia-agendar-turno-flujo-principal-01.puml`

Tipo de problema:
UML

Severidad:
Media

### Explicación técnica:
El PlantUML contiene una instanciación duplicada de la notificación: aparecen dos mensajes Servicio -> Notif: new Notif(notificacionID, "turnoAgendado") y un único create Notif. Esto produce una inconsistencia en el flujo de creación de objetos (duplicación de mensaje de creación), y puede inducir a error al interpretar el ciclo de vida del objeto Notif o al generar la representación PNG.

### Sugerencia de mejora:

Eliminar la línea duplicada y dejar una única secuencia correcta: primero el mensaje que solicita la creación con parámetros (o create Notif seguido por la inicialización), por ejemplo:

Servicio -> Notif: new Notif(notificacionID, "turnoAgendado")
create Notif
O alternativamente:
create Notif
Notif -> Notif: enviarNotificacion(...)
Asegurar que solo exista una invocación de creación y que los parámetros estén en la misma línea que la creación/mensaje.
DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia
[ ] Rechazar sugerencia

Justificación del revisor humano:

### HALLAZGO #2

Archivo:
- `diagramas_de_secuencias.md`

Tipo de problema:
Consistencia

Severidad:
⚠️ Media

### Explicación técnica:

- El índice de Diagramas de Secuencia enlaza a archivos .puml, mientras que el índice de Diagramas de Actividades ([diagramas/04-diagramas-actividades/diagramas_de_actividades.md]) enlaza a las versiones .png. 

- En el repositorio existen ambos formatos (.puml y .png) para cada diagrama de secuencia; la inconsistencia en la convención de enlace (puml vs png) resulta en una experiencia de navegación y presentación no uniforme y contradice cambios previos que estandarizaron índices hacia .png para visualización estática.

### Sugerencia de mejora:

- Estandarizar la política de índices: actualizar diagramas_de_secuencias.md para apuntar a los archivos .png (p. ej. 05-secuencia-agendar-turno-flujo-principal-01.png) para consistencia con 04-diagramas-actividades. Alternativamente, documentar explícitamente en un README/índice la decisión de enlazar a .puml (si se prefiere editar fuente PlantUML) y aplicar la misma regla a todos los índices.

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia
[ ] Rechazar sugerencia

Justificación del revisor humano:

## HALLAZGO #3

Archivo:

- `diagramas_de_secuencias.md`
- `05-secuencia-consultar-agenda-medica-flujo-principal-05.puml`
Tipo de problema:
Consistencia | Trazabilidad

Severidad:
⚠️ Media

### Explicación técnica:

- En diagramas_de_secuencias.md la entrada para el diagrama 05 se describe como "Consultar Agenda Medica 05 - Visualizar Agenda Medica 04 - Ver Agenda - Flujo Alterno", mientras que el título interno del archivo 05-secuencia-consultar-agenda-medica-flujo-principal-05.puml es "Consultar Agenda Médica (Flujo Principal)". Hay una discrepancia observable entre el descriptor del índice (indica "Flujo Alterno") y el título real del diagrama (indica "Flujo Principal"), lo que puede confundir al consumidor del artefacto sobre qué flujo está modelado y dificulta la trazabilidad entre escenario/documentación y diagrama.

### Sugerencia de mejora:

- Harmonizar la etiqueta: corregir el texto en diagramas_de_secuencias.md o el título dentro del .puml para que ambos indiquen el mismo flujo (si el diagrama modela un flujo alterno, renombrar el título del .puml a "Flujo Alterno"; si modela el flujo principal, corregir la descripción en el índice). Además, actualizar cualquiera de los escenarios/MD asociados si el flujo real difiere del esperado.

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia
[ ] Rechazar sugerencia

Justificación del revisor humano:

### RESUMEN GENERAL DE LA PR

✅ Qué cumple correctamente:

- Los 5 diagramas de secuencia están presentes en 05-diagramas-secuencia en formatos .puml y .png.
- La documentación IA asociada (esp-secuencia.md) existe y documenta objetivos, prompts, iteraciones y convenciones de notación.
- changelog.md registra la PR #130 y existe trazabilidad básica hacia el conjunto de artefactos añadidos.
- Los .puml muestran uso de fragmentos alt, create/destroy y mensajes con parámetros en camelCase según las convenciones del proyecto.

⚠️ Riesgos detectados:

- Inconsistencias de enlace (puml vs png) pueden causar confusión al navegar la documentación (riesgo medio para la usabilidad de la entrega).

- Discrepancia en el etiquetado de flujo (índice vs título del diagrama) afecta la trazabilidad entre escenario y diagrama (riesgo medio para revisión funcional).
- Duplicación de mensaje de creación en el diagrama de agendar turno puede inducir a una interpretación errónea del ciclo de vida del objeto (riesgo medio para entendimiento técnico).

📊 Calidad general de la entrega

Calidad técnica: buena — diagramas completos y detallados, convenciones de notación aplicadas.

Calidad documental: sólida en contenidos IA y prompts; mejora en detalles de trazabilidad y consistencia de índices.


## Code Review 5 POST-MERGE
### PR revisada #137

- Rama: `fix/reordenar-archivos-diagramas`

### Prompt utilizado  


```
Actúa como revisor técnico senior de la materia Diseño Orientado a Objetos.

Realiza una revisión técnica retrospectiva de una Pull Request ya mergeada. PR #137

Analiza los artefactos incorporados por la PR y valida consistencia técnica, documental y cumplimiento de convenciones.

INSTRUCCIONES IMPORTANTES

- Evalúa únicamente problemas reales observables
- No inventes hallazgos hipotéticos
- Enumera cada observación de forma independiente
- Sé técnico, concreto y objetivo
- Considera que se trata de una revisión post-merge

Valida especialmente:

- Estructura de carpetas
- Existencia y nomenclatura de archivos
- Consistencia UML
- Coherencia entre diagramas y escenarios
- Correctitud de documentación IA
- Uso correcto de formato Markdown
- Actualización de changelog
- Trazabilidad entre artefactos

Para cada hallazgo usa EXACTAMENTE esta estructura:

==================================================

HALLAZGO #<número>

Archivo:

Tipo de problema:
(documentación | UML | nomenclatura | trazabilidad | consistencia | otro)

Severidad:
(baja | media | alta)

Explicación técnica:
Por qué representa una inconsistencia real.

Sugerencia de mejora:
Corrección concreta recomendada.

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia
[ ] Rechazar sugerencia

Justificación del revisor humano:

---
Al finalizar agrega:

RESUMEN GENERAL DE LA PR

- Qué cumple correctamente
- Riesgos detectados
- Calidad general de la entrega

VEREDICTO TÉCNICO RETROSPECTIVO

APPROVE / OBSERVACIONES POST-MERGE / REQUIERE AJUSTES DOCUMENTALES

No completes la sección "DECISIÓN DEL REVISOR HUMANO".
Debe quedar vacía para edición manual.
```
### Resultados de la IA

Voy a generar los hallazgos observables de la PR #137 basados en los archivos actuales del repositorio. A continuación los entrego.

==================================================

### HALLAZGO #1

Archivo:
- `diagramas_de_actividades.md`
- `diagramas_de_secuencias.md`

Tipo de problema:
consistencia

Severidad:
⚠️ Media

### Explicación técnica:

Los índices muestran políticas distintas: diagramas_de_actividades.md enlaza a archivos .png mientras que diagramas_de_secuencias.md enlaza a los .puml fuente. Ambos formatos (.puml y .png) existen en los directorios, pero la falta de una convención única para los índices provoca navegación inconsistente y dificulta la experiencia del lector (qué archivo abrir para ver el diagrama) así como la trazabilidad entre fuente y artefacto presentado.

### Sugerencia de mejora:

Establecer y aplicar una regla única para todos los índices. Recomendación práctica: actualizar diagramas_de_secuencias.md para enlazar a los .png (coincidiendo con diagramas_de_actividades.md) y mantener los .puml en el repositorio como fuentes; alternativamente, si se prefiere enlazar a fuentes, cambiar diagramas_de_actividades.md a .puml. Documentar la decisión en diagramasUML.md para evitar ambigüedad.

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia
[ ] Rechazar sugerencia

Justificación del revisor humano:

### HALLAZGO #2

Archivo:
- `documentador-coordinador.md`

Tipo de problema:
Trazabilidad | Documentación

Severidad:
⚠️ Media

Explicación técnica:

El documento de revisiones registra en iteraciones previas que el índice de actividades apuntaba a .puml y que la aprobación consideró ese estado; además el propio texto menciona que "Este cambio fue introducido explícitamente por PR #137 ... para que apunten a .png". Hay una mezcla de afirmaciones históricas y post-merger sin una sección que documente explícitamente la decisión final ni su justificación técnica. Esto reduce la trazabilidad (qué se aprobó vs qué quedó finalmente en el repo) y deja incertidumbre sobre la intención del cambio.

Sugerencia de mejora:

Añadir una sección "Notas Post-Merge / PR #137" en documentador-coordinador.md que describa: qué archivos se cambiaron, motivo del cambio (por ej. preferencia por imágenes para visualización), fecha/commit/autor que aplicó el cambio y el impacto en los índices. Actualizar cualquier afirmación previa que diga "apunta correctamente a .puml" para reflejar el estado actual o indicar que fue modificado tras la aprobación.

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia
[ ] Rechazar sugerencia

Justificación del revisor humano:

### HALLAZGO #3

Archivo:
- `diagramas_de_actividades.md`

Tipo de problema: Nomenclatura

Severidad:
⚠️ Baja

Explicación técnica:
Los títulos listados en el índice muestran variaciones de capitalización (ej.: "Diagrama de actividad - Registrar Turno Médico" vs "Diagrama de Actividad - Cancelar Turno"). La inconsistencia es menor pero afecta la presentación y la uniformidad del índice, y puede complicar búsquedas y generación automatizada de índices.

Sugerencia de mejora:
Normalizar la nomenclatura de las entradas del índice (ej. usar título en Title Case: "Diagrama de Actividad - Registrar Turno Médico" para todas las entradas) y aplicar la misma convención en todos los índices (diagramasUML.md, diagramas_de_actividades.md, diagramas_de_secuencias.md).

DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia
[ ] Rechazar sugerencia

Justificación del revisor humano:

### HALLAZGO #4

Archivo:
- `diagramas_de_secuencias.md`
- `05-secuencia-consultar-agenda-medica-flujo-principal-05.puml`

Tipo de problema:
Trazabilidad | Consistencia

Severidad:
⚠️ Media

### Explicación técnica:

En el índice la entrada para el diagrama 05 indica "Flujo Alterno" ("Consultar Agenda Medica 05 - Visualizar Agenda Medica 04 - Ver Agenda - Flujo Alterno"), mientras que el título interno del .puml es "Consultar Agenda Médica (Flujo Principal)". La discrepancia entre la descripción del índice y el título del diagrama confunde sobre qué flujo está representado y rompe la trazabilidad entre el escenario de caso de uso y el artefacto gráfico.

### Sugerencia de mejora:

Alinear la descripción del índice con el título del .puml: decidir si el artefacto modela el flujo principal o alterno y corregir el texto correspondiente (o renombrar el título dentro del .puml si realmente es otro flujo). Además, verificar el archivo de escenario asociado en 03-escenarios-casos-de-uso para garantizar coherencia entre escenario y diagrama.

### DECISIÓN DEL REVISOR HUMANO:

[ ] Aceptar sugerencia
[ ] Rechazar sugerencia

Justificación del revisor humano:

### RESUMEN GENERAL DE LA PR

✅ Qué cumple correctamente:

- La PR #137 aplicó el cambio técnico esperado: los archivos .png de los diagramas existen y diagramas_de_actividades.md fue actualizado para enlazarlos.
- El changelog.md registra la PR #137 con descripción clara del objetivo del cambio.
- No hay archivos faltantes: tanto .puml como .png coexisten en los directorios relevantes.

⚠️ Riesgos detectados:

- Inconsistencia entre índices (png vs puml) puede causar confusión a usuarios y herramientas automáticas (riesgo medio).
- Falta de nota post-merge en la documentación IA que explique la decisión rompe la trazabilidad de la revisión (riesgo medio).
- Pequeñas inconsistencias de nomenclatura afectan la presentación y mantención (riesgo bajo).

📊 Calidad general de la entrega:

Técnica: adecuada — los artefactos fuente y sus renders están presentes y accesibles.

Documental: correcta en registro (changelog) pero con oportunidades de mejora en trazabilidad y en documentación post-merge.