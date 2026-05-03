# Persona

- **Superclase:** —
- **Subclases:** Paciente, Medico, Secretaria
- **Pensamiento del objeto:**  
  "Soy la representación abstracta de cualquier persona en el sistema. Conozco el nombre completo, el teléfono de contacto y el correo electrónico que me identifican. No existo por mí mismo: mis subclases me dan sentido."
- **Responsabilidades:**  
  — Conocer nombre, apellido, telefono, mail
- **Colaboraciones:**  
  — (las subclases delegan en mí para los atributos comunes)
- **Propiedad:**  
  Clase base abstracta; no se instancia directamente

> ⚠️ Corrección de diseño: El boceto define nombre/apellido/telefono/mail por separado en Paciente, Medico y Secretaria. Esto viola el principio DRY. La introducción ya propone Persona como clase base. Se unifica aquí.
