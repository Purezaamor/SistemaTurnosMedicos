# Principio de Sustitución de Liskov (LSP)

## Propósito

El principio de Sustitución de Liskov establece que los objetos de una subclase deben poder reemplazar a los objetos de su clase base sin alterar el comportamiento esperado del sistema.

## Motivación

El sistema de turnos médicos presenta una jerarquía de clases basada en Persona, de la cual derivan Paciente, Medico y Secretaria.

Es necesario garantizar que estas subclases respeten el comportamiento definido en la clase base.

## Problema detectado

Un diseño incorrecto podría llevar a que las subclases modifiquen o eliminen comportamientos esenciales, generando inconsistencias y errores en el sistema.

## Solución aplicada

Se definió una jerarquía coherente:

Persona

* Paciente
* Medico
* Secretaria

Todas las subclases mantienen los atributos y comportamientos definidos en Persona, extendiendo funcionalidad sin alterar su contrato.

## Diagrama UML

Ver archivo:

diagramas/01-diagrama-clases/01-solid-03-lsp.png

## Justificación técnica

Las subclases pueden utilizarse como instancias de Persona sin generar efectos inesperados.

Esto asegura coherencia en el diseño, favorece la reutilización de código y garantiza el cumplimiento del principio LSP.
