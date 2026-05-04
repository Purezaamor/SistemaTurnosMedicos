# Paciente

- **Superclase:** Persona
- **Subclases:** —
- **Pensamiento del objeto:**  
  "Soy quien solicita atención médica. Conozco mi DNI, mi fecha de nacimiento y mi obra social. Soy identificado de forma inequívoca por mi DNI, lo que evita confusiones con homónimos. Sé qué turnos tengo, pero delego en la Agenda la lógica de verificar si un horario está libre."
- **Responsabilidades:**  
  — Conocer dni, fechaNacimiento, obraSocial (heredados: nombre, apellido, telefono, mail)
- **Colaboraciones:**  
  Turno, Agenda
- **Propiedad:**  
  Creado y gestionado por Secretaria

> ⚠️ Corrección de diseño: El boceto asigna a Paciente los métodos pedirTurno(), cancelarTurno() y verHorariosDisponibles(). Esto es incorrecto: un paciente es un dato del dominio, no un agente que ejecuta lógica de negocio.
