# Especialista en Patrón de Diseño de Comportamiento

## Prompt utilizado con Copilot Agent Mode

```
Diseñar un diagrama de clases que implemente el patrón Observer para manejar notificaciones en el Sistema de Turnos Médicos.

Contexto:

- diagramas/01-diagrama-clases/06-clases-diagrama-final.puml

- diagramas/01-diagrama-clases/01-solid-01-srp.puml

- diagramas/01-diagrama-clases/01-solid-02-ocp.puml

- diagramas/01-diagrama-clases/01-solid-03-lsp.puml

- diagramas/01-diagrama-clases/01-solid-04-isp.puml

- diagramas/01-diagrama-clases/01-solid-05-dip.puml

Problema:
Cuando un turno cambia de estado (creado, cancelado, reprogramado), el sistema debe notificar a múltiples canales (email, SMS, WhatsApp). Actualmente esta lógica está acoplada en la clase Turno.

Solución propuesta:
Aplicar patrón Observer.

- Crear interfaz IObservador con método actualizar(evento)

- Crear clase base Observable con lista de observadores y métodos para agregar/remover/notificar

- Turno hereda de Observable

- Crear observadores concretos: NotificadorEmail, NotificadorSMS, NotificadorWhatsApp

Requisitos:

- Relaciones UML correctas (herencia, implementación de interfaces, asociación)

- Nombres claros y coherentes con el dominio

```

## Archivos de contexto referenciados

- `diagramas/01-diagrama-clases/06-clases-diagrama-final.puml`
- `diagramas/01-diagrama-clases/01-solid-01-srp.puml`
- `diagramas/01-diagrama-clases/01-solid-02-ocp.puml`
- `diagramas/01-diagrama-clases/01-solid-03-lsp.puml`
- `diagramas/01-diagrama-clases/01-solid-04-isp.puml`
- `diagramas/01-diagrama-clases/01-solid-05-dip.puml`

### Output obtenido
El primer resultado generado incluía un diseño donde Turno mantenía una relación directa con cada notificador concreto. Esto fue identificado como un acoplamiento indebido respecto del patrón Observer.

Además, en esta primera versión no se había contemplado aún la estructura del documento en formato .md ni la integración del contenido del anexo textual, ya que el foco inicial estuvo exclusivamente en la generación del diagrama PlantUML.

### Ajustes realizados
Se reemplazó la dependencia directa de Turno hacia los notificadores concretos por una dependencia a la interfaz IObservador, reduciendo el acoplamiento.
Se incorporó la clase base Observable para centralizar la gestión de suscriptores y favorecer la reutilización.
Se corrigió la cardinalidad de la relación entre Turno y los observadores, estableciendo correctamente una relación uno-a-muchos.
Se revisó y ajustó el contenido del anexo textual en el documento .md para que reflejara fielmente el diseño final del diagrama.
Se generó y estructuró el documento principal en formato Markdown, integrando tanto el diagrama PlantUML como su explicación asociada, asegurando coherencia entre artefactos.

### Iteraciones
Primera iteración: Copilot generó un diagrama con acoplamiento directo entre Turno y los notificadores concretos. Se identificó la necesidad de refactorizar hacia una abstracción mediante la interfaz IObservador.
Segunda iteración: Se incorporó la clase Observable para encapsular la lógica de suscripción y notificación, alineando el diseño con DIP y OCP.
Tercera iteración: Se generó el documento .md completo, integrando el diagrama final con su descripción y corrigiendo inconsistencias entre el modelo y el anexo textual.
Versión final: Se validó la coherencia entre el diagrama PlantUML, el contenido del Markdown y el anexo, asegurando consistencia del artefacto de entrega.