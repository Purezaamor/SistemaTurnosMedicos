# Polimorfismo

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

![Diagrama de polimorfismo - Observer](../../../diagramas/01-diagrama-clases/capturas-pilares/poo-polimorfismo-ejemplo-3.png)

*En este diagrama se observa cómo diferentes clases (NotificadorEmail, NotificadorSMS, NotificadorWhatsApp) implementan la misma interfaz IObservador. Cada una tiene su propia versión del método `actualizar()`, lo que permite que el sistema trate a todas como IObservador y llame al método sin conocer el tipo concreto.*

### Ejemplo de código

```
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
```

### Justificación técnica

El bucle recorre una lista de `IObservador` y llama a `actualizar()` en cada uno. No necesita saber qué tipo concreto es cada observador. Cada implementación responde de forma diferente: email, SMS, WhatsApp. Esto es polimorfismo: el mismo mensaje (`actualizar()`) produce comportamientos distintos según el tipo concreto del objeto.