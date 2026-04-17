# Introducción

## Paradigma Orientado a Objetos

El paradigma orientado a objetos (POO) es un enfoque de programación que organiza el software en objetos que representan entidades del mundo real. Cada objeto contiene atributos y métodos que definen su comportamiento.

Este paradigma permite desarrollar sistemas más organizados, reutilizables y fáciles de mantener.

---

## Fundamentos de la Programación Orientada a Objetos

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

*   **RF1 - Ciclo de vida del turno:** El sistema debe permitir el alta, reprogramación y cancelación de turnos vinculados a un profesional y un paciente específico, gestionando los estados: Programado, Presente, Atendido, Cancelado y Ausente [5, 6].
*   **RF2 - Validación de disponibilidad:** El sistema debe impedir automáticamente la superposición horaria para un mismo profesional, permitiendo únicamente la carga manual de hasta dos (2) sobreturnos autorizados.
*   **RF3 - Gestión de agenda médica:** El sistema debe permitir configurar bloqueos horarios por compromisos fijos o licencias, y proveer la apertura manual de bloques para horarios de atención variables.
*   **RF4 - Registro de arribo (Check-in):** El sistema debe capturar la hora real de llegada del paciente para calcular desviaciones respecto al horario planificado y permitir la visualización de la sala de espera en tiempo real.
*   **RF5 - Auditoría de cambios:** El sistema debe registrar de forma automática e inalterable el historial de cada modificación (usuario, fecha/hora y valor modificado) para garantizar la trazabilidad del proceso [7].

### Requisitos No Funcionales (RNF)
*   **RNF1 - Usabilidad:** La interfaz debe ser intuitiva y permitir a los usuarios operar la agenda diaria en menos de tres interacciones, minimizando la necesidad de capacitación técnica extensa [8, 9].
*   **RNF2 - Integridad por encapsulamiento:** La lógica de validación de turnos debe residir exclusivamente en la clase `Agenda`, asegurando que sea la única entidad con responsabilidad para manipular la colección de turnos [10, 11].
*   **RNF3 - Restricción de infraestructura:** El modelo de dominio inicial debe limitar la atención a una única sala física de consulta para simplificar la gestión del MVP [12].
*   **RNF4 - Escalabilidad:** El diseño arquitectónico debe permitir la futura incorporación de nuevos profesionales y múltiples consultorios sin requerir una reingeniería del núcleo del sistema [8].
*   **RNF5 - Plazo de entrega (MVP):** Las funcionalidades críticas de gestión y prevención de conflictos deben estar validadas y operativas para principios de julio de 2026 [12].




---

## Alcance del MVP

Esta entrega inicial se enfoca en resolver la problemática crítica de la **gestión de agenda y prevención de conflictos horarios**. 
* **Incluido:** Gestión integral de turnos (alta, baja, modificación), validación automática de disponibilidad, registro de check-in de pacientes y administración manual de sobreturnos.
* **Restricción MVP:** Se operará bajo la limitación de una única sala física de consulta y un único profesional médico para simplificar el modelo de dominio inicial [3, 5].

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

🔗 [Acceder al NotebookLM] https://notebooklm.google.com/notebook/58bfbaaf-a9ca-48a9-b641-21619e4ec0d2

---

## Diseño de Clases Iniciales

### Clases Identificadas
- **Persona**: Clase base con atributos `nombre` y `telefono`.
- **Paciente**: Hereda de Persona, agrega `dni` y `obraSocial`.
- **Medico**: Hereda de Persona, agrega `especialidad`.
- **Turno**: Contiene `fecha`, `hora`, `estado`, y referencias a Paciente y Medico.

### Diagrama de Clases
![Diagrama de Clases](./../../diagramas/01-diagrama-clases/01-boceto-inicial.png)

---

## Revisión del revisor - Diseño de Clases

**Hallazgos**
- El boceto identifica clases clave (Persona, Paciente, Medico, Turno) y herencia básica, alineado con principios de POO.
- Faltan relaciones explícitas (flechas de herencia y asociaciones) en el diagrama, lo que dificulta la comprensión visual.
- No se incluye la clase Agenda mencionada en RNF5, ni métodos para las clases.
- Atributos son básicos pero suficientes para el MVP; Turno debería tener referencias a Paciente y Medico para integridad.

**Sugerencias**
- Actualizar el diagrama para mostrar herencia (Paciente/Medico → Persona) y asociaciones (Turno con Paciente y Medico).
- Agregar clase Agenda con métodos para validar disponibilidad y gestionar turnos.
- Incluir métodos esenciales en cada clase (ej. getters/setters, validar en Turno).
- Considerar agregar clase Sala si se expande más allá del MVP.

**Decisión del revisor humano**




