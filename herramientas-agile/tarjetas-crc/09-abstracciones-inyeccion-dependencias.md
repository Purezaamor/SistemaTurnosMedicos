# Abstracciones e Inyeccion de Dependencias

## Objetivo

Reducir acoplamiento entre clases concretas del sistema de turnos medicos, manteniendo la coherencia del dominio (agenda, disponibilidad, sobreturnos, check-in y auditoria).

## Dependencias concretas detectadas

- Agenda <-> Turno (dependencia mutua de comportamiento).
- Agenda -> Disponibilidad concreta.
- Servicios de turnos -> HistorialCambios concreto.
- Casos de uso -> mecanismo de notificacion concreto.
- Uso de conceptos vagos como Sistema y Usuario en tarjetas de historial.

## Abstracciones propuestas

- RepositorioTurnos: persistencia y consulta de turnos.
- RepositorioAgenda: persistencia y consulta de agenda por medico.
- PoliticaDisponibilidad: validacion de superposicion y reglas de agenda.
- AutorizadorSobreturno: validacion de autorizacion y limite de sobreturnos.
- RegistroAuditoria: registro inalterable de eventos de cambio.
- NotificadorPaciente: envio de notificaciones (por ejemplo WhatsApp).
- RelojSistema: marca temporal desacoplada y testeable.
- ActorSistema: identidad del usuario operativo que ejecuta acciones.

## Donde aplicar inyeccion de dependencias

- ServicioGestionTurnos:
  - inyectar RepositorioAgenda
  - inyectar RepositorioTurnos
  - inyectar PoliticaDisponibilidad
  - inyectar RegistroAuditoria
  - inyectar RelojSistema

- ServicioDisponibilidad:
  - inyectar RepositorioAgenda
  - inyectar PoliticaDisponibilidad
  - inyectar RegistroAuditoria

- ServicioNotificaciones:
  - inyectar NotificadorPaciente

La entidad Agenda conserva reglas de negocio y no depende de infraestructura.
La entidad Turno conserva su ciclo de vida y no depende de almacenamiento ni transporte.

## Abstracciones descartadas por no corresponder al dominio

- IPaciente, IMedico, ISecretaria: no aportan variacion de negocio real; son entidades del dominio.
- IAgenda (como reemplazo de la entidad): no se justifica en el MVP con una unica agenda por profesional.
- Interfaces de vista o presentacion en dominio (por ejemplo vistaActual): corresponde a UI, no a modelo de negocio.

## Ajustes de nomenclatura recomendados

- Mantener Medico como termino unico en todo el proyecto (evitar mezcla con Profesional).
- Mantener Secretaria como subclase de Persona para identidad de dominio.
- Separar UsuarioSistema como concepto de seguridad/aplicacion cuando se necesiten credenciales y roles tecnicos.

## Resultado esperado

- Menor acoplamiento entre capa de aplicacion y entidades.
- Mejor testabilidad de reglas de disponibilidad y auditoria.
- Mejor extensibilidad para nuevos canales de notificacion y nuevos mecanismos de persistencia.
- Coherencia con RF2 (disponibilidad y sobreturnos) y RF5/RNF3 (trazabilidad y auditoria).
