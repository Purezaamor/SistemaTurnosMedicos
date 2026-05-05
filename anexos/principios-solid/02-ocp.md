# Principio Abierto/Cerrado (OCP)

## Propósito

El principio Abierto/Cerrado establece que las entidades de software deben estar abiertas para su extensión, pero cerradas para su modificación.

## Motivación

En el sistema de turnos médicos, la clase Turno inicialmente contenía lógica condicional para manejar distintos tipos de consultas (presencial, virtual, etc.). Este enfoque implicaba modificar la clase cada vez que se agregaba un nuevo tipo de turno.

Esto generaba un diseño rígido, difícil de mantener y propenso a errores.

## Problema detectado

Se identificó el uso de estructuras condicionales dentro de la clase Turno para determinar comportamientos según el tipo de consulta.

Cada nuevo tipo de turno requería modificar el código existente, violando el principio OCP.

## Solución aplicada

Se redefinió la clase Turno como abstracta y se crearon subclases específicas:

* TurnoPresencial
* TurnoVirtual
* TurnoDomicilio

Cada subclase implementa su comportamiento particular, permitiendo extender el sistema sin modificar la clase base.

## Diagrama UML

Ver archivo:

diagramas/01-diagrama-clases/01-solid-02-ocp.png

## Justificación técnica

La solución elimina la necesidad de modificar la clase Turno ante nuevos requerimientos, delegando la variabilidad a nuevas subclases.

Esto reduce el acoplamiento, mejora la mantenibilidad y permite escalar el sistema de manera controlada, cumpliendo correctamente con el principio OCP.
