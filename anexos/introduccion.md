# Introducción

## Paradigma Orientado a Objetos

El paradigma orientado a objetos (POO) es un enfoque de programación que organiza el software en objetos que representan entidades del mundo real. Cada objeto contiene atributos y métodos que definen su comportamiento.

Este paradigma permite desarrollar sistemas más organizados, reutilizables y fáciles de mantener.

---

## Fundamentos de la Programación Orientada a Objetos

*   **Abstracción:** Consiste en identificar los aspectos esenciales de un objeto para el dominio del problema, descartando detalles irrelevantes.
    *   *Ejemplo:* En lugar de usar datos técnicos sueltos para las horas, modelamos el concepto de **"Intervalo de Tiempo"** o **"Disponibilidad"**, que captura la semántica de los bloques horarios y los solapamientos [10, 11].
*   **Encapsulamiento:** Es la ocultación de los datos internos de un objeto, exponiendo solo lo necesario a través de métodos públicos.
    *   *Ejemplo:* La clase **`Agenda`** mantiene su lista de turnos como privada. Ninguna entidad externa puede modificarla directamente; toda acción debe pasar por el método `validarDisponibilidad()` para asegurar que no existan superposiciones [4, 12].
*   **Herencia:** Permite que una clase derive de otra, heredando sus atributos y métodos.
    *   *Ejemplo:* Tanto **`Paciente`** como **`Profesional`** pueden heredar de una clase base **`Persona`**, compartiendo atributos comunes como nombre, teléfono y email, pero manteniendo sus comportamientos específicos (como la capacidad del médico de autorizar sobreturnos) [5, 13].
*   **Polimorfismo:** Es la capacidad de que un mismo método responda de formas distintas según el objeto que lo ejecute.
    *   *Ejemplo:* El método **`enviarRecordatorio()`** se comporta de forma distinta si el objeto es de tipo **WhatsApp** (mensaje corto) o **Email** (correo formal). Asimismo, el método `getDuracion()` devolverá 15 minutos para un objeto de tipo **ConsultaControl** y 30 minutos para uno de tipo **ConsultaPrimeraVez** [14, 15].


---

## Requisitos del sistema

*   **RF1 - Ciclo de vida del turno:** El sistema debe permitir el alta, reprogramación y cancelación de turnos vinculados a un profesional y un paciente específico, gestionando los estados: Programado, Presente, Atendido, Cancelado y Ausente [5, 6].
*   **RF2 - Validación de disponibilidad:** El sistema debe impedir automáticamente la superposición horaria para un mismo profesional, permitiendo únicamente la carga manual de hasta dos (2) sobreturnos autorizados.
*   **RF3 - Gestión de agenda médica:** El sistema debe permitir configurar bloqueos horarios por compromisos fijos o licencias, y proveer la apertura manual de bloques para horarios de atención variables.
*   **RF4 - Registro de arribo (Check-in):** El sistema debe capturar la hora real de llegada del paciente para calcular desviaciones respecto al horario planificado y permitir la visualización de la sala de espera en tiempo real.
*   **RF5 - Auditoría de cambios:** El sistema debe registrar de forma automática e inalterable el historial de cada modificación (usuario, fecha/hora y valor modificado) para garantizar la trazabilidad del proceso [7].

### Requisitos No Funcionales (RNF)
*   **RNF1 - Usabilidad:** La interfaz debe ser intuitiva y permitir a los usuarios operar la agenda diaria en menos de tres interacciones, minimizando la necesidad de capacitación técnica extensa [8, 9].
* **RNF2 - Usabilidad (Accesibilidad para Usuario no Técnico):** El sistema debe poseer una interfaz de usuario intuitiva y de baja carga cognitiva, permitiendo que el Dr. Molina y la secretaria realicen las operaciones de gestión de turnos en menos de tres interacciones. El diseño debe priorizar la claridad visual para eliminar la ambigüedad y el error humano derivado de los registros manuales [1, 2].

*   **RNF3 - Auditabilidad y Trazabilidad (Integridad de la Información):** El sistema debe garantizar la integridad de los datos mediante un historial de cambios inalterable. Cada modificación en el estado o programación de un turno debe registrar de forma automática al usuario responsable y la marca temporal exacta, permitiendo resolver disputas administrativas sobre cambios o cancelaciones no notificadas [3, 4].

*  **RNF4 - Integridad y Seguridad de Datos (Identificación Única):** El sistema debe asegurar la distinción inequívoca de los pacientes mediante un identificador único, evitando la mezcla de información o la asignación errónea de turnos entre pacientes con nombres idénticos (homónimos) [7, 8].
* **RNF5 - Escalabilidad y Extensibilidad (Crecimiento del Dominio):** La arquitectura del sistema debe estar diseñada para permitir la incorporación futura de nuevos profesionales médicos, especialidades y salas de consulta sin requerir una reingeniería del núcleo de gestión de turnos [3, 9, 10]. El modelo debe ser capaz de soportar el crecimiento previsto del consultorio durante el primer año [11].




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

🔗 [Acceder al NotebookLM](https://notebooklm.google.com/notebook/58bfbaaf-a9ca-48a9-b641-21619e4ec0d2)

---

## Diseño de Clases Iniciales

### Clases Identificadas
- **Persona**: Clase base con atributos `nombre` y `telefono`.
- **Paciente**: Hereda de Persona, agrega `dni` y `obraSocial`.
- **Medico**: Hereda de Persona, agrega `especialidad`.
- **Turno**: Contiene `fecha`, `hora`, `estado`, y referencias a Paciente y Medico.

### Diagrama de Clases
![Diagrama de Clases](./../../diagramas/01-diagrama-clases/01-boceto-inicial.excalidraw)

---





