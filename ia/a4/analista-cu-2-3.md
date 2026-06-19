# Uso de IA - Analista de Casos de Uso 2 y 3

## Prompt utilizado

```
Analizá y generá los diagramas de clases UML correspondientes a los Casos de Uso 2 y 3 del proyecto.

Contexto obligatorio a revisar antes de modelar

Utilizá como fuente de información y referencia los siguientes artefactos:

diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
Diagrama de caso de uso correspondiente ubicado en:
diagramas/02-casos-de-uso/
Escenario del caso de uso correspondiente ubicado en:
diagramas/03-escenarios-casos-de-uso/
Diagrama de actividades correspondiente ubicado en:
diagramas/04-diagramas-actividades/
Diagrama de secuencia correspondiente ubicado en:
diagramas/05-diagramas-secuencia/
Tarjetas CRC involucradas ubicadas en:
herramientas-agile/tarjetas-crc/
Objetivo

Generar un diagrama de clases UML completo para cada caso de uso analizado, asegurando consistencia entre todos los artefactos del proyecto.

Requisitos mínimos del diagrama

Cada diagrama debe incluir:

Clases identificadas a partir de los artefactos analizados.
Atributos con sus tipos de datos.
Métodos con parámetros y tipo de retorno.
Relaciones UML correctas, utilizando cuando corresponda:
Asociación
Agregación
Composición
Dependencia
Herencia
Multiplicidades en las relaciones cuando sean necesarias.
Coherencia con:
Tarjetas CRC
Diagramas de secuencia
Diagramas de actividades
Casos de uso y escenarios
Criterios de consistencia
Los nombres de clases deben reflejar las responsabilidades definidas en las tarjetas CRC.
Los atributos deben surgir de la información persistente o de estado identificada en los escenarios.
Los métodos deben derivarse principalmente de los mensajes intercambiados en los diagramas de secuencia.
Evitar clases redundantes o sin responsabilidades claras.
Mantener una separación adecuada entre clases de interfaz, control y entidad cuando corresponda.
Respetar las convenciones UML y las buenas prácticas de diseño orientado a objetos.
Archivos a generar

Para cada caso de uso:

Crear el archivo PlantUML:
diagramas/01-diagrama-clases/02-clases-[nombre-caso-uso]-02.puml
diagramas/01-diagrama-clases/03-clases-[nombre-caso-uso]-03.puml
Generar también la imagen PNG correspondiente.
Entregable esperado
Explicar brevemente las clases identificadas y la justificación de cada una.
Mostrar el código PlantUML completo.
Verificar que todas las clases, atributos, métodos y relaciones sean consistentes con los diagramas de secuencia y las tarjetas CRC.
Generar los archivos .puml y .png en la ubicación indicada.

Antes de crear el diagrama, realizar un análisis de los artefactos para identificar entidades, controladores, interfaces y relaciones relevantes. No inventar clases o métodos que no estén respaldados por la documentación existente.
```

## Archivos utilizados como contexto

**Tarjetas CRC (A2) - Responsabilidades y colaboraciones:**
- [herramientas-agile/tarjetas-crc/01-tarjeta-crc-persona.md](../../herramientas-agile/tarjetas-crc/01-tarjeta-crc-persona.md) — Clase base Persona
- [herramientas-agile/tarjetas-crc/02-tarjeta-crc-paciente.md](../../herramientas-agile/tarjetas-crc/02-tarjeta-crc-paciente.md) — Actor principal
- [herramientas-agile/tarjetas-crc/03-tarjeta-crc-medico.md](../../herramientas-agile/tarjetas-crc/03-tarjeta-crc-medico.md) — Proveedor de disponibilidad
- [herramientas-agile/tarjetas-crc/04-tarjeta-crc-turno.md](../../herramientas-agile/tarjetas-crc/04-tarjeta-crc-turno.md) — Entidad central del ciclo de vida
- [herramientas-agile/tarjetas-crc/05-tarjeta-crc-agenda.md](../../herramientas-agile/tarjetas-crc/05-tarjeta-crc-agenda.md) — Gestor de disponibilidad y sobreturnos
- [herramientas-agile/tarjetas-crc/07-tarjeta-crc-secretaria.md](../../herramientas-agile/tarjetas-crc/07-tarjeta-crc-secretaria.md) — Procesadora de operaciones

**Diagramas de Secuencia (A3) - Participantes y mensajes:**
- [diagramas/05-diagramas-secuencia/05-secuencia-reprogramar-turno-flujo-principal-02.puml](../../diagramas/05-diagramas-secuencia/05-secuencia-reprogramar-turno-flujo-principal-02.puml) — UC2 con 7 participantes, 33 pasos
- [diagramas/05-diagramas-secuencia/05-secuencia-cancelar-turno-flujo-principal-03.puml](../../diagramas/05-diagramas-secuencia/05-secuencia-cancelar-turno-flujo-principal-03.puml) — UC3 con objeto temporal Notificacion

**Diagramas de Actividades (A3) - Decisiones y swimlanes:**
- [diagramas/04-diagramas-actividades/04-actividad-reprogramar-turno-existente-02.puml](../../diagramas/04-diagramas-actividades/04-actividad-reprogramar-turno-existente-02.puml) — UC2
- [diagramas/04-diagramas-actividades/04-actividad-cancelar-turno-03.puml](../../diagramas/04-diagramas-actividades/04-actividad-cancelar-turno-03.puml) — UC3

**Escenarios de Casos de Uso (A1) - Flujos principales:**
- [diagramas/03-escenarios-casos-de-uso/03-reprogramar-turno-flujo-principal-01.md](../../diagramas/03-escenarios-casos-de-uso/03-reprogramar-turno-flujo-principal-01.md) — 5 pasos UC2
- [diagramas/03-escenarios-casos-de-uso/03-cancelar-turno-flujo-principal-01.md](../../diagramas/03-escenarios-casos-de-uso/03-cancelar-turno-flujo-principal-01.md) — 6 pasos UC3

## Ajustes realizados al output de la IA

Corrección y refinamiento de diagramas de clases generados por IA: se ajustaron relaciones UML (composición, asociaciones y dependencias), se eliminaron duplicaciones entre atributos y asociaciones, se revisaron responsabilidades de clases de interfaz y servicio, y se alinearon atributos y métodos con los casos de uso, diagramas de secuencia y tarjetas CRC.