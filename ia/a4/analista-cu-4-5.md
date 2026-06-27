# Analista Funcional de Casos de Uso 4 y 5

## Prompt utilizado con Copilot Agent Mode (CU4)

Diseñar un diagrama de clases para el caso de uso "Visualizar Agenda Médica" del Sistema de Turnos Médicos.

Contexto:

- Boceto inicial: diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw

- Diagrama de casos de uso: diagramas/02-casos-de-uso/02-caso-uso-visualizar-agenda-medica-04.puml

- Escenario: diagramas/03-escenarios-casos-de-uso/03-visualizar-agenda-medica-flujo-principal-04.md

- Diagrama de actividades: diagramas/04-diagramas-actividades/04-actividad-visualizar-agenda-medica-04.puml

- Diagrama de secuencia: diagramas/05-diagramas-secuencia/05-secuencia-consultar-agenda-medica-flujo-principal-05.puml

- Tarjetas CRC: herramientas-agile/tarjetas-crc/ (Medico, Agenda, Turno)

Requisitos:

- Nombre de clases, atributos con tipos, métodos con parámetros y retorno

- Relaciones UML: herencia, composición, asociación


## Archivos de contexto referenciados

- `diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw`
- `diagramas/02-casos-de-uso/02-caso-uso-visualizar-agenda-medica-04.puml`
- `diagramas/03-escenarios-casos-de-uso/03-visualizar-agenda-medica-flujo-principal-04.md`
- `diagramas/04-diagramas-actividades/04-actividad-visualizar-agenda-medica-04.puml`
- `diagramas/05-diagramas-secuencia/05-secuencia-consultar-agenda-medica-flujo-principal-05.puml`
- `herramientas-agile/tarjetas-crc/`

## Output obtenido

[Código PlantUML generado por Copilot]

## Ajustes realizados

- Se agregó la clase Persona con herencia para Medico y Paciente
- Se agregó composición (Agenda compone Turnos)
- Se ajustaron los nombres de los métodos para que coincidan con las tarjetas CRC
- Se agregó el tipo de retorno `List<Turno>` en `getAgenda()`

## Iteraciones

- Primer intento: Copilot generó un diagrama básico sin herencia ni composición. Se agregaron manualmente.
- Versión final: Diagrama validado con los requisitos de la consigna.

## Prompt utilizado con Copilot Agent Mode (CU5)

Diseñar un diagrama de clases para el caso de uso "Administrar Disponibilidad" del Sistema de Turnos Médicos.

Contexto:

- Boceto inicial: diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw

- Diagrama de casos de uso: diagramas/02-casos-de-uso/02-caso-uso-administrar-disponibilidad-05.puml

- Escenario: diagramas/03-escenarios-casos-de-uso/03-administrar-disponibilidad-flujo-principal-05.md

- Diagrama de actividades: diagramas/04-diagramas-actividades/04-actividad-administrar-disponibilidad-05.puml

- Diagrama de secuencia: diagramas/05-diagramas-secuencia/05-secuencia-administrar-disponibilidad-flujo-principal-04.puml

- Tarjetas CRC: herramientas-agile/tarjetas-crc/ (Secretaria, Medico, Agenda, Disponibilidad)

Requisitos:

- Nombre de clases, atributos con tipos, métodos con parámetros y retorno

- Relaciones UML: herencia, agregación, composición, asociación


## Output obtenido (CU5)

[Código PlantUML]

## Ajustes realizados (CU5)

- Se agregó la clase Persona con herencia para Secretaria y Medico
- Se agregó agregación (Agenda contiene Disponibilidad)
- Se agregó composición (Agenda compone Turnos)
- Se ajustaron las multiplicidades

## Iteraciones (CU5)

- Primer intento: Copilot no incluyó Disponibilidad ni herencia. Se agregaron manualmente.
- Versión final: Diagrama validado.

## Archivos de contexto referenciados (global)

- Todos los diagramas de la carpeta `diagramas/01-diagrama-clases/`
- Todas las tarjetas CRC de `herramientas-agile/tarjetas-crc/`
- Diagramas de secuencia de `diagramas/05-diagramas-secuencia/`

## Iteraciones globales

- Se verificó que los diagramas de CU4 y CU5 sean coherentes con las tarjetas CRC y los diagramas de secuencia de A3.
- Se aplicaron herencia, agregación, composición y asociación según correspondía.
