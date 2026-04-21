# Documentador y Coordinador de Repositorio - Actividad Obligatoria N°2

## Objetivo del rol
Coordinar la integración de entregables, revisar PRs, asegurar cumplimiento de estructura, naming, changelog y documentación asociada.

---

## Code Review 1
### PR revisada
Feature: Modelado de Diagramas de Casos de Uso - Actividad 2

### Archivos de contexto usados
- `anexos/introduccion.md`
- `diagramas/02-casos-de-uso/`
- `diagramas/diagramasUML.md`
- `changelog.md`

### Prompt utilizado
Le pedí a Copilot Agent Mode que lea `anexos/introduccion.md` y revise la PR verificando cumplimiento de los requisitos del rol Modelador de Diagramas de Casos de Uso, validando actores, relaciones, coherencia con el sistema, estructura de archivos, índices, changelog y documentación del uso de IA.

### Observaciones detectadas
- Documentación de IA incompleta
- Falta de actores en UC02


### Ajustes solicitados
- Completar sección de ajustes realizados
- Corregir actores en UC02


### Veredicto
Request Changes

---

## Code Review 2

### PR revisada
Feature: Diseñador de Tarjetas CRC - Actividad 2 (PR #XX)

### Archivos de contexto usados
- anexos/introduccion.md
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
- changelog.md
- README.md

### Prompt utilizado en Copilot Agent Mode
"Leé anexos/introduccion.md y el diagrama de clases inicial, y revisá esta Pull Request verificando si cumple con los requisitos del rol Diseñador de Tarjetas CRC en la Actividad Obligatoria N°2. Validá estructura de carpetas, archivos individuales, completitud de las tarjetas CRC, coherencia con el dominio del sistema, documentación de IA y actualización del changelog."

### Observaciones detectadas
- Las tarjetas CRC fueron documentadas dentro de `introduccion.md` en lugar de la estructura requerida.
- No existe la carpeta `herramientas-agile/tarjetas-crc/`.
- No se crearon archivos individuales por clase.
- No existe el archivo `herramientas-agile/herramientas_agile.md`.
- No existe el archivo `ia/a2/disenador-tarjetas-crc.md`.
- No se actualizó `changelog.md`.
- Faltan campos obligatorios en las tarjetas CRC (pensamiento del objeto y superclase/subclase).
- No se creó una Issue asociada a la PR.
- La descripción de la PR es incompleta.

### Ajustes solicitados
- Crear la carpeta `herramientas-agile/tarjetas-crc/`.
- Separar las tarjetas CRC en archivos individuales con naming correcto.
- Crear y actualizar `herramientas-agile/herramientas_agile.md`.
- Completar todos los campos obligatorios de cada tarjeta CRC.
- Crear `ia/a2/disenador-tarjetas-crc.md` documentando el uso de IA.
- Actualizar `changelog.md`.
- Crear una Issue asociada y vincularla a la PR.
- Completar la descripción de la PR detallando el trabajo realizado.

### Veredicto
Request Changes

## Code Review 3

### PR revisada
Feature: Desarrollador de Escenarios de Casos de Uso - Actividad 2 (PR #XX)

### Archivos de contexto usados
- anexos/introduccion.md
- changelog.md
- README.md

### Prompt utilizado en Copilot Agent Mode
"Leé anexos/introduccion.md y revisá esta Pull Request verificando si cumple con los requisitos del rol Especialista en Escenarios de Casos de Uso en la Actividad Obligatoria N°2. Validá estructura de carpetas, archivos individuales, completitud de campos obligatorios, coherencia con el sistema, documentación de IA y actualización del changelog."

### Observaciones detectadas
- Los escenarios fueron documentados dentro de `introduccion.md` en lugar de la estructura requerida.
- No existe la carpeta `diagramas/03-escenarios-casos-de-uso/`.
- No se crearon archivos individuales por escenario.
- No existe el archivo `diagramas/03-escenarios-casos-de-uso/escenarios_de_casos_de_uso.md`.
- No existe el archivo `ia/a2/especialista-escenarios.md`.
- No se actualizó `changelog.md`.
- Faltan campos obligatorios en cada escenario: ID, área, evento activador, tipo de señal, suposiciones, requerimientos, aspectos sobresalientes, prioridad y riesgo.
- No se creó una Issue asociada a la PR.
- La descripción de la PR es incompleta.

### Ajustes solicitados
- Crear la carpeta `diagramas/03-escenarios-casos-de-uso/`.
- Separar los escenarios en archivos individuales con naming correcto.
- Crear el índice `escenarios_de_casos_de_uso.md`.
- Completar todos los campos obligatorios de cada escenario.
- Crear `ia/a2/especialista-escenarios.md`.
- Actualizar `changelog.md`.
- Crear una Issue asociada y vincularla a la PR.
- Completar la descripción de la PR detallando el trabajo realizado.
- Remover los escenarios de `introduccion.md` para evitar duplicación.

### Veredicto
Request Changes

## Code Review 4
[repetir]

---

## Tareas de coordinación realizadas
- Coordinación de PRs
- Validación de estructura del repositorio
- Control de changelog.md
- Revisión de README.md
- Integración de índices