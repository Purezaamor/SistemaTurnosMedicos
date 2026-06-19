# Arquitecto de Dominio

## Prompt utilizado con Copilot Agent Mode (Diagrama final)

Diseñar el diagrama de clases final unificado del Sistema de Turnos Médicos.

Contexto:

- Boceto inicial: diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw

- Todas las tarjetas CRC: herramientas-agile/tarjetas-crc/

- Todos los diagramas de secuencia: diagramas/05-diagramas-secuencia/

- Diagramas de clases por caso de uso:

  - diagramas/01-diagrama-clases/01-clases-registrar-turno-medico-01.puml

  - diagramas/01-diagrama-clases/04-clases-visualizar-agenda-medica-04.puml

  - diagramas/01-diagrama-clases/05-clases-administrar-disponibilidad-05.puml

Requisitos:

- Incluir todas las clases del sistema con atributos y métodos

- Relaciones UML: herencia, asociación, agregación, composición, dependencia

- Multiplicidades correctas

## Archivos de contexto referenciados

- `diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw`
- `herramientas-agile/tarjetas-crc/`
- `diagramas/05-diagramas-secuencia/`
- `diagramas/01-diagrama-clases/01-clases-registrar-turno-medico-01.puml`
- `diagramas/01-diagrama-clases/04-clases-visualizar-agenda-medica-04.puml`
- `diagramas/01-diagrama-clases/05-clases-administrar-disponibilidad-05.puml`

## Output obtenido

[Código PlantUML generado por Copilot]

## Ajustes realizados

- Se unificaron los nombres de atributos y métodos de los diagramas parciales
- Se agregó la clase Persona como superclase común
- Se aplicaron las relaciones de herencia, composición y agregación
- Se corrigieron multiplicidades
- Se agregaron interfaces INotificador e IRepositorioTurnos
- Se ajustaron los controladores para reflejar las responsabilidades reales

## Iteraciones

- Primer intento: Copilot generó un diagrama con relaciones incompletas.
- Segundo intento: Se agregaron interfaces y se completaron las relaciones.
- Versión final: Diagrama unificado con todas las clases, relaciones y multiplicidades correctas.

## Prompt utilizado para los pilares POO

Analizar el diagrama de clases final del Sistema de Turnos Médicos y extraer ejemplos de los cuatro pilares del paradigma orientado a objetos: encapsulamiento, herencia, polimorfismo y abstracción.

Para cada pilar, identificar al menos dos ejemplos concretos referenciando clases, atributos o métodos específicos.

## Output obtenido (Pilares POO)

[Acá va el output de Copilot para los pilares]

## Ajustes realizados (Pilares POO)

- Se ajustaron los ejemplos para que sean concretos y puntuales
- Se eliminaron ejemplos genéricos o poco claros

## Prompt utilizado para el Happy Path Global

Redactar un pseudocódigo para el happy path global del Sistema de Turnos Médicos que muestre el sistema funcionando de punta a punta.

Requisitos:

- Instanciar los objetos principales del sistema

- Mostrar colaboración entre clases con llamadas a métodos

- Seguir un flujo narrativo comentado

- No usar sintaxis de ningún lenguaje particular

- Incluir tabla de trazabilidad con artefactos de origen

## Output obtenido (Happy Path Global)

[Acá va el output de Copilot]

## Ajustes realizados (Happy Path Global)

- Se ajustaron los nombres de los métodos para que coincidan con el diagrama final
- Se agregaron comentarios explicativos en cada paso
- Se completó la tabla de trazabilidad
