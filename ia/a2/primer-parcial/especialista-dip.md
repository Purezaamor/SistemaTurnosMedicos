# Especialista en Inversión de Dependencias (DIP)

## Prompt utilizado con Copilot Agent

```
Leer anexos/introduccion.md, diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw y las tarjetas CRC para identificar dependencias hacia clases concretas y proponer abstracciones.
```

## Archivos de contexto referenciados

- `anexos/introduccion.md`
- `diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw`
- `herramientas-agile/tarjetas-crc/` (todas las tarjetas CRC)

## Output obtenido

Copilot identificó las siguientes dependencias problemáticas:
- `ControladorTurnos` depende directamente de `Turno` y `Agenda` (clases concretas)
- `Notificador` depende de `CorreoService` concreto
- `Agenda` depende de `Turno` concreto

Propuso las siguientes abstracciones:
- `ITurno`
- `IAgenda`
- `INotificador`
- `IRepositorioTurnos`

## Ajustes realizados

- Se descartó la abstracción `IEspecialista` porque no aportaba valor al dominio
- Se renombró `INotificadorService` a `INotificador` por simplicidad
- Se ajustó el diagrama UML para reflejar las dependencias invertidas correctamente
- Se eliminó pseudocódigo Java que Copilot sugirió (no solicitado en la consigna)