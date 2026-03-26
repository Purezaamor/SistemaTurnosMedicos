# Introducción

## Paradigma Orientado a Objetos

El paradigma orientado a objetos (POO) es un enfoque de programación que organiza el software en objetos que representan entidades del mundo real. Cada objeto contiene atributos y métodos que definen su comportamiento.

Este paradigma permite desarrollar sistemas más organizados, reutilizables y fáciles de mantener.

---

## Fundamentos de la Programacion Orientada a Objetos

### -Encapsulamiento
Permite proteger los datos de un objeto.

Ejemplo: Un paciente solo puede modificar sus datos mediante métodos.

### -Abstracción
Se enfoca en lo importante.

Ejemplo: Un turno solo necesita fecha, hora y médico.

### -Herencia
Permite reutilizar código.

Ejemplo:
Persona → Paciente / Médico

### -Polimorfismo
Un mismo método puede tener diferentes comportamientos.

---

## Requisitos del sistema

### Requisitos Funcionales

-RF1: Registrar pacientes  
-RF2: Registrar médicos  
-RF3: Solicitar turnos  
-RF4: Cancelar turnos  
-RF5: Visualizar agenda  

### Requisitos No Funcionales

-RNF1: Interfaz simple  
-RNF2: Seguridad de datos  
-RNF3: Disponibilidad  
-RNF4: Rapidez del sistema  
-RNF5: Escalabilidad  

---

## 🚩 Casos de Uso

### 📌 1. Registrar Turno Médico

**▫️Actor(es) involucrado(s):** Secretaria Valeria / Paciente.

**▫️Descripción breve:** Permite reservar un espacio de atención para un paciente con un profesional específico.

**▫️Flujo principal de eventos:**
1.	El actor selecciona la opción para crear un nuevo turno.
2.	El sistema solicita identificar al paciente y al médico.
3.	El actor elige una fecha y hora de los espacios disponibles.
4.	El sistema verifica que no existan conflictos de agenda para ese médico.
5.	El sistema confirma la reserva y registra el movimiento en el historial de cambios.

**▫️Precondiciones:** 
- El médico y el paciente deben estar registrados en el sistema.

**▫️Postcondiciones:**
- El turno queda reservado y el horario deja de estar disponible para otros.

### 📌 2. Reprogramar Turno Existente

**▫️Actor(es) involucrado(s):** Secretaria Valeria.

**▫️Descripción breve:** Cambia la fecha o el horario de una cita ya pactada a solicitud del médico o paciente.

**▫️Flujo principal de eventos:**
1.	El actor busca el turno original por nombre de paciente o fecha.
2.	El actor selecciona la función de "Reprogramar".
3.	El sistema muestra el calendario con la disponibilidad actual del profesional.
4.	El actor selecciona el nuevo horario disponible.
5.	El sistema actualiza la cita y registra el motivo del cambio en el historial.

**▫️Precondiciones:** 
-  Debe existir un turno previo asignado.

**▫️Postcondiciones:**
- El horario anterior se libera y el nuevo queda ocupado.

### 📌 3. Cancelar Turno

**▫️Actor(es) involucrado(s):** Paciente / Secretaria Valeria.

**▫️Descripción breve:** Anula una reserva de turno liberando el espacio en la agenda médica.

**▫️Flujo principal de eventos:**
1.	El actor accede a la lista de turnos programados.
2.	El actor selecciona el turno específico que desea dar de baja.
3.	El sistema solicita una confirmación de la cancelación.
4.	El actor confirma la acción.
5.	El sistema libera el espacio en la agenda y envía una notificación mínima por WhatsApp.

**▫️Precondiciones:** 
-   El turno debe estar en estado "Pendiente" o "Confirmado".

**▫️Postcondiciones:**
-  El turno cambia su estado a "Cancelado" y se libera la disponibilidad.

### 📌 4. Visualizar Agenda Médica (Día/Semana)

**▫️Actor(es) involucrado(s):**  Médico (Dr. Molina) / Secretaria Valeria.

**▫️Descripción breve:** Permite consultar la distribución de citas y espacios libres en diferentes vistas temporales.

**▫️Flujo principal de eventos:**
1.	El actor ingresa al módulo de "Agenda".
2.	El actor selecciona el filtro por profesional médico.
3.	El actor elige entre la vista diaria o vista semanal.
4.	El sistema recupera y muestra todos los turnos y bloqueos de ese período.
5.	El actor navega entre los días para verificar la carga de trabajo.

**▫️Precondiciones:** 
-   Debe haber turnos o disponibilidad cargada en el sistema.

**▫️Postcondiciones:**
-  El actor visualiza el estado actual de la agenda.

### 📌 5. Administrar Disponibilidad del Profesional

**▫️Actor(es) involucrado(s):** Médico / Secretaria Valeria.

**▫️Descripción breve:** Define los días y rangos horarios en los que el médico atiende, estableciendo la base para evitar conflictos.

**▫️Flujo principal de eventos:**
1.	El actor selecciona el perfil del profesional a configurar.
2.	El actor define los días de la semana y los bloques horarios de atención.
3.	El actor indica periodos de licencia o bloqueos específicos (ej. vacaciones).
4.	El sistema valida que los nuevos horarios no entren en conflicto con turnos ya otorgados.
5.	El sistema guarda la configuración y actualiza la oferta de turnos para los pacientes.

**▫️Precondiciones:** 
-    El profesional debe estar dado de alta.

**▫️Postcondiciones:**
-   La agenda queda configurada con los nuevos parámetros de disponibilidad.
-   ---
## Notebook de análisis

Se utilizó NotebookLM para analizar los requisitos del sistema.

🔗 [Acceder al NotebookLM](https://notebooklm.google.com/notebook/273191bd-0f6f-400f-ba99-9b9bd4cfc947)
