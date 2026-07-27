# Abstracción

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

![Diagrama de abstracción - Observer](../../../diagramas/01-diagrama-clases/capturas-pilares/poo-abstraccion-ejemplo-3.png)

*En este diagrama se observa la interfaz IObservador, que define el contrato `actualizar(evento)`, y sus implementaciones concretas (NotificadorEmail, NotificadorSMS, NotificadorWhatsApp). La abstracción permite que el sistema dependa de la interfaz y no de los detalles de implementación, facilitando agregar nuevos tipos de notificación sin modificar el código existente.*

### Ejemplo de código

```
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
```

### Justificación técnica

El código utiliza `IObservador` como tipo, no las clases concretas. Esto permite que `Turno` pueda notificar a cualquier objeto que implemente la interfaz, sin importar su tipo concreto. Esto es abstracción en acción: el sistema depende de la interfaz, no de los detalles.