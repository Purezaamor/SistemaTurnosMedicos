# Patrón de Diseño Estructural: Adapter (Adaptador)

## 1. Introducción a los Patrones Estructurales y su relación con SOLID
Los patrones estructurales se centran en cómo se combinan las clases y objetos para formar estructuras más complejas y eficientes sin perder flexibilidad. En el contexto del Sistema de Turnos Médicos del Dr. Molina, la adopción del patrón **Adapter** establece un puente limpio entre el dominio interno de la aplicación y servicios externos heterogéneos. 

Su relación con los principios SOLID es directa y fundamental:
* **Open/Closed Principle (OCP):** El sistema queda abierto a la extensión y cerrado a la modificación. Es posible incorporar nuevos proveedores de salud (obras sociales o prepagas) implementando nuevos adaptadores sin alterar las clases existentes (como `Agenda` o `Turno`).
* **Dependency Inversion Principle (DIP):** Las clases de alto nivel (`Agenda`) ya no dependen de las APIs concretas e inestables de terceros, sino de una abstracción de bajo acoplamiento (`IElegibilidadTurno`).
* **Interface Segregation Principle (ISP):** La interfaz de comunicación con el cliente se mantiene pequeña, cohesiva y específica para las necesidades de nuestro negocio (`validar()` y `obtenerMotivo()`), evitando que el sistema dependa de métodos complejos u obsoletos de los sistemas externos.
* **Single Responsibility Principle (SRP):** La responsabilidad de transformar y mapear los tipos de datos del dominio interno hacia los contratos de los sistemas externos queda encapsulada exclusivamente dentro de su respectiva clase adaptadora.

## 2. Propósito y Tipo del Patrón Seleccionado
* **Tipo:** Estructural.
* **Propósito:** Convertir la interfaz de una clase externa en otra interfaz que el cliente espera. Permite que clases con interfaces incompatibles trabajen juntas, unificando los diferentes métodos de validación de los prestadores de salud bajo un único contrato.

## 3. Motivación Detallada del Problema y la Solución
* **Problema:** El Dr. Molina requiere que el sistema valide si un turno médico es elegible para cobertura por parte de la Obra Social o Prepaga del paciente antes de consolidar el registro. Sin embargo, entidades como OSDE, Galeno o Swiss Medical exigen formatos de datos completamente heterogéneos, protocolos de comunicación específicos y nomenclaturas de métodos disímiles (ej. `verificarAfiliado()`, `validarPrestacion()`, etc.). Acoplar la clase `Agenda` a cada una de estas APIs externas provocaría una alta fragilidad en el código y violaría las bases del diseño orientado a objetos.
* **Solución:** Se introduce la interfaz `IElegibilidadTurno` que estandariza la operación dentro de nuestro dominio. Las clases `AdapterOSDE` y `AdapterSwissMedical` implementan esta interfaz y actúan como traductores, encapsulando las instancias de los servicios externos nativos (`ServicioValidacionOSDE` y `ServicioValidacionSwissMedical`) y mapeando sus respuestas al formato booleano uniforme que el sistema requiere.

## 4. Estructura de Clases con Diagrama UML
![Diagrama del Patrón Estructural Adapter](../../diagramas/01-diagrama-clases/01-patron-estructural-adapter.png)

## 5. Justificación Técnica de la Solución Proposed
La arquitectura propuesta garantiza el aislamiento absoluto del núcleo del negocio. Si un proveedor externo cambia los parámetros de su API o si se decide dar de baja una obra social, el impacto del cambio se reduce exclusivamente a su clase adaptadora correspondiente. La lógica de asignación y registro de turnos dentro de `Agenda` permanece inalterada, estable y segura frente a fallos externos de red o cambios de contratos en plataformas de terceros.