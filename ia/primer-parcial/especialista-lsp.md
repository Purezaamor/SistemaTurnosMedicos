# Uso de IA - Especialista en Principio de Sustitución de Liskov (LSP)

## Prompt utilizado

```
Analizar el sistema de turnos médicos a partir de su diagrama de clases y requisitos funcionales.
Aplicar el Principio de Sustitución de Liskov (LSP) del paradigma SOLID.
Evaluar jerarquías de herencia existentes o propuestas.
Verificar que las subclases puedan sustituir a sus superclases sin alterar el comportamiento del sistema.
Detectar posibles violaciones del principio y proponer correcciones.
```

## Archivos utilizados como contexto

* anexos/introduccion.md
* diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
* herramientas-agile/tarjetas-crc/

## Análisis realizado por la IA

Se revisaron las jerarquías de clases del sistema, especialmente aquellas relacionadas con personas y roles dentro del sistema de turnos médicos.

Se evaluó si las subclases respetan el comportamiento esperado de sus clases base.

## Problemas identificados

* Posible sobrecarga de responsabilidades en subclases
* Métodos heredados que podrían no aplicar a todas las especializaciones
* Riesgo de comportamiento inesperado al sustituir superclases

## Propuesta de corrección LSP

* Mantener una jerarquía base `Persona`

* Especializaciones coherentes:

  * `Paciente`
  * `Medico`
  * `Administrativo`

* Asegurar que todas las subclases respeten el contrato de la clase base sin alterar su comportamiento

## Ajustes realizados al output de la IA

* Se eliminaron jerarquías incorrectas o forzadas
* Se redefinieron responsabilidades de cada subclase
* Se validó que no existan métodos incompatibles con LSP
* Se alineó el modelo con el dominio del sistema

## Resultado

Se garantiza el cumplimiento del principio LSP, permitiendo que cualquier subclase pueda sustituir a su clase base sin romper el funcionamiento del sistema.
