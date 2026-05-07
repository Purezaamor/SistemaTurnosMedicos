# Uso de IA - Especialista en Principio Abierto/Cerrado (OCP)

## Prompt utilizado

```
Analizar el sistema de turnos médicos a partir de su diagrama de clases y requisitos funcionales.
Aplicar el Principio Abierto/Cerrado (OCP) del paradigma SOLID.
Identificar clases con lógica condicional que puedan reemplazarse por polimorfismo.
Proponer extensiones del sistema sin modificar código existente.
Generar mejoras en el diseño orientado a objetos del sistema de turnos médicos.
```

## Archivos utilizados como contexto

* anexos/introduccion.md
* diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
* herramientas-agile/tarjetas-crc/

## Análisis realizado por la IA

Se identificaron puntos del sistema donde existen decisiones basadas en condicionales (if/switch) relacionadas con tipos de turnos o especialidades médicas.

Se propuso reemplazar dichas estructuras por un diseño basado en polimorfismo, utilizando clases abstractas o interfaces.

## Propuesta de diseño OCP

* Crear una abstracción base: `Turno`
* Derivar implementaciones específicas:

  * `TurnoConsultaGeneral`
  * `TurnoEspecialidad`
  * `TurnoUrgencia`

Esto permite extender el sistema sin modificar la clase base.

## Ajustes realizados al output de la IA

* Se adaptaron los nombres de clases al dominio del sistema
* Se eliminaron decisiones condicionales explícitas
* Se validó consistencia con el modelo existente
* Se ajustó el nivel de abstracción para mantener claridad del dominio

## Resultado

El sistema cumple con OCP al permitir nuevas variantes de Turno sin modificar el código existente, favoreciendo extensibilidad y mantenimiento.
