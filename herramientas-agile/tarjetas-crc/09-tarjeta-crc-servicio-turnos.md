# Tarjeta CRC — ServicioTurnos

|  |  |  |  |
|---|---|---|---|
| **Nombre de la Clase:** | ServicioTurnos | | |
| **Superclase:** | — | | |
| **Subclase:** | — | | |
| **Responsabilidades** | **Colaboradores** | **Pensamiento del objeto** | **Propiedad** |
| Validar disponibilidad para reprogramar un turno | Agenda, Turno, HistorialCambio, Medico | Coordino la consulta de disponibilidad y verifico las reglas de negocio antes de permitir una reprogramación. | agenda: Agenda |
| Reprogramar turno y registrar cambio | Agenda, Turno, HistorialCambio | Coordino la actualización del turno y registro el cambio realizado. | historialCambio: HistorialCambio |
| Autorizar sobreturno cuando corresponde | Agenda, Medico | Verifico si corresponde autorizar un sobreturno según las reglas del sistema. | notificacion: Notificacion |
| Emitir evento de reprogramación | Notificacion | Genero la notificación correspondiente una vez completada la reprogramación. | |

**Notas:** Implementar como servicio de aplicación que orquesta entidades del dominio; debe ser transaccional y registrar en `HistorialCambio` toda reprogramación.

**Fuente:** [anexos/analisis-funcional/02-caso-de-uso-reprogramar-turno.md](../../anexos/analisis-funcional/02-caso-de-uso-reprogramar-turno.md#L107-L107)
