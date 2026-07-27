# Anexo - Fundamentos del Diseño Orientado a Objetos

**Mesa N° 3 - Alejo Guerricabeitia - Matrícula 156954**

---

## Introducción

El diseño orientado a objetos (OO) se basa en cuatro pilares fundamentales que permiten construir sistemas modulares, reutilizables y fáciles de mantener: **Abstracción**, **Encapsulamiento**, **Herencia** y **Polimorfismo**.

Estos principios están estrechamente relacionados con los principios **SOLID** y los **patrones de diseño**, ya que proporcionan la base teórica sobre la cual se construyen soluciones más robustas y flexibles.

En este anexo se explica cada fundamento, se muestra un ejemplo concreto extraído del Sistema de Turnos Médicos y se justifica su aplicación técnica.

---

## Abstracción

### Explicación del concepto

La **abstracción** consiste en representar los conceptos esenciales de un dominio, ocultando los detalles de implementación. Se enfoca en **qué** hace un objeto, no en **cómo** lo hace.

En el diseño orientado a objetos, la abstracción se logra mediante:
- **Clases abstractas**: definen comportamientos comunes que serán implementados por subclases.
- **Interfaces**: establecen contratos que las clases deben cumplir.

**Relación con SOLID y patrones de diseño:**
- **SRP** (Responsabilidad Única): la abstracción permite definir responsabilidades claras.
- **OCP** (Abierto/Cerrado): las abstracciones permiten extender el sistema sin modificar código existente.
- **DIP** (Inversión de Dependencias): los módulos de alto nivel dependen de abstracciones, no de implementaciones concretas.
- **Patrón Strategy**: utiliza abstracciones para intercambiar algoritmos.
- **Patrón Observer**: utiliza interfaces para desacoplar sujetos y observadores.

### Ejemplo en el proyecto

**Clases seleccionadas:**
- `IObservador` (interfaz)
- `NotificadorEmail`, `NotificadorSMS`, `NotificadorWhatsApp` (implementaciones concretas)

**Diagrama UML:**

![Diagrama de abstracción - Observer](../../diagramas/01-diagrama-clases/capturas-pilares/poo-abstraccion-ejemplo-3.png)

*En este diagrama se observa la interfaz IObservador, que define el contrato `actualizar(evento)`, y sus implementaciones concretas (NotificadorEmail, NotificadorSMS, NotificadorWhatsApp). La abstracción permite que el sistema dependa de la interfaz y no de los detalles de implementación, facilitando agregar nuevos tipos de notificación sin modificar el código existente.*

### Ejemplo de código

// Definición de la abstracción (interfaz)
interface IObservador {
actualizar(evento: String): void
}

// Implementación concreta 1
class NotificadorEmail implementa IObservador {
actualizar(evento: String): void {
enviarEmail("paciente@mail.com", "Evento: " + evento)
}
}

// Implementación concreta 2
class NotificadorSMS implementa IObservador {
actualizar(evento: String): void {
enviarSMS("+5491123456789", "Evento: " + evento)
}
}

// Uso de la abstracción
Turno turno = new Turno()
turno.agregarObservador(new NotificadorEmail())
turno.agregarObservador(new NotificadorSMS())
turno.cambiarEstado("CANCELADO") // Ambos observadores son notificados


**Justificación técnica:**

El código utiliza `IObservador` como tipo, no las clases concretas. Esto permite que `Turno` pueda notificar a cualquier objeto que implemente la interfaz, sin importar su tipo concreto. Esto es abstracción en acción: el sistema depende de la interfaz, no de los detalles.

---

## Encapsulamiento

### Explicación del concepto

El **encapsulamiento** consiste en ocultar los detalles internos de un objeto y exponer solo lo necesario a través de una interfaz pública. Los atributos se declaran como privados (`-`) y se accede a ellos mediante métodos públicos (`+`).

**Relación con SOLID y patrones de diseño:**
- **SRP** (Responsabilidad Única): el encapsulamiento permite que cada clase gestione su propio estado.
- **OCP** (Abierto/Cerrado): el encapsulamiento protege la lógica interna, permitiendo cambios seguros.
- **Patrón Singleton**: encapsula la creación de una única instancia.
- **Patrón Facade**: encapsula la complejidad de un subsistema.

### Ejemplo en el proyecto

**Clase seleccionada:** `Turno`

**Diagrama UML:**

![Diagrama de encapsulamiento - Turno](../../diagramas/01-diagrama-clases/capturas-pilares/poo-encapsulamiento-ejemplo-3.png)

*En este diagrama se observa la clase Turno con sus atributos privados (-) y métodos públicos (+). El encapsulamiento protege el estado interno del objeto (fecha, hora, estado) y solo permite modificarlo a través de métodos controlados como `cancelar()` o `reprogramar()`.*

### Ejemplo de código

class Turno {

fecha: Date

hora: Time

estado: String

// Métodos públicos (interfaz)

getEstado(): String {
return this.estado
}

cancelar(): void {
if (this.estado == "CONFIRMADO") {
this.estado = "CANCELADO"
this.notificarObservadores("CANCELADO")
}
}

reprogramar(nuevaFecha: Date): void {
if (this.estado == "CONFIRMADO") {
this.fecha = nuevaFecha
this.notificarObservadores("REPROGRAMADO")
}
}
}

// Uso
Turno turno = new Turno("2026-06-20", "10:00", "CONFIRMADO")
turno.cancelar() // ✅ Válido, cambia el estado
// turno.estado = "CANCELADO" // ❌ Inválido, el atributo es privado

**Justificación técnica:**

El atributo `estado` es privado y solo se modifica mediante `cancelar()` y `reprogramar()`. Estos métodos validan que el turno esté en un estado válido antes de cambiarlo. Esto protege la integridad del objeto y evita estados inconsistentes.

---

## Herencia

### Explicación del concepto

La **herencia** permite que una clase (subclase) herede atributos y métodos de otra clase (superclase). Promueve la reutilización de código y la creación de jerarquías de clases.

**Relación con SOLID y patrones de diseño:**
- **LSP** (Sustitución de Liskov): las subclases deben poder sustituir a sus superclases.
- **OCP** (Abierto/Cerrado): la herencia permite extender el sistema sin modificar código existente.
- **Patrón Template Method**: utiliza herencia para definir el esqueleto de un algoritmo.
- **Patrón Factory Method**: las subclases deciden qué clase instanciar.

### Ejemplo en el proyecto

**Clases seleccionadas:**
- `Persona` (superclase)
- `Paciente`, `Medico`, `Secretaria` (subclases)

**Diagrama UML:**

![Diagrama de herencia - Persona](../../diagramas/01-diagrama-clases/capturas-pilares/poo-herencia-ejemplo-3.png)

*En este diagrama se observa la jerarquía de herencia: Persona como superclase con atributos comunes (nombre, apellido, teléfono, email), y Paciente, Medico y Secretaria como subclases que heredan estos atributos y agregan los suyos propios.*

### Ejemplo de código

// Superclase
class Persona {

nombre: String

dni: String

telefono: String

getNombre(): String {
return this.nombre
}
}

// Subclase 1
class Paciente hereda Persona {

obraSocial: String

getObraSocial(): String {
return this.obraSocial
}
}

// Subclase 2
class Medico hereda Persona {

especialidad: String

matricula: String

getEspecialidad(): String {
return this.especialidad
}
}

// Uso (polimorfismo por herencia)
function imprimirNombre(persona: Persona): void {
mostrar(persona.getNombre()) // Funciona con cualquier subtipo
}

Paciente paciente = new Paciente("Juan", "12345678", "011-1234567", "OSDE")
Medico medico = new Medico("Dra. Pérez", "87654321", "011-998877", "Cardiología", "M-001")

imprimirNombre(paciente) // ✅ "Juan"
imprimirNombre(medico) // ✅ "Dra. Pérez"

**Justificación técnica:**

`Paciente` y `Medico` heredan de `Persona`. Ambos comparten `nombre`, `dni` y `telefono`, pero cada uno agrega atributos específicos. La función `imprimirNombre()` recibe `Persona` y funciona con cualquier subclase, demostrando la reutilización y consistencia que ofrece la herencia.

---

## Polimorfismo

### Explicación del concepto

El **polimorfismo** permite que diferentes clases respondan al mismo mensaje de forma diferente. Se logra mediante:
- **Sobrescritura de métodos**: subclases implementan su propia versión de un método definido en la superclase.
- **Implementación de interfaces**: diferentes clases implementan el mismo contrato.

**Relación con SOLID y patrones de diseño:**
- **LSP** (Sustitución de Liskov): el polimorfismo permite sustituir subtipos por sus supertipos.
- **OCP** (Abierto/Cerrado): el polimorfismo permite agregar nuevas variantes sin modificar código existente.
- **Patrón Strategy**: utiliza polimorfismo para intercambiar algoritmos.
- **Patrón Observer**: utiliza polimorfismo para notificar observadores de diferentes tipos.

### Ejemplo en el proyecto

**Clases seleccionadas:**
- `IObservador` (interfaz)
- `NotificadorEmail`, `NotificadorSMS`, `NotificadorWhatsApp` (implementaciones concretas)

**Diagrama UML:**

![Diagrama de polimorfismo - Observer](../../diagramas/01-diagrama-clases/capturas-pilares/poo-polimorfismo-ejemplo-3.png)

*En este diagrama se observa cómo diferentes clases (NotificadorEmail, NotificadorSMS, NotificadorWhatsApp) implementan la misma interfaz IObservador. Cada una tiene su propia versión del método `actualizar()`, lo que permite que el sistema trate a todas como IObservador y llame al método sin conocer el tipo concreto.*

### Ejemplo de código

// Interfaz común (contrato)
interface IObservador {
actualizar(evento: String): void
}

// Implementación 1
class NotificadorEmail implementa IObservador {
actualizar(evento: String): void {
enviarEmail("paciente@mail.com", "Evento: " + evento)
}
}

// Implementación 2
class NotificadorSMS implementa IObservador {
actualizar(evento: String): void {
enviarSMS("+5491123456789", "Evento: " + evento)
}
}

// Implementación 3
class NotificadorWhatsApp implementa IObservador {
actualizar(evento: String): void {
enviarWhatsApp("+5491123456789", "Evento: " + evento)
}
}

// Uso del polimorfismo
List<IObservador> observadores = [new NotificadorEmail(), new NotificadorSMS()]

for each (obs in observadores) {
obs.actualizar("Turno registrado")
// Cada observador reacciona de forma diferente
}

**Justificación técnica:**

El bucle recorre una lista de `IObservador` y llama a `actualizar()` en cada uno. No necesita saber qué tipo concreto es cada observador. Cada implementación responde de forma diferente: email, SMS, WhatsApp. Esto es polimorfismo: el mismo mensaje (`actualizar()`) produce comportamientos distintos según el tipo concreto del objeto.

---

## Conclusión

Los cuatro fundamentos del diseño orientado a objetos (abstracción, encapsulamiento, herencia y polimorfismo) son la base de cualquier sistema bien diseñado. En el Sistema de Turnos Médicos, estos principios se aplican de forma explícita:

- **Abstracción**: a través de interfaces como `IObservador`.
- **Encapsulamiento**: protegiendo el estado interno de clases como `Turno`.
- **Herencia**: mediante jerarquías como `Persona` → `Paciente/Medico/Secretaria`.
- **Polimorfismo**: permitiendo que diferentes observadores reaccionen a eventos de forma única.

Estos fundamentos no solo hacen que el sistema sea más comprensible, sino que también facilitan su extensión y mantenimiento a largo plazo.



 
 