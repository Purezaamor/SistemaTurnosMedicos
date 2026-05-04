# Documentador y Coordinador - Actividad Obligatoria N°2

## Descripción del Rol

El rol de **Documentador y Coordinador** tiene como objetivo garantizar la correcta organización del repositorio, la documentación del trabajo realizado por cada integrante y la trazabilidad de las decisiones mediante el uso de GitHub.

---

## Code Review 1

### PR revisada
Feature: Modelador de Casos de Uso - Actividad 2

### Archivos de contexto usados
- anexos/introduccion.md
- README.md

### Prompt utilizado en Copilot Agent Mode

```text
Leé anexos/introduccion.md y revisá la Pull Request verificando si los casos de uso cumplen con los requisitos funcionales definidos en la Actividad 1.
```

### Observaciones detectadas
- La documentación del uso de IA no estaba completa (faltaba incluir prompt y contexto).
- En el caso de uso UC02 no se encontraban correctamente definidos los actores secundarios.

### Ajustes solicitados
- Completar documentación de IA.
- Corregir la definición de actores en UC02.

### Veredicto
Request Changes

---

## Code Review 2

### PR revisada
Feature: Diseñador de Tarjetas CRC - Actividad 2 (PR #51)

### Archivos de contexto usados
- anexos/introduccion.md
- changelog.md

### Prompt utilizado en Copilot Agent Mode

```text
Revisá las tarjetas CRC verificando estructura, responsabilidades, colaboradores y cumplimiento de la consigna.
```

### Observaciones detectadas
- Las tarjetas CRC estaban embebidas en introduccion.md.
- No existía la estructura de carpetas requerida.
- No se documentó el uso de IA.
- No se actualizó el changelog.

### Ajustes solicitados
- Crear carpeta `herramientas-agile/tarjetas-crc/`.
- Separar tarjetas en archivos individuales.
- Documentar IA.
- Actualizar changelog.

### Veredicto
Request Changes

---

## Code Review 3

### PR revisada
Feature: Desarrollador de Escenarios de Casos de Uso - Actividad 2 (PR #50)

### Archivos de contexto usados
- anexos/introduccion.md
- changelog.md

### Prompt utilizado en Copilot Agent Mode

```text
Validá los escenarios de casos de uso verificando estructura, completitud y coherencia con el sistema.
```

### Observaciones detectadas
- Los escenarios estaban dentro de introduccion.md.
- No existían archivos individuales.
- Faltaban múltiples campos obligatorios.
- No se documentó el uso de IA.
- No se actualizó el changelog.

### Ajustes solicitados
- Crear carpeta de escenarios.
- Separar escenarios en archivos.
- Completar todos los campos requeridos.
- Documentar IA.
- Actualizar changelog.

### Veredicto
Request Changes

---

## Code Review 4

### PR revisada
Feature: Modelador de Diagramas de Casos de Uso - Actividad 2 (PR #20)

### Archivos de contexto usados
- anexos/introduccion.md
- diagramas/02-casos-de-uso/

### Prompt utilizado en Copilot Agent Mode

```text
Revisá los diagramas de casos de uso validando coherencia, actores y sintaxis UML.
```

### Observaciones detectadas
- En el archivo `diagramas/02-casos-de-uso/02-caso-uso-reprogramar-turno-existente-02.puml` se identificó el uso de asociaciones entre actores y casos de uso que requerían validación de sintaxis UML.
- Se solicitó verificar que el diagrama renderice correctamente y que la imagen `.png` correspondiente refleje fielmente el contenido del archivo `.puml`.

### Ajustes solicitados
- Revisar y corregir, si corresponde, las asociaciones entre actores y casos de uso en `diagramas/02-casos-de-uso/02-caso-uso-reprogramar-turno-existente-02.puml`, asegurando el uso consistente de la notación UML (líneas `--` o flechas `-->` según el criterio adoptado en el resto de los diagramas).
- Regenerar el archivo `diagramas/02-casos-de-uso/02-caso-uso-reprogramar-turno-existente-02.png` a partir del `.puml` actualizado.
- Verificar que el `.png` coincida exactamente con el contenido del `.puml` (sin diferencias de render ni elementos desactualizados).

### Veredicto
Request Changes

---

## Code Review 5 (Auto-review)

### PR revisada
feature/doc-coord-repo-update-readme-md-a2

### Archivos de contexto usados
- README.md
- changelog.md
- ia/a2/documentador-coordinador.md

### Prompt utilizado en Copilot Agent Mode

```text
Revisá la coherencia entre README, changelog y documentación del rol Documentador y Coordinador.
```

### Observaciones detectadas
- Se verificó en `README.md` que el integrante Alejo Guerricabeitia figura en dos filas debido a la asignación de dos roles (Diseñador de Tarjetas CRC y Especialista en Escenarios), lo cual responde a una contingencia del equipo.
- Se detectaron enlaces en `README.md` hacia archivos aún no integrados en la rama (por ejemplo: `diagramas/diagramasUML.md` y `herramientas-agile/herramientas_agile.md`).
- Se identificaron placeholders sin resolver en `ia/a2/documentador-coordinador.md`, que luego fueron reemplazados por los números reales de PR.

### Ajustes realizados
- Se documentó la contingencia del equipo en `README.md` y `changelog.md`.
- Se comentaron los enlaces a archivos no existentes para evitar errores de navegación.
- Se reemplazaron los placeholders `#XX` por los números reales de PR.

### Veredicto
Approve - rama lista para integración

---

## Code Review 6

### PR revisada
Feature: Modelador de Diagramas de Casos de Uso - Update Use Case 1 (PR #20)

### Archivos de contexto usados
- diagramas/02-casos-de-uso/
- changelog.md

### Prompt utilizado en Copilot Agent Mode

```text
Revisá la PR después de correcciones verificando si ya está lista para aprobar.
```

### Observaciones detectadas
- Se verificó la existencia de 5 diagramas de casos de uso en formato `.puml` y sus respectivas imágenes `.png`.
- Los actores definidos (Paciente, Médico, Secretaría) son consistentes con los casos de uso del sistema.
- Las relaciones `<<include>>` y `<<extend>>` se aplican correctamente según los flujos principales y alternativos.
- La sintaxis PlantUML es válida y los diagramas renderizan sin errores.
- Los archivos se encuentran correctamente ubicados en `diagramas/02-casos-de-uso/` y referenciados en los índices.
- Existe documentación de IA en `ia/a2/modelador-diagramas-casos-uso.md` con prompt, contexto y ajustes realizados.
- El `changelog.md` incluye la contribución correspondiente a la PR.

### Ajustes solicitados
- Ninguno

### Veredicto
Approve

---

## Code Review 7

### PR revisada
feature/a2-tarjetas-crc

### Archivos de contexto usados
- anexos/introduccion.md
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
- herramientas-agile/tarjetas-crc/
- ia/a2/disenador-tarjetas-crc.md
- changelog.md

### Prompt utilizado en Copilot Agent Mode

```text
Analizá la PR como segunda revisión después de Request Changes previo. Validá estructura de carpetas, completitud de tarjetas CRC, existencia del índice de herramientas ágiles, documentación de IA y coherencia con el dominio del sistema.
```

### Observaciones detectadas
- Se creó la carpeta `herramientas-agile/tarjetas-crc/` y las tarjetas fueron separadas en archivos individuales.
- Las 5 tarjetas CRC incluyen los campos obligatorios.
- Existe `ia/a2/disenador-tarjetas-crc.md` con prompt, contexto y ajustes.
- Sigue faltando `herramientas-agile/herramientas_agile.md`.
- Se recomienda revisar la tarjeta `Turno` para explicitar referencias a paciente y médico.
- Se recomienda revisar la representación de auditoría/historial en el diseño CRC.

### Ajustes solicitados
- Crear `herramientas-agile/herramientas_agile.md`.
- Ajustar la tarjeta `Turno` para explicitar referencias del dominio.
- Revisar cómo se modela la responsabilidad de auditoría/historial.

### Veredicto
Request Changes

---

## Code Review 8

### PR revisada
feature/a2-tarjetas-crc

### Archivos de contexto usados
- anexos/introduccion.md
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
- herramientas-agile/tarjetas-crc/
- herramientas-agile/herramientas_agile.md
- ia/a2/disenador-tarjetas-crc.md
- changelog.md

### Prompt utilizado en Copilot Agent Mode

```text
Analizá la PR como revisión de seguimiento después de Request Changes previos. Validá si se corrigió la estructura requerida, la coherencia de dominio de la tarjeta Turno, la representación de auditoría/historial y la documentación asociada.
```

### Observaciones detectadas
- Se creó `herramientas-agile/herramientas_agile.md`.
- La tarjeta `Turno` fue actualizada para incluir referencias a paciente y médico.
- Se incorporó la tarjeta `HistorialCambios`, cubriendo la auditoría de cambios del sistema.
- El changelog fue actualizado.
- La documentación de IA requiere un ajuste menor para reflejar que el resultado final contiene 6 tarjetas CRC.

### Ajustes solicitados
- Actualizar `ia/a2/disenador-tarjetas-crc.md` para reflejar el resultado final real (6 tarjetas CRC).

### Veredicto
Approve

---

## Code Review 9

### PR revisada
feature/escenarios-cu (PR #50)

### Archivos de contexto usados
- anexos/introduccion.md
- changelog.md
- diagramas/
- ia/a2/

### Prompt utilizado en Copilot Agent Mode

```text
Analizá la PR como revisión de seguimiento después de Request Changes previos. Validá si se creó la estructura de escenarios, si existen los archivos individuales, el índice, la documentación de IA y la completitud de los campos obligatorios.
```

### Observaciones detectadas
- No existe la carpeta `diagramas/03-escenarios-casos-de-uso/`.
- No existen archivos individuales de escenarios.
- No existe `escenarios_de_casos_de_uso.md`.
- No existe `ia/a2/especialista-escenarios.md`.
- No se implementaron los campos obligatorios requeridos para cada escenario.
- El changelog refleja referencias parciales, pero no hay entregable implementado en esta rama.

### Ajustes solicitados
- Crear la estructura completa de escenarios.
- Documentar al menos 5 escenarios en archivos individuales.
- Crear el índice correspondiente.
- Crear la documentación de IA.
- Completar todos los campos obligatorios.
- Verificar coherencia entre changelog y PR.

### Veredicto
Request Changes

---

## Code Review 10

### PR revisada
feature/escenarios-cu (PR #50)

### Archivos de contexto usados
- anexos/introduccion.md
- diagramas/03-escenarios-casos-de-uso/
- diagramas/03-escenarios-casos-de-uso/escenarios_de_casos_de_uso.md
- ia/a2/especialista-escenarios.md
- changelog.md

### Prompt utilizado en Copilot Agent Mode
```text
Analizá la PR como revisión final después de Request Changes previos, validando estructura, completitud y coherencia.
```

### Observaciones detectadas
- Se creó la estructura completa de escenarios.
- Los escenarios se encuentran en archivos individuales.
- Se incorporó el índice correspondiente.
- Se documentó el uso de IA.
- Se completaron los campos obligatorios.

### Ajustes solicitados
- Ninguno

### Veredicto
Approve

---

## Code Review Final

### PR revisada
feature/doc-coord-repo-update-readme-md-a2

### Archivos de contexto usados
- README.md
- changelog.md
- ia/a2/documentador-coordinador.md

### Prompt utilizado en Copilot Agent Mode
```text
Revisá la coherencia general del proyecto desde el rol Documentador y Coordinador.
```

### Observaciones detectadas
- Se corrigieron inconsistencias en README.
- Se documentaron correctamente las revisiones.
- Se validó coherencia entre changelog y PRs.

### Ajustes realizados
- Ajustes finales en documentación.
- Validación de trazabilidad.

### Veredicto
Approve

---

## Tareas de coordinación realizadas
- Coordinación de PRs
- Validación de estructura del repositorio
- Control de changelog.md
- Revisión de README.md
- Integración de índices
