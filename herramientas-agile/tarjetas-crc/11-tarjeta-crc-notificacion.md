# Tarjeta CRC — Notificacion

|  |  |  |  |
|---|---|---|---|
| **Nombre de la Clase:** | Notificacion | | |
| **Superclase:** | — | | |
| **Subclase:** | — | | |
| **Responsabilidades** | **Colaboradores** | **Pensamiento del objeto** | **Propiedad** |
| Generar mensajes de evento para turnos | ServicioTurnos, Turno, Paciente, Medico | Conozco cómo generar y enviar mensajes de dominio (confirmaciones, cancelaciones, reprogramaciones) hacia los actores afectados usando los canales disponibles (email, SMS, en-app). | Servicio de infraestructura para la capa de aplicación; idempotente y con registro de reenvío en caso de fallo |
| Enviar notificación a un receptor | ServicioTurnos, Turno, Paciente, Medico, sistema de mensajería / mailer | | |
| Registrar intentos de envío | ServicioTurnos, Turno, Paciente, Medico, sistema de mensajería / mailer | | |
| Separar formato de mensaje de entrega física | sistema de mensajería / mailer | | |

**Notas:** Debe separarse la lógica de formato del mensaje (plantillas) de la entrega física (canales). Las notificaciones deben ser auditables y respetar la política de reintentos.

**Fuente:** [anexos/analisis-funcional/03-caso-de-uso-cancelar-turno.md](../../anexos/analisis-funcional/03-caso-de-uso-cancelar-turno.md#L108-L108)
