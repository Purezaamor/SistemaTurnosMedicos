# Encapsulamiento

## Explicación del concepto

El **encapsulamiento** consiste en ocultar los detalles internos de un objeto y exponer solo lo necesario a través de una interfaz pública. Los atributos se declaran como privados (`-`) y se accede a ellos mediante métodos públicos (`+`).

**Relación con SOLID y patrones de diseño:**
- **SRP** (Responsabilidad Única): el encapsulamiento permite que cada clase gestione su propio estado.
- **OCP** (Abierto/Cerrado): el encapsulamiento protege la lógica interna, permitiendo cambios seguros.
- **Patrón Singleton**: encapsula la creación de una única instancia.
- **Patrón Facade**: encapsula la complejidad de un subsistema.

## Ejemplo en el proyecto

**Clase seleccionada:** `Turno`

**Diagrama UML:**

![Diagrama de encapsulamiento - Turno](../../../diagramas/01-diagrama-clases/capturas-pilares/poo-encapsulamiento-ejemplo-3.png)

*En este diagrama se observa la clase Turno con sus atributos privados (-) y métodos públicos (+). El encapsulamiento protege el estado interno del objeto (fecha, hora, estado) y solo permite modificarlo a través de métodos controlados como `cancelar()` o `reprogramar()`.*

## Ejemplo de código

class Turno {

- fecha: Date

- hora: Time

- estado: String

// Métodos públicos (interfaz)

- getEstado(): String {
return this.estado
}

- cancelar(): void {
if (this.estado == "CONFIRMADO") {
this.estado = "CANCELADO"
this.notificarObservadores("CANCELADO")
}
}

- reprogramar(nuevaFecha: Date): void {
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