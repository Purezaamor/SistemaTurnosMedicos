# Uso de IA - Especialista en Principios de Extensión (OCP + LSP)

## Prompt utilizado

```
Analizar el sistema de turnos médicos a partir de su diagrama de clases y requisitos funcionales.
Aplicar los principios SOLID, específicamente OCP y LSP.
Identificar oportunidades de mejora en el diseño orientado a objetos,
proponiendo una estructura extensible y jerarquías de herencia correctas.
Generar ejemplos aplicados al dominio del sistema.
```

## Archivos utilizados como contexto

* anexos/introduccion.md
* diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw

## Output generado por la IA (fragmento)

* Sugerencia de abstracción de la clase Turno
* Identificación de subclases según tipo de consulta
* Propuesta de jerarquía Persona con especializaciones

## Ajustes realizados al resultado de la IA

* Se adaptaron los nombres de clases al dominio del sistema
* Se ajustaron responsabilidades para evitar solapamientos
* Se validó la coherencia entre clases del modelo existente
* Se integraron las soluciones propuestas con el diseño previamente definido

## Iteraciones realizadas

* Iteración 1: generación inicial con errores de modelado
* Iteración 2: corrección de jerarquías y responsabilidades
* Iteración 3: refinamiento del modelo y validación final según consigna

## Resultado final

Se logró aplicar correctamente:

* OCP mediante la extensión de la clase Turno sin modificar su estructura base
* LSP mediante una jerarquía consistente basada en Persona

Cumpliendo con los principios de diseño orientado a objetos requeridos en la actividad.
