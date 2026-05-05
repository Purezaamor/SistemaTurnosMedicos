Prompt utilizado con Copilot Agent:
Leer anexos/introduccion.md,
diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw y
las tarjetas CRC de herramientas-agile/tarjetas-crc/ como contexto. Identificar dependencias hacía clases concretas en el diseño actual
y proponga abstracciones (interfaces o clases abstractas) para invertirlas,
indicando dónde aplicar inyección de dependencias. Revisá críticamente el
resultado: descartá abstracciones que no correspondan al dominio, ajustá
nombres y verificá coherencia con el sistema de turnos médicos.

Archivos referenciados:
- anexos/introduccion.md
- diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw
- herramientas-agile/tarjetas-crc/

Ajustes realizados:
- Renombré ciertas interfaces para mayor coherencia con el dominio médico.
- Reemplacé la dependencia concreta por una interfaz en el módulo de asignación de turnos.
- Agregué una clase abstracta para manejo de notificaciones.