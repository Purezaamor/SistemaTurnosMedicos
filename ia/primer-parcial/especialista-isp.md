# Especialista ISP (Documentación de Copilot Agent Mode)

**Prompt puesto en el Chat IA:**

```texto
Por favor lee los siguientes archivos: "anexos/introduccion.md", "diagramas/01-diagrama-clases/01-boceto inicial.excalidraw" y la carpeta "herramientas-agile/tarjetas-crc" como contexto y haz lo siguiente: Identificá responsabilidades en las clases actuales del Sistema de Turnos Médicos que podrían abstraerse en interfaces cohesivas. Detectá posibles 'interfaces gordas' que obligarían a clases a implementar métodos que no usan y proponé interfaces segregadas según el principio ISP
```

**Archivos usados como contexto:**
- `anexos/introduccion.md`
- `diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw`
- `herramientas-agile/tarjetas-crc/`

**Respuesta conseguida:**

La IA encontró hallazgos principales de "interfaces gordas" en las clases Turno, Agenda y Secretaria. Propuso 11 Interfaces Segregadas:
1. `IIdentificable`, 
2. `IRegistrable`,
3. `IConEstado`, 
4. `ICancelable`, 
5. `IReprogramable`,
6. `IHistorializable`, 
7. `IGestorDisponibilidad`, 
8. `IGestorSobreturnos`,
9. `INotificable`, 
10. `IOperadorTurnos`, 
11. `IVerificadorLlegada`

**Ajustes realizados:**
La IA dio en el clavo con la respusta, de esas 11 interfaces sugeridas por Copilot reduje a 6 interfaces más representativas del dominio para evitar sobre-complicar el diseño, enfocandose en cuellos de botella identificados en Turno y Agenda, quedandome con `ICancelable`, `IReprogramable`, `IVerificadorLlegada`, `INotificable`, `IOperadorTurnos`, `IValidadorDisponibilidad`. El cual el siguiente paso fue trasladar estas propuestas de interfaces al diagrama PlantUML.