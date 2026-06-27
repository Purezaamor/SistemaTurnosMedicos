# Documentación del Proceso de Inteligencia Artificial - Especialista Creacional

## 1. Prompt Utilizado
```text
Actúa como un Arquitecto de Software Experto. Necesito diseñar e implementar el patrón de diseño creacional **Factory Method** para nuestro Sistema de Turnos Médicos, resolviendo el problema de que `ControladorTurnos` e instanciaciones directas acoplan el sistema a la clase concreta `Turno`.

Para garantizar la consistencia, analiza minuciosamente los siguientes archivos de contexto de nuestro repositorio:
#file:diagramas/01-diagrama-clases/01-diagrama-clases-final.puml
#file:diagramas/01-diagrama-clases/01-solid-01-srp.puml
#file:diagramas/01-diagrama-clases/01-solid-02-ocp.puml
#file:diagramas/01-diagrama-clases/01-solid-03-lsp.puml
#file:diagramas/01-diagrama-clases/01-solid-04-isp.puml
#file:diagramas/01-diagrama-clases/01-solid-05-dip.puml

Objetivo de la tarea:
1. Generar el código PlantUML para el nuevo archivo independiente: `diagramas/01-diagrama-clases/01-patron-creacional-factory.puml`.
2. En este nuevo diagrama, muestra la abstracción `Turno` (como clase base o abstracta), sus subclases concretas (`TurnoPresencial`, `TurnoVirtual`, `Sobreturno`), la interfaz o clase abstracta `CreadorTurnos` (Fábrica) con su método virtual `crearTurno()`, y los creadores concretos (`CreadorTurnoPresencial`, `CreadorTurnoVirtual`, `CreadorSobreturno`).
3. Muestra cómo `ControladorTurnos` ahora depende de la abstracción `CreadorTurnos` y no de las clases concretas de los Turnos (aplicando DIP y OCP).
4. Todo el código debe estar en español, limpio y usar la skinparam classAttributeIconSize 0.

Por favor, genera únicamente el código PlantUML estructurado para este patrón.
```

## 2. Ajustes realizados al Output de la IA e Iteraciones
- Iteración 1: El modelo inicial propuesto por la IA generaba nombres de métodos en inglés (createTurno()). Se solicitó una corrección explícita para mantener la nomenclatura en idioma español (crearTurno()) de acuerdo a las pautas de unificación del equipo.
- Iteración 2: Se ajustó manualmente el diagrama PlantUML para incluir notas aclaratorias (note top of CreadorTurnos) con el fin de enriquecer la legibilidad visual del artefacto antes de su exportación a formato de imagen `.png`.