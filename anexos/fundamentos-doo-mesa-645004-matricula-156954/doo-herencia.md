# Herencia

## Explicación del concepto

La **herencia** permite que una clase (subclase) herede atributos y métodos de otra clase (superclase). Promueve la reutilización de código y la creación de jerarquías de clases.

**Relación con SOLID y patrones de diseño:**
- **LSP** (Sustitución de Liskov): las subclases deben poder sustituir a sus superclases.
- **OCP** (Abierto/Cerrado): la herencia permite extender el sistema sin modificar código existente.
- **Patrón Template Method**: utiliza herencia para definir el esqueleto de un algoritmo.
- **Patrón Factory Method**: las subclases deciden qué clase instanciar.

## Ejemplo en el proyecto

**Clases seleccionadas:**
- `Persona` (superclase)
- `Paciente`, `Medico`, `Secretaria` (subclases)

**Diagrama UML:**

![Diagrama de herencia - Persona](../../diagramas/01-diagrama-clases/capturas-pilares/poo-herencia-ejemplo-3.png)

*En este diagrama se observa la jerarquía de herencia: Persona como superclase con atributos comunes (nombre, apellido, teléfono, email), y Paciente, Medico y Secretaria como subclases que heredan estos atributos y agregan los suyos propios.*

## Ejemplo de código

```java
// Superclase
class Persona {
    - nombre: String
    - dni: String
    - telefono: String

    + getNombre(): String {
        return this.nombre
    }
}

// Subclase 1 (hereda de Persona)
class Paciente extends Persona {
    - obraSocial: String

    + getObraSocial(): String {
        return this.obraSocial
    }
}

// Subclase 2 (hereda de Persona)
class Medico extends Persona {
    - especialidad: String
    - matricula: String

    + getEspecialidad(): String {
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
imprimirNombre(medico)   // ✅ "Dra. Pérez"
```

## Justificación técnica

En el código, la palabra clave `extends` (o `hereda` en el pseudocódigo) indica que `Paciente` y `Medico` **heredan** de `Persona`. Esto significa que `Paciente` y `Medico` tienen automáticamente los atributos y métodos de `Persona` (`nombre`, `dni`, `telefono`, `getNombre()`). Esto demuestra la reutilización y consistencia que ofrece la herencia.