# Principio de Responsabilidad Única (SRP)

## Propósito del principio
El principio de responsabilidad única (SRP) establece que una clase debe tener una única razón para cambiar. Esto permite reducir el acoplamiento y mejorar la mantenibilidad del sistema.

## Motivación
En el sistema de turnos médicos se detectaron clases con múltiples responsabilidades.

Ejemplo:
- La clase `Turno` gestiona estado, validación y lógica de negocio.
- La clase `Agenda` administra disponibilidad y lógica de horarios.

Esto genera acoplamiento y dificulta modificaciones futuras.

## Problema detectado
Las clases concentran más de una responsabilidad, violando SRP.

## Solución propuesta
Se separan responsabilidades en clases específicas:

- `Turno`: gestión del turno
- `Agenda`: gestión de disponibilidad
- `ValidadorTurno`: validaciones
- `HistorialCambios`: registro de cambios

## Justificación técnica
La separación permite:
- menor acoplamiento
- mayor reutilización
- facilidad de testing
- mejor escalabilidad

## Prompt utilizado

Analizá el sistema de turnos médicos e identificá violaciones al principio SRP. Proponé una refactorización separando responsabilidades.


## Archivos de contexto
- anexos/introduccion.md
- diagramas
- tarjetas CRC

## Output
La IA identificó clases con múltiples responsabilidades y propuso separarlas.

## Ajustes realizados
Se adaptó la solución al dominio real del sistema.