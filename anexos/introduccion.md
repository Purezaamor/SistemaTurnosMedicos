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

- RF1: Registrar pacientes  
- RF2: Registrar médicos  
- RF3: Solicitar turnos  
- RF4: Cancelar turnos  
- RF5: Visualizar agenda  

### Requisitos No Funcionales

- RNF1: Interfaz simple  
- RNF2: Seguridad de datos  
- RNF3: Disponibilidad  
- RNF4: Rapidez del sistema  
- RNF5: Escalabilidad  

---

## Casos de uso

### Caso 1: Registrar paciente
Actor: Secretaria  

Flujo:
1-Ingresa al sistema  
2-Selecciona registrar  
3-Carga datos  
4-Confirma  
5-Sistema guarda  

Pre: Usuario logueado  
Post: Paciente registrado  

---

### Caso 2: Registrar médico
Actor: Administrador  

Flujo similar al anterior  

---

### Caso 3: Solicitar turno
Actor: Paciente  

Flujo:
1-Selecciona turno  
2-Elige médico  
3-Elige fecha  
4-Confirma  
5-Se registra  

---

### Caso 4: Cancelar turno
Actor: Secretaria  

Flujo:
1-Busca turno  
2-Cancela  
3-Confirma  
4-Sistema elimina  

---

### Caso 5: Ver agenda
Actor: Médico  

Flujo:
1-Ingresa  
2-Ve agenda  
3-Filtra  
4-Consulta  
5-Visualiza  

---

## Diseño de clases

Clases:

Persona  
-Nombre  
-Telefono  

Paciente  
-Dni  
-Obra Social  

Medico  
-Especialidad  

Turno  
-Fecha  
-Hora  
-Estado  

Relaciones:
-Paciente → Turno 
-Médico → Turno  
