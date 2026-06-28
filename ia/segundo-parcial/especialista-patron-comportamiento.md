# Especialista en Patrón de Diseño de Comportamiento

## Prompt utilizado con Copilot Agent Mode
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

## Archivos de contexto referenciados

- `diagramas/01-diagrama-clases/06-clases-diagrama-final.puml`
- `diagramas/01-diagrama-clases/01-solid-01-srp.puml`
- `diagramas/01-diagrama-clases/01-solid-02-ocp.puml`
- `diagramas/01-diagrama-clases/01-solid-03-lsp.puml`
- `diagramas/01-diagrama-clases/01-solid-04-isp.puml`
- `diagramas/01-diagrama-clases/01-solid-05-dip.puml`

## Output obtenido

[Código PlantUML generado por Copilot]

El output inicial incluía una relación directa entre Turno y cada notificador. Se ajustó para que la relación sea a través de la interfaz IObservador.

## Ajustes realizados

- Se cambió la relación de Turno a cada observador concreto por una asociación a la interfaz.
- Se agregó la clase base Observable para reutilizar la lógica de gestión de observadores.
- Se corrigió la multiplicidad (uno a muchos) entre Turno y observadores.

## Iteraciones

- Primer intento: Copilot generó un diagrama con acoplamiento directo entre Turno y los notificadores. Se corrigió para que dependa de la interfaz.
- Segundo intento: Se agregó la clase Observable para cumplir con DIP y OCP.
- Versión final: Diagrama validado y consistente con los principios SOLID.