# Análisis Funcional - Caso de Uso 5: Administrar Disponibilidad

## Descripción del caso de uso y trazabilidad con requisitos funcionales

**Actor:** Secretaria

**Flujo principal:**
1. La secretaria selecciona un médico y una fecha.
2. El sistema muestra los horarios actuales.
3. La secretaria agrega o elimina horarios de disponibilidad.
4. El sistema actualiza la agenda del médico.

**Flujos alternativos:**
<<<<<<< HEAD
- Si el médico ya tiene turnos asignados:
  1. El sistema muestra un mensaje indicando que existen turnos asignados en esa franja horaria.
  2. El sistema lista los turnos afectados (paciente, fecha, hora).
  3. El sistema ofrece dos opciones: "Cancelar turnos y eliminar disponibilidad" o "Mantener turnos y no eliminar disponibilidad".
  4. Si el usuario confirma la cancelación, se cancelan los turnos afectados y se elimina la disponibilidad.
  5. Si el usuario no confirma, se cancela la operación y se mantiene la disponibilidad.
=======
- Si el médico ya tiene turnos asignados, no se puede eliminar esa disponibilidad.
>>>>>>> develop

**Trazabilidad con RFs (A1):**
- **RF5 (Administrar disponibilidad):** La secretaria puede configurar los horarios de atención de los médicos.

## Diagrama de casos de uso (A2)

![Diagrama de casos de uso - Administrar Disponibilidad](../../diagramas/02-casos-de-uso/02-caso-uso-administrar-disponibilidad-05.png)

## Diagrama de actividades (A3)

![Diagrama de actividades - Administrar Disponibilidad](../../diagramas/04-diagramas-actividades/04-actividad-administrar-disponibilidad-05.png)

## Diagrama de secuencia (A3)

![Diagrama de secuencia - Administrar Disponibilidad](../../diagramas/05-diagramas-secuencia/05-secuencia-administrar-disponibilidad-flujo-principal-04.png)

## Diagrama de clases (CU5)

![Diagrama de clases - Administrar Disponibilidad](../../diagramas/01-diagrama-clases/05-clases-administrar-disponibilidad-05.png)

## Pseudocódigo del caso de uso

Secretaria secretaria = new Secretaria("Ana", "S001")
Medico medico = new Medico("Dr. Pérez", "Cardiología", "12345")
Fecha fecha = new Fecha("2026-06-15")
horariosActuales = secretaria.consultarDisponibilidad(medico, fecha)
secretaria.registrarDisponibilidad(medico, fecha, "14:00")
mostrar("Disponibilidad actualizada correctamente")
